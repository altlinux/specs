Name: diaoul-sphinx-themes
Version: 20130519
Release: alt1
Summary: Diaoul Sphinx Styles
License: BSD
Group: Development/Tools
Url: https://github.com/Diaoul/diaoul-sphinx-themes
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/Diaoul/diaoul-sphinx-themes.git
Source: %name-%version.tar
BuildArch: noarch

%description
This repository contains sphinx styles Diaoul uses in most of his
projects. It is a derivative of Mitsuhiko's themes for Flask and Flask
related projects.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
cp -fR * %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130519-alt1
- Initial build for Sisyphus

