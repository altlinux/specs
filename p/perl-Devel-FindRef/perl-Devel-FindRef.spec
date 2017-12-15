%define _unpackaged_files_terminate_build 1
Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Scalar/Util.pm) perl(XSLoader.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Devel-FindRef
Version:        1.45
Release:        alt1.1
Summary:        Where is that reference to my variable hiding?
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Devel-FindRef/
Source0:        http://www.cpan.org/authors/id/M/ML/MLEHMANN/Devel-FindRef-%{version}.tar.gz
# fixing format warnings
Patch0:         perl-Devel-FindRef-1.44-fix-format-warnings.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=786085
Patch2:         Devel-FindRef-fix.patch
BuildRequires:  perl(ExtUtils/MakeMaker.pm) perl(Canary/Stability.pm)
BuildRequires:  perl(common/sense.pm)
Source44: import.info

%description
Tracking down reference problems (e.g. you expect some object to be
destroyed, but there are still references to it that keep it alive) can be
very hard. Fortunately, perl keeps track of all its values, so tracking
references "backwards" is usually possible.

%prep
%setup -q -n Devel-FindRef-%{version}
%patch0 -p1
%patch2 -p1

%build
# remove me in proper upstream release
#[ %version = 1.44 ] || exit 3
%define _without_test 1
# end remove

yes | perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%check
make test

%files
%doc Changes COPYING README
%{perl_vendor_archlib}/auto/Devel
%{perl_vendor_archlib}/Devel

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.45-alt1.1
- rebuild with new perl 5.26.1

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.45-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt3_3.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt3_3.1
- rebuild with new perl 5.22.0

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt3_3
- quick hack for perl 5.22

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt2_3
- fixed build with new perl 5.22

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt1_3.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt1_1
- update to new release by fcimport

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.422-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.42-alt4_20
- Sisyphus build

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1.42-alt3_20
- rebuild to get rid of unmets

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_20
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_19
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1.42-alt2_18
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1_18
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1_16
- fc import

