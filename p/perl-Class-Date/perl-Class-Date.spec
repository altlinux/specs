%define dist Class-Date
Name: perl-%dist
Version: 1.1.10
Release: alt3

Summary: Class for easy date and time manipulation 
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
This module is intended to provide a general-purpose date and datetime type
for perl.  You have a Class::Date class for absolute date and datetime, and
have a Class::Date::Rel class for relative dates.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Class
%perl_vendor_autolib/Class

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.1.10-alt3
- rebuilt for perl-5.14

* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 1.1.10-alt2
- specfile cleanup

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1.9-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.9-alt1
- automated CPAN update

* Sat Mar 25 2006 Andrey Brindeew <abr@altlinux.org> 1.1.8-alt1
- 1.1.8

* Sun Dec 12 2004 Andrey Brindeew <abr@altlinux.org> 1.1.7-alt1
- First build for ALT Linux

