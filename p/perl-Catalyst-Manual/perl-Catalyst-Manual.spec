%define dist Catalyst-Manual
Name: perl-%dist
Version: 5.9002
Release: alt1
Epoch: 1

Summary: The Catalyst developer's manual
License: Artistic and GPL
Group: Development/Perl

URL: http://search.cpan.org/dist/Catalyst-Manual/
Source: http://www.cpan.org/authors/id/H/HK/HKCLARK/Catalyst-Manual-5.9002.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Dec 27 2010 (-bi)
BuildRequires: perl-Module-Install

%description
This is just the Catalyst manual.  If you want to develop Catalyst
apps, please install Catalyst::Devel.  If you'd like a tutorial and
a full example Catalyst application, please install
Task::Catalyst::Tutorial.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Catalyst*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1:5.9002-alt1
- automated CPAN update

* Mon Dec 27 2010 Alexey Tourbin <at@altlinux.ru> 1:5.8005-alt1
- 5.8004 -> 5.8005

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 1:5.8004-alt1
- 5.7013 -> 5.8004

* Sun Oct 05 2008 Michael Bochkaryov <misha@altlinux.ru> 5.701300-alt2
- fix conflict with Catalyst::Runtime

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 5.701300-alt1
- 5.7013 version
- fix directory ownership violation

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 5.701200-alt1
- 5.7012 version build

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 5.700501-alt1
- first build for ALT Linux Sisyphus

