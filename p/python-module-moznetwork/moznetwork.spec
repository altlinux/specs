%define oname moznetwork

%def_disable check

Name: python-module-%oname
Version: 0.24
Release: alt1
Summary: Library of network utilities for use in Mozilla testing
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/moznetwork/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mozinfo

%py_provides %oname

%description
Library of network utilities for use in Mozilla testing.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt1
- Initial build for Sisyphus

