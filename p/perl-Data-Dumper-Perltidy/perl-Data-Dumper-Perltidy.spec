# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Perl/Tidy.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.03
%define module_name Data-Dumper-Perltidy
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: Dump and pretty print Perl data structures.
Group: Development/Perl
License: perl
URL: http://jmcnamara.github.com/data-dumper-perltidy/

Source0: http://cpan.org.ua/authors/id/J/JM/JMCNAMARA/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/D*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 0.03-alt2
- to Sisyphus as perl-Devel-Trepan dep

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

