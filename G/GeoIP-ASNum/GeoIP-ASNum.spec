Name: GeoIP-ASNum
Version: 20160118
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
