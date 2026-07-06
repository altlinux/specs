%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%global sover 3

%global glib2_version 2.72.0
%global libxmlb_version 0.3.19
%global libusb_version  0.1.12
%global libcurl_version 7.62.0
%global libjcat_version 0.2.0
%global systemd_version 249

# 1.9.3: test suite fails on ppc64le
%ifarch ppc64le
%def_without check
%endif

%def_with check

%def_enable tests

# fwupd-efi is only available on these arches
%ifarch %efi_arches
%def_enable uefi
%endif

%ifarch x86_64 %ix86
%def_enable msr
%endif

%define fwupd_pluginsdir %_libdir/fwupd-%version

Name: fwupd
Version: 2.1.6
Release: alt1

Summary: Firmware update daemon
License: LGPL-2.1+
Group: System/Configuration/Hardware
Url: https://github.com/fwupd/fwupd

Source0: %name-%version.tar
Source2: fwupd.watch
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-uefi >= 0.9-alt1

BuildRequires: bash-completion
BuildRequires: cmake
BuildRequires: git-core
BuildRequires: gi-docgen
BuildRequires: glib2-devel >= %glib2_version
BuildRequires: libappstream-glib-devel
BuildRequires: libmm-glib-devel
BuildRequires: libqmi-glib-devel
BuildRequires: libmbim-glib-devel
BuildRequires: /usr/bin/protoc /usr/bin/protoc-gen-c
BuildRequires: libcolord-devel
BuildRequires: liblzma-devel
BuildRequires: libcbor-devel
BuildRequires: libcurl-devel >= %libcurl_version
BuildRequires: libelf-devel
BuildRequires: libgnutls-devel
BuildRequires: gnutls-utils
BuildRequires: libgpgme-devel
BuildRequires: libusb-devel >= %libusb_version
BuildRequires: libblkid-devel
BuildRequires: libjcat-devel >= %libjcat_version
BuildRequires: libpango-gir-devel
BuildRequires: libpolkit-devel
BuildRequires: libdrm-devel
BuildRequires: libsoup-devel
BuildRequires: libsqlite3-devel
BuildRequires: libsystemd-devel >= %systemd_version
BuildRequires: libtpm2-tss-devel
BuildRequires: libudev-devel
BuildRequires: libumockdev-devel
BuildRequires: libuuid-devel
BuildRequires: libxmlb-devel >= %libxmlb_version
BuildRequires: meson
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-jinja2
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel
BuildRequires: /proc

# Build with passim starting from p11
# No passim in p10 due to old libsoup3.0 and glib2
%if "%(rpmvercmp '%ubt_id' 'M110')" >= "0"
BuildRequires: libpassim-devel
%endif

%if_enabled uefi
BuildRequires: libpango-devel
BuildRequires: libcairo-devel libcairo-gobject-devel
BuildRequires: libfreetype-devel
BuildRequires: fontconfig
BuildRequires: fonts-ttf-dejavu
BuildRequires: gnu-efi
Requires: fwupd-efi
Provides: fwupdate
Obsoletes: fwupdate
%endif

%if_with check
BuildRequires: polkit
%endif

Requires: bubblewrap

# See https://bugzilla.altlinux.org/59016
Requires: udisks2

Obsoletes: fwupd-labels <= %EVR

%description
fwupd is a daemon to allow session software to update device firmware.

%package -n libfwupd%sover
Summary: Libraries for %name
Group: System/Libraries

%description -n libfwupd%sover
Libraries for %name.

%package -n libfwupd-devel
Summary: Development package for %name
Group: Development/C
Obsoletes: %name-devel < %EVR
Provides: %name-devel = %EVR

%description -n libfwupd-devel
Files for development with %name.

%package -n libfwupd-devel-docs
Summary: Documentation for libfwupd-devel
Group: Documentation

%description -n libfwupd-devel-docs
Documentation for libfwupd-devel.

%package tests
Group: System/Configuration/Hardware
Summary: Data files for installed tests

%description tests
Data files for installed tests.

%package plugin-modem-manager
Group: System/Configuration/Hardware
Summary: fwupd plugin using ModemManger
Requires: %name = %EVR

%description plugin-modem-manager
This provides the optional package which is only required on hardware that
might have mobile broadband hardware. It is probably not required on servers.

%prep
%setup
%patch0 -p1

%build
%meson \
    -Ddocs=enabled \
    --debug \
    -Dfirmware-packager=true \
    -Dman=true \
    -Dlvfs=true \
    -Dsupported_build=enabled \
%if_enabled tests
    -Dtests=true \
%else
    -Dtests=false \
%endif
    -Dplugin_modem_manager=enabled \
    -Defi_app_location=%_libdir/efi \
    -Dbluez=enabled

%meson_build

%install
%meson_install

# CET is available only since i686
%ifarch i386 i486 i586
rm -f %buildroot%_libexecdir/fwupd/fwupd-detect-cet ||:
%endif

mkdir -p --mode=0700 %buildroot%_localstatedir/fwupd
mv %buildroot%_docdir/fwupd %buildroot%_docdir/fwupd-devel-%version
rm -f %buildroot%_docdir/fwupd-devel-%version/lib*
mv %buildroot%_docdir/libfw* %buildroot%_docdir/fwupd-devel-%version/

%find_lang %name

%check
%meson_test

%files -f %name.lang
%doc README.md COPYING
%_man1dir/fwupdtool.1*
%_man1dir/fwupdmgr.1*
%if_enabled uefi
%_man1dir/dbxtool.1*
%endif
%_man5dir/*
%_man8dir/*
%config(noreplace)%_sysconfdir/fwupd/fwupd.conf
%dir %_libexecdir/fwupd
%_libexecdir/fwupd/fwupd
%_bindir/fwupdtool
%ifarch x86_64
%_libexecdir/fwupd/fwupd-detect-cet
%endif
%_datadir/bash-completion/completions/*
%_datadir/fish/vendor_completions.d/fwupdmgr.fish
%_iconsdir/hicolor/*/apps/org.freedesktop.fwupd.*
%if_enabled uefi
%_bindir/dbxtool
%endif
%_bindir/fwupdmgr
%dir %_sysconfdir/fwupd
%dir %_sysconfdir/fwupd/remotes.d
%_sysconfdir/fwupd/bios-settings.d
%config(noreplace)%_sysconfdir/fwupd/remotes.d/*.conf
%_sysconfdir/pki/fwupd
%_sysconfdir/pki/fwupd-metadata
%dir %_datadir/fwupd
%dir %_datadir/fwupd/metainfo
%dir %_datadir/fwupd/remotes.d
%dir %_datadir/fwupd/remotes.d/vendor
%_datadir/dbus-1/system.d/org.freedesktop.fwupd.conf
%_datadir/fwupd/remotes.d/vendor/firmware
%_datadir/dbus-1/interfaces/org.freedesktop.fwupd.xml
%_datadir/polkit-1/actions/org.freedesktop.fwupd.policy
%_datadir/polkit-1/rules.d/org.freedesktop.fwupd.rules
%_datadir/dbus-1/system-services/org.freedesktop.fwupd.service
%_datadir/metainfo/org.freedesktop.fwupd.metainfo.xml
%_datadir/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs-testing.metainfo.xml
%_datadir/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs.metainfo.xml
%_datadir/fwupd/firmware_packager.py
%_datadir/fwupd/add_capsule_header.py
%_datadir/fwupd/install_dell_bios_exe.py
%_datadir/fwupd/simple_client.py
%_unitdir/fwupd.service
%_unitdir/fwupd-refresh.timer
%_unitdir/fwupd-refresh.service
%_systemddir/system-shutdown/fwupd.shutdown
%dir %_localstatedir/fwupd
%dir %_datadir/fwupd/quirks.d
%_datadir/fwupd/quirks.d/builtin.quirk.gz
%_libdir/girepository-1.0/Fwupd-2.0.typelib
%dir %fwupd_pluginsdir
%fwupd_pluginsdir/libfwupd*.so
%_modulesloaddir/fwupd-i2c.conf
%if_enabled msr
%_modulesloaddir/fwupd-msr.conf
%endif
%if_enabled uefi
%config(noreplace)%_sysconfdir/grub.d/35_fwupd
%_datadir/fwupd/uefi-capsule-ux.zip
%endif
%_sysusersdir/fwupd.conf

%files -n libfwupd%sover
%_libdir/libfwupd.so.%{sover}*

%files plugin-modem-manager
%fwupd_pluginsdir/libfu_plugin_modem_manager.so

%files -n libfwupd-devel
%_datadir/dbus-1/interfaces/org.freedesktop.fwupd.xml
%_datadir/gir-1.0/Fwupd-2.0.gir
%_includedir/fwupd-3
%_libdir/libfwupd.so
%_libdir/pkgconfig/fwupd.pc
%_datadir/vala/vapi/*

%files -n libfwupd-devel-docs
%_docdir/fwupd-devel-%version

%files tests
%if_enabled tests
%dir %_datadir/fwupd/host-emulate.d
%_datadir/fwupd/host-emulate.d/*.json.gz
%_datadir/installed-tests/fwupd
%_libexecdir/installed-tests/fwupd
%_datadir/fwupd/remotes.d/fwupd-tests.conf
%endif

%changelog
* Wed Jul 01 2026 Egor Ignatov <egori@altlinux.org> 2.1.6-alt1
- New version 2.1.6.

* Wed Jun 10 2026 Egor Ignatov <egori@altlinux.org> 2.1.5-alt1
- New version 2.1.5.

* Sat May 30 2026 Egor Ignatov <egori@altlinux.org> 2.1.4-alt1
- New version 2.1.4.

* Thu May 21 2026 Egor Ignatov <egori@altlinux.org> 2.1.3-alt1
- New version 2.1.3.

* Thu May 07 2026 Egor Ignatov <egori@altlinux.org> 2.1.2-alt2
- Add udisks2 dependency (closes: #59016)
- Fix dbxtool "no path set for sysfsdir-fw" (closes: #59017)

* Fri Apr 24 2026 Egor Ignatov <egori@altlinux.org> 2.1.2-alt1
- New version 2.1.2.

* Mon Mar 30 2026 Egor Ignatov <egori@altlinux.org> 2.1.1-alt1
- New version 2.1.1.

* Fri Feb 27 2026 Egor Ignatov <egori@altlinux.org> 2.0.20-alt1
- New version 2.0.20.

* Wed Dec 24 2025 Egor Ignatov <egori@altlinux.org> 2.0.19-alt1
- 2.0.19

* Sun Dec 07 2025 Egor Ignatov <egori@altlinux.org> 2.0.18-alt1
- 2.0.18

* Fri Nov 14 2025 Egor Ignatov <egori@altlinux.org> 2.0.17-alt1
- 2.0.17

* Tue Sep 30 2025 Egor Ignatov <egori@altlinux.org> 2.0.16-alt1
- 2.0.16

* Thu Jun 19 2025 Egor Ignatov <egori@altlinux.org> 2.0.12-alt1
- 2.0.12
- add introspection data file to -devel package as well (closes: #49681)

* Mon May 12 2025 Egor Ignatov <egori@altlinux.org> 2.0.9-alt1
- 2.0.9

* Wed Apr 16 2025 Ivan A. Melnikov <iv@altlinux.org> 2.0.8-alt1.1
- NMU: fix FTBFS on loongarch64, riscv64 and i586
  - enable uefi on loongarch64 and riscv64;
  - backport patch from upstream to fix x86 build.

* Thu Apr 10 2025 Egor Ignatov <egori@altlinux.org> 2.0.8-alt1
- 2.0.8

* Wed Mar 26 2025 Egor Ignatov <egori@altlinux.org> 2.0.7-alt1
- 2.0.7

* Fri Feb 14 2025 Egor Ignatov <egori@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Feb 04 2025 Egor Ignatov <egori@altlinux.org> 2.0.5-alt1
- 2.0.5

* Tue Jan 21 2025 Egor Ignatov <egori@altlinux.org> 2.0.4-alt1
- 2.0.4

* Fri Dec 20 2024 Egor Ignatov <egori@altlinux.org> 2.0.3-alt1
- 2.0.3 (closes: #52485)

* Mon Dec 02 2024 Egor Ignatov <egori@altlinux.org> 2.0.2-alt1
- 2.0.2
- New libfwupd ABI version.

* Mon Dec 02 2024 Egor Ignatov <egori@altlinux.org> 1.9.26-alt2
- Fix libfwupd dependency on fwupd.

* Fri Nov 29 2024 Egor Ignatov <egori@altlinux.org> 1.9.26-alt1
- 1.9.26
- Package according to Shared Libs Policy.

* Wed Sep 25 2024 Egor Ignatov <egori@altlinux.org> 1.9.25-alt1
- 1.9.25

* Thu Aug 22 2024 Egor Ignatov <egori@altlinux.org> 1.9.24-alt1
- 1.9.24

* Fri Jun 14 2024 Egor Ignatov <egori@altlinux.org> 1.9.21-alt1
- 1.9.21

* Mon May 20 2024 Egor Ignatov <egori@altlinux.org> 1.9.20-alt1
- 1.9.20

* Wed Apr 24 2024 Egor Ignatov <egori@altlinux.org> 1.9.18-alt1
- 1.9.18

* Tue Apr 23 2024 Egor Ignatov <egori@altlinux.org> 1.9.17-alt1
- 1.9.17

* Fri Apr 05 2024 Egor Ignatov <egori@altlinux.org> 1.9.16-alt1
- 1.9.16

* Wed Apr 03 2024 Egor Ignatov <egori@altlinux.org> 1.9.15-alt2
- disable passim for p10 and older branches

* Mon Mar 25 2024 Egor Ignatov <egori@altlinux.org> 1.9.15-alt1
- 1.9.15

* Fri Feb 16 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.9.13-alt2
- build with libpassim

* Fri Feb 09 2024 Egor Ignatov <egori@altlinux.org> 1.9.13-alt1
- 1.9.13

* Wed Jan 24 2024 Egor Ignatov <egori@altlinux.org> 1.9.12-alt1
- 1.9.12

* Sun Jan 07 2024 Egor Ignatov <egori@altlinux.org> 1.9.11-alt1
- 1.9.11

* Tue Dec 05 2023 Egor Ignatov <egori@altlinux.org> 1.9.10-alt1
- 1.9.10

* Tue Nov 21 2023 Egor Ignatov <egori@altlinux.org> 1.9.9-alt1
- 1.9.9

* Thu Nov 16 2023 Egor Ignatov <egori@altlinux.org> 1.9.8-alt1
- 1.9.8

* Tue Nov 14 2023 Egor Ignatov <egori@altlinux.org> 1.9.7-alt1
- 1.9.7

* Mon Sep 25 2023 Egor Ignatov <egori@altlinux.org> 1.9.5-alt1
- 1.9.5

* Tue Aug 22 2023 Egor Ignatov <egori@altlinux.org> 1.9.4-alt1
- 1.9.3 -> 1.9.4

* Fri Jul 14 2023 Egor Ignatov <egori@altlinux.org> 1.9.3-alt1
- 1.9.2 -> 1.9.3

* Tue Jun 13 2023 Egor Ignatov <egori@altlinux.org> 1.9.2-alt1
- 1.9.1 -> 1.9.2

* Fri May 19 2023 Egor Ignatov <egori@altlinux.org> 1.9.1-alt1
- 1.8.14 -> 1.9.1

* Fri Mar 31 2023 Egor Ignatov <egori@altlinux.org> 1.8.14-alt1
- New version 1.8.14.

* Mon Feb 27 2023 Egor Ignatov <egori@altlinux.org> 1.8.12-alt1
- 1.8.10 -> 1.8.12

* Tue Jan 31 2023 Egor Ignatov <egori@altlinux.org> 1.8.10-alt1
- 1.8.9 -> 1.8.10

* Tue Jan 03 2023 Egor Ignatov <egori@altlinux.org> 1.8.9-alt1
- 1.8.8 -> 1.8.9

* Fri Dec 16 2022 Egor Ignatov <egori@altlinux.org> 1.8.8-alt1
- 1.8.7 -> 1.8.8
- enable tests for all architectures
- start tests with vm-run only if uefi enabled
- aarch64: disable 'lenovo-thinklmi-self-test'

* Wed Nov 23 2022 Egor Ignatov <egori@altlinux.org> 1.8.7-alt1
- 1.8.5 -> 1.8.7
- run tests in qemu (vm-run)
- clean up spec

* Sun Sep 25 2022 Anton Farygin <rider@altlinux.ru> 1.8.5-alt1
- 1.8.4 -> 1.8.5

* Mon Sep 19 2022 Anton Farygin <rider@altlinux.ru> 1.8.4-alt1
- 1.8.1 -> 1.8.4

* Sat Jun 04 2022 Anton Farygin <rider@altlinux.ru> 1.8.1-alt1
- 1.8.0 -> 1.8.1

* Thu May 12 2022 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.7.7 -> 1.8.0

* Mon Apr 11 2022 Anton Farygin <rider@altlinux.ru> 1.7.7-alt1
- 1.7.6 -> 1.7.7

* Mon Mar 28 2022 Anton Farygin <rider@altlinux.ru> 1.7.6-alt1
- 1.7.5 -> 1.7.6

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 1.7.5-alt1
- 1.7.5
- switched to use /usr/libexec for libexecdir instead of /usr/lib

* Thu Jan 27 2022 Ivan A. Melnikov <iv@altlinux.org> 1.7.4-alt2
- enable build with flashrom on all architectures

* Wed Jan 26 2022 Anton Farygin <rider@altlinux.ru> 1.7.4-alt1
- 1.7.3 -> 1.7.4

* Fri Dec 24 2021 Anton Farygin <rider@altlinux.ru> 1.7.3-alt1
- 1.7.2 -> 1.7.3

* Thu Dec 02 2021 Nikolai Kostrigin <nickel@altlinux.org> 1.7.2-alt3
- improve package backportability by unconditionally not packing
  of fwupd-detect-cet on ix86 at all

* Thu Dec 02 2021 Nikolai Kostrigin <nickel@altlinux.org> 1.7.2-alt2
- remove unused BR: gi-docgen causing extensive dependencies on python modules
- update minimal required version of libgusb to 0.3.5

* Mon Nov 22 2021 Anton Farygin <rider@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Nov 15 2021 Anton Farygin <rider@altlinux.ru> 1.7.1-alt1
- 1.7.1
- built with flashrom support
- removed labels subpackage
- enabled redfish and nvme plugins for all architectures
- removed ExclusiveArch - try build it for e2k

* Wed Jun 23 2021 Egor Ignatov <egori@altlinux.org> 1.6.1-alt1
- 1.6.1
- cleanup spec
- enable man pages

* Thu Apr 15 2021 Anton Farygin <rider@altlinux.org> 1.5.9-alt1
- 1.5.9

* Fri Apr 09 2021 Nikolai Kostrigin <nickel@altlinux.org> 1.5.8-alt2
- add ALT release information to SBAT section

* Thu Mar 25 2021 Anton Farygin <rider@altlinux.org> 1.5.8-alt1
- 1.5.8

* Tue Mar 09 2021 Anton Farygin <rider@altlinux.org> 1.5.7-alt1
- 1.5.7

* Fri Feb 19 2021 Anton Farygin <rider@altlinux.org> 1.5.6-alt1
- 1.5.6

* Thu Feb 04 2021 Nikita Ermakov <arei@altlinux.org> 1.5.5-alt2
- Added riscv64 to ExclusiveArch tag
- Removed extra libefivar-devel BR

* Wed Jan 13 2021 Anton Farygin <rider@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Thu Dec 24 2020 Anton Farygin <rider@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Wed Nov 25 2020 Anton Farygin <rider@altlinux.ru> 1.5.2-alt1
- 1.5.2
- cleanup build requires

* Mon Nov 09 2020 Anton Farygin <rider@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue Sep 15 2020 Anton Farygin <rider@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Wed Aug 05 2020 Anton Farygin <rider@altlinux.ru> 1.4.5-alt1
- 1.4.5
- the package with tests became architecture-dependent due to the arm platform

* Sat Jun 13 2020 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Thu May 21 2020 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Mon Mar 30 2020 Anton Farygin <rider@altlinux.ru> 1.3.9-alt2
- 1.3.9

* Thu Mar 26 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.8-alt2
- Rebuilt with libgusb 0.3.4 due to broken symbol versioning
  of g_usb_version_string function.
- Added explicit libgusb >= 0.3.4 dependency.

* Wed Feb 19 2020 Anton Farygin <rider@altlinux.ru> 1.3.8-alt1
- 1.3.8

* Sun Feb 02 2020 Anton Farygin <rider@altlinux.ru> 1.3.7-alt1
- 1.3.7

* Fri Jan 10 2020 Anton Farygin <rider@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Fri Dec 27 2019 Anton Farygin <rider@altlinux.ru> 1.3.5-alt2
- added gcab to requires list (used in firmware_packager.py)

* Mon Dec 02 2019 Anton Farygin <rider@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Mon Nov 25 2019 Anton Farygin <rider@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Tue Nov 19 2019 Anton Farygin <rider@altlinux.ru> 1.3.3-alt2
- fixed work with EFI secure boot (closes: #37486)

* Thu Nov 07 2019 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- 1.3.3
- enabled tests

* Mon Sep 30 2019 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Mon Sep 16 2019 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Mon Jul 15 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.9-alt2
- Added ppc64le to ExclusiveArch tag.

* Fri May 24 2019 Anton Farygin <rider@altlinux.ru> 1.2.9-alt1
- 1.2.9

* Thu Apr 25 2019 Anton Farygin <rider@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Tue Apr 16 2019 Anton Farygin <rider@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Mon Apr 01 2019 Anton Farygin <rider@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Wed Mar 06 2019 Anton Farygin <rider@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Mon Feb 11 2019 Anton Farygin <rider@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Mon Jan 07 2019 Anton Farygin <rider@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Mon Dec 03 2018 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Mon Nov 12 2018 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Wed Oct 17 2018 Anton Farygin <rider@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Mon Sep 03 2018 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Tue Jul 31 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri May 04 2018 Anton Farygin <rider@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Thu Mar 22 2018 Anton Farygin <rider@altlinux.ru> 1.0.6-alt1
- new version
- temporarily disabled check section due to impossible testing of the thunderbolt interface in the hasher environment

* Wed Mar 07 2018 Anton Farygin <rider@altlinux.ru> 1.0.5-alt1
- first build for ALT, based on RH spec

