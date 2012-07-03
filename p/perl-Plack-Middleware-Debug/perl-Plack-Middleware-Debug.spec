%define dist Plack-Middleware-Debug
%def_without test

Name: perl-%dist
Version: 0.14
Release: alt1

Summary: The debug middleware offers a configurable set of panels that displays information about the current request and response.
Group: Development/Perl
License: GPL or Artistic
Url: %CPAN %dist

BuildArch: noarch
Source: perl-%dist-%version.tar

BuildRequires: perl-Plack perl-Text-MicroTemplate perl-Data-Dump perl-Catalyst-Devel perl-Class-Method-Modifiers perl-Module-Versions

%description
%name

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%doc README examples

%changelog
* Mon Feb 20 2012 Eugene Prokopiev <enp@altlinux.ru> 0.14-alt1
- first build for Sisyphus

