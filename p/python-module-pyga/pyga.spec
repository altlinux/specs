%define oname pyga

%def_with python3

Name: python-module-%oname
Version: 2.5.0
Release: alt1.git20140809
Summary: Server side implemenation of Google Analytics in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyga/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kra3/py-ga-mob.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python-tools-2to3
%endif

%py_provides %oname

%description
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

%package -n python3-module-%oname
Summary: Server side implemenation of Google Analytics in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

This package contains documentation for %oname.

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

%make -C doc pickle
mkdir -p build/docs
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst RELEASES
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst RELEASES
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20140809
- Initial build for Sisyphus

