Name: libretro-mame
Version: 0.263
Release: alt1

Summary: MAME libretro core (Arcade only)
License: GPL2
Group: Emulators

Url: https://github.com/libretro/mame
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libexpat-devel rapidjson libsqlite3-devel libutf8proc-devel zlib-devel libjpeg-devel liblinenoise-devel glibc-devel
BuildRequires: libflac-devel libglm-devel libportaudio2-devel libportmidi-devel fontconfig-devel eglexternalplatform-devel egl-wayland-devel libwayland-egl-devel wayland-devel
BuildRequires: git-core libxcb libSDL2_ttf-devel libXi-devel libXinerama-devel libalsa-devel python-modules-compiler
BuildRequires: python-modules-encodings python-modules-logging python-modules-xml qt5-base-devel libpulseaudio-devel
BuildRequires: libuv-devel asio-devel gettext-tools libstdc++-devel-static

Requires: retroarch
ExcludeArch: ppc64le

%description
%summary

This is arcade-only build.

This package is for RetroArch/Libretro front-end.

%prep
%setup -n %name-%version

%build
%ifarch %ix86
%make_build OSD="retro" verbose=1 RETRO=1 NOWERROR=1 OS="linux" TARGETOS="linux" CONFIG="libretro" NO_USE_MIDI="1" TARGET=mame SUBTARGET=arcade
%else
%make_build OSD="retro" verbose=1 RETRO=1 NOWERROR=1 OS="linux" TARGETOS="linux" CONFIG="libretro" NO_USE_MIDI="1" PTR64=1 TARGET=mame SUBTARGET=arcade
%endif

%install
mkdir -p %buildroot%_libexecdir/libretro
install -Dp -m0644 ./mamearcade_libretro.so %buildroot%_libexecdir/libretro

%files
%doc README.md COPYING
%_libexecdir/libretro/mamearcade_libretro.so

%changelog
* Wed Mar 27 2024 Artyom Bystrov <arbars@altlinux.org> 0.263-alt1
- Initial commit for Sisyphus