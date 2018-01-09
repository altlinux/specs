%define foomatic_version 4.0.3
%define snapshot 20180109

%def_disable foo2zjs

Name: foomatic-db
Version: 4.0.%snapshot
Release: alt1

Summary: Foomatic printer database
License: GPL
Group: Publishing

BuildArch: noarch

Url: http://www.openprinting.org

# it is no more true for 4.x
# foomatic-db included foomatic-db-hpijs (exept for hpijs junk in db/source)
#Provides: foomatic-db-hpijs = %version-%release
#Provides: hplip-foomatic = 2.8.0
#Obsoletes: hplip-foomatic < 2.8.0

# http://www.openprinting.org/download/foomatic/
Source0: http://www.openprinting.org/download/foomatic/%name-%version.tar

# sync with SuSE cups-drivers-1.3.9-2.10.src.rpm
# note: cups-drivers-1.3.8-A4.patch is hacked manually for 4.0
#Patch0: cups-drivers-1.1.23-stcolor.patch
Patch0: foomatic-db-20100623-cups-drivers-stcolor.patch
#Patch1: cups-drivers-1.3.8-A4.patch
Patch1: cups-drivers-1.3.8-A4-alt.patch
Patch2: cups-drivers-1.3.8-hl7x0_language-alt.patch
Patch5: cups-drivers-1.3.8-samsunggdi-alt.patch

PreReq: foomatic-db-engine >= %foomatic_version

#we need foomatic-kitload during install
BuildPreReq: foomatic-db-engine cups >= 1.2.1

# Automatically added by buildreq on Fri May 26 2006 (-bi)
BuildRequires: cups foomatic-db-engine 
# autoremove conflicts
BuildRequires: foomatic-db-foo2zjs

%description
This package is the Foomatic database, an XML database containing
information about the capabilities of near 1000 printers and around
250 drivers. Especially it contains the information how and with which
options the drivers have to be executed.

The site http://www.linuxprinting.org/ is based in this database.

%if_enabled foo2zjs
%package -n foomatic-db-foo2zjs
BuildArch: noarch
Summary: Database of printers supported by foo2zjs drivers
Summary(ru_RU.UTF8): База данных принтеров, которые поддерживаются драйверами foo2zjs.
Group: System/Configuration/Hardware
#Requires: %name = %version-%release

%description -n foomatic-db-foo2zjs
Database of printers that are supported by foo2zjs drivers.

%description -l ru_RU.UTF-8 -n foomatic-db-foo2zjs
База данных принтеров, которые поддерживаются драйверами foo2zjs.
%endif

%package -n foomatic-db-docs
BuildArch: noarch
Summary: documentation files for the Foomatic printer database.
Summary(ru_RU.UTF8): Документация к базе данных принтеров Foomatic. 
Group: Documentation

%description -n foomatic-db-docs
This package is the documentation files for the Foomatic database.
It contains README and ChangeLog.

%description -l ru_RU.UTF-8 -n foomatic-db-docs
Документация к базе данных принтеров Foomatic. 
Включает в себя README и ChangeLog.

%prep
%setup -q
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch5 -p2

xz ChangeLog

%build
./make_configure
%configure --disable-gzip-ppds


# Delete drivers with empty command line prototype, they would give
# unusable printer/driver combos.
FOOMATICDB=`pwd` %_sbindir/foomatic-cleanupdrivers

%install
# Install data files
make	PREFIX=%_prefix \
        DESTDIR=%buildroot \
        install

# alt bug #26381
find %buildroot/usr/share/cups/model/ -name '*.htm' -print -delete
find %buildroot/usr/share/foomatic/db/ -name '*.htm' -print -delete

##force A4
#find %buildroot/%_datadir/%name/model -name "*.ppd" -print0 |
#	xargs -r0 perl -pi -e 's:^(\*Default.*)Letter\s*$:$1A4\n:; \
#		s:^(\*ImageableArea A4.*\:\s+)"0 0 595 842":$1"24 48 571 818":; \
#		s:^(\*ImageableArea Letter.*\:\s+)"0 0 612 792":$1"24 48 588 768":; \
#		s:\s\n:\n:'

#force A4
find %buildroot/%_datadir/%name/source/PPD -type f -name "*.ppd" -print0 |
	xargs -r0 perl -pi -e 's:^(\*Default.*)Letter\s*$:$1A4\n:; \
		s:\s\n:\n:'

# remove file conflicts with foomatic-db-foo2zjs
for i in `rpm -ql foomatic-db-foo2zjs| grep /usr/share/foomatic/db/source/printer/`; do
	rm -f %buildroot$i
done
# just in case
grep -rl 'foo2' %buildroot/usr/share/foomatic/db/source/printer | sed -e 's,%buildroot,,' | sort -u > foomatic-db-foo2zjs.ls
find %buildroot/usr/share/foomatic/db/source/printer -type f | sed -e 's,%buildroot,,' | sort > foomatic-db-all.ls
comm -23 foomatic-db-all.ls foomatic-db-foo2zjs.ls > foomatic-db-main.ls


%files -f foomatic-db-main.ls
%doc USAGE
%dir %_datadir/foomatic
%dir %_datadir/foomatic/db
%dir %_datadir/foomatic/db/source
%dir %_datadir/foomatic/db/source/printer
%_datadir/foomatic/db/oldprinterids
%_datadir/foomatic/db/source/PPD
%_datadir/foomatic/db/source/driver
%_datadir/foomatic/db/source/opt
%_datadir/foomatic/xmlschema

# killed by foomatic-cleanupdrivers
#%exclude %_datadir/foomatic/db/source/driver/foo2*

%_datadir/cups/model/foomatic-db-ppds

#not found in tarball
#%exclude %_datadir/foomatic/db/source/PPD/*.sh

%if_enabled foo2zjs
%files -n foomatic-db-foo2zjs -f foomatic-db-foo2zjs.ls
# killed by foomatic-cleanupdrivers
#%_datadir/foomatic/db/source/driver/foo2*
%endif

%files -n foomatic-db-docs
%doc README ChangeLog.xz

%changelog
* Tue Jan 09 2018 Cronbuild Service <cronbuild@altlinux.org> 4.0.20180109-alt1
- repocop cronbuild 20180109. At your service.

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.20170906-alt1.1
- compressed changelog (repocop warning)

* Wed Sep 06 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.20170906-alt1
- repocop cronbuild 20170906. At your service.

* Wed May 31 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.20170531-alt1
- repocop cronbuild 20170531. At your service.

* Wed Mar 22 2017 Cronbuild Service <cronbuild@altlinux.org> 4.0.20170322-alt1
- repocop cronbuild 20170322. At your service.

* Wed Dec 14 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.20161214-alt1
- repocop cronbuild 20161214. At your service.

* Wed Oct 05 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.20161005-alt1
- repocop cronbuild 20161005. At your service.

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.20160920-alt1
- repocop cronbuild 20160920. At your service.

* Tue Jun 28 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.20160628-alt1
- repocop cronbuild 20160628. At your service.

* Tue Jun 14 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.20160614-alt1
- repocop cronbuild 20160614. At your service.

* Tue Apr 19 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.20160419-alt1
- repocop cronbuild 20160419. At your service.

* Sun Apr 03 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.20160403-alt1
- repocop cronbuild 20160403. At your service.

* Sun Mar 06 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.20160306-alt1
- repocop cronbuild 20160306. At your service.

* Sat Feb 20 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.20160220-alt1
- repocop cronbuild 20160220. At your service.

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 4.0.20150823-alt1
- repocop cronbuild 20150823. At your service.

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 4.0.20150424-alt1
- repocop cronbuild 20150424. At your service.

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 4.0.20150227-alt1
- repocop cronbuild 20150227. At your service.

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140911-alt1
- repocop cronbuild 20140911. At your service.

* Thu Jul 03 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140703-alt1
- repocop cronbuild 20140703. At your service.

* Wed Jun 18 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140618-alt1
- repocop cronbuild 20140618. At your service.

* Fri Jun 13 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.20140426-alt1
- improved foo2zjs conflict remover

* Thu Jun 12 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.20140425-alt1
- rebuild to remove conflict with foo2zjs

* Thu Apr 24 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140424-alt1
- repocop cronbuild 20140424. At your service.

* Thu Apr 10 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140410-alt1
- repocop cronbuild 20140410. At your service.

* Wed Mar 26 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140326-alt1
- repocop cronbuild 20140326. At your service.

* Thu Mar 13 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140313-alt1
- repocop cronbuild 20140313. At your service.

* Wed Jan 29 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140129-alt1
- repocop cronbuild 20140129. At your service.

* Thu Jan 16 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140116-alt1
- repocop cronbuild 20140116. At your service.

* Wed Jan 01 2014 Cronbuild Service <cronbuild@altlinux.org> 4.0.20140101-alt1
- repocop cronbuild 20140101. At your service.

* Thu Dec 05 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20131205-alt1
- repocop cronbuild 20131205. At your service.

* Wed Nov 20 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20131120-alt1
- repocop cronbuild 20131120. At your service.

* Thu Sep 26 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20130926-alt1
- repocop cronbuild 20130926. At your service.

* Wed Sep 11 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20130911-alt1
- repocop cronbuild 20130911. At your service.

* Thu Jun 06 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20130606-alt1
- repocop cronbuild 20130606. At your service.

* Fri Apr 05 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20130405-alt1
- repocop cronbuild 20130405. At your service.

* Fri Mar 22 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20130322-alt1
- repocop cronbuild 20130322. At your service.

* Sat Mar 09 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20130309-alt1
- repocop cronbuild 20130309. At your service.

* Fri Feb 22 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20130222-alt1
- repocop cronbuild 20130222. At your service.

* Sat Jan 26 2013 Cronbuild Service <cronbuild@altlinux.org> 4.0.20130126-alt1
- repocop cronbuild 20130126. At your service.

* Sat Dec 29 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20121229-alt1
- repocop cronbuild 20121229. At your service.

* Fri Nov 30 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20121130-alt1
- repocop cronbuild 20121130. At your service.

* Fri Sep 21 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120921-alt1
- repocop cronbuild 20120921. At your service.

* Fri Sep 07 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120907-alt1
- repocop cronbuild 20120907. At your service.

* Fri Aug 24 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120824-alt1
- repocop cronbuild 20120824. At your service.

* Fri Jul 27 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120727-alt1
- repocop cronbuild 20120727. At your service.

* Fri Jul 13 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120713-alt1
- repocop cronbuild 20120713. At your service.

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120604-alt1
- repocop cronbuild 20120604. At your service.

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120521-alt1
- repocop cronbuild 20120521. At your service.

* Mon Mar 26 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120326-alt1
- repocop cronbuild 20120326. At your service.

* Mon Mar 12 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120312-alt1
- repocop cronbuild 20120312. At your service.

* Sun Mar 04 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120304-alt1
- repocop cronbuild 20120304. At your service.

* Sun Feb 19 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120219-alt1
- repocop cronbuild 20120219. At your service.

* Sun Feb 05 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120205-alt1
- repocop cronbuild 20120205. At your service.

* Sun Jan 22 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120122-alt1
- repocop cronbuild 20120122. At your service.

* Sun Jan 08 2012 Cronbuild Service <cronbuild@altlinux.org> 4.0.20120108-alt1
- repocop cronbuild 20120108. At your service.

* Sun Dec 25 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20111225-alt1
- repocop cronbuild 20111225. At your service.

* Sun Dec 11 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20111211-alt1
- repocop cronbuild 20111211. At your service.

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 4.0.20111208-alt1
- repocop cronbuild 20111208. At your service.

* Tue Oct 11 2011 Andrey Cherepanov <cas@altlinux.org> 4.0.20110911-alt2
- complete remove all wrong driver information files

* Wed Sep 28 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110911-alt1
- bugfix release (closes: #26381)

* Sat Sep 10 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110910-alt1
- repocop cronbuild 20110910. At your service.

* Sat Aug 27 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110827-alt1
- repocop cronbuild 20110827. At your service.

* Sat Aug 13 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110813-alt1
- repocop cronbuild 20110813. At your service.

* Sat Jul 30 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110730-alt1
- repocop cronbuild 20110730. At your service.

* Fri Jul 15 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110715-alt1
- repocop cronbuild 20110715. At your service.

* Fri Jul 01 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110701-alt1
- repocop cronbuild 20110701. At your service.

* Fri Jun 17 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110617-alt1
- repocop cronbuild 20110617. At your service.

* Fri Jun 03 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110603-alt1
- repocop cronbuild 20110603. At your service.

* Fri May 20 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110520-alt1
- repocop cronbuild 20110520. At your service.

* Fri May 06 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110506-alt1
- repocop cronbuild 20110506. At your service.

* Fri Apr 22 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110422-alt1
- repocop cronbuild 20110422. At your service.

* Fri Apr 08 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110408-alt1
- repocop cronbuild 20110408. At your service.

* Fri Mar 25 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110325-alt1
- repocop cronbuild 20110325. At your service.

* Fri Mar 11 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110311-alt1
- repocop cronbuild 20110311. At your service.

* Fri Feb 25 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110225-alt1
- repocop cronbuild 20110225. At your service.

* Fri Feb 11 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110211-alt1
- repocop cronbuild 20110211. At your service.

* Fri Jan 28 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110128-alt1
- repocop cronbuild 20110128. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 4.0.20110114-alt1
- repocop cronbuild 20110114. At your service.

* Mon Dec 13 2010 Cronbuild Service <cronbuild@altlinux.org> 4.0.20101213-alt1
- repocop cronbuild 20101213. At your service.

* Mon Nov 29 2010 Cronbuild Service <cronbuild@altlinux.org> 4.0.20101129-alt1
- repocop cronbuild 20101129. At your service.

* Mon Nov 15 2010 Cronbuild Service <cronbuild@altlinux.org> 4.0.20101115-alt1
- repocop cronbuild 20101115. At your service.

* Mon Oct 18 2010 Cronbuild Service <cronbuild@altlinux.org> 4.0.20101018-alt1
- repocop cronbuild 20101018. At your service.

* Tue Oct 05 2010 Cronbuild Service <cronbuild@altlinux.org> 4.0.20101005-alt1
- repocop cronbuild 20101005. At your service.

* Tue Sep 21 2010 Cronbuild Service <cronbuild@altlinux.org> 4.0.20100921-alt1
- repocop cronbuild 20100921. At your service.

* Tue Sep 07 2010 Cronbuild Service <cronbuild@altlinux.org> 4.0.20100907-alt1
- repocop cronbuild 20100907. At your service.

* Wed Sep 01 2010 Cronbuild Service <cronbuild@altlinux.org> 4.0.20100901-alt1
- repocop cronbuild 20100901. At your service.

* Sat Jul 31 2010 Igor Vlasenko <viy@altlinux.ru> 4.0.20100731-alt1
- repocop cronbuild 20100731. At your service.

* Wed Jul 07 2010 Igor Vlasenko <viy@altlinux.ru> 4.0.20100707-alt1
- repocop cronbuild 20100707. At your service.

* Wed Jun 30 2010 Igor Vlasenko <viy@altlinux.ru> 4.0.20100630-alt1
- repocop cronbuild 20100630. At your service.

* Thu Jun 24 2010 Igor Vlasenko <viy@altlinux.ru> 4.0.20100624-alt1
- repocop cronbuild 20100624. At your service.

* Wed Jun 23 2010 Igor Vlasenko <viy@altlinux.ru> 4.0.20100623-alt1
- repocop cronbuild 20100623. At your service.

* Thu Nov 19 2009 Igor Vlasenko <viy@altlinux.ru> 4.0.20091119-alt1
- foomatic-db-4.0-20091119
- added foomatic-db-docs subpackage (big changelog)
- added disabled by default foomatic-db-foo2zjs subpackage

* Wed Sep 09 2009 Igor Vlasenko <viy@altlinux.ru> 4.0.20090909-alt1
- foomatic-db-4.0-20090909
- removed foomatic-db-hpijs, dropped by upstream

* Thu Dec 04 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2.20081126-alt9
- requres foomatic-db-engine >= version

* Wed Dec 03 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2.20081126-alt8
- snapshot 20081126
- added a bunch of fresh SuSE patches
- new backports-friendly version

* Sat Aug 09 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt7.20080809
- snapshot 20080809

* Mon Jun 09 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt7.20080607
- added optional foomatic-db-hpijs
- added Provides: foomatic-db-hpijs, hplip-foomatic

* Sat Jun 07 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt6.20080607
- snapshot 20080607

* Wed Mar 26 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt6.20080326
- snapshot 20080326

* Thu Nov 08 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt6.20071012
- add suse patch: force A4 format

* Mon Oct 15 2007 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt5.20071012
- snapshot 20071012

* Thu Oct 11 2007 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt5.20070919
- CMU (co-maintainer upload):
  snapshot 20070919 

* Thu Sep 06 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt4
- 20070820

* Fri May 26 2006 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt3
- replace gutenprint with gimp-print

* Fri May 26 2006 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt2
- new snapshot

* Mon Apr 03 2006 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt1.20060329
- new snapshot

* Thu Apr 14 2005 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt1.20050404
- 3.0.2 snapshot

* Fri Jan 28 2005 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt3.20040828
- added update-printers-db in post script

* Tue Sep 21 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt2.20040828
- latest snapshot

* Wed May 05 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1.20040428
- latest snapshot

* Wed Feb 11 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1.20040128
- new foomatic snapshot
- exclude gimp-print.xml driver

* Fri Dec 26 2003 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1.20031219
- fix permissions of data files

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt0.20031219
- 3.0.1

* Mon Sep 29 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt3.20030310
- fix build in hasher
- TODO: update database after update of GS

* Mon Mar 31 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt2.20030310
- latest snapshot

* Wed Feb 26 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt1.20030213
- Initial release
