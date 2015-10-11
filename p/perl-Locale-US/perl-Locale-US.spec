%define _unpackaged_files_terminate_build 1
%define module Locale-US

Name: perl-%module
Version: 3.04
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Map from US two-letter codes to states and vice versa
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/A/AC/ACCARDO/Locale-US-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 15 2009
BuildRequires: perl-devel perl(Data/Section/Simple.pm)

%description
Two letter codes for state identification in the United States and vice versa.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Locale

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 3.04-alt1
- automated CPAN update

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.112150-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 1.2-alt1
- Initial build.
