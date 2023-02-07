Name: SDL2_image
Version: 2.6.3
Release: alt1

Summary: Simple DirectMedia Layer - Image library
License: Zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_image/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/libsdl-org/SDL_image/archive/release-%version/SDL_image-release-%version.tar.gz
Source: SDL_image-release-%version.tar

BuildRequires: libSDL2-devel
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

%description -n lib%name-devel
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PNM (PPM/PGM/PBM), XPM, LBM, PCX, GIF, JPEG, PNG,
TGA, and TIFF formats.

This is the libraries, include files and other resources you can use
to develop SDL applications.

%prep
%setup -n SDL_image-release-%version

%build
%configure \
	--disable-static \
	--disable-stb-image \
	--disable-jpg-shared \
	--disable-png-shared \
	--disable-tif-shared \
	--disable-jxl-shared \
	--disable-webp-shared
%make_build

%install
%makeinstall_std
%__rm -f %buildroot%_libdir/lib%name.la

%files -n lib%name
%doc CHANGES.txt README.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/SDL_image.h
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so
%_libdir/cmake/%name

%changelog
* Tue Feb 07 2023 Nazarov Denis <nenderus@altlinux.org> 2.6.3-alt1
- Version 2.6.3

* Sat Aug 20 2022 Nazarov Denis <nenderus@altlinux.org> 2.6.2-alt1
- Version 2.6.2

* Tue Jul 19 2022 Nazarov Denis <nenderus@altlinux.org> 2.6.0-alt2
- --disable-*-shared: Link, rather than dlopen

* Sun Jul 10 2022 Nazarov Denis <nenderus@altlinux.org> 2.6.0-alt1
- Version 2.6.0

* Wed Feb 10 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.5-alt1
- Versioon 2.0.5

* Mon Apr 08 2019 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt3
- Remove libpng15 from build requires (ALT #36560)

* Sun Apr 07 2019 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt2
- Remove %ubt macro

* Fri Nov 02 2018 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt1%ubt
- Version 2.0.4

* Sun Mar 11 2018 Nazarov Denis <nenderus@altlinux.org> 2.0.3-alt1%ubt
- Version 2.0.3

* Sun Nov 19 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt2%ubt
- Fix build

* Thu Oct 26 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1%ubt
- Version 2.0.2

* Tue Oct 10 2017 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1%ubt
- Rebuilt with new libwebp

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
