Name: pcsc-lite-ccid
Version: 1.8.1
Release: alt1

Summary: Generic USB CCID smart card reader driver
License: BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group: System/Libraries
URL: https://ccid.apdu.fr

Requires: pcsc-lite

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: flex
BuildRequires: pkgconfig(libpcsclite) pkgconfig(libusb-1.0) pkgconfig(zlib) pkgconfig(udev)

Provides: ccid = %version-%release
Obsoletes: ccid < %version-%release
Conflicts: pcsc-lite-openct
Requires(pre): pcsc-lite
Provides: pcsc-ifd-handler

%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
Generic USB CCID (Chip/Smart Card Interface Devices) driver for use with the
PC/SC Lite daemon.

%prep
%setup

%build
%meson -Dserial=true
%meson_build

%install
%meson_install

%post
# Restart pcscd
%post_service pcscd

%files
%doc AUTHORS README.md
%config(noreplace) %_sysconfdir/reader.conf.d/libccidtwin
%ifddir/ifd-ccid.bundle
%_libdir/pcsc/drivers/serial/libccidtwin.so
%_udev_rulesdir/92_pcscd_ccid.rules

%changelog
* Thu Jun 11 2026 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version.

* Wed May 27 2026 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version.

* Fri Feb 06 2026 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version.

* Fri Oct 03 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version.

* Wed Apr 09 2025 Alexey Shabalin <shaba@altlinux.org> 1.6.2-alt2
- Use meson for build.

* Thu Mar 20 2025 Andrey Cherepanov <cas@altlinux.org> 1.6.2-alt1
- New version.
- Remove deprecated submodules.

* Sat Jul 06 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.1-alt1
- New version.

* Sat Jun 01 2024 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.

* Fri Jan 05 2024 Andrey Cherepanov <cas@altlinux.org> 1.5.5-alt1
- New version.

* Mon Oct 30 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.4-alt1
- New version.

* Thu Oct 26 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.3-alt1
- New version.

* Mon Feb 20 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt1
- New version.
- Conflicted with pcsc-lite-openct (ALT #45282).

* Wed Jan 26 2022 Andrey Cherepanov <cas@altlinux.org> 1.4.36-alt1
- New version.

* Tue Feb 09 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.34-alt1
- New version.
- Clatify license name and version.

* Fri Jun 26 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.33-alt1
- New version.

* Mon Jun 15 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.32-alt2
- Rebuild with pcsc-lite-1.9.0.

* Wed Apr 22 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.32-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.31-alt1
- New version.

* Thu Feb 22 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.29-alt1
- New version.

* Sat Oct 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.28-alt1
- New version

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.27-alt1
- New version

* Thu May 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.26-alt2
- pcsc: fixed realloc usage.

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.26-alt1
- new version 1.4.26

* Thu Sep 15 2016 Andrey Cherepanov <cas@altlinux.org> 1.4.24-alt1
- New version 1.4.24
- Drop obsoleted patch
- Build from upstream Git repository

* Mon Sep 21 2015 Michael Shigorin <mike@altlinux.org> 1.4.20-alt1
- 1.4.20 (closes: #31292)

* Tue May 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt3
- Add JaCarta Flash support (ALT #27377)

* Wed Mar 21 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt2
- Add JaCarta support (Alladin)

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt1
- [1.4.5]

* Sun Jun 27 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.13-alt1
- [1.3.13]

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.11-alt1
- Initial build

