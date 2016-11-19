%define _unpackaged_files_terminate_build 1
%define module_version 0.05
%define module_name Test2-Plugin-NoWarnings
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IPC/Run3.pm) perl(Test/More.pm) perl(Test2/API.pm) perl(Test2/Bundle/Extended.pm) perl(Test2/Event.pm) perl(Test2/Require/Module.pm) perl(Test2/Util/HashBase.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt1
Summary: Fail if tests warn
Group: Development/Perl
License: artistic_2
URL: http://metacpan.org/release/Test2-Plugin-NoWarnings

Source: http://www.cpan.org/authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-%{version}.tar.gz
BuildArch: noarch

%description
Loading this plugin causes your tests to fail if there any warnings while they
run. Each warning generates a new failing test and the warning content is
outputted via `diag'.

This module uses `$SIG{__WARN__}', so if the code you're testing sets this,
then this module will stop working.
%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md LICENSE Changes
%perl_vendor_privlib/T*

%changelog
* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- to Sisyphus

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Wed Aug 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

