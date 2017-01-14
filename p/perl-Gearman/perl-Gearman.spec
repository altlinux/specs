%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators perl(Perl/OSType.pm) perl(Test/Exception.pm) perl(Test/Timer.pm) perl(File/Which.pm) perl(IO/Socket/IP.pm) perl(Net/EmptyPort.pm) perl(Ref/Util.pm) perl(Test/Differences.pm) perl(IO/Socket/SSL.pm) perl(List/MoreUtils.pm) perl(Proc/Guard.pm)
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/Gearman/Task.pm
Name:           perl-Gearman
Version:        2.002.004
Release:        alt1
Summary:        Distributed job system
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://danga.com/gearman/
Source0:        http://www.cpan.org/authors/id/P/PA/PALIK/Gearman-%{version}.tar.gz
BuildArch:      noarch


BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Errno.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(fields.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IO/Socket/INET.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Socket.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(String/CRC32.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)



Source44: import.info
%filter_from_provides /^perl\\(Gearman.Client.pm\\)$/d

%description
Gearman provides a generic application framework to farm out work to other
machines or processes that are better suited to do the work. It allows you
to do work in parallel, to load balance processing, and to call functions
between languages. 

%prep
%setup -q -n Gearman-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES TODO
%{perl_vendor_privlib}/Gearman

%changelog
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

