# Installing GHMM
Installing GHMM on Mac OS 10.10 is generally straightforward, but as far as we know, you must install GHMM itself from source.

## Steps
* Make sure that you have XCode and the XCode command line tools installed
* Make sure that you have homebrew installed. Homebrew is probably the best modern package manager for Mac OS X and is similar to `apt-get` or `yum` on Debian or CentOS systems, respectively. After installing homebrew, run `brew update` and `brew install swig`. `swig` is required for compilation of GHMM
* Download GHMM source from svn: `svn checkout svn://svn.code.sf.net/p/ghmm/code/trunk/ghmm ghmm`; once downloaded, `cd` into the directory and run:
    * ./autogen.sh
    * ./configure
    * make
    * make install

Then you should be good to go!

## Other Resources

You may want to confer with [http://ghmm.sourceforge.net/installation.html](http://ghmm.sourceforge.net/installation.html) for more information about other systems. The instructions there for Mac OS X may also be appropriate, though they reference the older package manager Fink.
