Summary: Remote control program for Pentax DSLR cameras
Name: pktriggercord
Version: 0.77.10
Release: alt1
License: GPLv3

Group: Graphics
Source: pkTriggerCord-%version.src.tar.gz
Url: http://pktriggercord.sourceforge.net

Patch1: pktriggercord-0.77.10-alt-makefile.patch

BuildRequires: libglade-devel

%description
pkTriggerCord is a remote control program for Pentax DSLR cameras.

%prep
%setup -q
%patch1 -p2

%build
make clean
make PREFIX=/usr

%install
make install PREFIX=%buildroot/usr/
mkdir -p %buildroot/lib/udev/rules.d/
mv %buildroot/etc/udev/pentax.rules %buildroot/lib/udev/rules.d/025-pentax-dslr.rules
mv %buildroot/etc/udev/samsung.rules %buildroot/lib/udev/rules.d/025-samsung-dslr.rules

%files
%doc Changelog BUGS
%_bindir/pktriggercord*
%_datadir/%name
%_man1dir/pktriggercord*
/lib/udev/rules.d/*.rules

%changelog
* Tue Jun 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.77.10-alt1
- 0.77.10

* Thu Jul 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.76.00-alt1
- Initial

