%define LibAtrac9_commit 946e05a9212976626a9f5e52f29c0a7202871f29
%define VulkanMemoryAllocator_commit a1d434708c217b2a6c7b365f1fe41fa03a562e59
%define ZArchive_commit 965b66c8d67b6b7e30fd63b3b75aa91a99ff303b
%define curl_commit 801bd5138ce31aa0d906fa4e2eabfc599d74e793
%define ffmpeg_core_commit 9ac4cfd195f192ed8b08566f49c28dbb48d08341
%define fontconfig_commit 72b9a48f57de6204d99ce1c217b5609ee92ece9b
%define harfbuzz_commit a1d9bfe62818ef0fa9cf63b6e6d51436b1c93cbc
%define icu_commit 049e0d6a420629ac7db77256987d083a563287b5
%define jxrlib_commit f7521879862b9085318e814c6157490dd9dbbdb4
%define libfvad_commit 532ab666c20d3cfda38bca63abbb0f152706c369
%define libjpeg_turbo_commit c85e6b905bf237038faa936dab160ebfc5da0344
%define libpsl_commit ba4c49a205408845834b1648ad23c15ee09f722b
%define libressl_openbsd_commit 078b3d1df8ca2011c1605cd40418c58fa0f5b143
%define libusb_cmake_commit bea6567b63796ab27c1c33257d230284fb2d8316
%define libxml2_commit 7846b0a677f8d3ce72486125fa281e92ac9970e8
%define mbedtls_commit 068ff080b369adfac81509f9b57b2afabaf82dc5
%define mbedtls_framework_commit dde0c4a0e448a0552f18817dcea633bb851fd288
%define mimalloc_commit f8401befa675adb13b98decababd7fdc59572477
%define nghttp2_commit 85e300c79fb6dbcfa9c1013215c8710c1c2cd3d2
%define ogg_commit be05b13e98b048f0b5a0f5fa8ce514d56db5f822
%define opus_commit 22244de5a79bd1d6d623c32e72bf1954b56235be
%define psl_list_commit 5db9b65997e3c9230ac4353b01994c2ae9667cb9
%define quickjs_commit 6d46d07d04041b40f4f49eaa7fdebe44c314c699
%define sqlite_commit 57520227c95396ce39ba6ecaac8d475b78dd3964
%define stb_commit 2c980bb59875b0d32144a71867fbdebb2f77cd20
%define vgmstream_commit 7c520e8f9b078dfde2f84f1b5bcbad0c6c415806
%define vorbis_commit c2aa86b05e981c96bf381fc6aa11cdd03eccc2fb
%define zlib_commit da607da739fa6047df13e66a2af6b8bec7c2a498
%define zstd_commit f8745da6ff1ad1e7bab384bd1f9d742439278e99

Name: anyps5
Version: 0.1.5
Release: alt1

Summary: Tool for porting PS5 executables to Linux and Windows
License: GPL-2.0-only
Group: Emulators

Url: https://boykopovar.github.io/AnyPS5/
Vcs: https://github.com/boykopovar/AnyPS5
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/boykopovar/AnyPS5/archive/v%version/AnyPS5-v%version.tar.gz
Source0: %name-v%version.tar
# https://github.com/shadps4-emu/ext-LibAtrac9/archive/%LibAtrac9_commit/LibAtrac9-%LibAtrac9_commit.tar.gz
Source1: LibAtrac9-%LibAtrac9_commit.tar
# https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/%VulkanMemoryAllocator_commit/VulkanMemoryAllocator-%VulkanMemoryAllocator_commit.tar.gz
Source2: VulkanMemoryAllocator-%VulkanMemoryAllocator_commit.tar
# https://github.com/Exzap/ZArchive/archive/%ZArchive_commit/ZArchive-%ZArchive_commit.tar.gz
Source3: ZArchive-%ZArchive_commit.tar
# https://github.com/curl/curl/archive/%curl_commit/curl-%curl_commit.tar.gz
Source4: curl-%curl_commit.tar
# https://github.com/KytyPS5/ext-ffmpeg-core/archive/%ffmpeg_core_commit/ffmpeg-core-%ffmpeg_core_commit.tar.gz
Source5: ffmpeg-core-%ffmpeg_core_commit.tar
# https://github.com/fontconfig/fontconfig/archive/%fontconfig_commit/fontconfig-%fontconfig_commit.tar.gz
Source6: fontconfig-%fontconfig_commit.tar
# https://github.com/harfbuzz/harfbuzz/archive/%harfbuzz_commit/harfbuzz-%harfbuzz_commit.tar.gz
Source7: harfbuzz-%harfbuzz_commit.tar
# https://github.com/unicode-org/icu/archive/%icu_commit/icu-%icu_commit.tar.gz
Source8: icu-%icu_commit.tar
# https://github.com/4creators/jxrlib/archive/%jxrlib_commit/jxrlib-%jxrlib_commit.tar.gz
Source9: jxrlib-%jxrlib_commit.tar
# https://github.com/dpirch/libfvad/archive/%libfvad_commit/libfvad-%libfvad_commit.tar.gz
Source10: libfvad-%libfvad_commit.tar
# https://github.com/libjpeg-turbo/libjpeg-turbo/archive/%libjpeg_turbo_commit/libjpeg-turbo-%libjpeg_turbo_commit.tar.gz
Source11: libjpeg-turbo-%libjpeg_turbo_commit.tar
# https://github.com/rockdaboot/libpsl/archive/%libpsl_commit/libpsl-%libpsl_commit.tar.gz
Source12: libpsl-%libpsl_commit.tar
# https://github.com/libressl/openbsd/archive/%libressl_openbsd_commit/libressl-openbsd-%libressl_openbsd_commit.tar.gz
Source13: libressl-openbsd-%libressl_openbsd_commit.tar
# https://github.com/libusb/libusb-cmake/archive/%libusb_cmake_commit/libusb-cmake-%libusb_cmake_commit.tar.gz
Source14: libusb-cmake-%libusb_cmake_commit.tar
# https://github.com/GNOME/libxml2/archive/%libxml2_commit/libxml2-%libxml2_commit.tar.gz
Source15: libxml2-%libxml2_commit.tar
# https://github.com/Mbed-TLS/mbedtls/archive/%mbedtls_commit/mbedtls-%mbedtls_commit.tar.gz
Source16: mbedtls-%mbedtls_commit.tar
# https://github.com/microsoft/mimalloc/archive/%mimalloc_commit/mimalloc-%mimalloc_commit.tar.gz
Source17: mimalloc-%mimalloc_commit.tar
# https://github.com/nghttp2/nghttp2/archive/%nghttp2_commit/nghttp2-%nghttp2_commit.tar.gz
Source18: nghttp2-%nghttp2_commit.tar
# https://github.com/xiph/ogg/archive/%ogg_commit/ogg-%ogg_commit.tar.gz
Source19: ogg-%ogg_commit.tar
# https://github.com/xiph/opus/archive/%opus_commit/opus-%opus_commit.tar.gz
Source20: opus-%opus_commit.tar
# https://github.com/quickjs-ng/quickjs/archive/%quickjs_commit/quickjs-%quickjs_commit.tar.gz
Source21: quickjs-%quickjs_commit.tar
# https://github.com/sqlite/sqlite/archive/%sqlite_commit/sqlite-%sqlite_commit.tar.gz
Source22: sqlite-%sqlite_commit.tar
# https://github.com/nothings/stb/archive/%stb_commit/stb-%stb_commit.tar.gz
Source23: stb-%stb_commit.tar
# https://github.com/vgmstream/vgmstream/archive/%vgmstream_commit/vgmstream-%vgmstream_commit.tar.gz
Source24: vgmstream-%vgmstream_commit.tar
# https://github.com/xiph/vorbis/archive/%vorbis_commit/vorbis-%vorbis_commit.tar.gz
Source25: vorbis-%vorbis_commit.tar
# https://github.com/madler/zlib/archive/%zlib_commit/zlib-%zlib_commit.tar.gz
Source26: zlib-%zlib_commit.tar
# https://github.com/facebook/zstd/archive/%zstd_commit/zstd-%zstd_commit.tar.gz
Source27: zstd-%zstd_commit.tar

# https://github.com/publicsuffix/list/archive/%psl_list_commit/psl-list-%psl_list_commit.tar.gz
Source28: psl-list-%psl_list_commit.tar
# https://github.com/Mbed-TLS/mbedtls-framework/archive/%mbedtls_framework_commit/mbedtls-framework-%mbedtls_framework_commit.tar.gz
Source29: mbedtls-framework-%mbedtls_framework_commit.tar

Patch1: %name-ffmpeg-system.patch
Patch2: %name-revision-override.patch
Patch3: %name-libc-weak-hooks.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glslang
BuildRequires: glslang-devel
BuildRequires: glibc-devel-static
BuildRequires: libSDL2-devel
BuildRequires: libavcodec-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libatomic-devel-static
BuildRequires: libfreetype-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: ninja-build
BuildRequires: pkg-config
BuildRequires: python3
BuildRequires: spirv-headers
BuildRequires: vulkan-headers

# The .prx payload is excluded from automatic dependency generation, so the
# host libraries it links against are listed explicitly (see the NEEDED lists
# of the built libraries).
Requires: libSDL2
Requires: libfreetype
Requires: libavcodec63 libavformat63 libavutil61 libavfilter12 libswresample7 libswscale10
Requires: libglslang16 libspirv-tools0
Requires: libstdc++6 libgcc1
Requires: libstdc++.so.6(GLIBCXX_3.4.35)(64bit)
Requires: libc.so.6(GLIBC_2.43)(64bit)

%description
AnyPS5 relinks PlayStation 5 executables (ELF) into native Linux executables
without emulation or a separate runtime process, and builds implementations of
the PS5 system prx libraries suitable for dynamic linking.

A relinked title looks for the system libraries in a libs/ directory next to
itself (the relinker default rpath is '$ORIGIN/libs'). The anyps5-relink
wrapper passes an additional rpath entry pointing to the system-wide copy of
the libraries installed under %_libexecdir/%name.

# The .prx files are PS5 guest-side shared objects: their inter-library
# DT_NEEDED (libc.prx, libkernel.prx, ...) resolves at dlopen() time from
# the same directory and must not become RPM dependencies.
%add_findreq_skiplist %_libexecdir/%name/*.prx
%add_findprov_skiplist %_libexecdir/%name/*.prx

%prep
%setup -n %name-v%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13 -b 14 -b 15 -b 16 -b 17 -b 18 -b 19 -b 20 -b 21 -b 22 -b 23 -b 24 -b 25 -b 26 -b 27 -b 28 -b 29

%__rm -rf 3rdparty/LibAtrac9
%__mv -Tf ../LibAtrac9-%LibAtrac9_commit 3rdparty/LibAtrac9
%__rm -rf 3rdparty/VulkanMemoryAllocator
%__mv -Tf ../VulkanMemoryAllocator-%VulkanMemoryAllocator_commit 3rdparty/VulkanMemoryAllocator
%__rm -rf 3rdparty/ZArchive
%__mv -Tf ../ZArchive-%ZArchive_commit 3rdparty/ZArchive
%__rm -rf 3rdparty/curl
%__mv -Tf ../curl-%curl_commit 3rdparty/curl
%__rm -rf 3rdparty/ffmpeg-core
%__mv -Tf ../ffmpeg-core-%ffmpeg_core_commit 3rdparty/ffmpeg-core
%__rm -rf 3rdparty/fontconfig
%__mv -Tf ../fontconfig-%fontconfig_commit 3rdparty/fontconfig
%__rm -rf 3rdparty/harfbuzz
%__mv -Tf ../harfbuzz-%harfbuzz_commit 3rdparty/harfbuzz
%__rm -rf 3rdparty/icu
%__mv -Tf ../icu-%icu_commit 3rdparty/icu
%__rm -rf 3rdparty/jxrlib
%__mv -Tf ../jxrlib-%jxrlib_commit 3rdparty/jxrlib
%__rm -rf 3rdparty/libfvad
%__mv -Tf ../libfvad-%libfvad_commit 3rdparty/libfvad
%__rm -rf 3rdparty/libjpeg-turbo
%__mv -Tf ../libjpeg-turbo-%libjpeg_turbo_commit 3rdparty/libjpeg-turbo
%__rm -rf 3rdparty/libpsl
%__mv -Tf ../libpsl-%libpsl_commit 3rdparty/libpsl
%__rm -rf 3rdparty/libressl-openbsd
%__mv -Tf ../libressl-openbsd-%libressl_openbsd_commit 3rdparty/libressl-openbsd
%__rm -rf 3rdparty/libusb-cmake
%__mv -Tf ../libusb-cmake-%libusb_cmake_commit 3rdparty/libusb-cmake
%__rm -rf 3rdparty/libxml2
%__mv -Tf ../libxml2-%libxml2_commit 3rdparty/libxml2
%__rm -rf 3rdparty/mbedtls
%__mv -Tf ../mbedtls-%mbedtls_commit 3rdparty/mbedtls
%__rm -rf 3rdparty/mimalloc
%__mv -Tf ../mimalloc-%mimalloc_commit 3rdparty/mimalloc
%__rm -rf 3rdparty/nghttp2
%__mv -Tf ../nghttp2-%nghttp2_commit 3rdparty/nghttp2
%__rm -rf 3rdparty/ogg
%__mv -Tf ../ogg-%ogg_commit 3rdparty/ogg
%__rm -rf 3rdparty/opus
%__mv -Tf ../opus-%opus_commit 3rdparty/opus
%__rm -rf 3rdparty/quickjs
%__mv -Tf ../quickjs-%quickjs_commit 3rdparty/quickjs
%__rm -rf 3rdparty/sqlite
%__mv -Tf ../sqlite-%sqlite_commit 3rdparty/sqlite
%__rm -rf 3rdparty/stb
%__mv -Tf ../stb-%stb_commit 3rdparty/stb
%__rm -rf 3rdparty/vgmstream
%__mv -Tf ../vgmstream-%vgmstream_commit 3rdparty/vgmstream
%__rm -rf 3rdparty/vorbis
%__mv -Tf ../vorbis-%vorbis_commit 3rdparty/vorbis
%__rm -rf 3rdparty/zlib
%__mv -Tf ../zlib-%zlib_commit 3rdparty/zlib
%__rm -rf 3rdparty/zstd
%__mv -Tf ../zstd-%zstd_commit 3rdparty/zstd
%__rm -rf 3rdparty/libpsl/list
%__mv -Tf ../psl-list-%psl_list_commit 3rdparty/libpsl/list
%__rm -rf 3rdparty/mbedtls/framework
%__mv -Tf ../mbedtls-framework-%mbedtls_framework_commit 3rdparty/mbedtls/framework
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
export ANYPS5_RELINKER_REVISION_OVERRIDE="v%version"
%cmake -GNinja \
	-DANYPS5_USE_SYSTEM_DEPS:BOOL=ON \
	-DANYPS5_ENABLE_SPIRV_TOOLS:BOOL=ON \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-Wno-dev
%cmake_build
%cmake_build --target libs

%install
%__mkdir_p %buildroot%_bindir %buildroot%_libexecdir/%name
%__install -m 755 %_cmake__builddir/core/relinker/relinker %buildroot%_bindir/relinker
%__install -m 755 %_cmake__builddir/core/libs/libs/*.prx %buildroot%_libexecdir/%name/
%__install -m 755 %_cmake__builddir/core/libs/libs/libmimalloc.so %buildroot%_libexecdir/%name/
{
	echo '#!/bin/sh'
	echo 'exec %_bindir/relinker --rpath "$ORIGIN/libs:%_libexecdir/%name" "$@"'
} > %buildroot%_bindir/%name-relink
chmod 755 %buildroot%_bindir/%name-relink

%check
%__mkdir_p build-check
cmake -S . -B build-check -G Ninja \
	-DANYPS5_RELINKER_ONLY:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-Wno-dev
%__cmake --build build-check --parallel
for t in optional_plt empty_tls linux_load_alignment elf_header; do
	python3 core/relinker/relinker/tests/test_$t.py build-check/core/relinker/relinker
done

%files
%doc README.md docs/user/USAGE.md
%_bindir/relinker
%_bindir/%name-relink
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
* Fri Nov 13 2026 Nazarov Denis <nenderus@altlinux.org> 0.1.5-alt1
- Version 0.1.5
