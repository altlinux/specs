# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(Fcntl.pm) perl(FindBin.pm) perl(Pod/Usage.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-App-Daemon
Version:        0.18
Release:        alt2_1
Summary:        Start an Application as a Daemon
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/App-Daemon/
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHILLI/App-Daemon-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Pid.pm)
BuildRequires:  perl(Log/Log4perl.pm)
BuildRequires:  perl(Proc/ProcessTable.pm)
BuildRequires:  perl(Sysadm/Install.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
App::Daemon helps running an application as a daemon.

%prep
%setup -q -n App-Daemon-%{version}
chmod 644 eg/*
sed -i -e 's!/usr/local!/usr!' eg/*

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;


%files
%doc Changes README eg
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_1
- moved to Sisyphus

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- fc import

