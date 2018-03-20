%global v_major 4.0
%global llvm_svnrel %nil
%global clang_svnrel %nil
%global rel alt3
%global llvm_name llvm%v_major
%global clang_name clang%v_major

%ifndef build_parallel_jobs
%global build_parallel_jobs 8
%endif

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')

%def_disable tests
%def_disable static
%def_enable compat

Name: %llvm_name
Version: 4.0.1
Release: %rel.rel
Summary: The Low Level Virtual Machine

Group: Development/C
License: NCSA
Url: http://llvm.org
Source0: http://llvm.org/releases/%version/llvm-%version.tar
Source1: http://llvm.org/releases/%version/clang-%version.tar
Patch1: alt-triple.patch
Patch2: alt-i586-fallback.patch
Patch3: alt-llvm-no-proc-fix.patch
Patch4: alt-cmake-path.patch
Patch5: llvm-alt-fix-linking.patch

BuildPreReq: /proc

BuildRequires(pre): cmake >= 3.4.3
BuildRequires: chrpath libstdc++-devel libffi-devel perl-Pod-Parser perl-devel
BuildRequires: python-modules-compiler python-modules-unittest python-modules-xml
BuildRequires: python-modules-json zip zlib-devel gcc-c++
BuildRequires: python-module-sphinx-devel binutils-devel ninja-build


Provides: llvm = %EVR
Obsoletes: llvm <= 3.8.0

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary
programming languages. The compiler infrastructure includes mirror sets
of programming tools as well as libraries with equivalent functionality.

%package devel
Group: Development/C
Summary: Libraries and header files for LLVM
Provides: llvm-devel = %EVR
Obsoletes: llvm-devel <= 3.8.0
Requires: %name = %EVR

%description devel
This package contains library and header files needed to develop new
native programs that use the LLVM infrastructure.

%package devel-static
Summary: Static libraries for LLVM
Group: Development/C
Provides: llvm-devel-static = %EVR
Obsoletes: llvm-devel-static <= 3.8.0
Requires: %name-devel = %EVR

%description devel-static
This package contains static libraries needed to develop new
native programs that use the LLVM infrastructure.

%package libs
Group: Development/C
Summary: LLVM shared libraries

%description libs
Shared libraries for the LLVM compiler infrastructure.

%package doc
Summary: Documentation for LLVM
Group: Documentation
BuildArch: noarch
Provides: llvm-doc = %EVR
Obsoletes: llvm-doc <= 3.8.0

%description doc
Documentation for the LLVM compiler infrastructure.

%package -n %clang_name
Summary: A C language family frontend for LLVM
License: NCSA
Group: Development/C
Requires: gcc
Provides: clang = %EVR
Obsoletes: clang <= 3.8.0

%description -n %clang_name
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

%package -n %clang_name-libs
Group: Development/C
Summary: clang shared libraries
Obsoletes: %clang_name <= 4.0.1-alt1.3.rel

%description -n %clang_name-libs
Shared libraries for the clang compiler.

%package -n %clang_name-devel
Summary: Header files for clang
Group: Development/C
Provides: clang-devel = %EVR
Obsoletes: clang-devel <= 3.8.0
Requires: %clang_name = %EVR

%description -n %clang_name-devel
This package contains header files for the Clang compiler.

%package -n %clang_name-devel-static
Summary: Static libraries for clang
Group: Development/C
Provides: clang-devel-static = %EVR
Obsoletes: clang-devel-static <= 3.8.0
Requires: %clang_name = %EVR

%description -n %clang_name-devel-static
This package contains static libraries for the Clang compiler.

%package -n %clang_name-analyzer
Summary: A source code analysis framework
License: NCSA
Group: Development/C
BuildArch: noarch
Provides: clang-analyzer = %EVR
Obsoletes: clang-analyzer <= 3.8.0
Requires: %clang_name = %EVR

%description -n %clang_name-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package -n %clang_name-doc
Summary: Documentation for Clang
Group: Documentation
BuildArch: noarch
Provides: clang-doc = %EVR
Obsoletes: clang-doc <= 3.8.0

%description -n %clang_name-doc
Documentation for the Clang compiler front-end.

%prep
%setup -n llvm-%version -a1
mv clang-%version tools/clang
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
# force off shared libs as cmake macros turns it on.
%cmake -G Ninja \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_SHARED_LINKER_FLAGS="-Wl,-Bsymbolic" \
	-DLLVM_TARGETS_TO_BUILD="host;AMDGPU;BPF;" \
	-DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD='AVR' \
	-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
	-DLLVM_ENABLE_ZLIB:BOOL=ON \
	-DLLVM_ENABLE_FFI:BOOL=ON \
	-DLLVM_ENABLE_RTTI:BOOL=ON \
	-DLLVM_OPTIMIZED_TABLEGEN:BOOL=ON \
	-DLLVM_BINUTILS_INCDIR="%_includedir/bfd" \
	\
	%if "%_lib" == "lib64"
	-DLLVM_LIBDIR_SUFFIX="64" \
	%else
	-DLLVM_LIBDIR_SUFFIX="" \
	%endif
	-DLLVM_BUILD_RUNTIME:BOOL=ON \
	\
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \
	-DLLVM_BUILD_TOOLS:BOOL=ON \
	\
	%if_enabled tests
	-DLLVM_INCLUDE_TESTS:BOOL=ON \
	-DLLVM_BUILD_TESTS:BOOL=ON \
	%endif
	\
	-DLLVM_INCLUDE_EXAMPLES:BOOL=ON \
	-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
	\
	-DLLVM_INCLUDE_UTILS:BOOL=ON \
	-DLLVM_INSTALL_UTILS:BOOL=OFF \
	\
	-DLLVM_INCLUDE_DOCS:BOOL=ON \
	-DLLVM_BUILD_DOCS:BOOL=ON \
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DSPHINX_WARNINGS_AS_ERRORS:BOOL=OFF \
	-DLLVM_ENABLE_DOXYGEN:BOOL=OFF \
	-DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
	-DLLVM_DYLIB_EXPORT_ALL:BOOL=ON \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_BUILD_EXTERNAL_COMPILER_RT:BOOL=ON \
	-DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF

ninja \
       -vvv \
       -j %build_parallel_jobs \
       -C BUILD

%install
pushd BUILD
cmake -DCMAKE_INSTALL_PREFIX=%buildroot%prefix ../
popd
ninja -C BUILD install

# And prepare Clang documentation
rm -rf BUILD/clang-docs
mkdir -p BUILD/clang-docs
for f in LICENSE.TXT NOTES.txt README.txt; do
  ln tools/clang/$f BUILD/clang-docs/
done
rm -rf tools/clang/docs/{doxygen*,Makefile*,*.graffle,tools}

file %buildroot%_bindir/* | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d
file %buildroot%_libdir/*.so | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d

%check
%if_enabled tests
LD_LIBRARY_PATH=%buildroot%_libdir:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
ninja -C BUILD check-all || :
%endif

%if_disabled compat
%files
%doc CREDITS.TXT LICENSE.TXT README.txt
%_bindir/*
%_man1dir/*
%exclude %_bindir/llvm-config*
%exclude %_bindir/*clang*
%exclude %_bindir/c-index-test
%exclude %_bindir/scan-*
%exclude %_man1dir/llvm-config.1.*
%exclude %_man1dir/clang.1*
%exclude %_man1dir/scan-build.1*

%files devel
%_bindir/llvm-config
%_man1dir/llvm-config.1.*
%_includedir/llvm
%_includedir/llvm-c
%_libdir/libLLVM.so
%_libdir/libLTO.so
%_libdir/LLVMHello.so
%_libdir/LLVMgold.so
%_libdir/BugpointPasses.so
%exclude %_libdir/libclang.so
%_datadir/cmake/Modules/llvm

#%%if_enabled static
#%%files devel-static
#%%_libdir/*.a
#%%exclude %_libdir/libclang*.a
#%%endif

%files doc
%doc %_docdir/llvm

%files -n %clang_name
%doc BUILD/clang-docs/*
%_bindir/*clang*
%_bindir/c-index-test
%_libdir/clang
%_man1dir/clang.1*

%files -n %clang_name-devel
%_includedir/clang
%_includedir/clang-c
%_libdir/libclang.so
%_datadir/cmake/Modules/clang

#%%if_enabled static
#%%files -n %clang_name-devel-static
#%%_libdir/libclang*.a
#%%endif

%files -n %clang_name-analyzer
%_prefix/libexec/*-analyzer
%_bindir/scan-build
%_bindir/scan-view
%_datadir/scan-build
%_datadir/scan-view
%_man1dir/scan-build.1*

%files -n %clang_name-doc
%doc %_docdir/clang
%endif # compat

%files -n %clang_name-libs
%_libdir/libclang.so.*

%files libs
%_libdir/libLLVM-*.so
%_libdir/libLTO.so.*

%changelog
* Tue Mar 20 2018 L.A. Kostis <lakostis@altlinux.ru> 4.0.1-alt3.rel
- .spec cleanups:
  + don't pack llvm,clang and -devel for compat build.
  + move clang libs to separate pkg.
  + use macros for versioning.

* Mon Mar 19 2018 L.A. Kostis <lakostis@altlinux.ru> 4.0.1-alt2.1.rel
- Disable debuginfo verbosity for x86_64.
- Use 'Release' as build target.

* Mon Mar 19 2018 L.A. Kostis <lakostis@altlinux.ru> 4.0.1-alt2.rel
- Prepare for llvm6.0:
  + Enable compat flag (to coexists with other llvms).
  + Don't pack clang.
  + Don't pack -static libs.
- Build time improvements:
  + Use fixed number of build jobs.
  + Use ninja build.
  + Disable debuginfo verbosity on i586 (reduces memory consumption).
- Move LLVMgold.so to -devel package (closes #34662).

* Sun Feb 04 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.1-alt1.3.rel
- Replaced X86 with native in the list of targets.
- Added provides and obsoletes to replace old llvm packages and its
  subpackages.

* Thu Oct 19 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1.2.rel
- NMU: changed CMake Modules install path

* Thu Sep 14 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.1-alt1.1.rel
- remove conflicts: llvm from -libs pkg (closes #33879).

* Sun Sep 10 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.1-alt1.rel
- Updated 4.0.0 release and build configuration:
  + Enabled AVR experimental target.

* Thu Sep 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt2.rel
- Installed example llvm plugins required by cmake modules.

* Sun Mar 19 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt1.rel
- Define cmake modules dir correctly (closes #33250).

* Mon Mar 13 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.9.rel
- Updated 4.0.0 release.

* Thu Dec 29 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.6.r290127
- Enabled gold plugin.

* Wed Dec 28 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.5.r290127
- Renamed clang to clang4.0 (to coexist with 3.x clang).

* Sun Dec 25 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.4.r290127
- repackage clang-analyzer, now with proper dirs.

* Thu Dec 22 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.3.r290127
- llvm: Fix segfault in libLLVM due missing /proc/cpuinfo.
- .spec: fix libs intersections between llvm and clang.
- .spec: remove unsupported stuff from clang-analyzer.

* Wed Dec 21 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.2.r290127
- Update build configuration:
  + Enabled BPF target.
  + Enabled optimisation.
  + Disabled unconditionally enabled tests.

* Mon Dec 19 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r290127
- Updated LLVM to SVN r290127.
- Enabled clang (SVN r290130).

* Tue Nov 08 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r286177
- Updated to SVN r286177.

* Fri Sep 30 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r282877
- Updated to SVN r282877.

* Fri Aug 05 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r277804
- Updated to SVN r277804.

* Sat Jun 25 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r273782
- Updated to SVN r273782.

* Wed Jun 15 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r272815
- Updated to SVN r272815.
- Enabled X86 target (for llvmpipe).

* Sun Jun 12 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r272517
- build as separate lib for Mesa-dev.

* Thu Jun 02 2016 Rudolf Kastl <rkastl@redhat.com> 3.9.0-0.1.r
- using a random svn checkout of 3.9
- removed CppBackend
- updated files section

* Thu Mar 10 2016 Dave Airlie <airlied@redhat.com> 3.8.0-1
- llvm 3.8.0 release

* Wed Mar 09 2016 Dan Horák <dan[at][danny.cz> 3.8.0-0.3
- install back memory consumption workaround for s390

* Thu Mar 03 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.2
- llvm 3.8.0 rc3 release

* Fri Feb 19 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.1
- llvm 3.8.0 rc2 release

* Tue Feb 16 2016 Dan Horák <dan[at][danny.cz> 3.7.1-7
- recognize s390 as SystemZ when configuring build

* Sat Feb 13 2016 Dave Airlie <airlied@redhat.com> 3.7.1-6
- export C++ API for mesa.

* Sat Feb 13 2016 Dave Airlie <airlied@redhat.com> 3.7.1-5
- reintroduce llvm-static, clang needs it currently.

* Fri Feb 12 2016 Dave Airlie <airlied@redhat.com> 3.7.1-4
- jump back to single llvm library, the split libs aren't working very well.

* Fri Feb 05 2016 Dave Airlie <airlied@redhat.com> 3.7.1-3
- add missing obsoletes (#1303497)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.1-1
- new upstream release
- enable gold linker

* Wed Nov 04 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- fix Requires for subpackages on the main package

* Tue Oct 06 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- initial version using cmake build system
