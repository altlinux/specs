%define dist Newt
Name: perl-%dist
Version: 1.08
Release: alt4.1.1.1.1

Summary: Perl bindings for the Newt library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Patch0: newt-perl-1.08-debian.patch
Patch1: newt-perl-1.08-typemap.patch
Patch2: newt-perl-1.08-fix.patch
Patch3: newt-perl-1.08-xs.patch
Patch4: newt-perl-1.08-lang.patch
Patch5: perl-Newt-bz385751.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libnewt-devel perl-devel

%description
This package provides Perl bindings for the Newt widget
library, which provides a color text mode user interface.

%prep
%setup -q -n %dist-%version
%patch0 -p1 -b .debian
%patch1 -p1 -b .valist
%patch2 -p1 -b .fix
%patch3 -p1 -b .exes
%patch4 -p1 -b .lang
%patch5 -p1 -b .bz385751
rm -rf newtlib

# requires user interaction
%def_without test

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_archlib/Newt*
%perl_vendor_autolib/Newt

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.08-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.08-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.08-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt2.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt2.1
- rebuilt with perl 5.12

* Mon Mar 01 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.08-alt2
- rebuild with newt52

* Tue Jan 27 2009 Denis Kuznetsov <dek@altlinux.ru> 1.08-alt1
- rebuild for altlinux

* Fri Apr  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-21
- resolve bz 385751

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-20
- Rebuild for new perl (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.08-19
- Autorebuild for GCC 4.3

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.08-18
- rebuild for new perl

* Thu Aug 30 2007 Joe Orton <jorton@redhat.com> 1.08-17
- clarify License tag

* Tue Mar  6 2007 Joe Orton <jorton@redhat.com> 1.08-15
- rename to perl-Newt; Obsolete and Provide newt-perl (#226196)

* Thu Mar  1 2007 Joe Orton <jorton@redhat.com> 1.08-14
- various cleanups (Jason Tibbs, #226196)
- require perl-devel

* Tue Feb 27 2007 Joe Orton <jorton@redhat.com> 1.08-13
- clean up URL, Source, BuildRoot, BuildRequires

* Thu Dec 14 2006 Joe Orton <jorton@redhat.com> 1.08-12
- fix test.pl (Charlie Brady, #181674)

* Thu Dec 14 2006 Joe Orton <jorton@redhat.com> 1.08-11
- fix directory ownership (#216610)

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 1.08-10
- fix compiler warnings (#155977)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.08-9.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.08-9.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.08-9.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Sep 27 2005 Petr Rockai <prockai@redhat.com> - 1.08-9
- rebuild against newt 0.52.0

* Fri Mar  4 2005 Joe Orton <jorton@redhat.com> 1.08-8
- rebuild

* Tue Aug 17 2004 Joe Orton <jorton@redhat.com> 1.08-7
- add perl MODULE_COMPAT requirement

* Mon Aug 16 2004 Joe Orton <jorton@redhat.com> 1.08-6
- rebuild

* Mon Sep  8 2003 Joe Orton <jorton@redhat.com> 1.08-5
- fix issue with non-English LANG setting (#67735)

* Tue Aug  5 2003 Joe Orton <jorton@redhat.com> 1.08-4
- rebuild

* Thu May  9 2002 Joe Orton <jorton@redhat.com> 1.08-3
- add newt requirement

* Wed Apr 03 2002 Gary Benson <gbenson@redhat.com> 1.08-2
- tweak perl dependency as suggested by cturner@redhat.com

* Wed Mar 20 2002 Gary Benson <gbenson@redhat.com>
- make like all the other perl modules we ship (bind to perl version,
  use perl dependency finding scripts, build filelist automatically).
- include documentation
- build against perl 5.6.1

* Thu Jan 10 2002 Joe Orton <jorton@redhat.com>
- Adapted for RHL

* Tue Sep 11 2001 Mark Cox <mjc@redhat.com>
- Change paths to new layout

* Mon Jun 11 2001 Joe Orton <jorton@redhat.com>
- Initial revision.
