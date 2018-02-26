Name: gl-117
Version: 1.3.2
Release: alt1

Summary: GL-117 is an action flight simulator
License: GPL
Group: Games/Arcade
Url: http://www.heptargon.de/gl-117/gl-117.html

Packager: Alexander Gvozdev <gab@altlinux.ru>

Requires: libSDL libfreeglut libSDL_gfx libSDL_image libSDL_mixer libGL libGLU

Source0: %name-%version-src.tar.bz2

BuildRequires: gcc-c++ libfreeglut-devel libSDL-devel libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel
BuildRequires: libXt-devel libjpeg-devel automake_1.10 libGLU-devel libGL-devel


%description
GL-117 is an action flight simulator for Linux/Unix and MSWindows. Enter the Eagle Squadron and succeed in several challanging missions leading though different landscapes. Five predefined levels of video quality and an amount of viewing ranges let you perfectly adjust the game to the performance of your system. Joystick, mouse, sound effects, music...

%prep
%setup -q -n gl-117-1.3.2-src

%build

%configure 

%make_build

%install
%make DESTDIR=%buildroot install


%files
%_bindir/gl-117
%doc AUTHORS README
%_datadir/gl-117/*





%changelog
* Sun Mar 22 2009 Alexander Gvozdev  <gab@altlinux.ru> 1.3.2-alt1
- Initial build for ALT Linux.
