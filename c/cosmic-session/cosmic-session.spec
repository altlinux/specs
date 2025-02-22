%def_disable snapshot
%define ver_major 1.0
%define beta .alpha.6
%define rdn_name com.system76.CosmicSession

%def_disable bootstrap
%def_enable check

Name: cosmic-session
Version: %ver_major.0
Release: alt0.60%beta

Summary: COSMIC Session Manager
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-session

Vcs: https://github.com/pop-os/cosmic-session.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

ExcludeArch: %ix86 armh ppc64le

Requires: cosmic-app-library
Requires: cosmic-applets
Requires: cosmic-bg
Requires: cosmic-comp
Requires: cosmic-greeter
Requires: cosmic-icons
Requires: cosmic-idle
Requires: cosmic-launcher
Requires: cosmic-notifications
Requires: cosmic-osd
Requires: cosmic-panel
Requires: cosmic-randr
Requires: cosmic-screenshot
Requires: cosmic-settings
Requires: cosmic-settings-daemon
Requires: cosmic-workspaces
#Requires: pop-fonts
Requires: switcheroo-control
Requires: xdg-desktop-portal-cosmic
#Requires: cosmic-edit
Requires: cosmic-files
#Requires: cosmic-store
Requires: cosmic-term
Requires: cosmic-player
Requires: cosmic-wallpapers
Requires: orca

BuildRequires(pre): rpm-build-rust
BuildRequires: just

%description
Session manager for the COSMIC desktop environment.

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

# fix path
sed -i 's|\/usr\(\/bin\/dbus-run-session\)|\1|' data/start-cosmic

%build
%rust_build

%install
just rootdir=%buildroot install
install -pD -m644 data/dconf/profile/cosmic %buildroot%_datadir/dconf/profile/cosmic

%check
%rust_test

%files
%_bindir/%name
%_bindir/start-cosmic
%_userunitdir/%name.target
%_desktopdir/cosmic-mimeapps.list
%_datadir/dconf/profile/cosmic
%_datadir/wayland-sessions/cosmic.desktop

%changelog
* Sat Feb 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.60.alpha.6
- 1.0.0-alpha.6

* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.51.alpha.5.1
- 1.0.0-alpha.5.1

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- updated to 1.0.0-alpha.5.1-g38e3686

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- updated to epoch-1.0.0-alpha.4-1-g78316ba

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus


