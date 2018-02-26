Name: mview
Version: 0.3.1
Release: alt1.1

Summary: Mesh Viewer

Group: Graphics
License: LGPL
Url: http://mview.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-src-%version.tar.bz2
Patch: %name-gcc43.patch

# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: gcc-c++ libqt4-devel

%description
The Mesh Viewer is an easy to use lightweight application to display
triangular meshes from a variety of file formats (see 3D formats).
It uses the OpenGL API to render the models.

%prep
%setup -q -n %name-src-%version
%patch

%build
export QTDIR=%_qt4dir
export PATH=$QTDIR/bin:$PATH
%make_build FLAGS=-fpermissive QT4

%install
install -D -m0755 %name %buildroot/%_bindir/%name

#longtitle="Mesh Viewer for 3D files"

%files
%doc README AUTHORS Documentation/*
%_bindir/%name

%changelog
* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.1
- Fixed build

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- fix build with gcc 4.3
- build with Qt4
- update buildreqs

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt0.1
- new version 0.3.1 (with rpmrb script)
- use smp build

* Tue Feb 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt2
- rebuild with gcc 3.4: add some fixes

* Thu Dec 16 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- first build for ALT Linux Sisyphus
