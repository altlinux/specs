%define oname WebDAV
Name: python-module-%oname
Version: 0.4.2
Release: alt1
Summary: This library provides a WebDAV client
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/Python_WebDAV_Library/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildArch: noarch

%description
This library provides a WebDAV client including ACP and searching
support.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

