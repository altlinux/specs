# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.00
%define module_name URI-Simple
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.00
Release: alt2
Summary: Simple way to parse uri
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MAMOD/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
This module is a direct port of javascript parseURI regex by Steven Levithan
Please See Original Code

This module will attempts to split URIs according to RFC 3986


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/U*

%changelog
* Tue Feb 09 2021 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- to Sisyphus as shutter dep

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- initial import by package builder

