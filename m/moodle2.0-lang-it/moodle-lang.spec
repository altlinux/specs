# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename it
%define packagversion 2.0.0
%define packagedate 201602101829
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Italian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-it
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
* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602101829-alt1
- repocop cronbuild 20160214. At your service.
- it.zip build 2016-02-10 18:29 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601191116-alt1
- repocop cronbuild 20160124. At your service.
- it.zip build 2016-01-19 11:16 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512091752-alt1
- repocop cronbuild 20151214. At your service.
- it.zip build 2015-12-09 17:52 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511241756-alt1
- repocop cronbuild 20151130. At your service.
- it.zip build 2015-11-24 17:56 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511201210-alt1
- repocop cronbuild 20151123. At your service.
- it.zip build 2015-11-20 12:10 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510200957-alt1
- repocop cronbuild 20151026. At your service.
- it.zip build 2015-10-20 09:57 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510142125-alt1
- repocop cronbuild 20151019. At your service.
- it.zip build 2015-10-14 21:25 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508311601-alt1
- repocop cronbuild 20150907. At your service.
- it.zip build 2015-08-31 16:01 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508240819-alt1
- repocop cronbuild 20150831. At your service.
- it.zip build 2015-08-24 08:19 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507141410-alt1
- repocop cronbuild 20150716. At your service.
- it.zip build 2015-07-14 14:10 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507071144-alt1
- repocop cronbuild 20150709. At your service.
- it.zip build 2015-07-07 11:44 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505241649-alt1
- repocop cronbuild 20150604. At your service.
- it.zip build 2015-05-24 16:49 UTC

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505171546-alt1
- repocop cronbuild 20150522. At your service.
- it.zip build 2015-05-17 15:46 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505051211-alt1
- repocop cronbuild 20150508. At your service.
- it.zip build 2015-05-05 12:11 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504161408-alt1
- repocop cronbuild 20150417. At your service.
- it.zip build 2015-04-16 14:08 UTC

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503121257-alt1
- repocop cronbuild 20150313. At your service.
- it.zip build 2015-03-12 12:57 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502230911-alt1
- repocop cronbuild 20150227. At your service.
- it.zip build 2015-02-23 09:11 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502101128-alt1
- repocop cronbuild 20150213. At your service.
- it.zip build 2015-02-10 11:28 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502042014-alt1
- repocop cronbuild 20150206. At your service.
- it.zip build 2015-02-04 20:14 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501291843-alt1
- repocop cronbuild 20150130. At your service.
- it.zip build 2015-01-29 18:43 UTC

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501081001-alt1
- repocop cronbuild 20150109. At your service.
- it.zip build 2015-01-08 10:01 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412161359-alt1
- repocop cronbuild 20141219. At your service.
- it.zip build 2014-12-16 13:59 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412051320-alt1
- repocop cronbuild 20141211. At your service.
- it.zip build 2014-12-05 13:20 UTC

* Thu Nov 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411251305-alt1
- repocop cronbuild 20141127. At your service.
- it.zip build 2014-11-25 13:05 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411121503-alt1
- repocop cronbuild 20141114. At your service.
- it.zip build 2014-11-12 15:03 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411061905-alt1
- repocop cronbuild 20141107. At your service.
- it.zip build 2014-11-06 19:05 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410201458-alt1
- repocop cronbuild 20141024. At your service.
- it.zip build 2014-10-20 14:58 UTC

* Thu Oct 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410161357-alt1
- repocop cronbuild 20141016. At your service.
- it.zip build 2014-10-16 13:57 UTC

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409121517-alt1
- repocop cronbuild 20140918. At your service.
- it.zip build 2014-09-12 15:17 UTC

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201408281455-alt1
- repocop cronbuild 20140911. At your service.
- it.zip build 2014-08-28 14:55 UTC

* Mon Jun 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406241146-alt1
- repocop cronbuild 20140630. At your service.
- it.zip build 2014-06-24 11:46 UTC

* Tue Jun 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406221802-alt1
- repocop cronbuild 20140624. At your service.
- it.zip build 2014-06-22 18:02 UTC

* Tue Jun 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406100954-alt1
- repocop cronbuild 20140617. At your service.
- it.zip build 2014-06-10 09:54 UTC

* Sun May 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405171753-alt1
- repocop cronbuild 20140518. At your service.
- it.zip build 2014-05-17 17:53 UTC

* Sat May 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405091220-alt1
- repocop cronbuild 20140510. At your service.
- it.zip build 2014-05-09 12:20 UTC

* Sun May 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404301415-alt1
- repocop cronbuild 20140504. At your service.
- it.zip build 2014-04-30 14:15 UTC

* Sun Apr 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404241629-alt1
- repocop cronbuild 20140427. At your service.
- it.zip build 2014-04-24 16:29 UTC

* Sat Apr 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404171812-alt1
- repocop cronbuild 20140419. At your service.
- it.zip build 2014-04-17 18:12 UTC

* Sun Apr 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404110757-alt1
- repocop cronbuild 20140413. At your service.
- it.zip build 2014-04-11 07:57 UTC

* Sun Apr 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404041423-alt1
- repocop cronbuild 20140406. At your service.
- it.zip build 2014-04-04 14:23 UTC

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403281428-alt1
- repocop cronbuild 20140329. At your service.
- it.zip build 2014-03-28 14:28 UTC

* Sun Mar 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403211218-alt1
- repocop cronbuild 20140323. At your service.
- it.zip build 2014-03-21 12:18 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403131449-alt1
- repocop cronbuild 20140314. At your service.
- it.zip build 2014-03-13 14:49 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402271705-alt1
- repocop cronbuild 20140301. At your service.
- it.zip build 2014-02-27 17:05 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402201251-alt1
- repocop cronbuild 20140221. At your service.
- it.zip build 2014-02-20 12:51 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402131405-alt1
- repocop cronbuild 20140215. At your service.
- it.zip build 2014-02-13 14:05 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312191125-alt1
- repocop cronbuild 20131220. At your service.
- it.zip build 2013-12-19 11:25 UTC

* Sat Dec 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312101435-alt1
- repocop cronbuild 20131214. At your service.
- it.zip build 2013-12-10 14:35 UTC

* Sat Nov 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311151715-alt1
- repocop cronbuild 20131116. At your service.
- it.zip build 2013-11-15 17:15 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311071445-alt1
- repocop cronbuild 20131108. At your service.
- it.zip build 2013-11-07 14:45 UTC

* Sat Nov 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311010955-alt1
- repocop cronbuild 20131102. At your service.
- it.zip build 2013-11-01 09:55 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310231043-alt1
- repocop cronbuild 20131025. At your service.
- it.zip build 2013-10-23 10:43 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310170633-alt1
- repocop cronbuild 20131018. At your service.
- it.zip build 2013-10-17 06:33 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309201709-alt1
- repocop cronbuild 20130927. At your service.
- it.zip build 2013-09-20 17:09 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309161440-alt1
- repocop cronbuild 20130920. At your service.
- it.zip build 2013-09-16 14:40 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309051323-alt1
- repocop cronbuild 20130906. At your service.
- it.zip build 2013-09-05 13:23 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308010808-alt1
- repocop cronbuild 20130802. At your service.
- it.zip build 2013-08-01 08:08 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307181352-alt1
- repocop cronbuild 20130719. At your service.
- it.zip build 2013-07-18 13:52 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306261309-alt1
- repocop cronbuild 20130628. At your service.
- it.zip build 2013-06-26 13:09 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306201303-alt1
- repocop cronbuild 20130621. At your service.
- it.zip build 2013-06-20 13:03 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306131019-alt1
- repocop cronbuild 20130614. At your service.
- it.zip build 2013-06-13 10:19 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306041142-alt1
- repocop cronbuild 20130607. At your service.
- it.zip build 2013-06-04 11:42 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305301307-alt1
- repocop cronbuild 20130531. At your service.
- it.zip build 2013-05-30 13:07 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305211103-alt1
- repocop cronbuild 20130524. At your service.
- it.zip build 2013-05-21 11:03 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305160843-alt1
- repocop cronbuild 20130517. At your service.
- it.zip build 2013-05-16 08:43 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305021315-alt1
- repocop cronbuild 20130509. At your service.
- it.zip build 2013-05-02 13:15 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303251222-alt1
- repocop cronbuild 20130327. At your service.
- it.zip build 2013-03-25 12:22 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303151252-alt1
- repocop cronbuild 20130319. At your service.
- it.zip build 2013-03-15 12:52 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303111859-alt1
- repocop cronbuild 20130313. At your service.
- it.zip build 2013-03-11 18:59 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303011426-alt1
- repocop cronbuild 20130304. At your service.
- it.zip build 2013-03-01 14:26 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302211359-alt1
- repocop cronbuild 20130225. At your service.
- it.zip build 2013-02-21 13:59 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302151335-alt1
- repocop cronbuild 20130218. At your service.
- it.zip build 2013-02-15 13:35 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302081433-alt1
- repocop cronbuild 20130211. At your service.
- it.zip build 2013-02-08 14:33 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302011046-alt1
- repocop cronbuild 20130204. At your service.
- it.zip build 2013-02-01 10:46 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301231613-alt1
- repocop cronbuild 20130128. At your service.
- it.zip build 2013-01-23 16:13 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301181315-alt1
- repocop cronbuild 20130121. At your service.
- it.zip build 2013-01-18 13:15 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212311346-alt1
- repocop cronbuild 20130107. At your service.
- it.zip build 2012-12-31 13:46 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212190813-alt1
- repocop cronbuild 20121224. At your service.
- it.zip build 2012-12-19 08:13 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212031348-alt1
- repocop cronbuild 20121210. At your service.
- it.zip build 2012-12-03 13:48 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211052054-alt1
- repocop cronbuild 20121112. At your service.
- it.zip build 2012-11-05 20:54 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211020958-alt1
- repocop cronbuild 20121105. At your service.
- it.zip build 2012-11-02 09:58 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210261809-alt1
- repocop cronbuild 20121029. At your service.
- it.zip build 2012-10-26 18:09 UTC

* Sun Oct 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210191639-alt1
- repocop cronbuild 20121021. At your service.
- it.zip build 2012-10-19 16:39 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209281743-alt1
- repocop cronbuild 20121001. At your service.
- it.zip build 2012-09-28 17:43 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209031500-alt1
- repocop cronbuild 20120904. At your service.
- it.zip build 2012-09-03 15:00 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208271704-alt1
- repocop cronbuild 20120828. At your service.
- it.zip build 2012-08-27 17:04 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207181247-alt1
- repocop cronbuild 20120724. At your service.
- it.zip build 2012-07-18 12:47 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207060938-alt1
- repocop cronbuild 20120709. At your service.
- it.zip build 2012-07-06 09:38 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206221655-alt1
- repocop cronbuild 20120625. At your service.
- it.zip build 2012-06-22 16:55 UTC

* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206111010-alt1
- repocop cronbuild 20120611. At your service.
- it.zip build 2012-06-11 10:10 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205301541-alt1
- repocop cronbuild 20120604. At your service.
- it.zip build 2012-05-30 15:41 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231549-alt1
- repocop cronbuild 20120528. At your service.
- it.zip build 2012-05-23 15:49 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205020915-alt1
- repocop cronbuild 20120507. At your service.
- it.zip build 2012-05-02 09:15 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204260714-alt1
- repocop cronbuild 20120430. At your service.
- it.zip build 2012-04-26 07:14 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204201050-alt1
- repocop cronbuild 20120423. At your service.
- it.zip build 2012-04-20 10:50 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204130751-alt1
- repocop cronbuild 20120416. At your service.
- it.zip build 2012-04-13 07:51 UTC

* Mon Apr 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204051431-alt1
- repocop cronbuild 20120409. At your service.
- it.zip build 2012-04-05 14:31 UTC

* Mon Mar 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203261748-alt1
- repocop cronbuild 20120326. At your service.
- it.zip build 2012-03-26 17:48 UTC

* Mon Mar 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203071224-alt1
- repocop cronbuild 20120312. At your service.
- it.zip build 2012-03-07 12:24 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203021451-alt1
- repocop cronbuild 20120306. At your service.
- it.zip build 2012-03-02 14:51 UTC

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202171607-alt1
- repocop cronbuild 20120221. At your service.
- it.zip build 2012-02-17 16:07 UTC

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202130752-alt1
- repocop cronbuild 20120214. At your service.
- it.zip build 2012-02-13 07:52 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201301101-alt1
- repocop cronbuild 20120131. At your service.
- it.zip build 2012-01-30 11:01 UTC

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201131805-alt1
- repocop cronbuild 20120117. At your service.
- it.zip build 2012-01-13 18:05 UTC

* Tue Jan 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201091024-alt1
- repocop cronbuild 20120110. At your service.
- it.zip build 2012-01-09 10:24 UTC

* Tue Jan 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112281450-alt1
- repocop cronbuild 20120103. At your service.
- it.zip build 2011-12-28 14:50 UTC

* Tue Dec 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112271712-alt1
- repocop cronbuild 20111227. At your service.
- it.zip build 2011-12-27 17:12 UTC

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112151056-alt1
- repocop cronbuild 20111220. At your service.
- it.zip build 2011-12-15 10:56 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112131442-alt1
- repocop cronbuild 20111213. At your service.
- it.zip build 2011-12-13 14:42 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111211610-alt2
- Fix requires

* Mon Nov 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111211610-alt1
- repocop cronbuild 20111121. At your service.
- it.zip build 2011-11-21 16:10 UTC

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111171327-alt1
- repocop cronbuild 20111118. At your service.
- it.zip build 2011-11-17 13:27 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151304-alt1
- repocop cronbuild 20111116. At your service.
- it.zip build 2011-11-15 13:04 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111041554-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111041554-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111041554-alt1
- repocop cronbuild 20111105. At your service.
- it.zip build 2011-11-04 15:54 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201547-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201547-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110201547-alt1
- it.zip build 2011-10-20 15:47 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110051735-alt1
- it.zip build 2011-10-05 17:35 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231416-alt1
- it.zip build 2011-09-23 14:16 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- it.zip build 2011-09-21 15:30 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141727-alt1
- it.zip build 2011-09-14 17:27 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109131401-alt1
- it.zip build 2011-09-13 14:01 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109121617-alt1
- it.zip build 2011-09-12 16:17 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109071500-alt1
- it.zip build 2011-09-07 15:00 UTC

* Wed Aug 17 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- it.zip build 2011-08-16 13:07 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-it
- it.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110319-alt1
- it_utf8.zip build 2011-03-19

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081204
- new build for ALT Linux from cvs
