%define oname sphinx_py3doc_enhanced_theme
Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20141014
Summary: A theme based on the theme of https://docs.python.org/3/
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx_py3doc_enhanced_theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionelmc/sphinx-py3doc-enhanced-theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%py_provides %oname

%description
A theme based on the theme of https://docs.python.org/3/ .

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141014
- Initial build for Sisyphus

