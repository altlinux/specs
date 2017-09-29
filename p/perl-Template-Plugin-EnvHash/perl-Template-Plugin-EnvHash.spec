# BEGIN SourceDeps(oneline):
BuildRequires: perl(English.pm) perl(Module/Build.pm) perl(Template.pm) perl(Template/Plugin.pm) perl(Test/Distribution.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.06
%define module_name Template-Plugin-EnvHash
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.06
Release: alt2
Summary: Environment Variable Hash for TT2
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SR/SRSHAH/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/T*

%changelog
* Fri Sep 29 2017 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2
- to Sisyphus

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- initial import by package builder

