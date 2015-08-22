%define oname ipyparallel

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 4.1.0
Release: alt1.dev.git20150819
Summary: Interactive Parallel Computing with IPython
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ipyparallel
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ipython/ipyparallel.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-ipython_genutils python-module-decorator
BuildPreReq: python-module-zmq ipython python-module-nose
BuildPreReq: python-module-jupyter_client python-module-ipykernel
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-ipython_genutils python3-module-decorator
BuildPreReq: python3-module-zmq ipython3 python3-module-nose
BuildPreReq: python3-module-jupyter_client python3-module-ipykernel
%endif

%py_provides %oname
%py_requires ipython_genutils decorator zmq IPython jupyter_client
%py_requires ipykernel

%description
Use multiple instances of IPython in parallel, interactively.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Use multiple instances of IPython in parallel, interactively.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Interactive Parallel Computing with IPython
Group: Development/Python3
%py3_provides %oname
%py3_requires ipython_genutils decorator zmq IPython jupyter_client
%py3_requires ipykernel

%description -n python3-module-%oname
Use multiple instances of IPython in parallel, interactively.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Use multiple instances of IPython in parallel, interactively.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Use multiple instances of IPython in parallel, interactively.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Use multiple instances of IPython in parallel, interactively.

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
	mv $i ip-$i.py3
done
popd
%endif

%python_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ip-$i
done
popd

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
iptest2 --coverage xml ipyparallel.tests
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
iptest3 --coverage xml ipyparallel.tests
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

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/build/html

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
* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev.git20150819
- Initial build for Sisyphus

