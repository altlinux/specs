%define dist Plack-Middleware-TemplateToolkit
%def_without test

Name: perl-%dist
Version: 0.25
Release: alt1

Summary: Middleware to allow your Plack-based application to serve files processed through Template Toolkit (TT).
License: GPL or Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source: perl-%dist-%version.tar

BuildRequires: perl-Plack perl-Plack-Middleware-Debug perl-Template

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
%doc README example

%changelog
* Mon Feb 20 2012 Eugene Prokopiev <enp@altlinux.ru> 0.25-alt1
- first build for Sisyphus

