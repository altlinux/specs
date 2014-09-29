%define oname pyfactory

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1.git20130326
Summary: Generic model factory framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyfactory/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kiip/pyfactory.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
PyFactory is a library for writing generic model factories useful for
unit testing.

%package -n python3-module-%oname
Summary: Generic model factory framework
Group: Development/Python3

%description -n python3-module-%oname
PyFactory is a library for writing generic model factories useful for
unit testing.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
PyFactory is a library for writing generic model factories useful for
unit testing.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PyFactory is a library for writing generic model factories useful for
unit testing.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CHANGELOG *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20130326
- Initial build for Sisyphus

