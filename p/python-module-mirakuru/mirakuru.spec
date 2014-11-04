%define oname mirakuru

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20141013
Summary: Process executor for tests
License: LGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/mirakuru/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ClearcodeHQ/mirakuru.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pytest-cov python-module-mock
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest-cov python3-module-mock
%endif

%py_provides %oname

%description
Maybe you want to be able to start database only when you start your
program, or maybe you need just to set up additional processes for your
tests, this is where you should consider using mirakuru, to add
superpowers to your program, or tests.

%package -n python3-module-%oname
Summary: Process executor for tests
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Maybe you want to be able to start database only when you start your
program, or maybe you need just to set up additional processes for your
tests, this is where you should consider using mirakuru, to add
superpowers to your program, or tests.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Maybe you want to be able to start database only when you start your
program, or maybe you need just to set up additional processes for your
tests, this is where you should consider using mirakuru, to add
superpowers to your program, or tests.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Maybe you want to be able to start database only when you start your
program, or maybe you need just to set up additional processes for your
tests, this is where you should consider using mirakuru, to add
superpowers to your program, or tests.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
touch tests/__init__.py
python setup.py test
%if_with python3
pushd ../python3
touch tests/__init__.py
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141013
- Initial build for Sisyphus

