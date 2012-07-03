%define gcc_branch 3.3

Name: gcc%gcc_branch
Version: 3.3.4
Release: alt7

Summary: GNU Compiler Collection
License: GPL
Group: Development/C
Url: http://gcc.gnu.org/
Packager: GCC Development Team <gcc@packages.altlinux.org>

%define priority 40
%define snapshot 200410291304
%define srcver 3_3-rhl-branch-%snapshot
%define srcfilename gcc-%srcver
%define srcdirname gcc-%srcver
%define os_release %distribution, build %version-%release
%define psuffix -%gcc_branch
%define gcc_target_dir %_libdir/gcc-lib/%_target_platform/%version
%define gcc_doc_dir %_docdir/gcc%psuffix
%define alternatives_deps alternatives >= 0:0.4

# Build parameters.
%def_enable compat
%def_disable debug
%def_without fortran
%def_without objc
%def_without treelang
%def_without java
%def_without ada
%def_without testsuite
%def_without pdf

Source: %srcfilename.tar

# RH patches.
Patch101: gcc33-rh-ice-hack.patch

# Debian patches.
Patch201: gcc33-deb-alt-names.patch
Patch202: gcc33-deb-protoize.patch
Patch203: gcc33-deb-libstdc++-doclink.patch
Patch204: gcc33-deb-test-summary.patch
Patch205: gcc33-deb-libobjc.patch
Patch206: gcc32-deb-libffi-install.patch
Patch207: gcc33-deb-libffi-no-debug.patch
Patch208: gcc33-deb-gcj-without-rpath.patch
Patch209: gcc33-deb-ada-gcc-name.patch

# SuSE patches.
#Patch501:

# MDK patches.
Patch601: gcc32-mdk-mklibgcc-serialize-crtfiles.patch
Patch602: gcc32-mdk-multi-do-libdir.patch
Patch603: gcc32-mdk-c++-classfn-member-template.patch
Patch604: gcc32-mdk-pr7768.patch
Patch605: gcc32-mdk-pr8213.patch

# ALT patches.
Patch700: gcc32-alt-libobjc_makefile.patch
Patch701: gcc33-alt-libjava-makefile.patch
Patch702: gcc32-alt-install.patch
Patch703: gcc32-alt-nowrap.patch
Patch704: gcc33-alt-bison.patch

Provides: gcc = %version-%release, %_bindir/%_target_platform-gcc, %_bindir/gcc
Obsoletes: egcs, gcc3.0, gcc3.1
Conflicts: glibc-devel < 2.2.6
PreReq: %alternatives_deps, gcc-common >= 1.4
Requires: cpp%gcc_branch = %version-%release, libgcc%gcc_branch >= %version-%release
Requires: binutils >= 2.15.90.0.3, glibc-devel, make >= 3.79.1

BuildPreReq: rpm-build >= 4.0.4-alt10
%set_autoconf_version 2.13
%set_automake_version 1.4

BuildPreReq: binutils >= 2.15.90.0.3, coreutils, flex, zlib-devel, glibc-devel-static, libalternatives-devel
# due to manpages
BuildPreReq: perl-Pod-Parser
%if_with ada
%set_gcc_version 3.3
BuildPreReq: gcc3.3-gnat
%endif #with_ada
%{?_with_pdf:BuildPreReq: tetex-dvips}
%{?_with_testsuite:BuildPreReq: dejagnu}

%description
This package contains the GNU Compiler Collection version %version.
You'll need this package in order to compile C code.
It is also required for all other GCC compilers, namely C++,
Fortran 77, Objective C and Java.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you will have to type
gcc%psuffix
in order to explicitly use the GNU C compiler version %version.

####################################################################
# GCC library

%package -n libgcc%gcc_branch
Summary: GNU GCC library
Group: System/Libraries
Provides: libgcc = %version-%release
Provides: libgcc3.2 = %version-%release
Obsoletes: libgcc <= %version, libgcc3.0, libgcc3.1, libgcc3.2
Conflicts: libgcc > %version

%description -n libgcc%gcc_branch
This package contains GCC shared support library which is needed
e.g. for exception handling support.

%package -n libgcc%gcc_branch-debug
Summary: GNU GCC library with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libgcc%gcc_branch = %version-%release

%description -n libgcc%gcc_branch-debug
This package contains GCC shared support library with debugging information.
You need this only if you want to step into GCC shared support library
routines during debugging.

####################################################################
# Preprocessor

%package -n cpp%gcc_branch
Summary: The GNU C-Compatible Compiler Preprocessor
Group: Development/C
Provides: cpp = %version-%release, %_bindir/cpp
Obsoletes: gcc-cpp, egcs-cpp, cpp = %version, cpp3.0, cpp3.1
PreReq: %alternatives_deps, gcc-common >= 1.4

%description -n cpp%gcc_branch
Cpp is the GNU C-Compatible Compiler Preprocessor.
The C preprocessor is a 'macro processor' which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define 'macros,' which are abbreviations for longer
constructs.

The C preprocessor provides four separate facilities that you can use as
you see fit:

* Inclusion of header files. These are files of declarations that can be
  substituted into your program.
* Macro expansion. You can define 'macros,' which are abbreviations for
  arbitrary fragments of C code, and then the C preprocessor will replace
  the macros with their definitions throughout the program.
* Conditional compilation. Using special preprocessing directives,
  you can include or exclude parts of the program according to various
  conditions.
* Line control. If you use a program to combine or rearrange source files
  into an intermediate file which is then compiled, you can use line
  control to inform the compiler about where each source line originated.

You should install this package if you are a programmer who is searching for
such a macro processor.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you will have to type
cpp%psuffix
in order to explicitly use the GNU C Preprocessor version %version.

####################################################################
# C++ Libraries

%package -n libstdc++%gcc_branch
Summary: GNU C++ library
Group: System/Libraries
Provides: libstdc++ = %version-%release
Provides: libstdc++3.2 = %version-%release
Provides: compat-libstdc++-%gcc_branch = %version-%release
Obsoletes: libstdc++ = %version, libstdc++3.0, libstdc++3.1, libstdc++3.2
Requires: libgcc%gcc_branch >= %version-%release

%description -n libstdc++%gcc_branch
The libstdc++ package contains a snapshot of the GCC Standard C++
Library v3, an ongoing project to implement the ISO/IEC 14882:1998
Standard C++ library.

%package -n libstdc++%gcc_branch-devel
Summary: Header files and libraries for C++ development
Group: Development/C++
Provides: libstdc++-devel = %version-%release, %_libdir/libstdc++.so
Obsoletes: libstdc++-devel = %version, libstdc++3.0-devel, libstdc++3.1-devel
PreReq: %alternatives_deps, gcc-c++-common >= 1.4
Requires: libstdc++%gcc_branch = %version-%release
Requires: glibc-devel

%description -n libstdc++%gcc_branch-devel
This is the GNU implementation of the standard C++ libraries.  This
package includes the header files and libraries needed for C++
development.

%package -n libstdc++%gcc_branch-devel-static
Summary: Static libraries for C++ development
Group: Development/C++
Provides: libstdc++-devel-static = %version-%release, %_libdir/libstdc++.a
Obsoletes: libstdc++-devel-static = %version, libstdc++3.0-devel-static, libstdc++3.1-devel-static
PreReq: %alternatives_deps, gcc-c++-common >= 1.4
Requires: libstdc++%gcc_branch-devel = %version-%release

%description -n libstdc++%gcc_branch-devel-static
This is the GNU implementation of the standard C++ libraries.  This
package includes the static libraries needed for C++ development.

%package -n libstdc++%gcc_branch-debug
Summary: GNU C++ library with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libstdc++%gcc_branch = %version-%release

%description -n libstdc++%gcc_branch-debug
The libstdc++ package contains a snapshot of the GCC Standard C++
Library v3 with debugging information.
You need this only if you want to step into GCC Standard C++ library
routines during debugging.

####################################################################
# C++ Compiler

%package c++
Summary: C++ support for gcc
Group: Development/C++
Provides: gcc-c++ = %version-%release, %_bindir/%_target_platform-g++, %_bindir/g++
Obsoletes: egcs-c++, gcc-c++ = %version, gcc3.0-c++, gcc3.1-c++
PreReq: %alternatives_deps, gcc-c++-common >= 1.4
Requires: %name = %version-%release, libstdc++%gcc_branch-devel = %version-%release

%description c++
This package adds C++ support to the GNU Compiler Collection.
It includes support for most of the current C++ specification,
including templates and exception handling.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you will have to type
g++%psuffix
in order to explicitly use the GNU C++ compiler version %version.

####################################################################
# Objective C Libraries

%package -n libobjc%gcc_branch
Summary: Objective C runtime libraries
Group: System/Libraries
Provides: libobjc = %version-%release
Provides: libobjc3.2 = %version-%release
Obsoletes: libobjc <= %version, libobjc3.0, libobjc3.1, libobjc3.2
PreReq: gcc-common >= 1.4
Conflicts: libobjc > %version

%description -n libobjc%gcc_branch
This package contains Objective C shared library which is needed to run
Objective-C dynamically linked programs.

%package -n libobjc%gcc_branch-devel
Summary: Header files and libraries for Objective C development
Group: Development/Other
Provides: libobjc-devel = %version-%release
PreReq: %alternatives_deps, gcc-common >= 1.4
Requires: libobjc%gcc_branch = %version-%release
Requires: glibc-devel

%description -n libobjc%gcc_branch-devel
This is the GNU implementation of the standard Objective C libraries.
This package includes the header files and libraries needed for
Objective C development.

%package -n libobjc%gcc_branch-devel-static
Summary: Static libraries for Objective C development
Group: Development/Other
Provides: libobjc-devel-static = %version-%release
PreReq: gcc-common >= 1.4
Requires: libobjc%gcc_branch-devel = %version-%release

%description -n libobjc%gcc_branch-devel-static
This is the GNU implementation of the standard Objective C libraries.  This
package includes the static libraries needed for Objective C development.

%package -n libobjc%gcc_branch-debug
Summary: Objective C runtime libraries with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libobjc%gcc_branch = %version-%release

%description -n libobjc%gcc_branch-debug
This package contains Objective C shared library with debugging information.
You need this only if you want to step into GCC Objective C shared library
routines during debugging.

####################################################################
# Objective C Compiler

%package objc
Summary: Objective C support for gcc
Group: Development/Other
Provides: gcc-objc = %version-%release
Obsoletes: gcc-objc = %version, gcc3.0-objc, gcc3.1-objc
PreReq: %alternatives_deps, gcc-common >= 1.4
Requires: %name = %version-%release, libobjc%gcc_branch-devel = %version-%release

%description objc
This package provides Objective-C support for the GCC.
Mainly used on systems running NeXTSTEP, Objective-C is an
object-oriented derivative of the C language.

####################################################################
# Treelang Compiler

%package treelang
Summary: Treelang support for gcc
Group: Development/Other
Provides: gcc-treelang = %version-%release
PreReq: %alternatives_deps, gcc-treelang-common >= 1.4
Requires: %name = %version-%release

%description treelang
This package provides the GNU Treelang compiler.

####################################################################
# Fortran 77 Library

%package -n libg2c%gcc_branch
Summary: Fortran 77 runtime libraries
Group: System/Libraries
Provides: libg2c = %version-%release, libf2c = %version-%release
Provides: libg2c3.2 = %version-%release
Obsoletes: libf2c, libf2c3.0, libf2c3.1, libf2c3.2
Conflicts: libg2c > %version

%description -n libg2c%gcc_branch
This package contains Fortran 77 shared library which is needed to run
Fortran 77 dynamically linked programs.

%package -n libg2c%gcc_branch-devel
Summary: Header files and libraries for Fortran 77 development
Group: Development/Other
Provides: libg2c-devel = %version-%release
PreReq: gcc-g77-common >= 1.4
Requires: libg2c >= %version-%release
Requires: glibc-devel

%description -n libg2c%gcc_branch-devel
This is the GNU implementation of the standard Fortran 77 libraries.
This package includes the header files and libraries needed for
Fortran 77 development.

%package -n libg2c%gcc_branch-devel-static
Summary: Static libraries for Fortran 77 development
Group: Development/Other
Provides: libg2c-devel-static = %version-%release
PreReq: gcc-g77-common >= 1.4
Requires: libg2c%gcc_branch-devel = %version-%release

%description -n libg2c%gcc_branch-devel-static
This is the GNU implementation of the standard Fortran 77 libraries.  This
package includes the static libraries needed for Fortran 77 development.

%package -n libg2c%gcc_branch-debug
Summary: Fortran 77 runtime libraries with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libg2c%gcc_branch = %version-%release

%description -n libg2c%gcc_branch-debug
This package contains Fortran 77 shared library with debugging information.
You need this only if you want to step into GCC Fortran 77 shared library
routines during debugging.

####################################################################
# Fortran 77 Compiler

%package g77
Summary: Fortran 77 support for gcc
Group: Development/Other
Provides: gcc-g77 = %version-%release, %_bindir/%_target_platform-g77, %_bindir/g77
Obsoletes: gcc-g77 = %version, gcc3.0-g77, gcc3.1-g77
PreReq: %alternatives_deps, gcc-g77-common >= 1.4
Requires: %name = %version-%release, libg2c%gcc_branch-devel = %version-%release

%description g77
This package provides support for compiling Fortran 77
programs with the GNU Compiler Collection.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you will have to type
g77%psuffix
in order to explicitly use the GNU Fortran 77 compiler version %version.

####################################################################
# Foreign Function Interface Library

%package -n libffi%gcc_branch
Summary: Foreign Function Interface library
Group: System/Libraries
Provides: libffi = %version-%release

%description -n libffi%gcc_branch
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package contains Foreign Function Interface shared library
which is needed to run Foreign Function Interface dynamically
linked programs.

%package -n libffi%gcc_branch-devel
Summary: Header files and library for Foreign Function Interface development
Group: Development/Other
Provides: libffi-devel = %version-%release
Requires: libffi%gcc_branch = %version-%release
Requires: glibc-devel

%description -n libffi%gcc_branch-devel
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package includes the header files and library needed for
Foreign Function Interface development.

%package -n libffi%gcc_branch-devel-static
Summary: Static library for Foreign Function Interface development
Group: Development/Other
Provides: libffi-devel-static = %version-%release
Requires: libffi%gcc_branch-devel = %version-%release

%description -n libffi%gcc_branch-devel-static
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package includes the static library needed for
Foreign Function Interface development.

%package -n libffi%gcc_branch-debug
Summary: Foreign Function Interface runtime library with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libffi%gcc_branch = %version-%release

%description -n libffi%gcc_branch-debug
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package contains Foreign Function Interface shared library
with debugging information.
You need this only if you want to step into Foreign Function Interface
shared library routines during debugging.

####################################################################
# Java Libraries

%package -n libgcj%gcc_branch
Summary: GNU Java runtime libraries
Group: System/Libraries
Provides: libgcj = %version-%release
Provides: libgcj3.2 = %version-%release
Obsoletes: libgcj <= %version, libgcj3.0, libgcj3.1, libgcj3.2
Requires: libgcj-common, zip >= 2.1

%description -n libgcj%gcc_branch
The Java(tm) runtime library. You will need this package to run your Java
programs compiled using the Java compiler from GNU Compiler Collection (gcj).

%package -n libgcj%gcc_branch-devel
Summary: Header files and libraries for Java development
Group: Development/Java
Provides: libgcj-devel = %version-%release
Obsoletes: libgcj-devel = %version, libgcj3.0-devel, libgcj3.1-devel
Requires: libgcj%gcc_branch = %version-%release, zlib-devel

%description -n libgcj%gcc_branch-devel
The Java(tm) development libraries and include files. You will need this
package to compile your Java programs using the GCC Java compiler (gcj).

%package -n libgcj%gcc_branch-devel-static
Summary: Static libraries for Java development
Group: Development/Java
Provides: libgcj-devel-static = %version-%release
Obsoletes: libgcj-devel-static = %version, libgcj3.0-devel-static, libgcj3.1-devel-static
Requires: libgcj%gcc_branch-devel = %version-%release

%description -n libgcj%gcc_branch-devel-static
The Java(tm) static libraries. You may need this
package to compile your Java programs using the GCC Java compiler (gcj).

%package -n libgcj%gcc_branch-debug
Summary: GNU Java runtime libraries with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libgcj%gcc_branch = %version-%release

%description -n libgcj%gcc_branch-debug
The Java(tm) runtime library with debugging information.
You need this only if you want to step into GCC Java(tm) runtime library
routines during debugging.

####################################################################
# Java Compiler

%package java
Summary: Java support for gcc
Group: Development/Java
Provides: gcc-java = %version-%release, %_bindir/gcj
Obsoletes: gcc-java <= %version, gcc3.0-java, gcc3.1-java, gcj3.1-tools, gcj%gcc_branch-tools
PreReq: %alternatives_deps, gcc-java-common >= 1.4
Requires: %name = %version-%release, libgcj%gcc_branch-devel = %version-%release
Conflicts: kaffe < 1.0.7

%description java
This package adds support for compiling Java(tm) programs and
bytecode into native code.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you will have to type
gcj%psuffix
in order to explicitly use the GNU Java compiler version %version.

####################################################################
# Ada 95 Libraries

%package -n libgnat%gcc_branch
Summary: Ada 95 runtime libraries
Group: System/Libraries
Provides: libgnat = %version-%release
Obsoletes: libgnat <= %version

%description -n libgnat%gcc_branch
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries.  It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the
Posix 1003.5 Binding (Florist).

%package -n libgnat%gcc_branch-devel
Summary: Header files and libraries for Ada 95 development
Group: Development/Other
Provides: libgnat-devel = %version-%release
PreReq: gcc-common >= 1.4
Requires: libgnat%gcc_branch = %version-%release

%description -n libgnat%gcc_branch-devel
This is the GNU implementation of the standard Ada 95 libraries.
This package includes the include files and libraries needed for
Ada 95 development.

%package -n libgnat%gcc_branch-devel-static
Summary: Static libraries for Ada 95 development
Group: Development/Other
Provides: libgnat-devel-static = %version-%release
PreReq: gcc-common >= 1.4
Requires: libgnat%gcc_branch-devel = %version-%release

%description -n libgnat%gcc_branch-devel-static
This is the GNU implementation of the standard Ada 95 libraries.  This
package includes the static libraries needed for Ada 95 development.

%package -n libgnat%gcc_branch-debug
Summary: Ada 95 runtime libraries with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libgnat%gcc_branch = %version-%release

%description -n libgnat%gcc_branch-debug
This package contains Ada 95 shared library with debugging information.
You need this only if you want to step into GCC Ada 95 shared library
routines during debugging.

####################################################################
# Ada 95 Compiler

%package gnat
Summary: Ada 95 support for gcc
Group: Development/Other
Provides: gcc-gnat = %version-%release, %_bindir/gnat
Obsoletes: gcc-gnat <= %version
Conflicts: gcc-gnat > %version
PreReq: %alternatives_deps, gcc-common >= 1.4
Requires: %name = %version-%release, libgnat%gcc_branch-devel = %version-%release

%description gnat
This package provides support for compiling Ada 95
programs with the GNU Compiler Collection.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you will have to type
gnat%psuffix
in order to explicitly use the GNU Ada compiler version %version.

####################################################################
# GCC documentation

%package doc
Summary: GCC documentation
Group: Development/Other
Provides: gcc-doc = %version-%release
Obsoletes: gcc-doc <= %version, gcc3.0-doc, gcc3.1-doc, gcc3.2-doc
Conflicts: gcc-doc > %version

%description doc
This package contains documentation for the GNU Compiler Collection
version %version.

%prep
%setup -q -n %srcdirname
find -type d -name CVS -print0 |
	xargs -r0 rm -rf --

# RH patches.
%patch101 -p0

# Debian patches.
%patch201 -p1
%patch202 -p0
%patch203 -p0
%patch204 -p0
%patch205 -p0
%patch206 -p0
%patch207 -p0
%patch208 -p1
%patch209 -p1

# SuSE patches.
#%patch501 -p0

# MDK patches.
%patch601 -p1
%patch602 -p1

# ALT patches.
%patch700 -p0
%patch701 -p1
%patch702 -p1
%patch703 -p1
%patch704 -p1

# Set proper version & contact info.
cp -p gcc/version.c gcc/version.c.orig
%__subst 's/3\.3\.4/%version/g' gcc/version.c gcc/doc/include/gcc-common.texi
%__subst 's/\(%gcc_branch\(\.[0-9]\+\)*\)\( [0-9]\+[a-z]*\)\?.*"/\1\3 (%os_release)"/' gcc/version.c
%__subst 's,<URL:[^>]*>,<URL:http://bugzilla.altlinux.ru/>,' gcc/version.c

# Misdesign in libstdc++
cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

%build
for f in */configure.in; do
	(cd "${f%%/*}" && [ configure.in -nt configure ] && autoconf)
done
for f in */Makefile.am; do
	(cd "${f%%/*}" && [ Makefile.am -nt Makefile.in ] && automake)
done

%define buildtarget build-%_target_platform
rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

CC=gcc
%remove_optflags %optflags_nocpp %optflags_notraceback
%ifarch %ix86
%global optflags %(printf %%s '%optflags' |sed 's/-mtune=[^[:space:]]\\+/-mcpu=i686/g')
%endif

CC="$CC" \
CFLAGS="%optflags" \
CXXFLAGS="%optflags" \
GCJFLAGS="%optflags" \
XCFLAGS="%optflags" \
TCFLAGS="%optflags" \
	../configure --prefix=%prefix \
	--libdir=%_libdir \
	--with-slibdir=/%_lib \
	--mandir=%_mandir \
	--infodir=%_infodir \
	--enable-shared \
	--enable-threads=posix \
	--disable-checking \
	--enable-long-long \
	--enable-__cxa_atexit \
	--enable-languages="c,c++%{?_with_fortran:,f77}%{?_with_objc:,objc}%{?_with_treelang:,treelang}%{?_with_java:,java}%{?_with_ada:,ada}" \
	--program-suffix=%psuffix \
	--enable-objc-gc \
	--with-system-zlib \
	--without-included-gettext \
	--disable-multilib \
	--host=%_target_platform --build=%_target_platform --target=%_target_platform

%make_build bootstrap-lean

%if_with ada
# SMP-incompatible build.
make -C gcc gnatlib-shared
make -C gcc gnattools
%endif #with_ada

%if_with testsuite
make -k check
../contrib/test_summary
%endif #with_testsuite

popd #%buildtarget

# build printable documentation
%if_with pdf
(cd gcc/doc; for f in gcc cpp cppinternals; do
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done)
%if_with fortran
(cd gcc/f; for f in g77; do
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done)
%endif #with_fortran
%if_with java
(cd gcc/java; for f in gcj
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done)
%endif #with_java
%if_with ada
(cd gcc/ada; for f in gnat_rm gnat_ug_unx; do
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done
mv gnat_ug_unx.pdf gnat_ug.pdf
)
%endif #with_ada
%endif #with_pdf

%install
mkdir -p %buildroot%gcc_doc_dir

# Copy various doc files here and there
CopyDocs()
{
	local n="$1"
	shift
	mkdir -p "%buildroot%gcc_doc_dir/$n"
	local d="$1"
	shift
	local f
	for f in "$d"/*{README,NEWS,ChangeLog,LICENSE,THREADS}*; do
		[ -f "$f" ] || continue
		install -pv -m644 "$f" "%buildroot%gcc_doc_dir/$n/"
	done
}

CopyDocs gcc gcc
CopyDocs g++ gcc/cp
CopyDocs libstdc++ libstdc++-v3
cp -av libstdc++-v3/docs/html %buildroot%gcc_doc_dir/libstdc++/

%if_with fortran
CopyDocs g77 gcc/f
CopyDocs libg2c libf2c
%endif #with_fortran

%if_with objc
CopyDocs objc gcc/objc
CopyDocs libobjc libobjc
%endif #with_objc

%if_with treelang
CopyDocs treelang gcc/treelang
%endif #with_treelang

%if_with java
CopyDocs boehm-gc boehm-gc
install -pv -m644 boehm-gc/doc/* %buildroot%gcc_doc_dir/boehm-gc/
CopyDocs java gcc/java
CopyDocs fastjar fastjar
CopyDocs libffi libffi
CopyDocs libjava libjava
%endif #with_java

%if_with ada
CopyDocs ada gcc/ada
%endif #with_ada

ln -s documentation.html %buildroot%gcc_doc_dir/libstdc++/html/index.html

# Compress changelogs.
find %buildroot%gcc_doc_dir -type f -name *ChangeLog\* \! -name \*.bz2 -print0 |
	xargs -r0 bzip2 -9 --

pushd %buildtarget
%makeinstall_std
popd #%buildtarget

# Rename binaries which will be packaged under alternatives control.
pushd %buildroot%_bindir
	rm -f addr2name.awk*
	for n in \
	  cpp \
	  gcc gcov protoize unprotoize \
	  g++ \
	  %{?_with_fortran:g77} \
	  %{?_with_treelang:tree1} \
	  %{?_with_java:gcj gcjh gij jcf-dump jv-scan grepjar jar rmic rmiregistry} \
	  ; do
		[ ! -f "%_target_platform-$n%psuffix" ] || continue
		mv -v "$n%psuffix" "%_target_platform-$n%psuffix"
		ln -s "%_target_platform-$n%psuffix" "$n%psuffix"
	done
	%{?_with_ada:ln -s gcc%psuffix gnatgcc}
popd

# Relocate libraries to the right directories.
pushd %buildroot%_libdir
	rm -f libiberty.a lib*.la
	mv *.a %buildroot%gcc_target_dir/
	for f in *.so; do
		v=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
		[ -f "$v" ]
		ln -s ../../../"$v" "%buildroot%gcc_target_dir/$f"
		rm -f "$f"
	done
popd
pushd %buildroot/%_lib
	for f in *.so; do
		v=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
		[ -f "$v" ]
		ln -s ../../../../../%_lib/"$v" "%buildroot%gcc_target_dir/$f"
		rm -f "$f"
	done
popd

%if_with ada
# Dispatch Ada 95 libraries.
pushd %buildroot%gcc_target_dir
	for n in gnat gnarl; do
		mv adalib/lib$n-*.so.* %buildroot%_libdir/
		rm -f adalib/lib$n.so.*
		ln -s ../../../lib$n-*.so.* lib$n.so
	done
	mv adalib/*.a .
popd
%endif #with_ada

# Normalize manpage names.
pushd %buildroot%_man1dir
	for f in cpp gcov %{?_with_java:gij}; do
		mv "$f".1 "$f"%psuffix.1
	done
popd

%if_with java
# Relocate Java headers to version-specific compiler directory.
mv %buildroot%_includedir/{ffi,j}*.h %buildroot%gcc_target_dir/include/
mv %buildroot%_includedir/{java,javax,gnu} %buildroot%gcc_target_dir/include/
mv %buildroot%_includedir/gcj/* %buildroot%gcc_target_dir/include/gcj/
rmdir %buildroot%_includedir/gcj

# Fix libgcj.spec and move it to compiler-specific directory.
%__subst -p 's/-lgcjgc//g;s/-lzgcj//g;s/-lpthread//g' %buildroot%_libdir/libgcj.spec
mv %buildroot%_libdir/libgcj.spec %buildroot%gcc_target_dir/
%endif #with_java

# buildreq substitution rules.
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
for n in cpp gcc gcc-c++ gcc-g77 gcc-gnat gcc-java gcc-objc gcc-treelang libg2c libg2c-devel libg2c-devel-static libgcc libffi libffi-devel libffi-devel-static libgcj libgcj-devel libgcj-devel-static libgnat libgnat-devel libgnat-devel-static libobjc libobjc-devel libobjc-devel-static libstdc++ libstdc++-devel libstdc++-devel-static; do
	pref="${n%%%%-*}"
	suf="${n#$pref}"
	t="${pref}%gcc_branch$suf"
	echo "$n" >"%buildroot%_sysconfdir/buildreqs/packages/substitute.d/$t"
done
chmod 644 %buildroot%_sysconfdir/buildreqs/packages/substitute.d/*

# buildreq ignore rules.
mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name <<EOF
^%gcc_target_dir(/include)?$
EOF

# no valid g++ manpage exists in 3.3 series.
rm -fv %buildroot%_man1dir/g++%psuffix.1
ln -s gcc%psuffix.1.bz2 %buildroot%_man1dir/g++%psuffix.1.bz2

%find_lang gcc%psuffix

mkdir -p %buildroot%_libdir/debug
cp -a %buildroot{/%_lib,%_libdir}/*.so.* %buildroot%_libdir/debug/

%if_enabled debug
# Don't strip in debug mode
%set_strip_method none
%endif #enabled_debug

%set_compress_method bzip2

#install alternatives stuff
install -d %buildroot%_altdir
cat >%buildroot%_altdir/cpp%gcc_branch<<EOF
%_bindir/%_target_platform-cpp	%_bindir/%_target_platform-cpp%psuffix	%priority
%_man1dir/cpp.1.bz2	%_man1dir/cpp%psuffix.1.bz2	%_bindir/%_target_platform-cpp%psuffix
EOF

cat >%buildroot%_altdir/%name<<EOF
%_bindir/%_target_platform-gcc	%_bindir/%_target_platform-gcc%psuffix	%priority
%_bindir/%_target_platform-gcov	%_bindir/%_target_platform-gcov%psuffix	%_bindir/%_target_platform-gcc%psuffix
%_bindir/%_target_platform-protoize	%_bindir/%_target_platform-protoize%psuffix	%_bindir/%_target_platform-gcc%psuffix
%_bindir/%_target_platform-unprotoize	%_bindir/%_target_platform-unprotoize%psuffix	%_bindir/%_target_platform-gcc%psuffix
%_man1dir/gcc.1.bz2	%_man1dir/gcc%psuffix.1.bz2	%_bindir/%_target_platform-gcc%psuffix
%_man1dir/gcov.1.bz2	%_man1dir/gcov%psuffix.1.bz2	%_bindir/%_target_platform-gcc%psuffix
EOF

cat >%buildroot%_altdir/c++%gcc_branch<<EOF
%_bindir/%_target_platform-g++	%_bindir/%_target_platform-g++%psuffix	%priority
%_bindir/%_target_platform-c++filt	%_bindir/%_target_platform-c++filt%psuffix	%_bindir/%_target_platform-g++%psuffix
%_man1dir/g++.1.bz2	%_man1dir/g++%psuffix.1.bz2	%_bindir/%_target_platform-g++%psuffix
EOF

%if_with fortran
cat >%buildroot%_altdir/g77%gcc_branch<<EOF
%_bindir/%_target_platform-g77	%_bindir/%_target_platform-g77%psuffix	%priority
%_man1dir/g77.1.bz2	%_man1dir/g77%psuffix.1.bz2	%_bindir/%_target_platform-g77%psuffix
EOF
%endif

%if_with treelang
cat >%buildroot%_altdir/tree1%gcc_branch<<EOF
%_bindir/%_target_platform-tree1	%_bindir/%_target_platform-tree1%psuffix	%priority
EOF
%endif

%if_with java
cat >%buildroot%_altdir/java%gcc_branch<<EOF
%_bindir/%_target_platform-gcj	%_bindir/%_target_platform-gcj%psuffix	%priority
%_bindir/%_target_platform-gcjh	%_bindir/%_target_platform-gcjh%psuffix	%_bindir/%_target_platform-gcj%psuffix
%_bindir/%_target_platform-gij	%_bindir/%_target_platform-gij%psuffix	%_bindir/%_target_platform-gcj%psuffix
%_bindir/%_target_platform-jcf-dump	%_bindir/%_target_platform-jcf-dump%psuffix	%_bindir/%_target_platform-gcj%psuffix
%_bindir/%_target_platform-jv-scan	%_bindir/%_target_platform-jv-scan%psuffix	%_bindir/%_target_platform-gcj%psuffix
%_bindir/%_target_platform-grepjar	%_bindir/%_target_platform-grepjar%psuffix	%_bindir/%_target_platform-gcj%psuffix
%_bindir/%_target_platform-jar	%_bindir/%_target_platform-jar%psuffix	%_bindir/%_target_platform-gcj%psuffix
%_bindir/%_target_platform-rmic	%_bindir/%_target_platform-rmic%psuffix	%_bindir/%_target_platform-gcj%psuffix
%_bindir/%_target_platform-rmiregistry	%_bindir/%_target_platform-rmiregistry%psuffix	%_bindir/%_target_platform-gcj%psuffix
%_man1dir/gcj.1.bz2	%_man1dir/gcj%psuffix.1.bz2	%_bindir/%_target_platform-gcj%psuffix
%_man1dir/gij.1.bz2	%_man1dir/gij%psuffix.1.bz2	%_bindir/%_target_platform-gcj%psuffix
EOF
%endif

%files -n libstdc++%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch
%_libdir/libstdc++.so.*

%if_disabled compat
%files -f gcc%psuffix.lang
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%_altdir/%name
%dir %gcc_doc_dir
%gcc_doc_dir/gcc
%_bindir/gcc%psuffix
%_bindir/gcov%psuffix
%_bindir/protoize%psuffix
%_bindir/unprotoize%psuffix
%_bindir/%_target_platform-gcc%psuffix
%_bindir/%_target_platform-gcov%psuffix
%_bindir/%_target_platform-protoize%psuffix
%_bindir/%_target_platform-unprotoize%psuffix
%_man1dir/gcc%psuffix.*
%_man1dir/gcov%psuffix.*
%dir %gcc_target_dir
%gcc_target_dir/libgcc_s.so
%gcc_target_dir/collect2
%gcc_target_dir/crt*.o
%gcc_target_dir/libgcc*.a
%gcc_target_dir/SYSCALLS.c.X
%gcc_target_dir/specs
%dir %gcc_target_dir/include
%gcc_target_dir/include/float.h
%gcc_target_dir/include/*mmintrin.h
%gcc_target_dir/include/iso646.h
%gcc_target_dir/include/limits.h
%gcc_target_dir/include/stdarg.h
%gcc_target_dir/include/stdbool.h
%gcc_target_dir/include/stddef.h
%gcc_target_dir/include/syslimits.h
%gcc_target_dir/include/unwind.h
%gcc_target_dir/include/varargs.h
%gcc_target_dir/include/README

%files -n libgcc%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcc%gcc_branch
/%_lib/libgcc_s.so.*

%files -n libgcc%gcc_branch-debug
%_libdir/debug/libgcc_s.so.*

%files -n cpp%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/cpp%gcc_branch
%_altdir/cpp%gcc_branch
%_bindir/cpp%psuffix
%_bindir/%_target_platform-cpp%psuffix
%_man1dir/cpp%psuffix.*
%dir %gcc_target_dir
%gcc_target_dir/cc1

%files -n libstdc++%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/libstdc++
%_includedir/c++/*
%dir %gcc_target_dir
%gcc_target_dir/libstdc++.so
%gcc_target_dir/libsupc++.a

%files -n libstdc++%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch-devel-static
%dir %gcc_target_dir
%gcc_target_dir/libstdc++.a

%files -n libstdc++%gcc_branch-debug
%_libdir/debug/libstdc++.so.*

%files c++
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-c++
%_altdir/c++%gcc_branch
%dir %gcc_doc_dir
%gcc_doc_dir/g++
%_bindir/g++%psuffix
%_bindir/%_target_platform-g++%psuffix
%_man1dir/g++%psuffix.1.*
%dir %gcc_target_dir
%gcc_target_dir/cc1plus

%if_with objc
%files -n libobjc%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libobjc%gcc_branch
%_libdir/libobjc*.so.*

%files -n libobjc%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libobjc%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/libobjc
%dir %gcc_target_dir
%gcc_target_dir/libobjc*.so
%dir %gcc_target_dir/include
%gcc_target_dir/include/objc

%files -n libobjc%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libobjc%gcc_branch-devel-static
%dir %gcc_target_dir
%gcc_target_dir/libobjc*.a

%files -n libobjc%gcc_branch-debug
%_libdir/debug/libobjc*.so.*

%files objc
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-objc
%dir %gcc_doc_dir
%gcc_doc_dir/objc
%dir %gcc_target_dir
%gcc_target_dir/cc1obj
%endif #with_objc

%if_with treelang
%files treelang
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-treelang
%_altdir/tree1%gcc_branch
%_bindir/tree1%psuffix
%_bindir/%_target_platform-tree1%psuffix
%dir %gcc_doc_dir
%gcc_doc_dir/treelang
%dir %gcc_target_dir
%gcc_target_dir/tree1
%endif #with_treelang

%if_with fortran
%files -n libg2c%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libg2c%gcc_branch
%_libdir/libg2c.so.*

%files -n libg2c%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libg2c%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/libg2c
%dir %gcc_target_dir
%gcc_target_dir/libg2c.so
%dir %gcc_target_dir/include
%gcc_target_dir/include/g2c.h

%files -n libg2c%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libg2c%gcc_branch-devel-static
%dir %gcc_target_dir
%gcc_target_dir/libg2c.a

%files -n libg2c%gcc_branch-debug
%_libdir/debug/libg2c.so.*

%files g77
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-g77
%_altdir/g77%gcc_branch
%dir %gcc_doc_dir
%gcc_doc_dir/g77
%_bindir/g77%psuffix
%_bindir/%_target_platform-g77%psuffix
%_man1dir/g77%psuffix.*
%dir %gcc_target_dir
%gcc_target_dir/f771
%gcc_target_dir/libfrtbegin.a
%endif #with_fortran

%if_with java
%files -n libffi%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libffi%gcc_branch
%_libdir/libffi.so.*

%files -n libffi%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libffi%gcc_branch-devel
%dir %gcc_target_dir
%gcc_target_dir/libffi.so
%dir %gcc_target_dir/include
%gcc_target_dir/include/ffi*.h
%gcc_doc_dir/libffi

%files -n libffi%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libffi%gcc_branch-devel-static
%dir %gcc_target_dir
%gcc_target_dir/libffi.a

%files -n libffi%gcc_branch-debug
%_libdir/debug/libffi.so.*

%files -n libgcj%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch
%_libdir/libgcj.so.*
%_libdir/lib-org-*.so.*
%_datadir/java/*

%files -n libgcj%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/boehm-gc
%gcc_doc_dir/libjava
%_bindir/jv-convert%psuffix
%_man1dir/jv-convert.*
%dir %gcc_target_dir
%gcc_target_dir/libgcj.spec
%gcc_target_dir/libgcj.so
%gcc_target_dir/lib-org-*.so
%dir %gcc_target_dir/include
%gcc_target_dir/include/j*.h
%gcc_target_dir/include/java
%gcc_target_dir/include/javax
%gcc_target_dir/include/gnu
%gcc_target_dir/include/gcj

%files -n libgcj%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-devel-static
%dir %gcc_target_dir
%gcc_target_dir/libgcj.a
%gcc_target_dir/lib-org-*.a

%files -n libgcj%gcc_branch-debug
%_libdir/debug/libgcj.so.*
%_libdir/debug/lib-org-*.so.*

%files java
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-java
%_altdir/java%gcc_branch
%dir %gcc_doc_dir
%gcc_doc_dir/fastjar
%gcc_doc_dir/java
%_bindir/gcj*%psuffix
%_bindir/%_target_platform-gcj*%psuffix
%_bindir/gij%psuffix
%_bindir/%_target_platform-gij%psuffix
%_bindir/jcf-dump%psuffix
%_bindir/%_target_platform-jcf-dump%psuffix
%_bindir/jv-scan%psuffix
%_bindir/%_target_platform-jv-scan%psuffix
%_bindir/*jar%psuffix
%_bindir/rmi*%psuffix
%_bindir/%_target_platform-rmi*%psuffix
%_man1dir/gij*.*
%_man1dir/gcj*.*
%_man1dir/jv-scan.*
%_man1dir/jcf-dump.*
%_man1dir/rmi*.*
%_man1dir/*jar%psuffix.*
%dir %gcc_target_dir
%gcc_target_dir/jc1
%gcc_target_dir/jvgenmain
%endif #with_java

%if_with ada
%files gnat
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-gnat
%_bindir/gnat*
%gcc_target_dir/gnat1
%gcc_target_dir/ada*

%files -n libgnat%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch
%_libdir/libgnat-*.so.*
%_libdir/libgnarl-*.so.*

%files -n libgnat%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch-devel
%gcc_target_dir/libgna*.so
%gcc_target_dir/libgmem.a
%dir %gcc_doc_dir
%gcc_doc_dir/ada

%files -n libgnat%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch-devel-static
%gcc_target_dir/libgna*.a

%files -n libgnat%gcc_branch-debug
%_libdir/debug/libgna*
%endif #with_ada

%files doc
%_infodir/cpp*.info*
%_infodir/gcc*.info*
%{?_with_fortran:%_infodir/g77.info*}
%{?_with_treelang:%_infodir/treelang.info*}
%{?_with_java:%_infodir/fastjar.info*}
%{?_with_java:%_infodir/gcj.info*}
%{?_with_ada:%_infodir/gnat-style.info*}
%{?_with_ada:%_infodir/gnat_rm.info*}
%{?_with_ada:%_infodir/gnat_ug_unx.info*}
%if_with pdf
%doc gcc/doc/cpp*.pdf
%doc gcc/doc/gcc*.pdf
%{?_with_fortran:%doc gcc/doc/g77.pdf}
%{?_with_ada:%doc gcc/doc/gnat*.pdf}
%endif #with_pdf
%endif #compat

%changelog
* Tue Nov 16 2010 Dmitry V. Levin <ldv@altlinux.org> 3.3.4-alt7
- Fixed build with new perl.

* Tue Jun 09 2009 Dmitry V. Levin <ldv@altlinux.org> 3.3.4-alt6
- Removed obsolete %%install_info/%%uninstall_info calls.
- Fixed build with fresh bison.

* Tue Feb 10 2009 Dmitry V. Levin <ldv@altlinux.org> 3.3.4-alt5
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Switched to alternatives-0.4.

* Tue Feb 10 2009 Aleksey Avdeev <solo@altlinux.ru> 3.3.4-alt4.1
- NMU
- Add provides for compatibility: compat-libstdc++-%%gcc_branch
  (Closes: #18796)

* Mon Mar 27 2006 Dmitry V. Levin <ldv@altlinux.org> 3.3.4-alt4
- Fixed build with new %%optflags.

* Mon Feb 20 2006 Dmitry V. Levin <ldv@altlinux.org> 3.3.4-alt3
- Fixed build on x86_64 (#9124).

* Fri Feb 17 2006 Dmitry V. Levin <ldv@altlinux.org> 3.3.4-alt2
- Enabled compatibility mode: package libstdc++%gcc_branch only.

* Thu Jun 23 2005 Dmitry V. Levin <ldv@altlinux.org> 3.3.4-alt1
- Updated to gcc-3_3-rhl-branch 200410291304.
- Enabled build with make-3.81beta3.

* Fri Jan 14 2005 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt7
- Converted alternatives config files to new format (0.2.0).
- When gnat is enabled, ensure that gcc3.3 is used for build.

* Wed Dec 29 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt6
- Updated interpackage dependencies.

* Sat May 15 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt5
- Rebuilt with binutils-2.15.90.0.3 and glibc-2.3.x.

* Tue Apr 20 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt4
- Synced with RH gcc-3.3.3-7 (gcc-3_3-branch 20040413).

* Fri Apr 09 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt3
- Synced with RH gcc-3.3.3-6 (gcc-3_3-branch 20040327).

* Wed Mar 17 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt2
- Synced with RH gcc-3.3.3-3 (gcc-3_3-branch 20040312).

* Fri Feb 20 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt1
- Synced with RH gcc-3.3.3-2 (gcc-3_3-branch 20040217).

* Thu Jan 22 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt0.2
- Synced with RH gcc-3.3.2-7 (gcc-3_3-branch 20040120).

* Sat Jan 03 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.3-alt0.1
- Synced with RH gcc-3.3.2-5 (gcc-3_3-branch 20031219).
- Minor specfile tweaks to ease gcc3.2/gcc3.3 upgrade.

* Wed Dec 24 2003 Dmitry V. Levin <ldv@altlinux.org> 3.3.2-alt1
- Updated to RH gcc-3.3.2-3 (gcc-3_3-branch 20031203),
  with -pie support.
- Updated patches.
- Relocated libgcc_s.so to %%gcc_target_dir.
- Changed %%gcc_target_dir/*.so symlink values.
- Packaged GNU Treelang compiler.
- Packaged GNAT (without alternatives support yet).

* Thu Oct 16 2003 Dmitry V. Levin <ldv@altlinux.org> 3.2.3-alt2
- Finalized alternatives transition.

* Wed Oct 15 2003 Stanislav Ievlev <inger@altlinux.ru> 3.2.3-alt1.4
- g++ manpage doesn't exist in 3.2 series, made symlink to gcc's manpage.

* Wed Oct 15 2003 Stanislav Ievlev <inger@altlinux.ru> 3.2.3-alt1.3
- added alternatives to g++ man-page, require more recent gcc-common version

* Tue Oct 14 2003 Stanislav Ievlev <inger@altlinux.ru> 3.2.3-alt1.2
- fix java alternatives config

* Tue Oct 14 2003 Stanislav Ievlev <inger@altlinux.ru> 3.2.3-alt1.1
- new alternatives support

* Mon Jun 09 2003 Dmitry V. Levin <ldv@altlinux.org> 3.2.3-alt1
- Updated to gcc_3_2-branch (20030506), dropped all non-alt patches.
- Merged:
  + RH: gcc-3_2-rhl8-branch (patches for fastjar,libffi,libiberty,libobjc);
  + Debian: gcc-3.2_3.2.3ds9-4 (15 patches);
  + SuSE (5 patches);
  + MDK (6 patches).
- Packaged libffi.
- Note that there are no rhl8-specific gcc patches in this release.

* Fri Nov 29 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt2
- Fixed typo in "%%triggerpostun c++".

* Tue Nov 26 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt1
- Updated to 3.2.1 release (3.2.1 20021119).
- Following patches merged upstream:
  + trunc_int_for_mode;
  + x86_64-q_regs_operand;
  + fold-const2;
  + i386-pr7242;
  + i386-pr7242;
  + loop-prefetch;
  + libstdc++-glibc23-1;
  + libstdc++-glibc23-2;
  + libstdc++-glibc23-3;
  + libstdc++-glibc23-4;
  + interface_only.
- Updated patches: tls, doc-gcov.
- Dropped patches: c++-tail-pad-backout.
- Added missing provides to gcc subpackage.
- Removed soname provides from -debug subpackages.
- Removed %_libdir/libstdc++.{so,a} (no longer needed).
- Moved java wrappers to separate subpackage (jdkgcj).
- Moved gccbug to separate subpackage (gcc-common).
- Removed prefixes from: jar grepjar rmic rmiregistry.
- Migrated to new alternatives scheme.

* Mon Sep 30 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt0.4
- Merged with rh gcc-3.2-7:
  * Tue Sep  3 2002 Bill Nottingham <notting@redhat.com> 3.2-7
  - fix calling of C++ destructors in certain cases
  * Tue Sep  3 2002 Jakub Jelinek <jakub@redhat.com> 3.2-6
  - update from CVS (but revert C++ tail padding patches
    for now)
  - further fixes to make libstdc++-v3 build on glibc 2.3
  - run libstdc++-v3 make check-abi on IA-32 during testing
  * Fri Aug 30 2002 Jakub Jelinek <jakub@redhat.com> 3.2-5
  - disable tail copy patches, they seem to still have problems
  - make libstdc++-v3 build on glibc 2.3 (and use thread-local
    locale model)
- libstdc++%gcc_branch:
  Added explicit versioned dependence on libgcc%gcc_branch (#0001332).
- %name-java: fixed update-alternatives.

* Fri Sep 06 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt0.3
- Disabled c++-tail-pad patch (causes internal errors in cpp code).
- Switched back to default stripping policy:
  make use of new (rpm-build >= 4.0.4-alt3) strip feature.
- Moved unstripped shared libraries to -debug subpackages.

* Fri Aug 30 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt0.2
- Merged with rh gcc-3.2-4:
  * Wed Aug 26 2002 Jakub Jelinek <jakub@redhat.com> 3.2-4
  - reorder alpha_encode_section_info checks slightly to fix an ICE
    when building glibc and to take better advantage of visibility
    attribute on Alpha
  - as gdb is not there yet, disable -momit-leaf-frame-pointer
    by default for now on IA-32
  - fix IA-64 bootstrap with tail padding patch (Jason Merrill, Daniel Berlin)
  - fix x86-64 %%RIP to %%rip, only output (%%rip) if no other relocation
    is used (Richard Henderson)
  * Fri Aug 23 2002 Jakub Jelinek <jakub@redhat.com> 3.2-3
  - take advantage of __attribute__((visibility())) on Alpha
  - avoid copying tail padding (Jason Merrill)
- Use /bin/readlink.
- Added "Conflicts: glibc-devel < 2.2.6".
- Raised alternatives priority from 15 to 30.

* Mon Aug 26 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt0.1
- Updated to snapshot 20020822.
- Merged ALT patches from 2.96 branch.
- Merged with rh gcc-3.2-2:
  * Thu Aug 22 2002 Jakub Jelinek <jakub@redhat.com> 3.2-2
  - fixed Dwarf2 DW_OP_GNU_push_tls_address patch from Richard Henderson.
  - don't mention removed -a and -ax options in the documentation
    (Nathan Sidwell, #72233).
  - fixed __typeof() followed by __asm() redirection from Alexandre Oliva.

* Wed Aug 21 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2-alt3
- Rewritten interpackage dependencies to make peace with other
  versions of GCC which may be installed in the system.
- Dropped gnat.
- Added %%with/%%without logic for conditional build.
- Cleaned up descriptions.
- Cleaned up %%prep and %%build sections.
- Rewritten %%install section (no idea how it could work before).
- Set proper version information.
- Fixed doc package (info documentation was incomplete).
- Relocated documentation to %_docdir/gcc-%version/.
- Relocated libgcj headers back to compiler-specific include directory.
- Renamed libf2c* to libg2c*.
- Libificated libg2c and libobjc packages.
- gcc: moved gccbug under update-alternatives control.
- c++: moved c++filt under update-alternatives control.
- libobjc: added libobjc_gc.* libraries.
- java: moved under update-alternatives control.
  (AKA: java now should be usable).
- Moved some manpages under update-alternatives control.
- Added buildreq substitution rules.
- Added buildreq ignore rules.
- Raised alternatives priority from 5 to 15.

* Mon Aug 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.2-alt2
- Synced with release tarball: 3.2 20020814 (release).
- Removed some patches - there are in tarball now.

* Tue Aug 13 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.2-alt1
- 3.2
- Added some Cooker & RawHide patches
- Fixed update-alternatives

* Mon Jun 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.1.1-alt1
- First build for Sisyphus
- Added some patches from CooKer
- Added patches from RH & Suse
