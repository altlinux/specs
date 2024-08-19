%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicSettings

%def_disable bootstrap
%def_enable check

Name: cosmic-settings
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC Settings
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-settings

Vcs: https://github.com/pop-os/cosmic-settings.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
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
%_desktopdir/%rdn_name.desktop
%_desktopdir/%rdn_name.*.desktop
%_datadir/polkit-1/rules.d/%name.rules
%_datadir/cosmic/com.system76.CosmicTheme.Dark.Builder/
%_datadir/cosmic/com.system76.CosmicTheme.Light.Builder/
%_datadir/cosmic/com.system76.CosmicTheme.Dark/
%_datadir/cosmic/com.system76.CosmicTheme.Light/
%_datadir/cosmic/com.system76.CosmicTheme.Mode/
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-27-g83a4296)


