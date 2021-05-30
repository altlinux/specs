Name: stylewriter
Version: 0.9.9.1
Release: alt1.git20170426.1
License: GPL
Group: System/Configuration/Printing

Url: https://github.com/Godzil/lpstyl/
Source: %name-%version.tar
BuildRequires: cmake gcc-c++

Summary: Non-MacOS StyleWriter driver
%description
This is a driver for certain types of Apple StyleWriter printers.

%prep
%setup

%build
%cmake
%cmake_build

%install
install -d %buildroot%_bindir
install -m0755 %_cmake__builddir/lpstyl %buildroot%_bindir

%files
%doc scripts README* printcap* styl.ppd
%_bindir/*

%changelog
* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 0.9.9.1-alt1.git20170426.1
- NMU: spec: adapted to new cmake macros.

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.9.9.1-alt1.git20170426
- Initial build for ALT

