%define module_version 0.15
%define module_name Spreadsheet-XLSX
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Archive/Zip.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Spreadsheet/ParseExcel.pm) perl(Spreadsheet/ParseExcel/Workbook.pm) perl(Test/Kwalitee.pm) perl(Test/More.pm) perl(Test/NoWarnings.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.15
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MI/MIKEB/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/S*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 0.15-alt2
- to Sisyphus as perl-Finance-Quote dep

* Tue Nov 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- initial import by package builder

