%define _unpackaged_files_terminate_build 1

Name: pcsc-lite-acsccid
Version: 1.1.13
Release: alt3

Summary: PCSC Driver for ACS CCID Based Smart Card Readers
License: LGPLv2.1+
Group: System/Servers

Url: http://acsccid.sourceforge.net/
Source: %name-%version.tar
Patch: %name-1.1.0-alt-ACR38U-CCID-rule.patch

BuildRequires: libusb-devel
BuildRequires: libpcsclite-devel
BuildRequires: flex
BuildRequires: autoconf-archive

Provides: pcsc-acsccid = %version-%release
Obsoletes: pcsc-acsccid < %version-%release
Requires(pre): pcsc-lite
Provides: pcsc-ifd-handler

%description
This package contains a ACS USB CCID (Chip/Smart Card Interface
Devices) driver.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup
%patch -p1
mkdir config
cp /usr/share/gettext/config.rpath config

%build
mkdir m4
%autoreconf -I %_datadir/gettext/m4
%configure --enable-composite-as-multislot --enable-twinserial
%make

%install
%makeinstall_std
install -Dp src/92_pcscd_acsccid.rules %buildroot%_udevrulesdir/92_pcscd_acsccid.rules

%post
# Restart pcscd
%post_service pcscd

%files
%doc AUTHORS COPYING README
%_udevrulesdir/*.rules
%_libdir/pcsc/drivers/*

%changelog
* Sun Jul 05 2026 Andrey Cherepanov <cas@altlinux.org> 1.1.13-alt3
- FTBFS: fixed build with new glibc.

* Tue Mar 10 2026 Andrey Cherepanov <cas@altlinux.org> 1.1.13-alt2
- Returned pcscd group in udev rules (ALT #58147).

* Thu Nov 20 2025 Andrey Cherepanov <cas@altlinux.org> 1.1.13-alt1
- New version.

* Wed Jul 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.1.12-alt1
- New version.

* Thu Apr 10 2025 Alexey Shabalin <shaba@altlinux.org> 1.1.11-alt2
- Add Provides: pcsc-ifd-handler.
- Fixed udev rules dir.
- Restart pcscd after install ifd-acsccid.

* Sat Mar 30 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.11-alt1
- New version.

* Mon Aug 07 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.10-alt1
- New version.

* Sat Mar 25 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- New version.

* Fri Jan 10 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.8-alt1
- New version.

* Sat Jul 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- New version.

* Wed Oct 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- New version.

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- new version 1.1.4

* Thu Sep 15 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- New version 1.1.3

* Wed Sep 23 2015 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.0
- updated patch (is it still needed?)

* Mon Dec 17 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4

* Tue Sep 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.3-alt2
- added 072f:90cc USB ID

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Nov 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt0.20110919
- 1.0.3-20110919

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1
- initial
