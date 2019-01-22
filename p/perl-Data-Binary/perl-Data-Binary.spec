# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.01
%define module_name Data-Binary
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt2
Summary: Simple detection of binary versus text in strings
Group: Development/Perl
License: artistic_2
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SN/SNKWATT/%module_name-%module_version.tar.gz
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
%doc changes.txt readme.txt README
%perl_vendor_privlib/D*

%changelog
* Tue Jan 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- to Sisyphus as Module-CPANTS-Analyse dep

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

