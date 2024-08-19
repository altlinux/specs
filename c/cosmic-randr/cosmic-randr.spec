%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1

%def_disable bootstrap
%def_enable check

Name: cosmic-randr
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC RandR
License: MPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-randr

Vcs: https://github.com/pop-os/cosmic-randr.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: just

#ExcludeArch: %ix86 armh

%description
COSMIC RandR is both a library and command line utility for displaying
and configuring Wayland outputs. Each display is represented as an
"output head", whereas all supported configurations for each display is
represented as "output modes".

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
%doc README*

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus


