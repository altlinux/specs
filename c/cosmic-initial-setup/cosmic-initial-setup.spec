%def_disable snapshot
%define ver_major 1.1
%define beta %nil
%define rdn_name com.system76.CosmicInitialSetup

%def_disable bootstrap
%def_enable check

Name: cosmic-initial-setup
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC Initial Setup
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-initial-setup

Vcs: https://github.com/pop-os/cosmic-initial-setup.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

ExcludeArch: %ix86 armh ppc64le

Requires: cosmic-session

BuildRequires(pre): rpm-build-rust rpm-build-xdg
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libssl)

%description
Initial setup for the COSMIC desktop environment.

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
just rootdir=%buildroot install

%check
%rust_test

%files
%_bindir/%name
%_xdgconfigdir/autostart/%rdn_name.desktop
%_desktopdir/%rdn_name.desktop
%_datadir/polkit-1/rules.d/20-%name.rules
%_datadir/cosmic-layouts/bottom-panel/com.system76.CosmicPanel/v1/
%_datadir/cosmic-layouts/bottom-panel/com.system76.CosmicPanel.Panel/v1/
%_datadir/cosmic-layouts/bottom-panel/icon.png
%_datadir/cosmic-layouts/bottom-panel/layout.kdl
%_datadir/cosmic-layouts/top-panel-and-bottom-dock/com.system76.CosmicPanel.Dock/v1/
%_datadir/cosmic-layouts/top-panel-and-bottom-dock/com.system76.CosmicPanel.Panel/v1/
%_datadir/cosmic-layouts/top-panel-and-bottom-dock/com.system76.CosmicPanel/v1/
%_datadir/cosmic-layouts/top-panel-and-bottom-dock/icon.png
%_datadir/cosmic-layouts/top-panel-and-bottom-dock/layout.kdl
%_datadir/cosmic-themes/*
%_iconsdir/hicolor/scalable/apps/%rdn_name.svg

%changelog
* Wed Jun 24 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Jun 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.16-alt1
- 1.0.16

* Thu Jun 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt1
- 1.0.15

* Wed May 27 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.14-alt1
- 1.0.14

* Wed May 13 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.13-alt1
- 1.0.13

* Thu May 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.12-alt1
- 1.0.12

* Tue May 05 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.11-alt1
- first build for Sisyphus


