%def_disable snapshot

%define __name RustConn
%define _name rustconn
%define ver_major 0.8
%define rdn_name io.github.totoshko88.%__name

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.9
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

%find_lang %name

%check
%rust_test

%files -f %name.lang
%_bindir/%name
%_bindir/%name-cli
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc *.md docs/*.md

%changelog
* Sat Feb 21 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.9-alt1
- 0.8.9

* Wed Feb 18 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt1
- 0.8.7

* Mon Feb 16 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.6-alt1
- first build for Sisyphus

