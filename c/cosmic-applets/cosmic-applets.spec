%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.5
%define rdn_name com.system76.CosmicApplets

%def_disable bootstrap
%def_enable check

Name: cosmic-applets
Version: %ver_major.0
Release: alt0.5%beta

Summary: COSMIC Panel Applets
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-applets

Vcs: https://github.com/pop-os/cosmic-applets.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(wayland-client)

# rustc-LLVM ERROR: out of memory
# Allocation failed
ExcludeArch: %ix86 armh

%description
Applets for the COSMIC Panel.

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
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
%_bindir/cosmic-app-list
%_bindir/cosmic-applet-a11y
%_bindir/cosmic-applet-audio
%_bindir/cosmic-applet-battery
%_bindir/cosmic-applet-bluetooth
%_bindir/cosmic-applet-input-sources
%_bindir/cosmic-applet-minimize
%_bindir/cosmic-applet-network
%_bindir/cosmic-applet-notifications
%_bindir/cosmic-applet-power
%_bindir/cosmic-applet-status-area
%_bindir/cosmic-applet-tiling
%_bindir/cosmic-applet-time
%_bindir/cosmic-applet-workspaces
%_bindir/cosmic-panel-button
%_desktopdir/*.desktop
%_datadir/cosmic/com.system76.CosmicAppList/
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
#%doc README*

%changelog
* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- 1.0.0-alpha.5

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- 1.0.0-alpha.4

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-18-g323e8a5)


