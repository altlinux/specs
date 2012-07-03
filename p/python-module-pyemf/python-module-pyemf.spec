Name: python-module-pyemf
Version: 2.0.0
Release: alt3.1

Summary: Pure Python Enhanced Metafile Library

Group: Development/Python
License: LGPL
Url: http://pyemf.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

%setup_python_module pyemf

Source: http://dl.sf.net/%modulename/%modulename-%version.tar.bz2
Patch: %modulename-%version.patch

# manually removed: eric
# Automatically added by buildreq on Mon Jan 02 2006
BuildRequires: python-devel python-modules-compiler python-modules-encodings

%description
Pure Python library for Enhanced Metafile (.emf) ECMA-234 compliant
scalable graphics files. ECMA-234 is the published API for the Windows
GDI, and .emf vector graphics files are natively supported by the
OpenOffice suite of tools and in RTF files.

%prep
%setup -q -n %modulename-%version
%patch

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt3.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3
- Rebuilt with python 2.6

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 2.0.0-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 2.0.0-alt2
- Build as noarch.

* Mon Oct 08 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- add patch from vsdviewer

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.1
- initial build for ALT Linux Sisyphus
