Name: libayemu
Version: 1.0.0
Release: alt2

Summary: AY/YM emulation library 
License: GPL
Group: System/Libraries
URL: http://sashnov.nm.ru/libayemu.html

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Wed Mar 25 2009
BuildRequires: gcc-c++

%description
AY/YM sound chip emulation library.

Install libayemu if you want play AY/YM music and sound effect in
console player, xmms plugin or your own games/demos.

%package devel
Summary: AY/YM emulation library headers and static libs
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains all of the headers and the static libraries for
libayemu.

You'll only need this package if you are doing development.

%package devel-static
Summary: AY/YM emulation static library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static libraries for libayemu.

You'll only need this package if you are doing development.

%prep
%setup -q

%build
%configure \
    --enable-shared \
    --enable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README RELEASENOTES THANKS TODO
%_libdir/libayemu*.so.*

%files devel
%_includedir/ayemu*.h
%_libdir/libayemu*.so

%files devel-static
%_libdir/libayemu.a*

%changelog
* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Rebuilt for soname set-versions

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 1.0.0-alt1
- 0.9.5 -> 1.0.0

* Tue May 23 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.5-alt1
- Initial build for Sisyphus

* Wed Sep 21 2005 Alexander Sashnov <sashnov@ngs.ru>
- split package to two: libayemu and libayemu-devel

* Thu Feb 10 2005 Alexander Sashnov <sashnov@ngs.ru>
- Start rpm spec written
