%define oname kotti_docs_theme
Name: python-module-%oname
Version: 0.3
Release: alt1.dev.git20130511
Summary: Sphinx Theme for Kotti Documentation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_docs_theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kotti/kotti_docs_theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%description
This theme is based on sphinx-bootstrap by Scotch Media and modified for
documentation of Kotti and Kotti add-ons.

%prep
%setup

%build
%python_build_debug

%install
%python_install

cp -fR %oname/themes %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20130511
- Initial build for Sisyphus

