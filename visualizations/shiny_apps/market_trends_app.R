library(shiny)
library(ggplot2)

# Carregar dados
market_data <- read.csv("processed/market_trends.csv")

# UI
ui <- fluidPage(
    titlePanel("Análise de Tendências de Mercado"),
    sidebarLayout(
        sidebarPanel(
            selectInput("variable", "Variável:", choices = colnames(market_data))
        ),
        mainPanel(
            plotOutput("trendPlot")
        )
    )
)

# Server
server <- function(input, output) {
    output$trendPlot <- renderPlot({
        ggplot(data = market_data, aes_string(x = "date", y = input$variable)) +
            geom_line() +
            labs(title = paste("Tendência de", input$variable), x = "Data", y = input$variable)
    })
}

# Run the application
shinyApp(ui = ui, server = server)
