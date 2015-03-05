%define oname pep257

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.alpha.git20150226
Summary: Python docstring style checker
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pep257/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/GreenSteam/pep257.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinxcontrib-issuetracker
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock
%endif

%py_provides %oname

%description
pep257 is a static analysis tool for checking compliance with Python PEP
257.

The framework for checking docstring style is flexible, and custom
checks can be easily added, for example to cover NumPy docstring
conventions.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pep257 is a static analysis tool for checking compliance with Python PEP
257.

The framework for checking docstring style is flexible, and custom
checks can be easily added, for example to cover NumPy docstring
conventions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pep257 is a static analysis tool for checking compliance with Python PEP
257.

The framework for checking docstring style is flexible, and custom
checks can be easily added, for example to cover NumPy docstring
conventions.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Python docstring style checker
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pep257 is a static analysis tool for checking compliance with Python PEP
257.

The framework for checking docstring style is flexible, and custom
checks can be easily added, for example to cover NumPy docstring
conventions.

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
py.test -vv
%if_with python3
pushd ../python3
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.alpha.git20150226
- Version 0.5.0-alpha
- Added docs

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150109
- Initial build for Sisyphus

