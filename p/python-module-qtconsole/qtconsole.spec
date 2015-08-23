%define oname qtconsole

%def_with python3

Name: python-module-%oname
Version: 4.0.1
Release: alt1
Summary: Jupyter Qt console
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/qtconsole
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests xvfb-run
BuildPreReq: python-module-traitlets-tests python-module-jupyter_core
BuildPreReq: python-module-jupyter_client python-module-Pygments
BuildPreReq: python-module-ipykernel python-module-mock
BuildPreReq: python-module-pexpect python-module-PyQt4
BuildPreReq: python-module-ipython_genutils-tests python-module-nose
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-traitlets-tests python3-module-jupyter_core
BuildPreReq: python3-module-jupyter_client python3-module-Pygments
BuildPreReq: python3-module-ipykernel python3-module-mock
BuildPreReq: python3-module-pexpect python3-module-PyQt4
BuildPreReq: python3-module-ipython_genutils-tests python3-module-nose
%endif

%py_provides %oname
%py_requires traitlets jupyter_core jupyter_client pygments ipykernel

%description
Qt-based console for Jupyter with support for rich media output.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Qt-based console for Jupyter with support for rich media output.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Jupyter Qt console
Group: Development/Python3
%py3_provides %oname
%py3_requires traitlets jupyter_core jupyter_client pygments ipykernel

%description -n python3-module-%oname
Qt-based console for Jupyter with support for rich media output.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Qt-based console for Jupyter with support for rich media output.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
export PYTHONPATH=$PWD
xvfb-run nosetests -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
xvfb-run nosetests3 -vv
popd
%endif

%files
%doc *.md docs/build/html
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
%doc *.md docs/build/html
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus

