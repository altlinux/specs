%define oname sphinx-better-theme
Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20131011
Summary: A nice-looking, customizable theme for Sphinx
License: BSD
Group: Development/Python
Url: https://github.com/irskep/sphinx-better-theme
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/irskep/sphinx-better-theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
BuildPreReq: python-module-sphinx-devel

%description
This is a modified version of the default Sphinx theme with the
following goals:

1. Remove frivolous colors, especially hard-coded ones
2. Improve readability by limiting width and using more whitespace
3. Encourage visual customization through CSS, not themeconf
4. Use semantic markup

v0.1 meets goals one and two. Goal three is partially complete; it's
simple to add your own CSS file without creating a whole new theme.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
This is a modified version of the default Sphinx theme with the
following goals:

1. Remove frivolous colors, especially hard-coded ones
2. Improve readability by limiting width and using more whitespace
3. Encourage visual customization through CSS, not themeconf
4. Use semantic markup

v0.1 meets goals one and two. Goal three is partially complete; it's
simple to add your own CSS file without creating a whole new theme.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%files docs
%doc docs/_build/html/*

%changelog
* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20131011
- Initial build for Sisyphus

