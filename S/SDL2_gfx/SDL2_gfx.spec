Name: SDL2_gfx
Version: 1.0.0
Release: alt1

Summary: Simple DirectMedia Layer - Graphics primitives and surface functions
License: zlib
Group: System/Libraries

Url: http://www.ferzkopp.net/joomla/software-mainmenu-14/4-ferzkopps-linux-software/19-sdlgfx
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://www.ferzkopp.net/Software/%name/%name-%version.tar.gz

BuildRequires: chrpath
BuildRequires: libSDL2-devel >= 2.0.1

%description
The SDL2_gfx library provides the basic drawing functions such as lines,
circles or polygons provided by SDL_gfx on SDL2 against renderers of SDL2.

%package -n lib%name
Summary: Simple DirectMedia Layer - Graphics primitives and surface functions
Group: System/Libraries

%description -n lib%name
The SDL2_gfx library provides the basic drawing functions such as lines,
circles or polygons provided by SDL_gfx on SDL2 against renderers of SDL2.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C
Requires: lib%name = %version-%release
Requires: libSDL2-devel >= 2.0.1

%description -n lib%name-devel
The SDL2_gfx library provides the basic drawing functions such as lines,
circles or polygons provided by SDL_gfx on SDL2 against renderers of SDL2.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%_libdir/lib%name.la
chrpath -d %buildroot%_libdir/lib%name-1.0.so.0.0.0

%files -n lib%name
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_libdir/lib%name-1.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/*.h
%_libdir/lib%name.so

%changelog
* Sat Nov 02 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux
