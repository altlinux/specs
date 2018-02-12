Name: GeoIP-Lite-City
Version: 201802.12
Release: alt1
# OK, day designation in version string is unneeded, this file updates strictly
# monthly. We need to introduce Epoch in order to drop day from version
Epoch: 1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: GeoLite City database file
License: OPEN DATA LICENSE (see LICENSE.txt)
Group: System/Libraries

Url: http://www.maxmind.com/app/geolitecity
Source: http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
Source1: GeoIP-data-LICENSE.txt

BuildArch: noarch

Requires: libGeoIP > 1.4.2-alt1

# Need to do it explicitly...
Provides: /usr/share/GeoIP/GeoLiteCity.dat

%description
This package contain the free edition city database for GeoIP.

%prep
%setup -T -c

%build
cp %SOURCE1 ./LICENSE.txt

%install
install -d %buildroot%_datadir/GeoIP
gunzip -c %_sourcedir/GeoLiteCity.dat.gz >%buildroot%_datadir/GeoIP/GeoLiteCity.dat

%files
%doc LICENSE.txt
%dir %_datadir/GeoIP/
%config(noreplace) %_datadir/GeoIP/GeoLiteCity.dat

# Why mark DB as config(noreplace)? User can update GeoLiteCity.dat directly
# fetching file from MaxMind site via monthly cron job. In such case
# this package may actually overwrite freshly downloaded DB with older
# version. We mark file norepace in order to prevent rpm from doing this.

%changelog
* Mon Feb 12 2018 Cronbuild Service <cronbuild@altlinux.org> 1:201802.12-alt1
- repocop cronbuild 20180212. At your service.

* Fri Jan 05 2018 Cronbuild Service <cronbuild@altlinux.org> 1:201801.05-alt1
- repocop cronbuild 20180105. At your service.

* Wed Dec 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201712.06-alt1
- repocop cronbuild 20171206. At your service.

* Wed Nov 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201711.15-alt1
- repocop cronbuild 20171115. At your service.

* Thu Oct 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201710.05-alt1
- repocop cronbuild 20171005. At your service.

* Fri Sep 08 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201709.08-alt1
- repocop cronbuild 20170908. At your service.

* Thu Aug 03 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201708.03-alt1
- repocop cronbuild 20170803. At your service.

* Tue Jul 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201707.04-alt1
- repocop cronbuild 20170704. At your service.

* Sat Jun 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201706.10-alt1
- repocop cronbuild 20170610. At your service.

* Fri May 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201705.05-alt1
- repocop cronbuild 20170505. At your service.

* Wed Apr 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201704.05-alt1
- repocop cronbuild 20170405. At your service.

* Thu Mar 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201703.09-alt1
- repocop cronbuild 20170309. At your service.

* Tue Feb 07 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201702.07-alt1
- repocop cronbuild 20170207. At your service.

* Thu Jan 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:201701.05-alt1
- repocop cronbuild 20170105. At your service.

* Fri Dec 09 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201612.09-alt1
- repocop cronbuild 20161209. At your service.

* Tue Dec 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201612.06-alt1
- repocop cronbuild 20161206. At your service.

* Thu Nov 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201611.03-alt1
- repocop cronbuild 20161103. At your service.

* Tue Oct 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201610.04-alt1
- repocop cronbuild 20161004. At your service.

* Sat Oct 01 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201610.01-alt1
- repocop cronbuild 20161001. At your service.

* Wed Sep 07 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201609.07-alt1
- repocop cronbuild 20160907. At your service.

* Tue Aug 02 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201608.02-alt1
- repocop cronbuild 20160802. At your service.

* Fri Jul 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201607.08-alt1
- repocop cronbuild 20160708. At your service.

* Wed Jun 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201606.08-alt1
- repocop cronbuild 20160608. At your service.

* Tue May 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201605.03-alt1
- repocop cronbuild 20160503. At your service.

* Sat Apr 30 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201604.30-alt1
- repocop cronbuild 20160430. At your service.

* Tue Apr 12 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201604.12-alt1
- repocop cronbuild 20160412. At your service.

* Wed Apr 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201604.06-alt1
- repocop cronbuild 20160406. At your service.

* Fri Mar 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201603.04-alt1
- repocop cronbuild 20160304. At your service.

* Thu Feb 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201602.04-alt1
- repocop cronbuild 20160204. At your service.

* Mon Jan 11 2016 Cronbuild Service <cronbuild@altlinux.org> 1:201601.11-alt1
- repocop cronbuild 20160111. At your service.

* Wed Dec 02 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201512.02-alt1
- repocop cronbuild 20151202. At your service.

* Thu Nov 05 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201511.05-alt1
- repocop cronbuild 20151105. At your service.

* Fri Oct 09 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201510.09-alt1
- repocop cronbuild 20151009. At your service.

* Tue Oct 06 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201510.06-alt1
- repocop cronbuild 20151006. At your service.

* Thu Sep 03 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201509.03-alt1
- repocop cronbuild 20150903. At your service.

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201508.23-alt1
- repocop cronbuild 20150823. At your service.

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201507.09-alt1
- repocop cronbuild 20150709. At your service.

* Wed Jun 03 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201506.03-alt1
- repocop cronbuild 20150603. At your service.

* Wed May 06 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201505.06-alt1
- repocop cronbuild 20150506. At your service.

* Thu Apr 09 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201504.09-alt1
- repocop cronbuild 20150409. At your service.

* Wed Mar 04 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201503.04-alt1
- repocop cronbuild 20150304. At your service.

* Thu Feb 05 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201502.05-alt1
- repocop cronbuild 20150205. At your service.

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 1:201501.09-alt1
- repocop cronbuild 20150109. At your service.

* Thu Dec 04 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201412.04-alt1
- repocop cronbuild 20141204. At your service.

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201411.07-alt1
- repocop cronbuild 20141107. At your service.

* Wed Oct 08 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201410.08-alt1
- repocop cronbuild 20141008. At your service.

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201409.11-alt1
- repocop cronbuild 20140911. At your service.

* Wed Jul 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201407.02-alt1
- repocop cronbuild 20140702. At your service.

* Thu Jun 05 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201406.05-alt1
- repocop cronbuild 20140605. At your service.

* Tue May 06 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201405.06-alt1
- repocop cronbuild 20140506. At your service.

* Thu Apr 03 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201404.03-alt1
- repocop cronbuild 20140403. At your service.

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201403.07-alt1
- repocop cronbuild 20140307. At your service.

* Wed Feb 05 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201402.05-alt1
- repocop cronbuild 20140205. At your service.

* Thu Jan 09 2014 Cronbuild Service <cronbuild@altlinux.org> 1:201401.09-alt1
- repocop cronbuild 20140109. At your service.

* Sat Dec 07 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201312.07-alt1
- repocop cronbuild 20131207. At your service.

* Thu Nov 07 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201311.07-alt1
- repocop cronbuild 20131107. At your service.

* Wed Oct 02 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201310.02-alt1
- repocop cronbuild 20131002. At your service.

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201309.05-alt1
- repocop cronbuild 20130905. At your service.

* Fri Aug 09 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201308.09-alt1
- repocop cronbuild 20130809. At your service.

* Thu Jul 04 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201307.04-alt1
- repocop cronbuild 20130704. At your service.

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201306.07-alt1
- repocop cronbuild 20130607. At your service.

* Sat May 11 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201305.11-alt1
- repocop cronbuild 20130511. At your service.

* Thu Apr 04 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201304.04-alt1
- repocop cronbuild 20130404. At your service.

* Fri Mar 08 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201303.08-alt1
- repocop cronbuild 20130308. At your service.

* Thu Feb 21 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201302.21-alt1
- repocop cronbuild 20130221. At your service.

* Tue Feb 12 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201302.12-alt1
- repocop cronbuild 20130212. At your service.

* Fri Jan 04 2013 Cronbuild Service <cronbuild@altlinux.org> 1:201301.04-alt1
- repocop cronbuild 20130104. At your service.

* Wed Dec 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201212.05-alt1
- repocop cronbuild 20121205. At your service.

* Sun Nov 11 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201211.11-alt1
- repocop cronbuild 20121111. At your service.

* Wed Oct 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201210.03-alt1
- repocop cronbuild 20121003. At your service.

* Thu Sep 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201209.06-alt1
- repocop cronbuild 20120906. At your service.

* Fri Aug 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201208.10-alt1
- repocop cronbuild 20120810. At your service.

* Thu Jul 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201207.05-alt1
- repocop cronbuild 20120705. At your service.

* Fri Jun 08 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201206.08-alt1
- repocop cronbuild 20120608. At your service.

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201205.22-alt1
- repocop cronbuild 20120522. At your service.

* Wed May 09 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201205-alt2
- manual alt2 release

* Thu May 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201205-alt1
- repocop cronbuild 20120503. At your service.

* Fri Apr 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201204-alt1
- repocop cronbuild 20120406. At your service.

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201203-alt1
- repocop cronbuild 20120307. At your service.

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201202-alt1
- repocop cronbuild 20120209. At your service.

* Sat Jan 07 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201201-alt1
- repocop cronbuild 20120107. At your service.

* Thu Dec 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201112-alt1
- repocop cronbuild 20111208. At your service.

* Wed Nov 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201111-alt1
- repocop cronbuild 20111102. At your service.

* Fri Sep 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201109-alt1
- repocop cronbuild 20110909. At your service.

* Sun Aug 07 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201108-alt1
- repocop cronbuild 20110807. At your service.

* Fri Jul 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201107-alt1
- repocop cronbuild 20110708. At your service.

* Thu Jun 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201106-alt1
- repocop cronbuild 20110602. At your service.

* Thu May 05 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201105-alt1
- repocop cronbuild 20110505. At your service.

* Tue Apr 05 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201104-alt1
- repocop cronbuild 20110405. At your service.

* Thu Mar 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201103-alt1
- repocop cronbuild 20110303. At your service.

* Fri Feb 04 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201102-alt1
- repocop cronbuild 20110204. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201101-alt1
- repocop cronbuild 20110114. At your service.

* Thu Nov 04 2010 Cronbuild Service <cronbuild@altlinux.org> 1:201011-alt1
- repocop cronbuild 20101104. At your service.

* Sun Oct 03 2010 Cronbuild Service <cronbuild@altlinux.org> 1:201010-alt1
- repocop cronbuild 20101003. At your service.

* Mon Sep 06 2010 Cronbuild Service <cronbuild@altlinux.org> 1:201009-alt1
- repocop cronbuild 20100906. At your service.

* Thu Feb 04 2010 Victor Forsiuk <force@altlinux.org> 1:201002-alt1
- February 2010 update.

* Thu Nov 05 2009 Victor Forsyuk <force@altlinux.org> 1:200911-alt1
- November 2009 update.

* Tue Aug 04 2009 Victor Forsyuk <force@altlinux.org> 20090801-alt1
- August 2009 update.

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 20090701-alt1
- July 2009 update.

* Mon Feb 09 2009 Victor Forsyuk <force@altlinux.org> 20090201-alt1
- February 2009 update.

* Thu Dec 04 2008 Victor Forsyuk <force@altlinux.org> 20081202-alt1
- December 2008 update.

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 20081003-alt1
- October 2008 update.

* Thu Aug 07 2008 Victor Forsyuk <force@altlinux.org> 20080804-alt1
- August 2008 update.

* Mon Jun 09 2008 Victor Forsyuk <force@altlinux.org> 20080602-alt1
- June 2008 update.

* Mon Apr 07 2008 Victor Forsyuk <force@altlinux.org> 20080401-alt1
- April 2008 update.

* Thu Mar 06 2008 Victor Forsyuk <force@altlinux.org> 20080305-alt1
- March 2008 update.

* Wed Jan 09 2008 Victor Forsyuk <force@altlinux.org> 20080103-alt1
- January 2008 update.

* Wed Oct 03 2007 Victor Forsyuk <force@altlinux.org> 20071002-alt1
- October 2007 update.

* Tue Sep 04 2007 Victor Forsyuk <force@altlinux.org> 20070902-alt1
- September 2007 update.
- This data is unusable without libGeoIP so add Requires.

* Fri Aug 31 2007 Victor Forsyuk <force@altlinux.org> 20070802-alt2
- Fix Provides.

* Fri Aug 10 2007 Victor Forsyuk <force@altlinux.org> 20070802-alt1
- August 2007 update.
- Correct License and package license text.

* Fri Jul 20 2007 Victor Forsyuk <force@altlinux.org> 20070702-alt1
- Initial build.
