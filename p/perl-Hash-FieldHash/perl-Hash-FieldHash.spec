%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Hash/Util/FieldHash/Compat.pm) perl(Mouse.pm) perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-Hash-FieldHash
Version:        0.15
Release:        alt1
Summary:        Lightweight field hash implementation
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Hash-FieldHash/
Source0:        http://www.cpan.org/authors/id/G/GF/GFUJI/Hash-FieldHash-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(CPAN/Meta.pm)
BuildRequires:  perl(CPAN/Meta/Prereqs.pm)
BuildRequires:  perl(Devel/PPPort.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/ParseXS.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Symbol.pm)
BuildRequires:  perl(Test/LeakTrace.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Synopsis.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XSLoader.pm)

# Avoid provides from private shared objects

Source44: import.info

%description
Hash::FieldHash provides the field hash mechanism, which supports the inside-
out technique.

%prep
%setup -q -n Hash-FieldHash-%{version}

%build
RELEASE_TESTING=1 perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
./Build test

%files
%doc LICENSE Changes README.md example
%if 0%{?_licensedir:1}
%doc LICENSE
%else
%doc LICENSE
%endif
%doc Changes README.md benchmark/ example/
%{perl_vendor_archlib}/auto/Hash/
%{perl_vendor_archlib}/Hash/

%changelog
* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1_5.1
- rebuild with new perl 5.24.1

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1_4
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1_3.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1_1
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.1
- rebuild with new perl 5.20.1

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- uploaded to Sisyphus as Scalar-Does deep dependency

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- update

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.12-alt3_7
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_6
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_5
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.12-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_4
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_2
- fc import

