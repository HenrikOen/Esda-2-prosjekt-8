import numpy as np
import matplotlib.pyplot as plt
import csv
import os



#Definin the file paths
filtered_signal      = "Malinger\\filtrert_signal.csv"
frekvensrespons         = "Malinger\\frekvensrespons.csv"
spectrum_noise   = "Malinger\\spectrum_noise.csv"
white_noise_scope  = "Malinger\\white_noise_scope.csv"


#Function for converting file to lists (oscilliscope):
def file_to_list(file, time_coloumn, Voltage1_column, Voltage2_column):
    Voltage1_list =[]
    Voltage2_list =[]
    time_list     = []
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            
            if len(row)==0:
                
                continue
            elif not (row[0][0].isdigit()) and not (row[0][0] == "-"):
                
                continue
                
            time_list.append(float(row[time_coloumn]))
            Voltage1_list.append(float(row[Voltage1_column]))
            Voltage2_list.append(float(row[Voltage2_column]))
            
            
            

    return  time_list, Voltage1_list, Voltage2_list

#Defining function to convert csv file to lists (Amplitude response):
def file_to_list_Response(file, freq_column, magnetude_column):
    freq_list=[]
    magnetude_list=[]
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            if len(row)==0:
                continue
            elif not (row[0][0].isdigit()):
                continue
            freq_list.append(float(row[freq_column]))
            magnetude_list.append(float(row[magnetude_column]))
            
        return freq_list, magnetude_list


filtered_signal_freq_list, filtered_signal_amplitdue, bruh = file_to_list(filtered_signal, 0, 1, 1)
white_noise_scope_time, white_noise_scope_amplitude, bruh = file_to_list(white_noise_scope, 0, 1, 1)

spectrum_noise_freq_list, spectrum_noise_amplitude_input,= file_to_list_Response(spectrum_noise, 0, 1)
spectrum_noise_freq_list, spectrum_noise_amplitude_output,= file_to_list_Response(spectrum_noise, 0, 3)
frekvensrespons_freq_list, frekvensrespons_amplitude_input = file_to_list_Response(frekvensrespons,0,1)
frekvensrespons_freq_list, frekvensrespons_amplitude_output = file_to_list_Response(frekvensrespons,0,2)






#creating folder for graphs:
folder_path = 'Graphs'
os.makedirs(folder_path, exist_ok=True)

#Plottign and saving graphs:


# plt.semilogx(freq_list, amplitude_in )


plt.plot(filtered_signal_freq_list[6000:-1], filtered_signal_amplitdue[6000:-1])
plt.title('Filteret signal')
plt.xlabel('time [s]')
plt.ylabel('Magnitude [V]')
# plt.legend(['$v_2$', '$v_1$'])
plt.grid()
print(len(filtered_signal_freq_list[3000:-1]))
plt.savefig('Graphs\ filtered_signal_scope.png')


plt.figure()
plt.plot(white_noise_scope_time[5000:-1], white_noise_scope_amplitude[5000:-1])
plt.title('White noise oscilliscope')
plt.xlabel('Time [s]')
plt.ylabel('Magnitude [V]')
# plt.legend(['$v_2$', '$v_1$'])
plt.grid()
plt.savefig('Graphs\ white_noise_scope.png')

plt.figure()
plt.semilogx(frekvensrespons_freq_list, frekvensrespons_amplitude_input)
plt.semilogx(frekvensrespons_freq_list, frekvensrespons_amplitude_output)
plt.legend(['input', 'output'])
plt.xlabel("frequency[Hz]")
plt.ylabel("amplitude[dB]")
plt.grid()
plt.savefig('Graphs\ amplituderesponse.png')



plt.figure()
plt.title('White noise spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.legend(['$v_2$', '$v_1$'])
plt.xlabel("frequency[Hz]")
plt.ylabel("amplitude[dB]")




# spectrum_noise_freq_list, spectrum_noise_amplitude_input, spectrum_noise_amplitude_output

plt.semilogx(spectrum_noise_freq_list, spectrum_noise_amplitude_input)
plt.semilogx(spectrum_noise_freq_list, spectrum_noise_amplitude_output)
plt.legend(['s(t)', 'y(t)'])
plt.xlabel("frequency[Hz]")
plt.ylabel("amplitude[dB]")
plt.savefig('Graphs\ spectrum_noise.png')

plt.show()
