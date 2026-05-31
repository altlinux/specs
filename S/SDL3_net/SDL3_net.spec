Name: SDL3_net
Version: 3.2.0
Release: alt1

Summary: Simple DirectMedia Layer - Portable network library
License: Zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_net/
Vcs: https://github.com/libsdl-org/SDL_net
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/libsdl-org/SDL_net/archive/release-%version/SDL_net-release-%version.tar.gz
Source: SDL_net-release-%version.tar

BuildRequires: cmake
BuildRequires: libSDL3-devel

%description
This is a portable network library for use with SDL.

%package -n lib%name
Summary: Simple DirectMedia Layer - Portable network library
Group: System/Libraries

%description -n lib%name
This is a portable network library for use with SDL.

%package -n lib%name-devel
Summary: Libraries and includes to develop SDL networked applications.
Group: Development/C

%description -n lib%name-devel
This is a portable network library for use with SDL.

This is the libraries and include files you can use to develop SDL networked applications.

%prep
%setup -n SDL_net-release-%version

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo
%cmake_build

%install
%cmake_install
%__rm -rf %buildroot%_datadir/licenses

%files -n lib%name
%doc AGENTS.md CLAUDE.md INSTALL.md LICENSE.txt README.md
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/SDL_net.h
%_pkgconfigdir/sdl3-net.pc
%_libdir/lib%name.so
%_libdir/cmake/%name

%changelog
* Sun May 31 2026 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt1
- Initial build for ALT Linux
