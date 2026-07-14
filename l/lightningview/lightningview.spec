%global _unpackaged_files_terminate_build 1
%def_with check

Name: lightningview
Version: 3.0.0
Release: alt1
Summary: A lightning-fast cross-platform image viewer
License: GPL-2.0
Group: Graphics
URL: https://lightningview.app
VCS: https://github.com/dividebysandwich/LightningView

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-fix-font-path.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: cmake
BuildRequires: clang-devel
BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(xkbcommon)

%if_with check
BuildRequires: desktop-file-utils
%endif

Requires: fonts-ttf-dejavu

%description
A lightning-fast cross-platform image viewer written in Rust.
This is a very slim image viewer that aims to replicate the most
important functions found in commercial software like ACDSee.

%prep
%setup -a1
%patch -p1
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/dividebysandwich/imagepipe?rev=cc9df677"]
git = "https://github.com/dividebysandwich/imagepipe"
rev = "cc9df677"
replace-with = "vendored-sources"

[source."git+https://patched@github.com/dividebysandwich/dnglab.git?rev=06dc3dab"]
git = "https://patched@github.com/dividebysandwich/dnglab.git"
rev = "06dc3dab"
replace-with = "vendored-sources"
EOF

%build
# build only for Wayland
cat > sdl3-toolchain.cmake <<EOF
set(SDL_X11 OFF CACHE BOOL "Disable X11 backend" FORCE)
EOF
export CMAKE_TOOLCHAIN_FILE="$PWD/sdl3-toolchain.cmake"
%rust_build

%install
%rust_install
install -Dm 0644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 0644 %name.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png

%check
%rust_test
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/256x256/apps/%name.png
%doc README.md

%changelog
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.0-alt1
- Updated to version 3.0.0.
- Build only for Wayland support.

* Sat Jun 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.6.2-alt1
- Initial build for ALT.
