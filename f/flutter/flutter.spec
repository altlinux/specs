%define _unpackaged_files_terminate_build 1

%define dart_version 3.13.7
%define llvm_version 22.1

Name: flutter
Version: 3.47.9
Release: alt2

Summary: Flutter framework
License: BSD-3-Clause
Group: Development/Other

URL: https://github.com/flutter/flutter.git
VCS: https://flutter.dev

# Original spec and patches — https://gitlab.alpinelinux.org/alpine/aports/-/tree/master/testing/flutter

Source0: %name-%version.tar.zst
Source1: submodules-%version.tar.zst
Source2: dart-vendor-%version.tar.zst
Source3: flutter-wrapper.sh
# https://storage.googleapis.com/flutter_infra_release/flutter/fonts/3012db47f3130e62f7cc0beabff968a33cbec8d8/fonts.zip
Source4: fonts.zip
# https://storage.googleapis.com/flutter_infra_release/gradle-wrapper/fd5c1f2c013565a3bea56ada6df9d2b8e96d56aa/gradle-wrapper.tgz
Source5: gradle-wrapper.tgz

Patch1: content-unaware-hash.patch
Patch2: doctor.patch
Patch3: git-revision.patch
Patch4: no-cache.patch
Patch5: no-vpython.patch
Patch6: not-in-git.patch
Patch7: pmos-if-touch-is-a-mouse-then-mouse-is-touch.patch
Patch8: shared-libcxx.patch
Patch9: system-dart.patch
Patch10: system-icu.patch
Patch11: target-musl.patch
Patch12: unbundle-engine.patch
Patch13: unbundle-icu.patch
Patch14: unbundle.patch
Patch15: version.patch

Patch16: unbundle-icu.patch.dart
Patch17: no-gn-check.patch
Patch18: impeller-public-generated-deps.patch
Patch19: no-werror.patch
Patch20: fml-climits.patch

BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: rpm-build-python3
BuildRequires: dart-lang-sdk = %dart_version
BuildRequires: /proc
BuildRequires: gn
BuildRequires: git
BuildRequires: unzip
BuildRequires: ninja-build
BuildRequires: clang%llvm_version
BuildRequires: llvm%llvm_version
BuildRequires: libstdc++-devel
BuildRequires: pkgconfig(SPIRV-Tools)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(zlib)

ExclusiveArch: x86_64 aarch64

%global flutter_root %_libexecdir/%name
%global engine_cache %flutter_root/bin/cache/artifacts/engine

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

%add_findprov_skiplist %flutter_root/packages/flutter_tools/.pub_cache/* %flutter_root/pub_cache/*
%add_findreq_skiplist  %flutter_root/packages/flutter_tools/.pub_cache/* %flutter_root/pub_cache/*

%description
%summary.

%package common
Summary: Flutter common parts
Group: Development/Other

Requires: clang%llvm_version
Requires: cmake
Requires: dart-lang-sdk = %dart_version
Requires: git
Requires: pkgconf
Requires: pkgconfig(gtk+-3.0)

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
%setup -a1 -a2
%autopatch -p1

echo -n "%version" > version
mkdir bin/cache

export devtools_version="$(grep 'devtools_rev' engine/src/flutter/third_party/dart/DEPS | head -n1 | awk -F\" '{ print $4 }')"
engine_version="$(cat bin/internal/engine.version)"
echo -n "$engine_version" > bin/cache/engine.stamp
echo -n "$engine_version" > bin/cache/engine_stamp.stamp
cat > bin/cache/engine_stamp.json <<EOF
{
	"build_time_ms": 0,
	"git_revision": "$engine_version",
	"git_revision_date": "2038-01-19T03:14:08.000Z",
	"content_hash": "0000000000000000000000000000000000000000"
}
EOF
cat > bin/cache/flutter.version.json <<EOF
{
	"frameworkVersion": "%version",
	"channel": "stable",
	"repositoryUrl": "https://github.com/flutter/flutter.git",
	"frameworkRevision": "sisyphus00000000000000000000000000000000",
	"frameworkCommitDate": "2038-01-19 03:14:08",
	"engineRevision": "$engine_version",
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
# Try to avoid aarch64 build "Too many open files" error
ulimit -Sn $(ulimit -Hn)

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

# Fix build fail: redefinitions
sed -i 's|G_DEFINE_AUTOPTR_CLEANUP_FUNC(PangoContext, g_object_unref)||' flutter/shell/platform/linux/fl_accessible_text_field.cc

for mode in %modes; do
  python3 ./flutter/tools/gn \
    --no-goma \
    --no-dart-version-git-info \
    --linux \
    --linux-cpu=%flutter_arch \
    --lto \
    --clang \
    --no-stripped \
    --no-prebuilt-dart-sdk \
    --build-glfw-shell \
    --build-engine-artifacts \
    --no-enable-unittests \
    --enable-fontconfig \
    --runtime-mode="$mode" \
    --gn-args="
      angle_build_tests=false
      angle_enable_libdrm=false
      angle_use_wayland=false
      dart_embed_icu_data=false
      host_libc=\"gnu\"
      target_libc=\"gnu\"
      treat_warnings_as_errors=false
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

sed -i 's|\(%_builddir/%name-%version/%flutter_root/pub_cache\)/packages/flutter_tools/.pub_cache|\1|' packages/flutter_tools/.dart_tool/package_config.json

%install
install -Dm755 %SOURCE3 %buildroot%flutter_root/bin/flutter
mkdir -p %buildroot%_bindir
ln -s ../lib/%name/bin/flutter %buildroot%_bindir/%name

install -Dm644 bin/cache/flutter.version.json bin/cache/engine.stamp bin/cache/engine_stamp.stamp bin/cache/engine_stamp.json -t %buildroot%flutter_root/bin/cache/
ln -s ../../../dart %buildroot%flutter_root/bin/cache/dart-sdk

install -Dm755 bin/cache/flutter_tools.snapshot %buildroot%flutter_root/bin/cache/flutter_tools.snapshot

mkdir -p %buildroot%engine_cache/common
cp -r %release_out/flutter_patched_sdk/ %buildroot%engine_cache/common/flutter_patched_sdk_product
cp -r %debug_out/flutter_patched_sdk/   %buildroot%engine_cache/common/flutter_patched_sdk

mkdir -p %buildroot%flutter_root/bin/cache/pkg
cp -rL %release_out/gen/dart-pkg/sky_engine %buildroot%flutter_root/bin/cache/pkg/sky_engine

cp -r packages %buildroot%flutter_root/packages
mkdir -p %buildroot%flutter_root/dev %buildroot%flutter_root/examples
touch %buildroot%flutter_root/dev/.intentionally-empty %buildroot%flutter_root/examples/.intentionally-empty

mkdir -p %buildroot%flutter_root/pub_cache
cp -r packages/flutter_tools/.pub_cache/* %buildroot%flutter_root/pub_cache

echo -n %version > %buildroot%flutter_root/version
mkdir -p %buildroot%flutter_root/bin/internal/
cp bin/internal/engine.version %buildroot%flutter_root/bin/internal/engine.version

mkdir -p %buildroot%flutter_root/bin/cache/artifacts/material_fonts
unzip %SOURCE4 -d %buildroot%flutter_root/bin/cache/artifacts/material_fonts

mkdir -p %buildroot%flutter_root/bin/cache/artifacts/gradle_wrapper
tar xf %SOURCE5 -C %buildroot%flutter_root/bin/cache/artifacts/gradle_wrapper

for mode in %modes; do
  case $mode in
    debug) mode_art_name=linux-%flutter_arch ;;
    *) mode_art_name=linux-%flutter_arch-$mode ;;
  esac
  mkdir -p %buildroot%engine_cache/$mode_art_name/
  unzip %out/linux_${mode}_%flutter_arch/zip_archives/$mode_art_name/artifacts.zip -d %buildroot%engine_cache/$mode_art_name/
done

cp -r %release_out/flutter_linux/ %buildroot%engine_cache/linux-%flutter_arch/flutter_linux
ln -s ../linux-%flutter_arch/flutter_linux %buildroot%engine_cache/linux-%flutter_arch-profile/flutter_linux
ln -s ../linux-%flutter_arch/flutter_linux %buildroot%engine_cache/linux-%flutter_arch-release/flutter_linux
mkdir -p %buildroot/usr/include/
ln -s ../lib/flutter/bin/cache/artifacts/engine/linux-%flutter_arch/flutter_linux %buildroot/usr/include/flutter_linux

install -Dm755 %release_out/libflutter_linux_gtk.so %buildroot%_libexecdir/libflutter_linux_gtk.so

cp engine/src/flutter/third_party/icu/flutter/icudtl.dat %buildroot%flutter_root/icudtl.dat

install -Dm755 %release_out/libflutter_linux_glfw.so %buildroot%_libexecdir/libflutter_linux_glfw.so

%files common
%engine_cache/common
%flutter_root/bin/cache/artifacts/material_fonts
%flutter_root/bin/cache/dart-sdk
%flutter_root/bin/cache/pkg
%flutter_root/bin/internal
%flutter_root/packages
%flutter_root/pub_cache

%files desktop
%_includedir/flutter_linux
%engine_cache/linux-%flutter_arch
%engine_cache/linux-%flutter_arch-release

%files developer
%engine_cache/linux-%flutter_arch-profile

%files gtk
%_libexecdir/libflutter_linux_gtk.so
%_libexecdir/flutter/icudtl.dat

%files glfw
%_libexecdir/libflutter_linux_glfw.so

%files tool
%_bindir/%name
%flutter_root/bin/cache/flutter_tools.snapshot
%flutter_root/bin/cache/flutter.version.json
%flutter_root/bin/cache/engine.stamp
%flutter_root/bin/cache/engine_stamp.stamp
%flutter_root/bin/cache/engine_stamp.json
%flutter_root/bin/cache/artifacts/gradle_wrapper
%flutter_root/bin/flutter
%flutter_root/version

%files tool-developer
%flutter_root/dev
%flutter_root/examples

%changelog
* Fri Nov 20 2026 David Sultaniiazov <x1z53@altlinux.org> 3.47.9-alt2
- Use user-wide SDK cache.

* Thu Nov 19 2026 David Sultaniiazov <x1z53@altlinux.org> 3.47.9-alt1
- 3.47.9 (via rebase).
- Drop unnecessary patches and adopt other patches.
- Fix GN dependency checks and build with GCC 16.
- Read engine revision from the upstream file.
- Build with system libpci.
- Add the engine stamps.
- Enable aarch64 build.
- Simplify the spec.

* Tue Nov 17 2026 David Sultaniiazov <x1z53@altlinux.org> 3.44.9-alt1
- 3.44.9 (via rebase).
- Update submodules and Dart vendor scripts.
- Adapt patches.
- Remove musl depending.
- Add internal symlink to system Dart.

* Fri Aug 28 2026 David Sultaniiazov <x1z53@altlinux.org> 3.41.9-alt1
- 3.41.9.
- Rebuild with Git history.
- Update plan.
- Remove update script.
- Update spec:
  + move patches to `.gear/patches`;
  + use `tar.zst` instead of `tar` in `rules`.

* Thu Nov 27 2025 David Sultaniiazov <x1z53@altlinux.org> 3.38.2-alt1
- Initial build.
