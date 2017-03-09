class BinarySearch(list):

    count = 0
    array = []
    limits = 0
    length = 0

    def __init__(self,a,b):
    	'''the constructor definition section that shows the slicing of arrays into values with
    	specified consecutive value difference. Initialises length to the length of the array.


    	'''
        self.a = a
        self.b = b
        count = 0
        array = []
        limits = 0
        length = 0


        limits = (self.a*self.b)

        for num in range(0,limits):        
            
            array.append(num)                   

        array = array[::self.b]                 

        self.array = array

        length = len(self.array)                
        
        self.length = length

    def search(self,x):
    	'''
    	The binary search procedure is as follows: the search is set to the highest part of the array
    	the array index 0 returns if the value added is 0. The entire algorithm that does the binary search follows through to 
    	the end

    	'''
        array = self.array
        count = 0
        end_result = {}
        low = 0;
        high = self.length-1                    

        if x==0:
            return array.index(0)              
        else:

            while high>=low:                     

                mid = (low + high)//2           
                middle_value= array[mid]       
                count +=1                       
            

                if middle_value < x:           
                    high = mid - 1

                elif middle_value > x:
                    high = mid + 1
                else:
                     return mid

            end_result["Count"]=count
            end_result["Index"]=array.index(x)          
        

            return end_result                  