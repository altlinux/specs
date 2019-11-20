Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(Capture/Tiny.pm) perl(ExtUtils/CBuilder.pm) perl(IO/All.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Pod/Markdown.pm) perl(Sub/Uplevel.pm) perl(YAML/Tiny.pm) perl(parent.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Parallel-Scoreboard
Version:        0.08
Release:        alt1_10
Summary:        Scoreboard for monitoring status of many processes
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Parallel-Scoreboard
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Parallel-Scoreboard-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}

BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Test/Warn.pm)
BuildRequires:  perl(Test/More.pm)

# Run-time deps
BuildRequires: perl(Class/Accessor/Lite.pm)
BuildRequires: perl(Digest/MD5.pm)
BuildRequires: perl(Fcntl.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(HTML/Entities.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)

BuildRequires: perl(inc/Module/Install.pm)
BuildRequires: perl(Module/Install/ReadmeFromPod.pm)
Source44: import.info


%description
Parallel::Scoreboard is a pure-perl implementation of a process scoreboard.
By using the module it is easy to create a monitor for many worker process,
like the status module of the Apache HTTP server.

%prep
%setup -q -n Parallel-Scoreboard-%{version}
rm -r inc
sed -i -e '/^inc\/.*$/d' MANIFEST


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_10
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_4
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_2
- update to new release by fcimport

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_4
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- update to new release by fcimport

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update to new release by fcimport

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_8
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_7
- import for Sisyphus (required for RT)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_7
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_5
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_5
- fc import

