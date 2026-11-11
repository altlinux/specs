%define abiversion 4
%define libname libcurl%abiversion-impersonate
%define boring_commit 156c7b75ae9b8c3b3f847acf264f17594c3859fb

Name: curl-impersonate
Version: 2.3.2
Release: alt1

Summary: curl with browser TLS and HTTP fingerprints

License: curl AND Apache-2.0 AND ISC AND OpenSSL AND MIT
Group: Networking/WWW
ExcludeArch: %ix86
URL: https://github.com/lexiforest/curl-impersonate
# Source-url: https://github.com/lexiforest/curl-impersonate/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# Source1-url: https://github.com/curl/curl/archive/curl-8_23_0.tar.gz
Source1: curl-8.23.0.tar
# Source2-url: https://github.com/google/boringssl/archive/156c7b75ae9b8c3b3f847acf264f17594c3859fb.tar.gz
Source2: boringssl-156c7b75ae9b8c3b3f847acf264f17594c3859fb.tar
# Source3-url: https://github.com/nghttp2/nghttp2/releases/download/v1.63.0/nghttp2-1.63.0.tar.bz2
Source3: nghttp2-1.63.0.tar
# Source4-url: https://github.com/ngtcp2/nghttp3/releases/download/v1.15.0/nghttp3-1.15.0.tar.bz2
Source4: nghttp3-1.15.0.tar
# Source5-url: https://github.com/ngtcp2/ngtcp2/releases/download/v1.20.0/ngtcp2-1.20.0.tar.bz2
Source5: ngtcp2-1.20.0.tar
Patch: shared-only-install.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake gcc-c++ golang ninja-build
BuildRequires: pkgconfig(libbrotlidec) pkgconfig(libzstd) pkgconfig(zlib)
BuildRequires: pkgconfig(libidn2) pkgconfig(libcares)

%description
curl-impersonate reproduces browser TLS and HTTP fingerprints.
BoringSSL is built from the upstream-pinned source commit and embedded because
the impersonation APIs and TLS extension behaviour require upstream patches.
The HTTP/2 and QUIC helper libraries are also built privately from the pinned
sources required by the browser fingerprint patches. Compression, IDN and DNS
resolver libraries use the system packages.

%package -n %libname
Summary: Browser-impersonating curl shared library

Group: System/Libraries
# The TLS trust store is data read at runtime and is not an ELF dependency.
Requires: ca-certificates

%description -n %libname
Shared libcurl-impersonate library, separate from the system libcurl.
Patched BoringSSL is embedded from a pinned source commit because browser TLS
fingerprints require its nonstandard extension ordering and compression APIs.
Pinned HTTP/2 and QUIC sources supply additional browser fingerprint APIs.

%package -n %libname-devel
Summary: Development files for libcurl-impersonate

Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
Headers and pkg-config metadata for libcurl-impersonate. Headers are installed
in a separate directory so they can coexist with the system libcurl headers.

%prep
%setup -a1 -a2 -a3 -a4 -a5
%patch -p1
# Apply the patches shipped by this release to exactly its pinned sources.
for dep in boringssl nghttp3 ngtcp2; do
    patch -d "$dep" -p1 < "patches/$dep.patch"
done
patch -d curl-8.23.0 -p1 < patches/curl.patch
mkdir licenses
cp boringssl/LICENSE licenses/BoringSSL
cp nghttp2/COPYING licenses/nghttp2
cp nghttp3/COPYING licenses/nghttp3
cp ngtcp2/COPYING licenses/ngtcp2
cp curl-8.23.0/COPYING licenses/curl

%build
export top="$PWD"
export private="$PWD/private"
# All sub-builds run sequentially and inherit hasher's memory-limited job count.
build_private() {
    source_dir="$1"
    shift
    cmake -G Ninja -S "$source_dir" -B "build-$source_dir" \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_C_FLAGS="%optflags -fPIC" \
        -DCMAKE_CXX_FLAGS="%optflags -fPIC" \
        -DCMAKE_INSTALL_PREFIX="$private" \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_PREFIX_PATH="$private" \
        -DCMAKE_SKIP_RPATH=ON \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTING=OFF "$@"
    cmake --build "build-$source_dir" --parallel %__nprocs
    cmake --install "build-$source_dir"
}
build_private boringssl
build_private nghttp2 -DENABLE_LIB_ONLY=ON -DBUILD_STATIC_LIBS=ON \
    -DENABLE_DOC=OFF -DCMAKE_DISABLE_FIND_PACKAGE_Libnghttp3=ON
build_private nghttp3 -DENABLE_LIB_ONLY=ON \
    -DENABLE_SHARED_LIB=OFF -DENABLE_STATIC_LIB=ON
build_private ngtcp2 -DENABLE_LIB_ONLY=ON \
    -DENABLE_SHARED_LIB=OFF -DENABLE_STATIC_LIB=ON \
    -DENABLE_OPENSSL=OFF -DENABLE_BORINGSSL=ON \
    -DENABLE_PICOTLS=OFF -DENABLE_WOLFSSL=OFF -DENABLE_GNUTLS=OFF \
    -DBORINGSSL_INCLUDE_DIR="$private/include" \
    -DBORINGSSL_LIBRARIES="$private/lib/libssl.a;$private/lib/libcrypto.a"

# Build the patched curl directly: the upstream superbuild downloads and
# statically bundles every dependency, including unmodified system libraries.
%cmake -S curl-8.23.0 \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DCMAKE_INSTALL_INCLUDEDIR=include/curl-impersonate \
    -DCMAKE_PREFIX_PATH="$private" \
    -DCMAKE_C_FLAGS="%optflags -I$private/include" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--exclude-libs,ALL" \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_PROJECT_CURL_INCLUDE="$top/cmake/WebCrypto.cmake" \
    -DCURL_IMPERSONATE_SOURCE_DIR="$top" \
    -DCURL_IMPERSONATE_VERSION=%version \
    -DCURL_IMPERSONATE_INSTALL_SHARED=ON -DCURL_DISABLE_INSTALL=ON \
    -DCURL_USE_OPENSSL=ON -DCURL_ENABLE_SSL=ON \
    -DOPENSSL_ROOT_DIR="$private" \
    -DOPENSSL_INCLUDE_DIR="$private/include" \
    -DOPENSSL_SSL_LIBRARY="$private/lib/libssl.a" \
    -DOPENSSL_CRYPTO_LIBRARY="$private/lib/libcrypto.a" \
    -DOPENSSL_USE_STATIC_LIBS=ON \
    -DHAVE_BORINGSSL=1 -DHAVE_AWSLC=0 -DHAVE_LIBRESSL=0 \
    -DHAVE_DES_ECB_ENCRYPT=1 -DHAVE_SSL_SET0_WBIO=1 \
    -DHAVE_SSL_SET1_ECH_CONFIG_LIST=1 \
    -DHAVE_SSL_SET_QUIC_USE_LEGACY_CODEPOINT=1 -DHAVE_OPENSSL_SRP=0 \
    -DCURL_USE_PKGCONFIG=OFF \
    -DNGHTTP2_INCLUDE_DIR="$private/include" \
    -DNGHTTP2_LIBRARY="$private/lib/libnghttp2.a" \
    -DNGHTTP3_INCLUDE_DIR="$private/include" \
    -DNGHTTP3_LIBRARY="$private/lib/libnghttp3.a" \
    -DNGTCP2_INCLUDE_DIR="$private/include" \
    -DNGTCP2_LIBRARY="$private/lib/libngtcp2.a" \
    -DNGTCP2_CRYPTO_BORINGSSL_LIBRARY="$private/lib/libngtcp2_crypto_boringssl.a" \
    -DUSE_NGHTTP2=ON -DUSE_NGTCP2=ON -DUSE_PROXY_HTTP3=ON \
    -DCURL_BROTLI=ON -DCURL_ZSTD=ON -DUSE_LIBIDN2=ON \
    -DENABLE_ARES=ON -DCARES_USE_STATIC_LIBS=OFF \
    -DCURL_CA_BUNDLE=%_datadir/ca-certificates/ca-bundle.crt \
    -DCURL_CA_PATH=%_datadir/ca-certificates/ \
    -DCURL_DISABLE_LDAP=ON -DCURL_DISABLE_LDAPS=ON \
    -DCURL_USE_LIBPSL=OFF -DUSE_LIBRTMP=OFF -DCURL_USE_LIBSSH2=OFF \
    -DCURL_DISABLE_WEBSOCKETS=OFF -DUSE_ECH=ON -DUSE_SSLS_EXPORT=ON \
    -DBUILD_SHARED_LIBS=ON -DBUILD_STATIC_LIBS=OFF -DBUILD_STATIC_CURL=OFF \
    -DBUILD_CURL_EXE=ON -DBUILD_TESTING=OFF \
    -DBUILD_MISC_DOCS=OFF -DENABLE_CURL_MANUAL=OFF
%cmake_build

%install
%cmake_install

%check
LD_LIBRARY_PATH="$PWD/%_cmake__builddir/lib" \
    %_cmake__builddir/src/curl-impersonate --version | tee version.out
grep -q BoringSSL version.out
grep -q impersonate version.out
# A real offline transfer through the library and the command line client.
echo 'curl-impersonate offline transfer' > test-input
LD_LIBRARY_PATH="$PWD/%_cmake__builddir/lib" \
    %_cmake__builddir/src/curl-impersonate --impersonate chrome152 \
    "file://$PWD/test-input" -o test-output
cmp test-input test-output

%files
%doc README.md LICENSE
%_bindir/curl-impersonate
%_bindir/curl_*

%files -n %libname
%doc LICENSE licenses
%_libdir/libcurl-impersonate.so.%abiversion
%_libdir/libcurl-impersonate.so.%abiversion.*

%files -n %libname-devel
%_includedir/curl-impersonate/
%_libdir/libcurl-impersonate.so
%_pkgconfigdir/libcurl-impersonate.pc
%dir %_libdir/cmake
%_libdir/cmake/CurlImpersonate/

%changelog
* Sat Nov 07 2026 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- initial build for Sisyphus.
- exclude %%ix86: pinned BoringSSL requires SSE2.

