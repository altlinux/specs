Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DateTime-Format-Epoch
Version:        0.16
Release:        alt1_14
Summary:        Convert DateTimes to/from epoch seconds
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DateTime-Format-Epoch
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-Epoch-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/LeapSecond.pm)
BuildRequires:  perl(Math/BigInt.pm)
BuildRequires:  perl(Math/BigInt/GMP.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
# Optional Tests
BuildRequires:  perl(Test/Pod.pm)
# Dependencies
Requires:       perl(DateTime.pm) >= 0.310
Requires:       perl(Math/BigInt.pm) >= 1.660
Requires:       perl(Math/BigInt/GMP.pm)

# Filter under-specified dependencies


Source44: import.info
%filter_from_requires /^perl(Math.BigInt.pm)/d
%filter_from_requires /^perl(DateTime.pm)/d

%description
This module can convert a DateTime object (or any object that can be
converted to a DateTime object) to the number of seconds since a given
epoch. It can also do the reverse.

%prep
%setup -q -n DateTime-Format-Epoch-%{version}
find -type f -print0 | xargs -0 sed -i 's/\r$//'

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=true NO_PERLLOCAL=true
%make_build

%install
make install DESTDIR=%{buildroot}
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes README TODO
%{perl_vendor_privlib}/DateTime/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_14
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_10
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_9
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_6
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_5
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_4
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_2
- update to new release by fcimport

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_5
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_4
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- fc import

