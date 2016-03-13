%define oname google-api-client

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt1.git20140913.1
Summary: Google API Client Library for Python
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/google-api-python-client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/google/google-api-python-client.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

%package docs
Summary: Documentation for Google API Client Library for Python
Group: Development/Documentation
BuildArch: noarch

%description docs
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

This package contains documentation for Google API Client Library for
Python.

%package -n python3-module-%oname
Summary: Google API Client Library for Python
Group: Development/Python3

%description -n python3-module-%oname
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

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

rm -f docs/build

%files
%doc CHANGELOG *.md
%python_sitelibdir/*

%files docs
%doc docs/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt1.git20140913.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20140913
- Initial build for Sisyphus

