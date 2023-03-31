%define glslang_commit 6d41bb9c557c5a0eec61ffba1f775dc5f717a8f7
%define spirv_cross_commit 4e2fdb25671c742a9fbe93a6034eb1542244c7e

Name: snes9x
Version: 1.62.3
Release: alt1

Summary: Super Nintendo Entertainment System emulator
License: Distributable
Group: Emulators

Url: http://www.snes9x.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: ppc64le

# https://github.com/%{name}git/%name/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/KhronosGroup/glslang/archive/%glslang_commit/glslang-%glslang_commit.tar.gz
Source1: glslang-%glslang_commit.tar
# https://github.com/KhronosGroup/SPIRV-Cross/archive/%spirv_cross_commit/SPIRV-Cross-%spirv_cross_commit.tar.gz
Source2: SPIRV-Cross-%spirv_cross_commit.tar

BuildRequires(pre): at-spi2-atk-devel
BuildRequires(pre): bzlib-devel
BuildRequires(pre): expat-devel
BuildRequires(pre): libXcomposite-devel
BuildRequires(pre): libXcursor-devel
BuildRequires(pre): libXdamage-devel
BuildRequires(pre): libXdmcp-devel
BuildRequires(pre): libXi-devel
BuildRequires(pre): libXtst-devel
BuildRequires(pre): libblkid-devel
BuildRequires(pre): libbrotli-devel
BuildRequires(pre): libdatrie-devel
BuildRequires(pre): libffi-devel
BuildRequires(pre): libfribidi-devel
BuildRequires(pre): libjpeg-devel
BuildRequires(pre): libmount-devel
BuildRequires(pre): libpcre2-devel
BuildRequires(pre): libpixman-devel
BuildRequires(pre): libselinux-devel
BuildRequires(pre): libthai-devel
BuildRequires(pre): libtiff-devel
BuildRequires(pre): libxkbcommon-devel
BuildRequires(pre): libwayland-cursor-devel

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libSDL2-devel
BuildRequires: libSM-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXv-devel
BuildRequires: libepoxy-devel
BuildRequires: libgtkmm3-devel
BuildRequires: libminizip-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libvulkan-devel
BuildRequires: libwayland-egl-devel

%description
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES) emulator.
It basically allows you to play most games designed for the SNES and Super Famicom
Nintendo game systems on your Mac, Linux, Windows and so on. The games include some
real gems that were only ever released in Japan.

%package cli
Summary: Super Nintendo Entertainment System emulator - CLI version
Group: Emulators

%description cli
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES) emulator.
It basically allows you to play most games designed for the SNES and Super Famicom
Nintendo game systems on your Mac, Linux, Windows and so on. The games include some
real gems that were only ever released in Japan.

%package gtk
Summary: Super Nintendo Entertainment System emulator - GTK version
Group: Emulators

%description gtk
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES) emulator.
It basically allows you to play most games designed for the SNES and Super Famicom
Nintendo game systems on your Mac, Linux, Windows and so on. The games include some
real gems that were only ever released in Japan.

This package contains a graphical user interface using GTK+.

%prep
%setup -b 1 -b 2

%__mv -Tf ../glslang-%glslang_commit external/glslang
%__mv -Tf ../SPIRV-Cross-%spirv_cross_commit external/SPIRV-Cross

%build
# Build CLI version
pushd unix
%configure \
	--enable-netplay
%make_build
popd

#build GTK version
pushd gtk
%cmake -DCMAKE_INSTALL_LOCALEDIR:PATH=share/locale
%cmake_build
popd

%install
# Install CLI version
%__install -Dp -m 0755 unix/%name %buildroot%_bindir/%name

# Install GTK version
pushd gtk
%cmake_install
%find_lang %name-gtk
popd

%files cli
%doc docs/*.txt unix/docs/readme_unix.html
%_bindir/%name

%files gtk -f gtk/%name-gtk.lang
%doc docs/*.txt gtk/AUTHORS
%_bindir/%name-gtk
%_datadir/%name
%_desktopdir/%name-gtk.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Fri Mar 31 2023 Nazarov Denis <nenderus@altlinux.org> 1.62.3-alt1
- Version 1.62.3

* Tue Mar 28 2023 Nazarov Denis <nenderus@altlinux.org> 1.62.2-alt1
- Version 1.62.2

* Sun Mar 06 2022 Nazarov Denis <nenderus@altlinux.org> 1.61-alt1
- Version 1.61

* Sun Sep 26 2021 Nazarov Denis <nenderus@altlinux.org> 1.60-alt3
- Add patch to fix compilation error in gcc11

* Fri May 03 2019 Nazarov Denis <nenderus@altlinux.org> 1.60-alt2
- Fix post-install unowned files

* Wed May 01 2019 Nazarov Denis <nenderus@altlinux.org> 1.60-alt1
- Version 1.60

* Tue Apr 30 2019 Nazarov Denis <nenderus@altlinux.org> 1.55-alt2
- Remove %ubt macro

* Tue Jan 09 2018 Nazarov Denis <nenderus@altlinux.org> 1.55-alt1%ubt
- Version 1.55

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 1.53-alt0.M70P.1
- Build for branch p7

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 1.53-alt0.M70T.1
- Build for branch t7

* Sun Oct 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.53-alt1
- Initial build for ALT Linux
