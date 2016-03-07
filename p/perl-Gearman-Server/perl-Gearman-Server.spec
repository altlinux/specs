# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Danga/Socket.pm) perl(Errno.pm) perl(FindBin.pm) perl(Gearman/Util.pm) perl(IO/Handle.pm) perl(IO/Socket/INET.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Sys/Hostname.pm) perl(base.pm) perl(fields.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Gearman-Server
Version:        1.12
Release:        alt1_4
Summary:        Function call "router" and load balancer
License:        GPL+ or Artistic
Group:          System/Servers
URL:            http://search.cpan.org/dist/Gearman-Server/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DO/DORMANDO/Gearman-Server-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(ExtUtils/MakeMaker.pm)


Source44: import.info
%filter_from_requires /^perl\\(Danga.Socket.pm\\)\s*$/d

%description
You run a Gearman server (or more likely, many of them for both high-
availability and load balancing), then have workers (using Gearman::Worker
from the Gearman module, or libraries for other languages) register their
ability to do certain functions to all of them, and then clients (using
Gearman::Client, Gearman::Client::Async, etc) request work to be done from
one of the Gearman servers.

%prep
%setup -q -n Gearman-Server-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES
%{_bindir}/gearmand
%{perl_vendor_privlib}/Gearman
%{_mandir}/man1/gearmand.*

%changelog
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

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_10
- update to new release by fcimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2
- build for Sisyphus (required for perl update)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_9
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_7
- update to new release by fcimport

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_5
- fc import

