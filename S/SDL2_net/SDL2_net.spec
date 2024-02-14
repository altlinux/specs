Name: SDL2_net
Version: 2.2.0
Release: alt1

Summary: Simple DirectMedia Layer - Portable network library
License: Zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_net/
Packager: Nazarov Denis <nenderus@altlinux.org>

# http://www.libsdl.org/projects/SDL_net/release/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: chrpath
BuildRequires: libSDL2-devel-static
BuildRequires: perl-parent

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
Requires: libSDL2-devel >= 2.0.1

%description -n lib%name-devel
This is a portable network library for use with SDL.

This is the libraries and include files you can use to develop SDL networked applications.

%prep
%setup

%build
./autogen.sh
%configure \
	--disable-gui \
	--disable-static
%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%_libdir/lib%name.la
chrpath -d %buildroot%_libdir/lib%name-2.0.so.*

%files -n lib%name
%doc CHANGES.txt README.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/SDL_net.h
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so
%_libdir/cmake/%name

%changelog
* Wed Feb 14 2024 Nazarov Denis <nenderus@altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Fri Jan 22 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Wed Feb 05 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt0.M70T.1
- Build for branch t7

* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Initial build for ALT Linux

