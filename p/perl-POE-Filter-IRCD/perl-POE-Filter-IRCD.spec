%define module POE-Filter-IRCD

Name: perl-%module
Version: 2.42
Release: alt2

Summary: A POE-based parser for the IRC protocol

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/%module-%version.tar.gz

# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: perl-POE perl-Test-Pod perl-Test-Pod-Coverage

%description
A POE filter for the IRC protocol.
POE::Filter::IRCD provides a convenient way of parsing and creating IRC protocol
lines. It provides the parsing engine for L<POE::Component::Server::IRC> and L<POE::Component::IRC>.
A standalone version exists as L<Parse::IRC>.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/Filter/*.pm

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 2.42-alt2
- drop %%perl_vendor_man3dir

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.42-alt1
- automated CPAN update

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 2.40-alt1
- 2.40

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.38-alt1
- initial build for ALT Linux Sisyphus

