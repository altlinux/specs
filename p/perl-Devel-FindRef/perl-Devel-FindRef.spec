# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Scalar/Util.pm) perl(XSLoader.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
# fedora __isa_bits tmp hack
%ifarch x86_64
%define __isa_bits 64
%else
%define __isa_bits 32
%endif
Name:           perl-Devel-FindRef
Version:        1.42
Release:        alt4_20
Summary:        Where is that reference to my variable hiding?
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Devel-FindRef/
Source0:        http://www.cpan.org/authors/id/M/ML/MLEHMANN/Devel-FindRef-%{version}2.tar.gz
Patch0:         0001-Fix-compiler-warnings.patch
Patch1:         0001-Fix-64-bit-warnings.patch
Patch2:         Devel-FindRef-fix.patch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(common/sense.pm)
Source44: import.info

%description
Tracking down reference problems (e.g. you expect some object to be
destroyed, but there are still references to it that keep it alive) can be
very hard. Fortunately, perl keeps track of all its values, so tracking
references "backwards" is usually possible.

%prep
%setup -q -n Devel-FindRef-%{version}2
%patch0 -p1
%if %{__isa_bits} == 64
%patch1 -p1
%endif
%patch2 -p1


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING README
%{perl_vendor_archlib}/auto/Devel
%{perl_vendor_archlib}/Devel

%changelog
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

