BuildRequires: libuuid-devel libXext-devel libedit-devel libdb6-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define _disable_ld_no_undefined 1
%global __requires_exclude swipl.sh

Summary:	Prolog interpreter and compiler
Name:		swi-prolog
Version:	7.4.2
Release:	alt2_2
License:	LGPLv2+
Group:		Development/Other
Url:		http://www.swi-prolog.org
Requires:	%{name}-nox
Requires:	%{name}-xpce
Source44: import.info
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl

#Recommends:	%{name}-doc

%description
Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.

%package nox
Group:		Development/Other
Summary:	SWI-Prolog without GUI components
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	libreadline-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	libgmp-devel
#Recommends:	%{name}-doc
URL:		http://www.swi-prolog.org/
Source0:	http://www.swi-prolog.org/download/stable/src/swipl-%{version}.tar.gz
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl


%description nox
This package provide SWI-Prolog and several libraries, but without
GUI components.

%package x
Group:          Development/Other
Summary:        %{name} native GUI library
Requires:       %{name}-nox = %{version}-%{release}
Provides:	%{name}-xpce
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl


%description x
XPCE is a toolkit for developing graphical applications in Prolog and
other interactive and dynamically typed languages.

%package java
Group:		Development/Java
Summary:	Java interface for %{name}
BuildRequires:	java-devel-default /proc
Requires:	%{name}-nox = %{version}-%{release}
Provides:	%{name}-jpl
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl


%description java
JPL is a dynamic, bi-directional interface between %{name} and Java
runtimes. It offers two APIs: Java API (Java-calls-Prolog) and Prolog
API (Prolog-calls-Java).

%package odbc
Group:		Development/Databases
Summary:	ODBC interface for %{name}
BuildRequires:	libunixODBC-devel libunixODBC-devel-compat libunixODBC2
Requires:	%{name}-nox = %{version}-%{release}
# pl is not perl
AutoReq: yes,noperl
AutoProv: yes,noperl


%description odbc
ODBC interface for SWI-Prolog to interact with database systems.

%package doc
Group:		Documentation
Summary:	Documentation for %{name}
Requires:	%{name}-nox = %{version}-%{release}
AutoReqProv: no

%description doc
Documentation for SWI-Prolog.

%prep
%setup -n swipl-%{version} -q

%build
%add_optflags %optflags_shared
%configure
%make

pushd packages
%configure
%make
popd

%install
make install DESTDIR=%buildroot

pushd packages
make install DESTDIR=%buildroot
%make html-install PLBASE=%{buildroot}%{_libdir}/swipl-%{version}
popd

%files

%files nox
%doc README.md LICENSE VERSION
%{_bindir}/swipl*
%{_libdir}/swipl-%{version}
%{_libdir}/pkgconfig/swipl.pc
%exclude %{_libdir}/swipl-%{version}/doc
%exclude %{_libdir}/swipl-%{version}/lib/*/libjpl.so
%exclude %{_libdir}/swipl-%{version}/lib/jpl.jar
%exclude %{_libdir}/swipl-%{version}/library/jpl.pl
%exclude %{_libdir}/swipl-%{version}/xpce/*
%exclude %{_libdir}/swipl-%{version}/lib/*/odbc4pl.so
%exclude %{_libdir}/swipl-%{version}/library/odbc.pl

%files x
%{_mandir}/*/xpce*
%doc %{_libdir}/swipl-%{version}/doc/Manual/*xpce.html
%{_bindir}/xpce*
%{_libdir}/swipl-%{version}/xpce/*

%files java
%doc packages/jpl/README.html
%doc %{_libdir}/swipl-%{version}/doc/packages/examples/jpl
%doc %{_libdir}/swipl-%{version}/doc/packages/jpl
%{_libdir}/swipl-%{version}/lib/*/libjpl.so
%{_libdir}/swipl-%{version}/lib/jpl.jar
%{_libdir}/swipl-%{version}/library/jpl.pl

%files odbc
%doc %{_libdir}/swipl-%{version}/doc/packages/odbc.html
%{_libdir}/swipl-%{version}/lib/*/odbc4pl.so
%{_libdir}/swipl-%{version}/library/odbc.pl

%files doc
%{_mandir}/*/swipl*
%dir %{_libdir}/swipl-%{version}/doc
%doc %{_libdir}/swipl-%{version}/doc/Manual
%exclude %{_libdir}/swipl-%{version}/doc/Manual/*xpce.html
%doc %{_libdir}/swipl-%{version}/doc/packages
%exclude %{_libdir}/swipl-%{version}/doc/packages/examples/jpl
%exclude %{_libdir}/swipl-%{version}/doc/packages/jpl
%exclude %{_libdir}/swipl-%{version}/doc/packages/odbc.html


%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 7.4.2-alt2_2
- added Url:

* Sun Mar 04 2018 Igor Vlasenko <viy@altlinux.ru> 7.4.2-alt1_2
- new version; picked from orphaned as import

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.15-alt1.qa2
- Rebuilt with gmp 5.0.5

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 5.6.15-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for swi-prolog
  * postun_ldconfig for swi-prolog
  * postclean-05-filetriggers for spec file

* Sun Jul 02 2006 Alexey Tourbin <at@altlinux.ru> 5.6.15-alt1
- 5.0.10 -> 5.6.15
- configured --enable-shared
- installed swi-prolog libraries under %plbase
- built and packaged manual.pdf

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.0.10-alt1.1
- Rebuilt with libreadline.so.5.

* Fri Jan 24 2003 Vitaly Lugovsky <vsl@altlinux.ru> 5.0.10-alt1
- 5.0.10

* Tue Nov 27 2001 Stanislav Ievlev <inger@altlinux.ru> 4.0.10-alt1
- 4.0.10

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Fri Oct 27 2000 Pixel <pixel@mandrakesoft.com> 3.4.1-1mdk
- new version

* Wed Aug 23 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-6mdk
- add packager field

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.3.6-5mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-4mdk
- BM

* Tue Jul 11 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-3mdk
- and pixel changed a few other things to stef's changes

* Mon Jul 10 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 3.3.6-2mdk
- makeinstall macro
- macroszifications

* Wed Jun  7 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-1mdk
- change name to swi-prolog
- new version
- fix licence
- fix buildroot
- much cleanup

* Wed Jun  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.2.9-2mdk
- first package for Mandrake

* Thu Jul 29 1999 David Kuester <kuestler@zeta.org.au>
- New source build version 3.2.9
* Tue Jun 22 1999 David Kuester <kuestler@zeta.org.au>
- New source build version 3.2.8
- Split the single patch in two (emacs) and (powerpc)
* Sun Nov 15 1998 Justin Cormack <jpc1@doc.ic.ac.uk>
- added changelog
- various tidying up things
- adjusted so will build on all architectures
- previous packagers:
- David Kuestler <kuestler@zeta.org.au>
- Kjetil Wiekhorst Jørgensen <jorgens@zarhan.pvv.org>
- Adam P. Jenkins <ajenkins@cs.umass.
