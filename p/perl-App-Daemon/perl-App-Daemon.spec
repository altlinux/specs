Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(Fcntl.pm) perl(FindBin.pm) perl(Pod/Usage.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-App-Daemon
Version:        0.22
Release:        alt1_14
Summary:        Start an Application as a Daemon
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/App-Daemon
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/App-Daemon-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
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
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README eg
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_14
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_10
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_6
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_1
- update to new release by fcimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_2
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_1
- moved to Sisyphus

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- fc import

