# True to show the video with the intermediate results
SHOW_VIDEO = True

# True to upload the video + intermediate results to next hop 
UPLOAD_DATA = True

# True if you want to save the rendered results into video files 
SAVE_VIDEO = False 

# The next hop's address (if you want upload the data)
SERVER_ADDR = 'localhost:50053'

# The number of cached frames (and metadata) 
QUEUE_SIZE = 64

# The list of videos as the input for the replay
VIDEO_LIST = ['data/v1.avi']

# The intermediate results (generated by each main module), should be same order as the video list 
META_LIST = ['res/main_act/v1.npy']

# True if you want to view the track id in the visualization
SHOW_TRACK = True 

# FPS that the gt module replays each video 
VIDEO_READ_FPS = 15

# FPS that we will use to save the result frames to video files  
VIDEO_WRITE_FPS = 20

# The shape of the input image (width, height), Make sure it matches your video 
IMG_SHAPE = (640, 480)
