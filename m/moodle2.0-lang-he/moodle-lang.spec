# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename he
%define packagversion 2.0.0
%define packagedate 201602251812
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Hebrew
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-he
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.0
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.0
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
* Sun Feb 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602251812-alt1
- repocop cronbuild 20160228. At your service.
- he.zip build 2016-02-25 18:12 UTC

* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602201631-alt1
- repocop cronbuild 20160221. At your service.
- he.zip build 2016-02-20 16:31 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601271714-alt1
- repocop cronbuild 20160131. At your service.
- he.zip build 2016-01-27 17:14 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601231712-alt1
- repocop cronbuild 20160124. At your service.
- he.zip build 2016-01-23 17:12 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512132149-alt1
- repocop cronbuild 20151214. At your service.
- he.zip build 2015-12-13 21:49 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512041459-alt1
- repocop cronbuild 20151207. At your service.
- he.zip build 2015-12-04 14:59 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511291520-alt1
- repocop cronbuild 20151130. At your service.
- he.zip build 2015-11-29 15:20 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511121829-alt1
- repocop cronbuild 20151116. At your service.
- he.zip build 2015-11-12 18:29 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- he.zip build 2015-11-08 22:20 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511010943-alt1
- repocop cronbuild 20151102. At your service.
- he.zip build 2015-11-01 09:43 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510060817-alt1
- repocop cronbuild 20151012. At your service.
- he.zip build 2015-10-06 08:17 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510021448-alt1
- repocop cronbuild 20151005. At your service.
- he.zip build 2015-10-02 14:48 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509271223-alt1
- repocop cronbuild 20150928. At your service.
- he.zip build 2015-09-27 12:23 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509202201-alt1
- repocop cronbuild 20150921. At your service.
- he.zip build 2015-09-20 22:01 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509101428-alt1
- repocop cronbuild 20150914. At your service.
- he.zip build 2015-09-10 14:28 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509041650-alt1
- repocop cronbuild 20150907. At your service.
- he.zip build 2015-09-04 16:50 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508291815-alt1
- repocop cronbuild 20150831. At your service.
- he.zip build 2015-08-29 18:15 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508171713-alt1
- repocop cronbuild 20150823. At your service.
- he.zip build 2015-08-17 17:13 UTC

* Fri Jul 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507060841-alt1
- repocop cronbuild 20150710. At your service.
- he.zip build 2015-07-06 08:41 UTC

* Sat Jul 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506271731-alt1
- repocop cronbuild 20150704. At your service.
- he.zip build 2015-06-27 17:31 UTC

* Fri Jun 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506252136-alt1
- repocop cronbuild 20150626. At your service.
- he.zip build 2015-06-25 21:36 UTC

* Fri Jun 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506161310-alt1
- repocop cronbuild 20150619. At your service.
- he.zip build 2015-06-16 13:10 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506100743-alt1
- repocop cronbuild 20150611. At your service.
- he.zip build 2015-06-10 07:43 UTC

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505191305-alt1
- repocop cronbuild 20150522. At your service.
- he.zip build 2015-05-19 13:05 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505051739-alt1
- repocop cronbuild 20150508. At your service.
- he.zip build 2015-05-05 17:39 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504241149-alt1
- repocop cronbuild 20150501. At your service.
- he.zip build 2015-04-24 11:49 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504091305-alt1
- repocop cronbuild 20150410. At your service.
- he.zip build 2015-04-09 13:05 UTC

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503111249-alt1
- repocop cronbuild 20150313. At your service.
- he.zip build 2015-03-11 12:49 UTC

* Thu Feb 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502151218-alt1
- repocop cronbuild 20150219. At your service.
- he.zip build 2015-02-15 12:18 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502082108-alt1
- repocop cronbuild 20150213. At your service.
- he.zip build 2015-02-08 21:08 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501291013-alt1
- repocop cronbuild 20150130. At your service.
- he.zip build 2015-01-29 10:13 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412091234-alt1
- repocop cronbuild 20141211. At your service.
- he.zip build 2014-12-09 12:34 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410190457-alt1
- repocop cronbuild 20141024. At your service.
- he.zip build 2014-10-19 04:57 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410041859-alt1
- repocop cronbuild 20141010. At your service.
- he.zip build 2014-10-04 18:59 UTC

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409131148-alt1
- repocop cronbuild 20140918. At your service.
- he.zip build 2014-09-13 11:48 UTC

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409111907-alt1
- repocop cronbuild 20140911. At your service.
- he.zip build 2014-09-11 19:07 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406291359-alt1
- repocop cronbuild 20140705. At your service.
- he.zip build 2014-06-29 13:59 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406161229-alt1
- repocop cronbuild 20140621. At your service.
- he.zip build 2014-06-16 12:29 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405140645-alt1
- repocop cronbuild 20140516. At your service.
- he.zip build 2014-05-14 06:45 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404221811-alt1
- repocop cronbuild 20140425. At your service.
- he.zip build 2014-04-22 18:11 UTC

* Sat Apr 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404181340-alt1
- repocop cronbuild 20140419. At your service.
- he.zip build 2014-04-18 13:40 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404100701-alt1
- repocop cronbuild 20140411. At your service.
- he.zip build 2014-04-10 07:01 UTC

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403261520-alt1
- repocop cronbuild 20140329. At your service.
- he.zip build 2014-03-26 15:20 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403192048-alt1
- repocop cronbuild 20140321. At your service.
- he.zip build 2014-03-19 20:48 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403091056-alt1
- repocop cronbuild 20140314. At your service.
- he.zip build 2014-03-09 10:56 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402240959-alt1
- repocop cronbuild 20140301. At your service.
- he.zip build 2014-02-24 09:59 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402192055-alt1
- repocop cronbuild 20140221. At your service.
- he.zip build 2014-02-19 20:55 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402122243-alt1
- repocop cronbuild 20140215. At your service.
- he.zip build 2014-02-12 22:43 UTC

* Sat Feb 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402041916-alt1
- repocop cronbuild 20140208. At your service.
- he.zip build 2014-02-04 19:16 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312191430-alt1
- repocop cronbuild 20131220. At your service.
- he.zip build 2013-12-19 14:30 UTC

* Sat Dec 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312101437-alt1
- repocop cronbuild 20131214. At your service.
- he.zip build 2013-12-10 14:37 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312052218-alt1
- repocop cronbuild 20131206. At your service.
- he.zip build 2013-12-05 22:18 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311281648-alt1
- repocop cronbuild 20131129. At your service.
- he.zip build 2013-11-28 16:48 UTC

* Sat Nov 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311202059-alt1
- repocop cronbuild 20131123. At your service.
- he.zip build 2013-11-20 20:59 UTC

* Sat Nov 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311091854-alt1
- repocop cronbuild 20131116. At your service.
- he.zip build 2013-11-09 18:54 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311060633-alt1
- repocop cronbuild 20131108. At your service.
- he.zip build 2013-11-06 06:33 UTC

* Sat Nov 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310271407-alt1
- repocop cronbuild 20131102. At your service.
- he.zip build 2013-10-27 14:07 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310232049-alt1
- repocop cronbuild 20131025. At your service.
- he.zip build 2013-10-23 20:49 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310171423-alt1
- repocop cronbuild 20131018. At your service.
- he.zip build 2013-10-17 14:23 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310082016-alt1
- repocop cronbuild 20131011. At your service.
- he.zip build 2013-10-08 20:16 UTC

* Thu Oct 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309281944-alt1
- repocop cronbuild 20131003. At your service.
- he.zip build 2013-09-28 19:44 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309261830-alt1
- repocop cronbuild 20130927. At your service.
- he.zip build 2013-09-26 18:30 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309192014-alt1
- repocop cronbuild 20130920. At your service.
- he.zip build 2013-09-19 20:14 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309101213-alt1
- repocop cronbuild 20130913. At your service.
- he.zip build 2013-09-10 12:13 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308251134-alt1
- repocop cronbuild 20130830. At your service.
- he.zip build 2013-08-25 11:34 UTC

* Thu Aug 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308221251-alt1
- repocop cronbuild 20130822. At your service.
- he.zip build 2013-08-22 12:51 UTC

* Fri Aug 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308152202-alt1
- repocop cronbuild 20130816. At your service.
- he.zip build 2013-08-15 22:02 UTC

* Fri Aug 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308041620-alt1
- repocop cronbuild 20130809. At your service.
- he.zip build 2013-08-04 16:20 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307301202-alt1
- repocop cronbuild 20130802. At your service.
- he.zip build 2013-07-30 12:02 UTC

* Fri Jul 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307251950-alt1
- repocop cronbuild 20130726. At your service.
- he.zip build 2013-07-25 19:50 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307181808-alt1
- repocop cronbuild 20130719. At your service.
- he.zip build 2013-07-18 18:08 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307081315-alt1
- repocop cronbuild 20130712. At your service.
- he.zip build 2013-07-08 13:15 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306301432-alt1
- repocop cronbuild 20130705. At your service.
- he.zip build 2013-06-30 14:32 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306190606-alt1
- repocop cronbuild 20130621. At your service.
- he.zip build 2013-06-19 06:06 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306081312-alt1
- repocop cronbuild 20130614. At your service.
- he.zip build 2013-06-08 13:12 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306060925-alt1
- repocop cronbuild 20130607. At your service.
- he.zip build 2013-06-06 09:25 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305292019-alt1
- repocop cronbuild 20130531. At your service.
- he.zip build 2013-05-29 20:19 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305211220-alt1
- repocop cronbuild 20130524. At your service.
- he.zip build 2013-05-21 12:20 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305151639-alt1
- repocop cronbuild 20130517. At your service.
- he.zip build 2013-05-15 16:39 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305082151-alt1
- repocop cronbuild 20130509. At your service.
- he.zip build 2013-05-08 21:51 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304161834-alt1
- repocop cronbuild 20130417. At your service.
- he.zip build 2013-04-16 18:34 UTC

* Tue Apr 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304091432-alt1
- repocop cronbuild 20130409. At your service.
- he.zip build 2013-04-09 14:32 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303261728-alt1
- repocop cronbuild 20130327. At your service.
- he.zip build 2013-03-26 17:28 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303181403-alt1
- repocop cronbuild 20130319. At your service.
- he.zip build 2013-03-18 14:03 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303091000-alt1
- repocop cronbuild 20130313. At your service.
- he.zip build 2013-03-09 10:00 UTC

* Tue Mar 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302271941-alt1
- repocop cronbuild 20130305. At your service.
- he.zip build 2013-02-27 19:41 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302242006-alt1
- repocop cronbuild 20130225. At your service.
- he.zip build 2013-02-24 20:06 UTC

* Tue Feb 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302161236-alt1
- repocop cronbuild 20130219. At your service.
- he.zip build 2013-02-16 12:36 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302110934-alt1
- repocop cronbuild 20130211. At your service.
- he.zip build 2013-02-11 09:34 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302041304-alt1
- repocop cronbuild 20130204. At your service.
- he.zip build 2013-02-04 13:04 UTC

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301281146-alt1
- repocop cronbuild 20130129. At your service.
- he.zip build 2013-01-28 11:46 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301150745-alt1
- repocop cronbuild 20130121. At your service.
- he.zip build 2013-01-15 07:45 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301131914-alt1
- repocop cronbuild 20130114. At your service.
- he.zip build 2013-01-13 19:14 UTC

* Tue Jan 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301052242-alt1
- repocop cronbuild 20130108. At your service.
- he.zip build 2013-01-05 22:42 UTC

* Tue Jan 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212292102-alt1
- repocop cronbuild 20130101. At your service.
- he.zip build 2012-12-29 21:02 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212231956-alt1
- repocop cronbuild 20121224. At your service.
- he.zip build 2012-12-23 19:56 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212171113-alt1
- repocop cronbuild 20121217. At your service.
- he.zip build 2012-12-17 11:13 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212101059-alt1
- repocop cronbuild 20121210. At your service.
- he.zip build 2012-12-10 10:59 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212032243-alt1
- repocop cronbuild 20121203. At your service.
- he.zip build 2012-12-03 22:43 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211251416-alt1
- repocop cronbuild 20121126. At your service.
- he.zip build 2012-11-25 14:16 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211152351-alt1
- repocop cronbuild 20121119. At your service.
- he.zip build 2012-11-15 23:51 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211071628-alt1
- repocop cronbuild 20121112. At your service.
- he.zip build 2012-11-07 16:28 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211041626-alt1
- repocop cronbuild 20121105. At your service.
- he.zip build 2012-11-04 16:26 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210282116-alt1
- repocop cronbuild 20121029. At your service.
- he.zip build 2012-10-28 21:16 UTC

* Sun Oct 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210142202-alt1
- repocop cronbuild 20121021. At your service.
- he.zip build 2012-10-14 22:02 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210142111-alt1
- repocop cronbuild 20121015. At your service.
- he.zip build 2012-10-14 21:11 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210071916-alt1
- repocop cronbuild 20121008. At your service.
- he.zip build 2012-10-07 19:16 UTC

* Sun Sep 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209301959-alt1
- repocop cronbuild 20120930. At your service.
- he.zip build 2012-09-30 19:59 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209141008-alt1
- repocop cronbuild 20120917. At your service.
- he.zip build 2012-09-14 10:08 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209091236-alt1
- repocop cronbuild 20120910. At your service.
- he.zip build 2012-09-09 12:36 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209021231-alt1
- repocop cronbuild 20120904. At your service.
- he.zip build 2012-09-02 12:31 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208150907-alt1
- repocop cronbuild 20120820. At your service.
- he.zip build 2012-08-15 09:07 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208071733-alt1
- repocop cronbuild 20120814. At your service.
- he.zip build 2012-08-07 17:33 UTC

* Mon Aug 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208061421-alt1
- repocop cronbuild 20120806. At your service.
- he.zip build 2012-08-06 14:21 UTC

* Mon Jul 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207241404-alt1
- repocop cronbuild 20120730. At your service.
- he.zip build 2012-07-24 14:04 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207231251-alt1
- repocop cronbuild 20120724. At your service.
- he.zip build 2012-07-23 12:51 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207151041-alt1
- repocop cronbuild 20120717. At your service.
- he.zip build 2012-07-15 10:41 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207050503-alt1
- repocop cronbuild 20120709. At your service.
- he.zip build 2012-07-05 05:03 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206211348-alt1
- repocop cronbuild 20120625. At your service.
- he.zip build 2012-06-21 13:48 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206181011-alt1
- repocop cronbuild 20120618. At your service.
- he.zip build 2012-06-18 10:11 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205291334-alt1
- repocop cronbuild 20120604. At your service.
- he.zip build 2012-05-29 13:34 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205241019-alt1
- repocop cronbuild 20120528. At your service.
- he.zip build 2012-05-24 10:19 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205150820-alt1
- repocop cronbuild 20120521. At your service.
- he.zip build 2012-05-15 08:20 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204301329-alt1
- repocop cronbuild 20120430. At your service.
- he.zip build 2012-04-30 13:29 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204151134-alt1
- repocop cronbuild 20120416. At your service.
- he.zip build 2012-04-15 11:34 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204021200-alt1
- repocop cronbuild 20120402. At your service.
- he.zip build 2012-04-02 12:00 UTC

* Mon Mar 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203221542-alt1
- repocop cronbuild 20120326. At your service.
- he.zip build 2012-03-22 15:42 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203191430-alt1
- repocop cronbuild 20120319. At your service.
- he.zip build 2012-03-19 14:30 UTC

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202161217-alt1
- repocop cronbuild 20120221. At your service.
- he.zip build 2012-02-16 12:17 UTC

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202141411-alt1
- repocop cronbuild 20120214. At your service.
- he.zip build 2012-02-14 14:11 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201261241-alt1
- repocop cronbuild 20120131. At your service.
- he.zip build 2012-01-26 12:41 UTC

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201191320-alt1
- repocop cronbuild 20120124. At your service.
- he.zip build 2012-01-19 13:20 UTC

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201171128-alt1
- repocop cronbuild 20120117. At your service.
- he.zip build 2012-01-17 11:28 UTC

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112190920-alt1
- repocop cronbuild 20111220. At your service.
- he.zip build 2011-12-19 09:20 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112061333-alt1
- repocop cronbuild 20111206. At your service.
- he.zip build 2011-12-06 13:33 UTC

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
