Name: etherwake
Version: 1.09
Release: alt1

Summary: A little tool to send magic Wake-on-LAN packets
License: GPL
Group: System/Configuration/Networking
Url: http://www.scyld.com/expert/wake-on-lan.html

# ftp://ftp.debian.org/debian/pool/main/e/etherwake/etherwake_1.09.orig.tar.gz
Source: %name-%version.tar
Patch1: etherwake-1.09-deb.patch
Patch2: etherwake-1.09-alt-format.patch

Conflicts: ethtool < 1:2.6.33, net-tools < 0:1.60-alt11

%description
You can wake up WOL compliant Computers which have been powered down to
sleep mode or start WOL compliant Computers with a BIOS feature.
WOL is an abbreviation for Wake-on-LAN. It is a standard that allows you
to turn on a computer from another location over a network connection.
A feature etherwake seperates from other implementations is, that it
also supports WOL passwords.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%__cc %optflags -o etherwake ether-wake.c

%install
install -pDm755 etherwake %buildroot%_sbindir/etherwake
install -pDm644 etherwake.8 %buildroot%_man8dir/etherwake.8
ln -s etherwake %buildroot%_sbindir/ether-wake
ln -s etherwake.8 %buildroot%_man8dir/ether-wake.8

%files
%_sbindir/*
%_man8dir/*

%changelog
* Wed Feb 03 2010 Dmitry V. Levin <ldv@altlinux.org> 1.09-alt1
- Initial revision based on Debian etherwake 1.09-3.
