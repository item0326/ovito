import warnings
warnings.filterwarnings('ignore', message='.*OVITO.*PyPI')
from ovito.io import import_file
from ovito.vis import Viewport, TachyonRenderer
from ovito.modifiers import SliceModifier
import os
import shutil
import time
filename='00NPT_*.cfg'
path = "./image"
output_imagename='NPT'

if not os.path.isdir(path): os.makedirs(path)

pipeline = import_file(filename)
pipeline.add_to_scene()
vp = Viewport(type = Viewport.Type.Back)
vp.zoom_all() #自動重新定位相機
pipeline.modifiers.append(SliceModifier(normal=(0,1,0), distance=150))
# for frame in range(pipeline.source.num_frames):
#     if os.path.exists(path + '/' + output_imagename + '%d.png' % (frame+1)):os.remove('./image/'+ output_imagename +'%d.png' % (frame+1))
 
# time.sleep(2)
for frame in range(pipeline.source.num_frames):
    vp.render_image(filename=output_imagename+'%d.png' % (frame+1),frame=frame,size=(800,600),renderer=TachyonRenderer())
    if os.path.exists(path + '/' + output_imagename + '%d.png' % (frame+1)):os.remove('./image/'+ output_imagename +'%d.png' % (frame+1))
    shutil.move('./'+ output_imagename + '%d.png' % (frame+1),path+'/')
# time.sleep(2)
# for frame in range(pipeline.source.num_frames):
#     shutil.move('./'+ output_imagename + '%d.png' % (frame+1),path+'/') 

     
                                                                                                   