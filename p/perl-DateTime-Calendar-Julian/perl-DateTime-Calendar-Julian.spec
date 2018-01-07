# BEGIN SourceDeps(oneline):
BuildRequires: perl(DateTime.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.04
%define module_name DateTime-Calendar-Julian
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/P/PI/PIJLL/%module_name-%module_version.tar.gz
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
%doc Changes README LICENSE
%perl_vendor_privlib/D*

%changelog
* Sun Jan 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- to Sisyphus as biber dep

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

