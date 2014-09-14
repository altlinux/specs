Name: vamp-plugin-tester
Version: 1.0
Release: alt1
Summary: Vamp Plugin Tester
License: MIT
Group: Sound
Url: http://sourceforge.net/p/vamp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel

%description
This program tests Vamp audio feature extraction plugins
(http://vamp-plugins.org/) for certain common failure cases.

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_bindir
install -m755 vamp-plugin-tester %buildroot%_bindir/

%files
%doc README
%_bindir/*

%changelog
* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

