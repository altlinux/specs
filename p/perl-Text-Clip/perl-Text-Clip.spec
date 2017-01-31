# BEGIN SourceDeps(oneline):
BuildRequires: perl(Any/Moose.pm) perl(ExtUtils/MakeMaker.pm) perl(Moose.pm) perl(Test/Most.pm)
# END SourceDeps(oneline)
%define module_version 0.0014
%define module_name Text-Clip
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.0014
Release: alt2
Summary: Clip and extract text in clipboard-like way
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/R/RO/ROKR/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/T*

%changelog
* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt2
- to Sisyphus

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt1
- initial import by package builder

