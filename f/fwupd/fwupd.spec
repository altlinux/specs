%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%def_enable tests
%def_enable dummy

# fwupdate is only available on these arches
%ifarch x86_64 aarch64
%def_enable uefi
%endif

%ifarch x86_64 %ix86
%def_enable msr
%endif

# libsmbios is only available on x86, and fwupdate is available on just x86_64
%ifarch x86_64
%def_enable dell
%endif

%def_enable flashrom

%define fwupd_plugins_version 5
%define fwupd_pluginsdir %_libdir/fwupd-plugins-%fwupd_plugins_version

Summary: Firmware update daemon
Name: fwupd
Version: 1.7.6
Release: alt1
License: LGPL-2.1+
Group: System/Configuration/Hardware
Url: https://github.com/fwupd/fwupd
Source0: %name-%version.tar
Source2: fwupd.watch
Patch0: %name-%version-alt.patch
BuildRequires: bash-completion
BuildRequires: cmake
BuildRequires: gcab
BuildRequires: rpm-build-python3
BuildRequires: git-core
BuildRequires: gtk-doc
BuildRequires: libappstream-glib-devel
BuildRequires: libprotobuf-c-devel
BuildRequires: /usr/bin/protoc /usr/bin/protoc-gen-c
BuildRequires: libarchive-devel
BuildRequires: libcolord-devel
BuildRequires: libcurl-devel
BuildRequires: libelf-devel
BuildRequires: libgcab-devel
BuildRequires: libgnutls-devel
BuildRequires: libgpgme-devel
BuildRequires: libgudev-devel
BuildRequires: libgusb-gir-devel
BuildRequires: libjcat-devel >= 0.1.10
BuildRequires: libpango-devel
BuildRequires: libpolkit-devel
%if_enabled dell
BuildRequires: libsmbios-devel
%endif
%if_enabled flashrom
BUildRequires: libflashrom-devel
%endif
BuildRequires: libsoup-devel
BuildRequires: libsqlite3-devel
BuildRequires: libsystemd-devel
BuildRequires: libtpm2-tss-devel
BuildRequires: libudev-devel
BuildRequires: libumockdev-devel
BuildRequires: libuuid-devel
BuildRequires: libxmlb-devel
BuildRequires: meson
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-pygobject3
BuildRequires: vala-tools
BuildRequires: /proc

%if_enabled uefi
BuildRequires: libpango-devel
BuildRequires: libcairo-devel libcairo-gobject-devel
BuildRequires: libfreetype-devel
BuildRequires: fontconfig
BuildRequires: fonts-ttf-dejavu
BuildRequires: gnu-efi libefivar-devel
Requires: gcab
Requires: fwupd-efi
Provides: fwupdate
Obsoletes: fwupdate
%endif

Requires: bubblewrap
Requires: libgusb >= 0.3.5

Obsoletes: fwupd-labels <= %EVR

%description
fwupd is a daemon to allow session software to update device firmware.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Files for development with %name.

%package tests
Group: System/Configuration/Hardware
Summary: Data files for installed tests

%description tests
Data files for installed tests.

%prep
%setup
%patch0 -p1

%build
%meson \
    -Ddocs=gtkdoc \
    -Dfirmware-packager=true \
    -Dman=true \
    -Dlvfs=true \
    -Dsupported_build=true \
    -Dplugin_flashrom=true \
%if_enabled msr
    -Dplugin_msr=true \
%else
    -Dplugin_msr=false \
%endif
%if_enabled tests
    -Dtests=true \
%else
    -Dtests=false \
%endif
%if_enabled dummy
    -Dplugin_dummy=true \
%else
    -Dplugin_dummy=false \
%endif
    -Dplugin_thunderbolt=true \
%if_enabled uefi
    -Dplugin_uefi_capsule=true \
    -Dplugin_uefi_pk=true \
    -Defi_binary=false \
%else
    -Dplugin_redfish=true \
    -Dplugin_uefi_capsule=false \
    -Dplugin_uefi_pk=false \
    -Dplugin_nvme=true \
%endif
%if_enabled dell
    -Dplugin_dell=true \
    -Dplugin_synaptics_mst=true \
%else
    -Dplugin_dell=false \
    -Dplugin_synaptics_mst=false \
%endif

%meson_build

%if_enabled tests
%check
export LD_LIBRARY_PATH=%buildroot%_libdir
export FWUPD_PLUGINDIR=%buildroot%fwupd_pluginsdir/  
%meson_test
%endif

%install
%meson_install
%ifarch %ix86
rm -f %buildroot%_libexecdir/fwupd/fwupd-detect-cet ||:
%endif

mkdir -p --mode=0700 %buildroot%_localstatedir/fwupd/gnupg
rm -rf %buildroot%_docdir/fwupd

%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS COPYING
%_man1dir/fwupdtool.1*
%_man1dir/fwupdagent.1*
%_man1dir/fwupdmgr.1*
%_man1dir/dfu-tool.1*
%if_enabled uefi
%_man1dir/fwupdate.1*
%_man1dir/dbxtool.1*
%endif
%config(noreplace)%_sysconfdir/fwupd/daemon.conf
%config(noreplace)%_sysconfdir/fwupd/thunderbolt.conf
%dir %_libexecdir/fwupd
%dir %_iconsdir/hicolor/scalable/apps
%_libexecdir/fwupd/fwupd
%_bindir/fwupdtool
%_bindir/fwupdagent
%_libexecdir/fwupd/fwupdoffline
%ifarch x86_64
%_libexecdir/fwupd/fwupd-detect-cet
%endif
%_datadir/bash-completion/completions/*
%_datadir/fish/vendor_completions.d/fwupdmgr.fish
%_iconsdir/hicolor/scalable/apps/org.freedesktop.fwupd.svg
%if_enabled uefi
%_bindir/fwupdate
%endif
%_bindir/dfu-tool
%if_enabled uefi
%_bindir/dbxtool
%endif
%_bindir/fwupdmgr
%dir %_sysconfdir/fwupd
%dir %_sysconfdir/fwupd/remotes.d
%config(noreplace)%_sysconfdir/fwupd/remotes.d/*.conf
%exclude %_sysconfdir/fwupd/remotes.d/fwupd-tests.conf
%_sysconfdir/pki/fwupd
%_sysconfdir/pki/fwupd-metadata
%dir %_datadir/fwupd
%dir %_datadir/fwupd/metainfo
%dir %_datadir/fwupd/remotes.d
%dir %_datadir/fwupd/remotes.d/vendor
%_datadir/dbus-1/system.d/org.freedesktop.fwupd.conf
%ifarch x86_64
%dir %_datadir/fwupd/remotes.d/dell-esrt
%_datadir/fwupd/remotes.d/dell-esrt/metadata.xml
%endif
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
%_presetdir/fwupd-refresh.preset
%_unitdir/fwupd-offline-update.service
%_unitdir/fwupd.service
%_unitdir/fwupd-refresh.timer
%_unitdir/fwupd-refresh.service
%_unitdir/system-update.target.wants/
/lib/systemd/system-shutdown/fwupd.shutdown
%dir %_localstatedir/fwupd
%dir %_datadir/fwupd/quirks.d
%_datadir/fwupd/quirks.d/*.quirk
%_libdir/libfwupd*.so.*
%_libdir/girepository-1.0/Fwupd-2.0.typelib
%_libdir/girepository-1.0/FwupdPlugin-1.0.typelib
/lib/udev/rules.d/*.rules
%dir %fwupd_pluginsdir
%fwupd_pluginsdir/libfu_plugin_ata.so
%fwupd_pluginsdir/libfu_plugin_amt.so
%fwupd_pluginsdir/libfu_plugin_acpi_dmar.so
%fwupd_pluginsdir/libfu_plugin_acpi_facp.so
%fwupd_pluginsdir/libfu_plugin_acpi_phat.so
%fwupd_pluginsdir/libfu_plugin_bcm57xx.so
%fwupd_pluginsdir/libfu_plugin_ccgx.so
%fwupd_pluginsdir/libfu_plugin_colorhug.so
%fwupd_pluginsdir/libfu_plugin_cpu.so
%fwupd_pluginsdir/libfu_plugin_cros_ec.so
%if_enabled dell
%fwupd_pluginsdir/libfu_plugin_dell.so
%fwupd_pluginsdir/libfu_plugin_dell_esrt.so
%endif
%fwupd_pluginsdir/libfu_plugin_dell_dock.so
%fwupd_pluginsdir/libfu_plugin_dfu.so
%fwupd_pluginsdir/libfu_plugin_dfu_csr.so
%fwupd_pluginsdir/libfu_plugin_ebitdo.so
%fwupd_pluginsdir/libfu_plugin_elanfp.so
%fwupd_pluginsdir/libfu_plugin_elantp.so
%fwupd_pluginsdir/libfu_plugin_emmc.so
%fwupd_pluginsdir/libfu_plugin_ep963x.so
%fwupd_pluginsdir/libfu_plugin_fresco_pd.so
%fwupd_pluginsdir/libfu_plugin_flashrom.so
%fwupd_pluginsdir/libfu_plugin_genesys.so
%fwupd_pluginsdir/libfu_plugin_goodixmoc.so
%fwupd_pluginsdir/libfu_plugin_hailuck.so
%if_enabled uefi
%fwupd_pluginsdir/libfu_plugin_lenovo_thinklmi.so
%endif
%fwupd_pluginsdir/libfu_plugin_fastboot.so
%fwupd_pluginsdir/libfu_plugin_jabra.so
%fwupd_pluginsdir/libfu_plugin_iommu.so
%fwupd_pluginsdir/libfu_plugin_linux_lockdown.so
%fwupd_pluginsdir/libfu_plugin_linux_sleep.so
%fwupd_pluginsdir/libfu_plugin_linux_swap.so
%fwupd_pluginsdir/libfu_plugin_linux_tainted.so
%fwupd_pluginsdir/libfu_plugin_logitech_hidpp.so
%fwupd_pluginsdir/libfu_plugin_logitech_bulkcontroller.so
%fwupd_pluginsdir/libfu_plugin_logind.so
%if_enabled msr
%fwupd_pluginsdir/libfu_plugin_msr.so
%_modulesloaddir/fwupd-msr.conf
%config(noreplace)%_sysconfdir/fwupd/msr.conf
%endif
%fwupd_pluginsdir/libfu_plugin_mtd.so
%fwupd_pluginsdir/libfu_plugin_nitrokey.so
%fwupd_pluginsdir/libfu_plugin_nordic_hid.so
%fwupd_pluginsdir/libfu_plugin_nvme.so
%fwupd_pluginsdir/libfu_plugin_optionrom.so
%fwupd_pluginsdir/libfu_plugin_parade_lspcon.so
%fwupd_pluginsdir/libfu_plugin_pci_bcr.so
%fwupd_pluginsdir/libfu_plugin_pci_mei.so
%fwupd_pluginsdir/libfu_plugin_pixart_rf.so
%fwupd_pluginsdir/libfu_plugin_powerd.so
%fwupd_pluginsdir/libfu_plugin_redfish.so
%config(noreplace)%_sysconfdir/fwupd/redfish.conf
%_modulesloaddir/fwupd-redfish.conf
%fwupd_pluginsdir/libfu_plugin_realtek_mst.so
%fwupd_pluginsdir/libfu_plugin_rts54hid.so
%fwupd_pluginsdir/libfu_plugin_rts54hub.so
%fwupd_pluginsdir/libfu_plugin_scsi.so
%fwupd_pluginsdir/libfu_plugin_superio.so
%fwupd_pluginsdir/libfu_plugin_steelseries.so
%fwupd_pluginsdir/libfu_plugin_synaptics_cape.so
%fwupd_pluginsdir/libfu_plugin_synaptics_rmi.so
%fwupd_pluginsdir/libfu_plugin_system76_launch.so
%fwupd_pluginsdir/libfu_plugin_synaptics_cxaudio.so
%fwupd_pluginsdir/libfu_plugin_synaptics_prometheus.so
%if_enabled dell
%fwupd_pluginsdir/libfu_plugin_synaptics_mst.so
%endif
%if_enabled dummy
%fwupd_pluginsdir/libfu_plugin_invalid.so
%fwupd_pluginsdir/libfu_plugin_test.so
%endif
%fwupd_pluginsdir/libfu_plugin_thelio_io.so
%fwupd_pluginsdir/libfu_plugin_thunderbolt.so
%fwupd_pluginsdir/libfu_plugin_tpm.so
%if_enabled uefi
%fwupd_pluginsdir/libfu_plugin_bios.so
%fwupd_pluginsdir/libfu_plugin_uefi_capsule.so
%fwupd_pluginsdir/libfu_plugin_uefi_pk.so
%fwupd_pluginsdir/libfu_plugin_uefi_recovery.so
%fwupd_pluginsdir/libfu_plugin_uefi_dbx.so
%config(noreplace)%_sysconfdir/fwupd/uefi_capsule.conf
%config(noreplace)%_sysconfdir/grub.d/35_fwupd
%_datadir/fwupd/uefi-capsule-ux.tar.xz
%endif
%fwupd_pluginsdir/libfu_plugin_uf2.so
%fwupd_pluginsdir/libfu_plugin_usi_dock.so
%fwupd_pluginsdir/libfu_plugin_vli.so
%fwupd_pluginsdir/libfu_plugin_upower.so
%fwupd_pluginsdir/libfu_plugin_wacom_usb.so
%fwupd_pluginsdir/libfu_plugin_wacom_raw.so
%fwupd_pluginsdir/libfu_plugin_analogix.so

%ghost %_localstatedir/fwupd/gnupg

%files devel
%_datadir/gir-1.0/Fwupd-2.0.gir
%_datadir/gir-1.0/FwupdPlugin-1.0.gir
%_datadir/gtk-doc/html/fwupd
%_includedir/fwupd-1
%_libdir/libfwupd*.so
%_libdir/pkgconfig/fwupd.pc
%_libdir/pkgconfig/fwupdplugin.pc
%_datadir/vala/vapi/*

%files tests
%dir %_datadir/installed-tests/fwupd
%dir %_datadir/installed-tests/fwupd/tests
%if_enabled uefi
%_datadir/installed-tests/fwupd/efi
%endif
%_datadir/installed-tests/fwupd/tests/*
%_datadir/installed-tests/fwupd/fwupd-tests.xml
%_datadir/installed-tests/fwupd/*.test
%_datadir/installed-tests/fwupd/*.cab
%_datadir/installed-tests/fwupd/*.sh
%_datadir/fwupd/device-tests/*.json
%_libexecdir/installed-tests/fwupd
%dir %_sysconfdir/fwupd/remotes.d
%config(noreplace)%_sysconfdir/fwupd/remotes.d/fwupd-tests.conf

%changelog
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

