# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(threads.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Tie-RefHash-Weak
Version:	0.09
Release:	alt3_20
Summary:	Tie::RefHash subclass with weakened references in the keys
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Tie-RefHash-Weak/
Source0:	http://search.cpan.org/CPAN/authors/id/N/NU/NUFFIN/Tie-RefHash-Weak-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(base.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(Task/Weaken.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Tie/RefHash.pm)
BuildRequires:	perl(Variable/Magic.pm)
Source44: import.info

%description
The Tie::RefHash module can be used to access hashes by reference. This is
useful when you index by object, for example.

%prep
%setup -q -n Tie-RefHash-Weak-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes TODO
%{perl_vendor_privlib}/Tie/

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3_19
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3_16
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3_15
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_14
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_13
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_12
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_10
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_10
- fc import

