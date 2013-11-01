Name: SDL2_ttf
Version: 2.0.12
Release: alt1

Summary: Simple DirectMedia Layer - Sample TrueType Font Library
License: zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_ttf/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://www.libsdl.org/projects/SDL_ttf/release/%name-%version.tar.gz

BuildRequires: chrpath
BuildRequires: libICE-devel
BuildRequires: libSDL2-devel >= 2.0.1
BuildRequires: libfreetype-devel

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
Requires: lib%name = %version-%release
Requires: libSDL2-devel >= 2.0.1

%description -n lib%name-devel
This library allows you to use TrueType fonts to render text in SDL
applications.

%prep
%setup

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%_libdir/lib%name.la
chrpath -d %buildroot%_libdir/lib%name-2.0.so.0.10.2

%files -n lib%name
%doc CHANGES.txt COPYING.txt README.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/SDL_ttf.h
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%changelog
* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.12-alt1
- Initial build for ALT Linux
