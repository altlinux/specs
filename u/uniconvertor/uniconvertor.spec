Name: uniconvertor
Version: 1.1.4
Release: alt1.1.1

Summary: Universal vector graphics translator

License: LGPL v2, GPL v2 (some packages)
Group: Office
Url: http://sk1project.org/modules.php?name=Products&product=uniconvertor

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://sk1project.org/downloads/uniconvertor/v%version/%name-%version.tar.bz2

%add_python_req_skip Sketch _sketch

# Automatically added by buildreq on Tue Dec 18 2007
BuildRequires: python-devel python-modules-compiler

BuildPreReq: rpm-build-compat >= 1.2

%description
UniConvertor is a universal vector graphics translator. It uses sK1
engine to convert one format to another.
sK1 Team (http://sk1project.org), copyright (C) 2007 by Igor E. Novikov,
Valek Filippov

Import filters:
    * CorelDRAW ver.7-X3 (CDR/CDT/CCX/CDRX/CMX)
    * Adobe Illustrator up to 9 ver. (AI postscript based)
    * Postscript (PS)
    * Encapsulated Postscript (EPS)
    * Computer Graphics Metafile (CGM)
    * Windows Metafile (WMF)
    * XFIG
    * Scalable Vector Graphics (SVG)
    * Skencil/Sketch/sK1 (SK and SK1)
    * Acorn Draw (AFF)

Export filters:
    * AI (Postscript based Adobe Illustrator 5.0 format)
    * SVG (Scalable Vector Graphics)
    * SK (Sketch/Skencil format)
    * SK1 (sK1 format)
    * CGM (Computer Graphics Metafile)
    * WMF (Windows Metafile)


%prep
%setup -q -n UniConvertor-%version

%build
%python_build

%install
%python_install

%files
%doc README
%_bindir/*
%python_sitelibdir/%name/
#%_desktopdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1.1
- Rebuilt with python 2.6

* Tue Jul 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- new version 1.1.4 (with rpmrb script)

* Thu Jan 15 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- new version 1.1.3 (with rpmrb script)

* Thu May 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new version 1.1.2 (with rpmrb script)

* Sat Mar 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)
- fix requires

* Tue Dec 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

