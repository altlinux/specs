Name: GeoIP-Lite-Country
Version: 20171206
Release: alt1
# OK, day designation in version string is unneeded, this file updates strictly
# monthly. We need to introduce Epoch in order to drop day from version
Epoch: 1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: GeoLite Country database file
License: OPEN DATA LICENSE (see LICENSE.txt)
Group: System/Libraries

Url: http://www.maxmind.com/app/geolitecountry
Source: http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
Source1: GeoIP-data-LICENSE.txt

BuildArch: noarch

Requires: libGeoIP > 1.4.2-alt1

# Need to do it explicitly...
Provides: /usr/share/GeoIP/GeoIP.dat

%description
This package contain the free edition country database for GeoIP. This
database simply contains IP blocks as keys, and countries as values. It
should be more complete and accurate than using reverse DNS lookups.

%prep
%setup -T -c

%build
cp %SOURCE1 ./LICENSE.txt

%install
install -d %buildroot%_datadir/GeoIP
gunzip -c %_sourcedir/GeoIP.dat.gz >%buildroot%_datadir/GeoIP/GeoIP.dat

%files
%doc LICENSE.txt
%dir %_datadir/GeoIP/
%config(noreplace) %_datadir/GeoIP/GeoIP.dat

# Why mark DB as config(noreplace)? User can update GeoIP.dat directly
# fetching file from MaxMind site via monthly cron job. In such case
# this package may actually overwrite freshly downloaded DB with older
# version. We mark file norepace in order to prevent rpm from doing this.

%changelog
* Wed Dec 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20171206-alt1
- repocop cronbuild 20171206. At your service.

* Wed Nov 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20171115-alt1
- repocop cronbuild 20171115. At your service.

* Wed Oct 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20171004-alt1
- repocop cronbuild 20171004. At your service.

* Thu Sep 07 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170907-alt1
- repocop cronbuild 20170907. At your service.

* Sat Aug 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170805-alt1
- repocop cronbuild 20170805. At your service.

* Thu Jul 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170706-alt1
- repocop cronbuild 20170706. At your service.

* Fri Jun 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170609-alt1
- repocop cronbuild 20170609. At your service.

* Thu May 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170504-alt1
- repocop cronbuild 20170504. At your service.

* Tue Apr 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170404-alt1
- repocop cronbuild 20170404. At your service.

* Wed Mar 08 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170308-alt1
- repocop cronbuild 20170308. At your service.

* Thu Feb 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170209-alt1
- repocop cronbuild 20170209. At your service.

* Wed Jan 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:20170104-alt1
- repocop cronbuild 20170104. At your service.

* Thu Dec 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161208-alt1
- repocop cronbuild 20161208. At your service.

* Wed Nov 02 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161102-alt1
- repocop cronbuild 20161102. At your service.

* Thu Oct 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20161006-alt1
- repocop cronbuild 20161006. At your service.

* Fri Sep 30 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160930-alt1
- repocop cronbuild 20160930. At your service.

* Fri Sep 09 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160909-alt1
- repocop cronbuild 20160909. At your service.

* Tue Sep 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160906-alt1
- repocop cronbuild 20160906. At your service.

* Thu Aug 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160804-alt1
- repocop cronbuild 20160804. At your service.

* Fri Jul 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160708-alt1
- repocop cronbuild 20160708. At your service.

* Wed Jun 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160608-alt1
- repocop cronbuild 20160608. At your service.

* Tue May 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160503-alt1
- repocop cronbuild 20160503. At your service.

* Wed Apr 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160406-alt1
- repocop cronbuild 20160406. At your service.

* Fri Mar 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160304-alt1
- repocop cronbuild 20160304. At your service.

* Thu Feb 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160204-alt1
- repocop cronbuild 20160204. At your service.

* Mon Jan 11 2016 Cronbuild Service <cronbuild@altlinux.org> 1:20160111-alt1
- repocop cronbuild 20160111. At your service.

* Wed Dec 02 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151202-alt1
- repocop cronbuild 20151202. At your service.

* Thu Nov 05 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151105-alt1
- repocop cronbuild 20151105. At your service.

* Tue Oct 27 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151027-alt1
- repocop cronbuild 20151027. At your service.

* Fri Oct 09 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151009-alt1
- repocop cronbuild 20151009. At your service.

* Tue Oct 06 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20151006-alt1
- repocop cronbuild 20151006. At your service.

* Thu Sep 03 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150903-alt1
- repocop cronbuild 20150903. At your service.

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150823-alt1
- repocop cronbuild 20150823. At your service.

* Fri Jul 24 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150724-alt1
- repocop cronbuild 20150724. At your service.

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150709-alt1
- repocop cronbuild 20150709. At your service.

* Wed Jun 03 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150603-alt1
- repocop cronbuild 20150603. At your service.

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150508-alt1
- repocop cronbuild 20150508. At your service.

* Wed Apr 08 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150408-alt1
- repocop cronbuild 20150408. At your service.

* Tue Mar 03 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150303-alt1
- repocop cronbuild 20150303. At your service.

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150207-alt1
- repocop cronbuild 20150207. At your service.

* Thu Jan 08 2015 Cronbuild Service <cronbuild@altlinux.org> 1:20150108-alt1
- repocop cronbuild 20150108. At your service.

* Wed Dec 03 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141203-alt1
- repocop cronbuild 20141203. At your service.

* Thu Nov 06 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141106-alt1
- repocop cronbuild 20141106. At your service.

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20141010-alt1
- repocop cronbuild 20141010. At your service.

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140911-alt1
- repocop cronbuild 20140911. At your service.

* Wed Jul 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140702-alt1
- repocop cronbuild 20140702. At your service.

* Thu Jun 05 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140605-alt1
- repocop cronbuild 20140605. At your service.

* Tue May 06 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140506-alt1
- repocop cronbuild 20140506. At your service.

* Thu Apr 03 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140403-alt1
- repocop cronbuild 20140403. At your service.

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140307-alt1
- repocop cronbuild 20140307. At your service.

* Wed Feb 05 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140205-alt1
- repocop cronbuild 20140205. At your service.

* Thu Jan 09 2014 Cronbuild Service <cronbuild@altlinux.org> 1:20140109-alt1
- repocop cronbuild 20140109. At your service.

* Sat Dec 07 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20131207-alt1
- repocop cronbuild 20131207. At your service.

* Thu Nov 07 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20131107-alt1
- repocop cronbuild 20131107. At your service.

* Wed Oct 02 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20131002-alt1
- repocop cronbuild 20131002. At your service.

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130905-alt1
- repocop cronbuild 20130905. At your service.

* Fri Aug 09 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130809-alt1
- repocop cronbuild 20130809. At your service.

* Thu Jul 04 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130704-alt1
- repocop cronbuild 20130704. At your service.

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130607-alt1
- repocop cronbuild 20130607. At your service.

* Sat May 11 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130511-alt1
- repocop cronbuild 20130511. At your service.

* Fri Apr 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130405-alt1
- repocop cronbuild 20130405. At your service.

* Wed Mar 06 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130306-alt1
- repocop cronbuild 20130306. At your service.

* Fri Feb 22 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130222-alt1
- repocop cronbuild 20130222. At your service.

* Thu Feb 07 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130207-alt1
- repocop cronbuild 20130207. At your service.

* Wed Jan 02 2013 Cronbuild Service <cronbuild@altlinux.org> 1:20130102-alt1
- repocop cronbuild 20130102. At your service.

* Thu Dec 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1:20121206-alt1
- repocop cronbuild 20121206. At your service.

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 1:20121112-alt1
- repocop cronbuild 20121112. At your service.

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 1:20121101-alt1
- returned day to version, as sometimes updates are more frequent.

* Thu Nov 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201211-alt1
- repocop cronbuild 20121101. At your service.

* Wed Oct 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201210-alt1
- repocop cronbuild 20121003. At your service.

* Thu Sep 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201209-alt1
- repocop cronbuild 20120906. At your service.

* Fri Aug 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201208-alt1
- repocop cronbuild 20120810. At your service.

* Thu Jul 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201207-alt1
- repocop cronbuild 20120705. At your service.

* Fri Jun 08 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201206-alt1
- repocop cronbuild 20120608. At your service.

* Thu May 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201205-alt1
- repocop cronbuild 20120503. At your service.

* Fri Apr 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201204-alt1
- repocop cronbuild 20120406. At your service.

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201203-alt1
- repocop cronbuild 20120307. At your service.

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201202-alt1
- repocop cronbuild 20120209. At your service.

* Wed Jan 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1:201201-alt1
- repocop cronbuild 20120104. At your service.

* Thu Dec 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201112-alt1
- repocop cronbuild 20111208. At your service.

* Wed Nov 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201111-alt1
- repocop cronbuild 20111102. At your service.

* Fri Sep 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201109-alt1
- repocop cronbuild 20110909. At your service.

* Sat Aug 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201108-alt1
- repocop cronbuild 20110806. At your service.

* Thu Jul 07 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201107-alt1
- repocop cronbuild 20110707. At your service.

* Sat Jun 04 2011 Cronbuild Service <cronbuild@altlinux.org> 1:201106-alt1
- repocop cronbuild 20110604. At your service.

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
- Fix provides.

* Fri Aug 10 2007 Victor Forsyuk <force@altlinux.org> 20070802-alt1
- August 2007 update.
- Correct License and package license text.

* Fri Jul 20 2007 Victor Forsyuk <force@altlinux.org> 20070702-alt1
- Initial build.
