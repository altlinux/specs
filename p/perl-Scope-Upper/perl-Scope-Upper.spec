%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Sub/Uplevel.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Scope-Upper
Summary:        Act on upper scopes
Version:        0.30
Release:        alt1.1.1
License:        GPL+ or Artistic
Source0:        http://www.cpan.org/authors/id/V/VP/VPIT/Scope-Upper-%{version}.tar.gz
URL:            http://search.cpan.org/dist/Scope-Upper
# Build
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(XSLoader.pm)
# Tests only
BuildRequires:  perl(feature.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(POSIX.pm)
# It's either Scalar::Util or B; with the former being preferred
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(threads/shared.pm)
# Optional tests only
BuildRequires:  perl(Time/HiRes.pm)
Requires:       perl(Exporter.pm)
Requires:       perl(XSLoader.pm)


Source44: import.info

%description
This module lets you defer actions that will take place when the control
flow returns into an upper scope. Currently, you can hook an upper scope
end, or localize variables, array/hash values or deletions of elements
in higher contexts. You can also return to an upper level and know which
context was in use then.

%prep
%setup -q -n Scope-Upper-%{version}
sed -i -e '1s,^#!.*perl,%(perl -MConfig -e 'print $Config{startperl}'),' \
    samples/*

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes samples
%{perl_vendor_archlib}/*
%exclude %dir %{perl_vendor_archlib}/auto

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1.1
- automated CPAN update

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt2_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt2_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt2_2
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt2_1.1
- rebuild with new perl 5.24.1

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt2_1
- to Sisyphus

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_1
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2_2
- update to new release by fcimport

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 0.28-alt2_1
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_1
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1_1
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.24-alt2_3
- rebuild to get rid of unmets

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_3
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2_4
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.22-alt2_3
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_2
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_2
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.18-alt2_3
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_3
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_1
- fc import

