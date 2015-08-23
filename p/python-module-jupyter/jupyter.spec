%define oname jupyter

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Jupyter metapackage. Install all the Jupyter components in one go.
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jupyter
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-notebook python-module-qtconsole
BuildPreReq: python-module-jupyter_console python-module-nbconvert
BuildPreReq: python-module-ipykernel python-module-ipywidgets
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-notebook python3-module-qtconsole
BuildPreReq: python3-module-jupyter_console python3-module-nbconvert
BuildPreReq: python3-module-ipykernel python3-module-ipywidgets
%endif

%py_provides %oname
%py_requires notebook qtconsole jupyter_console nbconvert ipykernel
%py_requires ipywidgets

%description
Install the Jupyter system, including the notebook, qtconsole, and the
IPython kernel.

%if_with python3
%package -n python3-module-%oname
Summary: Jupyter metapackage. Install all the Jupyter components in one go.
Group: Development/Python3
%py3_provides %oname
%py3_requires notebook qtconsole jupyter_console nbconvert ipykernel
%py3_requires ipywidgets

%description -n python3-module-%oname
Install the Jupyter system, including the notebook, qtconsole, and the
IPython kernel.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Install the Jupyter system, including the notebook, qtconsole, and the
IPython kernel.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Install the Jupyter system, including the notebook, qtconsole, and the
IPython kernel.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python jupyter.py --version
%if_with python3
pushd ../python3
python3 jupyter.py --version
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

