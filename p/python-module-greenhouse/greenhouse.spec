%define oname greenhouse

%def_without python3

Name: python-module-%oname
Version: 2.2.0
Release: alt2.git20141230.1
Summary: An I/O parallelism library making use of coroutines
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/greenhouse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/teepark/greenhouse.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-greenlet
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-greenlet
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires greenlet

%description
Non-blocking IO with coroutines to mimic blocking IO with threads.

%if_with python3
%package -n python3-module-%oname
Summary: An I/O parallelism library making use of coroutines
Group: Development/Python3
%py3_provides %oname
%py3_requires greenlet

%description -n python3-module-%oname
Non-blocking IO with coroutines to mimic blocking IO with threads.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Non-blocking IO with coroutines to mimic blocking IO with threads.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Non-blocking IO with coroutines to mimic blocking IO with threads.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
python run_all_tests.py -v ||:
%if_with python3
pushd ../python3
python3 setup.py test
python3 run_all_tests.py -v ||:
popd
%endif

%files
%doc *.markdown RELEASE_NOTES examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.markdown RELEASE_NOTES examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.0-alt2.git20141230.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.git20141230
- Fixed build

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20141230
- Initial build for Sisyphus

