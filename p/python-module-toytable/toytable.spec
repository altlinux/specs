%define oname toytable

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.43
Release: alt1.1
Summary: Simple in-memory tables in pure Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/toytable/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-bintrees python-module-six
#BuildPreReq: python-module-mock python-module-nose
#BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-bintrees python3-module-six
#BuildPreReq: python3-module-mock python3-module-nose
#BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires bintrees six

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-coverage python-module-nose python-module-pbr python-module-pytest python-module-unittest2 python3-module-coverage python3-module-html5lib python3-module-nose python3-module-pbr python3-module-pytest python3-module-unittest2 rpm-build-python3

%description
Toytable is a lightweight python table library. It provides a class
called Table which is suitable for representing one-dimensional tables
(e.g. time-sequences).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock nose coverage

%description tests
Toytable is a lightweight python table library. It provides a class
called Table which is suitable for representing one-dimensional tables
(e.g. time-sequences).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Simple in-memory tables in pure Python
Group: Development/Python3
%py3_provides %oname
%py3_requires bintrees six

%description -n python3-module-%oname
Toytable is a lightweight python table library. It provides a class
called Table which is suitable for representing one-dimensional tables
(e.g. time-sequences).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires mock nose coverage

%description -n python3-module-%oname-tests
Toytable is a lightweight python table library. It provides a class
called Table which is suitable for representing one-dimensional tables
(e.g. time-sequences).

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/toytable_tests

%files tests
%python_sitelibdir/toytable_tests

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/toytable_tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/toytable_tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.43-alt1.1
- NMU: Use buildreq for BR.

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.43-alt1
- Initial build for Sisyphus

