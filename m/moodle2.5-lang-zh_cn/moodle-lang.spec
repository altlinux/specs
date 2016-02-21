# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename zh_cn
%define packagversion 2.5.0
%define packagedate 201602200032
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Chinese (Simplified)
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-zh_cn
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.5
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.5
Provides: %moodle_name-%packagetype-%packagename-version = %packagedate
Provides: %moodle_name-%packagetype-%packagename = %version-%release
Provides: %moodle_name-%packagetype-%oldpackagename = %version-%release
Conflicts: %moodle_name-%packagetype-%packagename < %version
Conflicts: %moodle_name-%packagetype-%oldpackagename < %version

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-fonts

%description
%summary

%prep
%setup

%build

%install
mkdir -p  %buildroot%moodle_langdir/
cp -rp * %buildroot%moodle_langdir/

# Create symlink for default.ttf
install -d %buildroot%default_ttfdir
ln -s -f $(relative %buildroot%_ttffontsdir/chinese-gb2312/gbsn00lp.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602200032-alt1
- repocop cronbuild 20160221. At your service.
- zh_cn.zip build 2016-02-20 00:32 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601211256-alt1
- repocop cronbuild 20160124. At your service.
- zh_cn.zip build 2016-01-21 12:56 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511240803-alt1
- repocop cronbuild 20151130. At your service.
- zh_cn.zip build 2015-11-24 08:03 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511230121-alt1
- repocop cronbuild 20151123. At your service.
- zh_cn.zip build 2015-11-23 01:21 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510060914-alt1
- repocop cronbuild 20151012. At your service.
- zh_cn.zip build 2015-10-06 09:14 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509250112-alt1
- repocop cronbuild 20150928. At your service.
- zh_cn.zip build 2015-09-25 01:12 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509130055-alt1
- repocop cronbuild 20150914. At your service.
- zh_cn.zip build 2015-09-13 00:55 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508281016-alt1
- repocop cronbuild 20150831. At your service.
- zh_cn.zip build 2015-08-28 10:16 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508070519-alt1
- repocop cronbuild 20150823. At your service.
- zh_cn.zip build 2015-08-07 05:19 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507210937-alt1
- repocop cronbuild 20150723. At your service.
- zh_cn.zip build 2015-07-21 09:37 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507132308-alt1
- repocop cronbuild 20150716. At your service.
- zh_cn.zip build 2015-07-13 23:08 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507070310-alt1
- repocop cronbuild 20150709. At your service.
- zh_cn.zip build 2015-07-07 03:10 UTC

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505091312-alt1
- repocop cronbuild 20150515. At your service.
- zh_cn.zip build 2015-05-09 13:12 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504180435-alt1
- repocop cronbuild 20150424. At your service.
- zh_cn.zip build 2015-04-18 04:35 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503270553-alt1
- repocop cronbuild 20150327. At your service.
- zh_cn.zip build 2015-03-27 05:53 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503020125-alt1
- repocop cronbuild 20150306. At your service.
- zh_cn.zip build 2015-03-02 01:25 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502100146-alt1
- repocop cronbuild 20150213. At your service.
- zh_cn.zip build 2015-02-10 01:46 UTC

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501160156-alt1
- repocop cronbuild 20150116. At your service.
- zh_cn.zip build 2015-01-16 01:56 UTC

* Fri Dec 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412250823-alt1
- repocop cronbuild 20141226. At your service.
- zh_cn.zip build 2014-12-25 08:23 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412150059-alt1
- repocop cronbuild 20141219. At your service.
- zh_cn.zip build 2014-12-15 00:59 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411060733-alt1
- repocop cronbuild 20141107. At your service.
- zh_cn.zip build 2014-11-06 07:33 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410070614-alt1
- repocop cronbuild 20141010. At your service.
- zh_cn.zip build 2014-10-07 06:14 UTC

* Fri Sep 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409191007-alt1
- repocop cronbuild 20140926. At your service.
- zh_cn.zip build 2014-09-19 10:07 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201408252217-alt1
- repocop cronbuild 20140919. At your service.
- zh_cn.zip build 2014-08-25 22:17 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406090304-alt1
- repocop cronbuild 20140613. At your service.
- zh_cn.zip build 2014-06-09 03:04 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405220618-alt1
- repocop cronbuild 20140523. At your service.
- zh_cn.zip build 2014-05-22 06:18 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405061410-alt1
- repocop cronbuild 20140509. At your service.
- zh_cn.zip build 2014-05-06 14:10 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404250120-alt1
- repocop cronbuild 20140425. At your service.
- zh_cn.zip build 2014-04-25 01:20 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404170728-alt1
- repocop cronbuild 20140418. At your service.
- zh_cn.zip build 2014-04-17 07:28 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404110119-alt1
- repocop cronbuild 20140411. At your service.
- zh_cn.zip build 2014-04-11 01:19 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403060139-alt1
- repocop cronbuild 20140307. At your service.
- zh_cn.zip build 2014-03-06 01:39 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312310327-alt1
- repocop cronbuild 20140103. At your service.
- zh_cn.zip build 2013-12-31 03:27 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312160649-alt1
- repocop cronbuild 20131220. At your service.
- zh_cn.zip build 2013-12-16 06:49 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- zh_cn.zip build 2013-12-13 05:46 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310070909-alt1
- repocop cronbuild 20131011. At your service.
- zh_cn.zip build 2013-10-07 09:09 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308311136-alt1
- repocop cronbuild 20130906. At your service.
- zh_cn.zip build 2013-08-31 11:36 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308280430-alt1
- repocop cronbuild 20130831. At your service.
- zh_cn.zip build 2013-08-28 04:30 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307201617-alt1
- repocop cronbuild 20130727. At your service.
- zh_cn.zip build 2013-07-20 16:17 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307181356-alt1
- repocop cronbuild 20130720. At your service.
- zh_cn.zip build 2013-07-18 13:56 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307121450-alt1
- repocop cronbuild 20130713. At your service.
- zh_cn.zip build 2013-07-12 14:50 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307030001-alt1
- repocop cronbuild 20130706. At your service.
- zh_cn.zip build 2013-07-03 00:01 UTC

* Sat Jun 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306270119-alt1
- repocop cronbuild 20130629. At your service.
- zh_cn.zip build 2013-06-27 01:19 UTC

* Sat Jun 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306220107-alt1
- repocop cronbuild 20130622. At your service.
- zh_cn.zip build 2013-06-22 01:07 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140511-alt1
- repocop cronbuild 20130615. At your service.
- zh_cn.zip build 2013-06-14 05:11 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305292351-alt1
- Rename package to moodle2.5-lang-zh_cn
- zh_cn.zip build 2013-05-29 23:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221013-alt1
- repocop cronbuild 20130524. At your service.
- zh_cn.zip build 2013-05-22 10:13 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304080842-alt1
- Rename package to moodle2.4-lang-zh_cn
- zh_cn.zip build 2013-04-08 08:42 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303030525-alt1
- repocop cronbuild 20130304. At your service.
- zh_cn.zip build 2013-03-03 05:25 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302110345-alt1
- repocop cronbuild 20130218. At your service.
- zh_cn.zip build 2013-02-11 03:45 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301270210-alt1
- repocop cronbuild 20130128. At your service.
- zh_cn.zip build 2013-01-27 02:10 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212292118-alt1
- repocop cronbuild 20130107. At your service.
- zh_cn.zip build 2012-12-29 21:18 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- zh_cn.zip build 2012-11-01 07:00 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210261002-alt1
- repocop cronbuild 20121029. At your service.
- zh_cn.zip build 2012-10-26 10:02 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210211520-alt1
- repocop cronbuild 20121022. At your service.
- zh_cn.zip build 2012-10-21 15:20 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210020550-alt1
- repocop cronbuild 20121008. At your service.
- zh_cn.zip build 2012-10-02 05:50 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209110500-alt1
- repocop cronbuild 20120911. At your service.
- zh_cn.zip build 2012-09-11 05:00 UTC

* Wed Sep 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120905. At your service.
- zh_cn.zip build 2012-08-31 10:30 UTC

* Wed Aug 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208260731-alt1
- repocop cronbuild 20120829. At your service.
- zh_cn.zip build 2012-08-26 07:31 UTC

* Wed Aug 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208200109-alt1
- repocop cronbuild 20120822. At your service.
- zh_cn.zip build 2012-08-20 01:09 UTC

* Wed Aug 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208141325-alt1
- repocop cronbuild 20120815. At your service.
- zh_cn.zip build 2012-08-14 13:25 UTC

* Wed Aug 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208070817-alt1
- repocop cronbuild 20120808. At your service.
- zh_cn.zip build 2012-08-07 08:17 UTC

* Wed Aug 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207250644-alt1
- repocop cronbuild 20120801. At your service.
- zh_cn.zip build 2012-07-25 06:44 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207151119-alt1
- repocop cronbuild 20120717. At your service.
- zh_cn.zip build 2012-07-15 11:19 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207061246-alt1
- repocop cronbuild 20120710. At your service.
- zh_cn.zip build 2012-07-06 12:46 UTC

* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207030019-alt1
- repocop cronbuild 20120704. At your service.
- zh_cn.zip build 2012-07-03 00:19 UTC

* Wed Jun 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206231235-alt1
- repocop cronbuild 20120627. At your service.
- zh_cn.zip build 2012-06-23 12:35 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206190153-alt1
- repocop cronbuild 20120619. At your service.
- zh_cn.zip build 2012-06-19 01:53 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121321-alt1
- repocop cronbuild 20120612. At your service.
- zh_cn.zip build 2012-06-12 13:21 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206051408-alt1
- repocop cronbuild 20120605. At your service.
- zh_cn.zip build 2012-06-05 14:08 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205290000-alt1
- repocop cronbuild 20120529. At your service.
- zh_cn.zip build 2012-05-29 00:00 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205210759-alt1
- repocop cronbuild 20120522. At your service.
- zh_cn.zip build 2012-05-21 07:59 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205141128-alt1
- repocop cronbuild 20120515. At your service.
- zh_cn.zip build 2012-05-14 11:28 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205050157-alt1
- repocop cronbuild 20120508. At your service.
- zh_cn.zip build 2012-05-05 01:57 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204290138-alt1
- repocop cronbuild 20120501. At your service.
- zh_cn.zip build 2012-04-29 01:38 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204180710-alt1
- repocop cronbuild 20120424. At your service.
- zh_cn.zip build 2012-04-18 07:10 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204150051-alt1
- repocop cronbuild 20120417. At your service.
- zh_cn.zip build 2012-04-15 00:51 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204062353-alt1
- repocop cronbuild 20120410. At your service.
- zh_cn.zip build 2012-04-06 23:53 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204021057-alt1
- repocop cronbuild 20120403. At your service.
- zh_cn.zip build 2012-04-02 10:57 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203260300-alt1
- repocop cronbuild 20120327. At your service.
- zh_cn.zip build 2012-03-26 03:00 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203190057-alt1
- Rename package to moodle2.2-lang-zh_cn
- zh_cn.zip build 2012-03-19 00:57 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203190057-alt1
- repocop cronbuild 20120320. At your service.
- zh_cn.zip build 2012-03-19 00:57 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203050017-alt1
- repocop cronbuild 20120307. At your service.
- zh_cn.zip build 2012-03-05 00:17 UTC

* Wed Feb 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202291152-alt1
- repocop cronbuild 20120229. At your service.
- zh_cn.zip build 2012-02-29 11:52 UTC

* Wed Feb 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202180928-alt1
- repocop cronbuild 20120222. At your service.
- zh_cn.zip build 2012-02-18 09:28 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202130111-alt1
- repocop cronbuild 20120215. At your service.
- zh_cn.zip build 2012-02-13 01:11 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202061021-alt1
- repocop cronbuild 20120208. At your service.
- zh_cn.zip build 2012-02-06 10:21 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201301220-alt1
- repocop cronbuild 20120201. At your service.
- zh_cn.zip build 2012-01-30 12:20 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201230846-alt1
- repocop cronbuild 20120125. At your service.
- zh_cn.zip build 2012-01-23 08:46 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201080425-alt1
- repocop cronbuild 20120111. At your service.
- zh_cn.zip build 2012-01-08 04:25 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112160535-alt1
- repocop cronbuild 20111221. At your service.
- zh_cn.zip build 2011-12-16 05:35 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112121304-alt1
- repocop cronbuild 20111214. At your service.
- zh_cn.zip build 2011-12-12 13:04 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112041131-alt1
- repocop cronbuild 20111207. At your service.
- zh_cn.zip build 2011-12-04 11:31 UTC

* Thu Dec 01 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111290202-alt1
- repocop cronbuild 20111201. At your service.
- zh_cn.zip build 2011-11-29 02:02 UTC

* Sun Nov 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111270215-alt1
- repocop cronbuild 20111127. At your service.
- zh_cn.zip build 2011-11-27 02:15 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111251135-alt1
- Rename package to moodle2.1-lang-zh_cn
- zh_cn.zip build 2011-11-25 11:35 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111220133-alt2
- Fix requires

* Tue Nov 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111220133-alt1
- repocop cronbuild 20111122. At your service.
- zh_cn.zip build 2011-11-22 01:33 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111130433-alt1
- repocop cronbuild 20111116. At your service.
- zh_cn.zip build 2011-11-13 04:33 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111021307-alt3
- Use %%_ttffontsdir/chinese-gb2312/gbsn00lp.ttf for
  %%moodle_langdir/zh_cn/fonts/default.ttf
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111021307-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111021307-alt1
- repocop cronbuild 20111105. At your service.
- zh_cn.zip build 2011-11-02 13:07 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110251310-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110251310-alt2
- Update for cronbuild use

* Tue Oct 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110251310-alt1
- zh_cn.zip build 2011-10-25 13:10 UTC

* Mon Oct 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241152-alt1
- zh_cn.zip build 2011-10-24 11:52 UTC

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110220330-alt1
- zh_cn.zip build 2011-10-22 03:30 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110050227-alt1
- zh_cn.zip build 2011-10-05 02:27 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109281117-alt1
- zh_cn.zip build 2011-09-28 11:17 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109270925-alt1
- zh_cn.zip build 2011-09-27 09:25 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231252-alt1
- zh_cn.zip build 2011-09-23 12:52 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- zh_cn.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109180903-alt1
- zh_cn.zip build 2011-09-18 09:03 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109160250-alt1
- zh_cn.zip build 2011-09-16 02:50 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109140833-alt1
- zh_cn.zip build 2011-09-14 08:33 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109120755-alt1
- zh_cn.zip build 2011-09-12 07:55 UTC

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109090955-alt1
- zh_cn.zip build 2011-09-09 09:55 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109081131-alt1
- zh_cn.zip build 2011-09-08 11:31 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109070725-alt1
- zh_cn.zip build 2011-09-07 07:25 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108240815-alt1
- zh_cn.zip build 2011-08-24 08:15 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108231110-alt1
- zh_cn.zip build 2011-08-23 11:10 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108221302-alt1
- zh_cn.zip build 2011-08-22 13:02 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108190203-alt1
- zh_cn.zip build 2011-08-19 02:03 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108150558-alt1
- zh_cn.zip build 2011-08-15 05:58 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108130645-alt1
- zh_cn.zip build 2011-08-13 06:45 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108120108-alt1
- Rename package to moodle2.0-lang-zh_cn
- zh_cn.zip build 2011-08-12 01:08 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- zh_cn_utf8.zip build 2010-05-26

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20080526
- new build for ALT Linux from cvs
