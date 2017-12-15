# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Cwd.pm) perl(Encode.pm) perl(Exporter.pm) perl(File/Spec.pm) perl(MIME/Base64.pm) perl(XSLoader.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Crypt-Eksblowfish
Version:        0.009
Release:        alt5_19.1
Summary:        Eksblowfish block cipher
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Crypt-Eksblowfish/
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Crypt-Eksblowfish-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Class/Mix.pm)
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)


Source44: import.info
Patch33: Crypt-Eksblowfish-0.009-2y.patch

%description
An object of this type encapsulates a keyed instance of the Eksblowfish
block cipher, ready to encrypt and decrypt.

%prep
%setup -q -n Crypt-Eksblowfish-%{version}
%patch33 -p1

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Crypt*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt5_19.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt5_19
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt5_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt5_16
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt5_15.1
- rebuild with new perl 5.24.1

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt5_15
- support of the newer $2y$ prefix by Valery Inozemtsev
  see https://rt.cpan.org/Public/Bug/Display.html?id=93688

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_15
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_14
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_13.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_13
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_11.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_9
- update to new release by fcimport

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt4_8
- moved to Sisyphus as dependency

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.009-alt3_8
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_7
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_6
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.009-alt2_5
- rebuild with new perl

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_5
- update to new release by fcimport

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_3
- fc import

