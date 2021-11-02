package com.company;

import java.util.Arrays;

public class MergeSort {

    public static void main(String[] args) {

        int [] arr = {3,2,5,3,1,7,6,5,4,5};
        mergeSort(arr);
        System.out.println(arr);
    }

    public static void mergeSort(int [] inputArray){
        if(inputArray.length < 2){
            return;
        }
//        int i = 0,j = 0, k = 0;
        int midsize = inputArray.length/2;
        int left[] = new int[midsize];
        int [] right = new int[inputArray.length-midsize];

        for(int i=0;i<midsize;i++){
            left[i]=inputArray[i];
        }
        for(int i=midsize;i<inputArray.length;i++){
            right[i-midsize] = inputArray[i];
        }
        mergeSort(left);
        mergeSort(right);

        merge(inputArray,left,right);
    }

    public static void merge(int [] inputArray,int [] left,int right[]){
        int leftSize = left.length;
        int rightSize = right.length;
        int i=0,j=0,k=0;

        while (i<leftSize && j<rightSize){
            if(left[i]<=right[j]){
                inputArray[k] = left[i];
                i++;
            }
            else {
                inputArray[k] = right[j];
                j++;
            }
            k++;
        }
        while (i<leftSize){
            inputArray[k] = left[i];
            i++;
            k++;
        }
        while (j<rightSize){
            inputArray[k]=right[j];
            j++;
            k++;
        }

    }

}
