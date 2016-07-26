%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Carp.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(POSIX.pm) perl(Test/More.pm) perl(Time/Local.pm) perl(Time/TZOffset.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.42
%define module_name POSIX-strftime-Compiler
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.42
Release: alt1
Summary: GNU C library compatible strftime for loggers and servers
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/POSIX-strftime-Compiler

Source: http://www.cpan.org/authors/id/K/KA/KAZEBURO/POSIX-strftime-Compiler-%{version}.tar.gz
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
* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2
- moved to Sisyphus as dependency

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- initial import by package builder

