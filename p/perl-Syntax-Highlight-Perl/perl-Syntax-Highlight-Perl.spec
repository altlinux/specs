# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(FileHandle.pm)
# END SourceDeps(oneline)
%define module_version 1.0
%define module_name Syntax-Highlight-Perl
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.0
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JO/JOHNSCA/%module_name-%module_version.tar.gz
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
%doc ChangeLog README
%perl_vendor_privlib/S*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 1.0-alt2
- to Sisyphus as perl-Devel-Trepan dep

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- initial import by package builder

