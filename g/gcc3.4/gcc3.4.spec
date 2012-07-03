%define gcc_branch 3.4

Name: gcc%gcc_branch
Version: 3.4.5
Release: alt15

Summary: GNU Compiler Collection
License: GPL
Group: Development/C
Url: http://gcc.gnu.org/
Packager: Dmitry V. Levin <ldv@altlinux.org>

%define priority 340
%define snapshot 20051201
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

# Build parameters.
%def_enable compat
%def_disable debug
%def_disable multilib
%def_with fortran
%def_with objc
%def_disable objc_gc
%def_with treelang
%def_without java
%ifarch %ix86 x86_64
%def_with ada
%else
%def_without ada
%endif
%def_without pdf
%def_disable check

Source: %srcfilename.tar
Source1: NEWS.html
Source2: README.Bugs

# RH patches.
Patch101: gcc34-rh-multi32-hack.patch
Patch102: gcc34-rh-ice-hack.patch
Patch103: gcc34-rh-ppc64-m32-m64-multilib-only.patch
Patch104: gcc34-rh-ia64-lib64.patch
Patch105: gcc34-rh-java-nomulti.patch
Patch106: gcc34-rh-gnuc-rh-release.patch
Patch107: gcc34-rh-pr16104.patch
Patch108: gcc34-rh-var-tracking-fix.patch
Patch109: gcc34-rh-i386-movsi-insv.patch
Patch110: gcc34-rh-pr18925.patch
Patch111: gcc34-rh-pr14084.patch
Patch112: gcc34-rh-hashtab-recursion.patch
Patch113: gcc34-rh-java-jnilink.patch
Patch114: gcc34-rh-pr21955.patch
Patch115: gcc34-rh-vsb-stack.patch
Patch116: gcc34-rh-pr18300.patch
Patch117: gcc34-rh-rh156291.patch
Patch118: gcc34-rh-weakref.patch
Patch119: gcc34-rh-dwarf2-usefbreg.patch
Patch120: gcc34-rh-dwarf2-prefer-1elt-vartracking.patch
Patch121: gcc34-rh-dwarf2-pr20268.patch
Patch122: gcc34-rh-dwarf2-inline-details.patch
Patch123: gcc34-rh-dwarf2-frame_base.patch
Patch124: gcc34-rh-dwarf2-i386-multreg1.patch
Patch125: gcc34-rh-dwarf2-i386-multreg2.patch
Patch126: gcc34-rh-rh176182.patch

# Debian patches.
Patch201: gcc34-deb-gcc-textdomain.patch
Patch202: gcc34-deb-libstdc++-doclink.patch
Patch203: gcc34-deb-protoize.patch
Patch204: gcc34-deb-amd64-specs.patch
Patch205: gcc34-deb-fastjar-update.patch
Patch206: gcc34-deb-gcj-without-rpath.patch
Patch207: gcc34-deb-libffi-soversion.patch
Patch208: gcc34-deb-libobjc.patch
Patch209: gcc34-deb-ada-gcc-name.patch
Patch210: gcc34-deb-cpu-default-i586.patch
Patch211: gcc34-deb-link-libs.patch

# SuSE patches.
#Patch501:

# MDK patches.
Patch601: gcc32-mdk-mklibgcc-serialize-crtfiles.patch
Patch602: gcc32-mdk-multi-do-libdir.patch
Patch603: gcc32-mdk-c++-classfn-member-template.patch
Patch604: gcc32-mdk-pr7768.patch
Patch605: gcc32-mdk-pr8213.patch

# ALT patches.
Patch701: gcc34-alt-install.patch
Patch702: gcc34-alt-nowrap.patch
Patch703: gcc34-alt-as-needed.patch
Patch704: gcc34-alt-makeinfo.patch
Patch705: gcc34-alt-bison.patch

Provides: gcc = %version-%release, %_bindir/%_target_platform-gcc, %_bindir/gcc
Obsoletes: egcs, gcc3.0, gcc3.1
Conflicts: glibc-devel < 2.2.6
PreReq: %alternatives_deps, gcc-common >= 1.4.7
Requires: cpp%gcc_branch = %version-%release, libgcc%gcc_branch >= %version-%release
Requires: %binutils_deps, glibc-devel

%set_autoconf_version 2.13
%set_automake_version 1.4
%set_libtool_version 1.4
%set_gcc_version 3.4

BuildPreReq: rpm-build >= 4.0.4-alt39, %alternatives_deps, %binutils_deps
BuildPreReq: coreutils, flex, zlib-devel, glibc-devel-static
# due to manpages
BuildPreReq: perl-Pod-Parser
%{?_with_objc:%{?_enable_objc_gc:BuildPreReq: libgc-devel}}
%{?_with_java:BuildPreReq: imake libXt-devel libart_lgpl-devel libgtk+2-devel libltdl3-devel xorg-cf-files}
%{?_with_ada:BuildPreReq: gcc%gcc_branch-gnat}
%{?_with_pdf:BuildPreReq: tetex-dvips}
%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu, /proc}}

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
Provides: libgcc3.2 = %version-%release, libgcc3.3 = %version-%release
Obsoletes: libgcc <= %version, libgcc3.0, libgcc3.1, libgcc3.2, libgcc3.3
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
Obsoletes: libgcc3.0, libgcc3.1
Conflicts: libstdc++ > %version
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
PreReq: %alternatives_deps, gcc-c++-common >= 1.4.7
Requires: libstdc++%gcc_branch >= %version-%release
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
PreReq: %alternatives_deps, gcc-c++-common >= 1.4.7
Requires: libstdc++%gcc_branch-devel = %version-%release

%description -n libstdc++%gcc_branch-devel-static
This is the GNU implementation of the standard C++ libraries.  This
package includes the static libraries needed for C++ development.

%package -n libstdc++%gcc_branch-devel-precompiled
Summary: Precompiled header files for C++ development
Group: Development/C++
Requires: libstdc++%gcc_branch-devel = %version-%release

%description -n libstdc++%gcc_branch-devel-precompiled
This is the GNU implementation of the standard C++ libraries.  This
package includes the precompiled header files needed for C++ development.

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
PreReq: %alternatives_deps, gcc-c++-common >= 1.4.7
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
Provides: libobjc3.2 = %version-%release, libobjc3.3 = %version-%release
Obsoletes: libobjc <= %version, libobjc3.0, libobjc3.1, libobjc3.2, libobjc3.3
Conflicts: libobjc > %version

%description -n libobjc%gcc_branch
This package contains Objective C shared library which is needed to run
Objective-C dynamically linked programs.

%package -n libobjc%gcc_branch-devel
Summary: Header files and libraries for Objective C development
Group: Development/Other
Provides: libobjc-devel = %version-%release
PreReq: %alternatives_deps, gcc-common >= 1.4.7
Requires: libobjc%gcc_branch >= %version-%release
Requires: glibc-devel

%description -n libobjc%gcc_branch-devel
This is the GNU implementation of the standard Objective C libraries.
This package includes the header files and libraries needed for
Objective C development.

%package -n libobjc%gcc_branch-devel-static
Summary: Static libraries for Objective C development
Group: Development/Other
Provides: libobjc-devel-static = %version-%release
PreReq: gcc-common >= 1.4.7
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
PreReq: %alternatives_deps, gcc-common >= 1.4.7
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
PreReq: %alternatives_deps, gcc-treelang-common >= 1.4.7
Requires: %name = %version-%release

%description treelang
This package provides the GNU Treelang compiler.

####################################################################
# Fortran 77 Library

%package -n libg2c%gcc_branch
Summary: Fortran 77 runtime libraries
Group: System/Libraries
Provides: libg2c = %version-%release, libf2c = %version-%release
Provides: libg2c3.2 = %version-%release, libg2c3.3 = %version-%release
Obsoletes: libf2c, libf2c3.0, libf2c3.1, libg2c3.2, libg2c3.3
Conflicts: libg2c > %version

%description -n libg2c%gcc_branch
This package contains Fortran 77 shared library which is needed to run
Fortran 77 dynamically linked programs.

%package -n libg2c%gcc_branch-devel
Summary: Header files and libraries for Fortran 77 development
Group: Development/Other
Provides: libg2c-devel = %version-%release
PreReq: gcc-fortran-common >= 1.4.7
Requires: libg2c%gcc_branch >= %version-%release
Requires: glibc-devel

%description -n libg2c%gcc_branch-devel
This is the GNU implementation of the standard Fortran 77 libraries.
This package includes the header files and libraries needed for
Fortran 77 development.

%package -n libg2c%gcc_branch-devel-static
Summary: Static libraries for Fortran 77 development
Group: Development/Other
Provides: libg2c-devel-static = %version-%release
PreReq: gcc-fortran-common >= 1.4.7
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
PreReq: %alternatives_deps, gcc-fortran-common >= 1.4.7
Requires: %name = %version-%release, libg2c%gcc_branch-devel = %version-%release

%description g77
This package provides support for compiling Fortran 77
programs with the GNU Compiler Collection.

If you have multiple versions of the GNU Compiler Collection
installed on your system, you will have to type
g77%psuffix
in order to explicitly use the GNU Fortran 77 compiler version %version.

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

%package -n libgcj%gcc_branch-awt
Summary: GNU Java AWT peer library
Group: System/Libraries
Provides: libgcj-awt = %version-%release
Obsoletes: libgcj-awt = %version, libgcj3.0-awt, libgcj3.1-awt
Requires: libgcj%gcc_branch = %version-%release

%description -n libgcj%gcc_branch-awt
The GNU Java AWT peer library.

%package -n libgcj%gcc_branch-devel
Summary: Header files and libraries for Java development
Group: Development/Java
Provides: libgcj-devel = %version-%release
Obsoletes: libgcj-devel = %version, libgcj3.0-devel, libgcj3.1-devel
Requires: libgcj%gcc_branch = %version-%release, libgcj%gcc_branch-awt = %version-%release, zlib-devel

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

%package -n libgcj%gcc_branch-awt-debug
Summary: GNU Java AWT peer library with debugging information
Group: System/Libraries
AutoProv: yes, nolib
Requires: libgcj%gcc_branch-awt = %version-%release

%description -n libgcj%gcc_branch-awt-debug
The GNU Java AWT peer library with debugging information.
You need this only if you want to step into GCC Java(tm) runtime library
routines during debugging.

####################################################################
# Java Compiler

%package java
Summary: Java support for gcc
Group: Development/Java
Provides: gcc-java = %version-%release, %_bindir/gcj
Obsoletes: gcc-java <= %version, gcc3.0-java, gcc3.1-java, gcj3.1-tools
PreReq: %alternatives_deps, gcc-java-common >= 1.4.7
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
installed on your system, you will have to type
gnat%psuffix
in order to explicitly use the GNU Ada compiler version %version.

####################################################################
# GCC documentation

%package doc
Summary: GCC documentation
Group: Development/Other
BuildArch: noarch
Provides: gcc-doc = %version-%release
Obsoletes: gcc-doc <= %version, gcc3.0-doc, gcc3.1-doc, gcc3.2-doc, gcc3.3-doc
Conflicts: gcc-doc > %version

%description doc
This package contains documentation for the GNU Compiler Collection
version %version.

%prep
%setup -n %srcdirname
find -type d -name CVS -print0 |
	xargs -r0 rm -rf --
rm -f gcc/po/*rw.po

# RH patches.
%ifarch sparc ppc
%patch101 -p0
%endif
%patch102 -p0
%patch103 -p0
%ifarch ia64
%if "%_lib" == "lib64"
%patch104 -p0
%endif
%endif
%patch105 -p0
#%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
#%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p0
%patch119 -p0
%patch120 -p0
%patch121 -p0
%patch122 -p0
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0

# Debian patches.
%patch201 -p0
%patch202 -p0
%patch203 -p0
%patch204 -p1
%patch205 -p0
%patch206 -p1
%patch207 -p0
%patch208 -p0
%patch209 -p0
%patch210 -p0
%patch211 -p0

# SuSE patches.
#%patch501 -p0

# MDK patches.
%patch601 -p1
%patch602 -p1

# ALT patches.
%patch701 -p1
%patch702 -p1
%patch703 -p1
%patch704 -p1
%patch705 -p1

find -type f -name \*.orig -delete -print

# Set proper version & contact info.
cp -p gcc/version.c gcc/version.c.orig
%__subst 's/3\.4\.[56]/%version/g' gcc/version.c gcc/doc/include/gcc-common.texi
%__subst 's/\(%gcc_branch\(\.[0-9]\+\)*\)\( [0-9]\+[a-z]*\)\?.*"/\1\3 (%os_release)"/' gcc/version.c
%__subst 's,<URL:[^>]*>,<URL:http://bugzilla.altlinux.ru/>,' gcc/version.c

# Misdesign in libstdc++.
cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

# Link lib-gnu-java-awt-peer-gtk with libgcj.
%__subst -p '/^lib_gnu_java_awt_peer_gtk_la_DEPENDENCIES =/ d' libjava/Makefile.*
%__subst -p 's|^lib_gnu_java_awt_peer_gtk_la_LIBADD = .*|& -L$(here)/.libs libgcj.la\nlib_gnu_java_awt_peer_gtk_la_DEPENDENCIES = libgcj.la libgcj.spec|' libjava/Makefile.*

sleep 1s
%__subst s/AC_LIBLTDL_CONVENIENCE/AC_LIBLTDL_INSTALLABLE/ \
	libjava/configure.in

%build
# Since autoreconf is not available for this package, just override deplibs_check_method.
export lt_cv_deplibs_check_method=pass_all

%if "%_lib" == "lib64"
find -type f -name Makefile\* -print0 |
	xargs -r0 grep -lZ '^[[:alpha:]_]*toolexeclibdir *=' -- |
	xargs -r0 subst -p 's,^\(^[[:alpha:]_]*toolexeclibdir *=\).*,\1 $(libdir),' --
%endif

for f in */configure.in; do
	d="${f%%/*}"
	if [ "$d/configure.in" -nt "$d/configure" ]; then
		pushd "$d"
		autoconf
		popd
	fi
done
for f in */Makefile.am; do
	d="${f%%/*}"
	if [ "$d/Makefile.am" -nt "$d/Makefile.in" ]; then
		pushd "$d"
		automake
		popd
	fi
done

%define buildtarget build-%_target_platform
rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

CC=%__cc
%remove_optflags %optflags_nocpp %optflags_notraceback

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
	--enable-__cxa_atexit \
	--enable-languages="c,c++%{?_with_fortran:,f77}%{?_with_objc:,objc}%{?_with_treelang:,treelang}%{?_with_java:,java}%{?_with_ada:,ada}" \
	--program-suffix=%psuffix \
	%{?_with_objc:%{?_enable_objc_gc:--enable-objc-gc}} \
	%{?_with_java:--enable-java-gc=boehm --enable-java-awt=gtk} \
	--with-system-zlib \
	--without-included-gettext \
	%{subst_enable multilib} \
	--host=%_target_platform --build=%_target_platform --target=%_target_platform

%ifarch %ix86 x86_64
%make_build profiledbootstrap
%else
%make_build bootstrap-lean
%endif

%if_with ada
# SMP-incompatible build.
make -C gcc gnatlib-shared
make -C gcc gnattools
%endif #with_ada

%{?!__buildreqs:%{?!_without_check:%{?!_disable_check:if [ -w /dev/ptmx ]; then make -k check ||:; ../contrib/test_summary ||:; fi}}}

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
ln -s documentation.html %buildroot%gcc_doc_dir/libstdc++/html/index.html

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
CopyDocs libjava libjava
%endif #with_java

%if_with ada
CopyDocs ada gcc/ada
%endif #with_ada

# Compress changelogs.
find %buildroot%gcc_doc_dir -type f -name *ChangeLog\* \! -name \*.bz2 -print0 |
	xargs -r0 bzip2 -9 --

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
	%{?_with_fortran:mv {g77,gfortran}%psuffix}
	%{?_with_treelang:mv {tree1,gtreelang}%psuffix}
	%{?_with_java:mv {jar,fastjar}%psuffix}
	%{?_with_java:mv {,g}rmic%psuffix}
	%{?_with_java:mv {,g}rmiregistry%psuffix}
	for n in \
	  cpp \
	  gcc gcov protoize unprotoize \
	  g++ \
	  %{?_with_fortran:gfortran} \
	  %{?_with_treelang:gtreelang} \
	  %{?_with_java:fastjar gcj gcjh gij jcf-dump jv-convert jv-scan grepjar grmic grmiregistry} \
	  ; do
		[ -f "%_target_platform-$n%psuffix" ] ||
			mv -v "$n%psuffix" "%_target_platform-$n%psuffix"
		ln -snf "%_target_platform-$n%psuffix" "$n%psuffix"
	done
	%{?_with_ada:ln -s gcc%psuffix gnatgcc}
popd

# Relocate libraries to the right directories.
pushd %buildroot%_libdir
	rm -f libiberty.a lib*.la
	mv *.a %buildroot%gcc_target_libdir/
	for f in *.so; do
		v=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
		[ -f "$v" ]
		ln -s ../../../"$v" "%buildroot%gcc_target_libdir/$f"
		rm -f "$f"
	done
popd
pushd %buildroot/%_lib
	for f in *.so; do
		v=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
		[ -f "$v" ]
		ln -s ../../../../../%_lib/"$v" "%buildroot%gcc_target_libdir/$f"
		rm -f "$f"
	done
popd

%if_with ada
# Dispatch Ada 95 libraries.
pushd %buildroot%gcc_target_libdir
	for n in gnat gnarl; do
		mv adalib/lib$n-*.so.* %buildroot%_libdir/
		rm -f adalib/lib$n.so.*
		ln -s ../../../lib$n-*.so.* lib$n.so
		ln -s ../../../lib$n-*.so.* lib$n%psuffix.so
	done
	mv adalib/*.a .
popd
%endif #with_ada

%if_with java
# Relocate Java headers to version-specific compiler directory.
mv %buildroot%_includedir/{ffi,j}*.h %buildroot%gcc_target_libdir/include/
mv %buildroot%_includedir/{java,javax,gnu} %buildroot%gcc_target_libdir/include/
mv %buildroot%_includedir/gcj/* %buildroot%gcc_target_libdir/include/gcj/
rmdir %buildroot%_includedir/gcj

# Fix libgcj.spec and move it to compiler-specific directory.
%__subst -p 's/-lgcjgc//g;s/-lzgcj//g;s/-lpthread//g' %buildroot%_libdir/libgcj.spec
mv %buildroot%_libdir/libgcj.spec %buildroot%gcc_target_libdir/

# Rename libgcj.pc to avoid conflict with libgcj4.1-devel.
mv %buildroot%_pkgconfigdir/libgcj{,%psuffix}.pc
%endif #with_java

# buildreq substitution rules.
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
for n in cpp gcc gcc-c++ gcc-g77 gcc-gnat gcc-java gcc-objc gcc-treelang libg2c libg2c-devel libg2c-devel-static libgcc libgcj libgcj-awt libgcj-devel libgcj-devel-static libgnat libgnat-devel libgnat-devel-static libobjc libobjc-devel libobjc-devel-static libstdc++ libstdc++-devel libstdc++-devel-static; do
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

# no valid g++ manpage exists in 3.4 series.
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

cat >%buildroot%_altdir/c++%gcc_branch <<EOF
%_bindir/%_target_platform-g++	%_bindir/%_target_platform-g++%psuffix	%priority
%_bindir/%_target_platform-c++filt	%_bindir/%_target_platform-c++filt%psuffix	%_bindir/%_target_platform-g++%psuffix
%_man1dir/g++.1.bz2	%_man1dir/g++%psuffix.1.bz2	%_bindir/%_target_platform-g++%psuffix
EOF

%if_with fortran
cat >%buildroot%_altdir/gfortran%gcc_branch <<EOF
%_bindir/%_target_platform-gfortran	%_bindir/%_target_platform-gfortran%psuffix	%priority
%_man1dir/gfortran.1.bz2	%_man1dir/g77%psuffix.1.bz2	%_bindir/%_target_platform-gfortran%psuffix
EOF
%endif

%if_with treelang
cat >%buildroot%_altdir/gtreelang%gcc_branch <<EOF
%_bindir/%_target_platform-gtreelang	%_bindir/%_target_platform-gtreelang%psuffix	%priority
EOF
%endif

%if_with java
cat >%buildroot%_altdir/java%gcc_branch <<EOF
%_bindir/%_target_platform-gcj	%_bindir/%_target_platform-gcj%psuffix	%priority
$(for i in fastjar gcjh gij grepjar grmic grmiregistry jcf-dump jv-convert jv-scan; do
	echo "%_bindir/%_target_platform-$i	%_bindir/%_target_platform-$i%psuffix	%_bindir/%_target_platform-gcj%psuffix"
done)
$(for i in gcj gcjh gij grepjar jcf-dump jv-convert jv-scan; do
	echo "%_man1dir/$i.1.bz2	%_man1dir/$i%psuffix.1.bz2	%_bindir/%_target_platform-gcj%psuffix"
done)
%_man1dir/grmic.1.bz2	%_man1dir/rmic%psuffix.1.bz2	%_bindir/%_target_platform-gcj%psuffix
%_man1dir/fastjar.1.bz2	%_man1dir/jar%psuffix.1.bz2	%_bindir/%_target_platform-gcj%psuffix
%_man1dir/grmiregistry.1.bz2	%_man1dir/rmiregistry%psuffix.1.bz2	%_bindir/%_target_platform-gcj%psuffix
EOF
%endif

%files -f gcc%psuffix.lang
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%_altdir/%name
%dir %gcc_doc_dir
%gcc_doc_dir/gcc
%gcc_doc_dir/NEWS.html
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
%gcc_target_libdir/include/float.h
%gcc_target_libdir/include/*mmintrin.h
%gcc_target_libdir/include/iso646.h
%gcc_target_libdir/include/limits.h
%gcc_target_libdir/include/stdarg.h
%gcc_target_libdir/include/stdbool.h
%gcc_target_libdir/include/stddef.h
%gcc_target_libdir/include/syslimits.h
%gcc_target_libdir/include/unwind.h
%gcc_target_libdir/include/varargs.h
%gcc_target_libdir/include/README
%gcc_target_libdir/libgcc_s.so
%gcc_target_libdir/crt*.o
%gcc_target_libdir/libgcc*.a
%gcc_target_libdir/libgcov.a
%gcc_target_libdir/SYSCALLS.c.X
%gcc_target_libdir/specs
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/collect2

%if_disabled compat
%files -n libgcc%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcc%gcc_branch
/%_lib/libgcc_s.so.*

%files -n libgcc%gcc_branch-debug
%_libdir/debug/libgcc_s.so.*

%files -n libstdc++%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libstdc++%gcc_branch
%_libdir/libstdc++.so.*

%files -n libstdc++%gcc_branch-debug
%_libdir/debug/libstdc++.so.*
%endif # compat

%files -n cpp%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/cpp%gcc_branch
%_altdir/cpp%gcc_branch
%_bindir/cpp%psuffix
%_bindir/%_target_platform-cpp%psuffix
%_man1dir/cpp%psuffix.*
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/cc1

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
%files -n libg2c%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libg2c%gcc_branch
%_libdir/libg2c.so.*

%files -n libg2c%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libg2c%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/libg2c
%dir %gcc_target_libdir
%gcc_target_libdir/libg2c.so
%dir %gcc_target_libdir/include
%gcc_target_libdir/include/g2c.h

%files -n libg2c%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libg2c%gcc_branch-devel-static
%dir %gcc_target_libdir
%gcc_target_libdir/libg2c.a

%files -n libg2c%gcc_branch-debug
%_libdir/debug/libg2c.so.*

%files g77
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-g77
%_altdir/gfortran%gcc_branch
%dir %gcc_doc_dir
%gcc_doc_dir/g77
%_bindir/gfortran%psuffix
%_bindir/%_target_platform-gfortran%psuffix
%_man1dir/g77%psuffix.*
%dir %gcc_target_libdir
%gcc_target_libdir/libfrtbegin.a
%dir %gcc_target_libexecdir
%gcc_target_libexecdir/f771
%endif #with_fortran

%if_with java
%files -n libgcj%gcc_branch
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch
%_libdir/libgcj.so.*
%_libdir/lib-org-*.so.*
%_datadir/java/*

%files -n libgcj%gcc_branch-awt
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-awt
%_libdir/lib-gnu-java-*.so.*

%files -n libgcj%gcc_branch-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-devel
%dir %gcc_doc_dir
%gcc_doc_dir/boehm-gc
%gcc_doc_dir/libjava
%_pkgconfigdir/libgcj%psuffix.pc
%dir %gcc_target_libdir
%gcc_target_libdir/libgcj.spec
%gcc_target_libdir/libgcj.so
%gcc_target_libdir/lib-org-*.so
%gcc_target_libdir/lib-gnu-java-*.so
%dir %gcc_target_libdir/include
%gcc_target_libdir/include/j*.h
%gcc_target_libdir/include/java
%gcc_target_libdir/include/javax
%gcc_target_libdir/include/gnu
%gcc_target_libdir/include/gcj

%files -n libgcj%gcc_branch-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/libgcj%gcc_branch-devel-static
%dir %gcc_target_libdir
%gcc_target_libdir/libgcj.a
%gcc_target_libdir/lib-org-*.a
%gcc_target_libdir/lib-gnu-java-*.a

%files -n libgcj%gcc_branch-debug
%_libdir/debug/libgcj.so.*
%_libdir/debug/lib-org-*.so.*

%files -n libgcj%gcc_branch-awt-debug
%_libdir/debug/lib-gnu-java-*.so.*

%files java
%config %_sysconfdir/buildreqs/packages/substitute.d/%name-java
%_altdir/java%gcc_branch
%dir %gcc_doc_dir
%gcc_doc_dir/fastjar
%gcc_doc_dir/java
%_bindir/*gcj*%psuffix
%_bindir/*gij%psuffix
%_bindir/*jcf-dump%psuffix
%_bindir/*jv-convert%psuffix
%_bindir/*jv-scan%psuffix
%_bindir/*jar%psuffix
%_bindir/*rmi*%psuffix
%_man1dir/gij%psuffix.*
%_man1dir/gcj%psuffix.*
%_man1dir/gcjh%psuffix.*
%_man1dir/jv-convert%psuffix.*
%_man1dir/jv-scan%psuffix.*
%_man1dir/jcf-dump%psuffix.*
%_man1dir/*rmi*%psuffix.*
%_man1dir/*jar%psuffix.*
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
%_datadir/gnat

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

%files doc
%_infodir/cpp*.info*
%_infodir/gcc*.info*
%{?_with_fortran:%_infodir/g77.info*}
%{?_with_treelang:%_infodir/treelang.info*}
%{?_with_java:%_infodir/fastjar.info*}
%{?_with_java:%_infodir/gcj.info*}
%{?_with_ada:%_infodir/gnat*.info*}

%if_with pdf
%doc gcc/doc/cpp*.pdf
%doc gcc/doc/gcc*.pdf
%{?_with_fortran:%doc gcc/doc/g77.pdf}
%{?_with_ada:%doc gcc/doc/gnat*.pdf}
%endif #with_pdf

%changelog
* Fri Dec 16 2011 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt15
- Disabled build and packaging of java subpackages.

* Tue Nov 16 2010 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt14
- Fixed build with new perl.

* Thu Aug 12 2010 Kirill A. Shutemov <kas@altlinux.org> 3.4.5-alt13
- Drop libffi* packages.
- Pack -doc subpackage as noarch.

* Tue Jun 09 2009 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt12
- Fixed build with fresh bison.

* Thu May 21 2009 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt11
- Fixed build with fresh makeinfo.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt10
- Disabled packaging of libgcc3.4 and libstdc++3.4 subpackages
  obsoleted by libgcc4.* and libstdc++4.* subpackages from gcc4.*.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt9
- Removed obsolete %%install_info/%%uninstall_info calls.
- Built with libtool-1.4.

* Tue Feb 10 2009 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt8
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls
- Switched to alternatives-0.4.

* Mon Mar 03 2008 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt7
- Fixed build with fresh makeinfo.

* Wed Sep 13 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt6
- Reenabled gnat.

* Tue Sep 05 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt5
- Changed build to use "%%set_gcc_version 3.4",
  to avoid problems with recent compilers.
- Renamed libgcj.pc -> libgcj-3.4.pc
  to avoid conflict with libgcj4.1-devel.
- Disabled gnat.

* Thu May 11 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt4
- Relaxed requirements on libgcc and libstdc++ to allow
  use of libgcc and libstdc++ from 4.x series.

* Mon May 08 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.5-alt3
- Reworked fortran, treelang and java packaging for compatibility with 4.x.

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
