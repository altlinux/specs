%define llvm_version 18.1
%define optflags_lto %nil
%define sover 111

%def_with bootstrap

%if_with bootstrap
%def_without check
%endif

Name: ldc
Version: 1.41.0
Release: alt1
Summary: The LLVM-based D Compiler
License: BSD-3-Clause and BSL-1.0 and Apache-2.0
Group: Development/Other
Url: https://github.com/ldc-developers/ldc
VCS: https://github.com/ldc-developers/ldc

Source0: %name-%version.tar
Source1: phobos-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
%if_with bootstrap
BuildRequires: gdmd
%else
BuildRequires: ldc ldc-devel
%endif
BuildRequires: llvm%llvm_version-devel
BuildRequires: zlib-devel
BuildRequires: libcurl-devel
BuildRequires: libedit-devel
BuildRequires: bash-completion
%if_with check
BuildRequires: ctest
BuildRequires: /proc
%endif

%description
LDC is a portable compiler for the D programming language with modern
optimization and code generation capabilities. The compiler uses the
official DMD frontend to support the latest version of D2, and relies
on the LLVM Core libraries for code generation.

%package devel
Summary: Development files for LDC
Group: Development/Other
Requires: %name = %EVR
Requires: libphobos2-ldc-devel = %EVR

%description devel
Development files for programs using LDC.

%package -n libdruntime-ldc%sover
Summary: D runtime library (druntime) built with LDC
Group: System/Libraries

%description -n libdruntime-ldc%sover
D runtime library (druntime) shared library built with the LDC compiler.

%package -n libdruntime-ldc-debug%sover
Summary: D runtime library (druntime) debug build
Group: System/Libraries

%description -n libdruntime-ldc-debug%sover
D runtime library (druntime) shared library, debug build.

%package -n libphobos2-ldc%sover
Summary: D standard library (Phobos) built with LDC
Group: System/Libraries

%description -n libphobos2-ldc%sover
D standard library (Phobos) shared library built with the LDC compiler.

%package -n libphobos2-ldc-debug%sover
Summary: D standard library (Phobos) debug build
Group: System/Libraries

%description -n libphobos2-ldc-debug%sover
D standard library (Phobos) shared library, debug build.

%package -n libldc-jit%sover
Summary: LDC JIT shared library
Group: System/Libraries

%description -n libldc-jit%sover
LDC just-in-time compilation shared library.

%package -n libphobos2-ldc-devel
Summary: Development files for D runtime and Phobos (LDC)
Group: Development/Other
Requires: libdruntime-ldc%sover = %EVR
Requires: libphobos2-ldc%sover = %EVR
Requires: libldc-jit%sover = %EVR

%description -n libphobos2-ldc-devel
Static libraries and symlinks for D runtime and Phobos standard library,
for use with the LDC compiler.

%prep
%setup -a1
rmdir runtime/phobos
mv phobos-%version runtime/phobos

%build
%cmake \
    -DMULTILIB=OFF \
    -DLLVM_ROOT_DIR=%_prefix/lib/llvm-%llvm_version \
%if_with bootstrap
    -DD_COMPILER=gdmd \
%else
    -DD_COMPILER=ldmd2 \
%endif
    -DPHOBOS_SYSTEM_ZLIB=ON \
    %nil

%cmake_build

%install
%cmake_install

%check
# LDC frontend unit tests
%cmake_build --target ldc2-unittest
%_cmake__builddir/bin/ldc2-unittest --version

# DMD-compatible testsuite (runnable tests, release mode)
%cmake_build --target build-run-dmd-testsuite
ctest --test-dir %_cmake__builddir --output-on-failure \
    -R "dmd-testsuite$" --timeout 600


%files
%doc README.md LICENSE CHANGELOG.md
%_bindir/ldc2
%_bindir/ldmd2
%_bindir/ldc-build-runtime
%_bindir/ldc-build-plugin
%_bindir/ldc-profdata
%_bindir/ldc-profgen
%_bindir/ldc-prune-cache
%_bindir/timetrace2txt
%_sysconfdir/ldc2.conf
%_datadir/bash-completion/completions/*

%files -n libdruntime-ldc%sover
%_libdir/libdruntime-ldc-shared.so.%sover
%_libdir/libdruntime-ldc-shared.so.%sover.*

%files -n libdruntime-ldc-debug%sover
%_libdir/libdruntime-ldc-debug-shared.so.%sover
%_libdir/libdruntime-ldc-debug-shared.so.%sover.*

%files -n libphobos2-ldc%sover
%_libdir/libphobos2-ldc-shared.so.%sover
%_libdir/libphobos2-ldc-shared.so.%sover.*

%files -n libphobos2-ldc-debug%sover
%_libdir/libphobos2-ldc-debug-shared.so.%sover
%_libdir/libphobos2-ldc-debug-shared.so.%sover.*

%files -n libldc-jit%sover
%_libdir/libldc-jit.so.%sover
%_libdir/libldc-jit.so.%sover.*

%files -n libphobos2-ldc-devel
%_libdir/libdruntime-ldc.a
%_libdir/libdruntime-ldc-debug.a
%_libdir/libphobos2-ldc.a
%_libdir/libphobos2-ldc-debug.a
%_libdir/libldc-jit-rt.a
%_libdir/libdruntime-ldc-shared.so
%_libdir/libdruntime-ldc-debug-shared.so
%_libdir/libphobos2-ldc-shared.so
%_libdir/libphobos2-ldc-debug-shared.so
%_libdir/libldc-jit.so
%_libdir/ldc_rt.dso.o

%files devel
%_includedir/core/
%_includedir/etc/
%_includedir/std/
%_includedir/ldc/
%_includedir/object.d
%_includedir/__importc_builtins.di
%_includedir/importc.h

%changelog
* Thu Feb 19 2026 Anton Farygin <rider@altlinux.org> 1.41.0-alt1
- initial build for ALT Linux
