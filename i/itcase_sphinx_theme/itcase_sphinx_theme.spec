Name: itcase_sphinx_theme
Version: 20141006
Release: alt1
Summary: It's copy of pylons_sphinx_theme
License: Free
Group: Development/Tools
Url: https://github.com/ITCase/itcase_sphinx_theme
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/ITCase/itcase_sphinx_theme.git
Source: %name-%version.tar
BuildArch: noarch

%description
This repository contains ITCase themes for ITCase related projects.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
cp -fR * %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20141006-alt1
- Initial build for Sisyphus

