%define oname lcms

Name: python-module-lcms
Version: 1.18
Release: alt1.2.1

Summary: Python binding for little cms color engine

License: LGPL
Group: System/Libraries
Url: http://www.littlecms.com
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %url/%oname-%version.tar.bz2
Patch: %name.patch

# Automatically added by buildreq on Thu Feb 21 2008
BuildRequires: gcc-c++ glibc-devel libjpeg-devel liblcms-devel libtiff-devel python-devel swig zlib-devel

%description
This package contains the python binding for
CMM engine to deal with color management stuff.

%prep
%setup -n %oname-%version
%patch

%build
cd python
rm -f lcms.py lcms_wrap.cxx
swig -python -c++ -I../include lcms.i
cd ..
%autoreconf
%configure --with-python --disable-static

cd python
%make_build

%install
cd python
%makeinstall_std
rm -f %buildroot%python_sitelibdir/_lcms.{a,la}

%files
%doc AUTHORS NEWS README*
%python_sitelibdir/_lcms.so
%python_sitelibdir/lcms.py*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.18-alt1.2.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt1.2
- Rebuilt for debuginfo

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt1.1
- Rebuilt with python 2.6

* Tue Mar 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt1
- new version 1.18 (with rpmrb script)

* Thu Feb 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt2
- rebuild with python 2.5
- regenerate swig file, update buildreq

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt1
- initial build for ALT Linux Sisyphus
