# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(diagnostics.pm)
# END SourceDeps(oneline)
%define module_version 0.10
%define module_name Geo-Coordinates-Transform
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.10
Release: alt2
Summary: Transform Latitude/Longitude between various different coordinate
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/T/TR/TROXEL/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/G*

%changelog
* Sat Oct 08 2022 Igor Vlasenko <viy@altlinux.org> 0.10-alt2
- to Sisyphus as perl-Geo-Gpx dep

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- initial import by package builder

