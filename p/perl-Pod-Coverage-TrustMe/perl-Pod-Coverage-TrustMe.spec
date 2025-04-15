%define module_name Pod-Coverage-TrustMe
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Cwd.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(Getopt/Long.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Pod/Simple.pm) perl(Pod/Usage.pm) perl(Test/Builder.pm) perl(Test/More.pm) perl(Test/Needs.pm) perl(Test/Pod/Coverage.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002001
Release: alt2
Summary: Pod::Coverage but more powerful
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/H/HA/HAARG/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Checks that all of the functions or methods provided by a package have
documentation. Compatible with most uses of the Pod::Coverage manpage, but with
additional features.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %EVR

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/T*
%perl_vendor_privlib/P*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Tue Apr 15 2025 Igor Vlasenko <viy@altlinux.org> 0.002001-alt2
- to Sisyphus as CPAN-Changes dep

* Mon Apr 07 2025 Igor Vlasenko <viy@altlinux.org> 0.002001-alt1
- updated by package builder

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.002000-alt1
- updated by package builder

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.ru> 0.001002-alt1
- initial import by package builder

