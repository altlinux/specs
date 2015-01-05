%define oname sphinx-readable-theme
Name: python-module-%oname
Version: 1.1.0
Release: alt1.git20140325
Summary: Sphinx Readable Theme
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-readable-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ignacysokolowski/sphinx-readable-theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-sphinx python-module-setuptools-tests

%py_provides sphinx_readable_theme

%description
A clean and readable Sphinx theme with focus on autodoc -- documentation
from docstrings.

Inspired by flask-sphinx-themes.

%prep
%setup

%build
%python_build_debug

%install
%python_install

rm -f docs/source/conf.py

%check
python setup.py test

%files
%doc *.rst docs/source/*
%python_sitelibdir/*

%changelog
* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20140325
- Initial build for Sisyphus

