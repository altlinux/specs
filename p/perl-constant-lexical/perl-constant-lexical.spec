# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Sub/Delete.pm) perl(base.pm) perl(threads.pm) perl(threads/shared.pm) perl(Lexical/Sub.pm)
# END SourceDeps(oneline)
%define module_version 2.0001
%define module_name constant-lexical
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.0001
Release: alt2
Summary: Perl pragma to declare lexical compile-time constants
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SP/SPROUT/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
This module creates compile-time constants in the manner of.constant.pm, but makes them local to the enclosing scope.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/c*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.0001-alt2
- moved to Sisyphus as dependency

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.0001-alt1
- initial import by package builder

