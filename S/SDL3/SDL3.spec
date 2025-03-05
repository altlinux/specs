%define _unpackaged_files_terminate_build 1

Name: SDL3
Version: 3.2.8
Release: alt1

Summary: Simple DirectMedia Layer
License: Zlib and MIT
Group: System/Libraries

Url: https://www.libsdl.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/libsdl-org/SDL/archive/release-%version/SDL-release-%version.tar.gz
Source: SDL-release-%version.tar

BuildRequires: cmake
BuildRequires: fcitx5-devel
BuildRequires: gcc-c++
BuildRequires: libXScrnSaver-devel
BuildRequires: libXext-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libalsa-devel
BuildRequires: libaudio-devel
BuildRequires: libdbus-devel
BuildRequires: libdecor-devel
BuildRequires: libdrm-devel
BuildRequires: libe2fs
BuildRequires: libesd-devel
BuildRequires: libgbm-devel
BuildRequires: libglvnd-devel
BuildRequires: libibus-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsamplerate-devel
BuildRequires: libslang2
BuildRequires: libsoup3.0-devel
BuildRequires: libudev-devel
BuildRequires: libunwind-devel
BuildRequires: libusb-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: libxkbcommon-devel
BuildRequires: pipewire-jack-libs-devel

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package -n lib%name
Summary: Simple DirectMedia Layer
Group: System/Libraries

%description -n lib%name
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C
Conflicts: rpm-build < 4.0.4-alt100.96

%description -n lib%name-devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.

%prep
%setup -n SDL-release-%version

%build
%cmake \
	-DSDL_TEST_LIBRARY:BOOL=OFF \
	-DSDL_INSTALL_DOCS:BOOL=ON
%cmake_build

%install
%cmake_install
%__rm -r %buildroot%_datadir/licenses

%files -n lib%name
%doc BUGS.txt CREDITS.md INSTALL.md LICENSE.txt README.md WhatsNew.txt
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_libdir/cmake/%name
%_man3dir/SDL*.3*
%_pkgconfigdir/sdl3.pc

%changelog
* Wed Mar 05 2025 Nazarov Denis <nenderus@altlinux.org> 3.2.8-alt1
- New version 3.2.8.

* Sun Mar 02 2025 Nazarov Denis <nenderus@altlinux.org> 3.2.6-alt1
- New version 3.2.6.

* Fri Feb 07 2025 Nazarov Denis <nenderus@altlinux.org> 3.2.4-alt1
- New version 3.2.4.

* Sun Feb 02 2025 Nazarov Denis <nenderus@altlinux.org> 3.2.2-alt1
- New version 3.2.2.

* Sun Jan 26 2025 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt1
- New version 3.2.0.

* Sat Jan 11 2025 Nazarov Denis <nenderus@altlinux.org> 3.1.8-alt1
- New version 3.1.8.

* Tue Dec 10 2024 Nazarov Denis <nenderus@altlinux.org> 3.1.6-alt1
- Initial build for ALT Linux (ALT #52381)
