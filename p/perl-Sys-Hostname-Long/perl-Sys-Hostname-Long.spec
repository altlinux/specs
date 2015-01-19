%define module Sys-Hostname-Long

Name: perl-%module
Version: 1.5
Release: alt1

Summary: Sys-Hostname-Long perl module
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/S/SC/SCOTT/Sys-Hostname-Long-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Mar 10 2005
BuildRequires: perl-devel

%description
Sys-Hostname-Long perl module - try every conceivable way to get full hostname.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
# remove empty hier:
rm -rf %buildroot%perl_vendor_privlib/*-linux
# shouldn't be in this location:
rm -f %buildroot%perl_vendor_privlib/Sys/Hostname/testall.pl

%files
%doc testall.pl
%perl_vendor_privlib/*

%changelog
* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Dec 18 2007 Victor Forsyuk <force@altlinux.org> 1.4-alt1
- 1.4
- Eliminate install time requirement for perl-devel caused by installed
  test script.

* Thu Mar 10 2005 Victor Forsyuk <force@altlinux.ru> 1.2-alt1
- Initial build for Sisyphus.
