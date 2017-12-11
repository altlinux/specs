Name: libbrotli
Version: 1.0.2
Release: alt1

Summary: Library implementing the Brotli compression algorithm

License: Apache-2.0 and MIT
Group: Development/C++
Url: http://daniel.haxx.se/blog/2015/09/30/libbrotli-is-brotli-in-lib-form/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/google/brotli/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++

BuildRequires: rpm-macros-cmake cmake ctest

%description
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n brotli
Summary: CLI to the Brotli compression
License: Apache-2.0
Group: File tools

%description -n brotli
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n libbrotlicommon0
Summary: Library implementing the Brotli common functions
License: Apache-2.0
Group: System/Libraries

%description -n libbrotlicommon0
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n libbrotlidec0
Summary: Library implementing the Brotli decompressor
License: Apache-2.0
Group: System/Libraries
Requires: libbrotlicommon0 = %version-%release

%description -n libbrotlidec0
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n libbrotlienc0
Summary: Library implementing the Brotli compressor
License: Apache-2.0
Group: System/Libraries
Requires: libbrotlicommon0 = %version-%release

%description -n libbrotlienc0
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package devel
Summary: Library implementing the Brotli compression algorithm
License: Apache-2.0
Group: Development/C++
Requires: libbrotlidec0 = %version-%release
Requires: libbrotlienc0 = %version-%release
Requires: libbrotlicommon0 = %version-%release

%description devel
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

This subpackage contains libraries and header files for developing
applications that want to make use of libcerror.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
# ignore static libs
rm -f %buildroot%_libdir/*.a

%check
LD_LIBRARY_PATH=$(pwd) make test

%files -n brotli
%_bindir/brotli

%files -n libbrotlicommon0
%_libdir/libbrotlicommon.so.1
%_libdir/libbrotlicommon.so.%version

%files -n libbrotlidec0
%_libdir/libbrotlidec.so.1
%_libdir/libbrotlidec.so.%version

%files -n libbrotlienc0
%_libdir/libbrotlienc.so.1
%_libdir/libbrotlienc.so.%version

%files devel
%_includedir/brotli/
%_libdir/libbrotli*.so
%_pkgconfigdir/*.pc
%doc README.md LICENSE CONTRIBUTING.md

%changelog
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
