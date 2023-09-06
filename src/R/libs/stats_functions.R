# Função para calcular a média móvel
moving_average <- function(data, window_size) {
  return(stats::filter(data, rep(1/window_size, window_size), sides=2))
}

# Função para realizar um teste-t de duas amostras
two_sample_t_test <- function(data1, data2) {
  test_result <- t.test(data1, data2)
  return(test_result)
}

# Função para calcular percentis
calculate_percentiles <- function(data, probs=c(0.25, 0.5, 0.75)) {
  return(quantile(data, probs=probs))
}

