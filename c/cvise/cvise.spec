Name: cvise
Version: 2.4.0
Release: alt1

Summary: Super-parallel Python port of the C-Reduce

License: BSD-3-Clause
Group: Development/C++
Url: https://github.com/marxin/cvise

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/marxin/cvise/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: astyle
BuildRequires: clang-devel
# https://bugzilla.altlinux.org/show_bug.cgi?id=39734

%ifarch %e2k
BuildRequires: llvm-devel-static clang-devel-static
%else
# rpm-build-info gives _distro_version
%if %_vendor == "alt" && %_distro_version == "Sisyphus"
BuildRequires: clang11.0-tools clangd11.0
%endif
# FIXME
BuildRequires: llvm-devel >= 10
BuildRequires: llvm-devel-static >= 10
BuildRequires: clang-devel-static >= 10
%endif

BuildRequires: cmake ctest
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: indent
BuildRequires: libncurses-devel
BuildRequires: zlib-devel
#BuildRequires: ninja

BuildRequires: python3-module-pebble
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pytest python3-module-pytest-flake8
BuildRequires: python3-module-pytest-shutil python3-module-pytest-xdist python3-module-pytest-cov
BuildRequires: unifdef
#BuildRequires: pytest3


BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.1.5

# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 3000


%add_python3_lib_path %_datadir/cvise

Requires: astyle
Requires: clang
Requires: indent
Requires: llvm
Requires: unifdef

#AutoProv: no

%description
C-Vise is a super-parallel Python port of the C-Reduce. The port is fully
compatible to the C-Reduce and uses the same efficient
LLVM-based C/C++ reduction tool named clang_delta.

C-Vise is a tool that takes a large C, C++ or OpenCL program that
has a property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ or OpenCL program that
has the same property. It is intended for use by people who discover
and report bugs in compilers and other tools that process C/C++ or OpenCL code.

%prep
%setup
# TODO: https://bugzilla.altlinux.org/show_bug.cgi?id=38660
#__subst '14ilist(APPEND CMAKE_PREFIX_PATH "/usr/share/cmake/Modules")' CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir
%cmake_build

%check
# run ctest -> python3 -m pytest
#make -C BUILD test

%install
%cmake_install
rm -rfv %buildroot%_datadir/cvise/tests/


%files
%doc COPYING
%_bindir/cvise
%_bindir/cvise-delta
%_datadir/cvise/
%dir %_libexecdir/cvise/
%_libexecdir/cvise/clex
%_libexecdir/cvise/clang_delta
%_libexecdir/cvise/strlex
%_libexecdir/cvise/topformflat

%changelog
* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version 2.4.0 (with rpmrb script)

* Wed Sep 01 2021 Michael Shigorin <mike@altlinux.org> 2.3.0-alt1.1
- build on e2k too (llvm9 for now)
- add missing BR: zlib-devel

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.0.0-alt2.1
- NMU: spec: adapted to new cmake macros.

* Fri Feb 26 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- add temp. BR to build with clang 11

* Mon Nov 16 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)
- temp. disable tests (need rewrite run)

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt2
- disable python modules provide, drop tests files from the package

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Tue Jul 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Tue Jun 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Sisyphus
