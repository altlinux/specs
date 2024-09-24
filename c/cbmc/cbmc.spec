# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# 831M and regression/libcprover-cpp/call_bmc.cpp does not even compile.
%define with_devel 0

Name: cbmc
Version: 6.3.1
Release: alt1
Summary: C Bounded Model Checker
License: BSD-4-Clause
Group: Development/C
Url: https://www.cprover.org/cbmc/
Vcs: https://github.com/diffblue/cbmc

Source: %name-%version.tar
Source1: java-models-library-0.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: libglpk-devel
BuildRequires: libcadical-devel-static
BuildRequires: ninja-build
BuildRequires: rpm-build-python3
BuildRequires: zlib-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: ctest
BuildRequires: perl-Term-ANSIColor
}}

%description
CBMC is a Bounded Model Checker for C and C++ programs. It supports C89,
C99, most of C11 and most compiler extensions provided by gcc and Visual
Studio. It also supports SystemC using Scoot. It allows verifying array
bounds (buffer overflows), pointer safety, exceptions and user-specified
assertions. Furthermore, it can check C and C++ for consistency with
other languages, such as Verilog. The verification is performed by
unwinding the loops in the program and passing the resulting equation
to a decision procedure.

         OOOOOOOOO
      OOO  .   .  OOO
     OO     \ /  OOOOO
    OO    `/ ! OOO   OO
    OO    | :OOO|    OO
    OO   ~|OOO: |~   OO
     OO  OOO_:_/ \  OO
      OOOO        OOO
        OOOOOOOOOOO

%package -n libcprover-devel
Summary: CProver C++ API
Group: Development/C++
Requires: %name = %EVR

%description -n libcprover-devel
Interface and the implementation of a new C++-based API for the CProver
libraries.

%prep
%setup
tar xf %SOURCE1 -C jbmc/lib

%build
# Fedora suggests to disable LTO.
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS) -DMINISAT_CONSTANTS_AS_MACROS -Wno-error=odr
%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse
sed -i '/^CC=/s/=.*/="$1 -msse2 -mfpmath=sse"/' src/ansi-c/library_check.sh
%endif
sed -i '/GIT_INFO/s/n\/a/%release%{?disttag::%disttag}/' src/util/CMakeLists.txt
%cmake \
	-DWITH_JBMC:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-Dsat_impl="system-cadical" \
	%nil
%cmake_build

%install
%cmake_install
# Fix misinstalls.
install -Dpm644 %buildroot/usr/etc/bash_completion.d/cbmc %buildroot%_datadir/bash-completion/completions/cbmc
rm %buildroot/usr/etc/bash_completion.d/cbmc
%if !%with_devel
rm %buildroot%_libdir/libcprover.*.a
rm -rf %buildroot%_includedir/cprover
%endif

%check
%_cmake__builddir/bin/cbmc --version
%_cmake__builddir/bin/cbmc --version |& grep -wF '%version'
%if 0
# 84% tests passed, 12 tests failed out of 75
%ctest --label-regex CORE
%endif

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md CHANGELOG TOOLS_OVERVIEW.md
%_bindir/cbmc
%_bindir/cprover
%_bindir/crangler
%_bindir/goto-*
%_bindir/symtab2gb
%_bindir/ls_parse.py
%_datadir/bash-completion/completions/cbmc
%_man1dir/*.1*

%if %with_devel
%files -n libcprover-devel
%_includedir/cprover
%_libdir/libcprover.*.a
%endif

%changelog
* Tue Sep 24 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 6.3.1-alt1
- Update to cbmc-6.3.1 (thx vt@).

* Tue Jul 30 2024 Vitaly Chikunov <vt@altlinux.org> 6.1.1-alt1
- Update to cbmc-6.1.1 (2024-07-29).

* Thu Jul 18 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 6.0.1-alt1
- Update to upstream 6.0.1 (thx vt@).

* Sun Mar 03 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 5.95.1-alt2
- Rebuilt with system cadical

* Sat Nov 25 2023 Vitaly Chikunov <vt@altlinux.org> 5.95.1-alt1
- Experimental build cbmc-5.95.1 (2023-10-30).
  Warning: This is so experimental that not all tests are passed.
