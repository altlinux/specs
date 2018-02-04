%define oname pybill

%def_without python3

Name: python-module-%oname
Version: 1.1.0
Release: alt2.1
Summary: PDF formatting tool for bills
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pybill/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Reportlab python-module-lxml
BuildPreReq: python-module-logilab-common
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Reportlab python3-module-lxml
BuildPreReq: python3-module-logilab-common python-tools-2to3
%endif

%py_provides %oname
%py_requires logilab.common

%description
PyBill is Logilab tool used to produce PDF documents from XML files
describing bills, debits, downpayments, claim forms or pro-formas.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
PyBill is Logilab tool used to produce PDF documents from XML files
describing bills, debits, downpayments, claim forms or pro-formas.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PyBill is Logilab tool used to produce PDF documents from XML files
describing bills, debits, downpayments, claim forms or pro-formas.

This package contains documentation for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: PDF formatting tool for bills
Group: Development/Python3
%py3_provides %oname
%py3_requires logilab.common

%description -n python3-module-%oname
PyBill is Logilab tool used to produce PDF documents from XML files
describing bills, debits, downpayments, claim forms or pro-formas.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
PyBill is Logilab tool used to produce PDF documents from XML files
describing bills, debits, downpayments, claim forms or pro-formas.

This package contains tests for %oname.
%endif

%prep
%setup

%prepare_sphinx doc
ln -s ../objects.inv doc/dev-manual/
ln -s ../objects.inv doc/user-manual/

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

export PYTHONPATH=$PWD/build/lib
%make -C doc/dev-manual html
%make -C doc/user-manual html

mv doc/dev-manual/_build/html dev-manual
mv doc/user-manual/_build/html user-manual

install -d %buildroot%_man1dir
install -p -m644 man/* %buildroot%_man1dir/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog README
%_bindir/*
%_man1dir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%files docs
%doc dev-manual user-manual examples configs

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Fixed build

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

