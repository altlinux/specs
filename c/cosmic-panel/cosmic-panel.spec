%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicPanel

%def_disable bootstrap
%def_enable check

Name: cosmic-panel
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC Panel
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-panel

Vcs: https://github.com/pop-os/cosmic-panel.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)

ExcludeArch: %ix86 armh

%description
Panel for the COSMIC desktop environment.

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
%_datadir/cosmic/%rdn_name/
%_datadir/cosmic/%rdn_name.Panel/
%_datadir/cosmic/%rdn_name.Dock/
%doc README*

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-4-ge184d10)


