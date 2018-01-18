Written by Nick Sullivan, The University of Adelaide

This package contains models needed to simulate tags that are used for visual
tracking. It was a pain in the ass to make. There's two main ways to spawn 
something in Gazebo using ROS: SDF files and URDF files.

SDF files are newer and nicer, but URDF are required when using a robot in ROS
(as of this writing). Both methods use a #.xacro file, then use xacro to parse
the file into the parameter server, which Gazebo spawner reads from to spawn
the model. So we're stuck with URDF if you want the tag to move with the robot. 
The annoying thing about URDF is that you can't dynamically apply textures as you
can with SDF (I think). It requires importing a .dae file, which are text dumps
from 3D modelling software. I installed Blender, blindly wandered through some
tutorials trying to make a goddam texture on a box, and eventually did using
the following procedure:

  Following here: http://blender.stackexchange.com/questions/160/can-blender-export-to-the-collada-format
  The most recent Blender is not available in the software centre, so we get
  it from another source. Download from the blender website. 
  Now I'm sorry for the vagueness of this description to make a textured square,
  but I don't know Blender very well:
    Create a new Blender model.
    Enter edit mode (tab)
    Select all (a)
    Unwrap (u->unwrap)
    At the top of the screen, screen layout->UV editing
    In the UV pane->Image->Open
    Select 'tab0.png'
    Screen layout->default
    In material (tiny sphere on the right)->options->face textures (enabled)
    File->export->collada
    Tick 'include UV Textures' and 'include material textures'
    Select a filename.
    
Hopefully you don't need to do that, as the .dae files can be edited to replace
the images, as well as to resize the tag. To follow the bouncing ball, start at 
the launch file. 


I WANT TO MAKE ANOTHER TAG
In one terminal: 
  roscore
In another:
  rosrun ar_track_alvar createMarker NUMBER
Rename it to tagNUMBER.png, move it into  'tag_world/meshes/images'.
Copy a 'tagNUMBER.dae', replace all instances of 'tagNUMBER' with your new number.
Or use the renaming script, as mentioned at the resize section.

I WANT TO RESIZE THE TAG
I couldn't find a way to dynamically resize the tag, so I made a script to copy
and paste the 'tag0.dae' multiple times so that manual changing is kept to a 
minimum.
Alter 'tag0.dae', I've marked the line where it specifies scale.
Copy 'tag0.dae' into the script folder.
Start a terminal and change into the script folder.
  python duplicate_dae.py
Copy the 'tag#.dae' files back into the meshes folder.

I WANT TO USE DIFFERENT IMAGES
Replace the images in 'meshes/images'. If you use different names you'll have to
update the references in the '.dae' files.


