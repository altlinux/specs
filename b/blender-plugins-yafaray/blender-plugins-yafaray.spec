Name: blender-plugins-yafaray
Version: 0.1.1
Release: alt1.1.1

Summary: YafaRay export scripts for Blender
License: LGPL
Group: Graphics
Url: http://www.yafaray.org/

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source0: YafaRay-blender.%version.zip

Requires: yafaray = %version
Obsoletes: yafaray-blender

# Automatically added by buildreq on Wed Nov 04 2009
BuildRequires: unzip

%description
Blender is the host application for YafaRay.
You need this package to run YafaRay directly from Blender.

%prep
%setup -n yafaray-blender

%build

%install
install -d -m755 %buildroot%_libdir/blender/scripts
install -p -m644 *.py %buildroot%_libdir/blender/scripts

%files
%_libdir/blender/scripts/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.1
- Rebuilt with python 2.6

* Wed Nov  4 2009 Sergey Kurakin <kurakin@altlinux.org> 0.1.1-alt1
- 0.1.1
- build separated from yafaray
- package renamed: yafaray-blender to blender-plugins-yafaray
