Name: fprint_demo
Version: 0.4
Release: alt1

Summary: GTK+ application to demonstrate and test libfprint's capabilities

License: GPL
Group: System/Configuration/Other
Url: http://www.reactivated.net/fprint/wiki/Fprint_demo

BuildRequires: libgtk+2-devel libfprint-devel

Source: %name-%version.tar

%description
fprint_demo is a simple GTK+ application to demonstrate and test
libfprint's capabilities. It is written in C and licensed under the
GNU GPL v2.

It provides access to many of the features offered by the backing
library, libfprint. 

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/fprint_demo

%changelog
* Fri Dec 12 2008 Denis Klimov <zver@altlinux.org> 0.4-alt1
- Init build for ALT Linux

