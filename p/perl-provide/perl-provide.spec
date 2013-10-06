%define module_version 0.03
%define module_name provide
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: easily choose between different version-specific implementations
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
%doc LICENSE README
%perl_vendor_privlib/p*

%changelog
* Sun Oct 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- Sisyphus build. required by Test-Easy update

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

