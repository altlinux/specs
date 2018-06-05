Name: zopfli
Version: 1.0.2
Release: alt1

Summary: Zlib compatible better compressor

License: ASL 2.0
Group: File tools
Url: https://github.com/google/zopfli

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/google/%name/archive/%name-%version.tar.gz
Source: %name-%version.tar

# https://github.com/google/zopfli/pull/92
Patch: 0001-Honor-user-C-XX-FLAGS.patch

BuildRequires: gcc-c++

%add_optflags -Wno-unused-function

%description
Zopfli is a compression algorithm bit-stream compatible with
compression used in gzip, Zip, PNG, HTTP requests, and others. Zopfli
compresses more (~5 percent) but is slower (~100x) and uses more CPU, and is
hence best suited for applications where data is compressed once and
sent over a network many times, for example, static content for the
web.

%package -n lib%name
Summary: Zopfli compress/decompress libraries
Group: System/Libraries

%description -n lib%name
Zopfli is a compression algorithm bit-stream compatible with
compression used in gzip, Zip, PNG, HTTP requests, and others. Zopfli
compresses more (~5 percent) but is slower (~100x) and uses more CPU, and is
hence best suited for applications where data is compressed once and
sent over a network many times, for example, static content for the
web.

This package provides Zopfli compress/decompress shared libraries.

%package -n lib%name-devel
Summary: Zopfli compress/decompress libraries
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Zopfli is a compression algorithm bit-stream compatible with
compression used in gzip, Zip, PNG, HTTP requests, and others. Zopfli
compresses more (~5 percent) but is slower (~100x) and uses more CPU, and is
hence best suited for applications where data is compressed once and
sent over a network many times, for example, static content for the
web.

This package provides development files for Zopfli compress/decompress
libraries.


%prep
%setup

%build
# TODO: use cmake
# TODO: add LDFLAGS with -lm
%make_build CFLAGS="%optflags -lm" \
    zopfli zopflipng
mkdir static && cp zopfli zopflipng static/
make clean
%make_build CFLAGS="%optflags -lm" CXXFLAGS="%optflags" \
    libzopfli libzopflipng

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir}
install -m 0755 static/zopfli static/zopflipng %buildroot%_bindir/
install -m 0644 libzopfli.so.%version libzopflipng.so.%version %buildroot%_libdir/
install -m 0644 src/zopflipng/zopflipng_lib.h %buildroot%_includedir/
install -m 0644 src/zopfli/zopfli.h %buildroot%_includedir/
# FIXME:
ln -s libzopfli.so.1 %buildroot%_libdir/libzopfli.so
ln -s libzopfli.so.%version %buildroot%_libdir/libzopfli.so.1
ln -s libzopflipng.so.1 %buildroot%_libdir/libzopflipng.so
ln -s libzopflipng.so.%version %buildroot%_libdir/libzopflipng.so.1

%files
%doc COPYING
%doc CONTRIBUTORS README README.zopflipng
%_bindir/zopfli
%_bindir/zopflipng

%files -n lib%name
%_libdir/libzopfli.so.*
%_libdir/libzopflipng.so.*

%files -n lib%name-devel
%_libdir/libzopfli.so
%_libdir/libzopflipng.so
%_includedir/zopflipng_lib.h
%_includedir/zopfli.h
%doc README


%changelog
* Tue Jun 05 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)
- add libzopfli and libzopfli-devel subpackages (ALT bug 34993)

* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar  2 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-2
- Ship zopflipng

* Wed Feb 10 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-1
- Update to 1.0.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0.0-1
- upstream release 1.0.0

* Sun Mar 03 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.20130303gitacc035
- initial spec
