%define module Class-Std-Fast

Name: perl-%module
Version: 0.0.8
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perl module that provides a faster but less secure version of Class::Std
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Class/%module-v%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Aug 01 2008
BuildRequires: perl-Class-Std perl-Log-Agent perl-Module-Build perl-Storable perl-Test-Pod perl-Test-Pod-Coverage

%description
This perl module provides a faster but less secure version of Class::Std.

%prep
%setup -n %module-v%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 0.0.8-alt1
- Initial build.
