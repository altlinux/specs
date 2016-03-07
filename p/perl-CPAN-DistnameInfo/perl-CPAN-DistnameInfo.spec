# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-CPAN-DistnameInfo
Version:        0.12
Release:        alt2_6
Summary:        Extract distribution name and version from a distribution filename
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/CPAN-DistnameInfo/
Source0:        http://www.cpan.org/authors/id/G/GB/GBARR/CPAN-DistnameInfo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Tests:
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Many online services that are centered around CPAN attempt to
associate multiple uploads by extracting a distribution name from the
filename of the upload. For most distributions this is easy as they
have used ExtUtils::MakeMaker or Module::Build to create the
distribution, which results in a uniform name. But sadly not all
uploads are created in this way.

CPAN::DistnameInfo uses heuristics that have been learnt by
http://search.cpan.org/ to extract the distribution name and version
from filenames and also report if the version is to be treated as a
developer release.

%prep
%setup -q -n CPAN-DistnameInfo-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/CPAN/

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_2
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_1
- update to new release by fcimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2
- build for Sisyphus (required for perl update)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_9
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_7
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_5
- fc import

