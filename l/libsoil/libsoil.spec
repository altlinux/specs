Name: libsoil
Version: 1.07
Release: alt1
Summary: Simple OpenGL Image Library
License: MIT
Group: System/Libraries
URL: http://www.lonesock.net/soil.html 

# git://git.debian.org/git/pkg-games/libsoil.git/
Source:	%name-%version.tar 
Patch: linking_correctly.patch

# Automatically added by buildreq on Tue Oct 30 2012
# optimized out: libX11-devel xorg-xproto-devel
BuildRequires: libGL-devel

%description
SOIL is a tiny C library used primarily for uploading textures into
OpenGL. It supports loading BMP, PNG, JPG, TGA, DDS, PSD and HDR files
as well as saving into TGA, BMP and DDS Files. It is also able to
perform common functions needed in loading OpenGL textures. This package
contains everything needed to develope software using libsoil.

%package devel
Summary: Development environment for %name
Group: Development/C
%description devel
Development environment for %name

%prep
%setup
%patch -p1

%build
cd src && %make_build -f ../projects/makefile/alternate\ Makefile.txt

%install
cd src && %makeinstall -f ../projects/makefile/alternate\ Makefile.txt DESTDIR=%buildroot INSTALL_FILE="install -D" INSTALL_DIR="install -d" LIBDIR="%_libdir"

%files
%_libdir/*.so.*
%exclude %_libdir/*.a

%files devel
%_libdir/*.so
%_includedir/SOIL

%changelog
* Tue Oct 30 2012 Fr. Br. George <george@altlinux.ru> 1.07-alt1
- Initial build from .deb

