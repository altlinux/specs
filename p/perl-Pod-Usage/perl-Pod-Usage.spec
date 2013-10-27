# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(Pod/PlainText.pm) perl(Pod/Text.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.63
%define module_name Pod-Usage
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.63
Release: alt1
Summary: Pod::Usage extracts POD documentation and shows usage information
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MAREKR/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/P*
%_bindir/*
%_man1dir/*

%changelog
* Sun Oct 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.63-alt1
- Sisyphus build

