%define oname ipykernel

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 4.0.3
Release: alt2
Summary: IPython Kernel for Jupyter
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ipykernel
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-traitlets ipython python-module-nose
BuildPreReq: python-module-jupyter_client python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-traitlets ipython3 python3-module-nose
BuildPreReq: python3-module-jupyter_client python3-module-mock
%endif

%py_provides %oname
%py_requires IPython traitlets jupyter_client

%description
This package provides the IPython kernel for Jupyter.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides the IPython kernel for Jupyter.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: IPython Kernel for Jupyter
Group: Development/Python3
%py3_provides %oname
%py3_requires IPython traitlets jupyter_client
%add_python3_req_skip gtk

%description -n python3-module-%oname
This package provides the IPython kernel for Jupyter.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package provides the IPython kernel for Jupyter.

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
rm -fR build
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Enabled check

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus

