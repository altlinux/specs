%define module Net-DNS-Codes

Name: perl-%module
Version: 0.11
Release: alt1

Summary: Net::DNS::Codes - collection of C library DNS codes
License: GPL
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/M/MI/MIKER/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 25 2012
BuildRequires: perl-devel

%description
Net::DNS::Codes provides forward and reverse lookup for most
common C library DNS codes as well as all the codes for the DNS
HEADER field.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net

%changelog
* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 0.11-alt1
- 0.11

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 05 2007 Victor Forsyuk <force@altlinux.org> 0.09-alt1
- Initial build.
