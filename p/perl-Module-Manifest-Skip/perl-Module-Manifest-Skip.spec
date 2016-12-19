# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Module-Manifest-Skip
Version:        0.23
Release:        alt1_6
Summary:        MANIFEST.SKIP Manangement for Modules
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Module-Manifest-Skip/
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/Module-Manifest-Skip-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/ShareDir/Install.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(File/ShareDir.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Moo.pm)
# Tests:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(File/ShareDir.pm)
Requires:       perl(File/Spec.pm)
Requires:       perl(Moo.pm) >= 0.091.013
Requires:       perl(warnings.pm)

# Remove under-speficied dependencies

Source44: import.info
%filter_from_requires /^perl\\(Moo.pm\\)$/d

%description
CPAN module authors use a MANIFEST.SKIP file to exclude certain well known
files from getting put into a generated MANIFEST file, which would cause them
to go into the final distribution package.

The packaging tools try to automatically skip things for you, but if you add
one of your own entries, you have to add all the common ones yourself.  This
module attempts to make all of this boring process as simple and reliable as
possible.


%prep
%setup -q -n Module-Manifest-Skip-%{version}

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
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_6
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_4
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_1
- update to new release by fcimport

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2_4
- update to new release by fcimport

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2_3
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_3
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_2
- update to new release by fcimport

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_1
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- fc import

