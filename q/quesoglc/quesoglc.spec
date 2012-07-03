%undefine __libtoolize
Name:		quesoglc
License:	LGPL
Group:		System/X11
Summary:	QuesoGLC is a free implementation of SGI's OpenGL Character Renderer (GLC)
Version:	0.7.2
Release:	alt2
Source:		%name-%version.tar
Packager:	Anton Farygin <rider@altlinux.ru>
URL:		http://quesoglc.sourceforge.net/

# Automatically added by buildreq on Thu Sep 11 2008
BuildRequires: fontconfig-devel gcc-c++ gcc-fortran glibc-devel-static imake libGL-devel libICE-devel libX11-devel libfreetype-devel libfribidi-devel xorg-cf-files libGLU-devel

%description
QuesoGLC is a free implementation of SGI's OpenGL Character Renderer (GLC).
QuesoGLC is based on the FreeType library, provides Unicode support and is
designed to be easily ported on any platform that supports both FreeType and
OpenGL.


%package devel
Summary: Header files for developing apps which will use QuesoGLC
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки приложений с использованием QuesoGLC
Group: Development/C
Requires: %name = %version-%release
Requires: glibc-devel

%description devel
The OpenGL Character Renderer (GLC) is a subroutine library that provides
OpenGL programs with character rendering services.

A GLC context is an instantiation of the GLC state machine. A GLC client
is a program that uses both OpenGL (henceforth, "GL") and GLC.  When a
client thread issues a GLC command, the thread's current GLC context
executes the command.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%_libdir/libGLC.so.*
%doc README INSTALL

%files devel
%_libdir/libGLC.so
%_pkgconfigdir/*.pc
%_includedir/GL/*.h


%changelog
* Tue Jan 25 2011 Anton Farygin <rider@altlinux.ru> 0.7.2-alt2
- rebuild in new environment

* Thu May 14 2009 Anton Farygin <rider@altlinux.ru> 0.7.2-alt1
- new version
- pkgconfig file added 

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 0.7.1-alt2
- URL and Packager added

* Thu Sep 11 2008 Anton Farygin <rider@altlinux.ru> 0.7.1-alt1
- first build for Sisyphus

