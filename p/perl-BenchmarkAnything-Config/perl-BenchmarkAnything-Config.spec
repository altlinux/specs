# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBD/SQLite.pm) perl(ExtUtils/MakeMaker.pm) perl(File/HomeDir.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/EOL.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(YAML/Any.pm) perl(blib.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 0.003
%define module_name BenchmarkAnything-Config
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003
Release: alt2
Summary: Read BenchmarkAnything configfile
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/BenchmarkAnything-Config

Source0: http://cpan.org.ua/authors/id/S/SC/SCHWIGON/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE
%perl_vendor_privlib/B*

%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2
- to Sisyphus

* Mon Oct 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

