%define dist Data-Alias
Name: perl-%dist
Version: 1.15
Release: alt2

Summary: Comprehensive set of aliasing operations
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Filter perl-Module-Install perl-Test-Pod

%description
Data::Alias is a module that allows you to apply "aliasing semantics" to
a section of code, causing aliases to be made whereever Perl would normally
make copies instead.  You can use this to improve efficiency and readability,
when compared to using references.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Data
%perl_vendor_autolib/Data

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.15-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Mon Jan 24 2011 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- 1.08 -> 1.11

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1
- new version 1.08
- built with perl 5.12

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 1.07-alt1
- initial revision
