%define module_version 1.001
%define module_name Config-INI-Reader-Multiline
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config/INI/Reader.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/CPAN/Meta.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(blib.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.001
Release: alt2
Summary: Parser for .ini files with line continuations
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BO/BOOK/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/C*

%changelog
* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 1.001-alt2
- to Sisyphus

* Sun Aug 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1
- regenerated from template by package builder

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1
- initial import by package builder

