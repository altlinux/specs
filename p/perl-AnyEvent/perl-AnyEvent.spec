%define _unpackaged_files_terminate_build 1
%define dist AnyEvent
Name: perl-%dist
Version: 7.12
Release: alt1

Summary: Framework for multiple event loops
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-%{version}.tar.gz

BuildArch: noarch

# XXX choose default model?
%add_findreq_skiplist */AnyEvent/Impl/*.pm

# classified as non-text
Provides: perl(AnyEvent/Util/uts46data.pl)

# Automatically added by buildreq on Wed Oct 26 2011 (-bi)
BuildRequires: perl-Async-Interrupt perl-EV perl-Guard perl-Net-SSLeay perl-Unicode-Normalize perl-devel perl(IO/AIO.pm) perl(AnyEvent/AIO.pm)

%description
AnyEvent provides an identical interface to multiple event loops. This allows
module authors to utilise an event loop without forcing module users to use the
same event loop (as only a single event loop can coexist peacefully at any one
time).

%prep
%setup -q -n %dist-%version
sed -i 's@require "lib/AnyEvent@require "AnyEvent@' lib/AnyEvent/Util.pm

# disable archlib hack
sed -i- '/ PM /,/}/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/AE.pm
%perl_vendor_privlib/AnyEvent*

%changelog
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
