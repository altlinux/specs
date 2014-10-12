Name: flask-sphinx-themes
Version: 20130715
Release: alt1
Summary: Flask Sphinx Styles
License: BSD
Group: Development/Tools
Url: https://github.com/mitsuhiko/flask-sphinx-themes
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/flask-sphinx-themes.git
Source: %name-%version.tar
BuildArch: noarch

%description
Sphinx styles for Flask and Flask related projects.

%prep

%install
install -d %buildroot%_datadir
cd %buildroot%_datadir
tar -xf %SOURCE0
rm -fR %name/.gear

%files
%_datadir/%name

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130715-alt1
- Initial build for Sisyphus

