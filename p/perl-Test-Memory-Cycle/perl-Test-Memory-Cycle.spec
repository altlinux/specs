%define module Test-Memory-Cycle

Name: perl-%module
Version: 1.04
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: A thin Test::More-compatible wrapper around Devel::Cycle module
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Test/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Aug 05 2008
BuildRequires: perl-CGI perl-Devel-Cycle perl-Test-Pod perl-Test-Pod-Coverage

%description
A thin Test::More-compatible wrapper around Devel::Cycle module.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Aug 11 2008 Victor Forsyuk <force@altlinux.org> 1.04-alt1
- Initial build.
