%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/Gearman/Task.pm
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Gearman
Version:        2.004.0013
Release:        alt1
Summary:        Perl interface for Gearman distributed job system
License:        GPL+ or Artistic
URL:            http://danga.com/gearman/
Source0:        http://www.cpan.org/authors/id/P/PA/PALIK/Gearman-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(fields.pm)
BuildRequires:  perl(IO/Select.pm)
BuildRequires:  perl(IO/Socket/IP.pm)
BuildRequires:  perl(IO/Socket/SSL.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Socket.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(String/CRC32.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(version.pm)
# Tests:
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Which.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Net/EmptyPort.pm)
BuildRequires:  perl(Perl/OSType.pm)
BuildRequires:  perl(Proc/Guard.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/TCP.pm)
BuildRequires:  perl(Test/Timer.pm)
BuildRequires:  perl(vars.pm)
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build cycle: perl-Gearman a.. perl-Gearman-Server a.. perl-Gearman
# perl-Gearman-Server for %%{_bindir}/gearmand
BuildRequires:  perl-Gearman-Server
%endif
# Devel::Gladiator not yet packaged
Requires:       perl(version.pm) >= 0.770

# Remove under-specifed dependencies

Source44: import.info
%filter_from_requires /^perl\\(version.pm\\)$/d

%description
Gearman provides a generic application framework to farm out work to other
machines or processes that are better suited to do the work. It allows you
to do work in parallel, to load balance processing, and to call functions
between languages. 

%prep
%setup -q -n Gearman-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README TODO
%{perl_vendor_privlib}/Gearman

%changelog
* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.004.0013-alt1
- automated CPAN update

* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.004.012-alt1
- automated CPAN update

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 2.004.011-alt1
- automated CPAN update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.004.010-alt1
- automated CPAN update

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 2.004.009-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.004.008-alt1_2
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.004.008-alt1_1
- update to new release by fcimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.004.008-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.004.004-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.003.002-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.003.001-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.002.004-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.130.004-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_3
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_1
- update to new release by fcimport

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_11
- update to new release by fcimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_10
- build for Sisyphus (required for perl update)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_9
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_7
- update to new release by fcimport

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_5
- fc import

