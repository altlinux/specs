%define oname tarjan

%def_with python3

Name: python-module-%oname
Version: 0.2.1.3
Release: alt1.git20140805.1.1
Summary: Implementation of Tarjan's algorithm: resolve cyclic deps
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/tarjan/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bwesterb/py-tarjan.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Tarjan's algorithm takes as input a directed (possibly cyclic!) graph
and returns as output its strongly connected components in a topological
order.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Tarjan's algorithm takes as input a directed (possibly cyclic!) graph
and returns as output its strongly connected components in a topological
order.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Implementation of Tarjan's algorithm: resolve cyclic deps
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Tarjan's algorithm takes as input a directed (possibly cyclic!) graph
and returns as output its strongly connected components in a topological
order.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Tarjan's algorithm takes as input a directed (possibly cyclic!) graph
and returns as output its strongly connected components in a topological
order.

This package contains tests for %oname.

%prep
%setup

sed -i 's|@VERSION@|%version|' setup.py

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
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 setup.py test
popd
%endif

%files
%doc *.md doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1.3-alt1.git20140805.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1.3-alt1.git20140805.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1.3-alt1.git20140805
- Initial build for Sisyphus

