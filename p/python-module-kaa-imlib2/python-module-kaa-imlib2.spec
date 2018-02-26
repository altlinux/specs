%define oname kaa-imlib2
Name: python-module-%oname
Version: 0.2.3
Release: alt1.1.1.1

Summary: Python bindings for Imlib2

License: LGPL
Group: Development/Python
Url: http://freevo.org/kaa

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname
%add_python_req_skip _Imlib2

Source: http://prdownloads.sf.net/freevo/%oname-%version.tar.bz2

BuildPreReq: rpm-build-compat >= 1.2

# Automatically added by buildreq on Sun Jul 22 2007
BuildRequires: imlib2-devel libfreetype-devel libpng-devel libXext-devel python-module-kaa-base python-module-PyXML libX11-devel

%description
Kaa-Imlib2 is a python module for Imlib2.  It is terribly incomplete.
Its main reason is to provide image manipulation routines for MeBox.

Only a small part of the Imlib2 API has been wrapped.  If you want to help by
adding more methods, patches will be happily accepted.

%prep
%setup -q -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS NEWS README TODO
%python_sitelibdir/kaa/imlib2/

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt1.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.1
- Rebuilt with python 2.6

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- new version 0.2.3 (with rpmrb script)
- cleanup spec

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- update buildreq

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.1
- initial build for ALT Linux Sisyphus

