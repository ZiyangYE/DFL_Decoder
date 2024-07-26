# DFL_Decoder
A small tool for decoding R&amp;S dfl files

I measured my chip and saved the data in dfl. 

Then I went home. 

Ah, dfl files don't look that convenient to use. 

I don't want to go to the lab again (I hate going out) 

Ok, let's write a little tool to convert dsl files into readable data. 

The instrument I use is the R&S FSWP, and there are no plans to support other instruments. 

For confidentiality reasons, I cannot provide a test file.


## STEP 0
A good compressed file manager can open .dfl files directly. 
 
Or you can change the suffix to .zip on Windows platform and then use 7zip to open it.

## STEP 1
Under _Applications\Ssa\Phase Noise_, there is a _ChannelSsa Buffers_ file, which is our target. 

I believe this will be different for different instruments, so please be flexible.

It's a xml file. Looks like

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<Database FWVersion="ES-MAIN_21.2.9.201">
	<Root Name="SrTbChannel" SaveItemType="22" NofProps="1" NofSta

....................
 ```

## STEP 2
Change the path in the script, then run it. 

I basically only used the built-in libraries of Python except numpy. It should be OK to use python3.11 with numpy. If there are any dependency issues, please solve them yourself.

The output is named output.npy & output.csv .

Please handle the horizontal and vertical axes yourself.

