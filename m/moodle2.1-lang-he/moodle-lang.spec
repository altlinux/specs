# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename he
%define packagversion 2.1.0
%define packagedate 201603041542
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Hebrew
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-he
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.1
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.1
Provides: %moodle_name-%packagetype-%packagename-version = %packagedate
Provides: %moodle_name-%packagetype-%packagename = %version-%release
Provides: %moodle_name-%packagetype-%oldpackagename = %version-%release
Conflicts: %moodle_name-%packagetype-%packagename < %version
Conflicts: %moodle_name-%packagetype-%oldpackagename < %version

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses

%description
%summary

%prep
%setup

%build

%install
mkdir -p  %buildroot%moodle_langdir/
cp -rp * %buildroot%moodle_langdir/

%files
%moodle_langdir/*

%changelog
* Sun Mar 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201603041542-alt1
- repocop cronbuild 20160306. At your service.
- he.zip build 2016-03-04 15:42 UTC

* Sun Feb 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201602251812-alt1
- repocop cronbuild 20160228. At your service.
- he.zip build 2016-02-25 18:12 UTC

* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201602201631-alt1
- repocop cronbuild 20160221. At your service.
- he.zip build 2016-02-20 16:31 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201601271714-alt1
- repocop cronbuild 20160131. At your service.
- he.zip build 2016-01-27 17:14 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201601231712-alt1
- repocop cronbuild 20160124. At your service.
- he.zip build 2016-01-23 17:12 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201512132149-alt1
- repocop cronbuild 20151214. At your service.
- he.zip build 2015-12-13 21:49 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201512051040-alt1
- repocop cronbuild 20151207. At your service.
- he.zip build 2015-12-05 10:40 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511291523-alt1
- repocop cronbuild 20151130. At your service.
- he.zip build 2015-11-29 15:23 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511121829-alt1
- repocop cronbuild 20151116. At your service.
- he.zip build 2015-11-12 18:29 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- he.zip build 2015-11-08 22:20 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511010943-alt1
- repocop cronbuild 20151102. At your service.
- he.zip build 2015-11-01 09:43 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201510060817-alt1
- repocop cronbuild 20151012. At your service.
- he.zip build 2015-10-06 08:17 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201510021448-alt1
- repocop cronbuild 20151005. At your service.
- he.zip build 2015-10-02 14:48 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201509271223-alt1
- repocop cronbuild 20150928. At your service.
- he.zip build 2015-09-27 12:23 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201509202201-alt1
- repocop cronbuild 20150921. At your service.
- he.zip build 2015-09-20 22:01 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201509101428-alt1
- repocop cronbuild 20150914. At your service.
- he.zip build 2015-09-10 14:28 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201509051547-alt1
- repocop cronbuild 20150907. At your service.
- he.zip build 2015-09-05 15:47 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201508291815-alt1
- repocop cronbuild 20150831. At your service.
- he.zip build 2015-08-29 18:15 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201508171713-alt1
- repocop cronbuild 20150823. At your service.
- he.zip build 2015-08-17 17:13 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507292215-alt1
- repocop cronbuild 20150730. At your service.
- he.zip build 2015-07-29 22:15 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507060841-alt1
- repocop cronbuild 20150709. At your service.
- he.zip build 2015-07-06 08:41 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506281103-alt1
- repocop cronbuild 20150702. At your service.
- he.zip build 2015-06-28 11:03 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506212001-alt1
- repocop cronbuild 20150625. At your service.
- he.zip build 2015-06-21 20:01 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506161310-alt1
- repocop cronbuild 20150618. At your service.
- he.zip build 2015-06-16 13:10 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506100743-alt1
- repocop cronbuild 20150611. At your service.
- he.zip build 2015-06-10 07:43 UTC

* Sat May 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201505191305-alt1
- repocop cronbuild 20150523. At your service.
- he.zip build 2015-05-19 13:05 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201505051739-alt1
- repocop cronbuild 20150508. At your service.
- he.zip build 2015-05-05 17:39 UTC

* Sat Apr 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504241149-alt1
- repocop cronbuild 20150425. At your service.
- he.zip build 2015-04-24 11:49 UTC

* Sat Apr 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504091305-alt1
- repocop cronbuild 20150411. At your service.
- he.zip build 2015-04-09 13:05 UTC

* Sat Mar 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503111249-alt1
- repocop cronbuild 20150314. At your service.
- he.zip build 2015-03-11 12:49 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503061555-alt1
- repocop cronbuild 20150306. At your service.
- he.zip build 2015-03-06 15:55 UTC

* Sat Feb 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201502151218-alt1
- repocop cronbuild 20150221. At your service.
- he.zip build 2015-02-15 12:18 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201502082108-alt1
- repocop cronbuild 20150213. At your service.
- he.zip build 2015-02-08 21:08 UTC

* Sat Jan 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201501291013-alt1
- repocop cronbuild 20150131. At your service.
- he.zip build 2015-01-29 10:13 UTC

* Sat Dec 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201412151226-alt1
- repocop cronbuild 20141220. At your service.
- he.zip build 2014-12-15 12:26 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201412091234-alt1
- repocop cronbuild 20141212. At your service.
- he.zip build 2014-12-09 12:34 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201410190457-alt1
- repocop cronbuild 20141024. At your service.
- he.zip build 2014-10-19 04:57 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201410041859-alt1
- repocop cronbuild 20141011. At your service.
- he.zip build 2014-10-04 18:59 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409131148-alt1
- repocop cronbuild 20140919. At your service.
- he.zip build 2014-09-13 11:48 UTC

* Fri Sep 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409111907-alt1
- repocop cronbuild 20140912. At your service.
- he.zip build 2014-09-11 19:07 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406291359-alt1
- repocop cronbuild 20140705. At your service.
- he.zip build 2014-06-29 13:59 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406250842-alt1
- repocop cronbuild 20140628. At your service.
- he.zip build 2014-06-25 08:42 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406161229-alt1
- repocop cronbuild 20140621. At your service.
- he.zip build 2014-06-16 12:29 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406042345-alt1
- repocop cronbuild 20140606. At your service.
- he.zip build 2014-06-04 23:45 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201405140645-alt1
- repocop cronbuild 20140516. At your service.
- he.zip build 2014-05-14 06:45 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404280627-alt1
- repocop cronbuild 20140502. At your service.
- he.zip build 2014-04-28 06:27 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404221811-alt1
- repocop cronbuild 20140425. At your service.
- he.zip build 2014-04-22 18:11 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404171458-alt1
- repocop cronbuild 20140418. At your service.
- he.zip build 2014-04-17 14:58 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404100702-alt1
- repocop cronbuild 20140411. At your service.
- he.zip build 2014-04-10 07:02 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403261520-alt1
- repocop cronbuild 20140328. At your service.
- he.zip build 2014-03-26 15:20 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403192048-alt1
- repocop cronbuild 20140321. At your service.
- he.zip build 2014-03-19 20:48 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403091056-alt1
- repocop cronbuild 20140314. At your service.
- he.zip build 2014-03-09 10:56 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403051052-alt1
- repocop cronbuild 20140307. At your service.
- he.zip build 2014-03-05 10:52 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402240959-alt1
- repocop cronbuild 20140228. At your service.
- he.zip build 2014-02-24 09:59 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402192055-alt1
- repocop cronbuild 20140221. At your service.
- he.zip build 2014-02-19 20:55 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402122243-alt1
- repocop cronbuild 20140214. At your service.
- he.zip build 2014-02-12 22:43 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402041916-alt1
- repocop cronbuild 20140207. At your service.
- he.zip build 2014-02-04 19:16 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401241238-alt1
- repocop cronbuild 20140131. At your service.
- he.zip build 2014-01-24 12:38 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401211711-alt1
- repocop cronbuild 20140124. At your service.
- he.zip build 2014-01-21 17:11 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401141819-alt1
- repocop cronbuild 20140117. At your service.
- he.zip build 2014-01-14 18:19 UTC

* Fri Jan 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401041417-alt1
- repocop cronbuild 20140110. At your service.
- he.zip build 2014-01-04 14:17 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312271922-alt1
- repocop cronbuild 20140103. At your service.
- he.zip build 2013-12-27 19:22 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312240954-alt1
- repocop cronbuild 20131227. At your service.
- he.zip build 2013-12-24 09:54 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312101437-alt1
- repocop cronbuild 20131213. At your service.
- he.zip build 2013-12-10 14:37 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312052218-alt1
- repocop cronbuild 20131206. At your service.
- he.zip build 2013-12-05 22:18 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311281648-alt1
- repocop cronbuild 20131129. At your service.
- he.zip build 2013-11-28 16:48 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311202059-alt1
- repocop cronbuild 20131122. At your service.
- he.zip build 2013-11-20 20:59 UTC

* Thu Nov 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311091854-alt1
- repocop cronbuild 20131114. At your service.
- he.zip build 2013-11-09 18:54 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311060633-alt1
- repocop cronbuild 20131108. At your service.
- he.zip build 2013-11-06 06:33 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310271407-alt1
- repocop cronbuild 20131101. At your service.
- he.zip build 2013-10-27 14:07 UTC

* Thu Oct 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310232049-alt1
- repocop cronbuild 20131024. At your service.
- he.zip build 2013-10-23 20:49 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310171423-alt1
- repocop cronbuild 20131018. At your service.
- he.zip build 2013-10-17 14:23 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310082016-alt1
- repocop cronbuild 20131011. At your service.
- he.zip build 2013-10-08 20:16 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309281944-alt1
- repocop cronbuild 20131004. At your service.
- he.zip build 2013-09-28 19:44 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309261830-alt1
- repocop cronbuild 20130927. At your service.
- he.zip build 2013-09-26 18:30 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309192014-alt1
- repocop cronbuild 20130920. At your service.
- he.zip build 2013-09-19 20:14 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309101213-alt1
- repocop cronbuild 20130913. At your service.
- he.zip build 2013-09-10 12:13 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308281357-alt1
- repocop cronbuild 20130830. At your service.
- he.zip build 2013-08-28 13:57 UTC

* Fri Aug 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308221251-alt1
- repocop cronbuild 20130823. At your service.
- he.zip build 2013-08-22 12:51 UTC

* Fri Aug 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308152202-alt1
- repocop cronbuild 20130816. At your service.
- he.zip build 2013-08-15 22:02 UTC

* Fri Aug 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308041620-alt1
- repocop cronbuild 20130809. At your service.
- he.zip build 2013-08-04 16:20 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307301202-alt1
- repocop cronbuild 20130802. At your service.
- he.zip build 2013-07-30 12:02 UTC

* Fri Jul 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307251950-alt1
- repocop cronbuild 20130726. At your service.
- he.zip build 2013-07-25 19:50 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307181808-alt1
- repocop cronbuild 20130719. At your service.
- he.zip build 2013-07-18 18:08 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307081315-alt1
- repocop cronbuild 20130712. At your service.
- he.zip build 2013-07-08 13:15 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306301432-alt1
- repocop cronbuild 20130705. At your service.
- he.zip build 2013-06-30 14:32 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306190606-alt1
- repocop cronbuild 20130621. At your service.
- he.zip build 2013-06-19 06:06 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306081312-alt1
- repocop cronbuild 20130614. At your service.
- he.zip build 2013-06-08 13:12 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306061147-alt1
- repocop cronbuild 20130607. At your service.
- he.zip build 2013-06-06 11:47 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305292019-alt1
- repocop cronbuild 20130531. At your service.
- he.zip build 2013-05-29 20:19 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305211302-alt1
- repocop cronbuild 20130524. At your service.
- he.zip build 2013-05-21 13:02 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305151639-alt1
- repocop cronbuild 20130517. At your service.
- he.zip build 2013-05-15 16:39 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305082151-alt1
- repocop cronbuild 20130509. At your service.
- he.zip build 2013-05-08 21:51 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201304161834-alt1
- repocop cronbuild 20130417. At your service.
- he.zip build 2013-04-16 18:34 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201304091432-alt1
- repocop cronbuild 20130410. At your service.
- he.zip build 2013-04-09 14:32 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303310944-alt1
- repocop cronbuild 20130403. At your service.
- he.zip build 2013-03-31 09:44 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303261728-alt1
- repocop cronbuild 20130327. At your service.
- he.zip build 2013-03-26 17:28 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303181403-alt1
- repocop cronbuild 20130320. At your service.
- he.zip build 2013-03-18 14:03 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303091000-alt1
- repocop cronbuild 20130313. At your service.
- he.zip build 2013-03-09 10:00 UTC

* Tue Mar 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302271941-alt1
- repocop cronbuild 20130305. At your service.
- he.zip build 2013-02-27 19:41 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302242006-alt1
- repocop cronbuild 20130225. At your service.
- he.zip build 2013-02-24 20:06 UTC

* Tue Feb 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302161236-alt1
- repocop cronbuild 20130219. At your service.
- he.zip build 2013-02-16 12:36 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302110934-alt1
- repocop cronbuild 20130211. At your service.
- he.zip build 2013-02-11 09:34 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302041304-alt1
- repocop cronbuild 20130204. At your service.
- he.zip build 2013-02-04 13:04 UTC

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301281146-alt1
- repocop cronbuild 20130129. At your service.
- he.zip build 2013-01-28 11:46 UTC

* Tue Jan 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301150745-alt1
- repocop cronbuild 20130122. At your service.
- he.zip build 2013-01-15 07:45 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301131923-alt1
- repocop cronbuild 20130114. At your service.
- he.zip build 2013-01-13 19:23 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301052242-alt1
- repocop cronbuild 20130107. At your service.
- he.zip build 2013-01-05 22:42 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212302114-alt1
- repocop cronbuild 20121231. At your service.
- he.zip build 2012-12-30 21:14 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212231956-alt1
- repocop cronbuild 20121224. At your service.
- he.zip build 2012-12-23 19:56 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212160757-alt1
- repocop cronbuild 20121217. At your service.
- he.zip build 2012-12-16 07:57 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212092217-alt1
- repocop cronbuild 20121210. At your service.
- he.zip build 2012-12-09 22:17 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211281120-alt1
- repocop cronbuild 20121203. At your service.
- he.zip build 2012-11-28 11:20 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211251416-alt1
- repocop cronbuild 20121126. At your service.
- he.zip build 2012-11-25 14:16 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211152351-alt1
- repocop cronbuild 20121119. At your service.
- he.zip build 2012-11-15 23:51 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211071628-alt1
- repocop cronbuild 20121112. At your service.
- he.zip build 2012-11-07 16:28 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211041626-alt1
- repocop cronbuild 20121105. At your service.
- he.zip build 2012-11-04 16:26 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210282116-alt1
- repocop cronbuild 20121029. At your service.
- he.zip build 2012-10-28 21:16 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210151801-alt1
- repocop cronbuild 20121022. At your service.
- he.zip build 2012-10-15 18:01 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210142202-alt1
- repocop cronbuild 20121015. At your service.
- he.zip build 2012-10-14 22:02 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210071916-alt1
- repocop cronbuild 20121008. At your service.
- he.zip build 2012-10-07 19:16 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209301959-alt1
- repocop cronbuild 20121001. At your service.
- he.zip build 2012-09-30 19:59 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209141008-alt1
- repocop cronbuild 20120918. At your service.
- he.zip build 2012-09-14 10:08 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209091236-alt1
- repocop cronbuild 20120911. At your service.
- he.zip build 2012-09-09 12:36 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209021231-alt1
- repocop cronbuild 20120904. At your service.
- he.zip build 2012-09-02 12:31 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208150907-alt1
- repocop cronbuild 20120820. At your service.
- he.zip build 2012-08-15 09:07 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208071733-alt1
- repocop cronbuild 20120814. At your service.
- he.zip build 2012-08-07 17:33 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208061421-alt1
- repocop cronbuild 20120807. At your service.
- he.zip build 2012-08-06 14:21 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207241404-alt1
- repocop cronbuild 20120731. At your service.
- he.zip build 2012-07-24 14:04 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207231251-alt1
- repocop cronbuild 20120724. At your service.
- he.zip build 2012-07-23 12:51 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207151041-alt1
- repocop cronbuild 20120717. At your service.
- he.zip build 2012-07-15 10:41 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207050503-alt1
- repocop cronbuild 20120710. At your service.
- he.zip build 2012-07-05 05:03 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206211348-alt1
- repocop cronbuild 20120626. At your service.
- he.zip build 2012-06-21 13:48 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206181011-alt1
- repocop cronbuild 20120619. At your service.
- he.zip build 2012-06-18 10:11 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205291334-alt1
- repocop cronbuild 20120605. At your service.
- he.zip build 2012-05-29 13:34 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205241019-alt1
- repocop cronbuild 20120529. At your service.
- he.zip build 2012-05-24 10:19 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205150820-alt1
- repocop cronbuild 20120521. At your service.
- he.zip build 2012-05-15 08:20 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204301329-alt1
- repocop cronbuild 20120430. At your service.
- he.zip build 2012-04-30 13:29 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204151134-alt1
- repocop cronbuild 20120417. At your service.
- he.zip build 2012-04-15 11:34 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204021200-alt1
- repocop cronbuild 20120403. At your service.
- he.zip build 2012-04-02 12:00 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203221542-alt1
- repocop cronbuild 20120327. At your service.
- he.zip build 2012-03-22 15:42 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203191430-alt1
- repocop cronbuild 20120320. At your service.
- he.zip build 2012-03-19 14:30 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203060922-alt1
- repocop cronbuild 20120306. At your service.
- he.zip build 2012-03-06 09:22 UTC

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202161217-alt1
- repocop cronbuild 20120221. At your service.
- he.zip build 2012-02-16 12:17 UTC

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202141443-alt1
- repocop cronbuild 20120214. At your service.
- he.zip build 2012-02-14 14:43 UTC

* Tue Feb 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202061439-alt1
- repocop cronbuild 20120207. At your service.
- he.zip build 2012-02-06 14:39 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201261241-alt1
- repocop cronbuild 20120131. At your service.
- he.zip build 2012-01-26 12:41 UTC

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201191327-alt1
- repocop cronbuild 20120124. At your service.
- he.zip build 2012-01-19 13:27 UTC

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201171128-alt1
- repocop cronbuild 20120117. At your service.
- he.zip build 2012-01-17 11:28 UTC

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112190920-alt1
- repocop cronbuild 20111220. At your service.
- he.zip build 2011-12-19 09:20 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111213. At your service.
- he.zip build 2011-12-09 16:00 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112061435-alt1
- repocop cronbuild 20111206. At your service.
- he.zip build 2011-12-06 14:35 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111241405-alt1
- Rename package to moodle2.1-lang-he
- he.zip build 2011-11-24 14:05

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111201348-alt2
- Fix requires

* Sun Nov 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111201348-alt1
- repocop cronbuild 20111120. At your service.
- he.zip build 2011-11-20 13:48 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111101425-alt1
- repocop cronbuild 20111116. At your service.
- he.zip build 2011-11-10 14:25 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- he.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- he.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-he
- he.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110804-alt1
- he_utf8.zip build 2011-08-04
- initial build for ALT Linux Sisyphus
