Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Hash-Flatten
Version:        1.19
Release:        alt3_26
Summary:        Flatten/unflatten complex data hashes
License:        GPLv2
URL:            https://metacpan.org/release/Hash-Flatten
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBC/Hash-Flatten-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  glibc-locales glibc-timezones glibc-utils iconv
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(Getopt/Std.pm)
BuildRequires:  perl(Log/Trace.pm)
BuildRequires:  perl(Test/Assertions.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests only
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Requires:     perl(overload.pm)
Source44: import.info

%description
Converts back and forth between a nested hash structure and a flat hash of
delimited key-value pairs. Useful for protocols that only support key-value
pairs (such as CGI and DBMs).

%prep
%setup -q -n Hash-Flatten-%{version}
iconv -f latin1 -t utf8 Changes > Changes.utf && \
    touch Changes.utf -r Changes && \
    mv Changes.utf Changes

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc --no-dereference COPYING
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_26
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_20
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_18
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_17
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_14
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_8
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.19-alt3_7
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.19-alt2_7
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.19-alt2_5
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_5
- fc import

