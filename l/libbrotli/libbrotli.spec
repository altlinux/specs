%define _name brotli
%def_enable check

Name: lib%_name
Version: 1.1.0
Release: alt1

Summary: Library implementing the Brotli compression algorithm
Group: Development/C++
License: Apache-2.0 and MIT
Url: http://daniel.haxx.se/blog/2015/09/30/libbrotli-is-brotli-in-lib-form/

# Source-url: https://github.com/google/brotli/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake ctest

%description
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n %_name
Summary: CLI to the Brotli compression
License: Apache-2.0
Group: File tools

%description -n %_name
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n %{name}common
Summary: Library implementing the Brotli common functions
License: Apache-2.0
Group: System/Libraries
Obsoletes: %{name}common0 <= 1.0.4
Provides: %{name}common0 = %version-%release

%description -n %{name}common
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n %{name}dec
Summary: Library implementing the Brotli decompressor
License: Apache-2.0
Group: System/Libraries
Requires: %{name}common = %version-%release
Obsoletes: %{name}dec0 <= 1.0.4
Provides: %{name}dec0 = %version-%release

%description -n %{name}dec
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n %{name}enc
Summary: Library implementing the Brotli compressor
License: Apache-2.0
Group: System/Libraries
Requires: %{name}common = %version-%release
Obsoletes: %{name}enc0 <= 1.0.4
Provides: %{name}enc0 = %version-%release

%description -n %{name}enc
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package devel
Summary: Library implementing the Brotli compression algorithm
License: Apache-2.0
Group: Development/C++
Requires: %{name}dec = %version-%release
Requires: %{name}enc = %version-%release
Requires: %{name}common = %version-%release

%description devel
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

This subpackage contains libraries and header files for developing
applications that want to make use of libcerror.

%prep
%setup
sed  -i "s|\-R\${libdir} ||" scripts/*.pc.in

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake_insource -DCMAKE_BUILD_TYPE="Release"
%make_build

%install
%makeinstall_std
# ignore static libs
rm -f %buildroot%_libdir/*.a

%check
%make test

%files -n brotli
%_bindir/brotli

%files -n %{name}common
%_libdir/%{name}common.so.1
%_libdir/%{name}common.so.%version

%files -n %{name}dec
%_libdir/%{name}dec.so.1
%_libdir/%{name}dec.so.%version

%files -n %{name}enc
%_libdir/%{name}enc.so.1
%_libdir/%{name}enc.so.%version

%files devel
%_includedir/brotli/
%_libdir/%{name}*.so
%_pkgconfigdir/*.pc
%doc README.md LICENSE CONTRIBUTING.md

%changelog
* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Sep 10 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt2
- fixed pc-files (ALT #38913)

* Mon Sep 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9

* Wed Oct 24 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Thu Sep 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Mon Jul 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5
- removed bad "0" suffix from library names

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- new version 1.0.4 (with rpmrb script)

* Sat Mar 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Mon Dec 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Tue Oct 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Thu Mar 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus

* Fri Oct  2 2015 jengelh@inai.de
- Initial package (version 0.1.0~git30) for build.opensuse.org
- Add inline.diff
