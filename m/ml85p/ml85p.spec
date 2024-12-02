Name: ml85p
Version: 0.2.0
Release: alt3

Summary: Driver for the Samsung ML-85G and QL-85G winprinters
License: GPL
Group: System/Configuration/Printing

Url: http://ww1.pragana.net/gdiprinters.html
# Source: http://ww1.pragana.net/%name-%version.tar.gz
Source: %name-%version.tar
Patch1: ml85p-0.2.0-build_fix.patch
Patch2: ml85p-ftbfs-gcc14.patch

# sys/io.h
ExclusiveArch: %ix86 x86_64

%description
%summary.

%prep
%setup
%patch1 -p1
%patch2 -p2
chmod 644 *
sed -i "s|/usr/local/bin|%_bindir|g" *

%build
rm -f ml85p
gcc %optflags -o ml85p ml85p.c

%install
install -pDm755 ml85p %buildroot%_bindir/%name

%files
%doc COPYING NEWS README THANKS ml85-print ml85-test printcap
%_bindir/*

%changelog
* Mon Dec 02 2024 Oleg Solovyov <mcpain@altlinux.org> 0.2.0-alt3
- fix ftbfs for gcc14

* Tue Oct 18 2022 Michael Shigorin <mike@altlinux.org> 0.2.0-alt2
- Minor spec cleanup

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.2.0-alt1
- Initial build for ALT

