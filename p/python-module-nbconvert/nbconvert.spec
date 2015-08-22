%define oname nbconvert

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 4.0.0
Release: alt1
Summary: Converting Jupyter Notebooks
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nbconvert
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests pandoc
BuildPreReq: python-module-mistune python-module-jinja2
BuildPreReq: python-module-Pygments python-module-traitlets-tests
BuildPreReq: python-module-jupyter_core python-module-nbformat
BuildPreReq: python-module-nose python-module-ipykernel
BuildPreReq: python-module-tornado python-module-jupyter_client
BuildPreReq: python-module-ipython_genutils-tests
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mistune python3-module-jinja2
BuildPreReq: python3-module-Pygments python3-module-traitlets-tests
BuildPreReq: python3-module-jupyter_core python3-module-nbformat
BuildPreReq: python3-module-nose python3-module-ipykernel
BuildPreReq: python3-module-tornado python3-module-jupyter_client
BuildPreReq: python3-module-ipython_genutils-tests
%endif

%py_provides %oname
%py_requires mistune jinja2 pygments traitlets jupyter_core nbformat
%py_requires tornado jupyter_client

%description
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Converting Jupyter Notebooks
Group: Development/Python3
%py3_provides %oname
%py3_requires mistune jinja2 pygments traitlets jupyter_core nbformat
%py3_requires tornado jupyter_client

%description -n python3-module-%oname
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains documentation for %oname.

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
export PATH=$PATH:%buildroot%_bindir
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
nosetests -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
nosetests3 -vv
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

