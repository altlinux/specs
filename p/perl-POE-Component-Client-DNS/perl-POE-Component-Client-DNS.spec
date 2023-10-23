%define module POE-Component-Client-DNS

Name: perl-POE-Component-Client-DNS
Version: 1.054
Release: alt2

Summary: Non-blocking/concurrent DNS queries using Net::DNS and POE

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: http://www.cpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-DNS-%{version}.tar.gz
Patch: https://salsa.debian.org/perl-team/modules/packages/libpoe-component-client-dns-perl/raw/master/debian/patches/net-dns-1.38-deprecations.patch

# Automatically added by buildreq on Fri Oct 23 2009
BuildRequires: perl-Net-DNS perl-POE perl-Test-NoWarnings

%description
POE::Component::Client::DNS provides a facility for non-blocking,
concurrent DNS requests.  Using POE, it allows other tasks to run
while waiting for name servers to respond.

%prep
%setup -q -n %module-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/*

%changelog
* Mon Oct 23 2023 Igor Vlasenko <viy@altlinux.org> 1.054-alt2
- fixed build

* Fri Nov 13 2015 Igor Vlasenko <viy@altlinux.ru> 1.054-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.053-alt1
- automated CPAN update

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.051-alt2
- drop %%perl_vendor_man3dir

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.051-alt1
- 1.051

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 1.01-alt1
- initial build for ALT Linux Sisyphus

