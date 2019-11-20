Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Catalyst-Plugin-Session-Store-File
Version:        0.18
Release:        alt2_29
Summary:        File storage backend for session data
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-Store-File
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/Catalyst-Plugin-Session-Store-File-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel >= 5.8.0
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Cache/Cache.pm)
BuildRequires:  perl(Cache/FileCache.pm)
BuildRequires:  perl(Catalyst/Plugin/Session.pm)
BuildRequires:  perl(Catalyst/Plugin/Session/Store.pm)
BuildRequires:  perl(Catalyst/Plugin/Session/Test/Store.pm)
BuildRequires:  perl(Catalyst/Runtime.pm)
BuildRequires:  perl(Catalyst/Utils.pm)
BuildRequires:  perl(Class/Data/Inheritable.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/AutoInstall.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  perl(Module/Install/WriteAll.pm)
BuildRequires:  perl(MRO/Compat.pm)
BuildRequires:  perl(Path/Class.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  sed
Requires:       perl(Cache/Cache.pm) >= 1.020
Requires:       perl(Catalyst/Plugin/Session.pm)
Requires:       perl(Catalyst/Runtime.pm) >= 5.700.0
Requires:       perl(Class/Data/Inheritable.pm) >= 0.040
Source44: import.info

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess
cache. It is based on Cache::FileCache.

%prep
%setup -q -n Catalyst-Plugin-Session-Store-File-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
PERL5_CPANPLUS_IS_RUNNING=1 /usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_29
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_25
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_23
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_22
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_20
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_19
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_17
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_13
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_11
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_10
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_10
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_8
- fc import

