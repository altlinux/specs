%def_disable snapshot
%define _name sysd-manager
%define ver_major 2.20
%define rdn_name io.github.plrigaux.%name
%define bus_name io.github.plrigaux.SysDManager

%def_disable bootstrap

Name: %_name
Version: %ver_major.2
Release: alt1

Summary: A GUI to manage systemd units
License: GPL-3.0
Group: System/Configuration/Boot and Init
Url: https://github.com/plrigaux/sysd-manager

Vcs: https://github.com/plrigaux/sysd-manager.git

%if_disabled snapshot
Source: https://github.com/plrigaux/sysd-manager/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define adw_ver 1.8
%define rust_ver 1.89

Requires: dconf polkit

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo >= %rust_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(libsystemd)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Manage your Services, Timers, Sockets and other units. You can enable,
disable, stop and start them. Also, you can view their config file
and peak at their journal logs.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ -d .cargo ] || mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build --manifest-path %name-proxy/Cargo.toml
%rust_build \
%ifarch %ix86 aarch64
    --config 'profile.release.lto=false' \
%endif
%nil
cargo run -p transtools -- packfiles

%install
%rust_install %name %name-proxy
install -v -Dm644 data/applications/%rdn_name.desktop \
    -t %buildroot%_datadir/applications
install -v -Dm644 data/icons/hicolor/scalable/apps/%rdn_name.svg \
    -t %buildroot%_iconsdir/hicolor/scalable/apps
install -v -Dm644 data/schemas/%rdn_name.gschema.xml \
    -t %buildroot%_datadir/glib-2.0/schemas
install -v -Dm644 data/metainfo/%rdn_name.metainfo.xml \
    -t %buildroot%_datadir/metainfo
cp -r target/locale %buildroot/%_datadir/

install -vDm644 sysd-manager-proxy/data/%bus_name.conf -T  %buildroot/%_datadir/dbus-1/system.d/%bus_name.conf
sed -i 's/{BUS_NAME}/%bus_name/
         s/{DESTINATION}/%bus_name/
         s/{ENVIRONMENT}//
         s/{INTERFACE}/%bus_name/' %buildroot/%_datadir/dbus-1/system.d/%bus_name.conf
install -vDm644 sysd-manager-proxy/data/%bus_name.policy -t %buildroot/%_datadir/polkit-1/actions
install -vDm644 sysd-manager-proxy/data/sysd-manager-proxy.service -T %buildroot%_unitdir/%name-proxy.service
sed -i  's/{BUS_NAME}/%bus_name/
         s/{DESTINATION}/%bus_name/
         s/{ENVIRONMENT}//
         s|{EXECUTABLE}|%_bindir/%name-proxy|
         s/{INTERFACE}/%bus_name/
         s/{SERVICE_ID}/sysd-manager-proxy/' %buildroot%_unitdir/%name-proxy.service


%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-proxy
%_unitdir/%name-proxy.service
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/system.d/%bus_name.conf
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/polkit-1/actions/%bus_name.policy
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc CHANGELOG* README*

%changelog
* Tue Jun 16 2026 Yuri N. Sedunov <aris@altlinux.org> 2.20.2-alt1
- 2.20.2

* Tue Jun 09 2026 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Mon May 25 2026 Yuri N. Sedunov <aris@altlinux.org> 2.19.6-alt1
- 2.19.6

* Sat May 16 2026 Yuri N. Sedunov <aris@altlinux.org> 2.19.4-alt1
- 2.19.4

* Tue Apr 28 2026 Yuri N. Sedunov <aris@altlinux.org> 2.19.2-alt1
- 2.19.2

* Fri Apr 24 2026 Yuri N. Sedunov <aris@altlinux.org> 2.19.1-alt1
- 2.19.1

* Sat Apr 18 2026 Yuri N. Sedunov <aris@altlinux.org> 2.18.0-alt1
- 2.18.0

* Fri Apr 03 2026 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0

* Tue Mar 24 2026 Yuri N. Sedunov <aris@altlinux.org> 2.14.8-alt1
- 2.14.8

* Sat Feb 21 2026 Yuri N. Sedunov <aris@altlinux.org> 2.13.2-alt1
- 2.13.2

* Fri Feb 06 2026 Yuri N. Sedunov <aris@altlinux.org> 2.12.5-alt1
- 2.12.5

* Tue Jan 27 2026 Yuri N. Sedunov <aris@altlinux.org> 2.12.2-alt1
- 2.12.2

* Thu Jan 15 2026 Yuri N. Sedunov <aris@altlinux.org> 2.11.5-alt1
- 2.11.5

* Tue Nov 11 2025 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- 2.7.1

* Wed Nov 05 2025 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Sun Oct 26 2025 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri Oct 24 2025 Yuri N. Sedunov <aris@altlinux.org> 2.5.2-alt1
- 2.5.2

* Sun Oct 19 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Thu Oct 16 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Oct 10 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Fri Sep 26 2025 Yuri N. Sedunov <aris@altlinux.org> 1.32.4-alt1
- 1.32.4

* Mon Sep 01 2025 Yuri N. Sedunov <aris@altlinux.org> 1.32.1-alt1
- 1.32.1

* Fri Aug 29 2025 Yuri N. Sedunov <aris@altlinux.org> 1.32.0-alt1
- 1.32.0

* Thu Aug 21 2025 Yuri N. Sedunov <aris@altlinux.org> 1.31.4-alt1
- 1.31.4

* Tue Aug 19 2025 Yuri N. Sedunov <aris@altlinux.org> 1.31.3-alt1
- 1.31.3

* Fri Aug 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.31.1-alt1
- 1.31.1

* Thu Aug 14 2025 Yuri N. Sedunov <aris@altlinux.org> 1.31.0-alt1
- 1.31.0

* Thu Jul 03 2025 Yuri N. Sedunov <aris@altlinux.org> 1.30.9-alt1
- 1.30.9

* Wed Jun 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.30.3-alt1
- 1.30.3

* Tue Jun 17 2025 Yuri N. Sedunov <aris@altlinux.org> 1.30.2-alt1
- 1.30.2

* Sun Jun 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.29.2-alt1
- 1.29.2

* Thu Jun 12 2025 Yuri N. Sedunov <aris@altlinux.org> 1.29.1-alt1
- 1.29.1

* Mon Jun 02 2025 Yuri N. Sedunov <aris@altlinux.org> 1.28.0-alt1
- 1.28.0

* Fri May 30 2025 Yuri N. Sedunov <aris@altlinux.org> 1.27.1-alt1
- 1.27.1

* Thu May 29 2025 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1
- 1.26.0

* Fri May 23 2025 Yuri N. Sedunov <aris@altlinux.org> 1.25.2-alt1
- 1.25.2

* Wed May 14 2025 Yuri N. Sedunov <aris@altlinux.org> 1.24.2-alt1
- 1.24.2

* Tue Apr 29 2025 Yuri N. Sedunov <aris@altlinux.org> 1.24.1-alt1
- 1.24.1

* Fri Apr 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1
- 1.24.0

* Fri Apr 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.23.0-alt1
- 1.23.0

* Sat Apr 12 2025 Yuri N. Sedunov <aris@altlinux.org> 1.22.4-alt1
- 1.22.4

* Thu Apr 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Tue Apr 01 2025 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt1
- 1.20.2

* Sat Mar 29 2025 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Thu Mar 27 2025 Yuri N. Sedunov <aris@altlinux.org> 1.19.1-alt1
- 1.19.1

* Wed Mar 19 2025 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Tue Mar 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Fri Mar 07 2025 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Wed Feb 26 2025 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Thu Feb 20 2025 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0

* Tue Feb 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Feb 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt1
- 1.13.2

* Sat Feb 08 2025 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Sun Jan 19 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Thu Jan 16 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Thu Jan 09 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sat Jan 04 2025 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Wed Jan 01 2025 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sun Dec 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Fri Dec 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Dec 10 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Sun Dec 01 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Fri Nov 29 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sun Nov 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Nov 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- first build for Sisyphus

