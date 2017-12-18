%define _unpackaged_files_terminate_build 1
%define dist Exception-Class
Name: perl-%dist
Version: 1.44
Release: alt1

Summary: A module that allows you to declare real exception classes in Perl
License: Artistic 2.0
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-Class-Data-Inheritable perl-Devel-StackTrace perl-devel

%description
Exception::Class allows you to declare exception hierarchies in your modules
in a "Java-esque" manner.  It features a simple interface allowing programmers
to 'declare' exception classes at compile time. It also has a base exception
class, Exception::Class::Base, that can be easily extended.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md CONTRIBUTING.md
%perl_vendor_privlib/Exception

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- automated CPAN update

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- 1.24 -> 1.32

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.24-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.24-alt2
- fix directory ownership violation

* Thu May 22 2008 Vitaly Lipatov <lav@altlinux.ru> 1.24-alt1
- new version 1.24 (with rpmrb script)

* Tue Jun 07 2005 Vitaly Lipatov <lav@altlinux.ru> 1.21-alt1
- first build for ALT Linux Sisyphus
