# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/Config.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec/Functions.pm) perl(IPC/Open2.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.006
%define module_name Devel-FindPerl
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.006
Release: alt2
Summary: Find the path to your perl
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEONT/%module_name-%module_version.tar.gz
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
%doc README LICENSE Changes
%perl_vendor_privlib/D*

%changelog
* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt2
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- initial import by package builder

