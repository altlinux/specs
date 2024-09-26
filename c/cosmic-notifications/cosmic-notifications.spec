%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.2
%define rdn_name com.system76.CosmicNotifications

%def_disable bootstrap
%def_enable check

Name: cosmic-notifications
Version: %ver_major.0
Release: alt0.2%beta

Summary: COSMIC Notifications Service
License: MPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-notifications

Vcs: https://github.com/pop-os/cosmic-notifications.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)

#ExcludeArch: %ix86 armh

%description
Layer Shell notifications daemon which integrates with COSMIC.

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
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus


