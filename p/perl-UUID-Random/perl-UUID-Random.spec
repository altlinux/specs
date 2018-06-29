%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.04
%define module_name UUID-Random
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt2
Summary: Generate random uuid strings
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/P/PE/PERLER/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/U*

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- to Sisyphus as perl-MongoDB dep

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

