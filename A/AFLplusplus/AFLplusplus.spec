%define _unpackaged_files_terminate_build 1

# use at least llvm 15
%if %(printf %%.0f %_llvm_version) < 15
%global _llvm_version 15.0
%endif

Name: AFLplusplus
Version: 5.02c
Release: alt1

Summary: American Fuzzy Lop plus plus (AFL++)
License: AGPL-3.0-or-later and Apache-2.0
Group: Development/Tools
VCS: https://github.com/AFLplusplus/AFLplusplus
Url: https://aflplus.plus

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Provides: afl++ = %EVR

Provides: afl = %EVR
Obsoletes: afl < %EVR

Requires: clang%_llvm_version lld%_llvm_version

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-llvm-common

BuildRequires: python3-dev
BuildRequires: gcc-c++ gcc-plugin-devel
BuildRequires: zlib-devel
BuildRequires: llvm%_llvm_version llvm%_llvm_version-devel
BuildRequires: clang%_llvm_version lld%_llvm_version

%add_verify_elf_skiplist %_libexecdir/afl/*

%add_verify_elf_skiplist %_datadir/afl/testcases/archives/common/ar/small_archive.a
%add_verify_elf_skiplist %_datadir/afl/testcases/others/elf/small_exec.elf

%add_findreq_skiplist %_datadir/afl/custom_mutators/*/*.py
%add_findreq_skiplist %_datadir/afl/custom_mutators/*/*/*.py

%add_findreq_skiplist %_datadir/afl/utils/distributed_fuzzing/sync_script.sh

%filter_from_requires /^opendoas$/d
%filter_from_requires /^afl-plot-ui$/d

%ifarch %ix86
%filter_from_requires /^\/usr\/bin\/afl-c++$/d
%filter_from_requires /^\/usr\/lib\/afl\/afl-compiler-rt.o$/d
%endif

AutoProv: no

%description
The fuzzer afl++ is afl with community patches, qemu 5.1 upgrade,
collision-free coverage, enhanced laf-intel & redqueen, AFLfast++
power schedules, MOpt mutators, unicorn_mode, and a lot more!

Built without qemu_mode, unicorn_mode and nyx_mode

%prep
%setup
%patch0 -p1

# preserve utils for later installation
cp -a utils utils.orig
find ./utils.orig -type f -exec chmod -x {} \;

%build
export ALTWRAP_LLVM_VERSION=%_llvm_version
export CC=clang
export CXX=clang++
export LD=ld.lld
export AR=llvm-ar
export NM=llvm-nm
export RANLIB=llvm-ranlib
export LLVM_CONFIG=llvm-config

# Compile with AFL_PERSISTENT_RECORD support
export CFLAGS="$CFLAGS -DAFL_PERSISTENT_RECORD"

export CFLAGS="$CFLAGS %optflags"
export CXXFLAGS="$CFLAGS"

%make_build PREFIX=%prefix NO_NYX=1 source-only

if ! test -e SanitizerCoverageLTO.so 2>&1 ; then
    echo "FATAL: AFL LLVM LTO mode build failed" >&2
    exit 1
fi

%install
export ALTWRAP_LLVM_VERSION=%_llvm_version
export CC=clang
export CXX=clang++
export LD=ld.lld

%makeinstall_std PREFIX=%prefix

# Install utils
mkdir -pv %buildroot%_datadir/afl
cp -a utils.orig %buildroot%_datadir/afl/utils

# Install utils
cp -a custom_mutators %buildroot%_datadir/afl/custom_mutators

# Install headers
cp -a include %buildroot%_datadir/afl/include

%files
%_bindir/afl-*
%_libexecdir/afl
%_datadir/afl
%_defaultdocdir/afl
%_man8dir/afl-*
%_includedir/afl

%changelog
* Mon Jun 29 2026 Egor Ignatov <egori@altlinux.org> 5.02c-alt1
- New version 5.02c.

* Fri Jun 19 2026 Egor Ignatov <egori@altlinux.org> 5.01c-alt1
- New version 5.01c.

* Thu Jun 04 2026 Egor Ignatov <egori@altlinux.org> 5.00c-alt1
- New version 5.00c.

* Thu Mar 19 2026 Egor Ignatov <egori@altlinux.org> 4.40c-alt1
- New version 4.40c.

* Thu Oct 02 2025 Egor Ignatov <egori@altlinux.org> 4.34c-alt1
- 4.34c

* Mon Jun 30 2025 Egor Ignatov <egori@altlinux.org> 4.33c-alt1
- 4.33c

* Tue May 27 2025 Egor Ignatov <egori@altlinux.org> 4.32c-alt1
- 4.32c
- Drop precompiled utils and custom_mutators.

* Wed Aug 14 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 4.21c-alt3
- Revert performance options: appears to be CPU-specific.

* Wed Aug 14 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 4.21c-alt2
- Build with arch-dependent performance options.

* Fri Aug 02 2024 Andrey Kovalev <ded@altlinux.org> 4.21c-alt1
- 4.21c

* Mon Apr 15 2024 Egor Ignatov <egori@altlinux.org> 4.20c-alt1
- 4.20c

* Wed Feb 07 2024 Egor Ignatov <egori@altlinux.org> 4.10c-alt1
- 4.10c

* Sun Dec 31 2023 Egor Ignatov <egori@altlinux.org> 4.09c-alt1
- 4.09c

* Tue Nov 07 2023 Egor Ignatov <egori@altlinux.org> 4.08c-alt3
- Build with python3 and AFL_PERSISTENT_RECORD support

* Mon Sep 18 2023 Egor Ignatov <egori@altlinux.org> 4.08c-alt2
- Conflicts with afl

* Sun Sep 03 2023 Egor Ignatov <egori@altlinux.org> 4.08c-alt1
- First build for ALT
