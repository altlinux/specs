Name: GeoIP-Lite-City
Version: 201207.05
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
