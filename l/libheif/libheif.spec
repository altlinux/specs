Name: libheif
Version: 1.2.0
Release: alt1%ubt
Summary: HEIF file format decoder and encoder
License: LGPLv3
Group: System/Libraries
Url: https://github.com/strukturag/libheif
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ libde265-devel libjpeg-devel libpng-devel libx265-devel

%description
HEIF is a new image file format employing HEVC (h.265) image coding for the
best compression ratios currently possible.

%package devel
Group: Development/C
Summary:  Development libraries for %name

%description devel
Development libraries for %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_libdir/%name.so.*
%_datadir/mime/packages/heif.xml
%_datadir/thumbnailers/heif.thumbnailer

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Jun 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1%ubt
- rebuild with libva 2.1.0

* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- initial release
