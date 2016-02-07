Name: cabextract
Version: 1.6
Release: alt1

Summary: Utility for extracting Microsoft Cabinet files
License: GPLv2+
Group: Archiving/Compression

URL: http://cabextract.org.uk/
Source: http://cabextract.org.uk/cabextract-%version.tar.gz
Patch: cabextract-1.0-alt-fixes.patch

# Automatically added by buildreq on Sat Jun 11 2011
BuildRequires: tzdata

%description
A program for extracting Microsoft Cabinet (.CAB) files.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc NEWS README

%changelog
* Sun Feb 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Sun Mar 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- 1.5

* Sat Jun 11 2011 Victor Forsiuk <force@altlinux.org> 1.4-alt1
- 1.4

* Tue Aug 03 2010 Victor Forsiuk <force@altlinux.org> 1.3-alt1
- 1.3

* Tue Aug 04 2009 Victor Forsyuk <force@altlinux.org> 1.2-alt2
- Fix URL.
- Regenarate configure with autoconf >= 2.62 to fix AC_FUNC_MKTIME that breaks
  with gcc 4.3.

* Mon Sep 25 2006 Victor Forsyuk <force@altlinux.ru> 1.2-alt1
- 1.2

* Tue Oct 19 2004 Victor Forsyuk <force@altlinux.ru> 1.1-alt1
- 1.1 (fixes a security flaw: http://www.securityfocus.com/bid/11376/).

* Thu May 20 2004 Victor Forsyuk <force@altlinux.ru> 1.0-alt1
- 1.0

* Wed Sep 25 2002 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- 0.6 (fixes umask problem).

* Fri Aug 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt2
- fix url

* Thu Nov 22 2001 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt1
- 0.5, spec cleanup

* Mon Jul 16 2001 AEN <aen@logic.ru> 0.2-alt1
- build for Sisyphus
