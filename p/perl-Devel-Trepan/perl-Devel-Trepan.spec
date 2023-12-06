# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-macros-mageia-compat
BuildRequires: perl(CPAN.pm) perl(Data/Dumper/Perltidy.pm) perl(Pod/Usage.pm) perl(Scope/Upper.pm) perl(Term/ANSIColor.pm) perl(Variable/Magic.pm) perl(threads.pm) perl(threads/shared.pm) perl-podlators
# END SourceDeps(oneline)

%add_findreq_skiplist %perl_vendor_privlib/Devel/Trepan/CmdProcessor/Command/Set_Subcmd/Display_Subcmd/Eval.pm
%add_findreq_skiplist %perl_vendor_privlib/Devel/Trepan/CmdProcessor/Command/Enable.pm
%add_findreq_skiplist %perl_vendor_privlib/Devel/Trepan/CmdProcessor/Command/*
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Devel-Trepan
%define upstream_version v1.0.1

Name:       perl-%{upstream_name}
Version:    1.0.1
Release:    alt3_2

Summary:    A gdb-like debugger port of Ruby Trepan
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Array/Columnize.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Devel/Callsite.pm)
BuildRequires: perl(Digest/SHA.pm)
BuildRequires: perl(File/HomeDir.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(Marpa/R2.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(PadWalker.pm)
BuildRequires: perl(Pod/Find.pm)
BuildRequires: perl(Pod/Text.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Syntax/Highlight/Perl/Improved.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Time/HiRes.pm)
BuildRequires: perl(rlib.pm)
BuildRequires: perl(version.pm)
BuildArch:  noarch

%{?perl_default_filter}
# Exclude internal broken dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::Trepan::
Source44: import.info

%description
Invocation
    From a shell:

        $ trepan.pl [trepan-opts] -- perl-program [perl-program-opts]

    For out-of-process (and possibly out-of server) debugging:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%if "%{version}" == "1.0.1"
# broken in perl 5.36
%make test ||:
%else
%make test
%endif

%install
%makeinstall_std

%files
%doc ChangeLog Changes LICENSE META.json META.yml  README SIGNATURE THANKS example
%perl_vendor_privlib/*
/usr/bin/trepan.pl

%changelog
* Wed Dec 06 2023 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt3_2
- FTBFS fix after perl 5.38

* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt2_2
- to Sisyphus as perl-Finance-Quote dep

* Tue Mar 10 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2
- update by mgaimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> v1.0.0-alt1_2
- update by mgaimport

* Mon Aug 27 2018 Igor Vlasenko <viy@altlinux.ru> v1.0.0-alt1_1
- update by mgaimport

* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1_2
- update by mgaimport

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1_1
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_2
- update by mgaimport

* Sat May 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_1
- update by mgaimport

* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_2
- new release

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1_1
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.52-alt2_1
- rebuild to get rid of unmets

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_1
- import

