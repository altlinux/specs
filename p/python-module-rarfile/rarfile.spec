%define oname rarfile

%def_with python3

Name: python-module-%oname
Version: 2.7
Release: alt1.git20141123
Summary: RAR archive reader for Python
License: ISC
Group: Development/Python
Url: https://pypi.python.org/pypi/rarfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/markokr/rarfile.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests pylint
BuildPreReq: python-module-pycrypto
BuildPreReq: python-module-sphinx-devel unrar
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests pylint-py3
BuildPreReq: python3-module-pycrypto
%endif

%py_provides %oname
Requires: unrar
%py_requires Crypto

%description
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

%package -n python3-module-%oname
Summary: RAR archive reader for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires Crypto

%description -n python3-module-%oname
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
pushd test
./test1.sh python
./test2.sh python
popd
%if_with python3
pushd ../python3
pushd test
./test1.sh python3
./test2.sh python3
popd
popd
%endif

%files
%doc LICENSE *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20141123
- Initial build for Sisyphus

