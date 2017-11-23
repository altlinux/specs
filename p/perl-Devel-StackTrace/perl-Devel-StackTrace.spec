%define _unpackaged_files_terminate_build 1
%define module Devel-StackTrace
Name: perl-%module
Version: 2.03
Release: alt1
Epoch: 1

Summary: Devel::StackTrace - An object representing a stack trace

License: Artistic
Group: Development/Perl
Url: %CPAN %module

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{module}-%{version}.tar.gz

BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md README.md LICENSE
%perl_vendor_privlib/Devel/StackTrace*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.03-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.02-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.01-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.00-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.34-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.32-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.31-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.30-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.27-alt1
- automated CPAN update

* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 1:1.26-alt1
- New version 1.26
- Spec cleanup

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1901-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1901-alt2
- fix directory ownership violation

* Mon Jun 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1901-alt1
- new version 1.1901 (with rpmrb script) - fix bug #16135

* Thu May 22 2008 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt1
- new version 1.18 (with rpmrb script)

* Mon Jun 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- first build for ALT Linux Sisyphus
