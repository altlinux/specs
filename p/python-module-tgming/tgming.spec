%define oname tgming
Name: python-module-%oname
Version: 0.0.7
Release: alt1
Summary: TurboGears2 Support for Ming MongoDB ORM
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/tgming/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
tgming is used by TurboGears2 to support ming backend. To create a ming
project just use quickstart command with --ming option it will
automatically setup tgming and all the required dependencies.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus

