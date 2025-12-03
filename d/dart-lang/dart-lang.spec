%define _unpackaged_files_terminate_build 1

Name: dart-lang
Version: 3.9.2
Release: alt1

Summary: Dart language
License: BSD-3-Clause
Group: Development/Other

Source0: %name-%version.tar
Source1: dart-wrapper.sh
Patch0: build-config.patch
Patch1: gcc13.patch
Patch2: no-werror.patch
Patch3: unbundle.patch
Patch4: unbundle-icu.patch
Patch5: where-we-are-heading-prefixes-are-not-needed.patch
Patch6: zlib-not-found.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gn
BuildRequires: git
BuildRequires: lld
BuildRequires: gcc-c++
BuildRequires: ripgrep
BuildRequires: samurai
BuildRequires: python3
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: dart-lang

ExclusiveArch: x86_64 aarch64

%ifarch x86_64
%define dart_arch x64
%define dart_out ReleaseX64
%endif
%ifarch aarch64
%define dart_arch arm64
%define dart_out ReleaseARM64
%endif

%description
%summary.

%package -n dartaotruntime
Summary: dartaotruntime
Group: Development/Tools

%description -n dartaotruntime
%summary.

%package sdk
Summary: Dart lang SDK
Group: Development/Tools

Provides: dart-lang-bootstrap

Requires: dart-lang dartaotruntime

%description sdk
%summary.

%prep
%setup
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1
%patch4 -p 1
%patch5 -p 1
%patch6 -p 1

# SOURCE
#
# Requires: teapot-tools pax-utils
#
# mkdir snapshot
# cd snapshot
#
# echo "
# solutions = [{
#   'name': 'sdk',
#   'url': 'https://dart.googlesource.com/sdk.git@3.9.2',
# }]
# target_cpu = ['x64', 'arm64']
# target_cpu_only = True
# " > .gclient
#
# gclient sync --no-history --nohooks --tpot-cipd-ignore-platformed
#
# for elf in $(scanelf -RA -F "%F" sdk); do
#   rm -f "$elf"
# done
#
# tar -cf dart-lang-3.9.2.tar \
#   --exclude="ChangeLog*" \
#   --exclude="sdk/buildtools/*/clang" \
#   --exclude="third_party/fuchsia/sdk/linux/arch" \
#   --exclude=".build-id" \
#   --exclude-backups \
#   --exclude-caches-all \
#   --exclude-vcs \
#   sdk

mkdir -p .git/logs
echo '' > .git/logs/HEAD

rm -rf tools/sdks/dart-sdk
ln -s %_libexecdir/dart tools/sdks/dart-sdk

ln -s %_bindir/gn buildtools/gn
mkdir -p buildtools/ninja
ln -s %_bindir/samu buildtools/ninja/ninja

# gclient hooks
python3 tools/generate_package_config.py
python3 tools/generate_sdk_version_file.py

# google analytics, doubleclick
echo '' > tools/bots/dartdoc_footer.html
rm third_party/devtools/web/devtools_analytics.js

# disarm analytics for sure
rg --no-ignore -l 'google-analytics\.com' . \
  | rg -v "\.map\$" \
  | xargs -t -n 1 -P ${JOBS:-2} sed -i -E 's|([^/]+\.)?google-analytics\.com|0\.0\.0\.0|g'
rg --no-ignore -l 'UA-[0-9]+-[0-9]+' . \
  | xargs -t -n 1 -P ${JOBS:-2} sed -i -E 's|UA-[0-9]+-[0-9]+|UA-2137-0|g'

# reusable system library settings
for _lib in icu zlib; do
  find . -type f -path "*third_party/$_lib/*" \
    \! -path "*third_party/$_lib/chromium/*" \
    \! -path "*third_party/$_lib/google/*" \
    \! -regex '.*\.\(gn\|gni\|isolate\|py\)' \
    -delete
done

python3 build/linux/unbundle/replace_gn_files.py --system-libraries icu zlib

%build
python3 ./tools/build.py \
  --no-clang \
  --arch="%dart_arch" \
  --mode=release \
  --no-verify-sdk-hash \
  --gn-args='dart_embed_icu_data=false dart_snapshot_kind="app-jit" dart_sysroot=""' \
  create_sdk runtime

%install
mkdir -p %buildroot%_bindir %buildroot%_libexecdir %buildroot%_includedir
cp -r out/%dart_out/dart-sdk %buildroot%_libexecdir/dart

install -Dm755 %SOURCE1 %buildroot%_bindir/dart
ln -s ../lib/dart/include %buildroot%_includedir/dart
ln -s ../lib/dart/bin/dartaotruntime %buildroot%_bindir/dartaotruntime

find %buildroot%_libexecdir/dart/bin/resources/devtools -type f -exec chmod 644 {} \;

%files
%_bindir/dart
%_includedir/dart
%_libexecdir/dart
%exclude %_libexecdir/dart/bin/dartaotruntime
%exclude %_libexecdir/dart/bin/snapshots/analysis_server.dart.snapshot
%exclude %_libexecdir/dart/bin/snapshots/dart2js_aot.dart.snapshot
%exclude %_libexecdir/dart/bin/snapshots/dartdevc.dart.snapshot
%exclude %_libexecdir/dart/bin/snapshots/gen_kernel_aot.dart.snapshot
%exclude %_libexecdir/dart/bin/snapshots/kernel-service.dart.snapshot
%exclude %_libexecdir/dart/bin/snapshots/kernel_worker_aot.dart.snapshot
%exclude %_libexecdir/dart/bin/snapshots/dart2wasm_product.snapshot
%exclude %_libexecdir/dart/bin/resources/dartdoc
%exclude %_libexecdir/dart/bin/resources/devtools
%exclude %_libexecdir/dart/bin/utils
%exclude %_libexecdir/dart/lib

%files -n dartaotruntime
%_bindir/dartaotruntime
%_libexecdir/dart/bin/dartaotruntime

%files sdk
%_libexecdir/dart/bin/snapshots/analysis_server.dart.snapshot
%_libexecdir/dart/bin/snapshots/dart2js_aot.dart.snapshot
%_libexecdir/dart/bin/snapshots/dartdevc.dart.snapshot
%_libexecdir/dart/bin/snapshots/gen_kernel_aot.dart.snapshot
%_libexecdir/dart/bin/snapshots/kernel-service.dart.snapshot
%_libexecdir/dart/bin/snapshots/kernel_worker_aot.dart.snapshot
%_libexecdir/dart/bin/snapshots/dart2wasm_product.snapshot
%_libexecdir/dart/bin/resources/dartdoc
%_libexecdir/dart/bin/resources/devtools
%_libexecdir/dart/bin/utils
%_libexecdir/dart/lib

%changelog
* Thu Nov 27 2025 David Sultaniiazov <x1z53@altlinux.org> 3.9.2-alt1
- Update to 3.9.2
- Splitting dart into dart, dartaotruntime and dart-bootstrap.

* Fri Jun 13 2025 David Sultaniiazov <x1z53@altlinux.org> 3.8.1-alt2
- Remove arm and riscv64 from source
- Add build for aarch64
- Fix patches applying

* Thu Jun 12 2025 David Sultaniiazov <x1z53@altlinux.org> 3.8.1-alt1
- Initial build
