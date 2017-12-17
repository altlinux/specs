# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl-Filter
Name:           perl-YAML-LibYAML
Version:        0.71
Release:        alt1_1.1.1.1
Summary:        Perl YAML Serialization using XS and libyaml
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/YAML-LibYAML/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RU/RURBAN/YAML-LibYAML-%{version}.tar.gz

# Build
BuildRequires:  coreutils
BuildRequires:  findutils
%ifnarch e2k
BuildRequires:  gcc-common
%endif
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  libyaml2, libyaml-devel

# Module
BuildRequires:  perl(B/Deparse.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XSLoader.pm)

%if_without check
%else
# Tests
BuildRequires:  perl(blib.pm)
BuildRequires:  perl(Devel/Peek.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IO/Pipe.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Base.pm)
BuildRequires:  perl(Test/Base/Filter.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Tie/Array.pm)
BuildRequires:  perl(Tie/Hash.pm)
BuildRequires:  perl(utf8.pm)

# Optional Tests
BuildRequires:  perl(Path/Class.pm)
%endif

# Dependencies

# Avoid provides for perl shared objects

Source44: import.info

%description
Kirill Siminov's "libyaml" is arguably the best YAML implementation. The C
library is written precisely to the YAML 1.1 specification. It was originally
bound to Python and was later bound to Ruby.

%prep
%setup -q -n YAML-LibYAML-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendor_archlib}/auto/YAML/
%{perl_vendor_archlib}/YAML/

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1_1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1_1.1.1
- rebuild with new perl 5.24.1

* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 0.71-alt1_1.1
- E2K: drop gcc-common
- BOOTSTRAP: avoid test BRs when --without check

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1_1
- update to new release by fcimport

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 0.41-alt2
- built for perl 5.18

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1_2
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1_1
- update to new release by fcimport

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_1
- update to new release by fcimport

* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt3_4
- Sisyphus release

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.38-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_4
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_2
- fc import

