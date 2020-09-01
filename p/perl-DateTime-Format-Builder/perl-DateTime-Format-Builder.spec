%define _unpackaged_files_terminate_build 1
%define module DateTime-Format-Builder

Name: perl-%module
Version: 0.83
Release: alt1
Epoch: 1

Summary: DateTime::Format::Builder - create DateTime parser classes and objects
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 27 2011
BuildRequires: perl-Class-Factory-Util perl-DateTime-Format-Mail perl-DateTime-Format-Strptime perl-Module-Build perl-Task-Weaken perl-Test-Pod

%description
DateTime::Format::Builder - create DateTime parser classes and objects.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CONTRIBUTING.md README.md Changes examples
%perl_vendor_privlib/DateTime/*

%changelog
* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.83-alt1
- automated CPAN update

* Mon Mar 04 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.82-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.81-alt1
- automated CPAN update

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1:0.80-alt1
- 0.80

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.7901-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Aug 05 2008 Victor Forsyuk <force@altlinux.org> 0.7901-alt1
- Initial build.
