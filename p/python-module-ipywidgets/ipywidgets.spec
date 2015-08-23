%define oname ipywidgets

%def_with python3

Name: python-module-%oname
Version: 4.0.2
Release: alt1
Summary: IPython HTML widgets for Jupyter
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ipywidgets
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests ipython
BuildPreReq: python-module-ipykernel python-module-traitlets-tests
BuildPreReq: python-module-notebook python-module-mock
BuildPreReq: python-module-nose python-module-ipython_genutils-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests ipython3
BuildPreReq: python3-module-ipykernel python3-module-traitlets-tests
BuildPreReq: python3-module-notebook python3-module-mock
BuildPreReq: python3-module-nose python3-module-ipython_genutils-tests
%endif

%py_provides %oname
%py_requires IPython ipykernel traitlets notebook

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: IPython HTML widgets for Jupyter
Group: Development/Python3
%py3_provides %oname
%py3_requires IPython ipykernel traitlets notebook

%description -n python3-module-%oname
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

This package contains tests for %oname.
%endif

%package examples
Summary: Examples for %oname
Group: Development/Documentation
BuildArch: noarch

%description examples
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

This package contains examples for %oname.

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
nosetests -vv
%if_with python3
pushd ../python3
nosetests3 -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%files examples
%doc examples/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus

