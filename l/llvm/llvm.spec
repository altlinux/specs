%def_disable doxygen
# our ocaml runtime is incomplete:
#configure: WARNING: --enable-bindings=ocaml specified, but ctypes is not installed
#configure: WARNING: --enable-bindings=ocaml specified, but OUnit 2 is not installed. Tests will not run
%def_without ocaml

%def_without gccbootstrap
%def_with crt

%define llvm_version 3.8.0
%define clang_version 3.8.0
%define compilerrt_version 3.8.0
%define clangtools_version 3.8.0

%define clang_name cfe

Name: llvm
Version: 3.8.0
Release: alt1
Summary: The Low Level Virtual Machine
Group: Development/C
License: NCSA
Url: http://llvm.org/

Source0: http://llvm.org/releases/%version/llvm-%llvm_version.src.tar.xz
Source1: http://llvm.org/releases/%version/%clang_name-%clang_version.src.tar.xz
Source2: http://llvm.org/releases/%version/compiler-rt-%clangtools_version.src.tar.xz
Source3: http://llvm.org/releases/%version/clang-tools-extra-%clangtools_version.src.tar.xz

Patch1: llvm+clang-3.8.0-alt-add-alt-triple.patch
Patch2: llvm+clang-3.3-alt-arm-default-to-hardfloat.patch
# Don't run gcc for ada files
Patch3: clang-disable-ada-extension.patch
# Use i586 as default target for 32bit
Patch4: default-to-i586.patch
Patch5: llvm-fix-find-gcc5-install.patch
Patch6: llvm-remove-clang-only-flags.patch
Patch7: cmake-host-triple.patch

%if_with crt
BuildPreReq: /proc
%endif

%if_with gccbootstrap
BuildRequires: gcc-c++
%else
BuildRequires: clang gcc gcc-c++
%endif

# Automatically added by buildreq on Thu Aug 29 2013 (-ba)
# optimized out: elfutils gnu-config groff-base libstdc++-devel llvm ocaml4 ocaml4-runtime perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Term-ANSIColor perl-podlators python-base python-modules rpm-build-ocaml4 tcl
BuildRequires: chrpath dejagnu libstdc++-devel groff-extra groff-ps libffi-devel perl-Pod-Parser perl-devel python-modules-compiler python-modules-unittest python-modules-xml python-modules-json zip

%if_with ocaml
BuildRequires: ocaml4-ocamldoc ocaml4 ocaml4-ocamlfind-mini
%endif

%if_enabled doxygen
BuildRequires: doxygen graphviz fonts-ttf-dejavu
%endif

%description
LLVM is a compiler infrastructure designed for compile-time,
link-time, runtime, and idle-time optimization of programs from
arbitrary programming languages.  The compiler infrastructure includes
mirror sets of programming tools as well as libraries with equivalent
functionality.

%package devel
Summary: Libraries and header files for LLVM
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains library and header files needed to develop new
native programs that use the LLVM infrastructure.

%package devel-static
Summary: Static libraries for LLVM
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static libraries needed to develop new
native programs that use the LLVM infrastructure.

%package doc
Summary: Documentation for LLVM
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description doc
Documentation for the LLVM compiler infrastructure.

%package -n clang
Summary: A C language family frontend for LLVM
License: NCSA
Group: Development/C
Requires: gcc

%description -n clang
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

%package -n clang-devel
Summary: Header files for clang
Group: Development/C
Requires: clang = %version-%release

%description -n clang-devel
This package contains header files for the Clang compiler.

%package -n clang-devel-static
Summary: Static libraries for clang
Group: Development/C
Requires: clang = %version-%release

%description -n clang-devel-static
This package contains static libraries for the Clang compiler.

%package -n clang-analyzer
Summary: A source code analysis framework
License: NCSA
Group: Development/C
Requires: clang = %version-%release

%description -n clang-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package -n clang-doc
Summary: Documentation for Clang
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description -n clang-doc
Documentation for the Clang compiler front-end.

%package apidoc
Summary: API documentation for LLVM
Group: Development/C
BuildArch: noarch
Requires: %name-docs = %version-%release

%description apidoc
API documentation for the LLVM compiler infrastructure.

%package -n clang-apidoc
Summary: API documentation for Clang
Group: Development/Languages
BuildArch: noarch
Requires: clang-doc = %version-%release

%description -n clang-apidoc
API documentation for the Clang compiler.

%package ocaml
Summary: OCaml binding for LLVM
Group: Development/Functional
Requires: %name = %version-%release
Requires: ocaml4-runtime

%description ocaml
OCaml binding for LLVM.

%package ocaml-devel
Summary: Development files for %name-ocaml
Group: Development/Functional
Requires: %name-devel = %version-%release
Requires: %name-ocaml = %version-%release
Requires: ocaml4

%description ocaml-devel
The %name-ocaml-devel package contains libraries and signature files
for developing applications that use %name-ocaml.

%package ocaml-devel-static
Summary: Static libraries for %name-ocaml
Group: Development/Functional
Requires: %name-devel = %version-%release
Requires: %name-devel-static = %version-%release
Requires: %name-ocaml = %version-%release
Requires: %name-ocaml-devel = %version-%release

%description ocaml-devel-static
The %name-ocaml-devel-static package contains static libraries
for developing applications that use %name-ocaml.

%package ocaml-doc
Summary: Documentation for LLVM's OCaml binding
Group: Documentation
BuildArch: noarch
Requires: %name-ocaml = %version-%release

%description ocaml-doc
HTML documentation for LLVM's OCaml binding.

%add_python_req_skip AppKit

%prep
%setup -n llvm-%{llvm_version}.src -a1 %{?_with_crt:-a2} -a3
mv %clang_name-%{clang_version}.src tools/clang
mv clang-tools-extra-%{clangtools_version}.src tools/clang/tools/extra
%if_with crt
mv compiler-rt-%{compilerrt_version}.src projects/compiler-rt
%endif

%patch1 -p1
%ifarch armh
%patch2 -p1
%endif

pushd tools/clang
%patch3 -p1
%patch4 -p1
popd
%patch5 -p1

%patch6 -p1
%patch7 -p1

sed -i "s|%{version}svn|%version|g" configure
sed -i 's|/lib /usr/lib $lt_ld_extra|%_libdir $lt_ld_extra|' configure

# build sets DOT_PATH = /usr/bin/dot, but _PATH_ is /usr/bin
find -name doxygen.cfg.in | xargs sed -i 's,\(^DOT_PATH[[:blank:]]*=\).*,\1,'
#sed -i 's/\(OmitFramePointer := \).*/\1/' Makefile.rules

sed -ri "/ifeq.*CompilerTargetArch/s#i386#i586#g" projects/compiler-rt/make/platform/clang_linux.mk

# some strange failing tests
rm tools/clang/test/Driver/{android-standalone,linux-header-search}.cpp

%build
mkdir build
cd build

%if_without gccbootstrap
CC=clang
CXX=clang++
export CC CXX
%endif

%if_with ocaml
OCAMLFIND=/usr/bin/ocamlfind-mini
export OCAMLFIND
%endif

%define  _configure_script ../configure
%define optflags_debug %nil

%configure \
%if_with gccbootstrap
	--with-extra-options="-fno-devirtualize" \
%endif
        --enable-cxx11 \
        --enable-optimized \
        --disable-assertions \
	--disable-werror \
	--disable-profiling \
	--disable-expensive-checks \
        --enable-targets=x86,x86_64,arm,aarch64,cpp,nvptx,r600 \
        --enable-jit \
        --enable-shared \
        --enable-libffi \
%if_with ocaml
	--enable-bindings=ocaml \
%else
	--enable-bindings=none \
%endif
	%{subst_enable doxygen} \
	#

# FIXME file this
# configure does not properly specify libdir
sed -i 's|(PROJ_prefix)/lib|(PROJ_prefix)/%_lib|g' Makefile.config
# llvm-config.cpp hardcodes lib in it
sed -i 's|ActiveLibDir = ActivePrefix + "/lib"|ActiveLibDir = ActivePrefix + "/%_lib"|g' ../tools/llvm-config/llvm-config.cpp

%make_build REQUIRES_RTTI=1 KEEP_SYMBOLS=1 OPTIMIZE_OPTION="%optflags" VERBOSE=1

%if_enabled doxygen
# hack to build docs during %%build, not %%install
for docdir in docs/ tools/clang/docs/; do
	sed -i "\,^doxygen: ,s,regendoc ,," $docdir/Makefile
	make VERBOSE=1 regendoc -C $docdir
	make VERBOSE=1 doxygen -C $docdir
done
%endif

%check
cd build
make check 2>&1 | tee llvm-testlog.txt

pushd tools/clang
make test 2>&1 | tee clang-testlog.txt
popd

%install
cd build

%makeinstall_std KEEP_SYMBOLS=1 VERBOSE=1 PROJ_docsdir=/moredocs

# Static analyzer not installed by default:
# http://clang-analyzer.llvm.org/installation#OtherPlatforms
mkdir -p %buildroot%_libdir/clang-analyzer

pushd ../tools/clang/tools
cp -pr scan-{build,view} %buildroot%_libdir/clang-analyzer/

find %buildroot%_libdir/clang-analyzer/ \( -name '*\.bat' -or -name Makefile -or -name CMakeLists.txt \) -delete

sed -r -i -e 's@\$RealBin/bin/clang@/usr/bin/clang@g' \
	%buildroot%_libdir/clang-analyzer/scan-build/bin/scan-build
mkdir -p %buildroot%_man1dir/
mv %buildroot%_libdir/clang-analyzer/scan-build/man/scan-build.1 %buildroot%_man1dir/
popd

# create launchers
for f in scan-{build,view}; do
  ln -s %_libdir/clang-analyzer/$f/bin/$f %buildroot%_bindir/$f
done

# Move documentation back to build directory
rm -rf moredocs
mv %buildroot/moredocs .
rm -f moredocs/*.tar.gz
rm -f moredocs/ocamldoc/html/*.tar.gz

# and separate the apidoc
%if_enabled doxygen
cp -al moredocs/html/doxygen apidoc
cp -al tools/clang/docs/doxygen/html clang-apidoc
%endif

# And prepare Clang documentation
rm -rf clang-docs
mkdir clang-docs
for f in LICENSE.TXT NOTES.txt README.txt; do
  ln ../tools/clang/$f clang-docs/
done
rm -rf ../tools/clang/docs/{doxygen*,Makefile*,*.graffle,tools}
subst 's|^\(DIRS.*\) docs\(.*\)|\1\2|' ../tools/clang/Makefile

# Get rid of erroneously installed example files.
rm -f %buildroot%_libdir/*LLVMHello.*
rm -f %buildroot%_libdir/*BugpointPasses.*

file %buildroot%_bindir/* | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d
file %buildroot%_libdir/*.so | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d
file %buildroot%_libdir/ocaml/*.so | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d

# remove documentation makefiles:
# they require the build directory to work
find examples -name 'Makefile' -delete

# need for build cmake projects
mkdir -p %buildroot%_datadir/CMake/Modules
install -p -m644 ../cmake/modules/*.cmake %buildroot%_datadir/CMake/Modules
ln -s LLVM-Config.cmake %buildroot%_datadir/CMake/Modules/LLVMConfig.cmake

%files
%doc CREDITS.TXT LICENSE.TXT README.txt build/llvm-testlog.txt
%exclude %_bindir/llvm-config
%_bindir/bugpoint
%_bindir/llc
%_bindir/lli*
%_bindir/llvm*
%_bindir/opt
%_bindir/obj2yaml
%_bindir/yaml2obj
%_bindir/verify-uselistorder
%_bindir/sancov
%_libdir/*.so
%exclude %_libdir/libclang.so
%_man1dir/*.1.*
%exclude %_man1dir/scan-build.1*

%files devel
%_bindir/llvm-config
%_includedir/llvm
%_includedir/llvm-c
%_datadir/CMake/Modules

%files devel-static
%_libdir/*.a
%exclude %_libdir/libclang*.a

%files -n clang
%doc build/clang-docs/* build/tools/clang/clang-testlog.txt
%_bindir/clang*
%_bindir/c-index-test
%_bindir/pp-trace
%prefix/lib/clang
%_libdir/libclang.so

%files -n clang-devel
%_includedir/clang
%_includedir/clang-c

%files -n clang-devel-static
%_libdir/libclang*.a

%files -n clang-analyzer
%_bindir/scan-build
%_bindir/scan-view
%_libdir/clang-analyzer
%_mandir/man1/scan-build.1*

%if_with ocaml
%files ocaml
%_libdir/ocaml/*.cma
%_libdir/ocaml/*.cmi

%files ocaml-devel
%_libdir/ocaml/META.llvm*
%_libdir/ocaml/*.a
%exclude %_libdir/ocaml/libLLVM*.a
%_libdir/ocaml/*.cmx*
%_libdir/ocaml/*.mli
%_libdir/ocaml/dllllvm*.so

%files ocaml-devel-static
%_libdir/ocaml/libLLVM*.a

%files ocaml-doc
%doc build/moredocs/ocamldoc/html/*
%endif

%if_enabled doxygen
%files -n clang-doc
%doc tools/clang/docs

%files doc
%doc examples build/moredocs/html

%files apidoc
%doc build/apidoc

%files -n clang-apidoc
%doc build/clang-apidoc
%endif

%changelog
* Fri Jun 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.8.0-alt1
- Updated to 3.8.0.
- Disabled build with debug symbols.

* Fri Nov 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.7.0-alt1
- Updated to 3.7.0.
- Updated patches (tnx to lakostis@).

* Tue Jun 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.0-alt2
- Fixed clang work with gcc >= 5.
- Built clang-devel-static as separate package.

* Thu Nov 27 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.0-alt1
- Updated to 3.5.0 (ALT: #30435).
- Rebuilt with clang.

* Wed Oct 08 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.4.2-alt1
- New version (bootstrap with gcc).

* Thu Apr 10 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.4-alt2
- clang: add R: gcc (any gcc).

* Thu Jan 09 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.4-alt1
- New version (#29710).
- clang: drop versioned R: gcc.
- Updated ALT triplet patch.
- Packaged symlinks in ocaml-devel-static subpackage.

* Fri Aug 30 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.3-alt2
- Built with clang.
- clang: added versioned R: gcc.
- llvm:
 + Dropped ld.so.conf file.
 + Packaged static libraries in devel-static subpackage.

* Mon Aug 19 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.3-alt1
- New version.

* Tue Apr 23 2013 Dmitry V. Levin <ldv@altlinux.org> 3.2-alt3
- Fixed build to enable proper debuginfo information.

* Sat Mar 09 2013 Valery Inozemtsev <shrek@altlinux.ru> 3.2-alt2
- update R600 target to mesa-9.1

* Sat Feb 23 2013 Valery Inozemtsev <shrek@altlinux.ru> 3.2-alt1
- 3.2

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1
- Version up (by george@) (ALT #27328)

* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 2.8-alt2
- Rebuild with ocaml-3.12.1

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.8-alt1.1
- rebuilt with perl 5.12

* Thu Nov 04 2010 Fr. Br. George <george@altlinux.ru> 2.8-alt1
- Merge new version from Rawhide

* Fri Apr 30 2010 Fr. Br. George <george@altlinux.ru> 2.7-alt1
- Merge new varsion from RawHide

* Sun Mar 28 2010 Michel Salim <salimma@fedoraproject.org> - 2.7-0.1.pre1
- Update to first 2.7 pre-release

* Tue Oct 27 2009 Fr. Br. George <george@altlinux.ru> 2.6-alt1
- Version up

* Fri Sep 18 2009 Michel Salim <salimma@fedoraproject.org> - 2.6-0.6.pre2
- Update to 2.6 pre-release2
- -devel subpackage now virtually provides -static

* Wed Sep  9 2009 Michel Salim <salimma@fedoraproject.org> - 2.6-0.5.pre1
- Disable var tracking assignments on PPC

* Wed Sep  9 2009 Michel Salim <salimma@fedoraproject.org> - 2.6-0.4.pre1
- Don't adjust clang include dir; files there are noarch (bz#521893)
- Enable clang unit tests
- clang and clang-analyzer renamed; no longer depend on llvm at runtime

* Mon Sep  7 2009 Michel Salim <salimma@fedoraproject.org> - 2.6-0.3.pre1
- Package Clang's static analyzer tools

* Mon Sep  7 2009 Michel Salim <salimma@fedoraproject.org> - 2.6-0.2.pre1
- PIC is now enabled by default; explicitly disable on %%{ix86}

* Mon Sep  7 2009 Michel Salim <salimma@fedoraproject.org> - 2.6-0.1.pre1
- First 2.6 prerelease
- Enable Clang front-end
- Enable debuginfo generation

* Sat Sep  5 2009 Michel Salim <salimma@fedoraproject.org> - 2.5-6
- Disable assertions (needed by OpenGTL, bz#521261)
- Align spec file with upstream build instructions
- Enable unit tests

* Sat Aug 22 2009 Michel Salim <salimma@fedoraproject.org> - 2.5-5
- Only disable PIC on %%ix86; ppc actually needs it

* Sat Aug 22 2009 Michel Salim <salimma@fedoraproject.org> - 2.5-4
- Disable use of position-independent code on 32-bit platforms
  (buggy in LLVM <= 2.5)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 21 2009 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- Import from FC, old package spec merged

* Wed Mar  4 2009 Michel Salim <salimma@fedoraproject.org> - 2.5-2
- Remove build scripts; they require the build directory to work

* Wed Mar  4 2009 Michel Salim <salimma@fedoraproject.org> - 2.5-1
- Update to 2.5
- Package build scripts (bug #457881)

* Tue Dec  2 2008 Michel Salim <salimma@fedoraproject.org> - 2.4-2
- Patched build process for the OCaml binding

* Tue Dec  2 2008 Michel Salim <salimma@fedoraproject.org> - 2.4-1
- Update to 2.4
- Package Ocaml binding

* Wed Jun 18 2008 Bryan O'Sullivan <bos@serpentine.com> - 2.3-2
- Add dependency on groff

* Wed Jun 18 2008 Bryan O'Sullivan <bos@serpentine.com> - 2.3-1
- LLVM 2.3

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2-4
- fix license tags

* Wed Mar  5 2008 Bryan O'Sullivan <bos@serpentine.com> - 2.2-3
- Fix compilation problems with gcc 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2-2
- Autorebuild for GCC 4.3

* Sun Jan 20 2008 Bryan O'Sullivan <bos@serpentine.com> - 2.1-2
- Fix review comments

* Sun Jan 20 2008 Bryan O'Sullivan <bos@serpentine.com> - 2.1-1
- Initial version
