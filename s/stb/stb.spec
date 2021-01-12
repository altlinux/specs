Name: stb
Version: 2.37
Release: alt1

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

%files -n lib%name-devel
%stbdir/*
%doc *.md docs/*

%changelog
* Tue Jan 12 2021 Michael Shigorin <mike@altlinux.org> 2.37-alt1
- initial package (for TetrisGL)

