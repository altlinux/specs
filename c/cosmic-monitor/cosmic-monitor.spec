%def_disable snapshot
%define ver_major 1.1
%define beta %nil
%define rdn_name com.system76.CosmicMonitor

%def_disable bootstrap
%def_enable check

Name: cosmic-monitor
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC System Monitor
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-monitor

Vcs: https://github.com/pop-os/cosmic-monitor.git

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
#ExcludeArch: %ix86 armh

%description
System Monitor for COSMIC desktop.

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
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
%_iconsdir/hicolor/*x*/apps/%rdn_name.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Wed Jun 24 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus


