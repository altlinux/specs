%def_disable snapshot
%define ver_major 1.0
%define beta .alpha.5.1
%define rdn_name com.system76.CosmicPlayer

%def_disable bootstrap
%def_enable check

Name: cosmic-player
Version: %ver_major.0
Release: alt0.51%beta

Summary: COSMIC Media Player
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-player

Vcs: https://github.com/pop-os/cosmic-player.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

ExcludeArch: %ix86 armh ppc64le

%define gst_api_ver 1.0

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav

BuildRequires(pre): rpm-build-rust
BuildRequires: just clang-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gstreamer-video-%gst_api_ver)

%description
Media player for the COSMIC desktop environment.

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
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml

%changelog
* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.51.alpha.5.1
- 1.0.0-alpha.5.1

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- first build for Sisyphus (52b9439)


