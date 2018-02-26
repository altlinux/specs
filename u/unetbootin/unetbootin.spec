%define rel 549

Name: unetbootin
# Upstream use bzr release as version number. Chances that this numbering
# scheme will change, so for now we use (temporarily) zero version and
# upstream bzr revision in release tag.
Version: 0
Release: alt0.%rel

Summary: Create bootable Live USB drives for a variety of Linux distributions
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://unetbootin.sourceforge.net/
Source: http://downloads.sourceforge.net/%name/%name-source-%rel.tar.gz
Patch1: unetbootin-549-desktop.patch

# Syslinux is only available on x86 architectures
ExclusiveArch: %ix86 x86_64

# Automatically added by buildreq on Sat Sep 03 2011
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libstdc++-devel
BuildRequires: gcc-c++ libqt4-network phonon-devel

# Required for operation, not detected automatically:
Requires: mtools syslinux p7zip fdisk

%description
UNetbootin allows you to create bootable Live USB drives for a variety
of Linux distributions from Windows or Linux, without requiring you to
burn a CD. You can either let it download one of the many distributions
supported out-of-the-box for you, or supply your own Linux .iso file if
you've already downloaded one or your preferred distribution isn't on
the list.

%prep
%setup -c
%patch1 -p1

%build
# Generate .qm files
lrelease-qt4 unetbootin.pro

qmake-qt4
%make_build

%install
install -D -p -m 755 unetbootin %buildroot%_bindir/unetbootin
install -D -p -m 644 unetbootin.desktop %buildroot%_desktopdir/unetbootin.desktop

# Install localization files
install -d %buildroot%_datadir/unetbootin
install -c -p -m 644 unetbootin_*.qm %buildroot%_datadir/unetbootin/

for i in 16 22 24 32 48 64 128 192 512; do
	install -pDm644 unetbootin_$i.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/unetbootin.png
done;

%files
%_bindir/*
%_datadir/unetbootin
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Sep 03 2011 Victor Forsiuk <force@altlinux.org> 0-alt0.549
- Revision 549.
- Add requires for fdisk (since it is now separated from util-linux, so optional).

* Tue Aug 17 2010 Victor Forsiuk <force@altlinux.org> 0-alt0.485
- Initial build.
