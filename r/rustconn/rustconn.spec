%def_disable snapshot

%define __name RustConn
%define _name rustconn
%define ver_major 0.18
%define rdn_name io.github.totoshko88.%__name

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Remote connections manager
License: GPL-3.0-or-later
Group: Networking/Remote access
Url: https://github.com/totoshko88/RustConn

Vcs: https://github.com/totoshko88/RustConn.git

%if_disabled snapshot
Source: https://github.com/totoshko88/RustConn/archive/v%version/%__name-%version.tar.gz
%else
Source: %__name-%version.tar
%endif
Source1: %__name-%version-cargo.tar

ExcludeArch: %ix86

Requires: openssh-clients
Requires: sshpass

# Optional runtime dependencies
#Recommends:     freerdp
#Recommends:     tigervnc
#Recommends:     virt-viewer
#Recommends:     picocom
#Recommends:     kubectl

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo >= 1.88
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(vte-2.91-gtk4)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(liblzma)
%{?_enable_check:BuildRequires: clippy}

%description
RustConn is a connection orchestrator for Linux with a
GTK4/Wayland-native interface.

It brings SSH, RDP, VNC, SPICE, Telnet, Serial, Kubernetes, and Zero
Trust connections under one roof -- with embedded Rust clients where
possible and seamless integration with external tools where needed.

%prep
%setup -n %__name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%__name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build -p %name -p %name-cli

%install
%rust_install %name %name-cli
install -Dm644 rustconn/assets/%rdn_name.desktop \
    %buildroot%_desktopdir/%rdn_name.desktop
install -Dm644 rustconn/assets/%rdn_name.metainfo.xml \
    %buildroot/%_datadir/metainfo/%rdn_name.metainfo.xml
install -Dm644 rustconn/assets/icons/hicolor/scalable/apps/%rdn_name.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/%rdn_name.svg
# screenshots
install -d %buildroot%_datadir/app-info/screenshots/%rdn_name
for screenshot in %_name/assets/screenshots/*.png; do
install -Dm644 $screenshot \
    %buildroot%_datadir/app-info/screenshots/%rdn_name/$(basename $screenshot)
done
# local files
for po_file in po/*.po; do
    lang=$(basename $po_file .po)
    mkdir -p %buildroot%_datadir/locale/$lang/LC_MESSAGES
    msgfmt -o %buildroot%_datadir/locale/$lang/LC_MESSAGES/%_name.mo $po_file
done

%find_lang %_name

%check
%rust_test

%files -f %_name.lang
%_bindir/%name
%_bindir/%name-cli
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%dir %_datadir/app-info/screenshots/%rdn_name
%_datadir/app-info/screenshots/%rdn_name/*.png
%doc *.md docs/*.md

%changelog
* Mon Jul 06 2026 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Mon Jun 22 2026 Yuri N. Sedunov <aris@altlinux.org> 0.16.13-alt1
- 0.16.13

* Tue Jun 16 2026 Yuri N. Sedunov <aris@altlinux.org> 0.16.6-alt1
- 0.16.6

* Tue Jun 09 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.11-alt1
- 0.15.11

* Mon Jun 01 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.4-alt1
- 0.15.4

* Mon May 25 2026 Yuri N. Sedunov <aris@altlinux.org> 0.14.7-alt1
- 0.14.7

* Mon May 18 2026 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Wed May 06 2026 Yuri N. Sedunov <aris@altlinux.org> 0.13.4-alt1
- 0.13.4

* Tue May 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3

* Tue Apr 28 2026 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Fri Apr 24 2026 Yuri N. Sedunov <aris@altlinux.org> 0.11.7-alt1
- 0.11.7

* Mon Apr 13 2026 Yuri N. Sedunov <aris@altlinux.org> 0.10.17-alt1
- 0.10.17

* Fri Apr 03 2026 Yuri N. Sedunov <aris@altlinux.org> 0.10.9-alt1
- 0.10.9

* Tue Mar 24 2026 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5

* Wed Mar 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt1
- 0.9.7

* Mon Mar 02 2026 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5

* Sun Mar 01 2026 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- 0.9.4

* Sat Feb 28 2026 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Wed Feb 25 2026 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Mon Feb 23 2026 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Sat Feb 21 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.9-alt1
- 0.8.9

* Wed Feb 18 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt1
- 0.8.7

* Mon Feb 16 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.6-alt1
- first build for Sisyphus

