%def_disable snapshot
%define ver_major 1.1
%define beta %nil
%define rdn_name com.system76.CosmicStore

%def_disable bootstrap
%def_enable check

Name: cosmic-store
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC Store
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-store

Vcs: https://github.com/pop-os/cosmic-store.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

Requires: appstream-data-desktop

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(flatpak)

#ExcludeArch: %ix86 armh

%description
Software center for COSMIC desktop.

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
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*x*/apps/%rdn_name.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

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

* Wed Apr 22 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.11-alt1
- 1.0.11

* Wed Apr 15 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.10-alt1
- 1.0.10

* Wed Apr 08 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9

* Tue Feb 24 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Wed Feb 18 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Wed Feb 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Tue Feb 03 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Wed Jan 28 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Wed Jan 21 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Wed Jan 14 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Wed Dec 31 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sat Dec 13 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus


