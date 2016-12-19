# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Data/Dump.pm) perl(List/MoreUtils.pm) perl(OpenGL.pm) perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-Math-MatrixReal
Version:        2.13
Release:        alt1_1
Summary:        Manipulate matrix of reals
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Math-MatrixReal/
Source0:        http://www.cpan.org/authors/id/L/LE/LETO/Math-MatrixReal-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(vars.pm)
# Tests:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Benchmark.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Math/Complex.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Most.pm)
BuildRequires:  perl(Test/Simple.pm)
Source44: import.info

%description
Implements the data type "matrix of reals" (and consequently also
"vector of reals") which can be used almost like any other basic
Perl type thanks to OPERATOR OVERLOADING, i.e.,

    $A = $matrix1 * $matrix2;
    $B = $A ** 2;
    $C = $A + 2*B;
    $D = $C - $B/2;
    $inverse = $C ** -1;
    $inverse = 1/$C;
    
does what you would like it to do.

%prep
%setup -q -n Math-MatrixReal-%{version}
chmod -x example/*

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc CHANGES CONTRIBUTING.md CREDITS example GOALS README.mkd OLD_README TODO
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_1
- update to new release by fcimport

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_3
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_1
- update to new release by fcimport

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_2
- update to new release by fcimport

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_1
- update to new release by fcimport

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_1
- update to new release by fcimport

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.09-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.09-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.09-alt2_5
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.09-alt2_4
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1_4
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1_2
- fc import

