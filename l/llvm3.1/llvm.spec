%def_disable doxygen

Name: llvm3.1
Version: 3.1
Release: alt1
Summary: The Low Level Virtual Machine
Group: Development/C
License: NCSA
Url: http://llvm.org/

Source0: http://llvm.org/releases/%version/llvm-%version.src.tar.gz
Source1: http://llvm.org/releases/%version/clang-%version.src.tar.gz
# Data files should be installed with timestamps preserved
Patch0: llvm-2.6-timestamp.patch

BuildRequires: chrpath groff python-dev dejagnu gcc-c++ ocamldoc tcl perl-devel perl-Pod-Parser zip
%if_enabled doxygen
BuildRequires: doxygen graphviz
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

%package doc
Summary: Documentation for LLVM
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description doc
Documentation for the LLVM compiler infrastructure.

%package -n clang%version
Summary: A C language family frontend for LLVM
License: NCSA
Group: Development/C

%description -n clang%version
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

%package -n clang%version-devel
Summary: Header files for clang
Group: Development/C
Requires: clang%version = %version-%release

%description -n clang%version-devel
This package contains header files for the Clang compiler.

%package -n clang%version-analyzer
Summary: A source code analysis framework
License: NCSA
Group: Development/C
Requires: clang%version = %version-%release

%description -n clang%version-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package -n clang%version-doc
Summary: Documentation for Clang
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description -n clang%version-doc
Documentation for the Clang compiler front-end.

%package apidoc
Summary: API documentation for LLVM
Group: Development/C
BuildArch: noarch
Requires: %name-docs = %version-%release

%description apidoc
API documentation for the LLVM compiler infrastructure.

%package -n clang%version-apidoc
Summary: API documentation for Clang
Group: Development/Languages
BuildArch: noarch
Requires: clang%version-doc = %version-%release

%description -n clang%version-apidoc
API documentation for the Clang compiler.

%package ocaml
Summary: OCaml binding for LLVM
Group: Development/Functional
Requires: %name = %version-%release
Requires: ocaml-runtime

%description ocaml
OCaml binding for LLVM.

%package ocaml-devel
Summary: Development files for %name-ocaml
Group: Development/Functional
Requires: %name-devel = %version-%release
Requires: %name-ocaml = %version-%release
Requires: ocaml

%description ocaml-devel
The %name-ocaml-devel package contains libraries and signature files
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
%setup -q -n llvm-%version.src -a1 %{?_with_gcc:-a2}
mv clang-%version.src tools/clang
%patch0 -p1 -b .timestamp

%build
%configure \
	--prefix=%prefix \
	--libdir=%_libdir/llvm \
	--datadir=%_libdir/llvm \
	--disable-assertions \
	--enable-debug-runtime \
	--enable-jit \
	--enable-targets=host \
	--enable-shared \
	--with-cxx-include-arch=%_arch-%_vendor-%_os \
	%{subst_enable doxygen}

# FIXME file this
# configure does not properly specify libdir
sed -i 's|(PROJ_prefix)/lib|(PROJ_prefix)/%_lib/llvm|g' Makefile.config
# fixed LLVM_LDFLAGS
sed -i 's|@LLVM_LDFLAGS@|-L%_libdir/llvm|' tools/llvm-config/BuildVariables.inc.in

%make_build

%check
# no current unexpected failures. Use || true if they recur to force ignore
make check 2>&1 | tee llvm-testlog.txt
(cd tools/clang && make test 2>&1) | tee clang-testlog.txt

%install
make DESTDIR=%buildroot PROJ_docsdir=/moredocs install

# Create ld.so.conf.d entry
mkdir -p %buildroot%_sysconfdir/ld.so.conf.d
cat >> %buildroot%_sysconfdir/ld.so.conf.d/llvm-%_arch.conf << EOF
%_libdir/llvm
EOF

# Static analyzer not installed by default:
# http://clang-analyzer.llvm.org/installation#OtherPlatforms
mkdir -p %buildroot%_libdir/clang-analyzer
# create launchers
for f in scan-{build,view}; do
  ln -s %_libdir/clang-analyzer/$f/$f %buildroot%_bindir/$f
done

(cd tools/clang/tools && cp -pr scan-{build,view} \
 %buildroot%_libdir/clang-analyzer/)

# Move documentation back to build directory
mv %buildroot/moredocs .
rm -f moredocs/*.tar.gz
rm -f moredocs/ocamldoc/html/*.tar.gz

# and separate the apidoc
%if_enabled doxygen
mv moredocs/html/doxygen apidoc
mv tools/clang/docs/doxygen/html clang-apidoc
%endif

# And prepare Clang documentation
mkdir clang-docs
for f in LICENSE.TXT NOTES.txt README.txt; do
  ln tools/clang/$f clang-docs/
done
rm -rf tools/clang/docs/{doxygen*,Makefile*,*.graffle,tools}
subst 's|^\(DIRS.*\) docs\(.*\)|\1\2|' tools/clang/Makefile

# Get rid of erroneously installed example files.
rm -f %buildroot%_libdir/llvm/*LLVMHello.*
rm -f %buildroot%_libdir/llvm/*BugpointPasses.*

#find %buildroot -name .dir -print0 | xargs -0r rm -f
file %buildroot/%_bindir/* | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d
file %buildroot/%_libdir/llvm/*.so | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d

# remove documentation makefiles:
# they require the build directory to work
find examples -name 'Makefile' -delete

%files
%doc CREDITS.TXT LICENSE.TXT README.txt llvm-testlog.txt
%_bindir/bugpoint
%_bindir/llc
%_bindir/lli
%exclude %_bindir/llvm-config
%_bindir/llvm*
%_bindir/opt
%_bindir/macho-dump
%config(noreplace) %_sysconfdir/ld.so.conf.d/llvm-%_arch.conf
%dir %_libdir/llvm
%_libdir/llvm/*.so
%_mandir/man1/*.1.*

%files devel
%_bindir/llvm-config
%_includedir/llvm
%_includedir/llvm-c
%_libdir/llvm/*.a

%files -n clang%version
%doc clang-docs/* clang-testlog.txt
%_bindir/clang*
%_bindir/c-index-test
%prefix/lib/clang

%files -n clang%version-devel
%_includedir/clang
%_includedir/clang-c

%files -n clang%version-analyzer
%_bindir/scan-build
%_bindir/scan-view
%_libdir/clang-analyzer

%files ocaml
%_libdir/ocaml/*.cma
%_libdir/ocaml/*.cmi

%files ocaml-devel
%_libdir/ocaml/*.a
%_libdir/ocaml/*.cmx*
%_libdir/ocaml/*.mli

%if_enabled doxygen
%files -n clang%version-doc
%doc tools/clang/docs/*

%files doc
%doc examples moredocs/html

%files ocaml-doc
%doc moredocs/ocamldoc/html/*

%files apidoc
%doc apidoc/*

%files -n clang%version-apidoc
%doc clang-apidoc/*
%endif

%changelog
* Mon Jul 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.1-alt1
- 3.1

* Mon Oct 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.9-alt1
- 2.9

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
