%define oname django-facebook-utils

%def_with python3

Name: python-module-%oname
Version: 1.0.4
Release: alt1.git20130201
Summary: Some Facebook utilities to use in Django projects
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook-utils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/caioariede/django-facebook-utils.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
The intent of this project is to provide some very basic utilities
related to Facebook.

At the moment there are only two features:

* An utility that forces the update of an URL in the Facebook's share
  cache.
* A Context Processor that allows you to hide Facebook Open Graph
  Protocol <meta> tags from other User Agents.

%package -n python3-module-%oname
Summary: Some Facebook utilities to use in Django projects
Group: Development/Python3

%description -n python3-module-%oname
The intent of this project is to provide some very basic utilities
related to Facebook.

At the moment there are only two features:

* An utility that forces the update of an URL in the Facebook's share
  cache.
* A Context Processor that allows you to hide Facebook Open Graph
  Protocol <meta> tags from other User Agents.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files
%doc README.markdown example
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.markdown example
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20130201
- Initial build for Sisyphus

