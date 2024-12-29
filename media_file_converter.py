"""
- Media File Converter
- Script that converts allows user to convert media files to others
- By Quincy Muzik 12/8/2024
"""

#API's / Modules
from moviepy import VideoFileClip

# Message Variable
welcomeMessage = "Media File Converter. SCUBA-Q Multimedia 2024. \n"
fileTypeMessage = "What type of file are you converting? (Audio or Video) \n"

# Orginal File Message Variable
videoFilePathMessage = "Please enter the name of file and its location that needs to be converted: \n"

# New File Message Variables
newFileNameMessage = "Please enter the new desired file name: \n "
newFileLocationMessage = "Please enter the location to be exported to: \n"
newFileExtensionMessage = "Please enter the desired file format extension for conversion: \n "

# While Loop Conditon Variable
repeat = True

# End of Conversion Message Varaible
endOfConversionUserResponseMessage = "Do you need to convert another file (Y or N)? \n"

# START OF EXECUTION ----------------------------------------------------------------------------------------------------

# Welcome the user to the script and its purpose
print(welcomeMessage)

# Ask the user to Provide a Video file path that needs to be converted
videoFileName = input(videoFilePathMessage)

# Insert Local Video File Path
clip = VideoFileClip(videoFileName)

# Loop for continuous execution
while repeat == True:

    # Ask the User if the file needs to be converted a video or audio file
    fileType = input(fileTypeMessage)

    # If the converted file will be audio:
    if fileType == 'Audio' or fileType == 'audio':

        # Ask the user to provide a audio file name for the finished converted file
        newFileName = input(newFileNameMessage) 

        # Ask the user to provide a file extension (.mp3, .wav, etc)
        newFileExtension = input(newFileExtensionMessage)

        # Ask the user to provide a location for the converted file
        newFileLocation = input(newFileLocationMessage)

        # Combine the previous inputs to form a new file for conversion
        newFile = newFileLocation + newFileName + newFileExtension

        # Convert the file 
        clip.audio.write_audiofile(newFile)

    # If the converted file will be video
    elif fileType == 'Video' or fileType == 'video':
        
        # Ask the user to provide a audio file name for the finished converted file
        newFileName = input(newFileNameMessage) 

        # Ask the user to provide a file extension (.mp3, .wav, etc)
        newFileExtension = input(newFileExtensionMessage)

        # Ask the user to provide a location for the converted file
        newFileLocation = input(newFileLocationMessage)

        # Combine the previous inputs to form a new file for conversion
        newFile = newFileLocation + newFileName + newFileExtension

        # Convert the file 
        clip.write_videofile(newFile)

    # Else user input cannot be understood
    else:
        print("Invalid Response, it must either be audio or video!")

    # Ask the user if they need to convert more files
    endOfConversionUserResponse = input(endOfConversionUserResponseMessage)

    # If the user does not need to convert another file
    if endOfConversionUserResponse == 'N' or endOfConversionUserResponse == 'n':
        break

    # If the user needs to convert another file
    elif endOfConversionUserResponse == 'Y' or endOfConversionUserResponse == 'y':
        # Ask the user to Provide a Video file path that needs to be converted
        videoFileName = input(videoFilePathMessage)

        # Insert Local Video File Path
        clip = VideoFileClip(videoFileName)
    
    # If the user enters anything else besides Y or N
    else:
        print("Invalid Response, it must be either Yes or No!")

# Let the User know the script has finished execution 
print("Thank you for using the Media File Converter! You can now close this window.")

# END OF EXECUTION ----------------------------------------------------------------------------------------------------- 
