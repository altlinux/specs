%define oname jupyter_console

%def_with python3

Name: python-module-%oname
Version: 4.1.0
Release: alt1.dev.git20150812.1
Summary: Jupyter Terminal Console
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jupyter_console
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jupyter/jupyter_console.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests /dev/pts
BuildPreReq: python-module-jupyter_client ipython
BuildPreReq: python-module-ipykernel python-module-mock
BuildPreReq: python-module-pexpect python-module-nose
BuildPreReq: python-module-coverage python-module-traitlets-tests
BuildPreReq: python-module-ipython_genutils-tests
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jupyter_client ipython3
BuildPreReq: python3-module-ipykernel python3-module-mock
BuildPreReq: python3-module-pexpect python3-module-nose
BuildPreReq: python3-module-coverage python3-module-traitlets-tests
BuildPreReq: python3-module-ipython_genutils-tests
%endif

%py_provides %oname
%py_requires jupyter_client IPython ipykernel

%description
A terminal-based console frontend for Jupter kernels. This code is based
on the single-process IPython terminal.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A terminal-based console frontend for Jupter kernels. This code is based
on the single-process IPython terminal.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Jupyter Terminal Console
Group: Development/Python3
%py3_provides %oname
%py3_requires jupyter_client IPython ipykernel

%description -n python3-module-%oname
A terminal-based console frontend for Jupter kernels. This code is based
on the single-process IPython terminal.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A terminal-based console frontend for Jupter kernels. This code is based
on the single-process IPython terminal.

This package contains tests for %oname.
%endif

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

export PYTHONPATH=$PWD
%make -C docs html

%check
nosetests -vv --with-coverage --cover-package=%oname %oname
%if_with python3
pushd ../python3
nosetests3 -vv --with-coverage --cover-package=%oname %oname
popd
%endif

%files
%doc *.md docs/_build/html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/_build/html
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.dev.git20150812.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev.git20150812
- Initial build for Sisyphus

