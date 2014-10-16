Name: gmsl
Version: 1.1.6
Release: alt1
Summary: GNU Make Standard Library
License: BSD
Group: Development/Tools
Url: http://sourceforge.net/projects/gmsl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%description
GNU Make Standard Library: a library of functions written for GNU Make
using GNU Make's built in functions.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
install -p -m644 gmsl __gmsl gmsl-tests %buildroot%_datadir/%name/

%files
%doc README *.html
%_datadir/%name

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1
- Initial build for Sisyphus

