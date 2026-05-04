%def_disable snapshot

%define __name CosmicTweaks
%define _name tweaks
%define binary_name cosmic-ext-%_name
%define rdn_name dev.edfloreshz.%__name
%define ver_major 0.2
%define beta %nil

%def_disable bootstrap
%def_enable check

Name: cosmic-%_name
Version: %ver_major.2
Release: alt1%beta

Summary: COSMIC Tweaks
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/cosmic-utils/tweaks

Vcs: https://github.com/cosmic-utils/tweaks.git

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif
Source1: %_name-%version%beta-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(openssl)

#ExcludeArch: %ix86 armh

%description
A tweaking tool offering access to advanced settings and features for
COSMIC desktop.

%prep
%setup -n %_name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
just rootdir=%buildroot install

%check
%rust_test

%files
%_bindir/%binary_name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/*/*.*
#%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Mon May 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Thu Dec 25 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus


