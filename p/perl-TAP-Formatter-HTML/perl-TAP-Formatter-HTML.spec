Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Alien/SeleniumRC.pm) perl(CPAN.pm) perl(Cwd.pm) perl(Fcntl.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(IO/File.pm) perl(Time/HiRes.pm) perl(base.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-TAP-Formatter-HTML
Version:        0.11
Release:        alt1_19
Summary:        TAP Test Harness output delegate for html output
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/TAP-Formatter-HTML
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/TAP-Formatter-HTML-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel >= 5.6.0
BuildRequires:  rpm-build-perl
BuildRequires:  perl(accessors.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(TAP/Parser.pm)
BuildRequires:  perl(Template.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(URI.pm)
Requires:       perl(accessors.pm) >= 0.020
Requires:       perl(TAP/Parser.pm) >= 3.100
Requires:       perl(Template.pm) >= 2.140
Requires:       perl(URI.pm) >= 1.350
Source44: import.info

%description
This module provides HTML output formatting for TAP::Harness (a replacement
for Test::Harness. It is largely based on ideas from TAP::Test::HTMLMatrix
(which was built on Test::Harness and thus had a few limitations - hence
this module). For sample output, see:

%prep
%setup -q -n TAP-Formatter-HTML-%{version}

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
%doc Changes README Todo
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_19
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_15
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_11
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_8
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_5
- update to new release by fcimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_4
- Sisyphus build

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Tue Jan 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_8
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_6
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_6
- fc import

