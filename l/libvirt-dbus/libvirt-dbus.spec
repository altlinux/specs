# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
# -*- rpm-spec -*-

%global meson_version 0.49.0
%global glib2_version 2.44.0
%global libvirt_version 3.1.0
%global libvirt_glib_version 0.0.7
%global system_user libvirtdbus

Name:    libvirt-dbus
Version: 1.4.1
Release: alt2
Summary: libvirt D-Bus API binding
License: LGPL-2.1-or-later
Group:   System/Libraries
Url:     https://libvirt.org/
Source0: https://libvirt.org/sources/dbus/%name-%version.tar.xz
Patch:   alt-service-option.patch

BuildRequires: gcc
BuildRequires: meson >= %meson_version
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: libvirt-devel >= %libvirt_version
BuildRequires: libvirt-glib-devel libvirt-glib-gir-devel
BuildRequires: python3-module-docutils python3-module-flake8
BuildRequires: rpm-macros-systemd
BuildRequires: libsystemd-devel libudev-devel systemd systemd-analyze systemd-homed systemd-networkd systemd-portable systemd-sysvinit

Requires: dbus
Requires: libgio >= %glib2_version
Requires: libvirt-libs >= %libvirt_version
Requires: libvirt-glib-gir >= %libvirt_glib_version
Requires: polkit

Requires(pre): shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-submap shadow-utils

%description
This package provides D-Bus API for libvirt

%prep
%setup
%patch -p1

%build
%meson \
    -Dinit_script=systemd
%meson_build

%install
%meson_install

%pre
getent group %system_user >/dev/null || groupadd -r %system_user
getent passwd %system_user >/dev/null || \
    useradd -r -g %system_user -d / -s /sbin/nologin \
    -c "Libvirt D-Bus bridge" %system_user
exit 0

%post
%post_service %name
%systemd_user_post %name.service

%preun
%preun_service %name
%systemd_user_preun %name.service

%postun
%systemd_user_postun_with_restart %name.service

%files
%doc NEWS.rst
%doc COPYING
%_sbindir/libvirt-dbus
%_unitdir/libvirt-dbus.service
%_userunitdir/libvirt-dbus.service
%_datadir/dbus-1/services/org.libvirt.service
%_datadir/dbus-1/system-services/org.libvirt.service
%_datadir/dbus-1/system.d/org.libvirt.conf
%_datadir/dbus-1/interfaces/org.libvirt.*.xml
%_datadir/polkit-1/rules.d/libvirt-dbus.rules
%_mandir/man8/libvirt-dbus.8*

%changelog
* Tue Jul 02 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.4.1-alt2
- Bump release number to correct upgrade from Autoimports to Sisyphus

* Mon Jul 01 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.4.1-alt1
- prepare port to Sisyphus

* Sat Mar 23 2024 Igor Vlasenko <viy@altlinux.org> 1.4.1-alt1_4
- update to new release by fcimport

* Fri Dec 01 2023 Igor Vlasenko <viy@altlinux.org> 1.4.1-alt1_2
- update to new release by fcimport

* Thu Aug 31 2023 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt2_8
- update to new release by fcimport

* Wed Feb 22 2023 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt2_7
- update to new release by fcimport

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt2_6
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt2_5
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt2_4
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt2_3
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_2
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- update to new release by fcimport

* Sat Jun 13 2020 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_4
- update to new release by fcimport

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3
- new version

