Name: pylons_sphinx_theme
Version: 1.0
Release: alt3
Summary: Pylons Sphinx Theme
License: Free
Group: Development/Tools
Url: https://github.com/Pylons/pylons_sphinx_theme
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pylons_sphinx_theme.git
Source: %name-%version.tar
BuildArch: noarch

%description
Pylons themes for Pylons related projects.

%prep
%setup

rm -fR .gear

%install
install -d %buildroot%_datadir/%name
cp -fR * %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- New snapshot

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- New snapshot

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

