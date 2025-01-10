%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.5
%define rdn_name com.system76.CosmicLauncher

%def_disable bootstrap
%def_enable check

Name: cosmic-launcher
Version: %ver_major.0
Release: alt0.5%beta

Summary: COSMIC Launcher
License: MPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-launcher

Vcs: https://github.com/pop-os/cosmic-launcher.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

# no pop-launcher for ppc64le
ExcludeArch: ppc64le armh

Requires: pop-launcher

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)

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
* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- 1.0.0-alpha.5

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- 1.0.0-alpha.4

* Sat Nov 02 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.3.alpha.3
- 1.0.0.alpha.3

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sat Aug 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.1
- required pop-launcher
- fixed build for loongarch64

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus


