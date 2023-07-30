%define module_name match-simple
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(MRO/Compat.pm) perl(Scalar/Util.pm) perl(Sub/Infix.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Tie/RefHash.pm) perl(match/simple/XS.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.012
Release: alt2
Summary: simplified clone of smartmatch operator
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/match-simple

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CREDITS Changes LICENSE COPYRIGHT README
%perl_vendor_privlib/m*

%changelog
* Sat Jul 29 2023 Igor Vlasenko <viy@altlinux.org> 0.012-alt2
- to Sisyphus as perl-IO-Prompter dep

* Wed Feb 15 2023 Igor Vlasenko <viy@altlinux.org> 0.012-alt1
- updated by package builder

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.011-alt1
- updated by package builder

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- regenerated from template by package builder

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- regenerated from template by package builder

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- regenerated from template by package builder

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- initial import by package builder

