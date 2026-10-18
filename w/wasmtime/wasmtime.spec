%define _unpackaged_files_terminate_build 1
# SONAME libwasmtime.so.MAJOR is set by c-api-soname.patch
%define soversion %(echo %version | cut -d. -f1)

# rustc runs out of 32-bit address space building wasmtime-cli
ExcludeArch: %ix86

Name: wasmtime
Version: 49.0.3
Release: alt1
Summary: Wasmtime is a standalone runtime for WebAssembly, WASI, and the Component Model by the Bytecode Alliance
License: Apache-2.0 with LLVM-exception
Group: Development/Tools
Url: https://wasmtime.dev/
Vcs: https://github.com/bytecodealliance/wasmtime

BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: elfutils
# for cpp.req on the C++ API headers
BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-rust

Requires: %name-common = %EVR

Source0: %name-%version.tar
Patch0: c-api-soname.patch

%description
Wasmtime is a standalone runtime for WebAssembly, WASI, and the
Component Model by the Bytecode Alliance. It allows you to run
WebAssembly code in a sandboxed environment, which is important for
security.

%package common
Summary: Wasmtime common files
Group: Other
BuildArch: noarch

%description common
This subpackage contains the license for the Wasmtime library and program.

%package docs
Summary: Documentation for Wasmtime
Group: Documentation
BuildArch: noarch
Requires: %name-common = %EVR

%description docs
Documentation for Wasmtime.

%package examples
Summary: Wasmtime examples
Group: Development/Documentation
BuildArch: noarch
Requires: %name-common = %EVR

%description examples
This package contains examples of how to use the Wasmtime API to
create applications. The examples are organized by topic, such as
WASM, WASI, and Component Model.

%package -n lib%name%soversion
Summary: Shared library to develop with Wasmtime
Group: System/Libraries
Requires: %name-common = %EVR
Provides: lib%name = %EVR
Obsoletes: lib%name < %EVR

%description -n lib%name%soversion
The lib%name%soversion package contains the Wasmtime runtime library,
which provides WebAssembly run time support for the Component Model,
the WASI API, and the Wasmtime API. The library can be used to
embed Wasmtime's runtime in a program.

%package -n lib%name-devel
Summary: Includes and docs to develop with Wasmtime
Group: Development/C
Requires: lib%name%soversion = %EVR

%description -n lib%name-devel
The lib%name-devel package contains the header files and
documentation to develop with the Wasmtime API. The Wasmtime API
provides a way to embed Wasmtime's runtime in a program and to
create applications that take advantage of the Component Model,
the WASI API, and the Wasmtime API.

%package -n lib%name-devel-static
Summary: Static library to develop with Wasmtime
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
The lib%name-devel-static package contains the static library
lib%name.a, which can be used to embed Wasmtime's runtime in a
program. The static library provides all the symbols that are
needed to use the Wasmtime API.

%prep
%setup -q
%autopatch -p1
%rust_prep

%build
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=1 --cfg=rustix_use_libc -Crelocation-model=pic"
export CFLAGS="-O3 -DPIC -fPIC"
export RUST_MIN_STACK=16777216
%rust_build
%rust_build -p %name-c-api
%cmake -S crates/c-api -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build

## Tests are disabled due to the lack of a packaged `wasm32-wasip1` target for rustc
#%check
#cargo test %_smp_mflags --release --no-fail-fast

%install
mkdir -p %buildroot{%_includedir,%_libdir}
install -Dp target/release/%name -t %buildroot%_bindir
install -Dm644 target/release/lib%name.so -T %buildroot%_libdir/lib%name.so.%soversion
ln -s lib%name.so.%soversion %buildroot%_libdir/lib%name.so
install -Dm644 target/release/lib%name.a -t %buildroot%_libdir
cp -r %_target_platform/include/* %buildroot%_includedir
# public C API headers (only generated conf.h is in the cmake build dir)
cd crates/c-api/include
find . \( -name '*.h' -o -name '*.hh' \) -exec cp --parents {} %buildroot%_includedir/ \;
cd -
mkdir -p %buildroot%_datadir/%name/
cp -a examples %buildroot%_datadir/%name/

%files
%_bindir/%name

%files common
%doc LICENSE

%files docs
%doc docs/*

%files examples
%dir %_datadir/%name
%_datadir/%name/examples/

%files -n lib%name%soversion
%_libdir/lib%name.so.%soversion

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so

%files -n lib%name-devel-static
%_libdir/lib%name.a

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 49.0.3-alt1
- new version 49.0.3
- exclude i586 build (rustc runs out of memory on 32-bit)
- build libwasmtime with SONAME libwasmtime.so.49 and package it as libwasmtime49
  according to Shared Libs Policy (closes: #55586)
- add common (license) and docs subpackages, make examples noarch
- use Rust macros (added BuildRequires: rpm-macros-rust),
  fix License (Apache-2.0 with LLVM-exception)
- added BuildRequires: gcc-c++ (cpp.req for the C++ API headers)
- package C API headers in libwasmtime-devel (only conf.h was packaged)
- based on the work of Korney Gedert (thanks to kiper@)
- security fixes:
  + CVE-2026-34941, GHSA-hx6p-xpx3-jvvv: fix heap OOB read in UTF-16 to latin1+utf16 string transcoding.
  + CVE-2026-34942, GHSA-jxhv-7h78-9775: fix panic when transcoding misaligned utf-16 strings.
  + CVE-2026-34943, GHSA-m758-wjhj-p3jq: fix panic when lifting flags component value.
  + CVE-2026-34944, GHSA-qqfj-4vcm-26hv: fix segfault or out-of-sandbox load with f64x2.splat on x86-64.
  + CVE-2026-34945, GHSA-m9w2-8782-2946: fix host data leakage with 64-bit tables and Winch.
  + CVE-2026-34946, GHSA-q49f-xg75-m9xw: fix host panic when Winch executes table.fill.
  + CVE-2026-34971, GHSA-jhxm-h53p-jm7w: fix miscompiled guest heap access (sandbox escape) on aarch64 Cranelift.
  + CVE-2026-34983, GHSA-hfr4-7c6c-48w2: fix use-after-free after cloning wasmtime::Linker.
  + CVE-2026-34987, GHSA-xx5w-cvp6-jv83: fix sandbox-escaping memory access with Winch on aarch64.
  + CVE-2026-34988, GHSA-6wgr-89rj-399p: fix data leakage between pooling allocator instances.
  + CVE-2026-35186, GHSA-f984-pcp8-v2p7: fix improperly masked table.grow return value with Winch.
  + CVE-2026-35195, GHSA-394w-hwhg-8vgm: fix out-of-bounds write or crash when transcoding component model strings.
  + CVE-2026-44216, GHSA-p8xm-42r7-89xg: fix panic when allocating a table exceeding host address space.
  + GHSA-32h6-97mm-8q3c: fix stack buffer overflow from unvalidated async-lifted callback result count.
  + GHSA-hgjw-h833-99q9: fix stores mixing up type indices between engines.
  + GHSA-jqpg-j7w6-42pr: fix dynamic record lifting allocating beyond hostcall fuel limit.
  + GHSA-q554-3cjc-rx7p: fix component-model handle tables not charged to any limit.
  + GHSA-vcg5-q8m5-8379: fix async-entrypoint requirement enforcement.
  + GHSA-vqjp-4c8c-hfgg: fix filesystem sandbox escape via trailing slashes in paths or symlinks.
  + GHSA-wjc8-633q-pwxr: fix stack overflow dropping a long chain of recursive types.

* Sat Apr 04 2026 Vitaly Lipatov <lav@altlinux.ru> 43.0.0-alt1
- new version 43.0.0
- (GHSA-hc7m-r6v8-hg9q, CVE-2025-64345) SECURITY: fix in versions 36-38
- (GHSA-4h67-722j-5pmc, CVE-2025-62711) SECURITY: fix in v38.0.3
- (GHSA-xjhv-v822-pf94) SECURITY: fix in v40.0.4/v41.0.4
- (GHSA-852m-cvvp-9p4w) SECURITY: fix in v42.0.0
- (GHSA-243v-98vx-264h) SECURITY: fix in v42.0.0

* Mon Jul 28 2025 Korney Gedert <kiper@altlinux.org> 35.0.0-alt1
- New version 35.0.0.
- fix: wasmtime-examples=34.0.1-alt1 post-install unowned files

* Mon Jun 30 2025 Korney Gedert <kiper@altlinux.org> 34.0.1-alt1
- Initial release
