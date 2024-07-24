Name:    RMG
Version: 0.5.7
Release: alt2
Summary: Rosalie's Mupen GUI 
Group: Emulators

License: GPL-3.0-only
URL:     https://github.com/Rosalie241/RMG
Source0: %name-%version.tar.gz

ExclusiveArch: x86_64 aarch64

BuildRequires: pkgconfig(SDL_ttf)
BuildRequires: pkgconfig(lirc)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(freetype2)
BuildRequires: boost-devel
BuildRequires: gzip libminizip-devel libspeexdsp-devel
BuildRequires: pkgconfig(glew)
BuildRequires: binutils nasm
BuildRequires: cmake gcc-c++ boost-filesystem-devel
BuildRequires: qt6-base-devel qt6-svg-devel
BuildRequires: libhidapi-devel
BuildRequires: libvulkan-devel

%description
Rosalie's Mupen GUI is a free and open-source mupen64plus front-end written in C++

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DPORTABLE_INSTALL=OFF -DDISCORD_RPC=OFF
%cmake_build

%install
%cmake_install
chmod +x %{buildroot}/usr/lib64/RMG/*.so
chmod +x %{buildroot}/usr/lib64/RMG/*/*.so
chmod +x %{buildroot}/usr/lib64/RMG/*/*/*.so

%files
/usr/bin/RMG
/usr/lib64/libRMG-Core.so
/usr/lib64/RMG/
/usr/share/RMG/
/usr/share/applications/com.github.Rosalie241.RMG.desktop
/usr/share/icons/hicolor/scalable/apps/com.github.Rosalie241.RMG.svg
/usr/share/metainfo/com.github.Rosalie241.RMG.appdata.xml

%changelog
* Wed Jul 24 2024 Artyom Bystrov <arbars@altlinux.org> 0.5.7-alt2
- FIx build (add libvulkan-devel to BR)

* Mon Feb 12 2024 Artyom Bystrov <arbars@altlinux.org> 0.5.7-alt1
- Initial commit