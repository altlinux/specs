%define oname moznetwork

Name: python-module-%oname
Version: 0.24
Release: alt2.1
Summary: Library of network utilities for use in Mozilla testing
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/moznetwork/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt2
- Enabled testing

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt1
- Initial build for Sisyphus

