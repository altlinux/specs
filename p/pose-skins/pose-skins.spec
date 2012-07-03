Name: pose-skins
Version: 1.9
Release: alt3

Summary: PalmOS emulator skins
Group: Emulators
License: GPL
URL:  http://www.palmos.com/dev/tools/emulator/

BuildArch: noarch
#This doesn't work until pose is exclusivearch
#Requires: pose
Packager: Fr. Br. George <george@altlinux.ru>
Source0: http://www.palmos.com/dev/tools/emulator/emulator-skins-19.tar.gz
Source1: HandspringSkins_3.1H5.zip

# Automatically added by buildreq on Wed Feb 04 2004
BuildRequires: unzip

%description
Palm OS Emulator is an application that emulates the hardware for most          
Palm Computing Platform Hardware devices (e.g., Pilot, PalmPilot, Palm          
III, Palm V, Palm VII, etc.).  The Emulator runs on most standard               
desktop computers, includes those running Windows 95, Windows 98,               
Windows NT 4.0, Windows 2000, Mac OS 8.6, Mac OS 9.x, Mac OS X, and             
several flavors of Unix.                                                        
                                                                                
With the Palm OS Emulator, you can emulate the functions of a Palm              
hardware device, including running the built-in application, as well as         
installing and running 3rd party applications.

This package contains skins for pose.

%prep
%setup -q -n Skins_v1.9 -a1

%build

%install

mkdir -p $RPM_BUILD_ROOT%_datadir/pose/skins

rm -f Handspring/*
mv -f HandspringSkins_3.1H5/Handspring/* Handspring
cp -r {Handspring,Palm,Symbol,TRG} $RPM_BUILD_ROOT%_datadir/pose/skins

%files
%_datadir/pose
%doc ReadMe.txt

%changelog
* Tue Mar 10 2009 Fr. Br. George <george@altlinux.ru> 1.9-alt3
- Resurrect from orphaned

* Wed Feb 04 2004 Dimitry V. Ketov <dketov@altlinux.ru> 1.9-alt2
- Fixed build requirements

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.9-alt1
- 1.9
- Added HandSpring skins

* Tue Oct 30 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.8-alt1
- First build for Sisyphus
