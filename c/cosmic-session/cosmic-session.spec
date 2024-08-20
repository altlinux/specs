%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicSession

%def_disable bootstrap
%def_enable check

Name: cosmic-session
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC Session Manager
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-session

Vcs: https://github.com/pop-os/cosmic-session.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
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
#Requires: switcheroo-control
Requires: xdg-desktop-portal-cosmic
#Requires: cosmic-edit
#Requires: cosmic-files
#Requires: cosmic-store
#Requires: cosmic-term
#Requires: cosmic-wallpapers

BuildRequires(pre): rpm-build-rust
BuildRequires: just

%description
Session manager for the COSMIC desktop environment.

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
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

%check
%rust_test

%files
%_bindir/%name
%_bindir/start-cosmic
%_userunitdir/%name.target
%_desktopdir/cosmic-mimeapps.list
%_datadir/wayland-sessions/cosmic.desktop

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus


