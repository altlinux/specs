Name: cdctl
Version: 0.15
Release: alt1

Summary: Controls your cdrom drive
License: Free for non-commercial use
Group: System/Kernel and hardware

Url: http://cdctl.sourceforge.net
Source: http://downloads.sourceforge.net/cdctl/%name-%version.tar.gz
Patch: http://www.netnitco.lkams.kernel.org/pub/mirrors/gentoo/portage/app-misc/cdctl/files/cdctl-0.15-cdc_ioctls.patch
Packager: Michael Shigorin <mike@altlinux.org>

%description
cdctl controls your cdrom drive under Linux.  It is an user-level
console application which gives the user access to the ioctl()
interfaces of the Uniform CDROM Driver of the Linux kernel.  It
can play audio CDs, control the drive's tray motor, change the
drive's volume levels, read the current type of disc in the
drive, and much more.

%prep
%setup
%patch -p1

%build
CXXFLAGS="%optflags" %configure
%make_build

%install
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*
%doc README LICENSE NEWS NUTSANDBOLTS PUBLICKEY

%changelog
* Mon Jan 21 2008 Michael Shigorin <mike@altlinux.org> 0.15-alt1
- built for ALT Linux
- somewhat upgraded spec fashion. :)
- added Gentoo patch

* Sun Mar 26 2000 Jason Spence <thalakan@technologist.com>
- First spec file for cdctl.
