The Mapper/Reducer python programs for word count have been separated by version. Any version should work locally but may require modification before running in an open source cloud environment due to environment variables and python versions.

The python file, 'WordCountTesting' contains the python command(s) that should be run in order to successfully execute:

1. 'cat word_count_data.txt' - Opens the specified text file containing the input for the mapper program
2. 'python mapper.py' - Runs the mapper python file, using text output from the previous command as its input
3. 'sort' - Sorts the output from the mapper
3. 'python reducer.py' - Runs the reducer python file, using the output from the previous step as its input
