Name: libbrotli
Version: 0.5.2
Release: alt1

Summary: Library implementing the Brotli compression algorithm

License: Apache-2.0 and MIT
Group: Development/C++
Url: http://daniel.haxx.se/blog/2015/09/30/libbrotli-is-brotli-in-lib-form/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/google/brotli/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++

BuildRequires: rpm-macros-cmake cmake

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

%package -n libbrotlidec0
Summary: Library implementing the Brotli decompressor
License: Apache-2.0
Group: System/Libraries

%description -n libbrotlidec0
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package -n libbrotlienc0
Summary: Library implementing the Brotli compressor
License: Apache-2.0
Group: System/Libraries

%description -n libbrotlienc0
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

%package devel
Summary: Library implementing the Brotli compression algorithm
License: Apache-2.0
Group: Development/C++
Requires: libbrotlidec0 = %version
Requires: libbrotlienc0 = %version

%description devel
Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling. It is
similar in speed with "DEFLATE" but offers more dense compression.

This subpackage contains libraries and header files for developing
applications that want to make use of libcerror.

%prep
%setup
%__subst "s|brotli_enc STATIC|brotli_enc SHARED|g" CMakeLists.txt
%__subst "s|brotli_dec STATIC|brotli_dec SHARED|g" CMakeLists.txt

%build
%cmake_insource
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_libdir/
cp -a libbrotli*.so* %buildroot/%_libdir/
mkdir -p %buildroot%_includedir/brotli/{common,dec,enc}/
cp -a common/*.h %buildroot%_includedir/brotli/common/
cp -a dec/decode.h %buildroot%_includedir/brotli/dec/
cp -a enc/encode.h %buildroot%_includedir/brotli/enc/

%check
# TODO: wait for correct linking
#make test

%files -n brotli
%_bindir/bro

%files -n libbrotlidec0
%_libdir/libbrotli_dec.so.0*

%files -n libbrotlienc0
%_libdir/libbrotli_enc.so.0*

%files devel
%_includedir/brotli/
%_libdir/libbrotli_*.so
#%_pkgconfigdir/*.pc
%doc README.md LICENSE CONTRIBUTING.md

%changelog
* Thu Mar 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus

* Fri Oct  2 2015 jengelh@inai.de
- Initial package (version 0.1.0~git30) for build.opensuse.org
- Add inline.diff
