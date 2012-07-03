%define module_name Geography-Countries

Name: perl-%module_name
Version: 2009041301
Release: alt1

Summary: Classes for 2-letter, 3-letter, and numerical codes for countries
Group: Development/Perl
License: distributable

URL: http://search.cpan.org/dist/%module_name
Source: http://www.cpan.org/authors/id/A/AB/ABIGAIL/Geography-Countries-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 10 2006 (-bi)
BuildRequires: perl-devel perl-Pod-Escapes perl-Pod-Simple perl-Test-Pod

%description
This module maps country names, and their 2-letter, 3-letter and
numerical codes, as defined by the ISO-3166 maintenance agency [1],
and defined by the UNSD.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

# Clean up buildroot
%__rm -rf %buildroot%perl_vendor_privlib/*-linux %buildroot/.perl.req

%files
%perl_vendor_privlib/*

%changelog
* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 2009041301-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.41-alt0.dev03.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Apr 10 2006 Victor Forsyuk <force@altlinux.ru> 1.41-alt0.dev03
- Development release from new mantainer (virtually no code changes,
  just updated data).
- Added build dependencies needed to run tests.

* Wed Oct 05 2005 Victor Forsyuk <force@altlinux.ru> 1.4-alt1
- Initial build.
