%define oname google-api-client

%def_with python3

Name: python-module-%oname
Version: 1.6.6
Release: alt1
Summary: Google API Client Library for Python
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/google-api-python-client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/google/google-api-python-client.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-httplib2 >= 0.8
BuildRequires: python-module-oauth2client >= 1.4.6
BuildRequires: python-module-six >= 1.6.1
BuildRequires: python-module-uritemplate >= 0.6

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-httplib2 >= 0.8
BuildRequires: python3-module-oauth2client >= 1.4.6
BuildRequires: python3-module-six >= 1.6.1
BuildRequires: python3-module-uritemplate >= 0.6
#BuildRequires: python-tools-2to3
%endif

%add_python_req_skip google.appengine.api
%add_python3_req_skip google.appengine.api

%description
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

%package docs
Summary: Documentation for Google API Client Library for Python
Group: Development/Documentation

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
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
* Thu Mar 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.6-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.5-alt1
- New version.

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt1.git20140913.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20140913
- Initial build for Sisyphus

