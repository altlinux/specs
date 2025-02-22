%def_disable snapshot
%define ver_major 1.0
%define beta .alpha.6
%define rdn_name com.system76.Cosmic

%def_disable bootstrap
%def_enable check

Name: cosmic-comp
Version: %ver_major.0
Release: alt0.60%beta

Summary: COSMIC Wayland Compositor
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-comp

Vcs: https://github.com/pop-os/cosmic-comp.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

ExcludeArch: %ix86 armh ppc64le

BuildRequires(pre): rpm-build-rust
BuildRequires: make
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libdisplay-info)

%description
Wayland compositor for the COSMIC desktop environment.

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
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
%_datadir/cosmic/com.system76.CosmicSettings.Shortcuts/v1/defaults
%_datadir/cosmic/com.system76.CosmicSettings.WindowRules/v1/tiling_exception_defaults

%changelog
* Sat Feb 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.60.alpha.6
- 1.0.0-alpha.6

* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.51.alpha.5.1
- 1.0.0-alpha.5.1

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- 1.0.0-alpha.5

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- updated to epoch-1.0.0-alpha.4-4-g7829e76

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-13-ga3c8111)


