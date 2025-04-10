# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Exporter.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.003
%define module_name Test-Settings
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003
Release: alt2
Summary: Ask or tell when certain types of tests should be run
Group: Development/Perl
License: perl
URL: https://github.com/wolfsage/Test-Settings

Source0: http://cpan.org.ua/authors/id/W/WO/WOLFSAGE/%module_name-%module_version.tar.gz
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
%doc README Changes LICENSE
%perl_vendor_privlib/T*

%changelog
* Thu Apr 10 2025 Igor Vlasenko <viy@altlinux.org> 0.003-alt2
- to Sisyphus as Tapper-Reports-Web dep

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

