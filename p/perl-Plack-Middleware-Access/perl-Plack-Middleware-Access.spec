%define dist Plack-Middleware-Access

Name: perl-%dist
Version: 0.4
Release: alt1

Summary: Middleware to restrict access depending on remote ip or other parameters.
License: GPL or Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source: http://www.cpan.org/authors/id/T/TA/TADAM/Plack-Middleware-Access-%{version}.tar.gz

BuildRequires: perl-Plack perl-Net-IP

%description
%name

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*

%changelog
* Mon Feb 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1
- automated CPAN update

* Mon Feb 11 2013 Eugene Prokopiev <enp@altlinux.ru> 0.3-alt1
- first build for Sisyphus
