Group: Development/C
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires(pre): rpm-macros-valgrind
%ifarch %valgrind_arches
BuildRequires: /usr/bin/valgrind
%endif
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:			ppl
Version:		1.2
Release:		alt2_21
Summary:		The Parma Polyhedra Library: a library of numerical abstractions
License:		GPLv3+
URL:			http://www.bugseng.com/ppl
Source0:		http://www.bugseng.com/products/ppl/download/ftp/releases/%{version}/%{name}-%{version}.tar.bz2
Source1:		ppl.hh
Source2:		ppl_c.h
# Fix configure test compromised by LTO
Patch0:			configure.patch
# Adapt to swipl 8.2.x
Patch1:			%{name}-pl82.patch

BuildRequires:		gcc-c++
BuildRequires:		automake
BuildRequires:		libtool
BuildRequires:		libgmp-devel libgmpxx-devel
BuildRequires:		m4
BuildRequires:		perl-devel
BuildRequires:		perl(Getopt/Long.pm)
BuildRequires:		perl(strict.pm)
BuildRequires:		perl(warnings.pm)
BuildRequires:		sharutils
Source44: import.info

%description
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

%package devel
Group: Development/C
Summary:	Development tools for the Parma Polyhedra Library C and C++ interfaces
Requires:	%{name} = %{version}-%{release}

%description devel
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.

%package static
Group: Development/C
Summary:	Static archives for the Parma Polyhedra Library C and C++ interfaces

%description static
The static archives for the Parma Polyhedra Library C and C++ interfaces.

%package utils
Group: Development/C
Summary:	Utilities using the Parma Polyhedra Library
Requires:	%{name} = %{version}-%{release}
BuildRequires:	libglpk-devel >= 4.13

%description utils
This package contains the mixed integer linear programming solver ppl_lpsol.
the program ppl_lcdd for vertex/facet enumeration of convex polyhedra,
and the parametric integer programming solver ppl_pips.

# This is the explicit list of arches gprolog supports
%if 0
%package gprolog
Group: Development/C
# The `gprolog' package is not available on ppc64:
# the GNU Prolog interface must thus be disabled for that architecture.
Summary:	The GNU Prolog interface of the Parma Polyhedra Library
BuildRequires:	gprolog >= 1.3.2
Requires:	%{name} = %{version}-%{release}, gprolog >= 1.3.2

%description gprolog
This package adds GNU Prolog support to the Parma Polyhedra Library (PPL).
Install this package if you want to use the library in GNU Prolog programs.
%endif

# This is the explicit list of arches gprolog supports
%if 0
%package gprolog-static
Group: Development/C
Summary:	The static archive for the GNU Prolog interface of the Parma Polyhedra Library
Requires:	%{name}-gprolog = %{version}-%{release}

%description gprolog-static
This package contains the static archive for the GNU Prolog interface
of the Parma Polyhedra Library.
%endif

%package swiprolog
Group: Development/C
Summary:	The SWI-Prolog interface of the Parma Polyhedra Library
BuildRequires:	swi-prolog-nox >= 5.10.2, swi-prolog-nox >= 5.10.2
Requires:	%{name} = %{version}-%{release}, swi-prolog-nox >= 5.10.2

# This can be removed when F35 reaches EOL
Obsoletes:      swiprolog-static < 1.2-13
Provides:       swiprolog-static = %{version}-%{release}

%description swiprolog
This package adds SWI-Prolog support to the Parma Polyhedra Library.
Install this package if you want to use the library in SWI-Prolog programs.

%package java
Group: Development/C
Summary:	The Java interface of the Parma Polyhedra Library
BuildRequires:	java-devel
BuildRequires:	javapackages-tools
Requires:	java-headless
Requires:	%{name} = %{version}-%{release}

%description java
This package adds Java support to the Parma Polyhedra Library.
Install this package if you want to use the library in Java programs.

%package java-javadoc
Group: Development/C
Summary:	Javadocs for %{name}-java
Requires:	%{name}-java = %{version}-%{release}
BuildArch: noarch

%description java-javadoc
This package contains the API documentation for Java interface
of the Parma Polyhedra Library.

%package docs
Group: Development/C
Summary:	Documentation for the Parma Polyhedra Library
Requires:	%{name} = %{version}-%{release}
BuildArch: noarch

%description docs
This package contains all the documentations required by programmers
using the Parma Polyhedra Library (PPL).
Install this package if you want to program with the PPL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1


# Fix detection of C++11 features
sed -i 's,== 201103L,>= 201103L,g' m4/ac_check_cxx11.m4

# Regenerate configure
autoreconf -fiv

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
CPPFLAGS="-I`swipl --dump-runtime-variables | grep PLBASE= | sed 's/PLBASE="\(.*\)";/\1/'`/include"
# This is the explicit list of arches gprolog supports
%if 0
CPPFLAGS="$CPPFLAGS -I%{_libdir}/gprolog-`gprolog --version 2>&1 | head -1 | sed -e "s/.* \([^ ]*\)$/\1/g"`/include"
%endif
# The javah tool was removed in JDK 10
if [ ! -e %{_bindir}/javah ]; then
  export JAVAH="%{_bindir}/javac"
  sed -e 's/\$(JAVAC)/& -h . -source 1.8 -target 1.8/' \
      -e '/^java_cxx_headers\.stamp$/d' \
      -i interfaces/Java/parma_polyhedra_library/Makefile.in
fi
CPPFLAGS="$CPPFLAGS -I%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux"
%configure --docdir=%{_datadir}/doc/%{name} --enable-shared --disable-rpath --enable-interfaces="cxx c gnu_prolog swi_prolog java" CPPFLAGS="$CPPFLAGS"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std INSTALL="install -p"
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/%{name}/*.la

# Do not install the swiprolog-static file, since pl-static no longer exists
rm -f %{buildroot}%{_libdir}/%{name}/libppl_swiprolog.a

# In order to avoid multiarch conflicts when installed for multiple
# architectures (e.g., i386 and x86_64), we rename the header files
# of the ppl-devel package.  They are substituted with ad-hoc 
# switchers that select the appropriate header file depending on
# the architecture for which the compiler is compiling.

# Since our header files only depend on the sizeof things, we smash
# ix86 onto i386 and arm* onto arm.  For the SuperH RISC engine family,
# we smash sh3 and sh4 onto sh.
normalized_arch=%{_arch}
%ifarch %{ix86}
normalized_arch=i386
%endif
%ifarch %{arm}
normalized_arch=arm
%endif
%ifarch sh3 sh4
normalized_arch=sh
%endif

mv %{buildroot}/%{_includedir}/ppl.hh %{buildroot}/%{_includedir}/ppl-${normalized_arch}.hh
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/ppl.hh
mv %{buildroot}/%{_includedir}/ppl_c.h %{buildroot}/%{_includedir}/ppl_c-${normalized_arch}.h
install -m644 %{SOURCE2} %{buildroot}/%{_includedir}/ppl_c.h

# Install the Javadocs for ppl-java.
mkdir -p %{buildroot}%{_javadocdir}
mv \
%{buildroot}/%{_datadir}/doc/%{name}/ppl-user-java-interface-%{version}-html \
%{buildroot}%{_javadocdir}/%{name}-java

%files
%doc %{_datadir}/doc/%{name}/BUGS
%doc %{_datadir}/doc/%{name}/COPYING
%doc %{_datadir}/doc/%{name}/CREDITS
%doc %{_datadir}/doc/%{name}/NEWS
%doc %{_datadir}/doc/%{name}/README
%doc %{_datadir}/doc/%{name}/README.configure
%doc %{_datadir}/doc/%{name}/TODO
%doc %{_datadir}/doc/%{name}/gpl.txt
%{_libdir}/libppl.so.*
%{_libdir}/libppl_c.so.*
%{_bindir}/ppl-config
%{_mandir}/man1/ppl-config.1*
%dir %{_libdir}/%{name}
%dir %{_datadir}/doc/%{name}
%dir %{_datadir}/ppl/

%files devel
%{_includedir}/ppl*.hh
%{_includedir}/ppl_c*.h
%{_libdir}/libppl.so
%{_libdir}/libppl_c.so
%{_mandir}/man3/libppl.3*
%{_mandir}/man3/libppl_c.3*
%{_datadir}/aclocal/ppl.m4
%{_datadir}/aclocal/ppl_c.m4

%files static
%{_libdir}/libppl.a
%{_libdir}/libppl_c.a

%files utils
%{_bindir}/ppl_lcdd
%{_bindir}/ppl_lpsol
%{_bindir}/ppl_pips
%{_mandir}/man1/ppl_lcdd.1*
%{_mandir}/man1/ppl_lpsol.1*
%{_mandir}/man1/ppl_pips.1*

%if 0
%files gprolog
%doc interfaces/Prolog/GNU/README.gprolog
%{_bindir}/ppl_gprolog
%{_datadir}/ppl/ppl_gprolog.pl
%{_libdir}/%{name}/libppl_gprolog.so
%endif

# This is the explicit list of arches gprolog supports
%if 0
%files gprolog-static
%{_libdir}/%{name}/libppl_gprolog.a
%endif

%files swiprolog
%doc interfaces/Prolog/SWI/README.swiprolog
# No longer installed on shared builds
# %%{_bindir}/ppl_pl
%{_libdir}/%{name}/libppl_swiprolog.so
%{_datadir}/%{name}/ppl_swiprolog.pl

%files java
%doc interfaces/Java/README.java
%{_libdir}/%{name}/libppl_java.so
%{_libdir}/%{name}/ppl_java.jar

%files java-javadoc
%{_javadocdir}/%{name}-java

%files docs
%doc %{_datadir}/doc/%{name}/ChangeLog*
%doc %{_datadir}/doc/%{name}/README.doc
%doc %{_datadir}/doc/%{name}/fdl.*
%doc %{_datadir}/doc/%{name}/gpl.pdf
%doc %{_datadir}/doc/%{name}/gpl.ps.gz
%doc %{_datadir}/doc/%{name}/ppl-user-%{version}-html/
%doc %{_datadir}/doc/%{name}/ppl-user-c-interface-%{version}-html/
%doc %{_datadir}/doc/%{name}/ppl-user-prolog-interface-%{version}-html/
%doc %{_datadir}/doc/%{name}/ppl-user-%{version}.pdf
%doc %{_datadir}/doc/%{name}/ppl-user-c-interface-%{version}.pdf
%doc %{_datadir}/doc/%{name}/ppl-user-java-interface-%{version}.pdf
%doc %{_datadir}/doc/%{name}/ppl-user-prolog-interface-%{version}.pdf
%doc %{_datadir}/doc/%{name}/ppl-user-%{version}.ps.gz
%doc %{_datadir}/doc/%{name}/ppl-user-c-interface-%{version}.ps.gz
%doc %{_datadir}/doc/%{name}/ppl-user-java-interface-%{version}.ps.gz
%doc %{_datadir}/doc/%{name}/ppl-user-prolog-interface-%{version}.ps.gz

%changelog
* Tue Oct 31 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.2-alt2_21
- NMU: fixed FTBFS on LoongArch

* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 1.2-alt2_20
- fixed build with LTO

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.2-alt1_20
- new version

