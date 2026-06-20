%define _unpackaged_files_terminate_build 1
%def_with check

# Build-time tools (e.g. v8_context_snapshot_generator) need $ORIGIN RPATHs
# preserved. Same setting as ALT chromium spec.
%set_verify_elf_method rpath=relaxed textrel=relaxed lfs=relaxed lint=relaxed

%define electron_outdir out/Release

# Bundled Chromium clang (currently 23) is ahead of what ALT ships, so pin
# to the matching packaged toolchain.
%define llvm_version 22.1
%define llvm_major   22

Name: electron
Version: 42.4.0
Release: alt1

Summary: Build cross-platform desktop apps with JavaScript, HTML, and CSS
License: MIT
Group: Development/Other
Url: https://electronjs.org/
Vcs: https://github.com/electron/electron.git

Source0: %name-%version.tar.zst
Source1: chromium.tar.zst
Source2: chromium-third-party.tar.zst
Source3: electron-yarn-cache.tar.zst
Patch0: %name-%version-alt.patch
### Start Patches
Patch1: 0001-vendor-chromium-Narrow-GN-dep-graph-to-electron.patch
Patch2: 0002-vendor-swiftshader-Use-bundled-llvm-16-and-fix-STL-i.patch
Patch3: 0003-vendor-chromium-Point-bindgen-at-system-libclang-und.patch
Patch4: 0004-vendor-chromium-Drop-clang-flags-unsupported-by-syst.patch
Patch5: 0005-vendor-chromium-Read-clang-runtime-libdir-from-CLANG.patch
Patch6: 0006-vendor-chromium-Drop-GN-check_version-dep-on-bundled.patch
Patch7: 0007-vendor-chromium-Add-libc-22-missing-transitive-inclu.patch
Patch8: 0008-vendor-chromium-Revert-ParseRequestCookieLine-to-con.patch
Patch9: 0009-vendor-chromium-Spell-out-optional-value_or-template.patch
Patch10: 0010-vendor-pthreadpool-Block-clang-22-stdatomic.h-via-__.patch
Patch11: 0011-vendor-mojo-Neutralize-vector-bool-static_assert-in-.patch
Patch12: 0012-vendor-chromium-Add-absolute-RPATH-from-CHROMIUM_RPA.patch
Patch13: 0013-vendor-chromium-Avoid-std-find-prvalue-in-private_ke.patch
Patch14: 0014-vendor-chromium-Force-use_safe_libcxx-for-the-V8-san.patch
Patch15: 0015-vendor-chromium-Replace-std-ranges-iota-with-std-iot.patch
Patch16: 0016-vendor-chromium-Drop-bytemuck-core-simd-LaneCount-bo.patch
Patch17: 0017-vendor-chromium-Gate-V8_USE-sanitizer-macros-on-GN.patch
Patch18: 0018-vendor-chromium-Use-glibc-SYS_SECCOMP-enum-drop-coll.patch
Patch19: 0019-vendor-chromium-Avoid-std-map-find-with-raw_ref-key-.patch
### End Patches

ExclusiveArch: x86_64 aarch64

# Loaded via dlopen, invisible to autoreq.
Requires: libvulkan1

BuildRequires(pre): rpm-build-licenses rpm-build-ninja
BuildRequires: /proc

# Toolchain
BuildRequires: clang%llvm_version clang%llvm_version-devel
BuildRequires: lld%llvm_version
BuildRequires: llvm%llvm_version-devel
BuildRequires: clang%llvm_version-support
BuildRequires: libclang%llvm_major
BuildRequires: gn >= 0.2384.1740f5c2
BuildRequires: esbuild
BuildRequires: nodejs >= 22.18.0
BuildRequires: rust
BuildRequires: rust-bindgen
BuildRequires: rustfmt
# Replaces chromium-bundled libc++; same as ALT chromium spec.
BuildRequires: libcxx-devel libcxx-static libcxxabi-devel libcxxabi-static

# Code generators / build-time tools (chromium codegen, post-build cleanup)
BuildRequires: bison flex gperf
BuildRequires: glibc-kernheaders
BuildRequires: chrpath elfutils patchutils xdg-utils

# Python modules used by mojo / blink / devtools build scripts
BuildRequires: python3(bs4)
BuildRequires: python3(html5lib)
BuildRequires: python3(markupsafe)
BuildRequires: python3(ply)
BuildRequires: python3(simplejson)

# GTK / GNOME stack
BuildRequires: libgtk+3-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libat-spi2-core-devel
BuildRequires: at-spi2-atk-devel
BuildRequires: libsecret-devel

# System libraries Chromium links against (not bundled in our config)
BuildRequires: libgio-devel
BuildRequires: libcups-devel
BuildRequires: libnss-devel libnspr-devel
BuildRequires: libdbus-devel
BuildRequires: libalsa-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libpci-devel
BuildRequires: libcap-devel
BuildRequires: libudev-devel
BuildRequires: libuuid-devel
BuildRequires: libcurl-devel
BuildRequires: libkrb5-devel
BuildRequires: libffi-devel
BuildRequires: libexpat-devel
BuildRequires: libnotify-devel
BuildRequires: pipewire-libs-devel

# Fonts / text
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: libharfbuzz-devel

# Graphics / GPU
BuildRequires: libGL-devel
BuildRequires: libgbm-devel
BuildRequires: libva-devel
BuildRequires: libdrm-devel

# X11
BuildRequires: libX11-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxshmfence-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXtst-devel

%if_with check
BuildRequires: xvfb-run
%endif

%description
Electron is a framework for building cross-platform desktop applications
with web technologies (JavaScript, HTML and CSS). It bundles the Chromium
rendering engine and the Node.js runtime into a single executable, so the
same code base runs on Linux, macOS and Windows.

This package provides the Electron runtime, command-line launcher and the
bundled resources. It is intended both as a dependency for Electron
applications and as a development tool for building and packaging them.

%prep
%setup -c -T
mkdir -p src/electron
tar -xf %SOURCE0 -C src/electron --strip-components=1
tar -xf %SOURCE1 -C src --strip-components=1
mkdir -p src/third_party
tar -xf %SOURCE2 -C src/third_party --strip-components=1

%patch0 -p1 -d src/electron

# Apply the chromium-side patches in .gear/patches/. Patch0 above is the
# electron-alt cumulative patch; the block below is refreshed by
# .gear/scripts/patches.sh from the .gear/patches/ contents.
### Start Apply Patches
%patch1 -p1 -d src
%patch2 -p1 -d src
%patch3 -p1 -d src
%patch4 -p1 -d src
%patch5 -p1 -d src
%patch6 -p1 -d src
%patch7 -p1 -d src
%patch8 -p1 -d src
%patch9 -p1 -d src
%patch10 -p1 -d src
%patch11 -p1 -d src
%patch12 -p1 -d src
%patch13 -p1 -d src
%patch14 -p1 -d src
%patch15 -p1 -d src
%patch16 -p1 -d src
%patch17 -p1 -d src
%patch18 -p1 -d src
%patch19 -p1 -d src
### End Apply Patches

mkdir -p src/electron/.yarn/cache
tar -xf %SOURCE3 -C src/electron/.yarn/cache --strip-components=1

( cd src/electron && \
    YARN_ENABLE_NETWORK=false \
    YARN_ENABLE_GLOBAL_CACHE=0 \
    YARN_ENABLE_TELEMETRY=false \
    node .yarn/releases/yarn-*.cjs install \
        --immutable --immutable-cache --mode=skip-build )

# ELECTRON_PATCH_NO_GIT switches the script from `git am` to GNU `patch`
# so we don't need a git tree inside the build root.
ELECTRON_PATCH_NO_GIT=1 \
    python3 src/electron/script/apply_all_patches.py \
        src/electron/patches/config.json

# Synthesize lastchange.py outputs: vendor is a bare tarball with no .git.
TS="${SOURCE_DATE_EPOCH:-$(date +%s)}"
mkdir -p src/build/util
printf '%s' "$TS" > src/build/util/LASTCHANGE.committime
printf 'LASTCHANGE=%040d-refs/heads/main@{#0}\nLASTCHANGE_YEAR=%s\n' \
    0 "$(date -u -d @$TS +%Y)" > src/build/util/LASTCHANGE

mkdir -p src/gpu/config src/skia/ext src/gpu/webgpu
printf '#define GPU_LISTS_VERSION "0"\n' > src/gpu/config/gpu_lists_version.h
printf '#define SKIA_COMMIT_HASH "0"\n'  > src/skia/ext/skia_commit_hash.h
printf '#define DAWN_COMMIT_HASH "0"\n'  > src/gpu/webgpu/dawn_commit_hash.h

# WebUI build expects a bundled node at this path; vendor doesn't ship it.
mkdir -p src/third_party/node/linux/node-linux-x64/bin
ln -sf /usr/bin/node src/third_party/node/linux/node-linux-x64/bin/node

# Vendor ships only an x86_64 esbuild binary (fails to exec on aarch64).
# esbuild refuses to run if host npm version != binary version, so rewrite
# the pin to the system package version. Same approach as ALT chromium.
# Bump %es_old when vendor is regenerated.
%define es_old "0\.25\.1"
%define es_new %(rpmquery --qf '%%{VERSION}' esbuild)
sed -i 's!%es_old!"%es_new"!g' \
    `grep -Rl \"%es_old\" src/third_party/devtools-frontend/src`
mkdir -p src/third_party/devtools-frontend/src/third_party/esbuild
ln -sf %_bindir/esbuild \
    src/third_party/devtools-frontend/src/third_party/esbuild/esbuild

test -f src/electron/build/args/release.gn
test -f src/.gn
test -d src/third_party/blink || test -d src/third_party/icu

%build
export PATH="%_bindir:$PATH"
cd src

export ALTWRAP_LLVM_VERSION="%llvm_version"

# Consumed by the patched rpath_for_built_shared_libraries config:
# $ORIGIN for build-time tools, absolute path once installed.
export CHROMIUM_RPATH="%_libdir/%name"

# A non-empty rust_sysroot_absolute flips use_chromium_rust_toolchain=false
# in build/config/rust.gni and skips the read_file() on the pruned
# third_party/rust-toolchain/VERSION.
RUST_SYSROOT="$(rustc --print sysroot)"
# Cache-busting key only; must be a single token because the rsp file is
# split on spaces.
RUSTC_VERSION="$(rustc --version | tr -d '()' | tr -s ' ' '-')"

CLANG_RESOURCE_DIR="$(/usr/bin/clang-%llvm_major -print-resource-dir)"
CLANG_VERSION="$(basename "$CLANG_RESOURCE_DIR")"

# ALT keeps compiler-rt under lib64/clang/<v>/lib (multilib); chromium GN
# hardcodes lib/clang/<v>/lib. Same workaround as ALT chromium's
# 0025-Fix-rust-clang-path.patch.
export CLANG_LIBDIR="$CLANG_RESOURCE_DIR/lib"

# Chromium's standard toolchain templates ignore CFLAGS/CXXFLAGS/LDFLAGS,
# so -stdlib=libc++ never reaches cc invocations and clang silently picks
# up libstdc++ headers — TU-wide ABI mismatch ("no viable conversion from
# 'const_iterator' ..." in net/cookies/cookie_util.cc). The unbundle:default
# toolchain honors $CC/$CXX/$AR/$CFLAGS/$CXXFLAGS/$LDFLAGS. Same as ALT
# chromium spec.
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export RANLIB="llvm-ranlib"
export CXXFLAGS="${CXXFLAGS:-} -stdlib=libc++ -I/usr/include/c++/v1"
export LDFLAGS="${LDFLAGS:-} -stdlib=libc++ -L%_libdir -lc++ -lc++abi"

# Chromium passes unstable -Z flags to rustc; only accepted on stable
# rustc with this flag.
export RUSTC_BOOTSTRAP=1

gn_arg=()
gn_arg+=( import\(\"//electron/build/args/release.gn\"\) )

# Toolchain
gn_arg+=( custom_toolchain=\"//build/toolchain/linux/unbundle:default\" )
gn_arg+=( host_toolchain=\"//build/toolchain/linux/unbundle:default\" )
gn_arg+=( clang_base_path=\"/usr/lib/llvm-%llvm_version\" )
gn_arg+=( clang_use_chrome_plugins=false )
gn_arg+=( clang_version=\"$CLANG_VERSION\" )

# Libc++ / sysroot
gn_arg+=( is_component_build=false )
gn_arg+=( use_sysroot=false )
gn_arg+=( use_custom_libcxx=false )

# System libraries
gn_arg+=( use_system_libffi=true )
gn_arg+=( use_system_vulkan_headers=true )

# Rust
gn_arg+=( rust_sysroot_absolute=\"$RUST_SYSROOT\" )
gn_arg+=( rustc_version=\"$RUSTC_VERSION\" )
gn_arg+=( rust_bindgen_root=\"/usr\" )

# Debug / warnings
gn_arg+=( treat_warnings_as_errors=false )
gn_arg+=( symbol_level=0 )
gn_arg+=( blink_symbol_level=0 )
gn_arg+=( v8_symbol_level=0 )
gn_arg+=( chrome_pgo_phase=0 )
# release.gn points v8_builtins_profiling_log_file at the Electron-generated
# V8 builtins profile, which is downloaded by gclient hooks and is absent
# from the vendored tree. v8/BUILD.gn adds it as a mksnapshot source whenever
# the path is non-empty (independent of chrome_pgo_phase), so ninja aborts:
# "electron-v8-builtins.profile missing and no known rule to make it". Clear
# it to build V8 without builtins PGO (C++ PGO is already off above).
gn_arg+=( v8_builtins_profiling_log_file=\"\" )

# Electron
gn_arg+=( override_electron_version=\"%version\" )

# ThinLTO adds ~1.5-2x per-file compile time on heavy blink/content TUs
# (measured via -ftime-report, task 417157 build/41), and aarch64 hits
# the 8h girar wall-clock limit before reaching the link step where the
# devirtualization payoff lives (build/44: 39064/45758 targets in 8h).
# x86_64 builds in ~1h and keeps ThinLTO. Mirrors chromium22.spec:511-516.
%ifarch aarch64
gn_arg+=( use_thin_lto=false )
gn_arg+=( thin_lto_enable_optimizations=false )
%endif

# build/toolchain/gcc_toolchain.gni hardcodes
# //third_party/rust-toolchain/bin/rustc as a rustc_wrapper input,
# independent of rust_sysroot_absolute (which only redirects the rustc
# actually invoked). The bundled toolchain is pruned from the vendor tree,
# so ninja aborts: "rustc missing and no known rule to make it". Point the
# expected paths at the system rust binaries. Same as ALT chromium spec.
mkdir -p third_party/rust-toolchain/bin
ln -sf %_bindir/rustc third_party/rust-toolchain/bin/rustc
ln -sf %_bindir/rustfmt third_party/rust-toolchain/bin/rustfmt
ln -sf %_bindir/bindgen third_party/rust-toolchain/bin/bindgen

# blink codegen runs a prebuilt CIPD gperf (third_party/gperf/cipd/bin/gperf)
# that is an x86_64 ELF, so it fails with "Exec format error" on aarch64.
# Replace it with the system gperf. Same as ALT chromium spec.
ln -sf %_bindir/gperf third_party/gperf/cipd/bin/gperf

gn gen %electron_outdir --args="${gn_arg[*]}"

# %ninja_build expands to -j$NPROCS (-j32 on the aarch64 builder). llvm-22 needs
# ~2.5 GB RAM per heavy content/browser TU, so at -j32 the builder swaps and the
# second half crawls (8 min/file), missing the 8h girar wall. ThinLTO on
# (build/44) and off (build/110) both died at ~39000/45700 targets in 8h, so the
# wall is memory thrash, not LTO. Cap jobs on aarch64 like chromium22.spec.
%ifarch aarch64
%_bindir/ninja -j24 -C %electron_outdir electron
%else
%ninja_build -C %electron_outdir electron
%endif

%install
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%_bindir

install -m 0755 src/%electron_outdir/electron %buildroot%_libdir/%name/electron

cp -a src/%electron_outdir/{resources,locales,angledata,hyphen-data} \
    %buildroot%_libdir/%name/
cp -a src/%electron_outdir/{*.pak,*.bin,*.dat} %buildroot%_libdir/%name/

# Skip libVkICD_mock_icd.so (tests-only) and libvulkan.so.1 (system).
cp -a src/%electron_outdir/{libEGL,libGLESv2,libffmpeg,libvk_swiftshader}.so \
    %buildroot%_libdir/%name/
install -m 0644 src/%electron_outdir/vk_swiftshader_icd.json \
    %buildroot%_libdir/%name/

install -m 0755 src/%electron_outdir/chrome_crashpad_handler \
    %buildroot%_libdir/%name/chrome_crashpad_handler

# Fallback for systems with unprivileged userns disabled (hardening
# profiles, future CVE mitigations); without it Electron aborts with
# "No usable sandbox". Build emits chrome_sandbox (underscore); the
# loader expects chrome-sandbox (hyphen). Mode 4711 matches ALT chromium.
install -m 4711 src/%electron_outdir/chrome_sandbox \
    %buildroot%_libdir/%name/chrome-sandbox

ln -s -r %buildroot%_libdir/%name/electron %buildroot%_bindir/electron

%check
cd src
EBIN="%electron_outdir/electron"
# The production binary has an absolute RPATH (%_libdir/%name) baked in
# for the installed layout, so in the build tree it can't find its
# sibling .so's (libffmpeg, libGLESv2, libvk_swiftshader, ...).
export LD_LIBRARY_PATH="$PWD/%electron_outdir"

# 1. --version reports the version we built. --no-sandbox because
#    even --version goes through content_main and brings up the
#    zygote, which needs unprivileged userns (absent in hasher).
$EBIN --no-sandbox --version | grep -F "%version"

# 2. Node embedding: ELECTRON_RUN_AS_NODE loads and exposes electron +
#    chrome + node runtime versions.
ELECTRON_RUN_AS_NODE=1 $EBIN -e '
  const v = process.versions;
  if (!v.electron || !v.chrome || !v.node)
      throw new Error("missing versions: " + JSON.stringify(v));
  console.log("versions:", v.electron, v.chrome, v.node);
'

# 3. Headless GUI lifecycle: real Electron app reaches `ready` and quits
#    cleanly. --no-sandbox because hasher chroot has no unprivileged
#    userns; xvfb-run supplies a fake display.
mkdir -p smoke-app
cat > smoke-app/package.json <<'EOF'
{ "name": "smoke", "main": "main.js" }
EOF
cat > smoke-app/main.js <<'EOF'
const { app } = require('electron');
app.whenReady().then(() => { console.log('ready'); app.quit(); });
EOF
xvfb-run -a $EBIN --no-sandbox smoke-app

%files
%doc src/electron/README.md src/electron/LICENSE
%_bindir/electron
%attr(4711,root,root) %_libdir/electron/chrome-sandbox
%_libdir/electron/

%changelog
* Fri Jun 19 2026 Ajrat Makhmutov <rauty@altlinux.org> 42.4.0-alt1
- First build for ALT.
