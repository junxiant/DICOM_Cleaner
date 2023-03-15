import pydicom
import pydicom._storage_sopclass_uids
import random
import os
from natsort import natsorted


# if __name__ == "__main__":
    
#     for folder in os.listdir('./20220228_1e3c69707d2b38b2d4f6'):
        
#         os.mkdir(f'./fix2/{folder}')
    
#         for file in natsorted(os.listdir(f'./20220228_1e3c69707d2b38b2d4f6/{folder}')):
            
#             ds = pydicom.dcmread(f'./20220228_1e3c69707d2b38b2d4f6/{folder}/{file}')
            
#             ds.ImageOrientationPatient = [round(x,2) for x in ds.ImageOrientationPatient]
            
#             ds.save_as(f'./fix2/{folder}/{file}', write_like_original=False)
            
            

if __name__ == "__main__":
                            
    ds = pydicom.dcmread(f'./Original_1.dcm')
    
    # ds.ImageOrientationPatient = [round(x, 2) for x in ds.ImageOrientationPatient]
    ds.ImageOrientationPatient = [0.99366,-0.08474,-0.07381,0.07984,0.99455,-0.06702]


    ds.save_as(f'./Changed_Orientation_1.dcm', write_like_original=False)