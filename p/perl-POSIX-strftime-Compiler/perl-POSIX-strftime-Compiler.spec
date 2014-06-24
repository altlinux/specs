# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Carp.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(POSIX.pm) perl(Test/More.pm) perl(Time/Local.pm) perl(Time/TZOffset.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.31
%define module_name POSIX-strftime-Compiler
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.31
Release: alt2
Summary: GNU C library compatible strftime for loggers and servers
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/POSIX-strftime-Compiler

Source0: http://cpan.org.ua/authors/id/K/KA/KAZEBURO/%module_name-%module_version.tar.gz
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
%doc README.md Changes LICENSE
%perl_vendor_privlib/P*

%changelog
* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2
- moved to Sisyphus as dependency

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- initial import by package builder

