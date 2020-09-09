#!/usr/bin/env python

import msgpack
from tabulate import tabulate


with open("map.msg", "rb") as my_file:
    my_byte_data = my_file.read()

my_data = msgpack.unpackb(my_byte_data)

print('\n\n')
print('------------------------------------------------------------------------------------------------------------------------------')
print('All the Level 1 keys:')
print('`````````````````````')
print(my_data.keys())

print('\n')
print('----------------------------------------------------  cameras  -------------------------------------------------------------')
keys = list(my_data['cameras'].keys())
print('Key')
print('---')
print(keys)
print('\n')

print('Value')
print('------')
print(tabulate(list(my_data['cameras'][keys[0]].items()), headers=['keys', 'values']))

print('\n')
print('----------------------------------------------------  landmarks  -------------------------------------------------------------')
print('Total', len(my_data['landmarks'].items()), 'landmarks')
print('\n')
count = 0
print('Keys\tValues')
print('----\t------')
for key,value in my_data['landmarks'].items():
	print(key, '\t', value)
	count += 1
	if count > 7:
		break
print('.')
print('.')
print('.')
print(len(my_data['landmarks'].items()), 'values available')

print('\n')
print('----------------------------------------------------  keyframes  -------------------------------------------------------------')
total_number_of_kf = len(my_data['keyframes'].items())
print('Total', total_number_of_kf, 'keyframes')
print('\n')

print('Keys (Keyframe index)')
print('---------------------')
print(my_data['keyframes'].keys())
print('\n')
print('Values (Keyframe features)')
print('--------------------------')
total_number_of_kf_features = len(list(my_data['keyframes']['0'].keys()))
print('Each Keyframe has', total_number_of_kf_features, 'different features:')
temp = 0
for k in my_data['keyframes']['0'].keys():
	print(temp, '-\t', k)
	temp += 1
print('\n')
print('(2,3,4,5,16,17 are large sized features)')
print('\n')

keyframe_number = 1

print('Detailing keyframe number ( <',len(my_data['keyframes'].items()),') :', keyframe_number)
print('-----------------------------------------')
keyframe_index = list(my_data['keyframes'].keys())[keyframe_number]
print('Keyframe index = ', keyframe_index)
print('\n')
features = list(my_data['keyframes'][keyframe_index].keys())

large_features = [2,3,4,5,16,17]
for i in range(18):
	if i not in large_features:
		if i == 0 or i == 15:
			print(i, '-\t', features[i], '\t\t\t', my_data['keyframes'][keyframe_index][features[i]])
		elif i == 8:
			print(i, '-\t', features[i], '\t', my_data['keyframes'][keyframe_index][features[i]])
		else:
			print(i, '-\t', features[i], '\t\t', my_data['keyframes'][keyframe_index][features[i]])
	else:
		if i==3:
			print(i, '-\t', features[i], '\t\t\t <Size: ', len(list(my_data['keyframes'][keyframe_index][features[i]])), '>')
		else:
			print(i, '-\t', features[i], '\t\t <Size: ', len(list(my_data['keyframes'][keyframe_index][features[i]])), '>')


print('\n')
print('2-', features[2])
print('---------')
print(my_data['keyframes'][keyframe_index][features[2]])

print('\n')
print('5-', features[5])
print('---------')
print(my_data['keyframes'][keyframe_index][features[5]])

count = 0
for lm in my_data['keyframes'][keyframe_index][features[5]]:
	if lm >= 0:
		count += 1
print('\n')
print('Total', count, 'values not -1')

print('\n')
print('17-', features[17])
print('-------------')
print(my_data['keyframes'][keyframe_index][features[17]])



print('\n')
print('4-', features[4])
print('---------')
total_keypoints = len(my_data['keyframes'][keyframe_index][features[4]])

print(total_keypoints, 'keypoints available, and each keypoint is dictionary of', my_data['keyframes'][keyframe_index][features[4]][0].keys())
print('\n')
print('First 10 keypoints: ')
count = 0
for kp in my_data['keyframes'][keyframe_index][features[4]]:
	print(kp)
	count += 1
	if count > 10:
		break

first = 0
second = 0
third = 0
fourth = 0
fifth = 0
sixth = 0
seventh = 0
eighth = 0
for kp in my_data['keyframes'][keyframe_index][features[4]]:
	if kp['oct'] == 0:
		first += 1
	if kp['oct'] == 1:
		second += 1
	if kp['oct'] == 2:
		third += 1
	if kp['oct'] == 3:
		fourth += 1
	if kp['oct'] == 4:
		fifth += 1
	if kp['oct'] == 5:
		sixth += 1
	if kp['oct'] == 6:
		seventh += 1
	if kp['oct'] == 7:
		eighth += 1

print('\n')
print(first, 'keypoints in oct 0')
print(second, 'keypoints in oct 1')
print(third, 'keypoints in oct 2')
print(fourth, 'keypoints in oct 3')
print(fifth, 'keypoints in oct 4')
print(sixth, 'keypoints in oct 5')
print(seventh, 'keypoints in oct 6')
print(eighth, 'keypoints in oct 7')

print('\n')
print('3-', features[3])
print('--------')
total_no_of_descs = len(my_data['keyframes'][keyframe_index][features[3]])
descs_length = len(my_data['keyframes'][keyframe_index][features[3]][0])
print(total_no_of_descs, 'descriptors, each of length', descs_length, 'are available')
print('\n')
print('First 10 descriptors: ')
count=0
for d in my_data['keyframes'][keyframe_index][features[3]]:
	print(d)
	count += 1
	if count>10:
		break


print('\n')
print('16-', features[16])
print('-----------')
total_val = len(my_data['keyframes'][keyframe_index][features[16]])
val_length = len(my_data['keyframes'][keyframe_index][features[16]][0])
print(total_val, 'values, each of length', val_length, 'are available')
print('\n')
print('First 10 values: ')
count=0
for d in my_data['keyframes'][keyframe_index][features[16]]:
	print(d)
	count += 1
	if count>10:
		break

print('\n')
print('----------------------------------------------------  other keys  -------------------------------------------------------------')
print('frame_next_id\t\t', my_data['frame_next_id'])
print('keyframe_next_id\t', my_data['keyframe_next_id'])
print('landmark_next_id\t', my_data['landmark_next_id'])
print('\n')






