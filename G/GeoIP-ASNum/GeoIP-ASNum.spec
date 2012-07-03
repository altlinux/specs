Name: GeoIP-ASNum
Version: 201207
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
