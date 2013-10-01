# BEGIN SourceDeps(oneline):
BuildRequires: perl(Devel/FindPerl.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec/Functions.pm) perl(FindBin.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.09
%define module_name Module-Path
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt2
Summary: get the full path to a locally installed module
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/N/NE/NEILB/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/M*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- regenerated from template by package builder

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- initial import by package builder

