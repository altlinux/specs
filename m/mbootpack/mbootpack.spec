%def_with zlib

Name: mbootpack
Version: 0.6a
Release: alt3
Summary: A tool that takes a multiboot kernel and modules
License: GPLv2
Group: System/Kernel and hardware
URL: http://www.tjd.phlegethon.org/software
Source: %url/%name-%version.tar
Patch: %name-%version-%release.patch
ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64

BuildRequires: help2man
%{?_with_zlib:BuildRequires: zlib-devel}

%description
%name is a tool that takes a multiboot kernel and modules (e.g. a Xen VMM,
linux kernel and initrd), and packages them up as a single file that looks like
a bzImage linux kernel. The aim is to allow you to boot multiboot kernels
(in particular, Xen) using bootloaders that don't support multiboot
(i.e. pretty much anything except GRUB and SYSLINUX).


%prep
%setup -q
%patch -p1


%build
%make_build CC="%__cc" CFLAGS="%optflags" VERSION="%version" %{?_with_zlib:WITH_ZLIB=1}


%install
install -pD -m 0755 {,%buildroot%_bindir/}%name
install -pD -m 0644 %name.man %buildroot%_man1dir/%name.1


%files
%doc Changes README
%_bindir/*
%_man1dir/*


%changelog
* Tue Mar 18 2014 Led <led@altlinux.ru> 0.6a-alt3
- added manpage
- added -V/--version option

* Mon Mar 17 2014 Led <led@altlinux.ru> 0.6a-alt2
- added CFLAGS for mbootpack compiling
- added optional build with zlib
- build with zlib

* Sun Jan 26 2014 Led <led@altlinux.ru> 0.6a-alt1
- initial build
