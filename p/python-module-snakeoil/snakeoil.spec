%define oname snakeoil

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.git20150323.1.1
Summary: Misc common functionality and useful optimizations
License: BSD & GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/snakeoil/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pkgcore/snakeoil.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools /dev/pts
BuildPreReq: python-module-coverage
BuildPreReq: python-modules-logging python-modules-xml
BuildPreReq: python-modules-multiprocessing python-modules-curses
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-coverage python3-modules-curses
%endif

%py_provides %oname
%py_requires logging xml multiprocessing curses

%description
snakeoil is a python library that implements optimized versions of
common python functionality. Some classes and functions have cpython
equivalents, but they all have native python implementations too.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
snakeoil is a python library that implements optimized versions of
common python functionality. Some classes and functions have cpython
equivalents, but they all have native python implementations too.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Misc common functionality and useful optimizations
Group: Development/Python3
BuildArch: noarch
%py3_provides %oname
%py3_requires curses

%description -n python3-module-%oname
snakeoil is a python library that implements optimized versions of
common python functionality. Some classes and functions have cpython
equivalents, but they all have native python implementations too.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
snakeoil is a python library that implements optimized versions of
common python functionality. Some classes and functions have cpython
equivalents, but they all have native python implementations too.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' '{}' +
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

find . -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/python3|#!/usr/bin/python|' '{}' +

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
find %buildroot%python3_sitelibdir_noarch -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/python33|#!/usr/bin/python3|' '{}' +
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS COPYING *.rst doc/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS COPYING *.rst doc/*.rst
%python3_sitelibdir_noarch/*
%exclude %python3_sitelibdir_noarch/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir_noarch/*/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.git20150323.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20150323.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150323
- Initial build for Sisyphus

