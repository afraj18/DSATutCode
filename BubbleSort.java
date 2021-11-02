package com.company;

import java.util.Arrays;

public class BubbleSort {
    public int[] bubbleSort(int [] list){
        int i,j,temp = 0;

        for (i=0;i<list.length-1;i++){
            for (j=0;j<list.length-1-i;j++){
                if(list[j]>list[j+1]){
                    temp = list[j];
                    list[j]=list[j+1];
                    list[j+1] = temp;
                }
            }
        }
        return list;

    }

    public static void main(String[] args) {
        int arr[] = {2,4,5,1,3};
        BubbleSort bs = new BubbleSort();
        int nrr[] = bs.bubbleSort(arr);
        System.out.println(Arrays.toString(nrr));
    }
}

