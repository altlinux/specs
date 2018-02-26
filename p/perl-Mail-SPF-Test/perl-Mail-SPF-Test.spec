%define module Mail-SPF-Test

Name: perl-%module
Version: 1.001
Release: alt1.1

Summary: Perl module for reading and manipulating SPF test-suite data
License: BSD
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Mail/%module-v%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Mar 31 2008
BuildRequires: perl-Module-Build perl-Net-DNS perl-NetAddr-IP

%description
Perl module for reading and manipulating SPF test-suite data.

%prep
%setup -n %module-v%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mail/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 1.001-alt1
- 1.001

* Wed May 16 2007 Victor Forsyuk <force@altlinux.org> 1.000-alt1
- Initial build.
