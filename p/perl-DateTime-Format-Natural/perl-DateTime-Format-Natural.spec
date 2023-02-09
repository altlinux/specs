%define _unpackaged_files_terminate_build 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DateTime/HiRes.pm) perl(DateTime/Locale.pm) perl(Term/ReadLine.pm) perl(Test/MockTime/HiRes.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DateTime-Format-Natural
Version:        1.16
Release:        alt1
Summary:        Create machine readable date/time with natural parsing logic
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DateTime-Format-Natural
Source0:        http://www.cpan.org/authors/id/S/SC/SCHUBIGER/DateTime-Format-Natural-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  glibc-locales glibc-timezones glibc-utils iconv
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(boolean.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Clone.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/TimeZone.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Module/Util.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Storable.pm)
# Tests only
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Date/Calc.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(Test/MockTime.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
DateTime::Format::Natural takes a string with a human readable date/time
and creates a machine readable one by applying natural parsing logic.

%package -n perl-DateTime-Format-Natural-Test
Group: Development/Perl
Summary:        Common test routines/data for perl-DateTime-Format-Natural
Requires:       %{name} = %{version}-%{release}

%description -n perl-DateTime-Format-Natural-Test
The DateTime::Format::Natural::Test class exports common test routines.

%prep
%setup -q -n DateTime-Format-Natural-%{version}
for f in Changes README; do
        iconv -f iso8859-1 -t utf-8 $f >$f.conf && mv $f.conf $f
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%exclude %{perl_vendor_privlib}/DateTime/Format/Natural/Test.pm
%{perl_vendor_privlib}/*
%{_bindir}/dateparse
%{_mandir}/man1/*

%files -n perl-DateTime-Format-Natural-Test
%{perl_vendor_privlib}/DateTime/Format/Natural/Test.pm


%changelog
* Thu Feb 09 2023 Igor Vlasenko <viy@altlinux.org> 1.16-alt1
- automated CPAN update

* Mon Jan 16 2023 Igor Vlasenko <viy@altlinux.org> 1.15-alt1
- automated CPAN update

* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1.14-alt1
- automated CPAN update

* Thu Jan 27 2022 Igor Vlasenko <viy@altlinux.org> 1.13-alt1
- automated CPAN update

* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 1.12-alt2
- fixed build

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 1.12-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Sat Jul 04 2020 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Wed Dec 11 2019 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_3
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_1
- update to new release by fcimport

* Sun Mar 31 2019 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- update to new release by fcimport

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_5
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_2
- update to new release by fcimport

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_1
- update to new release by fcimport

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_1
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_2
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_1
- moved to Sisyphus

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_3
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_1
- fc import

