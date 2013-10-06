%define module_version 2.01
%define module_name Test-Resub
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.01
Release: alt2
Summary: Lexically scoped monkey patching for testing
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/B/BE/BELDEN/%module_name-%module_version.tar.gz
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
* Sun Oct 06 2013 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2
- Sisyphus build. required by Test-Easy update

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- initial import by package builder

