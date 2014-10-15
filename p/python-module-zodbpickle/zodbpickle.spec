%define oname zodbpickle

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.2
Release: alt1.git20130817
Summary: Fork of Python 3 pickle module
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zodbpickle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zodbpickle.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-coverage
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%add_findreq_skiplist %python_sitelibdir/%oname/pickle_3.py
%add_findreq_skiplist %python_sitelibdir/%oname/pickletools_3.py
%add_findreq_skiplist %python_sitelibdir/%oname/tests/pickletester_3.py

%description
This package presents a uniform pickling interface for ZODB.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip test

%description tests
This package presents a uniform pickling interface for ZODB.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Fork of Python 3 pickle module
Group: Development/Python3
%py3_provides %oname
%add_findreq_skiplist %python3_sitelibdir/%oname/pickle_2.py
%add_findreq_skiplist %python3_sitelibdir/%oname/pickletools_2.py
%add_findreq_skiplist %python3_sitelibdir/%oname/tests/pickletester_2.py

%description -n python3-module-%oname
This package presents a uniform pickling interface for ZODB.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip __main__

%description -n python3-module-%oname-tests
This package presents a uniform pickling interface for ZODB.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
for i in $(find ../python3 -type f -name '*.py'); do
	2to3 -w -n $i ||:
done
%endif

%build
%add_optflags -fno-strict-aliasing
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20130817
- Initial build for Sisyphus

