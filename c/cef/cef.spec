%define _unpackaged_files_terminate_build 1
%define abiversion 156
%define chromium_version 156.0.8078.79
%define llvm_version 22.1
%define target out/Release
%define cef_arch %_target_cpu
%ifarch x86_64
%define cef_arch x64
%endif
%ifarch aarch64
%define cef_arch arm64
%endif
%define cef_target out/Release_GN_%cef_arch
%define cef_libdir %_libdir/cef%abiversion
%define cef_sdkdir %_datadir/cef

%ifndef build_parallel_jobs
%global build_parallel_jobs %__nprocs
%endif
# Retain the released ALT Chromium concurrency ceiling.
%define max_jobs 42

# Public ALT distribution API key, retained from the Chromium build inputs.
%define api_key               AIzaSyAIIWz7zaCwYcUSe3ZaRPviXjMjkBP4-xY

Name: cef
Version: 156.0.15
Release: alt1

Summary: Chromium Embedded Framework
License: BSD-3-Clause and LGPL-2.1+
Group: System/Libraries
URL: https://github.com/chromiumembedded/cef
VCS: https://github.com/chromiumembedded/cef.git

# The engine and ALT patches come from chromium-%chromium_version-alt1.
Source0: chromium.tar.zst
Source500: cef-%version.tar.gz
Source501: cef_source_version.json
Source502: cef-check-host-tools.py
Patch500: cef-alt-chromium156.patch
Patch501: cef-alt-source-archive.patch
Patch502: cef-tests-platform.patch
# Keep the resource index consistent with ALT's Catapult patch, Patch026.
Patch503: cef-alt-resources.patch
Patch504: cef-distribution.patch
Patch505: cef-tests-alt.patch
Patch506: cef-external-begin-frame.patch
Patch507: cef-tests-lifetime.patch
Patch508: cef-native-arm64.patch
Patch509: cef-tests-cors.patch
Patch510: cef-system-libraries.patch
Patch511: cef-typescript-stdlib.patch
Patch001: 0001-OPENSUSE-enables-reading-of-the-master-preference.patch
Patch002: 0002-ALT-Set-appropriate-desktop-file-name-for-default-br.patch
Patch003: 0003-DEBIAN-manpage-fixes.patch
Patch004: 0004-DEBIAN-ps-print.patch
Patch005: 0005-ALT-Use-rpath-link-and-absolute-rpath.patch
Patch006: 0006-ALT-allow-to-override-clang-through-env-variables.patch
Patch007: 0007-OPENSUSE-chromium-152-value_or.patch
Patch008: 0008-FEDORA-bootstrap-with-python3.patch
Patch009: 0009-DEBIAN-system-golang.patch
Patch010: 0010-gentoo-stylesheet.patch
Patch011: 0011-DEBIAN-allow-building-against-system-libraries-even-.patch
Patch012: 0012-DEBIAN-swiftshader-use-llvm-16.patch
Patch013: 0013-DEBIAN-use-system-opus-library-instead-of-embedded.patch
Patch014: 0014-DEBIAN-build-using-system-openjpeg.patch
Patch015: 0015-DEBIAN-use-system-jpeg-library.patch
Patch016: 0016-DEBIAN-disable-font-tests.patch
Patch017: 0017-DEBIAN-disable-tests.patch
Patch018: 0018-Use-yandex-search-as-default.patch
Patch019: 0019-DEBIAN-bindgen.patch
Patch020: 0020-ALT-swiftshader-fix-llvm.patch
Patch021: 0021-FEDORA-System-brotli.patch
Patch022: 0022-ALT-block-error-from-google.patch
Patch023: 0023-Add-missing-headers.patch
Patch024: 0024-DEBIAN-chromium-148-rust-bytemuck.patch
Patch025: 0025-Fix-rust-clang-path.patch
Patch026: 0026-DEBIAN-remove-dependencies-on-third_party-catapult.patch
Patch027: 0027-DEBIAN-disable-tests-swiftshader.patch
Patch029: 0029-DEBIAN-swiftshader-fix-build.patch
Patch030: 0030-DEBIAN-disable-rustc-allow-features.patch
Patch031: 0031-FEDORA-disable-screen-ai-service.patch
Patch032: 0032-FEDORA-chromium-145-rustc-ftbfs.patch
Patch033: 0033-DEBIAN-gn-inputs.patch
Patch034: 0034-DEBIAN-gn-inputs2.patch
Patch036: 0036-ALT-disable-lens-overlay.patch
Patch037: 0037-ALT-clang-path.patch
Patch038: 0038-DEBIAN-iota.patch
Patch040: 0040-DEBIAN-verification-tokens.patch
Patch041: 0041-DEBIAN-highway-include-path.patch
Patch042: 0042-DEBIAN-material-utils.patch
Patch043: 0043-DEBIAN-memory-allocator-dcheck-assert-fix.patch
Patch044: 0044-DEBIAN-av1-vaapi.patch
Patch045: 0045-DEBIAN-node-version-ck.patch
Patch046: 0046-DEBIAN-libcpp-headers.patch
Patch047: 0047-DEBIAN-libpng-testonly.patch
Patch048: 0048-DEBIAN-disable-ai-search-shortcuts.patch
Patch049: 0049-DEBIAN-clang19-cookie-string-view.patch
Patch050: 0050-OPENSUSE-chromium-155-v8_include_cpp.patch
Patch051: 0051-OPENMANDRIVA-if-chromeos-can-do-it-so-can-linux.patch
Patch052: 0052-OPENMANDRIVA-enable-hw-video-encode.patch
Patch053: 0053-OPENMANDRIVA-drop-workarounds-for-ancient-mesa-bugs.patch
Patch054: 0054-DEBIAN-disable-tos-dialog.patch
Patch055: 0055-DEBIAN-llvm-22-clang22.patch
Patch056: 0056-ALT-highway-path.patch
Patch057: 0057-DEBIAN-llvm-22-shut-up-clang.patch
Patch058: 0058-DEBIAN-llvm.patch
Patch059: 0059-DEBIAN-llvm-19-clone-traits.patch
Patch060: 0060-DEBIAN-fixes-crubit.patch
Patch061: 0061-DEBIAN-autofill-binarypb.patch
Patch062: 0062-DEBIAN-nodejs-set-intersection.patch
Patch063: 0063-OPENSUSE-chromium-146-static-assert.patch
Patch064: 0064-OPENSUSE-bring_back_and_disable_allowlist.patch
Patch065: 0065-DEBIAN-stdatomic.patch
Patch066: 0066-DEBIAN-swiftshader-dependencies.patch
Patch067: 0067-DEBIAN-only-address-sanitizer.patch
Patch068: 0068-DEBIAN-safe-libcxx.patch
Patch069: 0069-DEBIAN-disable-enterprise-tests.patch
Patch070: 0070-DEBIAN-llvm-22-ignore-for-ubsan.patch
Patch071: 0071-FEDORA-chromium-139-rust-FTBFS-suppress-warnings.patch
Patch072: 0072-DEBIAN-disable-ai.patch
Patch073: 0073-FEDORA-chromium-145-rust-1.88-undefined-symbol.patch
Patch074: 0074-DEBIAN-llvm-19-const-profile.patch
Patch075: 0075-DEBIAN-llvm-19-keyfactory.patch
Patch076: 0076-DEBIAN-tsc-split-comp.patch
Patch077: 0077-DEBIAN-llvm-19-raw-ref-map-find.patch
Patch078: 0078-DEBIAN-revert-v8-sanitize.patch
Patch079: 0079-DEBIAN-arm-logging.patch
Patch091: 0091-DEBIAN-partition-alloc-serialize-pool-init.patch
Patch092: 0092-DEBIAN-rust-prebuilt-stdlib-libs.patch
Patch093: 0093-OPENSUSE-chromium-156-blink_static_cast.patch
Patch094: 0094-OPENSUSE-chromium-146-value_or.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: bison
BuildRequires: brotli
BuildRequires: bzlib-devel
BuildRequires: elfutils
# The DevTools JS bridge requires this esbuild service protocol version.
BuildRequires: esbuild = 0.28.2
BuildRequires: flex
BuildRequires: glibc-kernheaders
BuildRequires: gperf
BuildRequires: libcups-devel
BuildRequires: libdouble-conversion-devel
BuildRequires: libcxx-devel
BuildRequires: libcxx-static
BuildRequires: libcxxabi-devel
BuildRequires: libcxxabi-static
BuildRequires: llvm-libunwind-devel
BuildRequires: llvm-libunwind-static
BuildRequires: libpthreadpool-devel
BuildRequires: ninja-build
BuildRequires: node
BuildRequires: typescript-go
BuildRequires: nvidia-settings-devel
BuildRequires: perl-Switch
BuildRequires: pkg-config
BuildRequires: usbids
BuildRequires: clang%llvm_version
BuildRequires: clang%llvm_version-devel
BuildRequires: clang%llvm_version-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk+-unix-print-3.0)
BuildRequires: llvm%llvm_version-devel
BuildRequires: lld%llvm_version-devel
BuildRequires: pkgconfig(absl_utility)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(atk-bridge-2.0)
BuildRequires: pkgconfig(atspi-2)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(dri)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(flatbuffers)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(krb5-gssapi)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libhwy)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(nspr)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(openh264)
BuildRequires: pkgconfig(re2)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb-proto)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xshmfence)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(opus)
BuildRequires: rust-bindgen
BuildRequires: python3
BuildRequires: python3(bs4)
BuildRequires: python3(html5lib)
BuildRequires: python3(markupsafe)
BuildRequires: python3(ply)
BuildRequires: python3(simplejson)
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: rustfmt
BuildRequires: golang
BuildRequires: cmake
BuildRequires: dbus
BuildRequires: fonts-ttf-dejavu
BuildRequires: fonts-ttf-liberation
BuildRequires: openbox-base
BuildRequires: python3(psutil)
BuildRequires: xcompmgr
BuildRequires: time
BuildRequires: xvfb-run

# The upstream CEF SDK supports x86_64 and aarch64.
ExcludeArch: %ix86

%description
The Chromium Embedded Framework embeds Chromium in native applications.
This package is built from CEF %version and the ALT Chromium
%chromium_version engine sources and patches.

%package -n libcef%abiversion
Summary: Chromium Embedded Framework runtime, ABI %abiversion
Group: System/Libraries

%description -n libcef%abiversion
The public CEF shared library and the matching Chromium engine resources.
Resource IDs, V8 snapshots and the private SwiftShader Vulkan driver belong
to this engine version and are installed in its ABI-specific directory.

%package -n libcef-devel
Summary: Development files for Chromium Embedded Framework
Group: Development/C++
Requires: libcef%abiversion = %EVR

%description -n libcef-devel
CEF headers, the public linker library and the upstream CMake/Bazel SDK.
The C++ wrapper sources are built by each consumer for its selected C API.
Use %cef_sdkdir as CEF_ROOT with the upstream CMake build interface.

%prep
%setup -q -n chromium -a500
mv cef-%version cef
%autopatch -p1
cp %SOURCE501 cef/cef_source_version.json

# CEF generators use the same system compiler as Chromium.
mkdir -p third_party/llvm-build/Release+Asserts/bin
ln -s %_bindir/clang third_party/llvm-build/Release+Asserts/bin/clang
sed -i \
        -e 's/"-ffile-compilation-dir=."//g' \
        -e 's/"-no-canonical-prefixes"//g' \
        -e 's/"-no-opaque-pointers",//g' \
        build/config/compiler/BUILD.gn
sed -i -e 's/-Wundef,//' tools/gn/build/gen.py
subst 's/-static-libstdc++/--stdlib=libc++/' \
    $(grep -Rl 'static-libstdc++' *)

mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s %_bindir/node third_party/node/linux/node-linux-x64/bin/node

# Upstream Linux host paths are shared by native x86_64 and aarch64 builds.
ln -sf %_bindir/tsgo third_party/typescript/linux-amd64/src/lib/tsc
ln -sf %_bindir/esbuild third_party/devtools-frontend/src/third_party/esbuild/esbuild

# gperf
mkdir -p third_party/gperf/cipd/bin/
ln -sf %_bindir/gperf third_party/gperf/cipd/bin/gperf

mkdir -p buildtools/third_party/eu-strip/bin
ln -sf %_bindir/eu-strip buildtools/third_party/eu-strip/bin/eu-strip

mkdir -p third_party/rust-toolchain/bin
ln -sf %_bindir/bindgen third_party/rust-toolchain/bin/bindgen
ln -sf %_bindir/rustfmt third_party/rust-toolchain/bin/rustfmt
ln -sf %_bindir/rustc third_party/rust-toolchain/bin/rustc

rm -f -- third_party/depot_tools/ninja
ln -s %_bindir/ninja third_party/depot_tools/ninja
ln -s %__python3 third_party/depot_tools/python

rm -v buildtools/linux64/gn

# Apply genuine CEF patches after the released ALT patches.
%__python3 cef/tools/patcher.py

%build
export ALTWRAP_LLVM_VERSION="%llvm_version"
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
export RANLIB="llvm-ranlib"
export LLVM_PREFIX=`llvm-config --prefix`
export LLVM_LIBDIR=`llvm-config --libdir`
export CLANG_MAJVER=`echo %llvm_version | cut -d. -f1`
export CLANG_LIBDIR="$LLVM_LIBDIR/clang/$CLANG_MAJVER/lib"

bits=$(getconf LONG_BIT)

export PATH="$PWD/third_party/depot_tools:$PATH"
export CHROMIUM_RPATH="%cef_libdir"

FLAGS=
FLAGS+=' -fno-delete-null-pointer-checks'
FLAGS+=' -I%_includedir/c++/v1'
FLAGS+=' -Wno-deprecated-declarations'
FLAGS+=' -Wno-implicit-fallthrough -Wno-nontrivial-memcall -Wno-shadow'
FLAGS+=' -Wno-macro-redefined'
FLAGS+=' -Wno-error -Wno-undef'

export CFLAGS="$FLAGS"
export CXXFLAGS="$FLAGS"
export LDFLAGS="$LDFLAGS -stdlib=libc++ -L%_libdir -lc++ -lc++abi"

# Debian:
# enable_vr=false

gn_arg=()
gn_arg+=( target_cpu=\"%cef_arch\" )
gn_arg+=( custom_toolchain=\"//build/toolchain/linux/unbundle:default\" )
gn_arg+=( host_toolchain=\"//build/toolchain/linux/unbundle:default\" )
gn_arg+=( is_official_build=true )
gn_arg+=( use_custom_libcxx=false )
# System libc++ must not free CEF-private GWP-ASan malloc allocations.
gn_arg+=( enable_gwp_asan_malloc=false )
gn_arg+=( use_sysroot=false )
gn_arg+=( use_gio=true )
gn_arg+=( use_glib=true )
gn_arg+=( use_libpci=true )
gn_arg+=( use_pulseaudio=true )
gn_arg+=( use_cups=true )
gn_arg+=( use_kerberos=true )
gn_arg+=( use_vaapi=true )
gn_arg+=( use_system_freetype=true )
gn_arg+=( use_system_harfbuzz=true )
gn_arg+=( use_system_lcms2=true )
gn_arg+=( use_system_libffi=true )
gn_arg+=( use_system_libjpeg=true )
gn_arg+=( use_system_libopenjpeg2=true )
gn_arg+=( use_libjpeg_turbo=true )
gn_arg+=( use_system_libpng=true )
gn_arg+=( use_system_minigbm=true )
gn_arg+=( use_system_zlib=true )
gn_arg+=( use_bundled_weston=false )
gn_arg+=( use_xkbcommon=true )
gn_arg+=( use_icf=false )
gn_arg+=( enable_linux_installer=false )
gn_arg+=( optimize_webui=false )
gn_arg+=( link_pulseaudio=true )
gn_arg+=( enable_hangout_services_extension=true )
gn_arg+=( treat_warnings_as_errors=false )
gn_arg+=( clang_warning_suppression_file=\"\" )
gn_arg+=( fatal_linker_warnings=false )
gn_arg+=( system_libdir=\"%_lib\" )
gn_arg+=( enable_nocompile_tests=false )

gn_arg+=( v8_use_metagen_instance_types=false )

# toolkit
gn_arg+=( use_qt5=false )
gn_arg+=( use_qt6=false )
gn_arg+=( use_gtk=true )
gn_arg+=( gtk_version=4 )

# ozone
gn_arg+=( use_ozone=true )
gn_arg+=( ozone_platform=\"x11\" )
gn_arg+=( ozone_platform_x11=true )
gn_arg+=( ozone_platform_wayland=true )
gn_arg+=( angle_has_histograms=false )
gn_arg+=( angle_build_tests=false )
gn_arg+=( build_angle_perftests=false )

# ffmpeg
gn_arg+=( ffmpeg_branding=\"Chrome\" )
gn_arg+=( proprietary_codecs=true )

# Remove debug
gn_arg+=( is_debug=false )
gn_arg+=( enable_iterator_debugging=false )
gn_arg+=( dcheck_always_on=false )
gn_arg+=( dcheck_is_configurable=false )
gn_arg+=( symbol_level=0 )
gn_arg+=( blink_symbol_level=0 )
gn_arg+=( v8_symbol_level=0 )
gn_arg+=( v8_enable_backtrace=true )
gn_arg+=( disable_fieldtrial_testing_config=true )

gn_arg+=( enable_enterprise_companion=false )
gn_arg+=( is_component_ffmpeg=false )
gn_arg+=( is_component_build=false )
gn_arg+=( enable_widevine=true )

gn_arg+=( rtc_use_pipewire=true )
gn_arg+=( rtc_link_pipewire=true )

gn_arg+=( clang_base_path=\"$LLVM_PREFIX\" )
gn_arg+=( is_clang=true )
gn_arg+=( clang_use_chrome_plugins=false )
gn_arg+=( use_lld=true )
gn_arg+=( use_thin_lto=true )
gn_arg+=( thin_lto_enable_optimizations=true )
gn_arg+=( is_cfi=false )
gn_arg+=( use_cfi_icall=false )
gn_arg+=( chrome_pgo_phase=0 )

# use system rust
export RUSTC_BOOTSTRAP=1
gn_arg+=( rust_sysroot_absolute=\"$(rustc --print sysroot)\" )
rust_version=$(rustc --version 2>/dev/null | awk -v OFS='-' '{print $1,$2}')
gn_arg+=( rustc_version=\"$rust_version\" )

gn_arg+=( icu_use_data_file=true )

gn_arg+=( angle_enable_vulkan=true )
gn_arg+=( angle_use_custom_libvulkan=false )
gn_arg+=( dawn_enable_vulkan_loader=false )
gn_arg+=( enable_vulkan=true )
gn_arg+=( use_system_libtiff=false )
gn_arg+=( safe_browsing_use_unrar=false )
gn_arg+=( build_dawn_tests=false )
gn_arg+=( webnn_use_tflite=false )
gn_arg+=( webnn_use_litert=false )
gn_arg+=( enable_perfetto_unittests=false )
gn_arg+=( skia_enable_skshaper_tests=false )
gn_arg+=( tint_build_unittests=false )
gn_arg+=( enable_screen_ai_browsertests=false )

gn_arg+=( google_api_key=\"%api_key\" )

# Clang path
gn_arg+=( clang_base_path=\"/usr/lib/llvm-%llvm_version\" )

# Remove bundled libraries for which we will use the system copies.
.rpm/scripts/unbundle
# Sisyphus provides the required libdrm and OpenH264 interfaces.
%__python3 build/linux/unbundle/replace_gn_files.py \
    --system-libraries libdrm openh264

# Bootstrap GN, then generate the CEF configuration.
%__python3 cef/tools/version_manager.py -u
%__python3 tools/gn/bootstrap/bootstrap.py \
    --gn-gen-args="${gn_arg[*]} enable_cef=false" --build-path=%target
cef_gn_arg=("${gn_arg[@]/optimize_webui=false/optimize_webui=true}")
export GN_DEFINES="${cef_gn_arg[*]}"
export GN_OUT_CONFIGS=Release_GN_%cef_arch
export GN_ARGUMENTS="--script-executable=%__python3"
export PATH="$PWD/%target:$PATH"
%__python3 cef/tools/gclient_hook.py
%__python3 cef/tools/version_manager.py -c

n=%build_parallel_jobs
[ "$n" -lt %max_jobs ] || n=%max_jobs
%__python3 %SOURCE502 %cef_target cef chrome_sandbox
ninja -j "$n" -C %cef_target cef chrome_sandbox

# Upstream release-only SDK export retains all headers and wrapper sources.
%__python3 cef/tools/make_distrib.py --output-dir="$PWD" --distrib-subdir=cef \
    --minimal --ninja-build --%cef_arch-build --no-archive --no-docs --no-symbols

%install
mkdir -p %buildroot%cef_libdir %buildroot%cef_sdkdir
cp -a cef_minimal/Release/. %buildroot%cef_libdir/
cp -a cef_minimal/Resources/. %buildroot%cef_libdir/
ln -s cef%abiversion/libcef.so.%abiversion \
    %buildroot%_libdir/libcef.so.%abiversion
ln -s libcef.so.%abiversion %buildroot%_libdir/libcef.so

for entry in include libcef_dll cmake bazel CMakeLists.txt BUILD.bazel \
        MODULE.bazel WORKSPACE .bazelrc .bazelversion; do
    cp -a cef_minimal/"$entry" %buildroot%cef_sdkdir/
done
rm %buildroot%cef_sdkdir/include/base/internal/README-TRANSFER.txt \
    %buildroot%cef_sdkdir/bazel/linux/pkg_config/README.cef
ln -s ../../%_lib/cef%abiversion %buildroot%cef_sdkdir/Release
ln -s ../../%_lib/cef%abiversion %buildroot%cef_sdkdir/Resources

%check
%__python3 -m unittest discover -s tools/typescript -p validate_tsconfig_test.py
# The upstream tools guidelines require two runs to detect parser-state leaks.
pushd cef
%__python3 -m unittest discover -s tools -p '*_test.py'
%__python3 -m unittest discover -s tools -p '*_test.py'
popd
%cef_target/libcef_static_unittests
# Check the first external frame in a fresh browser process.
dbus-run-session -- %__python3 testing/xvfb.py %cef_target/ceftests \
    --use-xvfb --no-sandbox --use-views \
    --gtest_filter='OSRTest.SingleFramePaint:OSRTest.SingleFramePaint2x'
# Chromium supplies the window manager/compositor and a real resolver fixture.
# Keep the ResolveHost API tests independent of external DNS availability.
dbus-run-session -- %__python3 testing/xvfb.py %cef_target/ceftests \
    --use-xvfb --no-sandbox --use-views \
    --host-resolver-rules='MAP www.google.com 127.0.0.1'
dbus-run-session -- %__python3 testing/xvfb.py %cef_target/ceftests \
    --use-xvfb --no-sandbox --use-views --use-alloy-style \
    --host-resolver-rules='MAP www.google.com 127.0.0.1'

%files -n libcef%abiversion
%doc LICENSE cef_minimal/LICENSE.txt cef_minimal/CREDITS.html
%_libdir/libcef.so.%abiversion
%dir %cef_libdir
%cef_libdir/libcef.so.%abiversion
%attr(4711,root,root) %cef_libdir/chrome-sandbox
%cef_libdir/libvk_swiftshader.so
%cef_libdir/vk_swiftshader_icd.json
%cef_libdir/v8_context_snapshot.bin
%cef_libdir/chrome_100_percent.pak
%cef_libdir/chrome_200_percent.pak
%cef_libdir/resources.pak
%cef_libdir/icudtl.dat
%cef_libdir/locales

%files -n libcef-devel
%_libdir/libcef.so
%cef_sdkdir

%changelog
* Sat Nov 07 2026 Ivan Khanas <xeno@altlinux.org> 156.0.15-alt1
- Initial build for ALT.
