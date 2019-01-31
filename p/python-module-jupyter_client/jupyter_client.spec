%define oname jupyter_client

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 5.1.0
Release: alt2
Summary: Jupyter protocol implementation and client libraries
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jupyter_client

Source: %name-%version.tar
Patch1: jupyter_client-5.1.0-tornado-5-support.patch
Patch2: jupyter_client-5.1.0-disable-pyzmq-zero-copy-optimizations-during-session.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-html5lib python-module-ipython_genutils-tests python-module-mock
BuildRequires: python-module-notebook python-module-objects.inv python-module-pytest python-module-zmq-tests
BuildRequires: python-module-sphinx_rtd_theme python-module-pathlib2

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-ipython_genutils-tests python3-module-notebook python3-module-pbr
BuildRequires: python3-module-unittest2 python3-module-zmq-tests python3-module-pytest
BuildRequires: python3-module-sphinx_rtd_theme python3-module-pathlib2
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
%patch1 -p1
%patch2 -p1

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
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%if_enabled check
%check
rm -fR build
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
export PYTHONPATH=$PWD
py.test3 -vv
popd
%endif
%endif

%files
%doc *.md
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
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 30 2019 Stanislav Levin <slev@altlinux.org> 5.1.0-alt2
- Applied upstream patches for Tornado5 support.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.0-alt1
- Updated to upstream release 5.1.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Enabled check

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

