%define module POE-Component-Client-DNS

Name: perl-POE-Component-Client-DNS
Version: 1.051
Release: alt2

Summary: Non-blocking/concurrent DNS queries using Net::DNS and POE

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %module-%version.tar.gz

# Automatically added by buildreq on Fri Oct 23 2009
BuildRequires: perl-Net-DNS perl-POE perl-Test-NoWarnings

%description
POE::Component::Client::DNS provides a facility for non-blocking,
concurrent DNS requests.  Using POE, it allows other tasks to run
while waiting for name servers to respond.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.051-alt2
- drop %%perl_vendor_man3dir

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.051-alt1
- 1.051

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 1.01-alt1
- initial build for ALT Linux Sisyphus

