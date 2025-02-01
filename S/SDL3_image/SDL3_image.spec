%define _unpackaged_files_terminate_build 1

Name: SDL3_image
Version: 3.2.0
Release: alt1

Summary: Simple DirectMedia Layer - Image library
License: Zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_image/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/libsdl-org/SDL_image/archive/release-%version/SDL_image-release-%version.tar.gz
Source: SDL_image-release-%version.tar

BuildRequires: cmake
BuildRequires: libSDL3-devel
BuildRequires: libavif-devel
BuildRequires: libe2fs
BuildRequires: libjpeg-devel
BuildRequires: libjxl-devel
BuildRequires: libpng-devel
BuildRequires: libslang2
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
%cmake
%cmake_build

%install
%cmake_install
%__rm -rf %buildroot%_datadir/licenses

%files -n lib%name
%doc CHANGES.txt INSTALL.md LICENSE.txt README.md
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/SDL_image.h
%_pkgconfigdir/sdl3-image.pc
%_libdir/lib%name.so
%_libdir/cmake/%name

%changelog
* Sat Feb 01 2025 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt1
- Initial build for ALT Linux

