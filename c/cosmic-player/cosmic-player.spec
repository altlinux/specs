%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.5
%define rdn_name com.system76.CosmicPlayer

%def_disable bootstrap
%def_enable check

Name: cosmic-player
Version: %ver_major.0
Release: alt0.5%beta

Summary: COSMIC Media Player
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-player

Vcs: https://github.com/pop-os/cosmic-player.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
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
#BuildRequires: pkgconfig(libavcodec)
#BuildRequires: pkgconfig(libavdevice)
#BuildRequires: pkgconfig(libavfilter)
#BuildRequires: pkgconfig(libavformat)
#BuildRequires: pkgconfig(libswscale)
#BuildRequires: pkgconfig(libswresample)

%description
Media player for the COSMIC desktop environment.

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
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml

%changelog
* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- first build for Sisyphus (52b9439)


