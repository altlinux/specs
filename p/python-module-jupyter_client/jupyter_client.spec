%define oname jupyter_client

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 4.0.0
Release: alt1
Summary: Jupyter protocol implementation and client libraries
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jupyter_client
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-traitlets python-module-jupyter_core
BuildPreReq: python-module-zmq-tests python-module-ipython_genutils-tests
BuildPreReq: python-module-nose
#BuildPreReq: python-module-ipykernel
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-traitlets python3-module-jupyter_core
BuildPreReq: python3-module-zmq-tests python3-module-ipython_genutils-tests
BuildPreReq: python3-module-nose
#BuildPreReq: python3-module-ipykernel
%endif

%py_provides %oname
%py_requires traitlets jupyter_core zmq

%description
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Jupyter protocol implementation and client libraries
Group: Development/Python3
%py3_provides %oname
%py3_requires traitlets jupyter_core zmq

%description -n python3-module-%oname
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

