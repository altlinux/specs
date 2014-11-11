%define oname sphinx-bootstrap-theme
Name: python-module-%oname
Version: 0.4.3
Release: alt1
Summary: Sphinx Bootstrap Theme
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-bootstrap-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%py_requires sphinx Fabric

%description
This Sphinx theme integrates the Twitter Bootstrap CSS / JavaScript
framework with various layout options, hierarchical menu navigation, and
mobile-friendly responsive design. It is configurable, extensible and
can use any number of different Bootswatch CSS themes.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt *.rst
%python_sitelibdir/*

%changelog
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1
- VErsion 0.4.3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

