%define oname lcms

%def_with python3

Name: python-module-lcms
Version: 1.19
Release: alt1.1

Summary: Python binding for little cms color engine

License: LGPL
Group: System/Libraries
Url: http://www.littlecms.com
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %url/%oname-%version.tar.bz2
Patch: %name.patch
Patch1: lcms-1.19-alt-python3.patch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libstdc++-devel python-base python-modules python-modules-compiler python-modules-encodings python-modules-logging python3 python3-base swig-data
BuildRequires: gcc-c++ libjpeg-devel liblcms-devel libtiff-devel python-devel python-tools-2to3 python3-devel rpm-build-python3 swig time zlib-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
%endif

%description
This package contains the python binding for
CMM engine to deal with color management stuff.

%package -n python3-module-%oname
Summary: Python binding for little cms color engine
Group: Development/Python3

%description -n python3-module-%oname
This package contains the python binding for
CMM engine to deal with color management stuff.

%prep
%setup -n %oname-%version
%patch

%if_with python3
cp -fR . ../python3
pushd ../python3
%patch1 -p2
popd
%endif

%build
pushd python
rm -f lcms.py lcms_wrap.cxx
swig -python -c++ -I../include lcms.i
cd ..
%autoreconf
%configure --with-python --disable-static
popd

pushd python
%make_build
popd

%if_with python3
export PYTHON=%_bindir/python3
pushd ../python3
pushd python
rm -f lcms.py lcms_wrap.cxx
swig -python -py3 -c++ -I../include lcms.i
cd ..
sed -i 's|\$(PYTHON_VERSION)|%_python3_version%_python3_abiflags|' \
	python/Makefile.am
%autoreconf
sed -i \
	's|am_cv_pathless_PYTHON in python|am_cv_pathless_PYTHON in python3|' \
	configure
%configure --with-python --disable-static
popd

pushd python
%make_build
popd
popd
%endif

%install
pushd python
%makeinstall_std
rm -f %buildroot%python_sitelibdir/_lcms.{a,la}
popd

%if_with python3
pushd ../python3/python
%makeinstall_std
rm -f %buildroot%python3_sitelibdir/_lcms.{a,la}
popd
2to3 -w -n %buildroot%python3_sitelibdir/lcms.py
%endif

%files
%doc AUTHORS NEWS README*
%python_sitelibdir/_lcms.so
%python_sitelibdir/lcms.py*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS README*
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.19-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.19-alt1
- Version 1.19
- Added module for Python 3

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
