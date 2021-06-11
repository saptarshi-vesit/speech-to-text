# speech-to-text

PREREQUISITES TO RUN PROGRAM:-
1)	Any version of Python 3(preferably the latest one) should be installed on the PC.
2)	To download python on your PC, click on the link https://www.python.org/downloads/ and as per the OS installed on your PC download the appropriate version on your PC.
3)	To edit the program any IDE(like pycharm, VS code, etc.) or Python IDLE would work.
4)	The python software downloaded on the PC should be compatible with the operating system of the PC.
5)	An active internet connection should be there to download the required libraries to run the program and to convert the audio file into ".wav " format.
6)	The microphone of the PC should work properly so that it can record the audio.

STEPS TO RUN PROGRAM:-
1)	Save the program file on your PC in a separate folder.
2)	Now record or select any audio file on your computer and convert it into ".wav" format by any online converter.
3)	Save the ".wav" audio file on your PC in the same folder where you have saved the program file.
4)	Open the python IDLE or the IDE installed on your PC.
5)	Open the program file.
6)	Now, there will be a command:"AUDIO_FILE=("Recording_english.wav")"
        in place of "AUDIO_FILE=("Recording_english.wav")" enter the name of your audio file.
7)	Go to the terminal and write the command "pip install speechrecognition" and press "ENTER"
8)	Wait for the library to get installed, once it is installed, run the program by clicking on the run icon.



INTRODUCTION:- 
This project shows how we can convert speech into text using a python program.
Python is an interpreted high level general purpose programming language.
The program used in this project makes use of “speechrecognition” library, the “speechrecognition” library can only convert audio files in “.wav ” format into text.

EXECUTION OF PROGRAM:-
At the beginning of the program, “speechrecognition” library is imported as “sr”.
The “.wav” file is then assigned to a variable.
The imported recognizer is the initialised using the command “sr.Recognizer()”.
The audio file is then given as a source to the recognizer using the function “.record()”.
The “.record ” function then reads the audio file.
Once the program understands the speech, it coverts it into text and prints it on the console.

APPLICATIONS:- 
1) Speech to text program could be used for typing purpose, as with help of it we can type just by dictating the words.
2) Could be used to communicate with people coming from different backgrounds.
3) It is helpfull for disabled people.


