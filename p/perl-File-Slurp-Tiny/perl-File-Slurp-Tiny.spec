# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurp.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 0.003
%define module_name File-Slurp-Tiny
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003
Release: alt1
Summary: A simple, sane and efficient file slurper
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
%doc Changes README LICENSE
%perl_vendor_privlib/F*

%changelog
* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- uploaded to Sisyphus as dependency

