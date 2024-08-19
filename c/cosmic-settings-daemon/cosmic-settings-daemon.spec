%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicSettingsDaemon

%def_disable bootstrap
%def_enable check

Name: cosmic-settings-daemon
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC Settings Daemon
License: GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-settings-daemon

Vcs: https://github.com/pop-os/cosmic-settings-daemon.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

ExcludeArch: %ix86 armh ppc64le

Requires: cosmic-settings

BuildRequires(pre): rpm-build-rust
BuildRequires: make
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libudev)

%description
%summary

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%makeinstall_std prefix=%_prefix

%check
%rust_test

%files
%_bindir/%name
%_datadir/cosmic/com.system76.CosmicSettings.Shortcuts/
%_datadir/polkit-1/rules.d/%name.rules

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-3-g93c5494)


