%define _unpackaged_files_terminate_build 1
%define module_name Pod-Strip

Name: perl-%module_name
Version: 1.100
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Remove POD from Perl code
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source0: http://www.cpan.org/authors/id/D/DO/DOMM/%{module_name}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 16 2009
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Pod::Strip is a subclass of Pod::Simple that strips all POD from Perl Code.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.md Changes
%perl_vendor_privlib/Pod/

%changelog
* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 1.100-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 16 2009 Victor Forsyuk <force@altlinux.org> 1.02-alt1
- Initial build.
