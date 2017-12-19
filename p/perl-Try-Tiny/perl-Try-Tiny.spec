%define _unpackaged_files_terminate_build 1
%define dist Try-Tiny
Name: perl-Try-Tiny
Version: 0.29
Release: alt1

Summary: Minimal try/catch with proper localization of $@
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-devel perl(Module/Metadata.pm)

%description
This module provides bare bones "try"/"catch" statements that are designed
to minimize common mistakes with eval blocks, and NOTHING else.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/Try
%perl_vendor_privlib/Try/Tiny.pm

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Sat Oct 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

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
