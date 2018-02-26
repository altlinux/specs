%define module_name Pod-Strip

Name: perl-%module_name
Version: 1.02
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Remove POD from Perl code
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/modules/by-module/Pod/%module_name-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 16 2009
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Pod::Strip is a subclass of Pod::Simple that strips all POD from Perl Code.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Pod/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 16 2009 Victor Forsyuk <force@altlinux.org> 1.02-alt1
- Initial build.
