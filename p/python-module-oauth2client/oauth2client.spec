%define oname oauth2client

Name: python-module-%oname
Version: 1.2
Release: alt1

Summary: OAuth 2.0 client library
License: Apache Software License
Group: Development/Python

Url: https://pypi.python.org/pypi/oauth2client/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-distribute

%setup_python_module %oname

%description
The oauth2client is a client library for OAuth 2.0.

%prep
%setup

%build
%python_build_debug
   
%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

