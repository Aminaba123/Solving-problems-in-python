import tensorflow as tf 
import numpy as np 
import os


#train_dir = '/home/hrz/projects/tensorflow/My-TensorFlow-tutorials/cats_vs_dogs/data/train/'

def get_files(file_dir):


	angry = []
	label_angry = []
	happy = []
	label_happy = []
	surprised = []
	label_surprised = []
	disgusted = []
	label_disgusted = []
	fearful = []
	label_fearful = []
	sadness = []
	label_sadness = []
	for sub_file_dir in os.listdir(file_dir):
		if sub_file_dir == 'angry':
			for name in os.listdir(file_dir+'/'+sub_file_dir):
				angry.append(file_dir+'/'+sub_file_dir+'/'+name)
				label_angry.append(0)
		elif sub_file_dir == 'disgusted':
			for name in os.listdir(file_dir+'/'+sub_file_dir):
				disgusted.append(file_dir+'/'+sub_file_dir+'/'+name)
				label_disgusted.append(1)
		elif sub_file_dir == 'fearful':
			for name in os.listdir(file_dir+'/'+sub_file_dir):
				fearful.append(file_dir+'/'+sub_file_dir+'/'+name)
				label_fearful.append(2)
		elif sub_file_dir == 'happy':
			for name in os.listdir(file_dir+'/'+sub_file_dir):
				happy.append(file_dir+'/'+sub_file_dir+'/'+name)
				label_happy.append(3)
		elif sub_file_dir == 'sadness':
			for name in os.listdir(file_dir+'/'+sub_file_dir):
				sadness.append(file_dir+'/'+sub_file_dir+'/'+name)
				label_sadness.append(4)
		elif sub_file_dir == 'surprised':
			for name in os.listdir(file_dir+'/'+sub_file_dir):
				surprised.append(file_dir+'/'+sub_file_dir+'/'+name)
				label_surprised.append(5)
	print('Already!!',len(label_angry))
