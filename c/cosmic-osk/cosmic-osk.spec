%def_disable snapshot
%define ver_major 1.10
%define beta %nil
%define rdn_name com.system76.CosmicOsk

%def_disable bootstrap
%def_enable check

Name: cosmic-osk
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC On-Screen Keyboard
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-osk

Vcs: https://github.com/pop-os/cosmic-osk.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(udev)

#ExcludeArch: %ix86 armh

%description
%summary

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%rust_build \
%ifarch %ix86 aarch64
    --config 'profile.release.lto=false'
%endif

%install
just rootdir=%buildroot install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Wed Oct 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Sat Sep 26 2026 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- first build for Sisyphus


