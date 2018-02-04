%define oname proteus

%def_without python3

Name: python-module-%oname
Version: 4.4.0
Release: alt1.1
Summary: Library to access Tryton server as a client
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/proteus/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: graphviz
BuildRequires: python-module-setuptools python-module-dateutil
BuildRequires: python-module-trytond-tests python-module-simplejson
BuildRequires: python-module-cdecimal python-modules-sqlite3
BuildRequires: python-module-pydot python-module-pygraphviz
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-dateutil
BuildRequires: python3-module-trytond-tests python3-module-simplejson
BuildRequires: python3-module-cdecimal python3-modules-sqlite3
BuildRequires: python3-module-pydot python3-module-pygraphviz
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
A library to access Tryton's models like a client.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A library to access Tryton's models like a client.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Library to access Tryton server as a client
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A library to access Tryton's models like a client.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description -n python3-module-%oname-tests
A library to access Tryton's models like a client.

This package contains tests for %oname.
%endif

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
export PYTHONPATH=$PWD
py.test -vv

%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test3 -vv
popd
%endif

%files
%doc CHANGELOG README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt1
- Updated to upstream release 4.4.0.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

