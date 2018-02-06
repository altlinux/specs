%define oname zodbpickle

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 0.6.1
Release: alt1.dev0.git20150414.1.1.1
Summary: Fork of Python 3 pickle module
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zodbpickle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zodbpickle.git
Source: %name-%version.tar

#BuildPreReq: python-module-setuptools
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-coverage
#BuildPreReq: python-test
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose
#BuildPreReq: python3-module-coverage
#BuildPreReq: python3-test
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%add_findreq_skiplist %python_sitelibdir/%oname/pickle_3.py
%add_findreq_skiplist %python_sitelibdir/%oname/pickletools_3.py
%add_findreq_skiplist %python_sitelibdir/%oname/tests/pickletester_3.py

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-coverage python-module-nose python-module-setuptools python-test python3-devel python3-module-coverage python3-module-nose python3-module-pytest rpm-build-python3 time

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
#if_with python3
%if 0
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.dev0.git20150414.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.dev0.git20150414.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1.dev0.git20150414.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.dev0.git20150414
- Version 0.6.1.dev0
- Enabled check

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20130817
- Initial build for Sisyphus

