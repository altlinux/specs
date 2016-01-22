Name: SDL2_image
Version: 2.0.1
Release: alt1

Summary: Simple DirectMedia Layer - Image library
License: zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_image/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://www.libsdl.org/projects/SDL_image/release/%name-%version.tar.gz

BuildRequires: chrpath
BuildRequires: libSDL2-devel >= 2.0.1
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel

%description
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PNM (PPM/PGM/PBM), XPM, LBM, PCX, GIF, JPEG, PNG,
TGA, and TIFF formats.

%package -n lib%name
Summary: Simple DirectMedia Layer - Image library
Group: System/Libraries

%description -n lib%name
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PNM (PPM/PGM/PBM), XPM, LBM, PCX, GIF, JPEG, PNG,
TGA, and TIFF formats.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C
Requires: lib%name = %version-%release
Requires: libSDL2-devel >= 2.0.1

%description -n lib%name-devel
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PNM (PPM/PGM/PBM), XPM, LBM, PCX, GIF, JPEG, PNG,
TGA, and TIFF formats.

This is the libraries, include files and other resources you can use
to develop SDL applications.

%prep
%setup

%build
%__autoconf
%configure \
	--disable-jpg-shared \
	--disable-png-shared \
	--disable-jpg-shared \
	--disable-tif-shared \
	--disable-webp-shared \
	--disable-static

%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%_libdir/lib%name.la
chrpath -d %buildroot%_libdir/lib%name-2.0.so.*

%files -n lib%name
%doc CHANGES.txt COPYING.txt README.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/SDL_image.h
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%changelog
* Fri Jan 22 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Wed Feb 05 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt2.M70T.1
- Build for branch t7

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt3
- rebuilt against libwebp.so.5

* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt2
- Fix url

* Wed Oct 30 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Initial build for ALT Linux
