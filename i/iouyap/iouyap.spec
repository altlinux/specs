Name: iouyap
Version: 0.97
Release: alt2
Summary: Bridge IOU to TAP, UDP and Ethernet
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://github.com/GNS3/iouyap

Source: %name-%version.tar

BuildRequires: gcc bison flex glibc-devel

%description
Bridge IOU to TAP, UDP and Ethernet, mainly used by gns3server

In order to use iouyap as non-root user, the user needs to be member of the
iouyap group!

%prep
%setup

%build
bison --yacc -dv netmap_parse.y
flex netmap_scan.l
gcc -I -Wall -fPIE %optflags -fcommon *.c iniparser/*.c -o %name -lpthread -pie

%install
mkdir -p %buildroot%_bindir
cp %name %buildroot%_bindir

%pre
%_sbindir/groupadd -r iouyap 2> /dev/null || :

%files
%doc LICENSE README.rst
%attr(0750,root,iouyap) %_bindir/%name

%changelog
* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 0.97-alt2
- Set CFLAGS+=-fcommon to workaround gcc10 errors
- Fix License Tag

* Fri Jun 29 2018 Anton Midyukov <antohami@altlinux.org> 0.97-alt1.1
- Rebuilt for aarch64

* Mon Aug 08 2016 Anton Midyukov <antohami@altlinux.org> 0.97-alt1
- Initial build for ALT Linux Sisyphus.
