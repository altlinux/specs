Name: kr-sphinx-themes
Version: 20120607
Release: alt1
Summary: Sphinx theme I use for most projects. Derivative of Mitsuhiko's Flask theme.
License: BSD
Group: Development/Python
Url: https://github.com/kennethreitz/kr-sphinx-themes
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kennethreitz/kr-sphinx-themes.git
Source: %name-%version.tar
BuildArch: noarch

%description
This repository contains sphinx styles Kenneth Reitz uses in most of his
projects. It is a drivative of Mitsuhiko's themes for Flask and Flask
related projects. To use this style in your Sphinx documentation, follow
this guide:

1. put this folder as _themes into your docs folder. Alternatively you
  can also use git submodules to check out the contents there.

2. add this to your conf.py:

  sys.path.append(os.path.abspath('_themes'))
  html_theme_path = ['_themes']
  html_theme = 'kr'

%prep
%setup

%install
install -d %buildroot%_datadir/%name
cp -fR * %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20120607-alt1
- Initial build for Sisyphus

