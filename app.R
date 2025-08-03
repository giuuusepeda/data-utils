library(shiny)
library(shinydashboard)
library(bslib)
library(dplyr)
library(ggplot2)
library(leaflet)
library(DT)
library(sf)
library(rnaturalearth)
library(rnaturalearthdata)

# Load data
maternal_df <- read.csv("data/maternal_mortality_clean.csv")

# Load world map for choropleth
world <- st_as_sf(rnaturalearth::ne_countries(scale = "medium", returnclass = "sf"))
world$iso_a3 <- as.character(world$iso_a3)

ui <- dashboardPage(
  dashboardHeader(title = "Maternal Mortality Dashboard"),
  dashboardSidebar(
    sidebarMenu(
      menuItem("Overview", tabName = "overview", icon = icon("info-circle")),
      menuItem("Explore by Map", tabName = "map", icon = icon("globe")),
      menuItem("Compare Regions", tabName = "compare", icon = icon("chart-bar")),
      menuItem("Full Dataset", tabName = "table", icon = icon("table"))
    )
  ),
  dashboardBody(
    
    tabItems(
      
      tabItem(tabName = "overview",
              fluidRow(
                valueBoxOutput("avg_mortality"),
                valueBoxOutput("max_country"),
                valueBoxOutput("min_country")
              ),
              fluidRow(
                box(title = "About this Dashboard", width = 12, solidHeader = TRUE, status = "primary",
                    p("This dashboard presents maternal mortality rates across countries and years using WHO data. It is designed to help explore patterns and outliers without requiring predefined questions."),
                    p("Use the map to click on a country and view its historical trend. Switch tabs to compare regional distributions or explore the full dataset with filters."),
                    p("All data comes from WHO's Global Health Observatory API, cleaned using a custom ETL pipeline.")
                )
              )
      ),
      
      tabItem(tabName = "map",
              fluidRow(
                box(width = 12, solidHeader = TRUE, status = "primary",
                    selectInput("year", "Select Year:",
                                choices = sort(unique(maternal_df$time_dim)),
                                selected = max(maternal_df$time_dim)),
                    leafletOutput("map", height = "500px"))
              ),
              fluidRow(
                box(title = "Trend for Selected Country", width = 12, solidHeader = TRUE,
                    plotOutput("trend", height = "300px"))
              )
      ),
      
      tabItem(tabName = "compare",
              fluidRow(
                box(title = "Regional Distribution", width = 12, solidHeader = TRUE,
                    plotOutput("distribution", height = "400px"))
              )
      ),
      
      tabItem(tabName = "table",
              fluidRow(
                box(title = "Maternal Mortality Dataset", width = 12, solidHeader = TRUE,
                    DTOutput("table"))
              )
      )
    )
  )
)

server <- function(input, output, session) {
  
  selected_year_data <- reactive({
    maternal_df %>% filter(time_dim == input$year)
  })
  
  output$map <- renderLeaflet({
    df <- selected_year_data()
    world_joined <- left_join(world, df, by = c("iso_a3" = "spatial_dim"))
    
    pal <- colorNumeric("YlOrRd", domain = world_joined$numeric_value)
    
    leaflet(world_joined) %>%
      addTiles() %>%
      addPolygons(fillColor = ~pal(numeric_value),
                  color = "white", weight = 1,
                  popup = ~paste0(name, ": ", round(numeric_value, 1)),
                  fillOpacity = 0.8) %>%
      addLegend(pal = pal, values = ~numeric_value,
                title = "Maternal Mortality",
                position = "bottomright")
  })
  
  selected_country <- reactiveVal(NULL)
  
  observeEvent(input$map_shape_click, {
    selected_country(input$map_shape_click$id)
  })
  
  output$trend <- renderPlot({
    req(selected_country())
    df <- maternal_df %>% filter(spatial_dim == selected_country())
    
    ggplot(df, aes(x = as.factor(time_dim), y = numeric_value)) +
      geom_line(group = 1, color = "#377eb8") +
      geom_point() +
      labs(title = paste("Trend in", selected_country()),
           x = "Year", y = "Mortality Rate") +
      theme_minimal()
  })
  
  output$distribution <- renderPlot({
    df <- selected_year_data()
    ggplot(df, aes(x = parent_location, y = numeric_value)) +
      geom_boxplot(fill = "#66c2a5") +
      labs(title = "Mortality by Region", x = "Region", y = "Mortality") +
      theme_minimal()
  })
  
  output$table <- renderDT({
    maternal_df %>%
      select(Country = spatial_dim,
             Year = time_dim,
             Mortality = numeric_value,
             Lower_Bound = low,
             Upper_Bound = high,
             Region = parent_location) %>%
      datatable(filter = "top", options = list(pageLength = 10))
  })
  
  output$avg_mortality <- renderValueBox({
    avg <- round(mean(maternal_df$numeric_value, na.rm = TRUE), 1)
    valueBox(avg, "Global Average", icon = icon("heartbeat"), color = "blue")
  })
  
  output$max_country <- renderValueBox({
    df <- maternal_df %>% filter(numeric_value == max(numeric_value, na.rm = TRUE))
    valueBox(paste0(df$spatial_dim[1], ": ", round(df$numeric_value[1], 1)),
             "Highest Mortality", icon = icon("arrow-up"), color = "red")
  })
  
  output$min_country <- renderValueBox({
    df <- maternal_df %>% filter(numeric_value == min(numeric_value, na.rm = TRUE))
    valueBox(paste0(df$spatial_dim[1], ": ", round(df$numeric_value[1], 1)),
             "Lowest Mortality", icon = icon("arrow-down"), color = "green")
  })
}

shinyApp(ui, server)
