library(shiny)
library(ggplot2)

# Carregar dados
ad_data <- read.csv("processed/ad_campaign_efficiency.csv")

# UI
ui <- fluidPage(
    titlePanel("Eficiência da Campanha Publicitária"),
    sidebarLayout(
        sidebarPanel(
            selectInput("campaign", "Campanha:", choices = unique(ad_data$campaign_name))
        ),
        mainPanel(
            plotOutput("campaignPlot")
        )
    )
)

# Server
server <- function(input, output) {
    output$campaignPlot <- renderPlot({
        subset_data <- subset(ad_data, campaign_name == input$campaign)
        ggplot(data = subset_data, aes(x = date, y = efficiency)) +
            geom_line() +
            labs(title = paste("Eficiência da Campanha:", input$campaign), x = "Data", y = "Eficiência")
    })
}

# Run the application
shinyApp(ui = ui, server = server)
