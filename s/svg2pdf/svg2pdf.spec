Name: svg2pdf
Version: 0.2
Release: alt1
Summary: Convert SVG files to only one PDF file
License: GPL v3
Group: File tools
Url: http://code.google.com/p/svg2pdf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%description
Convert SVG files to only one PDF file.

%prep
%setup

%install
install -d %buildroot%_bindir
install -p -m755 SVG2PDF %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

