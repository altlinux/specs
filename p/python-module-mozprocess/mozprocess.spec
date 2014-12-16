%define oname mozprocess
Name: python-module-%oname
Version: 0.21
Release: alt1
Summary: Mozilla-authored process handling
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/mozprocess/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mozinfo

%py_provides %oname

%description
Mozilla-authored process handling.

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
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21-alt1
- Initial build for Sisyphus

