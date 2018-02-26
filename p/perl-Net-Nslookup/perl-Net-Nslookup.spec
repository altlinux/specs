%define _without_test 1
%define module Net-Nslookup

Name: perl-Net-Nslookup
Version: 2.00
Release: alt1

Summary: Provide nslookup(1)-like capabilities

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: http://www.cpan.org/authors/id/D/DA/DARREN/Net-Nslookup-%{version}.tar.gz

# Automatically added by buildreq on Fri Dec 19 2008
BuildRequires: perl-Net-DNS perl-devel

%description
Net::Nslookup provides the capabilities of the standard UNIX command
line tool nslookup(1). Net::DNS is a wonderful and full featured module,
but quite often, all you need is `nslookup $host`.  This module
provides that functionality.

Net::Nslookup exports a single function, called "nslookup".
"nslookup" can be used to retrieve A, PTR, CNAME, MX, and NS records.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/*

%changelog
* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.19-alt2
- drop %%perl_vendor_man3dir

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.19-alt1
- 1.19

* Fri Dec 19 2008 Alexey Shabalin <shaba@altlinux.ru> 1.18-alt1
- initial build for ALT Linux Sisyphus

