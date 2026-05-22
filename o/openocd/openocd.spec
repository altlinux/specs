Name: openocd
Version: 0.12.0
Release: alt10

Summary: Debugging, in-system programming and boundary-scan testing for embedded devices
License: GPLv2
Group: Development/Tools
Url: http://sourceforge.net/projects/openocd

Requires: libjaylink >= 0.4.0

Source: %name-%version-%release.tar

BuildRequires: texinfo
BuildRequires: pkgconfig(capstone)
BuildRequires: pkgconfig(hidapi-hidraw)
BuildRequires: pkgconfig(jimtcl)
BuildRequires: pkgconfig(libftdi1)
BuildRequires: pkgconfig(libgpiod)
BuildRequires: pkgconfig(libjaylink)
BuildRequires: pkgconfig(libusb-1.0)

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system
programming and boundary-scan testing for embedded devices. Various
different boards, targets, and interfaces are supported to ease
development time.

Install OpenOCD if you are looking for an open source solution for
hardware debugging.

%prep
%setup

%build
%autoreconf
%configure  --disable-werror \
            --disable-doxygen-html \
            --disable-internal-jimtcl \
            --disable-internal-libjaylink \
            #
%make_build

%install
%makeinstall_std
install -pm644 -D contrib/60-openocd.rules %buildroot%_udevrulesdir/60-openocd.rules
rm -rf %buildroot%_datadir/openocd/contrib

%pre
/usr/sbin/groupadd -r -f plugdev &>/dev/null ||:

%files
%doc COPYING README.md
%_udevrulesdir/*.rules
%_bindir/openocd
%_datadir/openocd
%_infodir/openocd.info*
%_man1dir/*

%changelog
* Fri May 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt10
- v0.12.0-1528-gdc803e74b

* Mon Feb 02 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt9
- v0.12.0-1389-gdb34f6f0a

* Fri Nov 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt8
- v0.12.0-1283-g4e78563a0

* Mon Jul 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt7
- added support for ch347-based JTAG adapters
- added support for k1921vk028, k1921vk035 and k1912vg015 MCUs

* Thu May 08 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt6
- v0.12.0-982-gafbd01b0a

* Wed Nov 13 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt5
- dropped jlink related udev rules and rely on libjaylink ones

* Sat Nov 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt4
- fixed atlink udev rule

* Sat Aug 10 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt3
- added support for Arterytek AT32 MCU family

* Mon Mar 11 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt2
- rebuilt with jimtcl-0.82 and internal libgpiod

* Wed Jan 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- 0.12.0 released

* Thu Dec 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt0.3
- v0.12.0-rc3

* Mon Oct 31 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt0.2
- v0.12.0-rc2

* Wed Sep 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt0.1
- v0.12.0-rc1

* Tue Aug 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt4
- v0.11.0-808-g9cd714cd1

* Mon Jun 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt3
- v0.11.0-715-g480d4e177

* Fri Mar 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt2
- 0.11.0 released

* Thu Dec 10 2020 Ildar Mulyukov <ildar@altlinux.ru> 0.11.0-alt1.rc1
- new version (git HEAD)

* Wed Sep 11 2019 Ildar Mulyukov <ildar@altlinux.ru> 0.10.0-alt1.git.930.g09eb941cb
- new version (git HEAD)

* Thu Jan 05 2017 Ildar Mulyukov <ildar@altlinux.ru> 0.10.0-alt0_rc1
- new version
- minor cleanups and additions
- fixes #32962

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1.1
- NMU: added BR: texinfo

* Thu Nov 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.0-alt1
- Updated to v0.9.0.

* Mon May 05 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.0-alt1.git8fa67bd
- Updated to v0.8.0-1-g8fa67bd.

* Sat Sep 21 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.0-alt1.git1304b27
- New version (1304b27).

* Wed Apr 10 2013 Andrey Kotoff <kotbegemot@altlinux.org> 0.6.0-alt1.git74db7f9
- Initial build.
