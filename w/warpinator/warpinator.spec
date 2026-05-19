%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name warpinator
%define ver_major 2.0
%define rdn_name org.x.Warpinator

%def_enable bundle_zeroconf
%def_enable bundle_landlock
%def_disable bundle_grpc

%def_enable check

Name: %_name
Version: %ver_major.4
Release: alt1

Summary: Warpinator - send and receive files across a local network
License: Apache-2.0
Group: Networking/File transfer
Url: https://github.com/linuxmint/warpinator

#BuildArch: noarch

Vcs: https://github.com/linuxmint/warpinator.git

%if_disabled snapshot
Source: https://github.com/linuxmint/warpinator/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%add_python3_path %_libexecdir/%_name
%add_python3_req_skip google

Requires: python3-module-pygobject3
Requires: typelib(Gtk) = 3.0
Requires: typelib(XApp) = 1.0
Requires: dconf polkit

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir rpm-build-xdg
BuildRequires: pkgconfig(python3) python3(setuptools)
BuildRequires: meson /usr/bin/glib-compile-resources
BuildRequires: gtk-update-icon-cache
BuildRequires: itstool libpolkit-devel
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstream-util
BuildRequires: /usr/bin/glib-compile-schemas}

%description
Warpinator is a GTK+3 app to send and receive files across a local network.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool bundle_zeroconf bundle-zeroconf} \
    %{subst_enable_meson_bool bundle_landlock bundle-landlock} \
    %{subst_enable_meson_bool bundle_grpc bundle-grpc}
%nil
%meson_build

%install
%meson_install
%find_lang %_name

%check
%__meson_test

%files -f %name.lang
%_xdgconfigdir/autostart/%_name-autostart.desktop
%_bindir/%_name
%_bindir/%_name-send
%_libexecdir/%_name/
%_datadir/%_name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/polkit-1/actions/org.x.warpinator.policy
%_datadir/metainfo/%rdn_name.appdata.xml
%_datadir/nemo/actions/%_name-send-check
%_datadir/nemo/actions/%_name-send.nemo_action
%doc README*

%changelog
* Tue May 19 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Fri Jan 09 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Sat Dec 13 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Dec 11 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Sat Nov 22 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Fri Aug 01 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.10-alt1
- 1.8.10

* Fri Jul 25 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.9-alt1
- 1.8.9

* Sat Feb 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.8-alt1
- first build for Sisyphus
