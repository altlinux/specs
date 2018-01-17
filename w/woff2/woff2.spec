Name: woff2
Version: 1.0.2
Release: alt2

Summary: WOFF2 compress/decompress tools
Group: File tools
License: Apache 2.0
Url: https://github.com/google/woff2
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/google/woff2.git
Source: %name-%version.tar
#Source: %url/archive/v%version/%name-%version.tar.gz

Requires: lib%name = %version-%release

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libbrotli-devel >= 0.6.0

%description
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF 1.0
with improved compression that is achieved by using the Brotli algorithm.
The primary purpose of the WOFF2 format is to efficiently package fonts
linked to Web documents by means of CSS @font-face rules.

This package provides WOFF2 compress/decompress tools.

%package -n lib%name
Summary: WOFF2 compress/decompress libraries
Group: System/Libraries

%description -n lib%name
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF 1.0
with improved compression that is achieved by using the Brotli algorithm.
The primary purpose of the WOFF2 format is to efficiently package fonts
linked to Web documents by means of CSS @font-face rules.

This package provides WOFF2 compress/decompress shared libraries.

%package -n lib%name-devel
Summary: WOFF2 compress/decompress libraries
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF 1.0
with improved compression that is achieved by using the Brotli algorithm.
The primary purpose of the WOFF2 format is to efficiently package fonts
linked to Web documents by means of CSS @font-face rules.

This package provides development files for WOFF2 compress/decompress
libraries.


%prep
%setup

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%_libdir
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%_bindir/
cp -a BUILD/woff2_* %buildroot%_bindir/

%files
%_bindir/woff2_compress
%_bindir/woff2_decompress
%_bindir/woff2_info

%files -n lib%name
%_libdir/libwoff2common.so.*
%_libdir/libwoff2dec.so.*
%_libdir/libwoff2enc.so.*
%doc LICENSE README.md

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc


%changelog
* Wed Jan 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- new lib%%name{,-devel} subpackages

* Mon Dec 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1.1
- autorebuild with libbrotli-1.0.2 (soname changes)

* Mon Dec 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Wed Oct 18 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- build new release

* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0-alt1
- initial build for ALT Linux Sisyphus
