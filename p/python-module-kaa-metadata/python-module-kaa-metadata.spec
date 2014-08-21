%define oname kaa-metadata

%def_without python3

Name: python-module-%oname
Version: 0.7.8
Release: alt1.git20130624

Summary: Module for retrieving information about media files

License: GPL
Group: Development/Python
Url: http://freevo.org/kaa

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname
%add_python_req_skip disc

Source: %name-%version.tar

BuildRequires: libdvdread-devel python-module-kaa-base python-module-PyXML
BuildPreReq: python-module-sphinx-devel libexiv2-devel gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
BuildPreReq: python3-module-kaa-base
%endif

%description
libxml2 and its python bindings.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
libxml2 and its python bindings.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
libxml2 and its python bindings.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Module for retrieving information about media files
Group: Development/Python3

%description -n python3-module-%oname
libxml2 and its python bindings.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc html
%make -C doc pickle

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/.build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS NEWS README TODO
%_bindir/mminfo
%python_sitelibdir/kaa/metadata/
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS README TODO
#%_bindir/mminfo.py3
%python3_sitelibdir/kaa/metadata/
%endif

%changelog
* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.8-alt1.git20130624
- Version 0.7.8

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

