%define gimpver 2.0
Name: sdl-ball
Version: 1.01
Release: alt2
Summary: Free/OpenSource brick-breaking game with pretty graphics
Group: Games/Arcade
License: GPLv2+
Url: http://sdl-ball.sourceforge.net/
Source0: http://dl.sourceforge.net/sourceforge/%name/%name-%version.tar.bz2
#Source1: %name.png
#Source2: %name.desktop
Patch: %name.as-needed.patch

# Automatically added by buildreq on Wed Nov 12
BuildRequires: gcc-c++ libGL-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libgimp-devel

%description
SDL-Ball is a Free/OpenSource brick-breaking game for Linux,BSD and
windows with pretty graphics. It is written in C++ using SDL and OpenGL,
here is the project page on sf.net.

Your mission: To smash your way through a series of progressively harder
and more tricky levels. Your tools: Ultrakinetic titanium balls and your
trusty Gruntmazter-3000-Paddle edition.

%package leveleditor
Group: Games/Arcade
Requires: gimp
Summary: Two level editors for SDL-Ball

%description leveleditor
SDL-Ball is a Free/OpenSource brick-breaking game with pretty graphics.

This package includes two level editors for SDL-Ball, JavaScript-based
(see %_defaultdocdir/%name-%version/index.html) and GIMP plugin. Start
gimp from a terminal in order to record the output from the plugin (you
need that)

%prep
%setup -n %name
# Lame .o in 1.01 
rm -f *.o
# TODO desktop

%build
%make DATADIR=%_gamesdatadir/%name/
gimptool-%gimpver --build leveleditor/gimp-leveleditor/gimp-sdlball.c

%install
mkdir -p %buildroot%_gamesdatadir %buildroot%_gamesbindir
mkdir -p %buildroot%_libdir/gimp/%gimpver/plug-ins
install -Ds %name %buildroot%_gamesbindir
install -Ds gimp-sdlball %buildroot%_libdir/gimp/%gimpver/plug-ins
cp -a themes %buildroot%_gamesdatadir/%name

%files
%doc README changelog.txt leveleditor
%_gamesbindir/%name
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*

%files leveleditor
%doc leveleditor
%_libdir/gimp/2.0/plug-ins/*

%changelog
* Mon May 28 2012 Fr. Br. George <george@altlinux.ru> 1.01-alt2
- Fix build

* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 1.01-alt1
- Autobuild version bump to 1.01

* Wed Nov 12 2008 Fr. Br. George <george@altlinux.ru> 0.13-alt1
- Version up

* Thu Oct 30 2008 Fr. Br. George <george@altlinux.ru> 0.12-alt1
- Initial build from scratch

