%define dist Locale-Hebrew
Name: perl-%dist
Version: 1.05
Release: alt3

Summary: Bidirectional Hebrew support
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Encode perl-Pod-Escapes perl-devel

%description
This module is based on code from the Unicode Consortium.
The charset on their code was bogus, therefore this module had to work
the real charset from scratch.  There might have some mistakes, though.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Locale
%perl_vendor_autolib/Locale

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt3
- disabled build dependency on perl-Module-Install

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1.1
- rebuilt with perl 5.12

* Sat Sep 09 2006 Vyacheslav Dikonov <slava@altlinux.ru> 1.04-alt1
- Initial build
