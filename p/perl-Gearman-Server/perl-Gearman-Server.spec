%define module_version 1.11
%define module_name Gearman-Server
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Danga/Socket.pm) perl(Errno.pm) perl(FindBin.pm) perl(Gearman/Util.pm) perl(IO/Handle.pm) perl(IO/Socket/INET.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Sys/Hostname.pm) perl(base.pm) perl(fields.pm) perl-devel
# END SourceDeps(oneline)
Name:           perl-Gearman-Server
Version:        1.11
Release:        alt2
Summary:        Function call "router" and load balancer
License:        perl
Group:          System/Servers
URL:            http://search.cpan.org/dist/Gearman-Server/
Source0:        http://cpan.org.ua/authors/id/D/DO/DORMANDO/%module_name-%module_version.tar.gz
BuildArch:      noarch

BuildRequires:  perl(ExtUtils/MakeMaker.pm)
Source44: import.info

%description
You run a Gearman server (or more likely, many of them for both high-
availability and load balancing), then have workers (using Gearman::Worker
from the Gearman module, or libraries for other languages) register their
ability to do certain functions to all of them, and then clients (using
Gearman::Client, Gearman::Client::Async, etc) request work to be done from
one of the Gearman servers.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES
%{_bindir}/gearmand
%{perl_vendor_privlib}/Gearman

%files scripts
%_bindir/*

%changelog
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

