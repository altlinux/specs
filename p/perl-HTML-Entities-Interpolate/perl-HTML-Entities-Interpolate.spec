Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-HTML-Entities-Interpolate
Version:        1.10
Release:        alt1_1
Summary:        Call HTML::Entities::encode_entities via a hash within a string
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/HTML-Entities-Interpolate/
Source0:        http://www.cpan.org/authors/id/R/RS/RSAVAGE/HTML-Entities-Interpolate-%{version}.tgz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Slurper.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(HTML/Entities.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Tie/Function.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)


Source44: import.info

%description
This is a pure perl module which calls HTML::Entities::encode_entities 
via a hash within a string.

%prep
%setup -q -n HTML-Entities-Interpolate-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/HTML*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1_2
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1_1
- update to new release by fcimport

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- new version

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_6
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_3
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- initial import by package builder

