%define module_version 1.19
%define module_name LEOCHARRE-CLI
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/PathInfo/Ext.pm) perl(File/Which.pm) perl(File/chmod.pm) perl(Getopt/Std.pm) perl(Linux/usermod.pm) perl(Test/Simple.pm) perl(YAML.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.19
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEOCHARRE/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/L*

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.19-alt2
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- initial import by package builder

