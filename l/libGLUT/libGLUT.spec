Name: libGLUT
Version: 8.0.1
Release: alt2
Epoch: 5
License: MIT
Summary: Mesa OpenGL Utility Toolkit library
Group: System/Libraries
Url: http://www.mesa3d.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: libglut = %epoch:%version-%release
Conflicts: freeglut libfreeglut

Source: %name-%version.tar

BuildRequires: gcc-c++ libGL-devel libGLU-devel libXi-devel libXmu-devel

%description
Mesa OpenGL Utility Toolkit library

%package devel
Summary: Mesa OpenGL Utility Toolkit development package
Group: Development/C
Requires: libGLUT = %epoch:%version-%release
Provides: libglut-devel = %epoch:%version-%release
Conflicts: freeglut-devel libfreeglut-devel

%description devel
Mesa OpenGL Utility Toolkit development package

%prep
%setup

%build
%autoreconf
%configure \
	--enable-texture-float \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

install -m644 include/GL/glutf90.h %buildroot%_includedir/GL

%files
%_libdir/*.so.*

%files devel
%_includedir/GL/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc


%changelog
* Tue Feb 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5:8.0.1-alt2
- Added GL/glutf90.h (ALT #26955)

* Tue Feb 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 5:8.0.1-alt1
- 8.0.1

