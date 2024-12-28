%def_disable snapshot

# required for "ring"
%define optflags_lto %nil

%define _name Fotema
%define ver_major 1.18
%define rdn_name app.fotema.%_name

%def_enable check
%def_disable bootstrap

Name: fotema
Version: %ver_major.3
Release: alt1

Summary: A photo gallery for GNOME
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/blissd/fotema

Vcs: https://github.com/blissd/fotema.git

ExclusiveArch: x86_64 aarch64

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

# for ort
%define onnx_ver 1.16.0
Source4: https://github.com/microsoft/onnxruntime/releases/download/v%onnx_ver/onnxruntime-linux-x64-%onnx_ver.tgz
Source5: https://github.com/microsoft/onnxruntime/releases/download/v%onnx_ver/onnxruntime-linux-aarch64-%onnx_ver.tgz

%define gtk_ver 4.0
%define adwaita_ver 1.5

# for glycin
Requires: bubblewrap glycin-loaders

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(shumate-1.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

BuildRequires: pkgconfig(openssl)
BuildRequires: libopencv-devel gcc-c++
# for glycin
BuildRequires: pkgconfig(libseccomp)
# for ffmpeg-next
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libavformat) >= 61
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libswresample)
# for bindgen
BuildRequires: clang-devel
# ? for gdk-sys
BuildRequires: pkgconfig(gdk-3.0)
# for ort
BuildRequires: /proc

%description
A photo gallery for everyone who wants their photos to live locally on their devices.
Why enjoy your photo library with Fotema?
- Many supported image formats. Fotema supports the same image formats as Loupe (the GNOME image viewer).
- View iOS Live Photos.
- Play videos.
- View your library by year or month.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

mkdir onnxruntime
%ifarch x86_64
tar zxf %SOURCE4 --strip-components=1 -C onnxruntime
%else %ifarch aarch64
tar zxf %SOURCE5 --strip-components=1 -C onnxruntime
%endif

%build
export ORT_STRATEGY=SYSTEM ORT_LIB_LOCATION=${PWD}/onnxruntime
%meson
%__meson_build

%install
export ORT_STRATEGY=SYSTEM ORT_LIB_LOCATION=${PWD}/onnxruntime
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sat Dec 28 2024 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Tue Dec 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- first build for Sisyphus (v1.18.2-21-g38ac8e9)



