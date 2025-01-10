%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.5

%def_disable bootstrap
%def_enable check

Name: cosmic-idle
Version: %ver_major.0
Release: alt0.5%beta

Summary: COSMIC Screensaver
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-idle

Vcs: https://github.com/pop-os/cosmic-idle.git

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
#%doc README*

%changelog
* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- 1.0.0-alpha.5

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- 1.0.0-alpha.4

* Sat Nov 02 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.3.alpha.3
- first build for Sisyphus


