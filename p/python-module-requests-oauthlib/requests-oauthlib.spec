%define oname requests-oauthlib

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20140606
Summary: OAuthlib authentication support for Requests
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-oauthlib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/requests/requests-oauthlib.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-oauthlib
BuildPreReq: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires oauthlib.common requests.compat

%description
This project provides first-class OAuth library support for Requests.

%package -n python3-module-%oname
Summary: OAuthlib authentication support for Requests
Group: Development/Python3
%py3_requires oauthlib.common requests.compat

%description -n python3-module-%oname
This project provides first-class OAuth library support for Requests.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This project provides first-class OAuth library support for Requests.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This project provides first-class OAuth library support for Requests.

This package contains documentation for %oname.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140606
- Initial build for Sisyphus

