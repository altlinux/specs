Name: rutilt
Version: 0.18
Release: alt2

Summary: Configure your wireless network devices with special support for rt2400/rt2500/rt2570

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Group: Networking/Other
Url: http://bonrom.cbbknet.com/

#Source: http://cbbk.free.fr/bonrom/files/RutilTv%version.tar.bz2
#Source: http://bonrom.cbbknet.com/?download=RutilTv0.18.tar.gz
Source: RutilTv%version.tar.bz2
Patch: %name-0.18-alt-set_ip.patch
Patch2: %name-0.13.patch
Patch1: %name-0.16.patch

# Automatically added by buildreq on Thu Jan 18 2007
BuildRequires: gcc-c++ libgtk+2-devel

%description
RutilT is a Gtk2/X utility for Linux that helps you configure your
wireless network devices (it has extra support for Ralink ones).
RutilT should work with any Linux wireless extension compliant kernel module.
It also features special support for rt2400, rt2500 and rt2570 devices.

%prep
%setup -q -n RutilTv%version
%patch -b .orig

%build
./configure.sh --kernel_sources=%_includedir/linux-default/ --prefix=%prefix
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_bindir/%name
%_bindir/rutilt_helper
# FIXME: set_ip.sh is not useful in ALT
%_desktopdir/%name.desktop
%_datadir/apps/%name/
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/*

%changelog
* Thu Dec 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt2
- change summary
- remove dhclient requires (bug #18240)

* Wed Dec 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- new version 0.18 (with rpmrb script)

* Wed Jun 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt1
- new version 0.16 (with rpmrb script)

* Tue Jul 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- new version 0.15 (with rpmrb script)

* Thu Jan 18 2007 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt0.1
- initial build for ALT Linux Sisyphus
