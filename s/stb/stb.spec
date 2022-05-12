Name: stb
Version: 2.37
Release: alt1.1

Summary: single-file libraries for C/C++
License: MIT or ALT-Public-Domain
Group: Development/C++

# see stb.h for the version
Url: http://github.com/nothings/stb
Source: %name-%version.tar

%define stbdir %_includedir/stb

%description
Noteworthy:
* image loader: stb_image.h
* image writer: stb_image_write.h
* image resizer: stb_image_resize.h
* font text rasterizer: stb_truetype.h
* typesafe containers: stb_ds.h

%package -n lib%name-devel
Summary: single-file libraries for C/C++
Group: Development/C++
BuildArch: noarch

%description -n lib%name-devel
Header files for STB library.

Noteworthy:
* image loader: stb_image.h
* image writer: stb_image_write.h
* image resizer: stb_image_resize.h
* font text rasterizer: stb_truetype.h
* typesafe containers: stb_ds.h

%prep
%setup

%build

%install
mv stb_vorbis.c stb_vorbis.h
mkdir -p %buildroot%stbdir
install -pm644 *.h %buildroot%stbdir
# Install stb.pc file
mkdir -p %buildroot%_datadir/pkgconfig
cat > %buildroot%_datadir/pkgconfig/%name.pc << END.
prefix=/usr
includedir=\${prefix}/include/stb

Name: %name
Version: %version
Description: Single-file libraries for C/C++
Cflags: -I\${includedir}
END.

%files -n lib%name-devel
%doc *.md docs/*
%stbdir/*
%_datadir/pkgconfig/%name.pc

%changelog
* Wed May 11 2022 Andrey Cherepanov <cas@altlinux.org> 2.37-alt1.1
- NMU: added stb.pc file

* Tue Jan 12 2021 Michael Shigorin <mike@altlinux.org> 2.37-alt1
- initial package (for TetrisGL)

