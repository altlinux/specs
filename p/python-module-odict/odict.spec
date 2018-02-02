%define oname odict

%def_with python3

Name: python-module-%oname
Version: 1.6.0
Release: alt1.dev0.git20150103.1.1.1
Summary: Ordered dictionary
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/odict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/odict.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-module-setuptools python-module-interlude
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
#BuildPreReq: python3-module-setuptools python3-module-interlude
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-interlude python-module-setuptools python3-module-interlude python3-module-pytest rpm-build-python3 time

%description
Dictionary in which the insertion order of items is preserved (using an
internal double linked list). In this implementation replacing an
existing item keeps it at its original position.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Dictionary in which the insertion order of items is preserved (using an
internal double linked list). In this implementation replacing an
existing item keeps it at its original position.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Ordered dictionary
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Dictionary in which the insertion order of items is preserved (using an
internal double linked list). In this implementation replacing an
existing item keeps it at its original position.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Dictionary in which the insertion order of items is preserved (using an
internal double linked list). In this implementation replacing an
existing item keeps it at its original position.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1.dev0.git20150103.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.0-alt1.dev0.git20150103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.dev0.git20150103.1
- NMU: Use buildreq for BR.

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.dev0.git20150103
- Version 1.6.0.dev0
- Added module for Python 3

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20140501
- Initial build for Sisyphus

