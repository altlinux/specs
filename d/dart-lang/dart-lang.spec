%define _unpackaged_files_terminate_build 1

Name: dart-lang
Version: 3.8.1
Release: alt1

Summary: Dart language
License: BSD-3-Clause
Group: Development/Other

Source0: %name-%version.tar
Source1: dart-wrapper.sh
Patch: %name-%version-alt.patch

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
BuildRequires: dart-lang-bootstrap

ExclusiveArch: x86_64

%description
%summary.

%prep
%setup
%patch -p 1

# SOURCE
#
# echo "
# solutions = [{
# 'name': 'sdk',
# 'url': 'https://dart.googlesource.com/sdk.git@3.8.1',
# }]
# target_cpu = ['x64', 'arm64', 'arm', 'riscv64']
# target_cpu_only = True
# " > .gclient
#
# gclient sync --no-history --nohooks --tpot-cipd-ignore-platformed
#
# for elf in $(scanelf -RA -F "%F" sdk); do
#   rm -f "$elf"
# done
#
# mv sdk dart-sdk-3.8.1
#
# tar -cf dart-sdk-3.8.1.tar \
#   --exclude="ChangeLog*" \
#   --exclude="sdk/buildtools/*/clang" \
#   --exclude="third_party/fuchsia/sdk/linux/arch" \
#   --exclude=".build-id" \
#   --exclude-backups \
#   --exclude-caches-all \
#   --exclude-vcs \
#   dart-sdk-3.8.1

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
  --arch="x64" \
  --mode=release \
  --no-verify-sdk-hash \
  --gn-args='dart_embed_icu_data=false dart_snapshot_kind="app-jit" dart_sysroot=""' \
  create_sdk runtime

%install
mkdir -p %buildroot%_bindir %buildroot%_libexecdir %buildroot%_includedir
cp -r %_builddir/%name-%version/out/ReleaseX64/dart-sdk %buildroot%_libexecdir/dart

install -Dm755 %SOURCE1 %buildroot%_bindir/dart
ln -s ../lib/dart/include %buildroot%_includedir/dart
ln -s ../lib/dart/bin/dartaotruntime %buildroot%_bindir/dartaotruntime

find %buildroot%_libexecdir/dart/bin/resources/devtools -type f -exec chmod 644 {} \;

%files
%_bindir/dart
%_bindir/dartaotruntime
%_includedir/dart
%_libexecdir/dart

%changelog
* Thu Jun 12 2025 David Sultaniiazov <x1z53@altlinux.org> 3.8.1-alt1
- Initial build
