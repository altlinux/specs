Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       perl-DBIx-Class-DynamicDefault 
Version:    0.04
Release:    alt2_23
# lib/DBIx/Class/DynamicDefault.pm -> GPL+ or Artistic
License:    GPL+ or Artistic 
Summary:    Automatically set and update fields 
Url:        https://metacpan.org/release/DBIx-Class-DynamicDefault
Source:     https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/DBIx-Class-DynamicDefault-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/ExtraTests.pm)
BuildRequires:  perl(Module/Install/Makefile.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  perl(Module/Install/WriteAll.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(DBIx/Class.pm)
# Tests:
BuildRequires:  perl(DBICx/TestDatabase.pm)
BuildRequires:  perl(DBIx/Class/Schema.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DBIx/Class.pm) >= 0.081.270


# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl(DBIx.Class.pm)/d

%description
Automatically set and update fields with values calculated at run time.


%prep
%setup -q -n DBIx-Class-DynamicDefault-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/DBIx/Class/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_23
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_19
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_17
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_5
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_4
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_3
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- fc import

