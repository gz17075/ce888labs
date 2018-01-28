To compare the fleet datasets, the following was done:

1.The data from the vehicles.csv file was read in and its columns distributed into two lists Current_Fleet and New_Fleet.
2.New_Fleet was formatted to deal with the missing entries by deriving the data from Current_Fleet.
3.The lists length's were equalised.
4.Data lists were then created to represent the Day numbers for the fleet data.
5.Two data frame plot areas were created, one for analysing Current_Fleet against day numbers, the other for New_Fleet against day numbers.

6.The standard deviation was calculated for Current_Fleet and New_Fleet data and written to the console.

7.New_Fleet scatterplot was created
![logo](./New_Fleet_scaterplot.pdf?raw=true)
![logo](./New_Fleet_scaterplot.png?raw=true)

Current_Fleet scatterplot was created
![logo](./Current_Fleet_scaterplot.pdf?raw=true)
![logo](./Current_Fleet_scaterplot.png?raw=true)


8.The data is then converted to Numpy lists so we can use the Numpy library to create histogram plots:
![logo](./Current_Fleet_histogram.pdf?raw=true)
![logo](./Current_Fleet_histogram.png?raw=true)
![logo](./New_Fleet_histogram.pdf?raw=true)
![logo](./New_Fleet_histogram.png?raw=true)

9.The lower and upper values are calculated from the lists and linear model graphs are drawn to show this against the standard deviation:
![logo](./Current_Fleet_bootstrap_confidence.pdf?raw=true)
![logo](./Current_Fleet_bootstrap_confidence.png?raw=true)
![logo](./New_Fleet_bootstrap_confidence.pdf?raw=true)
![logo](./New_Fleet_bootstrap_confidence.png?raw=true)



