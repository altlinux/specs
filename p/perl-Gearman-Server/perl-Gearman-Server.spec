# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-Gearman-Server
Version:        1.130.1
Release:        alt1_2
Summary:        Function call router and load balancer
License:        GPL+ or Artistic
Group:          System/Servers
URL:            http://search.cpan.org/dist/Gearman-Server/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PA/PALIK/Gearman-Server-v%{version}.tar.gz
# Use absolute interpreter
Patch0:         Gearman-Server-v1.130.0-Do-not-use-usr-bin-env.patch
# Load IO::Socket::INET in Gearman/Server.pm
Patch1:         Gearman-Server-v1.130.1-Load-IO-Socket-INET.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Danga/Socket.pm)
BuildRequires:  perl(Errno.pm)
BuildRequires:  perl(fields.pm)
BuildRequires:  perl(Gearman/Util.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IO/Socket/INET.pm)
BuildRequires:  perl(Pod/Usage.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Socket.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Sys/Hostname.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Script.pm)


Source44: import.info
%filter_from_requires /^perl\\(Danga.Socket.pm\\)$/d

%description
You run a Gearman server (or more likely, many of them for both high-
availability and load balancing), then have workers (using Gearman::Worker
from the Gearman module, or libraries for other languages) register their
ability to do certain functions to all of them, and then clients (using
Gearman::Client, Gearman::Client::Async, etc) request work to be done from
one of the Gearman servers.

%prep
%setup -q -n Gearman-Server-v%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README.md
%{_bindir}/gearmand
%{perl_vendor_privlib}/Gearman
%{_mandir}/man1/gearmand.*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.130.1-alt1_2
- update to new release by fcimport

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.130.1-alt1
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

