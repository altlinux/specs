%def_enable snapshot
%define binary_name cosmic-app-library
%define ver_major 1.0
%define beta .alpha.2
%define rdn_name com.system76.CosmicAppLibrary

%def_disable bootstrap
%def_enable check

Name: cosmic-applibrary
Version: %ver_major.0
Release: alt0.2%beta

Summary: COSMIC App Library
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-applibrary

Vcs: https://github.com/pop-os/cosmic-applibrary.git

Provides: %binary_name = %EVR

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

# rustc-LLVM ERROR: out of memory
# Allocation failed
ExcludeArch: %ix86 armh

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)

%description
Cosmic App Library is an application launcher for the COSMIC desktop
that lists all installed applications in a grid.

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
%_bindir/%binary_name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-5-g864564b)


