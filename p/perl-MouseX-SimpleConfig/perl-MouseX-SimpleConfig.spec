# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config/Any.pm) perl(English.pm) perl(ExtUtils/MakeMaker.pm) perl(Mouse.pm) perl(Mouse/Role.pm) perl(MouseX/ConfigFromFile.pm) perl(Path/Class/File.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.11
%define module_name MouseX-SimpleConfig
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.11
Release: alt2
Summary: A Mouse role for setting attributes from a simple configfile
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MJ/MJGARDNER/%module_name-%module_version.tar.gz
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
%doc Changes README LICENSE
%perl_vendor_privlib/M*

%changelog
* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- moved to Sisyphus as dependency

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- initial import by package builder

