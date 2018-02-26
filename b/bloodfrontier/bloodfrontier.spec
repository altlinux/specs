%define rev svn6200
Name: bloodfrontier
Version: 0.84
Release: alt2.%rev
Summary: Blood Frontier is a free multiplayer/singleplayer FPS
Group: Games/Arcade
License: Zlib
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://www.bloodfrontier.com/
Source: http://sourceforge.net/projects/bloodfrontier/files/BloodFrontier/%name.tar.gz
Source1: bloodfrontier_client.sh
Source2: bloodfrontier_server.sh
Source3: %name.desktop
Source4: %name.png

Patch0: bloodfrontier-makefile.patch

Requires: %name-data = %version

# Automatically added by buildreq on Sun Jul 26 2009
BuildRequires: gcc-c++ libGL-devel libSDL_sound-devel libSDL_image-devel libSDL_mixer-devel libX11-devel zlib-devel

%description
The game is a single-player and multi-player first-person shooter,
built as a total conversion of Cube Engine 2, which lends itself
toward a balanced gameplay, completely at the control of map makers,
while maintaining a general theme of tactics and low gravity.

%prep
%setup -q -n %name
%patch0 -p1

%build
%make_build -C src/ CFLAGS="%optflags" CXXOPTFLAGS="%optflags"

%install
mkdir -p %buildroot%_bindir

install -pD -m 755 %SOURCE1 %buildroot%_bindir/bloodfrontier_client
install -pD -m 755 %SOURCE2 %buildroot%_bindir/bloodfrontier_server

mkdir -p %buildroot%_desktopdir
install -pD -m 644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_liconsdir
install -pD -m 644 %SOURCE4 %buildroot%_liconsdir/%name.png

install -pD -m 755 %_builddir/%name/src/bfclient %buildroot%_bindir/
install -pD -m 755 %_builddir/%name/src/bfserver %buildroot%_bindir/

%files
%_bindir/*
%_desktopdir/%name.desktop
%_liconsdir/*.png

%changelog
* Sat Jun 12 2010 Andrew Clark <andyc@altlinux.org> 0.84-alt2.svn6200
- spec cleanup

* Mon Jun 7 2010 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn6200
- version update to 0.84-alt1.svn6200
- added patch to fix game build

* Fri Mar 12 2010 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn5546
- version update to 0.84-alt1.svn5546

* Wed Dec 30 2009 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn5059
- version update to 0.84-alt1.svn5059

* Thu Dec  3 2009 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn4822
- version update to 0.84-alt1.svn4822
- small fixes in desktop file

* Mon Sep 28 2009 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn4292
- version update to 0.84-alt1.svn4292
- data files are separeted into data package

* Wed Jun 17 2009 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn3914
- initial build for ALT.

