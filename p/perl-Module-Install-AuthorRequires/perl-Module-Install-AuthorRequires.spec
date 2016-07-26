# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Module-Install-AuthorRequires
Version:        0.02
Release:        alt2_12
Summary:        Declare author-only dependencies
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Module-Install-AuthorRequires/
Source0:        http://www.cpan.org/authors/id/F/FL/FLORA/Module-Install-AuthorRequires-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Module/Install/Base.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Modules often have optional requirements, for example dependencies that
are useful for (optional) tests, but not required for the module to
work properly.

Simply using this module "author_requires" command allows to specify such
developer specific dependencies in a proper way.

%prep
%setup -q -n Module-Install-AuthorRequires-%{version}
# Remove bundled module
rm -r inc
sed -i -e '/^inc/ d' MANIFEST 

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_12
- update to new release by fcimport

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_11
 - to Sisyphus as dependency

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_11
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_10
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_7
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- fc import

