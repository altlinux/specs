Name: sphinx-theme-minimalism
Version: 20110206
Release: alt1
Summary: A simple Sphinx theme inspired by Flasks documentation
License: Free
Group: Development/Python
Url: https://github.com/DasIch/sphinx-theme-minimalism
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/DasIch/sphinx-theme-minimalism.git
Source: %name-%version.tar
BuildArch: noarch

%description
A simple Sphinx theme inspired by Flasks documentation.

%install
install -d %buildroot%_datadir
pushd %buildroot%_datadir
tar -xf %SOURCE0
rm -fR %name/.gear
popd

%files
%_datadir/%name

%changelog
* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110206-alt1
- Initial build for Sisyphus

