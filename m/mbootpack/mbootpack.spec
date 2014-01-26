Name: mbootpack
Version: 0.6a
Release: alt1
Summary: A tool that takes a multiboot kernel and modules
License: GPLv2
Group: System/Kernel and hardware
URL: http://www.tjd.phlegethon.org/software
Source: %url/%name-%version.tar
Patch: %name-%version-%release.patch
ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64

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
%make_build CFLAGS="%optflags"


%install
install -pD -m 0755 {,%buildroot%_bindir/}%name


%files
%doc Changes README
%_bindir/*


%changelog
* Sun Jan 26 2014 Led <led@altlinux.ru> 0.6a-alt1
- initial build
