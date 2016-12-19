# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Perl/Critic.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Statistics-Basic
Version:        1.6611
Release:        alt1_5
Summary:        A collection of very basic statistics modules
License:        LGPLv2+
Group:          Development/Other
URL:            http://search.cpan.org/dist/Statistics-Basic/
Source0:        http://www.cpan.org/authors/id/J/JE/JETTERO/Statistics-Basic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Number/Format.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Scalar/Util.pm)
# Tests
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Number/Format.pm) >= 1.42

# Remove underspecified dependecies

Source44: import.info
%filter_from_requires /perl\\(Number.Format.pm\\)$/d

%description
use Statistics::Basic qw(:all);

my $median = median( 1,2,3 );
my $mean   = mean(  [1,2,3]); # array refs are ok too

my $variance = variance( 1,2,3 );
my $stddev   = stddev(   1,2,3 );

my $correlation = correlation( [1 .. 3], [1 .. 3] );


%prep
%setup -q -n Statistics-Basic-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=perl NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.6611-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.6611-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.6611-alt1_3
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.6611-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.6607-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.6607-alt2_7
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.6607-alt2_6
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.6607-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.6607-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6607-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.6607-alt1_3
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.6607-alt1_1
- fc import

