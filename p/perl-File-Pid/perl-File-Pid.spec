Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-File-Pid
Version:        1.01
Release:        alt3_20
Summary:        Pid File Manipulation
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-Pid/
Source0:        http://www.cpan.org/authors/id/C/CW/CWEST/File-Pid-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Class/Accessor/Fast.pm) >= 0.19


Source44: import.info
%filter_from_requires /^perl\\(Class.Accessor.Fast.pm\\)$/d

%description
This software manages a pid file for you. It will create a pid file,
query the process within to discover if it's still running, and remove
the pid file.

%prep
%setup -q -n File-Pid-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_20
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_17
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_11
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_10
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_10
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_8
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_8
- fc import

