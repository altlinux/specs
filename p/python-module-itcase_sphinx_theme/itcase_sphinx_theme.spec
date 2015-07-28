%define oname itcase_sphinx_theme
Name: python-module-%oname
Version: 0.1.8
Release: alt1.git20150723
Summary: ITCase Sphinx themes for documentation styling
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/itcase-sphinx-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ITCase/itcase_sphinx_theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json

%py_provides %oname

%description
ITCase Sphinx themes for documentation styling.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.git20150723
- Initial build for Sisyphus

