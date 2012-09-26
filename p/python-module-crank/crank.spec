%define oname crank
Name: python-module-%oname
Version: 0.6.4
Release: alt1
Summary: Generalization of dispatch mechanism for use across frameworks
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/crank/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Generalization of dispatch mechanism for use across frameworks.

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
* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus

