Name: GeoIP-ASNum
Version: 20171120
Release: alt1
# OK, day designation in version string is unneeded, this file updates strictly
# monthly. We need to introduce Epoch in order to drop day from version
Epoch: 1

Packager: Alexey Shabalin <shaba@altlinux.ru>

Summary: GeoIPASNum database file
License: OPEN DATA LICENSE (see LICENSE.txt)
Group: System/Libraries

Url: http://www.maxmind.com/app/geolitecity
Source: http://geolite.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz
Source1: GeoIP-data-LICENSE.txt

BuildArch: noarch

Requires: libGeoIP > 1.4.2-alt1

# Need to do it explicitly...
Provides: /usr/share/GeoIP/GeoIPASNum.dat

%description
This package contain the maps IPv4 addresses to ASN, including the name of the ASN.

%prep
%setup -T -c

%build
cp %SOURCE1 ./LICENSE.txt

%install
install -d %buildroot%_datadir/GeoIP
gunzip -c %_sourcedir/GeoIPASNum.dat.gz >%buildroot%_datadir/GeoIP/GeoIPASNum.dat

%files
%doc LICENSE.txt
%dir %_datadir/GeoIP/
%_datadir/GeoIP/GeoIPASNum.dat

%changelog
* Mon Nov 20 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20171120-alt1
- repocop cronbuild 20171120. At your service.

* Tue Nov 14 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20171114-alt1
- repocop cronbuild 20171114. At your service.

* Sat Oct 14 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20171014-alt1
- repocop cronbuild 20171014. At your service.

* Sun Oct 08 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20171008-alt1
- repocop cronbuild 20171008. At your service.

* Sat Sep 23 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170923-alt1
- repocop cronbuild 20170923. At your service.

* Sun Sep 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170917-alt1
- repocop cronbuild 20170917. At your service.

* Mon Sep 11 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170911-alt1
- repocop cronbuild 20170911. At your service.

* Sat Sep 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170902-alt1
- repocop cronbuild 20170902. At your service.

* Sun Aug 27 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170827-alt1
- repocop cronbuild 20170827. At your service.

* Mon Aug 21 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170821-alt1
- repocop cronbuild 20170821. At your service.

* Sat Aug 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170812-alt1
- repocop cronbuild 20170812. At your service.

* Sun Aug 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170806-alt1
- repocop cronbuild 20170806. At your service.

* Mon Jul 31 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170731-alt1
- repocop cronbuild 20170731. At your service.

* Sat Jul 22 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170722-alt1
- repocop cronbuild 20170722. At your service.

* Sun Jul 16 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170716-alt1
- repocop cronbuild 20170716. At your service.

* Mon Jul 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170710-alt1
- repocop cronbuild 20170710. At your service.

* Sat Jul 01 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170701-alt1
- repocop cronbuild 20170701. At your service.

* Sun Jun 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170625-alt1
- repocop cronbuild 20170625. At your service.

* Mon Jun 19 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170619-alt1
- repocop cronbuild 20170619. At your service.

* Sat Jun 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170610-alt1
- repocop cronbuild 20170610. At your service.

* Sun Jun 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170604-alt1
- repocop cronbuild 20170604. At your service.

* Mon May 29 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170529-alt1
- repocop cronbuild 20170529. At your service.

* Sat May 20 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170520-alt1
- repocop cronbuild 20170520. At your service.

* Sun May 14 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170514-alt1
- repocop cronbuild 20170514. At your service.

* Mon May 08 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170508-alt1
- repocop cronbuild 20170508. At your service.

* Sat Apr 29 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170429-alt1
- repocop cronbuild 20170429. At your service.

* Sun Apr 23 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170423-alt1
- repocop cronbuild 20170423. At your service.

* Mon Apr 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170417-alt1
- repocop cronbuild 20170417. At your service.

* Sat Apr 08 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170408-alt1
- repocop cronbuild 20170408. At your service.

* Sun Apr 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170402-alt1
- repocop cronbuild 20170402. At your service.

* Mon Mar 27 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170327-alt1
- repocop cronbuild 20170327. At your service.

* Sat Mar 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170318-alt1
- repocop cronbuild 20170318. At your service.

* Sun Mar 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170312-alt1
- repocop cronbuild 20170312. At your service.

* Mon Mar 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170306-alt1
- repocop cronbuild 20170306. At your service.

* Sat Feb 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170204-alt1
- repocop cronbuild 20170204. At your service.

* Sun Jan 29 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170129-alt1
- repocop cronbuild 20170129. At your service.

* Mon Jan 23 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170123-alt1
- repocop cronbuild 20170123. At your service.

* Sat Jan 14 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170114-alt1
- repocop cronbuild 20170114. At your service.

* Sun Jan 08 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170108-alt1
- repocop cronbuild 20170108. At your service.

* Mon Jan 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170102-alt1
- repocop cronbuild 20170102. At your service.

* Sat Dec 24 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161224-alt1
- repocop cronbuild 20161224. At your service.

* Sun Dec 18 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161218-alt1
- repocop cronbuild 20161218. At your service.

* Mon Dec 12 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161212-alt1
- repocop cronbuild 20161212. At your service.

* Sat Dec 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161203-alt1
- repocop cronbuild 20161203. At your service.

* Sun Nov 27 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161127-alt1
- repocop cronbuild 20161127. At your service.

* Thu Nov 24 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161124-alt1
- repocop cronbuild 20161124. At your service.

* Mon Nov 21 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161121-alt1
- repocop cronbuild 20161121. At your service.

* Sun Nov 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161106-alt1
- repocop cronbuild 20161106. At your service.

* Mon Oct 31 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161031-alt1
- repocop cronbuild 20161031. At your service.

* Tue Oct 25 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161025-alt1
- repocop cronbuild 20161025. At your service.

* Wed Oct 19 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161019-alt1
- repocop cronbuild 20161019. At your service.

* Sun Oct 16 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161016-alt1
- repocop cronbuild 20161016. At your service.

* Thu Oct 13 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161013-alt1
- repocop cronbuild 20161013. At your service.

* Mon Oct 10 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161010-alt1
- repocop cronbuild 20161010. At your service.

* Tue Oct 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161004-alt1
- repocop cronbuild 20161004. At your service.

* Sun Sep 25 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160925-alt1
- repocop cronbuild 20160925. At your service.

* Tue Sep 13 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160913-alt1
- repocop cronbuild 20160913. At your service.

* Sun Sep 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160904-alt1
- repocop cronbuild 20160904. At your service.

* Mon Aug 29 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160829-alt1
- repocop cronbuild 20160829. At your service.

* Tue Aug 23 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160823-alt1
- repocop cronbuild 20160823. At your service.

* Wed Aug 17 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160817-alt1
- repocop cronbuild 20160817. At your service.

* Mon Aug 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160808-alt1
- repocop cronbuild 20160808. At your service.

* Tue Aug 02 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160802-alt1
- repocop cronbuild 20160802. At your service.

* Wed Jul 27 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160727-alt1
- repocop cronbuild 20160727. At your service.

* Mon Jul 18 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160718-alt1
- repocop cronbuild 20160718. At your service.

* Tue Jul 12 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160712-alt1
- repocop cronbuild 20160712. At your service.

* Sat Jul 09 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160709-alt1
- repocop cronbuild 20160709. At your service.

* Wed Jul 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160706-alt1
- repocop cronbuild 20160706. At your service.

* Thu Jun 30 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160630-alt1
- repocop cronbuild 20160630. At your service.

* Mon Jun 27 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160627-alt1
- repocop cronbuild 20160627. At your service.

* Tue Jun 21 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160621-alt1
- repocop cronbuild 20160621. At your service.

* Wed Jun 15 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160615-alt1
- repocop cronbuild 20160615. At your service.

* Thu Jun 09 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160609-alt1
- repocop cronbuild 20160609. At your service.

* Mon Jun 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160606-alt1
- repocop cronbuild 20160606. At your service.

* Tue May 31 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160531-alt1
- repocop cronbuild 20160531. At your service.

* Sat May 28 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160528-alt1
- repocop cronbuild 20160528. At your service.

* Tue May 10 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160510-alt1
- repocop cronbuild 20160510. At your service.

* Wed May 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160504-alt1
- repocop cronbuild 20160504. At your service.

* Mon Apr 25 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160425-alt1
- repocop cronbuild 20160425. At your service.

* Tue Apr 19 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160419-alt1
- repocop cronbuild 20160419. At your service.

* Wed Apr 13 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160413-alt1
- repocop cronbuild 20160413. At your service.

* Mon Apr 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160404-alt1
- repocop cronbuild 20160404. At your service.

* Tue Mar 29 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160329-alt1
- repocop cronbuild 20160329. At your service.

* Wed Mar 23 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160323-alt1
- repocop cronbuild 20160323. At your service.

* Mon Mar 14 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160314-alt1
- repocop cronbuild 20160314. At your service.

* Wed Mar 09 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160309-alt1
- repocop cronbuild 20160309. At your service.

* Mon Feb 29 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160229-alt1
- repocop cronbuild 20160229. At your service.

* Wed Feb 24 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160224-alt1
- repocop cronbuild 20160224. At your service.

* Mon Feb 15 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160215-alt1
- repocop cronbuild 20160215. At your service.

* Mon Feb 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160208-alt1
- repocop cronbuild 20160208. At your service.

* Wed Feb 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160203-alt1
- repocop cronbuild 20160203. At your service.

* Mon Jan 25 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160125-alt1
- repocop cronbuild 20160125. At your service.

* Mon Jan 18 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160118-alt1
- repocop cronbuild 20160118. At your service.

* Mon Jan 11 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160111-alt1
- repocop cronbuild 20160111. At your service.

* Mon Jan 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160104-alt1
- repocop cronbuild 20160104. At your service.

* Mon Dec 28 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151228-alt1
- repocop cronbuild 20151228. At your service.

* Tue Dec 22 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151222-alt1
- repocop cronbuild 20151222. At your service.

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151214-alt1
- repocop cronbuild 20151214. At your service.

* Tue Dec 08 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151208-alt1
- repocop cronbuild 20151208. At your service.

* Wed Dec 02 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151202-alt1
- repocop cronbuild 20151202. At your service.

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151123-alt1
- repocop cronbuild 20151123. At your service.

* Tue Nov 17 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151117-alt1
- repocop cronbuild 20151117. At your service.

* Fri Oct 30 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151030-alt1
- repocop cronbuild 20151030. At your service.

* Wed Oct 21 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151021-alt1
- repocop cronbuild 20151021. At your service.

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151012-alt1
- repocop cronbuild 20151012. At your service.

* Tue Oct 06 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151006-alt1
- repocop cronbuild 20151006. At your service.

* Wed Sep 30 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150930-alt1
- repocop cronbuild 20150930. At your service.

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150921-alt1
- repocop cronbuild 20150921. At your service.

* Tue Sep 15 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150915-alt1
- repocop cronbuild 20150915. At your service.

* Wed Sep 09 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150909-alt1
- repocop cronbuild 20150909. At your service.

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150831-alt1
- repocop cronbuild 20150831. At your service.

* Tue Aug 25 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150825-alt1
- repocop cronbuild 20150825. At your service.

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150823-alt1
- repocop cronbuild 20150823. At your service.

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150730-alt1
- repocop cronbuild 20150730. At your service.

* Mon Jun 15 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150615-alt1
- repocop cronbuild 20150615. At your service.

* Wed Jun 03 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150603-alt1
- repocop cronbuild 20150603. At your service.

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150522-alt1
- repocop cronbuild 20150522. At your service.

* Mon May 04 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150504-alt1
- repocop cronbuild 20150504. At your service.

* Tue Apr 21 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150421-alt1
- repocop cronbuild 20150421. At your service.

* Mon Apr 06 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150406-alt1
- repocop cronbuild 20150406. At your service.

* Thu Mar 19 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150319-alt1
- repocop cronbuild 20150319. At your service.

* Wed Mar 04 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150304-alt1
- repocop cronbuild 20150304. At your service.

* Wed Feb 11 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150211-alt1
- repocop cronbuild 20150211. At your service.

* Mon Feb 02 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150202-alt1
- repocop cronbuild 20150202. At your service.

* Tue Jan 27 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150127-alt1
- repocop cronbuild 20150127. At your service.

* Sat Jan 24 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150124-alt1
- repocop cronbuild 20150124. At your service.

* Tue Jan 06 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150106-alt1
- repocop cronbuild 20150106. At your service.

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141213-alt1
- repocop cronbuild 20141213. At your service.

* Mon Dec 01 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141201-alt1
- repocop cronbuild 20141201. At your service.

* Sun Nov 16 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141116-alt1
- repocop cronbuild 20141116. At your service.

* Mon Nov 10 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141110-alt1
- repocop cronbuild 20141110. At your service.

* Tue Nov 04 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141104-alt1
- repocop cronbuild 20141104. At your service.

* Thu Oct 23 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141023-alt1
- repocop cronbuild 20141023. At your service.

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141011-alt1
- repocop cronbuild 20141011. At your service.

* Wed Oct 08 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141008-alt1
- repocop cronbuild 20141008. At your service.

* Wed Sep 17 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140917-alt1
- repocop cronbuild 20140917. At your service.

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140911-alt1
- repocop cronbuild 20140911. At your service.

* Wed Jul 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140702-alt1
- repocop cronbuild 20140702. At your service.

* Mon Jun 23 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140623-alt1
- repocop cronbuild 20140623. At your service.

* Wed Jun 04 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140604-alt1
- repocop cronbuild 20140604. At your service.

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140523-alt1
- repocop cronbuild 20140523. At your service.

* Mon May 05 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140505-alt1
- repocop cronbuild 20140505. At your service.

* Mon Apr 14 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140414-alt1
- repocop cronbuild 20140414. At your service.

* Sat Apr 05 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140405-alt1
- repocop cronbuild 20140405. At your service.

* Wed Apr 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140402-alt1
- repocop cronbuild 20140402. At your service.

* Tue Mar 18 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140318-alt1
- repocop cronbuild 20140318. At your service.

* Thu Mar 06 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140306-alt1
- repocop cronbuild 20140306. At your service.

* Wed Feb 19 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140219-alt1
- repocop cronbuild 20140219. At your service.

* Mon Feb 03 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140203-alt1
- repocop cronbuild 20140203. At your service.

* Wed Jan 22 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140122-alt1
- repocop cronbuild 20140122. At your service.

* Wed Jan 15 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140115-alt1
- repocop cronbuild 20140115. At your service.

* Thu Jan 09 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140109-alt1
- repocop cronbuild 20140109. At your service.

* Thu Dec 19 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20131219-alt1
- repocop cronbuild 20131219. At your service.

* Wed Dec 04 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20131204-alt1
- repocop cronbuild 20131204. At your service.

* Tue Nov 19 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20131119-alt1
- repocop cronbuild 20131119. At your service.

* Thu Nov 07 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20131107-alt1
- repocop cronbuild 20131107. At your service.

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20131101-alt1
- repocop cronbuild 20131101. At your service.

* Sun Sep 29 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130929-alt1
- repocop cronbuild 20130929. At your service.

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130905-alt1
- repocop cronbuild 20130905. At your service.

* Wed Aug 21 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130821-alt1
- repocop cronbuild 20130821. At your service.

* Fri Aug 09 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130809-alt1
- repocop cronbuild 20130809. At your service.

* Thu Jul 25 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130725-alt1
- repocop cronbuild 20130725. At your service.

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130719-alt1
- repocop cronbuild 20130719. At your service.

* Thu Jul 04 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130704-alt1
- repocop cronbuild 20130704. At your service.

* Wed Jun 19 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130619-alt1
- repocop cronbuild 20130619. At your service.

* Thu Jun 13 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130613-alt1
- repocop cronbuild 20130613. At your service.

* Tue Jun 04 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130604-alt1
- repocop cronbuild 20130604. At your service.

* Thu May 23 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130523-alt1
- repocop cronbuild 20130523. At your service.

* Tue May 14 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130514-alt1
- repocop cronbuild 20130514. At your service.

* Wed May 08 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130508-alt1
- repocop cronbuild 20130508. At your service.

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130417-alt1
- repocop cronbuild 20130417. At your service.

* Tue Apr 09 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130409-alt1
- repocop cronbuild 20130409. At your service.

* Mon Apr 01 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201304-alt1
- repocop cronbuild 20130401. At your service.

* Fri Mar 08 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201303-alt1
- repocop cronbuild 20130308. At your service.

* Wed Feb 06 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201302-alt1
- repocop cronbuild 20130206. At your service.

* Fri Jan 04 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201301-alt1
- repocop cronbuild 20130104. At your service.

* Wed Dec 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201212-alt1
- repocop cronbuild 20121205. At your service.

* Fri Nov 02 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201211-alt1
- repocop cronbuild 20121102. At your service.

* Wed Oct 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201210-alt1
- repocop cronbuild 20121003. At your service.

* Thu Sep 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201209-alt1
- repocop cronbuild 20120906. At your service.

* Sat Aug 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201208-alt1
- repocop cronbuild 20120804. At your service.

* Mon Jul 02 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201207-alt1
- repocop cronbuild 20120702. At your service.

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201206-alt1
- repocop cronbuild 20120605. At your service.

* Thu May 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201205-alt1
- repocop cronbuild 20120503. At your service.

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201204-alt1
- repocop cronbuild 20120403. At your service.

* Sun Mar 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201203-alt1
- repocop cronbuild 20120304. At your service.

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201202-alt1
- repocop cronbuild 20120203. At your service.

* Wed Jan 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201201-alt1
- repocop cronbuild 20120104. At your service.

* Fri Dec 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201112-alt1
- repocop cronbuild 20111202. At your service.

* Wed Nov 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201111-alt1
- repocop cronbuild 20111102. At your service.

* Mon Oct 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201110-alt1
- repocop cronbuild 20111003. At your service.

* Fri Sep 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201109-alt1
- repocop cronbuild 20110902. At your service.

* Wed Aug 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201108-alt1
- repocop cronbuild 20110803. At your service.

* Fri Jul 01 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201107-alt1
- repocop cronbuild 20110701. At your service.

* Wed Jun 01 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201106-alt1
- repocop cronbuild 20110601. At your service.

* Mon May 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201105-alt1
- repocop cronbuild 20110502. At your service.

* Sat Apr 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201104-alt1
- repocop cronbuild 20110402. At your service.

* Thu Mar 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201103-alt1
- repocop cronbuild 20110303. At your service.

* Fri Feb 04 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201102-alt1
- repocop cronbuild 20110204. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201101-alt1
- repocop cronbuild 20110114. At your service.

* Thu Nov 04 2010 Cronbuild Service <cronbuild@altlinux.org> 1:201011-alt1
- repocop cronbuild 20101104. At your service.

* Tue Oct 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1:201010-alt1
- repocop cronbuild 20101005. At your service.

* Thu Sep 16 2010 Cronbuild Service <cronbuild@altlinux.org> 1:201009-alt2
- repocop cronbuild 20100916. At your service.

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1:201003-alt2
- do not mark file in /usr as config

* Thu Mar 04 2010 Alexey Shabalin <shaba@altlinux.ru> 1:201003-alt1
- March 2010 update.
- Initial build.
