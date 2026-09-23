# 1.4.0 is the first release written in Rust (1.3.14 was the last in Zig).
# git_commit is the bun-v1.4.2 tag peel, used as GIT_SHA for `bun --revision`;
# it is not part of the RPM version.
%define git_commit 744846f844374847c902b5e7fd59b4342a51ef99
%define git_short 744846f8
# The WebKit revision Source1 was made from. Checked against
# scripts/build/deps/webkit.ts in %%prep, so a version bump cannot leave the
# engine behind.
%define webkit_commit 2e2aa2290fac856d6f451ceacb58f7f5b44dd057
# The SQLite amalgamation in Bun's tree. Used for both the bundled() Provides
# and the %%check that asserts it against sqlite_version(), so the two cannot
# drift apart on a version bump.
%define bundled_sqlite 3.53.2
# The LLVM release selected through ALT's llvm-alt-tool-wrapper via
# ALTWRAP_LLVM_VERSION in %%build. Patch5 raises bun's pinned LLVM to this
# major.
%define llvm_version 22.1
# Building Bun requires an existing Bun: 24 of the build's code-generation
# steps use Bun.build and Bun.Transpiler, for which Node.js has no equivalent,
# and Bun's own bundler is what emits the JavaScript builtins with
# JavaScriptCore private-name intrinsics. The bun-bootstrap package supplies
# that first Bun. Turn this switch off once bun is in the distribution: it then
# builds with the Bun that is already there, and no foreign binary is
# involved.
%def_with bootstrap
# Bun pins a Rust nightly, but every unstable feature it uses is present in the
# distribution compiler; only the nightly gate is missing. Build with the
# distribution compiler and open the gate, which is what rustc's own bootstrap
# does.
%def_without rust_nightly

Name: bun
Version: 1.4.2
Release: alt1

Summary: Fast all-in-one JavaScript runtime and toolkit
# Bun itself is MIT, but it is one statically linked executable and everything
# in the Provides: bundled() list below ends up inside it, so the tag covers
# the whole binary. The notable ones are JavaScriptCore and tinycc (LGPL-2.1)
# and the Servo CSS crates (MPL-2.0); blessing comes from the SQLite
# amalgamation, Unicode-3.0 from unicode-ident, BSD-3-Clause from lol-html and
# lsquic. picohttpparser (MIT OR Artistic-1.0-Perl) is taken under its
# permissive half. See LICENSE.md, which upstream keeps current.
#
# LGPL-2.1 section 6 is satisfied by shipping the engine's source: WebKit is
# Source1 and is part of the src.rpm.
License: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND MPL-2.0 AND Unicode-3.0 AND Zlib AND blessing
Group: Development/Other
Url: https://bun.sh/
Vcs: https://github.com/oven-sh/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/oven-sh/%name/archive/%name-v%version/%name-%name-v%version.tar.gz
Source: %name-%name-v%version.tar
# The JavaScriptCore half of WebKit, the oven-sh/WebKit fork at the revision
# bun pins; not fetched by bun's dependency machinery, which expects a manual
# checkout.
# https://github.com/oven-sh/WebKit/archive/%webkit_commit/WebKit-%webkit_commit.tar.gz
Source1: WebKit-%webkit_commit.tar
# The C and C++ dependencies Bun downloads while building, in the
# content-addressed layout scripts/build/download.ts reads.
Source2: %name-prefetch-%version.tar
# Rust crates, from cargo vendor.
Source3: %name-vendor-%version.tar
# npm packages the code generators need.
Source4: %name-node-modules-%version.tar
# The generators for the sources above. They are run by the maintainer on a
# version bump, not by the package; kept here so the generated sources can be
# reproduced from what the package ships.
Source5: bun_prefetch
Source6: bun-deps.mjs
Source7: bun_webkit
# Bun's build installs the pinned Rust nightly with rustup and downloads its
# dependencies. Neither is possible in a build environment, and both are
# avoidable: serve the downloads from the prefetch cache and use the Rust that
# the distribution ships.
Patch0: bun-offline-build.patch
# Two allow() attributes name a lint that is newer than the released compiler,
# and the workspace denies warnings, so the unknown lint is fatal. Allowing
# unknown_lints alongside it is correct on both compilers.
Patch1: bun-unknown-lint.patch
# Emit debug information debugedit can read, so rpm can build a debuginfo
# package: DWARF 5 from rustc, as clang and the standard library already emit,
# and without the DWARF 5 accelerator table, which debugedit does not know.
Patch2: bun-uniform-dwarf.patch
# Do not let WebKit put types in their own units. The linker keeps one copy of
# each and drops the rest, leaving .debug_str_offsets entries no unit refers to
# any more, and debugedit asserts on the first of those.
Patch3: bun-webkit-no-type-units.patch
# Link zstd, brotli, libdeflate, libspng, libwebp and libjpeg-turbo from the
# distribution instead of the vendored copies. These are the bundled C
# libraries whose pin is an unmodified upstream release rather than a fork and
# that Bun reaches through their installed public headers, so each can be
# tracked like any other shared library. See the patch header for the details
# that are specific to each of them.
Patch4: bun-system-libs.patch
# Raise the LLVM version bun pins from 21 to the distribution default.
Patch5: bun-llvm-22.patch

BuildRequires: rust-cargo
# The C/C++ toolchain and the linker the ALT wrapper selects (ALTWRAP_LLVM_VERSION
# in %%build). Patch5 raises bun's pinned LLVM to this major; scripts/build/
# tools.ts enforces the version for the C compiler and the linker.
BuildRequires: clang%llvm_version
BuildRequires: cmake >= 3.24
BuildRequires: gcc-c++
# The final executable links libstdc++ and libatomic statically
# (-static-libstdc++ -static-libgcc -l:libatomic.a).
BuildRequires: libstdc++-devel-static
BuildRequires: libatomic-devel-static
# Bun patches several of its vendored C dependencies with `git apply`.
BuildRequires: git-core
BuildRequires: lld%llvm_version
BuildRequires: llvm%llvm_version
BuildRequires: ninja-build
BuildRequires: perl
# Bun's own static-hashtable generator uses bigint; WebKit's cmake uses JSON::PP.
# ALT's perl does not carry these, and they are not pulled in by anything else.
BuildRequires: perl-bignum
BuildRequires: perl-JSON-PP
BuildRequires: pkg-config
BuildRequires: python3
# Not a floor upstream states - upstream pins a nightly - but the oldest
# release this was actually built with. An older compiler fails deep in the
# workspace instead of here.
BuildRequires: rustc >= 1.97
BuildRequires: unzip
BuildRequires: zstd
# Unbundled by Patch4. brotlicommon has no header of its own but is a separate
# pkg-config module, and the link line names it.
BuildRequires: libbrotli-devel
BuildRequires: libdeflate-devel
BuildRequires: libjpeg-devel
BuildRequires: libspng-devel
BuildRequires: libwebp-devel
BuildRequires: libzstd-devel
# JavaScriptCore's own build system.
BuildRequires: ruby
BuildRequires: libicu-devel
# Bun is a single statically linked executable and everything still listed here
# ends up inside it. Each is pinned to an exact commit, several are upstream
# forks (boringssl, tinycc, mimalloc, lol-html) and the JavaScript engine is a
# fork of WebKit, so none of them can be unbundled the way the six in Patch4
# were. Unversioned because upstream pins commits rather than releases.
Provides: bundled(bcrypt) = 0.19.0
Provides: bundled(boringssl)
Provides: bundled(c-ares)
Provides: bundled(hdr_histogram)
Provides: bundled(highway)
Provides: bundled(libarchive)
Provides: bundled(lol-html)
Provides: bundled(ls-hpack)
Provides: bundled(ls-qpack)
Provides: bundled(lsquic)
Provides: bundled(mimalloc)
Provides: bundled(picohttpparser)
Provides: bundled(rust-argon2)
# bun:sqlite and node:sqlite are built against the SQLite amalgamation in Bun's
# own tree. Unbundling is not possible even in principle: the alternative Bun
# offers (LAZY_LOAD_SQLITE) is a macOS-only path that dlopens a hardcoded
# "libsqlite3.dylib" (src/jsc/bindings/sqlite/lazy_sqlite3.h), so on Linux
# there is no configuration that links or loads the system library.
Provides: bundled(sqlite3) = %bundled_sqlite
Provides: bundled(tinycc)
Provides: bundled(usockets)
Provides: bundled(uwebsockets)
Provides: bundled(webkit)
Provides: bundled(zlib-ng)
# Upstream supports linux-x64 and linux-arm64 only, and Bun can only be built
# where an upstream bootstrap binary is published for the same architecture.
ExclusiveArch: x86_64 aarch64
%if_with bootstrap
BuildRequires: %name-bootstrap = %version
%else
BuildRequires: %name
%endif

%description
Bun is an all-in-one JavaScript runtime and toolkit with a bundler, test
runner, and Node.js-compatible package manager.

%prep
%setup -n %name-%name-v%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# The WebKit source must be the revision bun is written against: its
# JavaScriptCore C++ API is private and unversioned.
grep -q "WEBKIT_VERSION = \"%webkit_commit\"" scripts/build/deps/webkit.ts || {
    echo "scripts/build/deps/webkit.ts does not pin %webkit_commit" >&2
    exit 1
}

# JavaScriptCore. Bun's build expects a manual checkout here. The test suites
# and the website are excluded by the tar rule in .gear/rules, so the source
# package does not carry five times the code the build reads.
mkdir -p vendor/WebKit
tar -xf %SOURCE1 -C vendor/WebKit --strip-components=1
# Tools/WebKitBot is a Node.js service whose lockfile names packages with
# published CVEs; none of it is built or shipped.
rm -rf vendor/WebKit/Tools/WebKitBot

# The dependency downloads, the Rust crates and the npm packages for the code
# generators. The tar rules in .gear/rules pack each committed directory with
# the leading path the build expects.
tar -xf %SOURCE2
tar -xf %SOURCE3
tar -xf %SOURCE4

# The build runs node_modules/.bin/esbuild (scripts/build/configure.ts), and
# bun links that name straight at the prebuilt binary for the architecture the
# install ran on, so it is the one thing in that archive that cannot serve both
# architectures. Point it at esbuild's own launcher instead - the node script
# npm links here, which picks the platform package at run time. The archive
# carries that package for every architecture this builds for; everything else
# in it already chooses at run time.
find . -path '*/node_modules/.bin/esbuild' -exec ln -sf ../esbuild/bin/esbuild {} \;
# That launcher is a Node script, and the build deliberately has no Node: run it
# with Bun instead, which executes Node programs as they are.
find . -path '*/node_modules/esbuild/bin/esbuild' -exec \
    sed -i '1s|^#!.*|#!/usr/bin/env %name|' {} +

# lol-html and rust-argon2 are both downloads and Rust path dependencies of the
# workspace, so they have to be unpacked before cargo can read the manifest.
# rust-argon2 was a crates.io dep in the snapshot; 1.4.0 vendors it to apply
# patches/rust-argon2/legacy-low-memory.patch (Bun.password still verifies
# argon2 hashes with memoryCost below 8).
mkdir -p vendor/lolhtml vendor/rust-argon2
tar -xzf "prefetch/by-url/$(grep -F 'oven-sh/lol-html' prefetch/manifest.sha256 | cut -d' ' -f1)" \
    -C vendor/lolhtml --strip-components=1
tar -xzf "prefetch/by-url/$(grep -F 'sru-systems/rust-argon2' prefetch/manifest.sha256 | cut -d' ' -f1)" \
    -C vendor/rust-argon2 --strip-components=1
patch -p1 -d vendor/rust-argon2 < patches/rust-argon2/legacy-low-memory.patch

# Point cargo at the vendored crates. This has to go in CARGO_HOME rather than
# .cargo/config.toml, which Bun's build regenerates on every configure.
mkdir -p .cargo-home
cat >.cargo-home/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$PWD/cargo-vendor"
EOF

%if_without rust_nightly
# Bun pins a Rust nightly. Use the distribution compiler instead and open the
# unstable-feature gate, as rustc's own bootstrap does.
rm -f rust-toolchain.toml
%endif

%build
# ALT's unversioned clang, clang++, ld.lld and llvm-ar are all the
# llvm-alt-tool-wrapper; ALTWRAP_LLVM_VERSION selects the release required
# above. Bun resolves its own toolchain (scripts/build/tools.ts) and never
# reads CC, CXX, AR or RANLIB - those are for the cc crate in the Rust
# workspace.
export ALTWRAP_LLVM_VERSION=%llvm_version
export CC=clang
export CXX=clang++
export AR=llvm-ar
export RANLIB=llvm-ranlib
export GIT_SHA="%git_commit"
# process.versions.zstd and .libdeflate are generated from the vendored commit
# hashes, which say nothing once the distribution libraries are linked instead
# (Patch4). Report what is actually linked. The other four have no such macro,
# so they need no counterpart.
export BUN_SYSTEM_VERSION_ZSTD="$(pkg-config --modversion libzstd)"
export BUN_SYSTEM_VERSION_LIBDEFLATE="$(pkg-config --modversion libdeflate)"
export CARGO_HOME="$PWD/.cargo-home"
export CARGO_NET_OFFLINE=true
%if_without rust_nightly
export RUSTC_BOOTSTRAP=1
%endif
# Serve every dependency download from the prepared cache.
export BUN_BUILD_PREFETCH_DIR="$PWD/prefetch"
export BUN_WEBKIT_PATH="$PWD/vendor/WebKit"
%if_with bootstrap
export PATH="%_libexecdir/%name-bootstrap/bin:$PATH"
%endif

# The build driver runs on Bun (it is a TypeScript program; running it under
# bun is upstream's documented alternative to Node 25+). The bootstrap Bun, if
# used, is reached here and by the code generators alike.
#
# --canary=off  otherwise the version is reported as a canary build.
# --lto=off     cross-language LTO needs rustc's own LLVM tools, which the
#               distribution compiler does not ship; it is off by default
#               outside upstream CI anyway.
# --baseline    on x86_64 this targets Nehalem (x86-64-v2); the default needs
#               AVX2. Not passed on aarch64, which has a single target.
build_args=(--profile=release
            --build-dir=build/release
            --cache-dir="$PWD/build/cache"
            --canary=off
            --lto=off
            --webkit=local)
%ifarch x86_64
build_args+=(--baseline=on)
%endif

%name scripts/build.ts "${build_args[@]}"

%install
# bun-profile, not bun: a release build links bun-profile and then strips it
# into bun with --strip-all --strip-debug. Installing the stripped one leaves
# rpm nothing to extract, so no debuginfo package is built and the result is
# still flagged unstripped. bun-profile is the same binary before that step.
%__install -Dpm 0755 build/release/bun-profile %buildroot%_bindir/%name
# Bun dispatches on argv[0]: invoked as bunx it runs `bun x`, the package
# runner (src/runtime/cli/mod.rs). Upstream's installer makes the same link.
%__ln_s %name %buildroot%_bindir/%{name}x

%check
%buildroot%_bindir/%name --version
# Anchored on the release form. A canary reports <ver>-canary.<stamp>+<sha>,
# which a bare substring match for the short sha would have accepted.
%buildroot%_bindir/%name --revision | grep -E "^%version\+%git_short"
%buildroot%_bindir/%name -e 'if (6 * 7 !== 42) process.exit(1)'
# The bundler and the package manager are the reason this package exists.
%buildroot%_bindir/%name build --help >/dev/null
%buildroot%_bindir/%name install --help >/dev/null

# The native surfaces this package makes bundled() claims about. --help exiting
# 0 proves nothing about any of them, and all three are statically linked, so
# nothing else in the build would notice if they broke.
#
# bun:sqlite, against the version the Provides advertises.
%buildroot%_bindir/%name -e 'import{Database}from"bun:sqlite";const v=new Database(":memory:").query("select sqlite_version() v").get().v;if(v!=="%bundled_sqlite")throw new Error("bundled(sqlite3) says %bundled_sqlite, runtime says "+v)'
# bun:ffi, dlopening a library built here rather than a system one, so the test
# fails on a broken FFI rather than on a missing dependency.
cat > _ffi_check.c <<'EOF'
long long ffi_smoke(long long a, long long b) { return a * b + 1; }
EOF
gcc -shared -fPIC -o _ffi_check.so _ffi_check.c
%buildroot%_bindir/%name -e 'import{dlopen,FFIType}from"bun:ffi";const{symbols:{ffi_smoke:f}}=dlopen("./_ffi_check.so",{ffi_smoke:{args:[FFIType.i64,FFIType.i64],returns:FFIType.i64}});const r=f(6n,7n);if(r!==43n)throw new Error("bun:ffi returned "+r)'
# bundled(tinycc): cc() compiles at run time with the vendored tcc. No
# #include, so this does not depend on the buildroot's libc headers.
cat > _tcc_check.c <<'EOF'
int tcc_smoke(int x) { return x * 2 + 2; }
EOF
%buildroot%_bindir/%name -e 'import{cc}from"bun:ffi";const{symbols:{tcc_smoke:g}}=cc({source:"./_tcc_check.c",symbols:{tcc_smoke:{args:["int"],returns:"int"}}});const r=g(20);if(r!==42)throw new Error("bundled(tinycc) returned "+r)'

# Patch4 must have taken effect: every unbundled library has to be an ELF
# dependency now. A silently reverted patch would otherwise still build and
# still pass every test above.
ldd %buildroot%_bindir/%name
for lib in libzstd libbrotlienc libbrotlidec libbrotlicommon libdeflate \
           libspng libwebp libwebpmux libwebpdemux libturbojpeg; do
    ldd %buildroot%_bindir/%name | grep -qE "\<$lib\.so" || \
        { echo "$lib is not linked - Patch4 did not take effect"; exit 1; }
done
# ... and each one works through the binary, not just at link time.
%buildroot%_bindir/%name -e 'const c=Bun.zstdCompressSync(Buffer.from("z".repeat(4096)));if(Bun.zstdDecompressSync(c).length!==4096)throw new Error("zstd round trip failed")'
%buildroot%_bindir/%name -e 'const z=require("node:zlib");const c=z.brotliCompressSync(Buffer.from("b".repeat(4096)));if(z.brotliDecompressSync(c).length!==4096)throw new Error("brotli round trip failed")'
# Bun.gzipSync/deflateSync are libdeflate, not zlib-ng.
%buildroot%_bindir/%name -e 'const b=Buffer.from("d".repeat(4096));for(const[c,d]of[[Bun.gzipSync,Bun.gunzipSync],[Bun.deflateSync,Bun.inflateSync]])if(d(c(b)).length!==4096)throw new Error("libdeflate round trip failed")'
# The three image codecs, chained so that one seed exercises all of them:
# libspng decodes, libjpeg-turbo re-encodes and decodes, libwebp likewise, and
# libspng encodes at the end. A struct-layout or ABI-constant mismatch between
# Bun's hand-written Rust externs and the distribution headers shows up here as
# a wrong size or a decode failure rather than at link time.
cat > _img_check.mjs <<'EOF'
const seed = Buffer.from(
  "iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAYAAADED76LAAAAXklEQVR42hXKMQHAMAgAsEqp" +
  "FKQgBSlIQQpOtvTIl3NOfZcgKZphOecKBEnRDHtfCIEgKZph44UUCJKiGTZfKIEgKZph64UW" +
  "CJKiGbZfGIEgKZph54UVCJKiGXbr+wH6kZfBPhkbiwAAAABJRU5ErkJggg==", "base64");
let bytes = seed;
for (const fmt of ["jpeg", "webp", "png"]) {
  bytes = await new Bun.Image(bytes)[fmt]().bytes();
  const m = await new Bun.Image(bytes).metadata();
  if (m.width !== 8 || m.height !== 8) {
    throw new Error(`${fmt}: got ${m.width}x${m.height}, expected 8x8`);
  }
  if (m.format !== fmt) throw new Error(`${fmt}: sniffed as ${m.format}`);
}
EOF
%buildroot%_bindir/%name run _img_check.mjs
# process.versions reports the linked libraries, not the vendored commits.
%buildroot%_bindir/%name -e 'for(const[k,w]of[["zstd","'"$(pkg-config --modversion libzstd)"'"],["libdeflate","'"$(pkg-config --modversion libdeflate)"'"]]){const v=process.versions[k];if(v!==w)throw new Error("process.versions."+k+" is "+v+", linked is "+w)}'

%files
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.md README.md REVIEW.md SECURITY.md
%_bindir/%name
%_bindir/%{name}x

%changelog
* Wed Sep 23 2026 Nazarov Denis <nenderus@altlinux.org> 1.4.2-alt1
- Initial build
