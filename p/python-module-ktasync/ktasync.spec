%define oname ktasync

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt2.git20140614.1.1
Summary: Binary protocol of Kyoto Tycoon with asyncio for io batching
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ktasync/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ganwell/ktasync.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-trollius 
BuildPreReq: python-module-nose python-tools-pep8
BuildPreReq: pyflakes python-module-coverage
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage python3-module-nose python3-module-setuptools python3-pyflakes python3-tools-pep8
%endif

%py_provides %oname

%description
Kyoto Tycoon is a lightweight database server with impressive
performance. It can be accessed via several protocols, including an
efficient binary protocol which is used in this Python library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Kyoto Tycoon is a lightweight database server with impressive
performance. It can be accessed via several protocols, including an
efficient binary protocol which is used in this Python library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Binary protocol of Kyoto Tycoon with asyncio for io batching
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Kyoto Tycoon is a lightweight database server with impressive
performance. It can be accessed via several protocols, including an
efficient binary protocol which is used in this Python library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Kyoto Tycoon is a lightweight database server with impressive
performance. It can be accessed via several protocols, including an
efficient binary protocol which is used in this Python library.

This package contains tests for %oname.

%prep
%setup

%make cpy

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
#py.test ktasync_test.py -vv
%endif
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version ktasync_test.py -vv
popd
%endif

%if_with python2
%files
%doc *.rst docs/source/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*test.*

%files tests
%python_sitelibdir/*test.*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/source/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*test.*
%exclude %python3_sitelibdir/*/*test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*test.*
%python3_sitelibdir/*/*test.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt2.git20140614.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt2.git20140614.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 0.0.1-alt2.git20140614
- Disabled unnecessary dependents

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20140614
- Initial build for Sisyphus

