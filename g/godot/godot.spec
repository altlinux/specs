%def_with builtin_bullet # need version >=2.88 to build against system library
%def_without builtin_enet
%def_without builtin_freetype
%def_without builtin_libogg
%def_without builtin_libpng
%def_without builtin_libtheora
%def_without builtin_libvorbis
%def_without builtin_libvpx
%def_without builtin_libwebp
%def_without builtin_mbedtls
%def_with builtin_opus # cannot find
%def_without builtin_pcre2
%def_with builtin_recast
%def_with builtin_squish
%def_with builtin_thekla_atlas
%def_without builtin_zlib
%def_with builtin_zstd # need version >=1.3.0 to build against system library

Name: godot
Version: 3.0.2
Release: alt2%ubt

Summary: Godot Engine - Multi-platform 2D and 3D game engine
License: %mit
Group: Development/Tools
Url: https://godotengine.org/

Source: godot-%version.tar

ExclusiveArch: x86_64 %ix86

Requires: libenet libpcre2

# optimized out: libX11-devel libXext-devel libXfixes-devel libXrender-devel libcom_err-devel libgpg-error libjson-c libkrb5-devel libstdc++-devel pkg-config python-base python-devel python-module-numpy python-module-setuptools python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-json python3 python3-base xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-ubt
BuildRequires: libXcursor-devel libXi-devel libXinerama-devel libXrandr-devel
BuildRequires: python-module-Reportlab python-module-configobj python-module-enum34 python-module-olefile python-module-pygobject3 python-module-pyxdg python3-module-yieldfrom python-modules-json
BuildRequires: scons pkgconfig libX11-devel libXcursor-devel libXrandr-devel libXinerama-devel libXi-devel libGL-devel libalsa-devel libpulseaudio-devel openssl-devel libudev-devel libGLU-devel libpng-devel gcc gcc-c++ libssl-devel ccache

%{!?_with_builtin_bullet:BuildRequires: libbullet-devel}
%{!?_with_builtin_enet:BuildRequires: libenet-devel}
%{!?_with_builtin_freetype:BuildRequires: libfreetype-devel}
%{!?_with_builtin_libogg:BuildRequires: libogg-devel}
%{!?_with_builtin_libpng:BuildRequires: libpng-devel}
%{!?_with_builtin_libtheora:BuildRequires: libtheora-devel}
%{!?_with_builtin_libvorbis:BuildRequires: libvorbis-devel}
%{!?_with_builtin_libvpx:BuildRequires: libvpx-devel}
%{!?_with_builtin_libwebp:BuildRequires: libwebp-devel}
%{!?_with_builtin_mbedtls:BuildRequires: libmbedtls-devel}
%{!?_with_builtin_opus:BuildRequires: libopus-devel}
%{!?_with_builtin_pcre2:BuildRequires: libpcre2-devel}
%{!?_with_builtin_recast:BuildRequires: librecast-devel}
%{!?_with_builtin_squish:BuildRequires: libsquish-devel}
%{!?_with_builtin_thekla_atlas:BuildRequires: libtheklaatlas-devel}
%{!?_with_builtin_zlib:BuildRequires: zlib-devel}
%{!?_with_builtin_zstd:BuildRequires: libzstd-devel}

Patch1: fix-zstd-linking.patch

%description
Godot Engine is a feature-packed, cross-platform game engine to create 2D and 3D
games from a unified interface. It provides a comprehensive set of common tools,
so that users can focus on making games without having to reinvent the wheel.
Games can be exported in one click to a number of platforms, including the major
desktop platforms (Linux, Mac OSX, Windows) as well as mobile (Android, iOS) and
web-based (HTML5) platforms.

%prep
%define buildsubdir godot-%version
%setup -q -n %buildsubdir
%{!?_with_builtin_zstd:%patch1 -p2}

%build
build() {
scons \
  builtin_bullet=%{!?_with_builtin_bullet:no}%{?_with_builtin_bullet:yes} \
  builtin_enet=%{!?_with_builtin_enet:no}%{?_with_builtin_enet:yes} \
  builtin_freetype=%{!?_with_builtin_freetype:no}%{?_with_builtin_freetype:yes} \
  builtin_libogg=%{!?_with_builtin_libogg:no}%{?_with_builtin_libogg:yes} \
  builtin_libpng=%{!?_with_builtin_libpng:no}%{?_with_builtin_libpng:yes} \
  builtin_libtheora=%{!?_with_builtin_libtheora:no}%{?_with_builtin_libtheora:yes} \
  builtin_libvorbis=%{!?_with_builtin_libvorbis:no}%{?_with_builtin_libvorbis:yes} \
  builtin_libvpx=%{!?_with_builtin_libvpx:no}%{?_with_builtin_libvpx:yes} \
  builtin_libwebp=%{!?_with_builtin_libwebp:no}%{?_with_builtin_libwebp:yes} \
  builtin_mbedtls=%{!?_with_builtin_mbedtls:no}%{?_with_builtin_mbedtls:yes} \
  builtin_opus=%{!?_with_builtin_opus:no}%{?_with_builtin_opus:yes} \
  builtin_pcre2=%{!?_with_builtin_pcre2:no}%{?_with_builtin_pcre2:yes} \
  builtin_recast=%{!?_with_builtin_recast:no}%{?_with_builtin_recast:yes} \
  builtin_squish=%{!?_with_builtin_squish:no}%{?_with_builtin_squish:yes} \
  builtin_thekla_atlas=%{!?_with_builtin_thekla_atlas:no}%{?_with_builtin_thekla_atlas:yes} \
  builtin_zlib=%{!?_with_builtin_zlib:no}%{?_with_builtin_zlib:yes} \
  builtin_zstd=%{!?_with_builtin_zstd:no}%{?_with_builtin_zstd:yes} \
  $@
}
GCC_USE_CCACHE=1 build platform=x11 tools=yes target=release_debug

%install
%ifarch x86_64
install -Dm 0755 bin/godot.x11.opt.tools.64 %buildroot%_bindir/godot
%endif
%ifarch %ix86
install -Dm 0755 bin/godot.x11.opt.tools.32 %buildroot%_bindir/godot
%endif

%files
%_bindir/*

%changelog
* Sun Jun 10 2018 Sergey Bubnov <omg@altlinux.org> 3.0.2-alt2%ubt
- restrict arch as x86 and x86_64

* Sat Jun 9 2018 Sergey Bubnov <omg@altlinux.org> 3.0.2-alt1%ubt
- 3.0.2-stable

* Sat Jun 9 2018 Sergey Bubnov <omg@altlinux.org> 3.0-alt2%ubt
- added %%ubt

* Sat Jun 9 2018 Sergey Bubnov <omg@altlinux.org> 3.0-alt2
- remove x86_64 arch restriction

* Mon Feb 21 2018 Sergey Bubnov <omg@altlinux.org> 3.0-alt1
- 3.0-stable
