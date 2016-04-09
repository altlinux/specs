# BEGIN SourceDeps(oneline):
BuildRequires: perl(Module/Build.pm) perl(Moose.pm) perl(Moose/Exporter.pm) perl(Moose/Role.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.05
%define module_name MooseX-Role-Strict
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2.1
Summary: use strict 'roles'
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/O/OV/OVID/%module_name-%module_version.tar.gz
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
%doc Changes README TODO
%perl_vendor_privlib/M*

%changelog
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2.1
- rebuild to restore role requires

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- moved to Sisyphus as perl update dependency

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

