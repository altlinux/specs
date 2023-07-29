# BEGIN SourceDeps(oneline):
BuildRequires: perl(Devel/StackTrace.pm) perl(Devel/StackTrace/Frame.pm) perl(Exception/Class.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Moo.pm) perl(Pod/Coverage/TrustPod.pm) perl(Pod/Wordlist.pm) perl(Scalar/Util.pm) perl(StackTrace/Auto.pm) perl(Test/CPAN/Changes.pm) perl(Test/EOL.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Test/Spelling.pm) perl(Test/Synopsis.pm) perl(Test/Version.pm) perl(base.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 1.000000
%define module_name Devel-StackTrace-Extract
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.000000
Release: alt2
Summary: Extract a stack trace from an exception object
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MA/MAXMIND/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
It's popular to store stack traces in objects that are thrown as exceptions,
but, this being Perl, there's more than one way to do it.  This module
provides a simple interface to attempt to extract the stack trace from various
well known exception classes that are on the CPAN.
%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.md Changes
%perl_vendor_privlib/D*

%changelog
* Sat Jul 29 2023 Igor Vlasenko <viy@altlinux.org> 1.000000-alt2
- to Sisyphus as perl-Log-Any dep

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- initial import by package builder

