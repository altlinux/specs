%define dist AnyEvent
Name: perl-%dist
Version: 6.02
Release: alt2

Summary: Framework for multiple event loops
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# XXX choose default model?
%add_findreq_skiplist */AnyEvent/Impl/*.pm

# classified as non-text
Provides: perl(AnyEvent/Util/uts46data.pl)

# Automatically added by buildreq on Wed Oct 26 2011 (-bi)
BuildRequires: perl-Async-Interrupt perl-EV perl-Guard perl-Net-SSLeay perl-Unicode-Normalize perl-devel

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
