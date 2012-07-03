Name: xhkeys
Version: 2.2.1
Release: alt2

Summary: xhkeys - a tool for your special keyboard
License: GPL
Group: System/X11
URL: http://wmalms.tripod.com/

Source0: %name-%version.tar.gz

Patch0: xhkeys-2.2.1-alt-fix-build.patch

Packager: Igor Zubkov <icesik@altlinux.ru>

# Automatically added by buildreq on Mon Jul 14 2008
BuildRequires: imake libXt-devel xorg-cf-files xorg-xextproto-devel

%description
This application is designed to suit any PC keyboard that has some extra
keys that otherwise make no use with X (e.g. multimedia keys on some
keyboard models).

With xhkeys you can assign a particular action to any key or key combination
(key and shift state) that can be of one of the following types:

 - built-in operation (e.g. window circulation)
 - calling an external application
 - calling a custom module (plugin)
 - sending a key event to a specified application
   (simulating key press/release)
 - sending a mouse button event to a specified application
   (simulating button press/release)

Features:
 - on-screen display
 - continuous plugin call (e.g. for monitoring CD Audio position)

The package includes configuration utility.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
mkdir -p %buildroot%_bindir/
install -p -m755 xhkeys %buildroot%_bindir/
install -p -m755 xhkconf %buildroot%_bindir/
mkdir -p %buildroot%_libdir/xhkeys/
install -p -m755 xhkeys_cdaudio.so %buildroot%_libdir/xhkeys/
install -p -m755 xhkeys_mixer.so %buildroot%_libdir/xhkeys/

%files
%doc XHkeys.sample manual.html xhkeys.lsm CHANGES
%_bindir/*
%dir %_libdir/xhkeys/
%_libdir/xhkeys/*.so

%changelog
* Mon Jul 14 2008 Igor Zubkov <icesik@altlinux.org> 2.2.1-alt2
- fix build
- buildreq

* Sat Nov 05 2005 Igor Zubkov <icesik@altlinux.ru> 2.2.1-alt1
- Initial build for Sisyphus

* Fri Jul 02 2004 Michael Glickman <michg@alphalink.com.au>
- Fixed Stop with cdaudio plugin
- Fixed configuration script (has_shape)
- No OSD on plugin error if message length is 0

* Thu Jul 01 2004 Michael Glickman <michg@alphalink.com.au>
- version 2.2.0
- OSD is now displayed in a separate window (not root window as before)
  which makes it always on top. The idea is shamelessly broowed from
  libxosd by Andre Renaud <andre@ignavus.net> - thanks,  Andrew.
- by default osd text is vertically aligned to the middle of osd window
  (used to be fixed 2 lines below top)
- new configuration resources related to OSD:  osdTextTop,  osdBkgrMask,
  osdBkgrColour(osdBkgrColor), osdFrameWidth, osdFrameColour(osdFrameColor)
- a simpler plugin interface
- optional display_name with --osd command line argument 
- added --disable-shape config option

* Thu Jun 24 2004 Michael Glickman <wmalms@yahoo.com>
- version 2.1.1
- Fixed status report for CD leadout 

* Sun Jun 20 2004 Michael Glickman <wmalms@yahoo.com>
- version 2.1.0
- Added WndClose operation
- Added to window target F - input focus owner
- Added key selection by KeySym code for Send Key Event
- In Key/Mouse Event:
   - setInputFocus the target window before XSendEvent,
     and restore old input focus after all events are send
   - PressRelease can now be zero, in which case target window
     is also raised and input focus is retained
- Changed default keytimeout and clicktimeout to 10 and 15 seconds resp
  (was 5 and 8 secs)
- Fixed documentation bugs and brought it up to date.

* Tue Jun 15 2004 Michael Glickman <wmalms@yahoo.com>
- version 2.0.0
- revised, added plugin and OSD support, cleaner
  xhkconf code, etc     

* Sun Apr 06 2003 Michael Glickman <wmalms@yahoo.com>
- version 1.0.2
  bug fixes (zombies after run ext app, etc)

* Tue Aug 06 2002 Michael Glickman <wmalms@yahoo.com>
- version 1.0.0
- first RPM release
