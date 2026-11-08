%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: pragtical
Version: 3.14.0
Release: alt1
Summary: The practical and pragmatic code editor
License: MIT
Group: Development/Tools
Url: https://pragtical.dev/
Vcs: https://github.com/pragtical/pragtical
Source: %name-%version.tar
Source1: %{name}_widget.tar
Source2: %{name}_lua-linenoise.tar
Patch0: %name-%version-alt.patch
# Automatically added by buildreq on Fri Nov 06 2026
# optimized out: fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libGLX-mesa libSDL3-devel libX11-devel libXau-devel libXext-devel libXrender-devel libcairo-devel libcrypt-devel libfreetype-devel libglvnd-devel libgpg-error libgraphite2-devel libicu-devel libp11-kit libpng-devel libstdc++-devel libxcb-devel llvm21.1-libs ninja-build openssl-config p11-kit-trust perl pkg-config python3 python3-base sh5 xz zlib-devel
BuildRequires: gcc-c++ libSDL3_image-devel libSDL3_mixer-devel libharfbuzz-devel liblinenoise-devel libluajit-devel libpcre2-devel libuchardet-devel meson

%description
Pragtical is a cross-platform code editor with a modern graphical interface,
developed using C and Lua(JIT), powered by SDL for rendering and input
management. It serves as a lightweight alternative to web-based editors like
VSCode and can be easily extended or themed with Lua plugins.

%prep
%setup
tar xf %SOURCE1 -C data
tar xf %SOURCE2 -C subprojects
%patch0 -p1

%build
%meson \
  -Duse_system_lua=true \
  -Dextra_colors=false \
  -Dextra_languages=false \
  -Dppm=false \
  -Ddirmonitor_backends=inotify \
  -Dnet=false \

%meson_build

%install
%meson_install
rm -f %buildroot%_datadir/doc/%name/licenses.md

%files
%doc LICENSE* README* changelog* licenses
%_bindir/%name
%_datadir/%name/
%_datadir/metainfo/*.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Fri Nov 06 2026 Ildar Mulyukov <ildar@altlinux.ru> 3.14.0-alt1
- Initial build for Sisyphus
