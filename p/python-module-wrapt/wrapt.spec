%define oname wrapt

%def_with python3

Name: python-module-%oname
Version: 1.9.0
Release: alt1.git20140822
Summary: A Python module for decorators, wrappers and monkey patching
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/wrapt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/GrahamDumpleton/wrapt.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tox
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tox
%endif

%py_provides %oname

%description
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%package -n python3-module-%oname
Summary: A Python module for decorators, wrappers and monkey patching
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
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

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
popd
%endif

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html blog

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.git20140822
- Initial build for Sisyphus

