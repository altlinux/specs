%define dist Mojolicious-Plugin-Authentication

Name: perl-%dist
Version: 1.21
Release: alt1
Summary: A plugin to make authentication a bit easier

Group: Development/Perl
License: Perl
Url: %CPAN %dist

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Module-Build perl-Mojolicious

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mojolicious/Plugin/*.pm
%doc example

%changelog
* Sun Mar 11 2012 Eugene Prokopiev <enp@altlinux.ru> 1.21-alt1
- initail build for Sisyphus

