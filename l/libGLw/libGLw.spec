Name: libGLw
Version: 1.0.0
Release: alt1
Epoch: 5
License: MIT
Summary: Mesa OpenGL widget library
Group: System/Libraries
Url: http://www.mesa3d.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

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
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-motif \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/GL/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc


%changelog
* Tue Feb 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 5:1.0.0-alt1
- 1.0.0

