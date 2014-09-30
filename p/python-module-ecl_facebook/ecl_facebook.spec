%define oname ecl_facebook
Name: python-module-%oname
Version: 1.4.1
Release: alt1.git20121214
Summary: Easy Facebook integration for Django
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ecl_facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/elmcitylabs/ECL-Facebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools python-modules-json

%description
ECL Facebook is a Facebook library for Python 2.7+. It makes the
Facebook API a joy to use and has built-in integration for Django and
Flask.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%changelog
* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20121214
- Initial build for Sisyphus

