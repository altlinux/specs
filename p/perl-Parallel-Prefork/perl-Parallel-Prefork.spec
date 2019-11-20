Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Parallel-Prefork
Version:        0.18
Release:        alt1_11
Summary:        Simple prefork server framework
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Parallel-Prefork
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Parallel-Prefork-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  rpm-build-perl
BuildRequires:  perl(Class/Accessor/Lite.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Parallel/Scoreboard.pm)
BuildRequires:  perl(Proc/Wait3.pm)
BuildRequires:  perl(Scope/Guard.pm)
BuildRequires:  perl(Signal/Mask.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Requires.pm)
BuildRequires:  perl(Test/SharedFork.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(warnings.pm)

BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/ReadmeFromPod.pm)
Source44: import.info


%description
Parallel::Prefork is much like Parallel::ForkManager, but supports graceful
shutdown and run-time reconfiguration.

%prep
%setup -q -n Parallel-Prefork-%{version}
rm -r inc
sed -i -e '/^inc\/*$/d' MANIFEST

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_11
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_7
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_3
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_2
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_4
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_1
- update to new release by fcimport

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_2
- update to new release by fcimport

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- converted for ALT Linux by srpmconvert tools

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_5
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_4
- import for Sisyphus (required for RT)

* Tue Jan 15 2013 Andrew Kornilov <hiddenman@altlinux.ru> 0.13-alt1
- initial build for ALT Linux Sisyphus

