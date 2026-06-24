%def_disable snapshot
%define ver_major 1.1
%define beta %nil
%define rdn_name com.system76.CosmicSettings

%def_disable bootstrap
%def_enable check

Name: cosmic-settings
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC Settings
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-settings

Vcs: https://github.com/pop-os/cosmic-settings.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

# error: could not compile `generator` (lib) due to 2 previous errors
ExcludeArch: %ix86 armh ppc64le

Requires: accountsservice
Requires: cosmic-randr
Requires: iso-codes
Requires: xkeyboard-config
Requires: fonts-ttf-open-sans
Requires: bluez
Requires: ppd-service

#? for VPN
Requires: NetworkManager-openvpn-gtk4
Requires: NetworkManager-pptp-gtk4
Requires: NetworkManager-vpnc-gtk4
Requires: NetworkManager-l2tp-gtk4
Requires: NetworkManager-openconnect-gtk4

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libpipewire-0.3) clang-devel
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(wayland-client)

%description
The settings application for the COSMIC desktop environment.

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%rust_build \
%ifarch aarch64
    --config 'profile.release.lto=false'
%endif
%nil

%install
just rootdir=%buildroot install

%check
%rust_test

%files
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_desktopdir/%rdn_name.*.desktop
%_datadir/polkit-1/rules.d/%name.rules
%_datadir/polkit-1/actions/%rdn_name.Users.policy
%_datadir/cosmic/com.system76.CosmicTheme.Dark.Builder/
%_datadir/cosmic/com.system76.CosmicTheme.Light.Builder/
%_datadir/cosmic/com.system76.CosmicTheme.Dark/
%_datadir/cosmic/com.system76.CosmicTheme.Light/
%_datadir/cosmic/com.system76.CosmicTheme.Mode/
%_datadir/cosmic/com.system76.CosmicComp/
%_iconsdir/hicolor/*/*/*.svg
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
- epoch-1.0.1-1-g2566969

* Thu Dec 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Dec 04 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.82.beta.9
- 1.0.0-beta.9

* Thu Nov 13 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.81.beta.6
- 1.0.0-beta.6

* Sun Sep 21 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.80.beta.1
- 1.0.0-beta.1

* Thu Apr 24 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.70.alpha.7
- 1.0.0-alpha.7

* Sat Feb 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.60.alpha.6
- 1.0.0-alpha.6

* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.51.alpha.5.1
- 1.0.0-alpha.5.1

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- 1.0.0-alpha.5

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- 1.0.0-alpha.4

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- updated to epoch-1.0.0-alpha.2-8-gc38e870

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-27-g83a4296)


