%define _unpackaged_files_terminate_build 1
%define dist Module-CoreList
Name: perl-%dist
Version: 5.20221220
Release: alt1

Summary: What modules shipped with versions of perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/B/BI/BINGOS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011 (-bi)
BuildRequires: perl-Pod-Parser perl-Test-Pod

%description
Module::CoreList provides information on which core and dual-life modules
shipped with each version of perl.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/corelist
%_man1dir/corelist*
%perl_vendor_privlib/Module

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 5.20221220-alt1
- automated CPAN update

* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 5.20221120-alt1
- automated CPAN update

* Sat Oct 22 2022 Igor Vlasenko <viy@altlinux.org> 5.20221020-alt1
- automated CPAN update

* Wed Sep 21 2022 Igor Vlasenko <viy@altlinux.org> 5.20220920-alt1
- automated CPAN update

* Mon Aug 22 2022 Igor Vlasenko <viy@altlinux.org> 5.20220820-alt1
- automated CPAN update

* Mon Jul 25 2022 Igor Vlasenko <viy@altlinux.org> 5.20220720-alt1
- automated CPAN update

* Wed Jun 22 2022 Igor Vlasenko <viy@altlinux.org> 5.20220620-alt1
- automated CPAN update

* Sat May 28 2022 Igor Vlasenko <viy@altlinux.org> 5.20220527-alt1
- automated CPAN update

* Fri Apr 22 2022 Igor Vlasenko <viy@altlinux.org> 5.20220420-alt1
- automated CPAN update

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 5.20220320-alt1
- automated CPAN update

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 5.20220220-alt1
- automated CPAN update

* Thu Jan 27 2022 Igor Vlasenko <viy@altlinux.org> 5.20220120-alt1
- automated CPAN update

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 5.20211220-alt1
- automated CPAN update

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 5.20211120-alt1
- automated CPAN update

* Sun Oct 24 2021 Igor Vlasenko <viy@altlinux.org> 5.20211020-alt1
- automated CPAN update

* Fri Sep 24 2021 Igor Vlasenko <viy@altlinux.org> 5.20210920-alt1
- automated CPAN update

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.org> 5.20210820-alt1
- automated CPAN update

* Sat Jul 24 2021 Igor Vlasenko <viy@altlinux.org> 5.20210723-alt1
- automated CPAN update

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 5.20210620-alt1
- automated CPAN update

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 5.20210521-alt1
- automated CPAN update

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 5.20210420-alt1
- automated CPAN update

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 5.20210320-alt1
- automated CPAN update

* Sun Feb 21 2021 Igor Vlasenko <viy@altlinux.org> 5.20210220-alt1
- automated CPAN update

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 5.20210123-alt1
- automated CPAN update

* Thu Jan 21 2021 Igor Vlasenko <viy@altlinux.ru> 5.20210120-alt1
- automated CPAN update

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 5.20201220-alt1
- automated CPAN update

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 5.20201120-alt1
- automated CPAN update

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 5.20201020-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200920-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200820-alt1
- automated CPAN update

* Thu Jul 23 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200717-alt1
- automated CPAN update

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200620-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200603-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200602-alt1
- automated CPAN update

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200320-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200220-alt1
- automated CPAN update

* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 5.20200120-alt1
- automated CPAN update

* Wed Dec 25 2019 Igor Vlasenko <viy@altlinux.ru> 5.20191220-alt1
- automated CPAN update

* Wed Nov 27 2019 Igor Vlasenko <viy@altlinux.ru> 5.20191120-alt1
- automated CPAN update

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 5.20191110-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 5.20191020-alt1
- automated CPAN update

* Sat Sep 21 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190920-alt1
- automated CPAN update

* Thu Aug 22 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190820-alt1
- automated CPAN update

* Wed Jul 31 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190720-alt1
- automated CPAN update

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190620-alt1
- automated CPAN update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190524-alt1
- automated CPAN update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190522-alt1
- automated CPAN update

* Tue Apr 23 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190420-alt1
- automated CPAN update

* Thu Mar 21 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190320-alt1
- automated CPAN update

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190220-alt1
- automated CPAN update

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 5.20190120-alt1
- automated CPAN update

* Fri Dec 21 2018 Igor Vlasenko <viy@altlinux.ru> 5.20181218-alt1
- automated CPAN update

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 5.20181130-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 5.20181020-alt1
- automated CPAN update

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180920-alt1
- automated CPAN update

* Tue Aug 21 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180820-alt1
- automated CPAN update

* Wed Jul 25 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180720-alt1
- automated CPAN update

* Thu Jun 28 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180626-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180622-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180420-alt1
- automated CPAN update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180414-alt1
- automated CPAN update

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180221-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180220-alt1
- automated CPAN update

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 5.20180120-alt1
- automated CPAN update

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 5.20171220-alt1
- automated CPAN update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 5.20171120-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 5.20171020-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 5.20170923-alt1
- automated CPAN update

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 5.20170821-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 5.20170720-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.20170420-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 5.20170320-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 5.20170220-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 5.20170120-alt1
- automated CPAN update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 5.20170115-alt1
- automated CPAN update

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 5.20161220-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 5.20161120-alt1
- automated CPAN update

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 5.20161020-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160920-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160820-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160720-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160620-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160520-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160429-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160320-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160121-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.20160120-alt1
- automated CPAN update

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 5.20151220-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 5.20151213-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 5.20151120-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 5.20151020-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 5.20150920-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 5.20150420-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 5.20150320-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 5.20150120-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 5.20141220-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 5.20141120-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 5.20141020-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 5.20141002-alt1
- automated CPAN update

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 5.20140914-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 5.021003-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 5.021002-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 5.021001-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 3.11-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 3.10-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 3.09-alt1
- automated CPAN update

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 3.07-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 3.04-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.03-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.02-alt1
- automated CPAN update

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 3.01-alt1
- automated CPAN update

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.00-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 2.99-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.97-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.94-alt1
- automated CPAN update

* Sun Apr 21 2013 Igor Vlasenko <viy@altlinux.ru> 2.87-alt1
- update (closes: 28877)

* Tue Nov 06 2012 Vladimir Lettiev <crux@altlinux.ru> 2.76-alt1
- 2.75 -> 2.76

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 2.75-alt1
- automated CPAN update

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.74-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.73-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 2.72-alt1
- 2.57 -> 2.72

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 2.57-alt1
- 2.56 -> 2.57

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 2.56-alt1
- automated CPAN update

* Tue Sep 06 2011 Vitaly Lipatov <lav@altlinux.ru> 2.55-alt1
- new version 2.55 (with rpmrb script)
- update buildreqs

* Sun Jan 30 2011 Vitaly Lipatov <lav@altlinux.ru> 2.44-alt1
- new version 2.44 (with rpmrb script)

* Tue Dec 14 2010 Vitaly Lipatov <lav@altlinux.ru> 2.41-alt1
- new version 2.41 (with rpmrb script)

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.35-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt2
- fix directory ownership violation

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- new version 2.12 (with rpmrb script)

* Sat Jul 30 2005 Vitaly Lipatov <lav@altlinux.ru> 2.02-alt2
- fix bug #7499 (fix unexpanded macros)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 2.02-alt1
- first build for ALT Linux Sisyphus
