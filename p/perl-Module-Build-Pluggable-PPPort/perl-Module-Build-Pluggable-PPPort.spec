# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Accessor/Lite.pm) perl(Devel/PPPort.pm) perl(Module/Build.pm) perl(Module/Build/Pluggable.pm) perl(Module/Build/Pluggable/Base.pm) perl(Test/Module/Build/Pluggable.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.04
%define module_name Module-Build-Pluggable-PPPort
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt2
Summary: Generate ppport.h
Group: Development/Perl
License: perl
Url: %CPAN %module_name

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
%doc LICENSE Changes README
%perl_vendor_privlib/M*

%changelog
* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- moved to Sisyphus as dependency

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

