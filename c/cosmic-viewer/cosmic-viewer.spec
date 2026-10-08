%def_disable snapshot
%define ver_major 1.10
%define beta %nil
%define rdn_name com.system76.CosmicViewer

%def_disable bootstrap
%def_enable check

Name: cosmic-viewer
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC Image Viewer
License: GPL-3.0
Group: Graphics
Url: https://github.com/pop-os/cosmic-viewer

Vcs: https://github.com/pop-os/cosmic-viewer.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

ExcludeArch: %ix86 armh

BuildRequires(pre): rpm-build-rust
BuildRequires: just
# for turbojpeg
BuildRequires: cmake gcc-c++ nasm
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libturbojpeg)
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(zlib)
BuildRequires: /usr/bin/appstreamcli /usr/bin/desktop-file-validate

%description
%summary

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

# Disable feature that enforces vendored libheif use:
sed -i '/"embedded-libheif",/d' Cargo.toml

%build
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
export TURBOJPEG_SOURCE=pkg-config
%rust_build

%install
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
just rootdir=%buildroot install

%check
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_test

%files
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/metainfo/%rdn_name.metainfo.xml
%_iconsdir/hicolor/*/apps/*.svg
%doc README*

%changelog
* Wed Oct 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Sat Sep 26 2026 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- first build for Sisyphus


