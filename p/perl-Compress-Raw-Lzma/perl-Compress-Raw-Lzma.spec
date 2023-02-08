%define _unpackaged_files_terminate_build 1
%define real_name Compress-Raw-Lzma

Name: perl-%real_name
Version: 2.204
Release: alt1
Summary: Low-level interface to lzma compression library
License: %perl_license
Group: Development/Perl
Url: https://metacpan.org/release/%real_name
Source0: https://cpan.metacpan.org/modules/by-module/Compress/%real_name-%version.tar.gz

BuildRequires(pre): rpm-build-licenses
# Module Build
BuildRequires: gcc
BuildRequires: perl-devel
BuildRequires: rpm-build-perl
BuildRequires: liblzma-devel
# Runtime
Requires: perl(XSLoader.pm)

%description
This module provides a Perl interface to the lzma compression library.
It is used by IO::Compress::Lzma.

%prep
%setup -n %real_name-%version

# Remove bundled test modules
rm -rv t/Test/
perl -i -ne 'print $_ unless m{^t/Test/}' MANIFEST

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/auto/Compress/
%perl_vendor_archlib/Compress/

%changelog
* Thu Feb 09 2023 Igor Vlasenko <viy@altlinux.org> 2.204-alt1
- new version

* Mon Jun 27 2022 Igor Vlasenko <viy@altlinux.org> 2.201-alt1
- new version

* Thu Apr 07 2022 Igor Vlasenko <viy@altlinux.org> 2.103-alt1
- new version

* Fri Nov 26 2021 L.A. Kostis <lakostis@altlinux.ru> 2.101-alt3
- Rebuild by human.
- Remove fcimport crap.

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 2.101-alt2_3
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 2.101-alt2_2
- update to new release by fcimport

* Wed Jun 16 2021 Cronbuild Service <cronbuild@altlinux.org> 2.101-alt2_1
- rebuild to get rid of unmets

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 2.101-alt1_1
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 2.100-alt2_1
- update to new release by fcimport

* Wed Jan 13 2021 Igor Vlasenko <viy@altlinux.ru> 2.100-alt1_1
- update to new release by fcimport

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 2.096-alt2_1
- rebuild with perl 5.30

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 2.096-alt1_1
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 2.093-alt1_5
- update to new release by fcimport

* Tue Apr 07 2020 Igor Vlasenko <viy@altlinux.ru> 2.093-alt1_4
- update to new release by fcimport

* Thu Feb 27 2020 Igor Vlasenko <viy@altlinux.ru> 2.093-alt1_3
- update to new release by fcimport

* Thu Dec 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.093-alt1_1
- update to new release by fcimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 2.090-alt1_1
- update to new release by fcimport

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 2.087-alt1_1
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 2.086-alt1_3
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.086-alt1_2
- update to new release by fcimport

* Thu Apr 11 2019 Igor Vlasenko <viy@altlinux.ru> 2.086-alt1_1
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 2.085-alt3_2
- update to new release by fcimport

* Tue Jan 29 2019 Cronbuild Service <cronbuild@altlinux.org> 2.085-alt3_1
- rebuild to get rid of unmets

* Tue Jan 29 2019 Cronbuild Service <cronbuild@altlinux.org> 2.085-alt2_1
- rebuild to get rid of unmets

* Fri Jan 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.085-alt1_1
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.082-alt1_4
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.082-alt1_3
- update to new release by fcimport

* Sun May 20 2018 Igor Vlasenko <viy@altlinux.ru> 2.082-alt1_2
- update to new release by fcimport

* Fri May 04 2018 Igor Vlasenko <viy@altlinux.ru> 2.082-alt1_1
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 2.074-alt2_5
- update to new release by fcimport

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.074-alt2_4
- rebuild with perl 5.26

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.074-alt1_4
- update to new release by fcimport

* Fri Sep 29 2017 Cronbuild Service <cronbuild@altlinux.org> 2.069-alt4_2
- rebuild to get rid of unmets

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 2.069-alt3_2
- rebuild to get rid of unmets

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.069-alt2_2
- rebuild to get rid of unmets

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.069-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 2.068-alt1_5
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 2.068-alt1_3
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.067-alt1_1
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.066-alt2_1
- rebuild to get rid of unmets

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.066-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.064-alt1_4
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.064-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.064-alt1_2
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.064-alt1_1
- update to new release by fcimport

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.063-alt1_1
- update to new release by fcimport

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 2.062-alt3_1
- rebuild with new liblzma

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.062-alt2_1
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.062-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.061-alt1_2
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 2.061-alt1_1
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.060-alt1_2
- update to new release by fcimport

* Mon Jan 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.060-alt1_1
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.059-alt1_1
- update to new release by fcimport

* Thu Nov 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.058-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.055-alt2_1
- rebuild with new perl

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.055-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 2.052-alt1_5
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.052-alt1_1
- fc import

