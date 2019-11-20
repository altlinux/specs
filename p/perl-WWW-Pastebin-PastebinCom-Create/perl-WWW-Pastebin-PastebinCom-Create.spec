Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(overload.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-WWW-Pastebin-PastebinCom-Create
Version:        1.003
Release:        alt1_16
Summary:        Paste to http://pastebin.com from Perl
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/WWW-Pastebin-PastebinCom-Create
Source0:        https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/WWW-Pastebin-PastebinCom-Create-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(LWP/UserAgent.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(Test/Kwalitee.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(WWW/Mechanize.pm)


Source44: import.info

%description
The module provides means of pasting large texts into http://pastebin.com
pastebin site.

%prep
%setup -q -n WWW-Pastebin-PastebinCom-Create-%{version}
# Disable the 01-paste test as it requires network access which we don't
# have when building in koji
rm t/01-paste.t

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README examples
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_16
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_12
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_10
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_8
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_6
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2_7
- update to new release by fcimport

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt2_6
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_3
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_1
- fc import

