Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Fatal.pm) perl(Text/Balanced.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-autovivification
Version:        0.18
Release:        alt1_1
Summary:        Lexically disable autovivification
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/autovivification/
Source0:        http://search.cpan.org/CPAN/authors/id/V/VP/VPIT/autovivification-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Runtime
BuildRequires:  perl(XSLoader.pm)
# Tests only
# Scalar::Util is preferred over B
# XXX: BuildRequires:  perl(B)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(threads/shared.pm)
BuildRequires:  perl(Time/HiRes.pm)
# Runtime dependencies
Requires:       perl(XSLoader.pm)


Source44: import.info

%description
When an undefined variable is dereferenced, it gets silently upgraded to an
array or hash reference (depending of the type of the dereferencing). This
behavior is called autovivification and usually does what you mean (e.g.
when you store a value) but it's sometimes unnatural or surprising because
your variables gets populated behind your back. This is especially true
when several levels of dereferencing are involved, in which case all levels
are vivified up to the last, or when it happens in intuitively read-only
constructs like exists.

%prep
%setup -q -n autovivification-%{version}

%build
perl Makefile.PL \
  INSTALLDIRS=vendor \
  OPTIMIZE="%{optflags}"  \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1
%make_build

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/autovivification.pm
%{perl_vendor_archlib}/auto/autovivification/

%changelog
* Sun Jan 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_1
- to Sisyphus as biber dependency

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2_1
- rebuild with perl 5.26

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_1
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3_6
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3_5
- update to new release by fcimport

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.16-alt3_4
- rebuild to get rid of unmets

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_4
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_2
- update to new release by fcimport

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 0.16-alt2_1
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.11-alt3_6
- rebuild to get rid of unmets

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_6
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_5
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_4
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.11-alt2_3
- rebuild to get rid of unmets

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.10-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- fc import

