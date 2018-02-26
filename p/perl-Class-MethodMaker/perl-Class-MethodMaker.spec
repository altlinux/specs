%define dist Class-MethodMaker
Name: perl-%dist
Version: 2.18
Release: alt2

Summary: Easy building of Perl Classes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-IPC-Run perl-autodie perl-devel

%description
This module solves the problem of having to continually write
accessor methods for your objects that perform standard tasks.

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
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.18-alt2
- rebuilt for perl-5.14

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 2.18-alt1
- 2.13 -> 2.18

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 2.13-alt1.1
- rebuilt with perl 5.12

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 2.13-alt1
- 2.07 -> 2.13

* Tue Jun 14 2005 Alexey Tourbin <at@altlinux.ru> 2.07-alt1
- initial revision (required for WWW::Bugzilla)
