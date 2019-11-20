Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Module-Package
Version:        0.30
Release:        alt2_21
Summary:        Postmodern Perl Module Packaging
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Module-Package
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Package-%{version}.tar.gz
# Fix building on Perl without "." in @INC, CPAN RT#121748
Patch0:         Module-Package-0.30-Fix-building-on-Perl-without-.-in-INC.patch
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(IO/All.pm)
BuildRequires:  perl(Module/Install.pm)
BuildRequires:  perl(Module/Install/AuthorRequires.pm)
BuildRequires:  perl(Module/Install/Base.pm)
BuildRequires:  perl(Module/Install/ManifestSkip.pm)
BuildRequires:  perl(Moo.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Data/Dumper.pm)
Requires:       perl(File/Path.pm)
Source44: import.info

%description
This module is a drop-in replacement for Module::Install. It does everything
Module::Install does, but just a bit better.

%prep
%setup -q -n Module-Package-%{version}
%patch0 -p1
# XXX: Do not unbundle ./inc/ because of bootstrap

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2_21
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2_17
- update to new release by fcimport

* Fri Apr 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2_16
- to Sisyphus as perl-Dancer2 dep

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_16
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_15
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_14
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_12
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_11
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_10
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_9
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_3
- update to new release by fcimport

* Sat May 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_1
- fc import

