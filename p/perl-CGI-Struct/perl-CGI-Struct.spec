%define module_version 1.21
%define module_name CGI-Struct
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CGI.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Storable.pm) perl(Test/Deep.pm) perl(Test/Deep/NoTest.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.21
Release: alt2
Summary: Build structures from CGI data
Group: Development/Perl
License: bsd
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/F/FU/FULLERMD/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/C*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt2
- moved to Sisyphus (for Catalyst-Runtime update)

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- initial import by package builder

