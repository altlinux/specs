%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define _name phosh-first-boot
%define ver_major 0.1
%define rdn_name mobi.phosh.FirstBoot
%define gettext_domain PhoshFirstBoot
%define greetd_user _greeter

%def_disable bootstrap
%def_enable check

Name: %_name
Version: %ver_major.0
Release: alt0.1

Summary: Phosh First Boot
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/PhoshMobi/phosh-first-boot

Vcs: https://github.com/PhoshMobi/phosh-first-boot.git

%if_disabled snapshot
Source: https://github.com/PhoshMobi/phosh-first-boot/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

%define adwaita_ver 1.9

Requires: dconf polkit phrog

BuildRequires(pre): rpm-macros-meson rpm-build-rust
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(pms-1.0)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(polkit-agent-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
An app to run at first boot to create the initial user.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' >> .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
export GETTEXT_SYSTEM=1
%meson \
    -Dsetup-user=%greetd_user \
    -Doutput-dir-group=%greetd_user
%nil
%meson_build
%rust_build

%install
export GETTEXT_SYSTEM=1
install -pD -m755 target/release/%{_name}{,-importer} \
    -t %buildroot%_libexecdir/
%meson_install
%find_lang %gettext_domain

%check
export GETTEXT_SYSTEM=1
%rust_test
%__meson_test

%files -f %gettext_domain.lang
%_libexecdir/%_name
%_libexecdir/%{_name}-importer
%_desktopdir/%rdn_name.desktop
%_userunitdir/%{_name}-importer.service
%_tmpfilesdir/%_name.conf
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/glib-2.0/schemas/00_%rdn_name.gschema.override
%_datadir/polkit-1/rules.d/20-%_name.rules
%_iconsdir/hicolor/*/*/*.svg
#%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS

%changelog
* Tue Jul 07 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt0.1
- first build for Sisyphus


