# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 1.03
%define module_name Array-OrdHash
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.03
Release: alt2
Summary: ordered associative array with array-like, hash-like and Object-oriented interface.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/W/WO/WOWASURIN/%module_name-%module_version.tar.gz
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
%doc README
%perl_vendor_privlib/A*

%changelog
* Tue Apr 18 2023 Igor Vlasenko <viy@altlinux.org> 1.03-alt2
- to Sisyphus as perl-User-Identity dep

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- initial import by package builder

