%define oname uuid
Name: python-module-%oname
Version: 1.30
Release: alt1
Summary: UUID object and generation functions
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/uuid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%py_provides %oname

%description
UUID object and generation functions.

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
* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.30-alt1
- Initial build for Sisyphus

