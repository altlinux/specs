%define inversion 2
%define pyversion 3.7
%define reldate 20180108

Name: python-sphinx-objects.inv
Version: %inversion.%pyversion.%reldate
Release: alt1
Serial: 1
Summary: Sphinx inventory version %inversion
License: BSD
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>
Url: https://docs.python.org/dev/objects.inv
Source: %url
BuildArch: noarch

%description
This package contains periodically updated Sphinx inventory version %inversion
for Python %pyversion.

%install
mkdir -p %buildroot%_datadir/python-sphinx
install -pDm644 %SOURCE0 %buildroot%_datadir/python-sphinx/objects.inv

%files
%_datadir/python-sphinx/

%changelog
* Mon Jan 08 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180108-alt1
- repocop cronbuild 20180108. At your service.

* Sat Jan 06 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180106-alt1
- repocop cronbuild 20180106. At your service.

* Sat Dec 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171230-alt1
- repocop cronbuild 20171230. At your service.

* Sun Dec 24 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171223-alt1
- repocop cronbuild 20171224. At your service.

* Thu Dec 21 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171221-alt1
- repocop cronbuild 20171221. At your service.

* Tue Dec 19 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171219-alt1
- repocop cronbuild 20171219. At your service.

* Mon Dec 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171218-alt1
- repocop cronbuild 20171218. At your service.

* Sat Dec 16 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171216-alt1
- repocop cronbuild 20171216. At your service.

* Fri Dec 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171215-alt1
- repocop cronbuild 20171215. At your service.

* Fri Dec 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171214-alt1
- repocop cronbuild 20171215. At your service.

* Wed Dec 13 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171213-alt1
- repocop cronbuild 20171213. At your service.

* Tue Dec 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171211-alt1
- repocop cronbuild 20171212. At your service.

* Sat Dec 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171209-alt1
- repocop cronbuild 20171209. At your service.

* Thu Nov 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171130-alt1
- repocop cronbuild 20171130. At your service.

* Thu Nov 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171129-alt1
- repocop cronbuild 20171130. At your service.

* Mon Nov 27 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171125-alt1
- repocop cronbuild 20171127. At your service.

* Fri Nov 24 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171123-alt1
- repocop cronbuild 20171124. At your service.

* Wed Nov 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171115-alt1
- repocop cronbuild 20171115. At your service.

* Thu Nov 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171108-alt1
- repocop cronbuild 20171109. At your service.

* Tue Nov 07 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171107-alt1
- repocop cronbuild 20171107. At your service.

* Sat Nov 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171104-alt1
- repocop cronbuild 20171104. At your service.

* Fri Nov 03 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171102-alt1
- repocop cronbuild 20171103. At your service.

* Tue Oct 31 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171031-alt1
- repocop cronbuild 20171031. At your service.

* Wed Oct 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171024-alt1
- repocop cronbuild 20171025. At your service.

* Wed Oct 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171017-alt1
- repocop cronbuild 20171018. At your service.

* Tue Oct 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171016-alt1
- repocop cronbuild 20171017. At your service.

* Thu Oct 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171011-alt1
- repocop cronbuild 20171012. At your service.

* Tue Oct 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171009-alt1
- repocop cronbuild 20171010. At your service.

* Fri Oct 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171006-alt1
- repocop cronbuild 20171006. At your service.

* Wed Oct 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171004-alt1
- repocop cronbuild 20171004. At your service.

* Sat Sep 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170930-alt1
- repocop cronbuild 20170930. At your service.

* Sat Sep 16 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170915-alt1
- repocop cronbuild 20170916. At your service.

* Fri Sep 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170914-alt1
- repocop cronbuild 20170915. At your service.

* Sun Sep 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170910-alt1
- repocop cronbuild 20170910. At your service.

* Sat Sep 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170908-alt1
- repocop cronbuild 20170909. At your service.

* Thu Sep 07 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170907-alt1
- repocop cronbuild 20170907. At your service.

* Thu Sep 07 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170906-alt1
- repocop cronbuild 20170907. At your service.

* Wed Sep 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170905-alt1
- repocop cronbuild 20170906. At your service.

* Tue Sep 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170904-alt1
- repocop cronbuild 20170905. At your service.

* Tue Aug 29 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170828-alt1
- repocop cronbuild 20170829. At your service.

* Fri Aug 11 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170810-alt1
- repocop cronbuild 20170811. At your service.

* Thu Aug 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170809-alt1
- repocop cronbuild 20170810. At your service.

* Tue Aug 08 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170807-alt1
- repocop cronbuild 20170808. At your service.

* Wed Aug 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170802-alt1
- repocop cronbuild 20170802. At your service.

* Sun Jul 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170730-alt1
- repocop cronbuild 20170730. At your service.

* Tue Jul 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170718-alt1
- repocop cronbuild 20170718. At your service.

* Wed Jul 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170704-alt1
- repocop cronbuild 20170705. At your service.

* Sat Jun 24 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170624-alt1
- repocop cronbuild 20170624. At your service.

* Wed Jun 21 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170620-alt1
- repocop cronbuild 20170621. At your service.

* Mon Jun 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170611-alt1
- repocop cronbuild 20170612. At your service.

* Fri Jun 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170609-alt1
- repocop cronbuild 20170609. At your service.

* Tue Jun 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170606-alt1
- repocop cronbuild 20170606. At your service.

* Sat Jun 03 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170603-alt1
- repocop cronbuild 20170603. At your service.

* Sat Jun 03 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170602-alt1
- repocop cronbuild 20170603. At your service.

* Wed May 31 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170531-alt1
- repocop cronbuild 20170531. At your service.

* Sun May 28 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170527-alt1
- repocop cronbuild 20170528. At your service.

* Thu May 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170524-alt1
- repocop cronbuild 20170525. At your service.

* Sun May 21 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170520-alt1
- repocop cronbuild 20170521. At your service.

* Fri May 19 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170519-alt1
- repocop cronbuild 20170519. At your service.

* Wed May 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170516-alt1
- repocop cronbuild 20170517. At your service.

* Sat May 13 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170512-alt1
- repocop cronbuild 20170513. At your service.

* Tue May 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170508-alt1
- repocop cronbuild 20170509. At your service.

* Sat May 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170505-alt1
- repocop cronbuild 20170506. At your service.

* Tue May 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170501-alt1
- repocop cronbuild 20170502. At your service.

* Thu Apr 27 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170426-alt1
- repocop cronbuild 20170427. At your service.

* Tue Apr 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170425-alt1
- repocop cronbuild 20170425. At your service.

* Sun Apr 23 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170422-alt1
- repocop cronbuild 20170423. At your service.

* Sat Apr 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170415-alt1
- repocop cronbuild 20170415. At your service.

* Fri Apr 14 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170413-alt1
- repocop cronbuild 20170414. At your service.

* Sun Apr 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170408-alt1
- repocop cronbuild 20170409. At your service.

* Thu Apr 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170405-alt1
- repocop cronbuild 20170406. At your service.

* Wed Apr 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170404-alt1
- repocop cronbuild 20170405. At your service.

* Fri Mar 31 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170330-alt1
- repocop cronbuild 20170331. At your service.

* Thu Mar 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170329-alt1
- repocop cronbuild 20170330. At your service.

* Wed Mar 29 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170328-alt1
- repocop cronbuild 20170329. At your service.

* Sun Mar 26 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170325-alt1
- repocop cronbuild 20170326. At your service.

* Thu Mar 23 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170322-alt1
- repocop cronbuild 20170323. At your service.

* Sat Mar 11 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170310-alt1
- repocop cronbuild 20170311. At your service.

* Thu Mar 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170308-alt1
- repocop cronbuild 20170309. At your service.

* Sat Mar 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170303-alt1
- repocop cronbuild 20170304. At your service.

* Thu Mar 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170301-alt1
- repocop cronbuild 20170302. At your service.

* Sat Feb 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170224-alt1
- repocop cronbuild 20170225. At your service.

* Sun Feb 19 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170219-alt1
- repocop cronbuild 20170219. At your service.

* Fri Feb 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170216-alt1
- repocop cronbuild 20170217. At your service.

* Sat Feb 11 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170211-alt1
- repocop cronbuild 20170211. At your service.

* Sun Feb 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170205-alt1
- repocop cronbuild 20170205. At your service.

* Thu Feb 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170202-alt1
- repocop cronbuild 20170202. At your service.

* Thu Jan 26 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170125-alt1
- repocop cronbuild 20170126. At your service.

* Wed Jan 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170117-alt1
- repocop cronbuild 20170118. At your service.

* Tue Jan 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170116-alt1
- repocop cronbuild 20170117. At your service.

* Sat Jan 14 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170113-alt1
- repocop cronbuild 20170114. At your service.

* Thu Dec 29 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20161228-alt1
- repocop cronbuild 20161229. At your service.

* Wed Dec 28 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20161227-alt1
- repocop cronbuild 20161228. At your service.

* Sun Dec 25 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20161224-alt1
- repocop cronbuild 20161225. At your service.

* Sat Dec 24 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20161223-alt1
- repocop cronbuild 20161224. At your service.

* Fri Dec 16 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161216-alt1
- repocop cronbuild 20161216. At your service.

* Thu Dec 08 2016 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.6.20161208-alt1
- 20161206 -> 20161208.
- Serial -> Epoch.

* Tue Dec 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161205-alt1
- repocop cronbuild 20161206. At your service.

* Mon Dec 05 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161204-alt1
- repocop cronbuild 20161205. At your service.

* Sun Nov 27 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161126-alt1
- repocop cronbuild 20161127. At your service.

* Fri Nov 25 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161124-alt1
- repocop cronbuild 20161125. At your service.

* Tue Nov 22 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161122-alt1
- repocop cronbuild 20161122. At your service.

* Mon Nov 14 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161114-alt1
- repocop cronbuild 20161114. At your service.

* Sat Nov 12 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161112-alt1
- repocop cronbuild 20161112. At your service.

* Fri Nov 11 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161110-alt1
- repocop cronbuild 20161111. At your service.

* Tue Nov 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161107-alt1
- repocop cronbuild 20161108. At your service.

* Mon Nov 07 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161106-alt1
- repocop cronbuild 20161107. At your service.

* Fri Nov 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161104-alt1
- repocop cronbuild 20161104. At your service.

* Thu Nov 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161102-alt1
- repocop cronbuild 20161103. At your service.

* Tue Nov 01 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161101-alt1
- repocop cronbuild 20161101. At your service.

* Mon Oct 31 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161030-alt1
- repocop cronbuild 20161031. At your service.

* Wed Oct 26 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161026-alt1
- repocop cronbuild 20161026. At your service.

* Fri Oct 21 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161020-alt1
- repocop cronbuild 20161021. At your service.

* Thu Oct 20 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161019-alt1
- repocop cronbuild 20161020. At your service.

* Mon Oct 10 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161009-alt1
- repocop cronbuild 20161010. At your service.

* Wed Oct 05 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161004-alt1
- repocop cronbuild 20161005. At your service.

* Mon Oct 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161001-alt1
- repocop cronbuild 20161003. At your service.

* Sat Sep 17 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.7.20160916-alt1
- repocop cronbuild 20160917. At your service.

* Tue Sep 13 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.7.20160913-alt1
- repocop cronbuild 20160913. At your service.

* Mon Sep 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160912-alt1
- repocop cronbuild 20160912. At your service.

* Sun Sep 11 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160911-alt1
- repocop cronbuild 20160911. At your service.

* Sat Sep 10 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160910-alt1
- repocop cronbuild 20160910. At your service.

* Thu Sep 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160908-alt1
- repocop cronbuild 20160908. At your service.

* Wed Sep 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160907-alt1
- repocop cronbuild 20160907. At your service.

* Tue Sep 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160906-alt1
- repocop cronbuild 20160906. At your service.

* Fri Sep 02 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160902-alt1
- repocop cronbuild 20160902. At your service.

* Tue Aug 30 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160829-alt1
- repocop cronbuild 20160830. At your service.

* Sat Aug 27 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160827-alt1
- repocop cronbuild 20160827. At your service.

* Wed Aug 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160824-alt1
- repocop cronbuild 20160824. At your service.

* Sun Aug 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160820-alt1
- repocop cronbuild 20160821. At your service.

* Sat Aug 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160819-alt1
- repocop cronbuild 20160820. At your service.

* Wed Aug 17 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160816-alt1
- repocop cronbuild 20160817. At your service.

* Mon Aug 15 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160815-alt1
- repocop cronbuild 20160815. At your service.

* Tue Aug 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160808-alt1
- repocop cronbuild 20160809. At your service.

* Sat Aug 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160806-alt1
- repocop cronbuild 20160806. At your service.

* Sat Jul 30 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160730-alt1
- repocop cronbuild 20160730. At your service.

* Sat Jul 16 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160716-alt1
- repocop cronbuild 20160716. At your service.

* Wed Jul 13 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160712-alt1
- repocop cronbuild 20160713. At your service.

* Sat Jul 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160708-alt1
- repocop cronbuild 20160709. At your service.

* Mon Jul 04 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160703-alt1
- repocop cronbuild 20160704. At your service.

* Sat Jun 25 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160624-alt1
- repocop cronbuild 20160625. At your service.

* Thu Jun 23 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160622-alt1
- repocop cronbuild 20160623. At your service.

* Wed Jun 22 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160621-alt1
- repocop cronbuild 20160622. At your service.

* Sun Jun 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160618-alt1
- repocop cronbuild 20160619. At your service.

* Sat Jun 18 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160617-alt1
- repocop cronbuild 20160618. At your service.

* Wed Jun 15 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160614-alt1
- repocop cronbuild 20160615. At your service.

* Sun Jun 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160612-alt1
- repocop cronbuild 20160612. At your service.

* Fri Jun 10 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160610-alt1
- repocop cronbuild 20160610. At your service.

* Thu Jun 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160608-alt1
- repocop cronbuild 20160609. At your service.

* Mon Jun 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160605-alt1
- repocop cronbuild 20160606. At your service.

* Sat Jun 04 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160604-alt1
- repocop cronbuild 20160604. At your service.

* Fri Jun 03 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160603-alt1
- repocop cronbuild 20160603. At your service.

* Thu Jun 02 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160601-alt1
- repocop cronbuild 20160602. At your service.

* Sat May 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160527-alt1
- repocop cronbuild 20160528. At your service.

* Wed May 25 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160524-alt1
- repocop cronbuild 20160525. At your service.

* Fri May 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160519-alt1
- repocop cronbuild 20160520. At your service.

* Sun May 15 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160515-alt1
- repocop cronbuild 20160515. At your service.

* Wed May 11 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160510-alt1
- repocop cronbuild 20160511. At your service.

* Mon May 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160508-alt1
- repocop cronbuild 20160509. At your service.

* Sun May 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160507-alt1
- repocop cronbuild 20160508. At your service.

* Sat Apr 30 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160429-alt1
- repocop cronbuild 20160430. At your service.

* Sat Apr 23 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160423-alt1
- repocop cronbuild 20160423. At your service.

* Tue Apr 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160416-alt1
- repocop cronbuild 20160419. At your service.

* Wed Apr 13 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160413-alt1
- repocop cronbuild 20160413. At your service.

* Tue Apr 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160411-alt1
- repocop cronbuild 20160412. At your service.

* Sat Apr 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160408-alt1
- repocop cronbuild 20160409. At your service.

* Tue Apr 05 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160404-alt1
- repocop cronbuild 20160405. At your service.

* Sat Apr 02 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160402-alt1
- repocop cronbuild 20160402. At your service.

* Fri Apr 01 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160401-alt1
- repocop cronbuild 20160401. At your service.

* Mon Mar 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160327-alt1
- repocop cronbuild 20160328. At your service.

* Thu Mar 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160323-alt1
- repocop cronbuild 20160324. At your service.

* Tue Mar 22 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160322-alt1
- repocop cronbuild 20160322. At your service.

* Mon Mar 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160321-alt1
- repocop cronbuild 20160321. At your service.

* Sun Mar 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160319-alt1
- repocop cronbuild 20160320. At your service.

* Sat Mar 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160318-alt1
- repocop cronbuild 20160319. At your service.

* Mon Mar 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160314-alt1
- repocop cronbuild 20160314. At your service.

* Sat Mar 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160311-alt1
- repocop cronbuild 20160312. At your service.

* Tue Mar 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160307-alt1
- repocop cronbuild 20160308. At your service.

* Fri Feb 26 2016 Dmitry V. Levin <ldv@altlinux.org> 2.3.6.20160226-alt1
- Initial revision.
