Name: iouyap
Version: 0.97
Release: alt1
Summary: Bridge IOU to TAP, UDP and Ethernet
License: GPLv3
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
gcc -I -Wall -fPIE %optflags *.c iniparser/*.c -o %name -lpthread -pie

%install
mkdir -p %buildroot%_bindir
cp %name %buildroot%_bindir

%pre
%_sbindir/groupadd -r iouyap 2> /dev/null || :

%files
%doc LICENSE README.rst
%attr(0750,root,iouyap) %_bindir/%name

%changelog
* Mon Aug 08 2016 Anton Midyukov <antohami@altlinux.org> 0.97-alt1
- Initial build for ALT Linux Sisyphus.
