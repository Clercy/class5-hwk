# class5-hwk

#Pseudo code  - My charting plan

1.0. Connect to dataset

1.1 Load dataset

2.0 Format the data

2.1 Add header

2.2 Create summary statistics np.mean(data), np.std(data)

3.1 Plot 1st chart (Each column separately)

3.1.1 Get data for each column (for column in data.columns)

3.1.2 Plot Histogram (matplotlib.pyplot.hist)

3.1.3 Create label for chart (plt.ylabel(column))

3.1.4 Generate files - ex:plt.plot(data[column])

3.1.5 Retrieve timestamp

3.1.6 Save file (savefig) filename: charttype + timestamp + '.png'

3.1.7 Close chart

3.1.8 Repeat for each column

3.2 Plot 2nd chart (In pairs)

3.2.1 Get data for each pair of columns (for column in data.columns)

3.2.2 Plot Scatterplot (matplotlib.pyplot.scatter)

3.2.3 Create label for chart (plt.ylabel(column))

3.2.4 Generate files - ex:plt.plot(data[column])

3.2.5 Retrieve timestamp

3.2.6 Save file (savefig) filename: charttype + timestamp + '.png'

3.2.7 Close chart

3.2.8 Repeat for each set

3.3 Plot 3rd chart (In pairs)

3.3.1 Get data for each pair of columns (for column in data.columns)

3.3.2 Plot Line Chart (matplotlib.pyplot.plot)

3.3.3 Create label for chart (plt.ylabel(column))

3.3.4 Generate files - ex:plt.plot(data[column])

3.3.5 Retrieve timestamp

3.3.6 Save file (savefig) filename: charttype + timestamp + '.png'

3.3.7 Close chart

3.3.8 Repeat for each set

4 Exit
