%define oname sphinx_rtd_theme
Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20140821
Summary: ReadTheDocs.org theme for Sphinx
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx_rtd_theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/snide/sphinx_rtd_theme.gi
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%description
This is a prototype mobile-friendly sphinx_ theme I made for
readthedocs.org_. It's currently in development and includes some rtd
variable checks that can be ignored if you're just trying to use it on
your project outside of that site.

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
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140821
- Initial build for Sisyphus

