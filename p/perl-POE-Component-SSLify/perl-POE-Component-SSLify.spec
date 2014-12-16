%define _unpackaged_files_terminate_build 1
%define dist POE-Component-SSLify
Name: perl-%dist
Version: 1.012
Release: alt1

Summary: Makes using SSL in the world of POE easy!
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AP/APOCAL/POE-Component-SSLify-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Module-Build perl-Net-SSLeay perl-POE perl-Task-Weaken perl-Test-NoWarnings perl-Test-Script perl-parent perl(Module/Build/Tiny.pm) perl(Test/FailWarnings.pm)

%description
This component represents the standard way to do SSL in POE.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/POE

%changelog
* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.008-alt1
- 0.20 -> 1.008

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- 0.20
- drop %%perl_vendor_man3dir

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- initial build for ALT Linux Sisyphus
