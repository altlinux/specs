%def_disable static

Name: SDL2_gfx
Version: 1.0.1
Release: alt2

Summary: Simple DirectMedia Layer - Graphics primitives and surface functions
License: zlib
Group: System/Libraries

Url: http://cms.ferzkopp.net/index.php/software/13-sdl-gfx
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://www.ferzkopp.net/Software/%name/%name-%version.tar.gz

BuildRequires: libSDL2-devel >= 2.0.3

%description
The %name library provides the basic drawing functions such as lines,
circles or polygons provided by SDL_gfx on SDL2 against renderers of SDL2.

%package -n lib%name
Summary: Simple DirectMedia Layer - Graphics primitives and surface functions
Group: System/Libraries

%description -n lib%name
The %name library provides the basic drawing functions such as lines,
circles or polygons provided by SDL_gfx on SDL2 against renderers of SDL2.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C
Requires: lib%name = %version-%release
Requires: libSDL2-devel >= 2.0.3

%description -n lib%name-devel
The %name library provides the basic drawing functions such as lines,
circles or polygons provided by SDL_gfx on SDL2 against renderers of SDL2.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries to develop SDL applications.
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The %name library provides the basic drawing functions such as lines,
circles or polygons provided by SDL_gfx on SDL2 against renderers of SDL2.
%endif

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static} \
%ifnarch %ix86 x86_64
	--disable-mmx \
%endif

%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%_libdir/lib%name.la

%files -n lib%name
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_libdir/lib%name-1.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/*.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Mon Jun 23 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.1-alt2
- Disable MMX on non x86 and x64 arch (thanks Sergey Bolshakov)

* Sat Jun 21 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.1-alt0.M70T.1
- Build for branch t7

* Sat Jun 21 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Wed Feb 05 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt0.M70T.1
- Build for branch t7

* Sat Nov 02 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux
