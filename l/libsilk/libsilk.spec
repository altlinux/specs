Summary:    libsilk is a library for the silk codec
Name:       libsilk
Version:    1.0.8
Release:    alt1
License:    Skype BSD-like 
Group:      System/Libraries
URL:        http://stash.freeswitch.org
Source:     %name-%version.tar
Patch0:     %name-%version-%release.patch

%description
libsilk is a library for the silk codec

%package devel
Summary:    silk development files
Group:      Development/C
Requires:   %name = %version-%release

%description devel
silk development files.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fisv
%configure
%make

%install
%make install DESTDIR=%buildroot

%files
%doc ChangeLog AUTHORS COPYING NEWS README 

%_libdir/libSKP_SILK_SDK.so.*
%_bindir/Decoder
%_bindir/Encoder
%_bindir/signalCompare

%files devel
%_includedir/silk
%_libdir/libSKP_SILK_SDK.so
%_libdir/pkgconfig/silk.pc

%changelog
* Wed Mar 02 2016 Anton Farygin <rider@altlinux.ru> 1.0.8-alt1
- first build for Sisyphus
