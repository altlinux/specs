# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(overload.pm) perl(warnings/register.pm)
# END SourceDeps(oneline)
%define module_version 1.02
%define module_name I18N-Collate
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.02
Release: alt2
Summary: compare 8-bit scalar data according to the current locale
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/I18N-Collate

Source0: http://cpan.org.ua/authors/id/F/FL/FLORA/%module_name-%module_version.tar.gz
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
%doc LICENSE README Changes
%perl_vendor_privlib/I*

%changelog
* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2
- to Sisyphus

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- initial import by package builder

