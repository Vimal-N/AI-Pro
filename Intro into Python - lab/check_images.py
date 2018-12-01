#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images.py
#
# TODO: 0. Fill in your information in the programming header below
# PROGRAMMER: Vimal Natarajan - VKN
# DATE CREATED:
# REVISED DATE: 05-06-2018            <=(Date Revised - if any)
# PURPOSE: Check images & report results: read them in, predict their
#          content (classifier), compare prediction to actual value labels
#          and output results
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir

# Imports classifier function for using CNN to classify images
from classifier import classifier

# Main program function defined below
def main():
    # DONE: 1. Define start_time to measure total program runtime by
    # collecting start time
    start_time = time()

    # DONE: 2. Define get_input_args() function to create & retrieve command
    # line arguments
    in_arg = get_input_args()
    #print("printing out command line arguments --> \n dir = ",in_arg.dir,"\n arch = ",in_arg.arch,"\n dogfile = ",in_arg.dogfile )

    # DONE: 3. Define get_pet_labels() function to create pet image labels by
    # creating a dictionary with key=filename and value=file label to be used
    # to check the accuracy of the classifier function
    answers_dic = get_pet_labels(in_arg.dir)
    # print("Total pet images key from the dictionary",len(answers_dic))
    # print("Printing some of them below:")
    # counter = 0
    # for key in answers_dic:
    #
    #     print("Key-value",counter+1," KEY: ",key,
    #           "VALUE: ",answers_dic[key])
    #     counter +=1

    # DONE: 4. Define classify_images() function to create the classifier
    # labels with the classifier function uisng in_arg.arch, comparing the
    # labels, and creating a dictionary of results (result_dic)
    result_dic = classify_images(in_arg.dir,answers_dic,in_arg.arch)
    print("Matches:")
    no_matches = 0
    no_notmatches = 0
    for key in result_dic:
        if result_dic[key][2]==1:
            no_matches +=1
            print("Real: %-26s Classifier: %-30s" % (result_dic[key][0],
                                                     result_dic[key][1]))
    print("No Match:")
    for key in result_dic:
        if result_dic[key][2]==0:
            no_notmatches +=1
            print("Real: %-26s Classifier: %-30s" % (result_dic[key][0],
                                                     result_dic[key][1]))

    print("\n matches count#",no_matches)
    print("\n No matches count#",no_notmatches)
    # TODO: 5. Define adjust_results4_isadog() function to adjust the results
    # dictionary(result_dic) to determine if classifier correctly classified
    # images as 'a dog' or 'not a dog'. This demonstrates if the model can
    # correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(result_dic,in_arg.dogfile)
    print("Matches:")
    no_matches = 0
    no_notmatches = 0
    for key in result_dic:
        if result_dic[key][2]==1:
            no_matches +=1
            print("Real: %-26s Classifier: %-30s petlabel: %1d clslabel: %1d"
            % (result_dic[key][0],result_dic[key][1],result_dic[key][3],
                result_dic[key][4]))
    print("No Match:")
    for key in result_dic:
        if result_dic[key][2]==0:
            no_notmatches +=1
            print("Real: %-26s Classifier: %-30s petlabel: %1d clslabel: %1d"
            % (result_dic[key][0],result_dic[key][1],result_dic[key][3],
                result_dic[key][4]))

    print("\n matches count#",no_matches)
    print("\n No matches count#",no_notmatches)

    # TODO: 6. Define calculates_results_stats() function to calculate
    # results of run and puts statistics in a results statistics
    # dictionary (results_stats_dic)
    results_stats_dic = calculates_results_stats(results_dic)

    # TODO: 7. Define print_results() function to print summary results,
    # incorrect classifications of dogs and breeds if requested.
    print_results()

    # DONE: 1. Define end_time to measure total program runtime
    # by collecting end time
    #sleep(10)
    end_time = time()

    # DONE: 1. Define tot_time to computes overall runtime in
    # seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:", tot_time," in seconds.")
    #print("\nTotal Elapsed Runtime:", str( int( (tot_time / 3600) ) ) + ":" +
     #     str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" +
     #     str( round(  ( (tot_time % 3600) % 60 ) ) ) )



# TODO: 2.-to-7. Define all the function below. Notice that the input
# paramaters and return values have been left in the function's docstrings.
# This is to provide guidance for acheiving a solution similar to the
# instructor provided solution. Feel free to ignore this guidance as long as
# you are able to acheive the desired outcomes with this lab.

def get_input_args():
    """
    Retrieves and parses the command line arguments created and defined using
    the argparse module. This function returns these arguments as an
    ArgumentParser object.
     3 command line arguements are created:
       dir - Path to the pet image files(default- 'pet_images/')
       arch - CNN model architecture to use for image classification(default-
              pick any of the following vgg, alexnet, resnet)
       dogfile - Text file that contains all labels associated to dogs(default-
                'dognames.txt'
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """
    #creates a parser
    parser  = argparse.ArgumentParser() #input("Enter the path of pet image (as pet_images/....) : ")
    parser.add_argument('--dir', type = str, default = 'pet_images/',
                        help = 'path to the folder my_folder')
    parser.add_argument('--arch', type = str, default = 'vgg',
                        help = 'choose a model')
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt',
                        help = 'Text file that contains dog name')

    return parser.parse_args()


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image
    files. Reads in pet filenames and extracts the pet image labels from the
    filenames and returns these label as petlabel_dic. This is used to check
    the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)
    """
    list_of_files = listdir(image_dir)
    #images_dir_filename = listdir(image_dir)
    #for file in images_dir_filename:
     #   file = image_dir+file
      #  print("Debug --> Printing Filename with Dirname",file)
    dictionary_file_name =  dict()
    for i in range(0,len(list_of_files),1):
        # print("File name from the listdir: ",list_of_files[i])
        image_filename = list_of_files[i].split("_")
        labels_of_pet = ""
        for eachword in image_filename:
            if eachword.isalpha():
                labels_of_pet += eachword.lower() + " "
        labels_of_pet = labels_of_pet.strip()
        if list_of_files[i] not in dictionary_file_name:
            dictionary_file_name[list_of_files[i]] = labels_of_pet
        else:
            print("Warning: Duplicate files exist in dictionary",
                    list_of_files[i])
    return(dictionary_file_name)


def classify_images(images_dir,petlabel_dic,model):
    """
    Creates classifier labels with classifier function, compares labels, and
    creates a dictionary containing both labels and comparison of them to be
    returned.
     PLEASE NOTE: This function uses the classifier() function defined in
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the
     classifier() function to classify images in this function.
     Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by pretrained CNN models (string)
      petlabel_dic - Dictionary that contains the pet image(true) labels
                     that classify what's in the image, where its' key is the
                     pet image filename & it's value is pet image label where
                     label is lowercase with space between each word in label
      model - pretrained CNN whose architecture is indicated by this parameter,
              values must be: resnet alexnet vgg (string)
     Returns:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and
                    classifer labels and 0 = no match between labels
    """
    #classifier()
    images_dir_filename = listdir(images_dir)
    #model_petlabel_dic = dict()
    results_dic = dict()
    # for block to pass values into classifer method and get model label
    # model lable will be added to a dictionary
    for key in petlabel_dic:
        file_name = images_dir+key
        # print(file_name)
        model_label = classifier(file_name,model)
        #print(model_label)
        model_label = model_label.lower()
        model_label = model_label.strip()
        truth = petlabel_dic[key]
        found = model_label.find(truth)
        if found>=0:
            if( (found ==0 and len(truth)==len(model_label) ) or
                ( ( (found==0) or (model_label[found-1]==" ") ) and
                  ( (found + len(truth)==len(model_label)) or
                    (model_label[found + len(truth):found+len(truth)+1] in
                    (","," ") )
                  )
                )
              ):
               if key not in results_dic:
                   results_dic[key] = [truth,model_label,1]

            else:
                   if key not in result_dic:
                       results_dic[key] = [truth,model_label,0]
        else:
            if key not in results_dic:
                results_dic[key] = [truth,model_label,0]
    return(results_dic)


def adjust_results4_isadog(results_dic, dogsfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    --- where idx 3 & idx 4 are added by this function ---
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
     dogsfile - A text file that contains names of all dogs from ImageNet
                1000 labels (used by classifier model) and dog names from
                the pet image files. This file has one dog name per line
                dog names are all in lowercase with spaces separating the
                distinct words of the dogname. This file should have been
                passed in as a command line argument. (string - indicates
                text file's name)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    dognames_dic = dict()
    with open(dogsfile,"r") as file:
        line = file.readline()
        while line !="":
            line=line.rstrip()
            if line not in dognames_dic:
                dognames_dic[line]=1
            else:
                print("# WARNING: Duplicate dog name in the dognames file")
            line = file.readline()
    for key in results_dic:
        if results_dic[key][0] in dognames_dic:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1,1))
            else:
                results_dic[key].extend((1,0))
        else:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0,1))
            else:
                results_dic[key].extend((0,0))



def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the run using classifier's model
    architecture on classifying images. Then puts the results statistics in a
    dictionary (results_stats) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats - Dictionary that contains the results statistics (either a
                     percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
    """
    results_stats = dict()
    results_stats['n_dog_img'] = 0
    results_stats['n_match'] = 0
    results_stats['n_correct_dogs'] = 0
    results_stats['n_notcorrect_dogs'] = 0
    results_stats['n_correct_breed'] = 0

    for key in results_stats:
        if results_dic[key][2] == 1:
            results_stats['n_match'] += 1
        if sum(results_dic[key][2:]) == 3:
            results_stats['n_correct_breed'] += 1
        if results_dic[key][3] == 1:
            results_stats['n_dog_img'] += 1
            if results_dic[key][4] == 1:
                results_stats['n_correct_dogs'] += 1
        else:
            if results_dic[key][4] == 0:
                results_stats['n_notcorrect_dogs'] += 1

    results_stats['n_images'] = len(results_dic)
    
    # Z = len(results_dic)
    # A,B,C,D,E,Y= 0,0,0,0,0,0
    # B = 0
    # C = 0
    # D = 0
    # E = 0
    # Y = 0
    # for key in results_stats:
    #     if results_stats[key][3] == 1 and results_stats[key][4] ==1:
    #         A += 1
    #     else:
    #         if results_stats[key][3] == 1:
    #             B +=1
    #         else:
    #             if results_dic[key][3] == 0 and results_dic[key][4] == 0:
    #                 C +=1
    #             else results_dic[key][3] == 0:
    #                 D +=1
    #     if results_dic[key][3] == 1 and results_dic[key][2] == 1:
    #         E +=1
    #     if results_dic[key][2] == 1:
    #         Y +=1
    # n_pct_dog = (A/B) *100
    # if D > 0:
    #     n_pct_non_dog = (C/D) *100
    # else:
    #     n_pct_non_dog = 0
    # n_pct_dog_breeds = (E/D)*100




    return results_stats


def print_results():
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
      results_stats - Dictionary that contains the results statistics (either a
                     percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
      model - pretrained CNN whose architecture is indicated by this parameter,
              values must be: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """
    pass



# Call to main function to run the program
if __name__ == "__main__":
    main()
