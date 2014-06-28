# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Class/Accessor/Lite.pm) perl(Class/Method/Modifiers.pm) perl(Data/OptList.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Module/Build.pm) perl(Module/Load.pm) perl(Test/More.pm) perl(Test/SharedFork.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.10
%define module_name Module-Build-Pluggable
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.10
Release: alt2
Summary: Module::Build meets plugins
Group: Development/Perl
License: perl
URL: https://github.com/tokuhirom/Module-Build-Pluggable

Source0: http://cpan.org.ua/authors/id/T/TO/TOKUHIROM/%module_name-%module_version.tar.gz
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
%doc Changes LICENSE README.md
%perl_vendor_privlib/T*
%perl_vendor_privlib/M*

%changelog
* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- moved to Sisyphus as dependency

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- initial import by package builder

