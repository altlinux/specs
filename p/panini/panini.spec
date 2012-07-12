Name: panini
Version: 0.71.104
Release: alt2.1

Summary: Panini perspective tool
License: GPLv3+
Group: Graphics

# panini previously known as pvqt
URL: http://sourceforge.net/projects/pvqt/
Source: http://downloads.sourceforge.net/pvqt/Panini-%version-src.zip
Source1: panini.desktop
Source2: panini16.png
Source3: panini32.png
Source4: panini48.png

# Automatically added by buildreq on Sun Jan 29 2012
# optimized out: fontconfig libGL-devel libGLU-devel libqt4-core libqt4-devel libqt4-gui libqt4-opengl libstdc++-devel zlib-devel
BuildRequires: gcc-c++ phonon-devel subversion unzip

%description
Panini is a visual tool for creating perspective views from panoramic and wide
angle photographs. More than a pano viewer, more than a view camera, with
features of both. For systems with OpenGL 2.0.

%prep
%setup -n Panini-%version-src

%build
touch panini.pro
qmake-qt4 panini.pro
# with libqt4-devel-4.8.0-alt1 above command no more add -lGLU to LIBS
# fix this by manually adding to SUBLIBS
%make_build CXX="g++ %optflags %optflags_nocpp" SUBLIBS="-lGLU -lz"

%install
install -pD -m755 Panini %buildroot%_bindir/panini
install -pD -m644 %_sourcedir/panini16.png %buildroot%_miconsdir/panini.png
install -pD -m644 %_sourcedir/panini32.png %buildroot%_niconsdir/panini.png
install -pD -m644 %_sourcedir/panini48.png %buildroot%_liconsdir/panini.png

%files
%doc panini-usage.txt
%_bindir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.71.104-alt2.1
- Fixed build

* Sun Jan 29 2012 Victor Forsiuk <force@altlinux.org> 0.71.104-alt2
- Fix FTBFS caused by changed result of Makefile generation by qmake in qt4-4.8.0-alt1.

* Mon Sep 21 2009 Victor Forsyuk <force@altlinux.org> 0.71.104-alt1
- 0.71.104
- Added .desktop file and icons.

* Tue Jun 30 2009 Victor Forsyuk <force@altlinux.org> 0.71.102-alt1
- 0.71.102

* Wed Feb 11 2009 Victor Forsyuk <force@altlinux.org> 0.62.83-alt1
- 0.62.83

* Fri Jan 30 2009 Victor Forsyuk <force@altlinux.org> 0.61.79-alt1
- Initial build.
