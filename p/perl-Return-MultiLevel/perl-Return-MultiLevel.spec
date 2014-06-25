# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.03
%define module_name Return-MultiLevel
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: return across multiple call levels
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MAUKE/%module_name-%module_version.tar.gz
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
%doc Changes README
%perl_vendor_privlib/R*

%changelog
* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- moved to Sisyphus

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

