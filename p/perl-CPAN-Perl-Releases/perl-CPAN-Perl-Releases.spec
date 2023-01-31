%define _unpackaged_files_terminate_build 1
Name: perl-CPAN-Perl-Releases
Version: 5.20230120
Release: alt1

Summary: Mapping Perl releases on CPAN to the location of the tarballs
Group: Development/Perl
License: perl

Url: %CPAN CPAN-Perl-Releases
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CPAN/Perl/Releases*
%doc Changes README

%changelog
* Tue Jan 31 2023 Igor Vlasenko <viy@altlinux.org> 5.20230120-alt1
- new version

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 5.20221220-alt1
- new version

* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 5.20221120-alt1
- new version

* Sat Oct 22 2022 Igor Vlasenko <viy@altlinux.org> 5.20221020-alt1
- new version

* Tue Sep 27 2022 Igor Vlasenko <viy@altlinux.org> 5.20220922-alt1
- new version

* Wed Sep 21 2022 Igor Vlasenko <viy@altlinux.org> 5.20220920-alt1
- new version

* Mon Aug 22 2022 Igor Vlasenko <viy@altlinux.org> 5.20220820-alt1
- new version

* Mon Jul 25 2022 Igor Vlasenko <viy@altlinux.org> 5.20220720-alt1
- new version

* Wed Jun 22 2022 Igor Vlasenko <viy@altlinux.org> 5.20220620-alt1
- new version

* Sat May 28 2022 Igor Vlasenko <viy@altlinux.org> 5.20220528-alt1
- new version

* Tue May 24 2022 Igor Vlasenko <viy@altlinux.org> 5.20220523-alt1
- new version

* Sat May 21 2022 Igor Vlasenko <viy@altlinux.org> 5.20220520-alt1
- new version

* Fri Apr 22 2022 Igor Vlasenko <viy@altlinux.org> 5.20220420-alt1
- new version

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 5.20220320-alt1
- new version

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 5.20220220-alt1
- new version

* Thu Jan 27 2022 Igor Vlasenko <viy@altlinux.org> 5.20220120-alt1
- new version

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 5.20211220-alt1
- new version

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 5.20211120-alt1
- new version

* Sun Oct 24 2021 Igor Vlasenko <viy@altlinux.org> 5.20211020-alt1
- new version

* Fri Sep 24 2021 Igor Vlasenko <viy@altlinux.org> 5.20210920-alt1
- new version

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.org> 5.20210821-alt1
- new version

* Sat Jul 24 2021 Igor Vlasenko <viy@altlinux.org> 5.20210722-alt1
- new version

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 5.20210620-alt1
- new version

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 5.20210521-alt1
- new version

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 5.20210515-alt1
- new version

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 5.20210420-alt1
- new version

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 5.20210320-alt1
- new version

* Sun Feb 21 2021 Igor Vlasenko <viy@altlinux.org> 5.20210220-alt1
- new version

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 5.20210123-alt1
- new version

* Thu Jan 21 2021 Igor Vlasenko <viy@altlinux.ru> 5.20210120-alt1
- new version

* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 5.20210109-alt1
- new version

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 5.20201220-alt1
- new version

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 5.20201120-alt1
- new version

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 5.20201020-alt1
- new version

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200920-alt1
- new version

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200820-alt1
- new version

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200620-alt1
- new version

* Wed Jun 10 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200607-alt1
- new version

* Sat Jun 06 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200601-alt1
- new version

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200320-alt1
- new version

* Sat Mar 14 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200229-alt1
- new version

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200220-alt1
- new version

* Sat Jan 25 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200120-alt1
- new version

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 5.20191220-alt1
- new version

* Wed Nov 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.22-alt1
- new version

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 4.20-alt1
- new version

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 4.18-alt1
- new version

* Tue Sep 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.14-alt1
- new version

* Thu Aug 22 2019 Igor Vlasenko <viy@altlinux.ru> 4.12-alt1
- new version

* Mon Jul 22 2019 Igor Vlasenko <viy@altlinux.ru> 4.10-alt1
- new version

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.08-alt1
- new version

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 4.06-alt1
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.04-alt1
- new version

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 4.02-alt1
- new version

* Mon Apr 22 2019 Igor Vlasenko <viy@altlinux.ru> 3.98-alt1
- new version

* Sat Apr 06 2019 Igor Vlasenko <viy@altlinux.ru> 3.94-alt1
- new version

* Thu Mar 21 2019 Igor Vlasenko <viy@altlinux.ru> 3.92-alt1
- new version

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 3.90-alt1
- new version

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 3.88-alt1
- automated CPAN update

* Sat Dec 22 2018 Igor Vlasenko <viy@altlinux.ru> 3.86-alt1
- automated CPAN update

* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 3.84-alt1
- automated CPAN update

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 3.80-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 3.78-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 3.76-alt1
- automated CPAN update

* Mon Jul 02 2018 Igor Vlasenko <viy@altlinux.ru> 3.68-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 3.66-alt1
- automated CPAN update

* Wed Jun 20 2018 Igor Vlasenko <viy@altlinux.ru> 3.64-alt1
- automated CPAN update

* Wed Jun 13 2018 Igor Vlasenko <viy@altlinux.ru> 3.60-alt1
- automated CPAN update

* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 3.58-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.56-alt1
- automated CPAN update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.54-alt1
- automated CPAN update

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 3.52-alt1
- automated CPAN update

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 3.50-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 3.48-alt1
- automated CPAN update

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 3.42-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.38-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 3.14-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.08-alt1
- automated CPAN update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.06-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.00-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.98-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.94-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.88-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.78-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.60-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.58-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.48-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.42-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.38-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.76-alt1
- automated CPAN update

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt1
- 0.72 -> 1.42

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt1
- initial build for ALTLinux

