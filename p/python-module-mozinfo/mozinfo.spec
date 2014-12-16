%define oname mozinfo

Name: python-module-%oname
Version: 0.7
Release: alt2
Summary: Library to get system information for use in Mozilla testing
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozinfo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mozfile python-modules-json

%py_provides %oname

%description
Library to get system information for use in Mozilla testing.

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
%_bindir/*
%python_sitelibdir/*

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Added necessary requirements
- Enabled testing

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

