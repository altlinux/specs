%define _unpackaged_files_terminate_build 1

%define flutter_channel stable
%define dart_version 3.10.1
%define llvm_version 21.1

Name: flutter
Version: 3.38.2
Release: alt1

Summary: Flutter framework
License: BSD-3-Clause
Group: Development/Other

URL: https://github.com/flutter/flutter.git
VCS: https://github.com/flutter/flutter.git

# Original spec and patches — https://gitlab.alpinelinux.org/alpine/aports/-/tree/master/testing/flutter

# From Alpine
%define engine_version c29809135135e262a912cf583b2c90deb9ded610
%define material_fonts_version 3012db47f3130e62f7cc0beabff968a33cbec8d8
%define gradle_wrapper_version fd5c1f2c013565a3bea56ada6df9d2b8e96d56aa

Source0: %name-%version.tar.zst
Source1: %name-%version-vendor.tar
Source2: flutter
# https://storage.googleapis.com/flutter_infra_release/flutter/fonts/%material_fonts_version/fonts.zip
Source3: fonts.zip
# https://storage.googleapis.com/flutter_infra_release/gradle-wrapper/%gradle_wrapper_version/gradle-wrapper.tgz
Source4: gradle-wrapper.tgz

Patch0: alpine-target.patch
Patch1: content-unaware-hash.patch
Patch2: doctor.patch
Patch3: git-revision.patch
Patch4: libstdc++13.patch
Patch5: musl-no-execinfo.patch
Patch6: musl-no-mallinfo.patch
Patch7: no-cache.patch
Patch8: no-vpython.patch
Patch9: not-in-git.patch
Patch10: opt-in-analytics.patch
Patch11: pmos-if-touch-is-a-mouse-then-mouse-is-touch.patch
Patch12: shared-libcxx.patch
Patch13: system-dart.patch
Patch14: system-icu.patch
Patch15: target-musl.patch
Patch16: unbundle-engine.patch
Patch17: unbundle-icu.patch
Patch18: unbundle.patch
Patch19: version.patch

Patch20: unbundle-icu.patch.dart

BuildRequires(pre): rpm-macros-musl
BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: rpm-build-python3
BuildRequires: dart-lang-sdk = %dart_version
BuildRequires: gn
BuildRequires: musl-devel
BuildRequires: /proc

# From Alpine
BuildRequires: clang%llvm_version
BuildRequires: llvm%llvm_version
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: samurai
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(SPIRV-Tools)
BuildRequires: libicu-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libsqlite3-devel
BuildRequires: zlib-devel
BuildRequires: ninja-build

# Maybe not needed
BuildRequires: bash
BuildRequires: pkgconf
BuildRequires: git
BuildRequires: zstd

# Failed when build
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: unzip

#ExclusiveArch: x86_64 aarch64
ExclusiveArch: x86_64

%ifarch x86_64
%define flutter_arch x64
%endif
%ifarch aarch64
%define flutter_arch arm64
%endif

%define out %_builddir/%name-%version/engine/src/out
%define modes release profile debug
%define release_out %out/linux_release_%flutter_arch
%define debug_out %out/linux_debug_%flutter_arch

%add_findprov_skiplist %_libexecdir/%name/packages/flutter_tools/.pub_cache/* %_libexecdir/%name/pub_cache/*
%add_findreq_skiplist  %_libexecdir/%name/packages/flutter_tools/.pub_cache/* %_libexecdir/%name/pub_cache/*

%description
%summary.

%package common
Summary: Flutter common parts
Group: Development/Other

Requires: bash
Requires: clang%llvm_version
Requires: cmake
Requires: dart-lang-sdk = %dart_version
Requires: git
Requires: pkgconfig(gtk+-3.0)
Requires: pkgconf
Requires: samurai

%description common
%summary.

%package desktop
Summary: Flutter release linux desktop target
Group: Development/Other

Requires: flutter-common = %EVR
Requires: flutter-glfw = %EVR
Requires: flutter-gtk = %EVR
Requires: flutter-tool = %EVR

%description desktop
%summary.

%package developer
Summary: Flutter app developer tools
Group: Development/Other

Requires: flutter-desktop = %EVR
Requires: flutter-tool-developer = %EVR

%description developer
%summary.

%package gtk
Summary: Flutter GTK embedder runtime
Group: Development/Other

%description gtk
%summary.

%package glfw
Summary: Flutter GLFW embedder runtime
Group: Development/Other

%description glfw
%summary.

%package tool
Summary: Flutter CLI tool
Group: Development/Other

Requires: flutter-common = %EVR

%description tool
%summary.

NOTE:

This tool cannot work with `debug` and `profile` modes.
Use `flutter run --release` for run.

If you know how to fix it, please open a Bugzilla report.

%package tool-developer
Summary: Flutter CLI tool, parts for app developers
Group: Development/Other

Requires: flutter-tool = %EVR

%description tool-developer
%summary.

%prep
%setup -a1
%autopatch -p1

echo -n "%version" > version
mkdir bin/cache

export devtools_version="$(grep 'devtools_rev' engine/src/flutter/third_party/dart/DEPS | head -n1 | awk -F\" '{ print $4 }')"
cat > bin/cache/flutter.version.json <<EOF
{
	"frameworkVersion": "%version",
	"channel": "%flutter_channel",
	"repositoryUrl": "https://github.com/flutter/flutter.git",
	"frameworkRevision": "sisyphus00000000000000000000000000000000",
	"frameworkCommitDate": "2038-01-19 03:14:08",
	"engineRevision": "%engine_version",
	"dartSdkVersion": "%dart_version",
	"devToolsVersion": "$devtools_version",
	"flutterVersion": "%version"
}
EOF

cd engine/src

mkdir -p flutter/third_party/dart/tools/sdks/dart-sdk/
ln -sv %_libexecdir/dart/bin flutter/third_party/dart/tools/sdks/dart-sdk/bin
mkdir -p flutter/prebuilts/linux-%flutter_arch/dart-sdk
ln -sv %_libexecdir/dart/bin flutter/prebuilts/linux-%flutter_arch/dart-sdk/bin

mkdir -p flutter/third_party/gn/
ln -sv %_bindir/gn flutter/third_party/gn/gn

mkdir -p flutter/third_party/dart/.git/logs
touch flutter/third_party/dart/.git/logs/HEAD

python3 flutter/third_party/dart/tools/generate_package_config.py
python3 flutter/third_party/dart/tools/generate_sdk_version_file.py
python3 flutter/tools/pub_get_offline.py

%define use_system freetype2 harfbuzz libjpeg-turbo libpng libwebp sqlite zlib
for _lib in %use_system; do
  find . -type f -path "*third_party/$_lib/*" \
    \! -path "*third_party/$_lib/chromium/*" \
    \! -path "*third_party/$_lib/google/*" \
    \! -regex '.*\.\(gn\|gni\|isolate\|py\)' \
    -delete
done

python3 build/linux/unbundle/replace_gn_files.py --system-libraries \
  %use_system icu

cd -

cd packages/flutter_tools/

export PUB_CACHE="${PWD}/.pub_cache"
dart pub get --offline

cd -

%build
cd engine/src

export CFLAGS="${CFLAGS/-g/} -O2 -Wno-error -Wno-absolute-value -Wno-implicit-float-conversion"
export CXXFLAGS="${CXXFLAGS/-g/} -O2 -Wno-error -Wno-absolute-value -Wno-implicit-float-conversion"
export PATH="%llvm_bindir:$PATH"

# Fix build fail: comment unused variables
sed -i "s|mnemonic = \".*\"|#\0|" flutter/impeller/tools/*

# Fix build fail: hpp11 to hpp, because hpp11 is "not supported format"
sed -i "s|hpp11|hpp|" flutter/third_party/vulkan-deps/glslang/src/BUILD.gn
ln -sf flutter/third_party/vulkan-deps/glslang/src/SPIRV/spirv.hpp11 flutter/third_party/vulkan-deps/glslang/src/SPIRV/spirv.hpp

# Fix build fail: undeclared memset
sed -i '1s|^|#include <cstring>\n|' flutter/fml/logging.h

for mode in %modes; do
  python3 ./flutter/tools/gn \
    --no-goma \
    --no-dart-version-git-info \
    --linux \
    --linux-cpu=%flutter_arch \
    --lto \
    --clang \
    --no-backtrace \
    --no-stripped \
    --no-prebuilt-dart-sdk \
    --build-glfw-shell \
    --build-engine-artifacts \
    --no-enable-unittests \
    --enable-fontconfig \
    --runtime-mode="$mode" \
    --gn-args="
      dart_embed_icu_data=false
      host_libc=\"musl\"
      target_libc=\"musl\"
      use_ccache=false
      use_custom_libcxx=false
      use_default_linux_sysroot=false
    "

  ninja -j%__nprocs -C "%out"/linux_${mode}_%flutter_arch artifacts
done

ninja -j%__nprocs -C "%release_out" flutter flutter_patched_sdk sky
ninja -j%__nprocs -C "%debug_out" flutter flutter_patched_sdk sky

cd -

dart --verbosity=error \
     --snapshot="bin/cache/flutter_tools.snapshot" --snapshot-kind="app-jit" \
     --packages="packages/flutter_tools/.dart_tool/package_config.json" \
     --no-enable-mirrors "packages/flutter_tools/bin/flutter_tools.dart"

sed -i 's|\(%_builddir/%name-%version/%_libexecdir/%name/pub_cache\)/packages/flutter_tools/.pub_cache|\1|' packages/flutter_tools/.dart_tool/package_config.json

%install
install -Dm755 %SOURCE2 %buildroot%_libexecdir/%name/bin/flutter
mkdir -p %buildroot%_bindir
ln -s ../lib/%name/bin/flutter %buildroot%_bindir/%name

install -Dm644 %_builddir/%name-%version/bin/cache/flutter.version.json -t %buildroot%_libexecdir/%name/bin/cache/

install -Dm755 %_builddir/%name-%version/bin/cache/flutter_tools.snapshot %buildroot%_libexecdir/%name/bin/cache/flutter_tools.snapshot

mkdir -p %buildroot%_libexecdir/%name/bin/cache/artifacts/engine/common
cp -r %release_out/flutter_patched_sdk/ %buildroot%_libexecdir/%name/bin/cache/artifacts/engine/common/flutter_patched_sdk_product
cp -r %debug_out/flutter_patched_sdk/   %buildroot%_libexecdir/%name/bin/cache/artifacts/engine/common/flutter_patched_sdk

mkdir -p %buildroot%_libexecdir/%name/bin/cache/pkg
cp -rL %release_out/gen/dart-pkg/sky_engine %buildroot%_libexecdir/%name/bin/cache/pkg/sky_engine

cp -r %_builddir/%name-%version/packages %buildroot%_libexecdir/%name/packages
mkdir -p %buildroot%_libexecdir/%name/dev %buildroot%_libexecdir/%name/examples
touch %buildroot%_libexecdir/%name/dev/.intentionally-empty %buildroot%_libexecdir/%name/examples/.intentionally-empty

mkdir -p %buildroot%_libexecdir/%name/pub_cache
cp -r %_builddir/%name-%version/packages/flutter_tools/.pub_cache/* %buildroot%_libexecdir/%name/pub_cache

echo -n %version > %buildroot%_libexecdir/%name/version
mkdir -p %buildroot%_libexecdir/%name/bin/internal/
echo -n %engine_version > %buildroot%_libexecdir/%name/bin/internal/engine.version

mkdir -p %buildroot%_libexecdir/%name/bin/cache/artifacts/material_fonts
unzip %SOURCE3 -d %buildroot%_libexecdir/%name/bin/cache/artifacts/material_fonts

mkdir -p %buildroot%_libexecdir/%name/bin/cache/artifacts/gradle_wrapper
tar xf %SOURCE4 -C %buildroot%_libexecdir/%name/bin/cache/artifacts/gradle_wrapper

for mode in %modes; do
  case $mode in
    debug) mode_art_name=linux-%flutter_arch ;;
    *) mode_art_name=linux-%flutter_arch-$mode ;;
  esac
  mkdir -p %buildroot%_libexecdir/%name/bin/cache/artifacts/engine/$mode_art_name/
  unzip %out/linux_${mode}_%flutter_arch/zip_archives/$mode_art_name/artifacts.zip -d %buildroot%_libexecdir/%name/bin/cache/artifacts/engine/$mode_art_name/
done

cp -r %release_out/flutter_linux/ %buildroot%_libexecdir/%name/bin/cache/artifacts/engine/linux-%flutter_arch/flutter_linux
ln -s ../linux-%flutter_arch/flutter_linux %buildroot%_libexecdir/%name/bin/cache/artifacts/engine/linux-%flutter_arch-profile/flutter_linux
ln -s ../linux-%flutter_arch/flutter_linux %buildroot%_libexecdir/%name/bin/cache/artifacts/engine/linux-%flutter_arch-release/flutter_linux
mkdir -p %buildroot/usr/include/
ln -s ../lib/flutter/bin/cache/artifacts/engine/linux-%flutter_arch/flutter_linux %buildroot/usr/include/flutter_linux

install -Dm755 %release_out/libflutter_linux_gtk.so %buildroot%_libexecdir/libflutter_linux_gtk.so

cp %_builddir/%name-%version/engine/src/flutter/third_party/icu/flutter/icudtl.dat %buildroot%_libexecdir/%name/icudtl.dat

install -Dm755 %release_out/libflutter_linux_glfw.so %buildroot%_libexecdir/libflutter_linux_glfw.so

%files common
%_libexecdir/%name/bin/cache/artifacts/engine/common
%_libexecdir/%name/bin/cache/artifacts/material_fonts
%_libexecdir/%name/bin/cache/pkg
%_libexecdir/%name/bin/internal
%_libexecdir/%name/packages
%_libexecdir/%name/pub_cache

%files desktop
%_includedir/flutter_linux
%_libexecdir/%name/bin/cache/artifacts/engine/linux-%flutter_arch
%_libexecdir/%name/bin/cache/artifacts/engine/linux-%flutter_arch-release

%files developer
%_libexecdir/%name/bin/cache/artifacts/engine/linux-%flutter_arch-profile
%_libexecdir/%name/bin/cache/artifacts/gradle_wrapper

%files gtk
%_libexecdir/libflutter_linux_gtk.so
%_libexecdir/flutter/icudtl.dat

%files glfw
%_libexecdir/libflutter_linux_glfw.so

%files tool
%_bindir/%name
%_libexecdir/%name/bin/cache/flutter_tools.snapshot
%_libexecdir/%name/bin/cache/flutter.version.json
%_libexecdir/%name/bin/flutter
%_libexecdir/%name/version

%files tool-developer
%_libexecdir/%name/dev
%_libexecdir/%name/examples

%changelog
* Thu Nov 27 2025 David Sultaniiazov <x1z53@altlinux.org> 3.38.2-alt1
- Initial build.
