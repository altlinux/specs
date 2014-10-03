%define name sqsh
%define release alt1
%define version 2.5.16.1

Name: 		%name
Version: 	%version
Release: alt1

Summary: 	SQL Shell. It is intended as a replacement for the Sybase 'isql'.
License: 	GPL
Group: 		Databases
Url: 		http://sourceforge.net/projects/sqsh/

Source0: 	%name-%version.tar.bz2

# Automatically added by buildreq on Sat May 22 2004
BuildRequires: libncurses-devel libreadline-devel
BuildRequires: libfreetds-devel >= 0.64
BuildPreReq: libX11-devel imake libXt-devel libXaw-devel libXext-devel
Requires: libfreetds >= 0.64

%description
Sqsh (pronounced skwish) is short for SQshelL (pronounced s-q-shell),
it is intended as a replacement for the venerable 'isql' program supplied
by Sybase. 

Sqsh is much more than a nice prompt (a la 'dsql', from David B. Joyner),
it is intended to provide much of the functionality provided by a good
shell, such as variables, aliasing, redirection, pipes, back-grounding,
job control, history, command substitution, and dynamic configuration.
Also, as a by-product of the design, it is remarkably easy to extend
and add functionality.

Sqsh can be used for make connection to any databases with TDS-protocol
support (eg. MS-SQL or Sybase). This package is build with FreeTDS
library (http://www.freetds.org).

%prep

%setup

%build
export SYBASE=/usr
export SYBASE_LIBDIR=%_libdir
%autoreconf
%configure \
	--with-readline=yes \
	--with-x

%make_build

%install
%makeinstall_std
%make DESTDIR=%buildroot install.man

%files
%config(noreplace) %_sysconfdir/sqshrc
%_bindir/sqsh
%_mandir/man1/sqsh.1*
%doc COPYING ChangeLog INSTALL README
%doc doc/FAQ doc/README* doc/sample.* doc/*.sqshrc doc/sqsh.html

%changelog
* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.16.1-alt1
- Version 2.5.16.1

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jul 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1.5-alt1
- 2.1.5
- rebuild with FreeTDS v0.82

* Sat Dec 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.3-alt5.1
- Rebuilt with libreadline.so.5.

* Wed May 25 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1.3-alt5
- 2.1.3
- rebuild with FreeTDS v0.63

* Sat May 22 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1-alt5
- rebuild with FreeTDS v0.62.3

* Mon Mar 17 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1-alt4
- real rebuild with the last most stable version of FreeTDS -- v0.61

* Wed Mar 05 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1-alt3
- rebuild with the last most stable version of FreeTDS -- v0.61

* Mon Feb 10 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1-alt2.1
- rebuild with the last most stable version of FreeTDS -- v0.61rc1

* Sun Oct 27 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1-alt2
- rebuild with new version of FreeTDS library

* Mon Jul 01 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1-alt1
- initial package for ALT Linux
