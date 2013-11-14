%define module_version 1.00002
%define module_name Sub-Delete
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(base.pm) perl(constant.pm) perl(strict.pm) perl(threads.pm) perl(threads/shared.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.00002
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SP/SPROUT/%module_name-%module_version.tar.gz
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
%doc README Changes
%perl_vendor_privlib/S*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.00002-alt2
- moved to Sisyphus (for Catalyst-Runtime update)

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.00002-alt1
- initial import by package builder

