# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-Math-Expression-Evaluator
Version:        0.3.2
Release:        alt2_12
Summary:        Parses, compiles and evaluates mathematics expressions
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Math-Expression-Evaluator/
Source0:        http://www.cpan.org/authors/id/M/MO/MORITZ/Math-Expression-Evaluator-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Benchmark.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Math/Trig.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
Math::Expression::Evaluator is a parser, compiler and interpreter for
mathematical expressions. It can handle normal arithmetic (including
powers wit ^ or **), built-in functions like sin() and variables.

%prep
%setup -q -n Math-Expression-Evaluator-v%{version}
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.pm' -exec chmod -x {} 2>/dev/null ';'

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes examples README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt2_12
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt2_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt2_7
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt2_6
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_4
- initial fc import

