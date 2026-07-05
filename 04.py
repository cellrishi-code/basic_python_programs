class Custom_dataset:
    
    def __init__(self,data_list):
        self.data_list = data_list
        
    def fetch_items(self,i):
        return self.data_list[i]
    
    def no_items(self):
        return len(self.data_list)
    
    
data_set = Custom_dataset(["sample a", "sample b", "sample c"])

print(f"items : {data_set.fetch_items(0)}, length :{data_set.no_items()}")

