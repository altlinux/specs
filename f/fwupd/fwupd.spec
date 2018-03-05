%def_enable tests
%def_enable dummy

# fwupdate is only available on these arches
%ifarch x86_64 aarch64
%def_enable uefi
%endif

# libsmbios is only available on x86, and fwupdate is available on just x86_64
%ifarch x86_64
%def_enable dell
%endif

Summary: Firmware update daemon
Name: fwupd
Version: 1.0.6
Release: alt1
License: GPLv2+
Group: System/Configuration/Hardware
Url: https://github.com/hughsie/fwupd
Source0: %name-%version.tar

BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: libappstream-glib-devel
BuildRequires: libjson-glib-devel
BuildRequires: libgudev-devel
BuildRequires: libudev-devel
BuildRequires: libgusb-devel
BuildRequires: libsoup-devel
BuildRequires: libsoup-gir-devel
BuildRequires: libcolord-devel
BuildRequires: libpolkit-devel
BuildRequires: libsqlite3-devel
BuildRequires: libsystemd-devel
BuildRequires: libgpgme-devel
BuildRequires: systemd 
BuildRequires: libumockdev-devel
BuildRequires: gcab
BuildRequires: libarchive-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgcab-devel
BuildRequires: valgrind-devel
BuildRequires: libelf-devel
BuildRequires: gtk-doc
BuildRequires: libuuid-devel
BuildRequires: libgnutls-devel
BuildRequires: gnutls-utils
BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: help2man

%if_enabled uefi
BuildRequires: python3 python3-module-pycairo python3-module-pygobject3 python3-module-Pillow
BuildRequires: libpango-devel
BuildRequires: libcairo-devel libcairo-gobject-devel
BuildRequires: libfreetype-devel
BuildRequires: fontconfig
BuildRequires: fonts-ttf-dejavu
%endif

%if_enabled dell
BuildRequires: libefivar-devel
BuildRequires: libsmbios-devel
%endif

%if_enabled uefi
BuildRequires: fwupdate-devel
%endif
Requires: fwupd-labels = %EVR
Requires: bubblewrap

%description
fwupd is a daemon to allow session software to update device firmware.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Files for development with %name.

%package labels
Group: System/Configuration/Hardware
Summary: Rendered labels for display during system firmware updates
# RedHat: BuildArch: noarch is disabled as we can get "different" .BMP files even when
# running the build on the same architecture due to the randomness introduced
# by the TTF files.

%description labels
Rendered labels for display during system firmware updates.

%package tests
Group: System/Configuration/Hardware
Summary: Data files for installed tests
BuildArch: noarch

%description tests
Data files for installed tests.

%prep
%setup

%build
%meson \
    -Dgtkdoc=true \
    -Dman=false \
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
    -Dplugin_uefi=true \
    -Dplugin_uefi_labels=true \
%else
    -Dplugin_uefi=false \
    -Dplugin_uefi_labels=false \
%endif
%if_enabled dell
    -Dplugin_dell=true \
    -Dplugin_synaptics=true \
%else
    -Dplugin_dell=false \
    -Dplugin_synaptics=false \
%endif
    -Dplugin_colorhug=true

%meson_build

%if_enabled tests
%check
export LD_LIBRARY_PATH=%buildroot%_libdir 
#meson_test
%endif

%install
%meson_install

mkdir -p --mode=0700 %buildroot%_localstatedir/fwupd/gnupg

%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS NEWS COPYING
%config(noreplace)%_sysconfdir/fwupd/daemon.conf
%dir %_libexecdir/fwupd
%_libexecdir/fwupd/fwupd
%_bindir/dfu-tool
%_bindir/fwupdmgr
%dir %_sysconfdir/fwupd
%dir %_sysconfdir/fwupd/remotes.d
%_sysconfdir/fwupd/remotes.d/fwupd.conf
%_sysconfdir/fwupd/remotes.d/lvfs.conf
%_sysconfdir/fwupd/remotes.d/lvfs-testing.conf
%_sysconfdir/fwupd/remotes.d/vendor.conf
%_sysconfdir/pki/fwupd
%_sysconfdir/pki/fwupd-metadata
%_sysconfdir/dbus-1/system.d/org.freedesktop.fwupd.conf
%_datadir/fwupd/remotes.d/fwupd/metadata.xml
%_datadir/fwupd/remotes.d/vendor/firmware
%_datadir/dbus-1/interfaces/org.freedesktop.fwupd.xml
%_datadir/polkit-1/actions/org.freedesktop.fwupd.policy
%_datadir/polkit-1/rules.d/org.freedesktop.fwupd.rules
%_datadir/dbus-1/system-services/org.freedesktop.fwupd.service
%_datadir/metainfo/org.freedesktop.fwupd.metainfo.xml
%_datadir/fwupd/firmware-packager
%_datadir/bash-completion/completions/fwupdmgr
%_unitdir/fwupd-offline-update.service
%_unitdir/fwupd.service
%_unitdir/system-update.target.wants/
%dir %_localstatedir/fwupd
%dir %_datadir/fwupd/quirks.d
%dir %_localstatedir/fwupd/builder
%_localstatedir/fwupd/builder/README.md
%_datadir/fwupd/quirks.d/*.quirk
%_libdir/libfwupd*.so.*
%_libdir/girepository-1.0/Fwupd-2.0.typelib
/lib/udev/rules.d/*.rules
%dir %_libdir/fwupd-plugins-3
%_libdir/fwupd-plugins-3/libfu_plugin_altos.so
%_libdir/fwupd-plugins-3/libfu_plugin_csr.so
%_libdir/fwupd-plugins-3/libfu_plugin_amt.so
%_libdir/fwupd-plugins-3/libfu_plugin_colorhug.so
%if_enabled dell
%_libdir/fwupd-plugins-3/libfu_plugin_dell.so
%endif
%_libdir/fwupd-plugins-3/libfu_plugin_dfu.so
%_libdir/fwupd-plugins-3/libfu_plugin_ebitdo.so
%_libdir/fwupd-plugins-3/libfu_plugin_nitrokey.so
%_libdir/fwupd-plugins-3/libfu_plugin_steelseries.so
%if_enabled dell
%_libdir/fwupd-plugins-3/libfu_plugin_synapticsmst.so
%endif
%if_enabled dummy
%_libdir/fwupd-plugins-3/libfu_plugin_test.so
%endif
%_libdir/fwupd-plugins-3/libfu_plugin_thunderbolt.so
%_libdir/fwupd-plugins-3/libfu_plugin_thunderbolt_power.so
%_libdir/fwupd-plugins-3/libfu_plugin_udev.so
%if_enabled uefi
%_libdir/fwupd-plugins-3/libfu_plugin_uefi.so
%config(noreplace)%_sysconfdir/fwupd/uefi.conf
%endif
%_libdir/fwupd-plugins-3/libfu_plugin_unifying.so
%_libdir/fwupd-plugins-3/libfu_plugin_upower.so
%ghost %_localstatedir/fwupd/gnupg

%files devel
%_datadir/gir-1.0/Fwupd-2.0.gir
%_datadir/gtk-doc/html/libfwupd
%_includedir/fwupd-1
%_libdir/libfwupd*.so
%_libdir/pkgconfig/fwupd.pc

%files labels
%if_enabled uefi
%_datadir/locale/*/LC_IMAGES/fwupd*
%endif

%files tests
%dir %_datadir/installed-tests/fwupd
%_datadir/installed-tests/fwupd/firmware-example.xml.gz
%_datadir/installed-tests/fwupd/firmware-example.xml.gz.asc
%_datadir/installed-tests/fwupd/*.test
%_datadir/installed-tests/fwupd/*.cab
%_datadir/installed-tests/fwupd/*.sh
%_datadir/installed-tests/fwupd/*.py*

%changelog
* Thu Mar 22 2018 Anton Farygin <rider@altlinux.ru> 1.0.6-alt1
- new version
- temporarily disabled check section due to impossible testing of the thunderbolt interface in the hasher environment

* Wed Mar 07 2018 Anton Farygin <rider@altlinux.ru> 1.0.5-alt1
- first build for ALT, based on RH spec

