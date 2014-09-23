%define oname instagram

Name: python-module-%oname
Version: 1.1.3
Release: alt1.git20140805
Summary: Instagram API client
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-instagram/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Instagram/python-instagram.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
Python Client for Instagram API
http://instagram.com/developers/

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.md
%python_sitelibdir/*

%changelog
* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20140805
- Initial build for Sisyphus

