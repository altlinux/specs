%define oname metakernel

%def_with python3

Name: python-module-%oname
Version: 0.10.2
Release: alt1.git20150824
Summary: Metakernel for Jupyter
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/metakernel
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Calysto/metakernel.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests /dev/pts
BuildPreReq: python-module-nose ipython python-module-jupyter_client
BuildPreReq: python-module-ipywidgets python-module-ipcluster_tools
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
BuildPreReq: python-module-sphinx-bootstrap-theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose ipython3 python3-module-jupyter_client
BuildPreReq: python3-module-ipywidgets python3-module-ipcluster_tools
%endif

%py_provides %oname
%py_requires IPython jupyter_client ipywidgets

%description
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Metakernel for Jupyter
Group: Development/Python3
%py3_provides %oname
%py3_requires IPython jupyter_client ipywidgets

%description -n python3-module-%oname
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

This package contains pickles for %oname.

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
export PYTHONPATH=$PWD
%make_install DESTDIR=%buildroot install

%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
%make_install DESTDIR=%buildroot install3
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
#nosetests -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
#nosetests3 -vv
popd
%endif

%files
%doc *.rst examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Tue Aug 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20150824
- Initial build for Sisyphus

