%define _libexecdir %_prefix/libexec
%def_disable snapshot

%define ver_major 0.14
%define beta %nil
%define api_ver 0
%define ui_api_ver 1
%define namespace Malcontent
%define xdg_name org.freedesktop.Malcontent
%define xdg_name1 org.freedesktop.MalcontentControl

# subprojects
%define libgsystemservice_ver 0.3.0
%define gvdb_ver 466fc220
%define tinycdb_ver 0.81

%def_disable check
%def_enable ui

Name: malcontent
Version: %ver_major.0
Release: alt1%beta

Summary: Parental controls implementation
Group: Security/Networking
License: LGPL-2.1-or-later and GPL-2.0-or-later
Url: https://gitlab.freedesktop.org/pwithnall/malcontent/

Vcs: https://gitlab.freedesktop.org/pwithnall/malcontent.git

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version%beta.tar.bz2
%else
Source: %name-%version%beta.tar
%endif
Source1: gvdb-%gvdb_ver.tar
Source2: libgsystemservice-%libgsystemservice_ver.tar
# our tinycdb is too old and unupdateble: @core
Source3: https://www.corpit.ru/mjt/tinycdb/tinycdb-%tinycdb_ver.tar.gz

%define glib_ver 2.54.2
%define gtk4_ver 4.12
%define adwaita_ver 1.6
%define accountsservice_ver 0.6.39
%define appstream_ver 0.12.10
%define flatpak_ver 1.14

Requires: lib%name = %EVR
Requires: polkit accountsservice >= %accountsservice_ver

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-macros-pam0 rpm-build-gir
BuildRequires: meson yelp-tools gi-docgen reuse
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(accountsservice) >= %accountsservice_ver
BuildRequires: pkgconfig(appstream) >= %appstream_ver
BuildRequires: pkgconfig(flatpak) >= %flatpak_ver
BuildRequires: pkgconfig(gobject-introspection-1.0) gir(AccountsService) = 1.0
BuildRequires: pam-devel
BuildRequires: libglib-testing-devel
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsystemd)
%{?_enable_ui:BuildRequires: pkgconfig(gtk4) >= %gtk4_ver gir(Gtk) = 4.0
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver gir(Adw) = 1}
%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstreamcli}
# for tinycdb
BuildRequires: libcdb-devel

%description
%name implements parental controls support which can be used by
applications to filter or limit the access of child accounts to
inappropriate content.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries
License: LGPL-2.1-or-later

%description -n lib%name
This package contains libmalcontent.

%package -n lib%name-gir
Summary: GObject introspection data for lib%name
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the %name library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
License: LGPL-2.1-or-later
Requires: lib%name = %EVR

%description -n lib%name-devel
This package provides development headers and libraries for %name
library.

%package -n lib%name-ui
Summary: UI library for %name
Group: System/Libraries
License: LGPL-2.1-or-later
Requires: lib%name = %EVR

%description -n lib%name-ui
This package provides shared %name-ui library.

%package -n lib%name-ui-gir
Summary: GObject introspection data for lib%name-ui
Group: System/Libraries
Requires: lib%name-ui = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name-ui-gir
GObject introspection data for the %name-ui library.

%package -n lib%name-ui-devel
Summary: Development files for lib%name-ui
License: LGPL-2.1-or-later
Group: Development/C
Requires: lib%name-ui = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-ui-devel
This package provides development headers and libraries for %name-ui
library.

%package control
Summary: Parental Controls UI
Group: Security/Networking
License: GPL-2.0-or-later
Requires: %name = %EVR
Requires: lib%name = %EVR
Requires: lib%name-ui = %EVR

%description control
This package contains a user interface for querying and setting parental
controls for users.

%package pam
Summary: Parental Controls PAM Module
Group: System/Base
License: LGPL-2.1-or-later
Requires: lib%name = %EVR

%description pam
This package contains a PAM module which prevents logins for users who
have exceeded their allowed computer time.

%package tools
Summary: Parental Controls Tools
Group: Security/Networking
License: GPL-2.0-or-later
Requires: lib%name = %EVR
Requires: lib%name-gir = %EVR

%description tools
This package contains tools for querying and updating the parental
controls settings for users.

%prep
%setup -n %name-%version%beta -a1 -a2 -a3
mv gvdb-%gvdb_ver/* subprojects/gvdb/
mv libgsystemservice-%libgsystemservice_ver subprojects/libgsystemservice
mv tinycdb-%tinycdb_ver subprojects/
cp subprojects/packagefiles/tinycdb/meson.build subprojects/tinycdb-%tinycdb_ver

%build
%meson -Dpamlibdir=%_pam_modules_dir \
       %{subst_enable_meson_feature ui ui}
%nil
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%check
%__meson_test

%files -f %name.lang
%_libexecdir/%name-timer-extension-agent
%_libexecdir/%name-timerd
%_libexecdir/%name-webd
%_libexecdir/%name-webd-update
%_unitdir/%name-timer-extension-agent.service
%_unitdir/%name-timerd.service
%_unitdir/%name-webd-update.service
%_unitdir/%name-webd-update.timer
%_unitdir/%name-webd.service
%_datadir/accountsservice/interfaces/*.xml
%_datadir/dbus-1/interfaces/*.xml
%_datadir/dbus-1/services/%xdg_name1.service
%_datadir/dbus-1/system-services/%{xdg_name}Timer1.ExtensionAgent.service
%_datadir/dbus-1/system-services/%{xdg_name}Timer1.service
%_datadir/dbus-1/system-services/%{xdg_name}Web1.service
%_datadir/dbus-1/system.d/%{xdg_name}Timer1.ExtensionAgent.conf
%_datadir/dbus-1/system.d/%{xdg_name}Timer1.conf
%_datadir/dbus-1/system.d/%{xdg_name}Web1.conf
%_datadir/polkit-1/actions/*.policy
%_datadir/polkit-1/rules.d/*.rules
%_sysusersdir/%name-timer-extension-agent.conf
%_sysusersdir/%name-timerd.conf
%_sysusersdir/%name-webd.conf
%_man8dir/%name-timer-extension-agent.8*
%_man8dir/%name-timerd.8*
%_man8dir/%name-webd.8*
%doc README.md NEWS

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*
%_libdir/libnss_%name.so.*

%files -n lib%name-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n lib%name-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_libdir/libnss_%name.so
%_pkgconfigdir/%name-%api_ver.pc
%_girdir/%namespace-%api_ver.gir

%if_enabled ui
%files -n lib%name-ui
%_libdir/lib%name-ui-%ui_api_ver.so.*

%files -n lib%name-ui-gir
%_typelibdir/%{namespace}Ui-%ui_api_ver.typelib

%files -n lib%name-ui-devel
%_libdir/lib%name-ui-%ui_api_ver.so
%_includedir/%name-ui-%ui_api_ver/
%_pkgconfigdir/%name-ui-%ui_api_ver.pc
%_girdir/%{namespace}Ui-%ui_api_ver.gir

%files control
%_bindir/%name-control
%_desktopdir/%xdg_name1.desktop
%_iconsdir/hicolor/scalable/apps/%xdg_name1.svg
%_iconsdir/hicolor/symbolic/apps/%xdg_name1-symbolic.svg
%_datadir/metainfo/%xdg_name1.metainfo.xml
%endif

%files pam
%_pam_modules_dir/pam_%{name}.so

%files tools
%_bindir/%name-client
%_man8dir/%name-client.*

%exclude %_datadir/doc/lib%name-%api_ver/
%exclude %_datadir/doc/lib%name-ui-%ui_api_ver/

%changelog
* Wed Mar 18 2026 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Wed Sep 03 2025 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Mon Nov 11 2024 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Wed Mar 20 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0 (ui ported to GTK4/libadwaita)

* Wed Jun 01 2022 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5

* Thu Mar 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Wed Nov 10 2021 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Tue Oct 12 2021 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- updated to 0.10.2-8-gb311cbd

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1
- BR: +rpm-build-python3

* Thu Dec 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Thu Sep 17 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- first build for Sisyphus


