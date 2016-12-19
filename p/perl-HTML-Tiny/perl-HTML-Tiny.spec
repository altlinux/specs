Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-HTML-Tiny
Version:        1.05
Release:        alt2_22
Summary:        Lightweight, dependency free HTML/XML generation
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/HTML-Tiny/
Source0:        http://www.cpan.org/authors/id/A/AN/ANDYA/HTML-Tiny-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info


%description
HTML::Tiny is a simple, dependency free module for generating HTML (and
XML). It concentrates on generating syntactically correct XHTML using a
simple Perl notation.

%prep
%setup -q -n HTML-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/HTML*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_22
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_19
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_13
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_12
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_12
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_10
- fc import

