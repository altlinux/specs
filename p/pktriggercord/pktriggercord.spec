Summary: Remote control program for Pentax DSLR cameras
Name: pktriggercord
Version: 0.85.00
Release: alt1
License: GPLv3

Group: Graphics
Source: %name-%version.tar
URL: http://pktriggercord.melda.info
VCS: https://github.com/asalamon74/pktriggercord

BuildRequires: libglade-devel

%description
pkTriggerCord is a remote control program for Pentax DSLR cameras.

%prep
%setup

%build
make PREFIX=%_prefix CFLAGS="$CFLAGS -Isrc/external/js0n"

%install
make install PREFIX=%_prefix DESTDIR=%buildroot
mkdir -p %buildroot/lib/udev/rules.d/
mv -v %buildroot/etc/udev/pentax.rules %buildroot/lib/udev/rules.d/025-pentax-dslr.rules
mv -v %buildroot/etc/udev/samsung.rules %buildroot/lib/udev/rules.d/025-samsung-dslr.rules

%files
%doc Changelog BUGS
%_bindir/pktriggercord*
%_datadir/%name
%_man1dir/pktriggercord*
/lib/udev/rules.d/*.rules

%changelog
* Sun Jan 12 2025 Grigory Ustinov <grenka@altlinux.org> 0.85.00-alt1
- Build new version.

* Mon Mar 29 2021 Grigory Ustinov <grenka@altlinux.org> 0.77.10-alt2
- Fixed FTBFS with -fcommon.

* Tue Jun 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.77.10-alt1
- 0.77.10

* Thu Jul 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.76.00-alt1
- Initial

