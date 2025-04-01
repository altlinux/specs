Name: SDL3_ttf
Version: 3.2.2
Release: alt1

Summary: Simple DirectMedia Layer - Sample TrueType Font Library
License: Zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_ttf/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/libsdl-org/SDL_ttf/archive/release-%version/SDL_ttf-release-%version.tar.gz
Source: SDL_ttf-release-%version.tar

BuildRequires: cmake
BuildRequires: libSDL3-devel
BuildRequires: libharfbuzz-devel

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package -n lib%name
Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Group: System/Libraries

%description -n lib%name
This library allows you to use TrueType fonts to render text in SDL
applications.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C

%description -n lib%name-devel
This library allows you to use TrueType fonts to render text in SDL
applications.

%prep
%setup -n SDL_ttf-release-%version

%build
%cmake
%cmake_build

%install
%cmake_install
%__rm -rf %buildroot%_datadir/licenses

%files -n lib%name
%doc CHANGES.txt INSTALL.md LICENSE.txt README.md
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name
%_pkgconfigdir/sdl3-ttf.pc
%_libdir/lib%name.so
%_libdir/cmake/%name

%changelog
* Tue Apr 01 2025 Nazarov Denis <nenderus@altlinux.org> 3.2.2-alt1
- Initial build for ALT Linux
