%define oname sigtools

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.b1.git20150111
Summary: Python module to manipulate function signatures
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sigtools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/epsy/sigtools.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-funcsigs
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-funcsigs
%endif

%py_provides %oname
%py_requires six funcsigs

%description
Utilities for working with 3.3's inspect.Signature objects.
The sigtools python library provides:

* Decorators to specify keyword-only parameters, annotations and
  positional-only parameters, even on python2: sigtools.modifiers
* Decorators to specify how *args, **kwargs are handled, in a way that
  can be introspected: sigtools.specifiers
* Function combination routines that preserve signatures:
  sigtools.wrappers
* Functions to manipulate signature objects likewise: sigtools.signatures

%package -n python3-module-%oname
Summary: Python module to manipulate function signatures
Group: Development/Python3
%py3_provides %oname
%py3_requires six funcsigs

%description -n python3-module-%oname
Utilities for working with 3.3's inspect.Signature objects.
The sigtools python library provides:

* Decorators to specify keyword-only parameters, annotations and
  positional-only parameters, even on python2: sigtools.modifiers
* Decorators to specify how *args, **kwargs are handled, in a way that
  can be introspected: sigtools.specifiers
* Function combination routines that preserve signatures:
  sigtools.wrappers
* Functions to manipulate signature objects likewise: sigtools.signatures

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst*
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b1.git20150111
- Initial build for Sisyphus

