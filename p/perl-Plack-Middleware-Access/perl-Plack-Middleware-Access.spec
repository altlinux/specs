%define dist Plack-Middleware-Access

Name: perl-%dist
Version: 0.3
Release: alt1

Summary: Middleware to restrict access depending on remote ip or other parameters.
License: GPL or Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source: %dist-%version.tar.gz

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
* Mon Feb 11 2013 Eugene Prokopiev <enp@altlinux.ru> 0.3-alt1
- first build for Sisyphus
