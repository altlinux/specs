Name: libGLw
Version: 8.0.0
Release: alt1.git20130123
Epoch: 5
License: MIT
Summary: Mesa OpenGL widget library
Group: System/Libraries
Url: http://www.mesa3d.org

# git://anongit.freedesktop.org/mesa/glw
Source: %name-%version.tar

BuildRequires: libGL-devel libX11-devel libXext-devel libXt-devel libopenmotif-devel

%description
Mesa OpenGL widget library

%package devel
Summary: Mesa OpenGL widget development package
Group: Development/C
Requires: libGL-devel libGLw = %epoch:%version-%release

%description devel
Mesa OpenGL widget development package

%prep
%setup

%build
%autoreconf
%configure \
	--enable-motif \
	--disable-static

%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/GL/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc


%changelog
* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5:8.0.0-alt1.git20130123
- Version 8.0.0

* Tue Feb 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 5:1.0.0-alt1
- 1.0.0

