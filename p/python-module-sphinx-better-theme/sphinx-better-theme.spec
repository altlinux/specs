%define oname sphinx-better-theme

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt2.git20131011
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
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
This is a modified version of the default Sphinx theme with the
following goals:

1. Remove frivolous colors, especially hard-coded ones
2. Improve readability by limiting width and using more whitespace
3. Encourage visual customization through CSS, not themeconf
4. Use semantic markup

v0.1 meets goals one and two. Goal three is partially complete; it's
simple to add your own CSS file without creating a whole new theme.

%package -n python3-module-%oname
Summary: A nice-looking, customizable theme for Sphinx
Group: Development/Python3

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt2.git20131011
- Added module for Python 3

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20131011
- Initial build for Sisyphus

