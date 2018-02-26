%define dist Data-Dump
Name: perl-%dist
Version: 1.21
Release: alt1

Summary: Pretty printing of data structures
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011 (-bi)
BuildRequires: perl-Term-ANSIColor perl-devel

%description
This module provide functions that takes a list of values as their argument
and produces a string as its result. The string contains Perl code that,
when "eval"ed, produces a deep copy of the original arguments.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Data

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 1.21-alt1
- 1.19 -> 1.21

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 1.19-alt1
- 1.17 -> 1.19

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.17-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Wed Mar 17 2010 Victor Forsiuk <force@altlinux.org> 1.15-alt1
- 1.15

* Sat Sep 13 2008 Michael Bochkaryov <misha@altlinux.ru> 1.11-alt1
- 1.11 version build
- fix directory ownership violation

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 1.08-alt1
- first build for ALT Linux Sisyphus
