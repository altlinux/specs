%define oname ktasync

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20140614
Summary: Binary protocol of Kyoto Tycoon with asyncio for io batching
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ktasync/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ganwell/ktasync.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-trollius python-module-pylama
BuildPreReq: python-module-nose python-tools-pep8
BuildPreReq: pyflakes pylint python-module-coverage
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-pylama
BuildPreReq: python3-module-nose python3-tools-pep8
BuildPreReq: python3-pyflakes pylint-py3 python3-module-coverage
%endif

%py_provides %oname
%py_requires trollius

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
%py3_requires asyncio

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
* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20140614
- Initial build for Sisyphus

