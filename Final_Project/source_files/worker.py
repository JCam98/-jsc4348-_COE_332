''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    Script File Name: worker.py
        
    Description: This module contains the source code used to execute jobs
    and update job statuses.'''

# Import modules:

from jobs import q, rd_jobs, rd_temp
import jobs
import numpy, random
import matplotlib.pyplot as plt

# Define "q.worker" decorator to remove items from the queue:
 
@q.worker
def execute_job(jid):
    
    
    ''' Define function that generates a plot of time-series data for a particular
     , and randomly-generated, temperature field: '''
    
    def generate_plot():

        temp_num = rd_temp.dbsize() # Get the number of temperature dictionaries in database
        
        ''' Use the "random" module to randomly-generate a temp field to 
        develop a time-series line plot of from the list: "GALT", "GMAXLT", 
        and "GMINLT": '''
        
        temp_field_list = ["GALT (Celsius)", "GMAXLT (Celsius)", "GMINLT(Celsius)"]
        temp_field = temp_field_list[random.randint(0,2)]
        
        # Use matplolib to generate plot of time-series temperature data: 
            
        time_array = numpy.array([]) # Initialize array to store time data
        temperature_array = numpy.array([]) # Initialize array to store temperature data 
        
        # Use for loop to append values to array storing time and temperature field values:
        
        for i in range(0,temp_num ):
            
            temp_key = i # Assign keyname to temperature    
            time_array = numpy.append(time_array, i)
            temperature_array = numpy.append(temperature_array, float(rd_temp.hget(temp_key, temp_field)))
                                                                                                                                                                                                                     
                                                                                                           
        # Use "Matplotlib" to generate a line plot of the time-series dataset:                                 
                                                                                                               
        plt.plot(time_array, temperature_array)                                                                
        plt.title("Plot of "  + temp_field + " vs. Time (Months) Starting from 01/01/1930 ")                                                               
        plt.xlabel("Time (Months)")                                                                                 
        plt.ylabel(temp_field)                                                                            
        plt.savefig('/Time-Series-Line-Plot.png')                                                              
                                                                                                               
        # Open image and add to redis database containing job information:                                                               
                                                                                                               
        with open('/Time-Series-Line-Plot.png', 'rb') as f:                                                    
           img = f.read()                                                                                      
                                                                                                               
        rd_jobs.hset(f'job.{jid}', "image", img) # Set the image in redis database
                                                                                                                                                                                                                                                                                                                                                                                                      
        return_status = "Plot Generated Successfully"
    
        return return_status
    
    # Invoke "generate_plot()" method to generate and store time-series line plot: 
        
    generate_plot()
 
    # Invoke "update_job_status()" function to designate job as "complete": 
        
    jobs.update_job_status(jid, "complete")
    
    
# Invoke "execute_job()" function to perform jobs: 

execute_job()    
