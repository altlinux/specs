%define _unpackaged_files_terminate_build 1
%def_with bootstrap

%define dist AnyEvent
Name: perl-%dist
Version: 7.17
Release: alt3

Summary: Framework for multiple event loops
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/ML/MLEHMANN/%{dist}-%{version}.tar.gz
Patch: AnyEvent-7.17-syntax-fix.patch

BuildArch: noarch

# classified as non-text
Provides: perl(AnyEvent/Util/uts46data.pl)

# missing
%add_findreq_skiplist */AnyEvent/Impl/Cocoa.pm
%add_findreq_skiplist */AnyEvent/Impl/FLTK.pm
%add_findreq_skiplist */AnyEvent/Impl/Qt.pm
# in autoimports
%add_findreq_skiplist */AnyEvent/Impl/UV.pm
# should be ryun inside Irssi
%add_findreq_skiplist */AnyEvent/Impl/Irssi.pm
%if_with bootstrap
# XXX choose default model?
%add_findreq_skiplist */AnyEvent/Impl/*.pm
%else
BuildRequires: perl(Event.pm) perl(Event/Lib.pm) perl(Glib.pm) perl(IO/Async/Loop.pm) perl(Irssi.pm) perl(POE.pm) perl(Tk.pm)
# in autoimports 
#BuildRequires: perl(UV.pm)
%endif

# Automatically added by buildreq on Wed Oct 26 2011 (-bi)
BuildRequires: perl-Async-Interrupt perl-EV perl-Guard perl-Net-SSLeay perl-Unicode-Normalize perl-devel perl(IO/AIO.pm) perl(AnyEvent/AIO.pm)

%description
AnyEvent provides an identical interface to multiple event loops. This allows
module authors to utilise an event loop without forcing module users to use the
same event loop (as only a single event loop can coexist peacefully at any one
time).

%prep
%setup -q -n %{dist}-%{version}
%patch -p1
sed -i 's@require "lib/AnyEvent@require "AnyEvent@' lib/AnyEvent/Util.pm

# disable archlib hack
sed -i- '/ PM /,/}/d' Makefile.PL

%build
%if_without bootstrap
export PERL_ANYEVENT_LOOP_TESTS=1
%endif
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/AE.pm
%perl_vendor_privlib/AnyEvent*

%changelog
* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 7.17-alt3
- enabled IO-AIO tests
- added bootstrap mode

* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 7.17-alt2
- fixes for perl 5.32+

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 7.17-alt1
- automated CPAN update

* Wed Jul 31 2019 Igor Vlasenko <viy@altlinux.ru> 7.16-alt1
- automated CPAN update

* Tue Feb 26 2019 Igor Vlasenko <viy@altlinux.ru> 7.15-alt1
- automated CPAN update

* Thu Jan 31 2019 Igor Vlasenko <viy@altlinux.ru> 7.14-alt2
- added AnyEvent-7.14-syntax-fix.patch for perl 5.28

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 7.14-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 7.13-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 7.12-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 7.11-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 7.09-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 7.08-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 7.07-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 7.05-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 7.04-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 7.02-alt1
- automated CPAN update

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt2
- noarch

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 6.02-alt1
- automated CPAN update

* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 5.31-alt1
- 5.22 -> 5.31

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 5.22-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Dec 11 2009 Victor Forsyuk <force@altlinux.org> 5.22-alt1
- 5.22

* Thu Oct 08 2009 Victor Forsyuk <force@altlinux.org> 5.12-alt1
- 5.12

* Wed Oct 22 2008 L.A. Kostis <lakostis@altlinux.ru> 4.3-alt1.1
- update buildreq (add -Storable).

* Wed Oct 22 2008 L.A. Kostis <lakostis@altlinux.ru> 4.3-alt1
- version 4.3.

* Sun Feb 18 2007 L.A. Kostis <lakostis@altlinux.ru> 2.51-alt1.1
- add missing dir.

* Fri Feb 16 2007 L.A. Kostis <lakostis@altlinux.ru> 2.51-alt1
- initial release.
