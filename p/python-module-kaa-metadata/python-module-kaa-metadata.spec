%define oname kaa-metadata
Name: python-module-%oname
Version: 0.7.5
Release: alt2.1.1

Summary: Module for retrieving information about media files

License: GPL
Group: Development/Python
Url: http://freevo.org/kaa

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname
%add_python_req_skip disc

Source: http://prdownloads.sf.net/freevo/%oname-%version.tar.bz2

BuildPreReq: rpm-build-compat >= 1.2

# Automatically added by buildreq on Sat May 26 2007
BuildRequires: libdvdread-devel python-module-kaa-base python-module-PyXML

%description
libxml2 and its python bindings

%prep
%setup -q -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS NEWS README TODO
#%_bindir/mminfo
%python_sitelibdir/kaa/metadata/

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.5-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.5-alt2.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt2
- Rebuilt with python 2.6

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.5-alt1.1
- rebuild with libdvdread.so.4

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- new version 0.7.5 (with rpmrb script)

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.1
- initial build for ALT Linux Sisyphus

