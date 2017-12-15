# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Clone.pm) perl(JSON.pm) perl(Module/Build.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Data-Clone
Version:        0.004
Release:        alt1_11.1
Summary:        Polymorphic data cloning
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Data-Clone/
Source0:        http://www.cpan.org/authors/id/G/GF/GFUJI/Data-Clone-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Devel/PPPort.pm)
BuildRequires:  perl(ExtUtils/ParseXS.pm)
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/AuthorTests.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/LeakTrace.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Requires.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(Tie/Array.pm)
BuildRequires:  perl(Tie/Hash.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(XSLoader.pm)
Requires:       perl(Exporter.pm)


Source44: import.info

%description
Data::Clone does data cloning, i.e. copies things recursively. This is
smart so that it works with not only non-blessed references, but also
with blessed references (i.e. objects). When clone() finds an object, it
calls a clone method of the object if the object has a clone, otherwise
it makes a surface copy of the object. That is, this module does
polymorphic data cloning.

%prep
%setup -q -n Data-Clone-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Data*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_11.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_11
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_8
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_7.1
- rebuild with new perl 5.24.1

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_6
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_5.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_5
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_3.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_2
- update to new release by fcimport

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_7
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.003-alt2_7
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_6
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_5
- update to new release by fcimport

* Thu Dec 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_4
- initial release

