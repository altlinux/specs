# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name glpk
%define lib_major		40
%define lib_name		lib%{name}%{lib_major}

%define lib_name_devel		lib%{name}-devel

Summary:	GLPK glpsol utility
Name:		glpk
Version:	5.0
Release:	alt1_1
License:	GPLv3+
Group:		Sciences/Mathematics
URL:		http://www.gnu.org/software/glpk/glpk.html
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	libgmp-devel
BuildRequires:	texlive
BuildRequires:	makeinfo texi2dvi
BuildRequires:	texlive-dist
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libgmp-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libsuitesparse-devel

# Un-bundle zlib (#1102855). Upstream won't accept; they want to be
# ANSI-compatible, and zlib makes POSIX assumptions.
Patch0:         %{name}-4.65-unbundle-zlib.patch
# Unbundle suitesparse
Patch1:         %{name}-4.65-unbundle-suitesparse.patch
# Fix violations of the ANSI C strict aliasing rules
Patch2:         %{name}-4.65-alias.patch
# See http://lists.gnu.org/archive/html/bug-glpk/2018-03/msg00000.html
Patch3:         %{name}-4.65-sagemath.patch
Source44: import.info

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the utility glpsol.

%package -n %{lib_name}
Summary:	GLPK shared libraries
Group:		Sciences/Mathematics
Obsoletes:	%{name} < %{version}

%description -n %{lib_name}
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the library needed to run programs dynamically
linked with GLPK.

%package -n %{lib_name_devel}
Summary:	Header files for development with GLPK
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the headers needed to develop applications using
GLPK.

%package        doc	
Group: Sciences/Mathematics
Summary:        Documentation for %{name}
BuildArch: noarch

%description    doc
Documentation subpackage for %{name}.

%prep
%setup -q

%build
export LIBS=-ldl

# Need to rebuild src/Makefile.in from src/Makefile.am
autoreconf -ifs

%configure --disable-static --with-gmp --enable-dl=dlfcn
# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
 sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
     -i libtool
%make_build

# Trust Knuth to produce a single-pass compiler for a multiple-pass language.
pushd doc
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex
popd

%install
make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}
rm -f %{buildroot}%{_libdir}/*.la
	
%check
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$RPM_BUILD_ROOT%{_libdir}"
make check
## Clean up directories that are included in docs
rm -Rf examples/{.deps,.libs,Makefile*,glpsol,glpsol.o} doc/*.tex

%files
%{_bindir}/glpsol

%files -n %{lib_name}
%{_libdir}/*.so.%{lib_major}
%{_libdir}/*.so.%{lib_major}.*

%files -n %{lib_name_devel}
%doc examples doc/*.txt doc/*.pdf AUTHORS ChangeLog NEWS README
%doc --no-dereference COPYING
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc doc examples


%changelog
* Sat Oct 16 2021 Igor Vlasenko <viy@altlinux.org> 5.0-alt1_1
- new version

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.48-alt1
- Version 4.48

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.47-alt2
- Rebuilt with gmp 5.0.5

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.47-alt1
- Version 4.47
- Disabled devel-static package

* Sun Sep 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.46-alt1
- Version 4.46

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.45-alt2
- Rebuilt for debuginfo

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.45-alt1
- Version 4.45

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.44-alt3
- Renamed glpk4 -> glpk

* Thu Sep 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.44-alt2
- Added link to glpk.h into %_includedir

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.44-alt1
- Version 4.44

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.40-alt1
- Version 4.40

* Thu Oct 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.39-alt1
- Version 4.39

* Wed Jul 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.38-alt1
- Version 4.38

* Thu Apr 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.37-alt2
- Move doc and examples into lib%name-devel-doc package

* Tue Apr 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.37-alt1
- Version 4.37

* Tue Apr 18 2006 Grigorij Mogaev <zcrendel@altlinux.ru> 4.9-alt1
- initial rpm, separate source project into four packages.

