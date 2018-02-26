%define dist Try-Tiny
Name: perl-Try-Tiny
Version: 0.11
Release: alt1

Summary: Minimal try/catch with proper localization of $@
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DO/DOY/Try-Tiny-0.11.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-devel

%description
This module provides bare bones "try"/"catch" statements that are designed
to minimize common mistakes with eval blocks, and NOTHING else.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%dir %perl_vendor_privlib/Try
%perl_vendor_privlib/Try/Tiny.pm

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- 0.06 -> 0.09

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- 0.02 -> 0.04
- fixed directory packaging

* Sun Nov 22 2009 Mikhail Pokidko <pma@altlinux.org> 0.02-alt1
- initial build for ALT Linux Sisyphus
