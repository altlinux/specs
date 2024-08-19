%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicOsd

%def_disable bootstrap
%def_enable check

Name: cosmic-osd
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC OSD
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-osd

Vcs: https://github.com/pop-os/cosmic-osd.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: make
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libpulse)

#ExcludeArch: %ix86 armh

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

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus


