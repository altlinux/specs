Name: tnef
Version: 1.4.16
Release: alt1

Summary: MS-TNEF attachments decoder
License: GPLv2+
Group: Text tools
Url: http://sourceforge.net/projects/%name

# VCS: https://github.com/verdammelt/tnef
Source: http://downloads.sf.net/%name/%name-%version.tar.gz

%description
TNEF is a program for unpacking MIME attachments of type "application/ms-tnef".

The TNEF program allows one to unpack the attachments which were encapsulated
into the TNEF attachment. Thus alleviating the need to use Microsoft Outlook to
view the attachment.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/%name
%_man1dir/*
%doc AUTHORS BUGS NEWS README* doc/FAQ

%changelog
* Thu Jan 11 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.16-alt1
- 1.4.16

* Thu Jun 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.15-alt1
- 1.4.15

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.13-alt1
- 1.4.13

* Sat Nov 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.12-alt1
- 1.4.12

* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 1.4.9-alt1
- 1.4.9

* Wed Apr 20 2011 Victor Forsiuk <force@altlinux.org> 1.4.8-alt1
- 1.4.8

* Mon Feb 01 2010 Victor Forsyuk <force@altlinux.org> 1.4.7-alt1
- 1.4.7

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 1.4.6-alt1
- 1.4.6

* Fri Oct 03 2008 Victor Forsyuk <force@altlinux.org> 1.4.5-alt1
- 1.4.5

* Fri May 30 2008 Victor Forsyuk <force@altlinux.org> 1.4.4-alt1
- 1.4.4

* Thu Sep 07 2006 Victor Forsyuk <force@altlinux.ru> 1.4.3-alt1
- 1.4.3
- Exclude from package file format description, add FAQ.

* Fri Aug 11 2006 Victor Forsyuk <force@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Mon Jun 05 2006 Victor Forsyuk <force@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Wed Oct 19 2005 Victor Forsyuk <force@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Fri Apr 22 2005 Victor Forsyuk <force@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Mon Nov 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1
- build: enabled automated testing by default.

* Thu Oct 10 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- Updated to 1.1.2

* Thu Oct 25 2001 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- 1.1.1

* Fri Oct 19 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt1
- 1.1

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 0.16-ipl1mdk
- 0.16

* Wed Nov 08 2000 Dmitry V. Levin <ldv@fandra.org> 0.15-ipl1mdk
- RE adaptions.

* Mon Nov 06 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.15-1mdk
- used srpm from rufus t firefly <rufus.t.firefly@linux-mandrake.com> :
	v0.14.1-1mdk
	removed bum strdup.h patch (fixed in 0.14.1)
- add macros

* Fri Oct 06 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  - v0.14-1mdk (initial packaging)
