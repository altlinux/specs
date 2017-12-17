%define _unpackaged_files_terminate_build 1
%define dist Sub-Identify
Name: perl-%dist
Version: 0.14
Release: alt1.1

Summary: Retrieve names of code references
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RG/RGARCIA/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod

%description
Sub::Identify allows you to retrieve the real name of code references.
For this, it uses perl's introspection mechanism, provided by the B module.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.mdown TODO.mdown
%perl_vendor_archlib/Sub
%perl_vendor_autolib/Sub

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt3
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt2
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1.3
- rebuilt for perl-5.14

* Fri Nov 12 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1.2
- new release

* Mon Oct 04 2010 Alexey Tourbin <at@altlinux.ru> 0.04-alt1.1
- rebuilt for perl-5.12

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.04-alt1
- 0.04 version

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- NMU fixing directory ownership violation

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 0.03-alt1
- first build for ALT Linux Sisyphus
