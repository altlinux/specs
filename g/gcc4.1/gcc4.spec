%define gcc_branch 4.1

Name: gcc%gcc_branch
Version: 4.1.2
Release: alt10

Summary: GNU Compiler Collection
License: GPL
Group: Development/C
Url: http://gcc.gnu.org/
Packager: Dmitry V. Levin <ldv@altlinux.org>

%ifarch ppc
# On ppc32, we build a 64-bit compiler with default 32-bit mode.
%define _target_platform ppc64-alt-linux
%endif

%define priority 410
%define snapshot 20070626
%define srcver %version-%snapshot
%define srcfilename gcc-%srcver
%define srcdirname gcc-%srcver
%define os_release %distribution, build %version-%release
%define psuffix -%gcc_branch
%define _libexecdir /usr/libexec
%define gcc_target_libdir %_libdir/gcc/%_target_platform/%version
%define gcc_target_libexecdir %_libexecdir/gcc/%_target_platform/%version
%define gcc_doc_dir %_docdir/gcc%psuffix
%define alternatives_deps alternatives >= 0:0.4
%define binutils_deps binutils >= 1:2.16.91.0.3-alt1

%if_enabled debug
# Don't strip in debug mode
%set_strip_method none
%endif #enabled_debug
%set_compress_method bzip2
# due to libmudflap and libgnarl
%set_verify_elf_method unresolved=relaxed

# Build parameters.
%def_enable compat
%def_disable debug
%def_enable multilib
%def_with cxx
%def_with fortran
%ifnarch %arm ppc ppc64
%def_with objc
%else
%def_without objc
%endif
%def_disable objc_gc
%def_with treelang
%def_without java
%def_disable plugin
%def_without ada
%def_without pdf
%def_disable check

Source: %srcfilename.tar
Source1: NEWS.gcc
Source2: README.Bugs

# RH patches.
Patch101: gcc41-rh-ice-hack.patch
Patch102: gcc41-rh-ppc64-m32-m64-multilib-only.patch
Patch103: gcc41-rh-ia64-libunwind.patch
Patch104: gcc41-rh-gnuc-rh-release.patch
Patch105: gcc41-rh-alt-java-nomulti.patch
Patch106: gcc41-rh-ada-pr18302.patch
Patch107: gcc41-rh-ada-tweaks.patch
Patch108: gcc41-rh-java-slow_pthread_self.patch
Patch109: gcc41-rh-ppc32-retaddr.patch
Patch110: gcc41-rh-dsohandle.patch
Patch111: gcc41-rh-rh184446.patch
Patch112: gcc41-rh-pr20297-test.patch
Patch113: gcc41-rh-hash-style-gnu.patch
Patch114: gcc41-rh-alt-java-libdotdotlib.patch
Patch115: gcc41-rh-pr28755.patch
Patch116: gcc41-rh-pr27898.patch
Patch119: gcc41-rh-pr32139.patch
Patch121: gcc41-rh-rh235008.patch
Patch122: gcc41-rh-pr31748.patch
Patch123: gcc41-rh-pr28690.patch
Patch124: gcc41-rh-pr32468.patch
Patch125: gcc41-rh-pr32468-2.patch
Patch126: gcc41-rh-rh245424.patch
Patch127: gcc41-rh-pr32550.patch
Patch128: gcc41-rh-rh247256.patch
Patch200: gcc41-rh-pr29703.patch
Patch201: gcc41-rh-libjava-anonverscript.patch
Patch202: gcc41-rh-ppc64-libffi-unwind.patch
Patch203: gcc41-rh-alt-pr30110.patch

# Debian patches.
Patch301: gcc41-deb-gcc-textdomain.patch
Patch302: gcc41-deb-libstdc++-doclink.patch
Patch303: gcc41-deb-libstdc++-doxygen.patch
Patch304: gcc41-deb-classmap-path.patch
Patch305: gcc41-deb-protoize.patch
Patch306: gcc41-deb-ada-link-lib.patch
Patch307: gcc41-deb-ada-gcc-name.patch
Patch308: gcc41-deb-armv4-eabi.patch

# SuSE patches.
#Patch501:

# MDK patches.
#Patch601:

# ALT patches.
Patch701: gcc41-alt-install.patch
Patch702: gcc41-alt-nowrap.patch
Patch703: gcc41-alt-as-needed.patch
Patch704: gcc41-alt-libmudflapth.patch
Patch705: gcc41-alt-libjava-makefile.patch
Patch706: gcc41-alt-libgnarl-makefile.patch
Patch707: gcc41-up-pr27096.patch
Patch708: gcc41-alt-spp-buffer-size.patch
Patch709: gcc41-alt-cpp_unique_options-cc1_options.patch
Patch710: gcc41-alt-nomultilib.patch
Patch711: gcc41-up-pr24998-arm-gnueabi.patch
Patch712: gcc41-up-pr30486.patch
Patch713: gcc41-up-pr28516.patch
Patch714: gcc41-alt-arm-cflags.patch
Patch715: gcc41-alt-makeinfo.patch

Provides: gcc = %version-%release, %_bindir/%_target_platform-gcc, %_bindir/gcc
Obsoletes: egcs, gcc3.0, gcc3.1
Conflicts: glibc-devel < 2.2.6
PreReq: %alternatives_deps, gcc-common >= 1.4.7
Requires: libgcc%gcc_branch >= %version-%release
Requires: cpp%gcc_branch = %version-%release
Requires: %binutils_deps, glibc-devel

BuildPreReq: rpm-build >= 4.0.4-alt39, %alternatives_deps, %binutils_deps
BuildPreReq: coreutils, flex, glibc-devel-static >= 2.4
# due to manpages
BuildPreReq: perl-Pod-Parser
%{?_with_ada:BuildPreReq: gcc-gnat}
%{?_with_fortran:BuildPreReq: libmpfr-devel}
%{?_with_java:BuildPreReq: fastjar imake jdkgcj libXt-devel libXtst-devel libalsa-devel libart_lgpl-devel libgtk+2-devel libltdl-devel xorg-cf-files zip zlib-devel %{?_enable_plugin:xulrunner-devel}}
%{?_with_objc:%{?_enable_objc_gc:BuildPreReq: libgc-devel}}
%{?_with_pdf:BuildPreReq: tetex-dvips}
%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu, /proc}}

####################################################################
# GCC Compiler

%description
This package contains the GNU Compiler Collection version %version.
You'll need this package in order to compile C code.
It is also required for all other GCC compilers.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
gcc%psuffix
in order to explicitly use the GNU C compiler version %version.

####################################################################
# GCC library

%package -n libgcc%gcc_branch
Summary: GCC shared support library
Group: System/Libraries
Provides: libgcc = %version-%release
Provides: libgcc3.2 = %version-%release
Provides: libgcc3.3 = %version-%release
Provides: libgcc3.4 = %version-%release
Obsoletes: libgcc <= %version, libgcc3.0, libgcc3.1, libgcc3.2, libgcc3.3, libgcc3.4
Conflicts: libgcc > %version

%description -n libgcc%gcc_branch
This package contains GCC shared support library which is needed
e.g. for exception handling support.

%package -n libgcc%gcc_branch-debug
Summary: GCC shared support library with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libgcc%gcc_branch = %version-%release

%description -n libgcc%gcc_branch-debug
This package contains GCC shared support library with debugging information.
You need this only if you want to step into GCC shared support library
routines during debugging.

####################################################################
# OpenMP library

%package -n libgomp%gcc_branch
Summary: GCC OpenMP shared support library
Group: System/Libraries
Provides: libgomp = %version-%release
Conflicts: libgomp > %version

%description -n libgomp%gcc_branch
This package contains GCC OpenMP shared support library.

%package -n libgomp%gcc_branch-devel
Summary: GCC OpenMP support files
Group: Development/Other
Provides: libgomp-devel = %version-%release
Requires: libgomp%gcc_branch >= %version-%release
Requires: glibc-devel

%description -n libgomp%gcc_branch-devel
This package contains GCC OpenMP headers and library.

%package -n libgomp%gcc_branch-devel-static
Summary: GCC OpenMP static support library
Group: Development/Other
Provides: libgomp-devel-static = %version-%release
Requires: libgomp%gcc_branch-devel = %version-%release

%description -n libgomp%gcc_branch-devel-static
This package contains GCC OpenMP static library.

%package -n libgomp%gcc_branch-debug
Summary: GCC OpenMP shared support library with debugging information
Group: Development/Other
AutoProv: yes, nolib
Requires: libgomp%gcc_branch = %version-%release

%description -n libgomp%gcc_branch-debug
This package contains GCC OpenMP shared support library with debugging
information.
You need this only if you want to step into GCC OpenMP shared support
library routines during debugging.

####################################################################
# mudflap library

%package -n libmudflap%gcc_branch
Summary: GCC mudflap shared support libraries
Group: System/Libraries
Provides: libmudflap = %version-%release
Conflicts: libmudflap > %version

%description -n libmudflap%gcc_branch
This package contains GCC shared support libraries which are needed for
mudflap support.

%package -n libmudflap%gcc_branch-devel
Summary: GCC mudflap support files
Group: Development/Other
Provides: libmudflap-devel = %version-%release
Requires: libmudflap%gcc_branch >= %version-%release
Requires: glibc-devel

%description -n libmudflap%gcc_branch-devel
This package contains headers and libraries for building
mudflap-instrumented programs.
To instrument a non-threaded program, add -fmudflap option to GCC and
when linking add -lmudflap, for threaded programs also add -fmudflapth
and -lmudflapth.

%package -n libmudflap%gcc_branch-devel-static
Summary: GCC mudflap static support libraries
Group: Development/Other
Provides: libmudflap-devel-static = %version-%release
Requires: libmudflap%gcc_branch-devel = %version-%release

%description -n libmudflap%gcc_branch-devel-static
This package contains static libraries for building statically linked
mudflap-instrumented programs.

%package -n libmudflap%gcc_branch-debug
Summary: GCC mudflap shared support libraries with debugging information
Group: Development/Other
AutoProv: yes, nolib
Requires: libmudflap%gcc_branch = %version-%release

%description -n libmudflap%gcc_branch-debug
This package contains GCC shared support libraries with debugging
information.

####################################################################
# Preprocessor

%package -n cpp%gcc_branch
Summary: The GNU C-Compatible Compiler Preprocessor
Group: Development/C
Provides: cpp = %version-%release, %_bindir/cpp
Obsoletes: gcc-cpp, egcs-cpp, cpp = %version, cpp3.0, cpp3.1
PreReq: %alternatives_deps, gcc-common >= 1.4.7

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

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
cpp%psuffix
in order to explicitly use the GNU C Preprocessor version %version.

####################################################################
# C++ Libraries

%package -n libstdc++%gcc_branch
Summary: GNU Standard C++ library
Group: System/Libraries
Provides: libstdc++ = %version-%release
Provides: libstdc++3.4 = %version-%release
Obsoletes: libgcc3.0, libgcc3.1, libstdc++3.4
Conflicts: libstdc++ > %version
Requires: libgcc%gcc_branch >= %version-%release
# due to TLS (#9732)
PreReq: glibc-core >= 6:2.3.6-alt7

%description -n libstdc++%gcc_branch
This package contains a rewritten standard compliant GCC Standard C++
Library.

%package -n libstdc++%gcc_branch-devel
Summary: Header files and libraries for C++ development
Group: Development/C++
Provides: libstdc++-devel = %version-%release, %_libdir/libstdc++.so
Obsoletes: libstdc++-devel = %version, libstdc++3.0-devel, libstdc++3.1-devel
PreReq: %alternatives_deps, gcc-c++-common >= 1.4.7
Requires: libstdc++%gcc_branch >= %version-%release
Requires: glibc-devel

%description -n libstdc++%gcc_branch-devel
This is the GNU implementation of the standard C++ libraries.
This package includes the header files and libraries needed for C++
development.  This includes rewritten implementation of STL.

%package -n libstdc++%gcc_branch-devel-static
Summary: Static libraries for C++ development
Group: Development/C++
Provides: libstdc++-devel-static = %version-%release, %_libdir/libstdc++.a
Obsoletes: libstdc++-devel-static = %version, libstdc++3.0-devel-static, libstdc++3.1-devel-static
PreReq: %alternatives_deps, gcc-c++-common >= 1.4.7
Requires: libstdc++%gcc_branch-devel = %version-%release

%description -n libstdc++%gcc_branch-devel-static
This is the GNU implementation of the standard C++ libraries.
This package includes static library needed for C++ development.

%package -n libstdc++%gcc_branch-devel-precompiled
Summary: Precompiled header files for C++ development
Group: Development/C++
Requires: libstdc++%gcc_branch-devel = %version-%release

%description -n libstdc++%gcc_branch-devel-precompiled
This is the GNU implementation of the standard C++ libraries.
This package includes the precompiled header files for C++ development.

%package -n libstdc++%gcc_branch-debug
Summary: GNU Standard C++ library with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libstdc++%gcc_branch = %version-%release

%description -n libstdc++%gcc_branch-debug
This package contains a rewritten standard compliant GCC Standard C++
Library with debugging information.
You need this only if you want to step into GCC Standard C++ library
routines during debugging.

####################################################################
# C++ Compiler

%package c++
Summary: C++ support for gcc
Group: Development/C++
Provides: gcc-c++ = %version-%release, %_bindir/%_target_platform-g++, %_bindir/g++
Obsoletes: egcs-c++, gcc-c++ = %version, gcc3.0-c++, gcc3.1-c++
PreReq: %alternatives_deps, gcc-c++-common >= 1.4.7
Requires: %name = %version-%release
Requires: libstdc++%gcc_branch-devel = %version-%release

%description c++
This package adds C++ support to the GNU Compiler Collection.
It includes support for most of the current C++ specification,
including templates and exception handling.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
g++%psuffix
in order to explicitly use the GNU C++ compiler version %version.

####################################################################
# Objective-C Libraries

%package -n libobjc%gcc_branch
Summary: Objective-C runtime library
Group: System/Libraries
Provides: libobjc = %version-%release
Provides: libobjc3.3 = %version-%release
Provides: libobjc3.4 = %version-%release
Obsoletes: libobjc <= %version, libobjc3.0, libobjc3.1, libobjc3.2, libobjc3.3, libobjc3.4

%description -n libobjc%gcc_branch
This package contains Objective-C shared library which is needed to run
Objective-C dynamically linked programs.

%package -n libobjc%gcc_branch-devel
Summary: Header files and library for Objective-C development
Group: Development/Other
Provides: libobjc-devel = %version-%release
PreReq: %alternatives_deps, gcc-common >= 1.4.7
Requires: libobjc%gcc_branch = %version-%release
Requires: glibc-devel

%description -n libobjc%gcc_branch-devel
This is the GNU implementation of the standard Objective-C libraries.
This package includes the header files and library needed for
Objective-C development.

%package -n libobjc%gcc_branch-devel-static
Summary: Static libraries for Objective-C development
Group: Development/Other
Provides: libobjc-devel-static = %version-%release
PreReq: gcc-common >= 1.4.7
Requires: libobjc%gcc_branch-devel = %version-%release

%description -n libobjc%gcc_branch-devel-static
This is the GNU implementation of the standard Objective-C libraries.
This package includes the static library needed for Objective-C
development.

%package -n libobjc%gcc_branch-debug
Summary: Objective-C runtime library with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libobjc%gcc_branch = %version-%release

%description -n libobjc%gcc_branch-debug
This package contains Objective-C shared library with debugging
information.  You need this only if you want to step into GCC Objective-C
shared library routines during debugging.

####################################################################
# Objective-C Compiler

%package objc
Summary: Objective-C support for GCC
Group: Development/Other
Provides: gcc-objc = %version-%release
Obsoletes: gcc-objc = %version, gcc3.0-objc, gcc3.1-objc
PreReq: %alternatives_deps, gcc-common >= 1.4.7
Requires: %name = %version-%release
Requires: libobjc%gcc_branch-devel = %version-%release

%description objc
This package provides Objective-C support for the GCC.
Mainly used on systems running NeXTSTEP, Objective-C is an
object-oriented derivative of the C language.

%package objc++
Summary: Objective-C++ support for GCC
Group: Development/Other
Provides: gcc-objc++ = %version-%release
PreReq: %alternatives_deps, gcc-common >= 1.4.7
Requires: %name-objc = %version-%release, %name-c++ = %version-%release

%description objc++
This package provides Objective-C++ support for the GCC.

####################################################################
# Treelang Compiler

%package treelang
Summary: Treelang support for gcc
Group: Development/Other
Provides: gcc-treelang = %version-%release
PreReq: %alternatives_deps, gcc-treelang-common >= 1.4.7
Requires: %name = %version-%release

%description treelang
This package provides the GNU Treelang compiler.

####################################################################
# GNU Fortran Library

%package -n libgfortran%gcc_branch
Summary: GNU Fortran runtime library
Group: System/Libraries
Provides: libgfortran = %version-%release

%description -n libgfortran%gcc_branch
This package contains GNU Fortran shared library which is needed to run
GNU Fortran dynamically linked programs.

%package -n libgfortran%gcc_branch-devel
Summary: Header files and library for GNU Fortran development
Group: Development/Other
Provides: libgfortran-devel = %version-%release
PreReq: gcc-fortran-common >= 1.4.7
Requires: libgfortran%gcc_branch = %version-%release
Requires: glibc-devel

%description -n libgfortran%gcc_branch-devel
This is the GNU implementation of the standard GNU Fortran libraries.
This package includes the header files and library needed for GNU
Fortran development.

%package -n libgfortran%gcc_branch-devel-static
Summary: Static libraries for GNU Fortran development
Group: Development/Other
Provides: libgfortran-devel-static = %version-%release
PreReq: gcc-fortran-common >= 1.4.7
Requires: libgfortran%gcc_branch-devel = %version-%release

%description -n libgfortran%gcc_branch-devel-static
This is the GNU implementation of the standard GNU Fortran libraries.
This package includes the static library needed for GNU Fortran
development.

%package -n libgfortran%gcc_branch-debug
Summary: GNU Fortran runtime library with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libgfortran%gcc_branch = %version-%release

%description -n libgfortran%gcc_branch-debug
This package contains GNU Fortran shared library with debugging
information.  You need this only if you want to step into GNU Fortran
shared library routines during debugging.

####################################################################
# GNU Fortran Compiler

%package fortran
Summary: GNU Fortran support for gcc
Group: Development/Other
Provides: gcc-fortran = %version-%release
Provides: gcc-g77 = %version-%release
Provides: %_bindir/%_target_platform-gfortran, %_bindir/gfortran
Provides: %_bindir/%_target_platform-g77, %_bindir/g77
Obsoletes: gcc-g77 = %version, gcc3.0-g77, gcc3.1-g77
PreReq: %alternatives_deps, gcc-fortran-common >= 1.4.7
Requires: %name = %version-%release, libgfortran%gcc_branch-devel = %version-%release

%description fortran
This package provides support for compiling GNU Fortran
programs with the GNU Compiler Collection.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
fortran%psuffix
in order to explicitly use the GNU Fortran compiler version %version.

####################################################################
# Java Libraries

%package -n libgcj_bc%gcc_branch
Summary: GNU libgcj_bc shared library
Group: System/Libraries
Provides: libgcj_bc = %version-%release
Conflicts: libgcj_bc > %version
Conflicts: libgcj%gcc_branch < 0:%version-%release,  libgcj4.3 < 0:4.3.2-alt4

%description -n libgcj_bc%gcc_branch
This package contains GNU libgcj_bc shared library.

%package -n libgcj%gcc_branch
Summary: GNU Java runtime libraries
Group: System/Libraries
Provides: libgcj = %version-%release
Obsoletes: libgcj = %version, libgcj3.0, libgcj3.1, libgcj3.2
Requires: libgcj_bc%gcc_branch >= %version-%release, libgcj-common, zip >= 2.1

%description -n libgcj%gcc_branch
The Java(tm) runtime library. You will need this package to run your Java
programs compiled using the Java compiler from GNU Compiler Collection (gcj).

%package -n libgcj%gcc_branch-plugins
Summary: GNU Java plugins
Group: System/Libraries
Provides: libgcj-plugins = %version-%release
Obsoletes: libgcj-plugins = %version, libgcj3.0-plugins, libgcj3.1-plugins, libgcj3.2-plugins
Requires: libgcj%gcc_branch = %version-%release

%description -n libgcj%gcc_branch-plugins
The GNU Java plugins.

%package -n libgcj%gcc_branch-devel
Summary: Header files and libraries for Java development
Group: Development/Java
Provides: libgcj-devel = %version-%release
Obsoletes: libgcj-devel = %version, libgcj3.0-devel, libgcj3.1-devel
Conflicts: libgcj3.4-devel < 0:3.4.5-alt5
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

%package -n libgcj%gcc_branch-src
Summary: Java library sources from GCC4 preview
Group: Development/Java
BuildArch: noarch
Requires: libgcj%gcc_branch = %version-%release
Provides: libgcj-src = %version-%release

%description -n libgcj%gcc_branch-src
The Java(tm) runtime library sources for use in Eclipse.

####################################################################
# Java Compiler

%package java
Summary: Java support for gcc
Group: Development/Java
Provides: gcc-java = %version-%release, %_bindir/gcj
Obsoletes: gcc-java <= %version, gcc3.0-java, gcc3.1-java, gcj3.1-tools
PreReq: %alternatives_deps, gcc-java-common >= 1.4.12
Requires: %name = %version-%release, libgcj%gcc_branch-devel = %version-%release
# due to GC requirements:
# GC Warning: Couldn't read /proc/stat
# GC Warning: GC_get_nprocs() returned -1
# Couldn't read /proc/self/stat
Requires: /proc
Conflicts: kaffe < 1.0.7

%description java
This package adds support for compiling Java(tm) programs and
bytecode into native code.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
gcj%psuffix
in order to explicitly use the GNU Java compiler version %version.

####################################################################
# Ada 95 Libraries

%package -n libgnat%gcc_branch
Summary: Ada 95 runtime libraries
Group: System/Libraries
Provides: libgnat = %version-%release

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
PreReq: gcc-common >= 1.4.7
Requires: libgnat%gcc_branch = %version-%release

%description -n libgnat%gcc_branch-devel
This is the GNU implementation of the standard Ada 95 libraries.
This package includes the include files and libraries needed for
Ada 95 development.

%package -n libgnat%gcc_branch-devel-static
Summary: Static libraries for Ada 95 development
Group: Development/Other
Provides: libgnat-devel-static = %version-%release
PreReq: gcc-common >= 1.4.7
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
PreReq: %alternatives_deps, gcc-common >= 1.4.7
Requires: %name = %version-%release, libgnat%gcc_branch-devel = %version-%release

%description gnat
This package provides support for compiling Ada 95
programs with the GNU Compiler Collection.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you may want to execute
gnat%psuffix
in order to explicitly use the GNU Ada compiler version %version.

####################################################################
# GCC localization

%package locales
Summary: The GNU Compiler Collection native language support files
Group: Development/C
BuildArch: noarch
Provides: gcc-locales = %version-%release
Requires: %name = %version-%release

%description locales
This packages contains files required for native language support for
the GNU Compiler Collection.

####################################################################
# GCC documentation

%package doc
Summary: GCC documentation
Group: Development/Other
BuildArch: noarch
Provides: gcc-doc = %version-%release
Obsoletes: gcc-doc <= %version, gcc3.0-doc, gcc3.1-doc, gcc3.2-doc, gcc3.3-doc, gcc3.4-doc
Conflicts: gcc-doc > %version

%description doc
This package contains documentation for the GNU Compiler Collection
version %version.

%prep
%setup -q -n %srcdirname

# Set proper version & contact info.
sed -i 's/4\.1\.3/4.1.2/' gcc/BASE-VER
sed -i \
	-e 's/^\(#define VERSUFFIX "\).*/\1 (%os_release)"/' \
	-e 's,<URL:[^>]*>,<URL:http://bugzilla.altlinux.org/>,' \
	gcc/version.c

# RH patches.
%patch101 -p0
%patch102 -p0
%patch103 -p0
#patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch119 -p0
%patch121 -p0
%patch122 -p0
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0
%patch127 -p0
%patch128 -p0
%patch200 -p0
%patch201 -p0
%patch202 -p0
%patch203 -p0

# Debian patches.
%patch301 -p0
%patch302 -p0
%patch303 -p0
%patch304 -p1
%patch305 -p0
%patch306 -p0
%patch307 -p0
%patch308 -p1

# SuSE patches.
#patch501

# MDK patches.
#patch601

# ALT patches.
%patch701 -p1
%patch702 -p1
%patch703 -p1
%patch704 -p1
%patch705 -p1
#patch706 -p1
%patch707 -p0
%patch708 -p0
%ifnarch ppc ppc64
%patch709 -p0
%patch710 -p2
%endif
%patch711 -p1
%patch712 -p0
%patch713 -p0
%ifarch %arm
%patch714 -p1
%endif
%patch715 -p1

find -type f -name \*.orig -delete -print

# Misdesign in libstdc++.
cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

%set_automake_version 1.9
%set_autoconf_version 2.5
%set_gcc_version %gcc_branch

# Never build with bundled libltdl.
sed -i s/AC_LIBLTDL_CONVENIENCE/AC_LIBLTDL_INSTALLABLE/ \
	libjava/configure.ac

%build
%add_optflags -D_GNU_SOURCE=1 -DHAVE_DECL_ASPRINTF=1 -DHAVE_DECL_VASPRINTF=1
for f in */Makefile.am; do
	d="${f%%/*}"
	if [ "$d/Makefile.am" -nt "$d/Makefile.in" ]; then
		pushd "$d"
		aclocal `sed -ne 's/^ACLOCAL_[A-Z_]*FLAGS[[:space:]]*=[[:space:]]*\(.*\)$/\1/p' Makefile.am`
		automake
		popd
	fi
done

# Hack to avoid building multilib libjava
# This hack is from Fedora's spec;
# we can't make a patch of, as Makefile.in is autogenerated;
# we can't patch Makefile.am directly, as automake
# will see 'else' and 'endif' and complain.
# Der Teufel soll das buserieren.
perl -pi -e 's/^all: all-recursive/ifeq (\$(MULTISUBDIR),)\nall: all-recursive\nelse\nall:\n\techo Multilib libjava build disabled\nendif/' libjava/Makefile.in
perl -pi -e 's/^install: install-recursive/ifeq (\$(MULTISUBDIR),)\ninstall: install-recursive\nelse\ninstall:\n\techo Multilib libjava install disabled\nendif/' libjava/Makefile.in
perl -pi -e 's/^check: check-recursive/ifeq (\$(MULTISUBDIR),)\ncheck: check-recursive\nelse\ncheck:\n\techo Multilib libjava check disabled\nendif/' libjava/Makefile.in

for f in */configure.ac; do
	d="${f%%/*}"
	if [ "$d/configure.ac" -nt "$d/configure" ]; then
		pushd "$d"
		autoconf
		popd
	fi
done

# Do not build fastjar.
sed -i '/maybe-.*-fastjar \\/d' Makefile.in
sed -i 's/ fastjar / /' configure.in configure

./contrib/gcc_update --touch

%define buildtarget build-%_target_platform
rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

%define _configure_script ../configure
%define _configure_target --host=%_target_platform --build=%_target_platform --target=%_target_platform
%remove_optflags %optflags_nocpp %optflags_notraceback
export CC=%__cc \
	CFLAGS="%optflags" \
	CXXFLAGS="%optflags" \
	FFLAGS="%optflags" \
	GCJFLAGS="%optflags" \
	TCFLAGS="%optflags" \
	XCFLAGS="%optflags" \
	ac_cv_file__proc_self_exe=yes \
	#

%configure \
	--program-suffix=%psuffix \
	--with-slibdir=/%_lib \
	--enable-shared \
	--enable-__cxa_atexit \
	--enable-threads=posix \
	--enable-checking=release \
	--with-system-zlib \
	--without-included-gettext \
	%{subst_enable multilib} \
	--enable-languages="c%{?_with_cxx:,c++}%{?_with_fortran:,fortran}%{?_with_objc:,objc%{?_with_cxx:,obj-c++}}%{?_with_treelang:,treelang}%{?_with_java:,java}%{?_with_ada:,ada}" \
	%{?_with_objc:%{?_enable_objc_gc:--enable-objc-gc}} \
	%{?_with_java:--enable-java-awt=gtk %{subst_enable plugin} --with-native-libdir=%_libdir/gcj%psuffix --enable-libgcj-multifile} \
%ifarch %ix86
	--with-cpu=%_target_cpu --with-arch=%_target_cpu --with-tune=pentium4 \
%endif
%ifarch ppc ppc64
	--disable-softfloat --enable-secureplt \
	--with-long-double-128 \
%endif
%ifarch ppc
	--with-cpu=default32 \
%endif
	#

%make_build BOOT_CFLAGS="%optflags" profiledbootstrap

%{?!__buildreqs:%{?!_without_check:%{?!_disable_check:if [ -w /dev/ptmx ]; then make -k check ||:; ../contrib/test_summary ||:; fi}}}

popd #%buildtarget

# build printable documentation
%if_with pdf
(cd gcc/doc; for f in gcc cpp cppinternals; do
  texi2dvi -p -t @afourpaper -t @finalout -I ../doc/include $f.texi
done)
%if_with fortran
(cd gcc/f; for f in gfortran; do
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
	for f in "$d"/*{README,NEWS,LICENSE,THREADS}*; do
		[ -f "$f" ] || continue
		install -pv -m644 "$f" "%buildroot%gcc_doc_dir/$n/"
	done
}

CopyDocs gcc gcc
CopyDocs libgomp libgomp
CopyDocs libmudflap libmudflap

%if_with cxx
CopyDocs g++ gcc/cp
CopyDocs libstdc++ libstdc++-v3
cp -av libstdc++-v3/docs/html %buildroot%gcc_doc_dir/libstdc++/
ln -s documentation.html %buildroot%gcc_doc_dir/libstdc++/html/index.html
%endif #with_cxx

%if_with fortran
CopyDocs gfortran gcc/f
CopyDocs libgfortran libgfortran
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
CopyDocs java gcc/java
CopyDocs libjava libjava
%endif #with_java

%if_with ada
CopyDocs ada gcc/ada
%endif #with_ada

install -pv -m644 %SOURCE1 %SOURCE2 %buildroot%gcc_doc_dir/

pushd %buildtarget
%makeinstall_std
popd #%buildtarget

# Remove install-tools.
rm -r %buildroot{%gcc_target_libdir,%gcc_target_libexecdir}/install-tools

# Rename binaries which will be packaged under alternatives control.
pushd %buildroot%_bindir
	rm gccbug%psuffix %_target_platform-gcc-%version {%_target_platform-,}c++%psuffix
	%{?_with_java:rm addr2name.awk%psuffix}
	for n in \
	  cpp \
	  gcc gcov protoize unprotoize \
	  %{?_with_cxx:g++} \
	  %{?_with_fortran:gfortran} \
	  %{?_with_treelang:gtreelang} \
	  %{?_with_java:gappletviewer gcj gcj-dbtool gcjh gij gjarsigner gjnih gkeytool grmic grmiregistry jcf-dump jv-convert jv-scan} \
	  ; do
		[ -f "%_target_platform-$n%psuffix" ] ||
			mv -v "$n%psuffix" "%_target_platform-$n%psuffix"
		ln -snf "%_target_platform-$n%psuffix" "$n%psuffix"
	done
	%{?_with_ada:ln -s gcc%psuffix gnatgcc}
popd

pushd %buildroot%_libdir
	rm lib*.la %{?_with_java:*/lib*.la}
	rm libssp* libiberty.a %{?_with_java:libffi*}
	mv *.a %buildroot%gcc_target_libdir/
	for f in *.so; do
		v=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
		[ -f "$v" ]
		ln -s ../../../"$v" "%buildroot%gcc_target_libdir/$f"
		rm "$f"
	done
popd
pushd %buildroot/%_lib
	for f in *.so; do
		v=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
		[ -f "$v" ]
		ln -s ../../../../../%_lib/"$v" "%buildroot%gcc_target_libdir/$f"
		rm "$f"
	done
popd

# Relocate gomp files.
mv %buildroot%_libdir/libgomp.spec %buildroot%gcc_target_libdir/
mv %buildroot%_prefix/include/omp.h %buildroot%gcc_target_libdir/include/

# Relocate mudflap files.
mv %buildroot%_prefix/include/mf-runtime.h %buildroot%gcc_target_libdir/include/

%if_with ada
# Dispatch Ada 95 libraries.
pushd %buildroot%gcc_target_libdir
	for n in gnat gnarl; do
		mv adalib/lib$n-*.so.* %buildroot%_libdir/
		rm adalib/lib$n.so.*
		ln -s ../../../lib$n-*.so.* lib$n.so
		ln -s ../../../lib$n-*.so.* lib$n%psuffix.so
	done
	mv adalib/*.a .
popd
%endif #with_ada

%if_with java
# gcj -static doesn't work properly anyway, unless using --whole-archive
find %buildroot \( \
	-name libgcj.a -o \
	-name libgij.a -o \
	-name libgtkpeer.a -o \
	-name libgcj_bc.a -o \
	-name libgcj-tools.a -o \
	-name libjvm.a \) -delete

# Relocate Java headers to version-specific compiler directory.
mv %buildroot%_includedir/ffi*.h %buildroot%gcc_target_libdir/include/
mv %buildroot%_includedir/c++/%version/{java,javax,gnu} %buildroot%gcc_target_libdir/include/
mv %buildroot%_includedir/c++/%version/gcj/* %buildroot%gcc_target_libdir/include/gcj/
rmdir %buildroot%_includedir/c++/%version/gcj

# Fix libgcj.spec and move it to compiler-specific directory.
sed -i 's/lib: /&%%{static:%%eJava programs cannot be linked statically}/' \
	%buildroot%_libdir/libgcj.spec
mv %buildroot%_libdir/libgcj.spec %buildroot%gcc_target_libdir/

mkdir -p %buildroot%_libdir/gcj%psuffix/classmap.db.d

# libgcj-src files
make DESTDIR=%buildroot -C %buildtarget/%_target_platform/libjava install-src.zip
%endif #with_java

# buildreq substitution rules.
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
for n in \
    cpp gcc libgcc \
    libgomp libgomp-devel libgomp-devel-static \
    libmudflap libmudflap-devel libmudflap-devel-static \
    %{?_with_cxx:gcc-c++ libstdc++ libstdc++-devel libstdc++-devel-static} \
    %{?_with_fortran:gcc-fortran libgfortran libgfortran-devel libgfortran-devel-static} \
    %{?_with_ada:gcc-gnat libgnat libgnat-devel libgnat-devel-static} \
    %{?_with_java:gcc-java libgcj libgcj-plugins libgcj-devel} \
    %{?_with_objc:gcc-objc libobjc libobjc-devel libobjc-devel-static %{?_with_cxx:gcc-objc++}} \
    %{?_with_treelang:gcc-treelang} \
    ; do
	pref="${n%%%%-*}"
	suf="${n#$pref}"
	t="${pref}%gcc_branch$suf"
	echo "$n" >"%buildroot%_sysconfdir/buildreqs/packages/substitute.d/$t"
done
chmod 644 %buildroot%_sysconfdir/buildreqs/packages/substitute.d/*

# buildreq ignore rules.
mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name <<EOF
^%gcc_target_libdir(/include)?$
^%gcc_target_libexecdir(/include)?$
EOF

%if_with cxx
# no valid g++ manpage exists in 4.1 series.
rm %buildroot%_man1dir/g++%psuffix.1
ln -s gcc%psuffix.1.bz2 %buildroot%_man1dir/g++%psuffix.1.bz2
%endif #with_cxx

%find_lang gcc%psuffix
%find_lang --append --output gcc%psuffix.lang cpplib%psuffix
%add_findprov_lib_path %_libdir/gcj%psuffix

mkdir -p %buildroot%_libdir/debug
cp -a %buildroot{/%_lib,%_libdir}/*.so.* %buildroot%_libdir/debug/

#install alternatives stuff
install -d %buildroot%_altdir
cat >%buildroot%_altdir/cpp%gcc_branch <<EOF
%_bindir/%_target_platform-cpp	%_bindir/%_target_platform-cpp%psuffix	%priority
%_man1dir/cpp.1.bz2	%_man1dir/cpp%psuffix.1.bz2	%_bindir/%_target_platform-cpp%psuffix
EOF

cat >%buildroot%_altdir/%name <<EOF
%_bindir/%_target_platform-gcc	%_bindir/%_target_platform-gcc%psuffix	%priority
%_bindir/%_target_platform-gcov	%_bindir/%_target_platform-gcov%psuffix	%_bindir/%_target_platform-gcc%psuffix
%_bindir/%_target_platform-protoize	%_bindir/%_target_platform-protoize%psuffix	%_bindir/%_target_platform-gcc%psuffix
%_bindir/%_target_platform-unprotoize	%_bindir/%_target_platform-unprotoize%psuffix	%_bindir/%_target_platform-gcc%psuffix
%_man1dir/gcc.1.bz2	%_man1dir/gcc%psuffix.1.bz2	%_bindir/%_target_platform-gcc%psuffix
%_man1dir/gcov.1.bz2	%_man1dir/gcov%psuffix.1.bz2	%_bindir/%_target_platform-gcc%psuffix
EOF

%if_with cxx
cat >%buildroot%_altdir/c++%gcc_branch <<EOF
%_bindir/%_target_platform-g++	%_bindir/%_target_platform-g++%psuffix	%priority
%_man1dir/g++.1.bz2	%_man1dir/g++%psuffix.1.bz2	%_bindir/%_target_platform-g++%psuffix
EOF
%endif #with_cxx

%if_with fortran
cat >%buildroot%_altdir/gfortran%gcc_branch <<EOF
%_bindir/%_target_platform-gfortran	%_bindir/%_target_platform-gfortran%psuffix	%priority
%_man1dir/gfortran.1.bz2	%_man1dir/gfortran%psuffix.1.bz2	%_bindir/%_target_platform-gfortran%psuffix
EOF
%endif #with_fortran

%if_with treelang
cat >%buildroot%_altdir/gtreelang%gcc_branch <<EOF
%_bindir/%_target_platform-gtreelang	%_bindir/%_target_platform-gtreelang%psuffix	%priority
EOF
%endif #with_treelang

%if_with java
cat >%buildroot%_altdir/java%gcc_branch <<EOF
%_bindir/%_target_platform-gcj	%_bindir/%_target_platform-gcj%psuffix	%priority
$(for i in gappletviewer gcj-dbtool gcjh gij gjarsigner gjnih gkeytool grmic grmiregistry jcf-dump jv-convert jv-scan; do
	echo "%_bindir/%_target_platform-$i	%_bindir/%_target_platform-$i%psuffix	%_bindir/%_target_platform-gcj%psuffix"
done)
$(for i in gcj gappletviewer gcj-dbtool gcjh gij gjarsigner gjnih gkeytool grmic grmiregistry jcf-dump jv-convert jv-scan; do
	echo "%_man1dir/$i.1.bz2	%_man1dir/$i%psuffix.1.bz2	%_bindir/%_target_platform-gcj%psuffix"
done)
EOF
%endif #with_java

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%_altdir/%name
%dir %gcc_doc_dir
%gcc_doc_dir/gcc
%gcc_doc_dir/NEWS.gcc
%gcc_doc_dir/README.Bugs
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
%dir %gcc_target_libdir
%dir %gcc_target_libdir/include
%gcc_target_libdir/SYSCALLS.c.X
%gcc_target_libdir/include/float.h
%gcc_target_libdir/include/iso646.h
%gcc_target_libdir/include/limits.h
%gcc_target_libdir/include/stdarg.h
%gcc_target_libdir/include/stdbool.h
%gcc_target_libdir/include/stddef.h
%gcc_target_libdir/include/syslimits.h
%gcc_target_libdir/include/unwind.h
%gcc_target_libdir/include/varargs.h
%ifarch %ix86 x86_64
%gcc_target_libdir/include/*intrin.h
%gcc_target_libdir/include/mm_malloc.h
%gcc_target_libdir/include/mm3dnow.h
%endif
%gcc_target_libdir/include/README
%gcc_target_libdir/libgcc_s.so
%gcc_target_libdir/crt*.o
%gcc_target_libdir/libgcc*.a
%gcc_target_libdir/libgcov.a
#%gcc_target_libdir/specs
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/collect2

%if_disabled compat
%files -n libgcc%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcc%gcc_branch
/%_lib/libgcc_s.so.*

%files -n libgcc%gcc_branch-debug
%_libdir/debug/libgcc_s.so.*

%files -n libgomp%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgomp%gcc_branch
%_libdir/libgomp.so.*

%files -n libgomp%gcc_branch-debug
%_libdir/debug/libgomp.so.*

%files -n libmudflap%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libmudflap%gcc_branch
%_libdir/libmudflap*.so.*

%files -n libmudflap%gcc_branch-debug
%_libdir/debug/libmudflap*.so.*
%endif # compat

%files -n libgomp%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgomp%gcc_branch-devel
%dir %gcc_target_libdir
%dir %gcc_target_libdir/include
%gcc_target_libdir/include/omp.h
%gcc_target_libdir/libgomp.so
%gcc_target_libdir/libgomp.spec
%dir %gcc_doc_dir
%gcc_doc_dir/libgomp

%files -n libgomp%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgomp%gcc_branch-devel-static
%dir %gcc_target_libdir
%gcc_target_libdir/libgomp.a

%files -n libmudflap%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libmudflap%gcc_branch-devel
%dir %gcc_target_libdir
%dir %gcc_target_libdir/include
%gcc_target_libdir/include/mf-runtime.h
%gcc_target_libdir/libmudflap*.so
%dir %gcc_doc_dir
%gcc_doc_dir/libmudflap

%files -n libmudflap%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libmudflap%gcc_branch-devel-static
%dir %gcc_target_libdir
%gcc_target_libdir/libmudflap*.a

%files -n cpp%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/cpp%gcc_branch
%_altdir/cpp%gcc_branch
%_bindir/cpp%psuffix
%_bindir/%_target_platform-cpp%psuffix
%_man1dir/cpp%psuffix.*
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/cc1

%if_with cxx
%if_disabled compat
%files -n libstdc++%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch
%_libdir/libstdc++.so.*

%files -n libstdc++%gcc_branch-debug
%_libdir/debug/libstdc++.so.*
%endif # compat

%files -n libstdc++%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/libstdc++
%_includedir/c++/*
%exclude %_includedir/c++/*/*/*/*.gch
%dir %gcc_target_libdir
%gcc_target_libdir/libstdc++.so
%gcc_target_libdir/libsupc++.a

%files -n libstdc++%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch-devel-static
%dir %gcc_target_libdir
%gcc_target_libdir/libstdc++.a

%files -n libstdc++%gcc_branch-devel-precompiled
%_includedir/c++/*/*/*/*.gch

%files c++
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-c++
%_altdir/c++%gcc_branch
%dir %gcc_doc_dir
%gcc_doc_dir/g++
%_bindir/g++%psuffix
%_bindir/%_target_platform-g++%psuffix
%_man1dir/g++%psuffix.*
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/cc1plus
%endif #with_cxx

%if_with objc
%files -n libobjc%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libobjc%gcc_branch
%_libdir/libobjc*.so.*

%files -n libobjc%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libobjc%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/libobjc
%dir %gcc_target_libdir
%gcc_target_libdir/libobjc*.so
%dir %gcc_target_libdir/include
%gcc_target_libdir/include/objc

%files -n libobjc%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libobjc%gcc_branch-devel-static
%dir %gcc_target_libdir
%gcc_target_libdir/libobjc*.a

%files -n libobjc%gcc_branch-debug
%_libdir/debug/libobjc*.so.*

%files objc
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-objc
%dir %gcc_doc_dir
%gcc_doc_dir/objc
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/cc1obj

%if_with cxx
%files objc++
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-objc++
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/cc1objplus
%endif #with_cxx
%endif #with_objc

%if_with treelang
%files treelang
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-treelang
%_altdir/gtreelang%gcc_branch
%_bindir/gtreelang%psuffix
%_bindir/%_target_platform-gtreelang%psuffix
%dir %gcc_doc_dir
%gcc_doc_dir/treelang
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/tree1
%endif #with_treelang

%if_with fortran
%files -n libgfortran%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgfortran%gcc_branch
%_libdir/libgfortran.so.*

%files -n libgfortran%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgfortran%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/libgfortran
%dir %gcc_target_libdir
%gcc_target_libdir/libgfortran.so
%gcc_target_libdir/finclude

%files -n libgfortran%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgfortran%gcc_branch-devel-static
%dir %gcc_target_libdir
%gcc_target_libdir/libgfortran.a

%files -n libgfortran%gcc_branch-debug
%_libdir/debug/libgfortran.so.*

%files fortran
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-fortran
%_altdir/gfortran%gcc_branch
%dir %gcc_doc_dir
%gcc_doc_dir/gfortran
%_bindir/gfortran%psuffix
%_bindir/%_target_platform-gfortran%psuffix
%_man1dir/gfortran%psuffix.*
%dir %gcc_target_libdir
%gcc_target_libdir/libgfortranbegin.a
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/f951
%endif #with_fortran

%if_with java
%if_disabled compat
%files -n libgcj_bc%gcc_branch
%_libdir/libgcj_bc*.so.*
%endif # compat

%files -n libgcj%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch
%_libdir/libgcj-*.so.*
%_libdir/libgcj.*.so.*
%_libdir/libgij.so.*
%_datadir/java/libgcj-%version.jar
%dir %_libdir/gcj%psuffix
%dir %_libdir/gcj%psuffix/classmap.db.d
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_libdir/gcj%psuffix/classmap.db
%_libdir/gcj%psuffix/libjvm.so

%files -n libgcj%gcc_branch-plugins
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-plugins
%dir %_libdir/gcj%psuffix
%_libdir/gcj%psuffix/lib*
%exclude %_libdir/gcj%psuffix/libjvm.so

%files -n libgcj%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/boehm-gc
%gcc_doc_dir/libjava
%_pkgconfigdir/libgcj.pc
%dir %gcc_target_libdir
%gcc_target_libdir/libgcj.spec
%gcc_target_libdir/libgcj*.so
%gcc_target_libdir/libgij.so
%dir %gcc_target_libdir/include
%gcc_target_libdir/include/j*.h
%gcc_target_libdir/include/java
%gcc_target_libdir/include/javax
%gcc_target_libdir/include/gnu
%gcc_target_libdir/include/gcj

%files -n libgcj%gcc_branch-debug
%_libdir/debug/libgcj*.so.*
%_libdir/debug/libgij.so.*

%files -n libgcj%gcc_branch-src
%dir %_datadir/java
%_datadir/java/src*.zip
%_datadir/java/libgcj-tools-%version.jar

%files java
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-java
%_altdir/java%gcc_branch
%dir %gcc_doc_dir
%gcc_doc_dir/java
%_bindir/*gappletviewer%psuffix
%_bindir/*gcj%psuffix
%_bindir/*gcj-dbtool%psuffix
%_bindir/*gcjh%psuffix
%_bindir/*gij%psuffix
%_bindir/*gjarsigner%psuffix
%_bindir/*gjnih%psuffix
%_bindir/*gkeytool%psuffix
%_bindir/*grmic%psuffix
%_bindir/*grmiregistry%psuffix
%_bindir/*jcf-dump%psuffix
%_bindir/*jv-convert%psuffix
%_bindir/*jv-scan%psuffix
%_man1dir/gcj%psuffix.*
%_man1dir/gcj-dbtool%psuffix.*
%_man1dir/gcjh%psuffix.*
%_man1dir/gij%psuffix.*
%_man1dir/gjnih%psuffix.*
%_man1dir/grmic%psuffix.*
%_man1dir/grmiregistry%psuffix.*
%_man1dir/jcf-dump%psuffix.*
%_man1dir/jv-convert%psuffix.*
%_man1dir/jv-scan%psuffix.*
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/jc1
%gcc_target_libexecdir/jvgenmain
%endif #with_java

%if_with ada
%files gnat
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-gnat
%_bindir/gnat*
%_bindir/gpr*
%dir %gcc_target_libdir
%gcc_target_libdir/ada*
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/gnat1

%files -n libgnat%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch
%_libdir/libgnat-*.so.*
%_libdir/libgnarl-*.so.*

%files -n libgnat%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch-devel
%gcc_target_libdir/libgna*.so
%ifarch %ix86
%gcc_target_libdir/libgmem.a
%endif
%dir %gcc_doc_dir
%gcc_doc_dir/ada

%files -n libgnat%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgnat%gcc_branch-devel-static
%gcc_target_libdir/libgna*.a

%files -n libgnat%gcc_branch-debug
%_libdir/debug/libgna*
%endif #with_ada

%files locales -f gcc%psuffix.lang

%files doc
%_infodir/cpp*.info*
%_infodir/gcc*.info*
%{?_with_fortran:%_infodir/gfortran.info*}
%{?_with_treelang:%_infodir/treelang.info*}
%{?_with_java:%_infodir/gcj.info*}
%{?_with_ada:%_infodir/gnat*.info*}

%if_with pdf
%doc gcc/doc/cpp*.pdf
%doc gcc/doc/gcc*.pdf
%{?_with_fortran:%doc gcc/doc/gfortran.pdf}
%{?_with_ada:%doc gcc/doc/gnat*.pdf}
%endif #with_pdf

%changelog
* Tue Nov 16 2010 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt10
- Fixed build with new perl.

* Thu Aug 12 2010 Kirill A. Shutemov <kas@altlinux.org> 4.1.2-alt9
- Drop libffi* packages

* Sat Jan 09 2010 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt8
- Disabled packaging of libgomp4.1 and libmudflap4.1 subpackages
  obsoleted by newer subpackages from gcc4.4.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt7
- Disabled packaging of libgcc4.1, libstdc++4.1 and libgcj_bc4.1
  subpackages obsoleted by newer subpackages from gcc4.4.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt6
- Removed obsolete %%install_info/%%uninstall_info calls.

* Fri Oct 31 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt5
- Fixed build with glibc-2.9.
- Fixed several 4.3.x coexistance issues.
- Disabled java and ada subpackages, 4.3+ should be enough.
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Switched to alternatives-0.4.
- Packaged gcc4.1-locales, gcc4.1-doc and libgcj4.1-src subpackages as noarch.

* Fri Oct 17 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt4
- Relaxed dependencies on libgcc, libstdc++ and libgfortran,
  this is required to allow coexistance with libgcc4.3,
  libstdc++4.3 and libgfortran4.3.
- Disabled fastjar build and packaging,
  it now lives in separate package.

* Sun Jun 08 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt3
- Removed c++filt from alternatives (at@).
- Added libgcj-src subpackage (viy@).
- Moved NLS files to new locales subpackage (closes: #11510).
- Do not package changelog files.

* Mon Mar 03 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt2
- Fixed build with fresh makeinfo (avm@).

* Thu Feb 21 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt1
- Updated to RH gcc-4.1.2-14.el5.

* Wed Oct 31 2007 Alex V. Myltsev <avm@altlinux.ru> 4.1.1-alt12
- Enabled multilib.

* Tue Jan 23 2007 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt11
- Updated to FC gcc-4.1.1-51.

* Sat Oct 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt10
- Updated to FC gcc-4.1.1-30.
- Removed libssp* subpackages (#10119).

* Sun Oct 08 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt9
- Added -D_FORTIFY_SOURCE=2 to default preprocessor options.
- Added -fstack-protector to default compiler options.
- Changed PARAM_SSP_BUFFER_SIZE from 8 to 4.

* Sun Oct 01 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt8
- Updated to FC gcc-4.1.1-28.
- Added --hash-style=gnu to default link options.

* Wed Sep 20 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt7
- Updated to FC gcc-4.1.1-24.
- Added /proc to java subpackage requirements.

* Tue Sep 12 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt6
- Updated to FC gcc-4.1.1-21.

* Fri Sep 08 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt5
- Updated to FC gcc-4.1.1-20.

* Thu Jun 29 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt4
- Updated to FC gcc-4.1.1-6.
- libstdc++4.1: Add requirement on glibc-core >= 6:2.3.6-alt7 (#9732).

* Thu Jun 22 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt3
- Updated to FC gcc-4.1.1-5.

* Tue Jun 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt2
- Updated to FC gcc-4.1.1-2.

* Thu May 25 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt1
- Updated to FC gcc-4.1.1-1.

* Fri May 19 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt4
- Updated to FC gcc-4.1.0-19.

* Mon May 15 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt3
- Updated to FC gcc-4.1.0-18.

* Sun May 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt2
- Updated to FC gcc-4.1.0-17.

* Sat May 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt1.1
- Corrected libgfortran%gcc_branch dependencies.

* Sat May 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt1
- Updated to FC gcc-4.1.0-16.

* Tue May 09 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.8
- Updated to FC gcc-4.1.0-15.

* Mon May 08 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.7
- Updated to FC gcc-4.1.0-14.

* Wed May 03 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.6
- Updated to FC gcc-4.1.0-13.

* Mon May 01 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.5
- Updated to FC gcc-4.1.0-12.

* Tue Apr 25 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.4
- Updated to FC gcc-4.1.0-11.

* Fri Apr 21 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.3
- Updated to FC gcc-4.1.0-10.

* Thu Apr 20 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.2
- Updated to FC gcc-4.1.0-9.

* Fri Apr 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.0-alt0.1
- Updated to FC gcc-4.1.0-8.
- Reviewed and updated patches.
- Reviewed and updated package dependencies.

* Thu Mar 09 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt2
- Relocated ffitarget.h (#9213).

* Wed Mar 08 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt1
- Updated to 3_4-rhl-branch 20051201 (RH gcc-3.4.5-2).

* Thu Mar 02 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt4
- Pass --as-needed option to GNU ld by default.
- Fixed build with make >= 3.81beta4.
- Fixed deplibs build issues on x86_64.
- Bootstrapped gnat for x86_64.
- Updated build dependencies.

* Thu Oct 20 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt3
- Fixed libgcj build to link with system libltdl.

* Wed Oct 12 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt2
- Updated to 3_4-rhl-branch 20050721 (RH gcc-3.4.4-2).
- Moved libgcj AWT peer library to separate subpackage.

* Thu Jun 23 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt1
- Updated to 3_4-rhl-branch 20050608.
- Reenabled java by default on all arches.
- Enabled build with make-3.81beta3.

* Fri Mar 18 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt6
- Merged with gcc-3_4-branch 20050314.
- Enabled testsuite by default.
- Packaged precompiled header files in separate subpackage.

* Mon Feb 28 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt5
- Updated to gcc-3_4-branch 20050222 (RH gcc-3.4.3-20).
- Removed bogus install dependence on make.
- Upgraded build and install dependencies on binutils.

* Sat Feb 12 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt4
- Updated to gcc-3_4-branch 20050210 (RH gcc-3.4.3-18).

* Tue Feb 08 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt3
- Updated to gcc-3_4-branch 20050125 (RH gcc-3.4.3-17).

* Thu Jan 13 2005 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt2
- Updated to gcc-3_4-branch 20050105 (RH gcc-3.4.3-13).
- Converted alternatives config files to new format (0.2.0).

* Thu Dec 30 2004 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt1
- Updated to gcc-3_4-branch 20041227 (RH gcc-3.4.3-11).

* Tue Dec 28 2004 Dmitry V. Levin <ldv@altlinux.org> 3.4.3-alt0.1
- Updated to gcc-3_4-branch 20041213 (RH gcc-3.4.3-10).
- Reviewed and updated patches.
- Reviewed and updated package dependencies.

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
- Relocated libgcc_s.so to %%gcc_target_libdir.
- Changed %%gcc_target_libdir/*.so symlink values.
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
