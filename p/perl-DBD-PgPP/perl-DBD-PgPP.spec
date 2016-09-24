# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBI.pm) perl(Digest/MD5.pm) perl(IO/Socket.pm)
# END SourceDeps(oneline)
%define module_version 0.08
%define module_name DBD-PgPP
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/A/AR/ARC/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/D*

%changelog
* Sat Sep 24 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- to Sisyphus

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

