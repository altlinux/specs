%define dist Net-CUPS
Name: perl-%dist
Version: 0.61
Release: alt1.2

Summary: Perl interface to the Common Unix Printing System API
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libcups-devel perl-devel

%description
Net::CUPS is an object oriented interface to the Common Unix Printing System.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_autolib/Net
%perl_vendor_archlib/Net

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.61-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.61-alt1.1
- rebuilt with perl 5.12

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.61-alt1
- New version 0.61

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.59-alt1
- New version 0.59

* Mon Apr 07 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.55-alt2
- Fix build with CUPS 1.3.7

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.55-alt1
- New version 0.55

* Sun Mar 25 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.51-alt1
- New version 0.51
  - Reworked the entire module into the new design

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.41-alt1
- Initial build for ALT Linux Sisyphus

* Thu Aug 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.41-alt0
- Initial build
