%def_disable snapshot

%define __name minimon
%define _name %__name-applet
%define binary_name cosmic-ext-applet-%__name
%define rdn_name io.github.cosmic_utils.%_name
%define ver_major 1.1
%define beta %nil

%def_disable bootstrap
%def_enable check

Name: cosmic-%_name
Version: %ver_major.2
Release: alt1%beta

Summary: Minimon COSMIC Applet
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/cosmic-utils/minimon-applet

Vcs: https://github.com/cosmic-utils/minimon-applet.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif
Source1: %_name-%version%beta-cargo.tar

Requires: cosmic-monitor

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)

#ExcludeArch: %ix86 armh

%description
A configurable COSMIC applet for displaying the following:
* CPU load
* CPU temperature
* Memory usage
* Network utilization
* Disk activity
* GPU and VRAM usage on Nvidia and AMD GPUs..

%prep
%setup -n %_name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version%beta-cargo.tar .cargo/ vendor/}

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
%_bindir/%binary_name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Wed Jul 01 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2
- requires cosmic-monitor instead of gnome-system-monitor

* Wed Jun 03 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Fri May 08 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Fri Feb 13 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri Dec 12 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus


