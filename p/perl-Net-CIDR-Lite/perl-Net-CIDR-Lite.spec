%define module Net-CIDR-Lite

Name: perl-%module
Version: 0.21
Release: alt1.1

Summary: Perl extension for merging IPv4 or IPv6 CIDR addresses
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/D/DO/DOUGW/Net-CIDR-Lite-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 08 2010
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl extension for merging IPv4 or IPv6 CIDR addresses.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.21-alt1
- 0.21

* Mon Apr 10 2006 Victor Forsyuk <force@altlinux.ru> 0.20-alt1
- 0.20
- Added build dependencies needed to run tests.

* Wed Jul 13 2005 Victor Forsyuk <force@altlinux.ru> 0.18-alt1
- 0.18

* Thu Mar 10 2005 Victor Forsyuk <force@altlinux.ru> 0.15-alt1
- Initial build for Sisyphus.
