# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename it
%define packagversion 2.4.0
%define packagedate 201603021721
%define moodlebranch 2.4
%define moodlepackagename %moodle_name%moodlebranch
%define langname Italian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.4-lang-it
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.4
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.4
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
* Sun Mar 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201603021721-alt1
- repocop cronbuild 20160306. At your service.
- it.zip build 2016-03-02 17:21 UTC

* Sun Feb 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201602261418-alt1
- repocop cronbuild 20160228. At your service.
- it.zip build 2016-02-26 14:18 UTC

* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201602101829-alt1
- repocop cronbuild 20160214. At your service.
- it.zip build 2016-02-10 18:29 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201601251730-alt1
- repocop cronbuild 20160131. At your service.
- it.zip build 2016-01-25 17:30 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201601191332-alt1
- repocop cronbuild 20160124. At your service.
- it.zip build 2016-01-19 13:32 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201512091752-alt1
- repocop cronbuild 20151214. At your service.
- it.zip build 2015-12-09 17:52 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511241756-alt1
- repocop cronbuild 20151130. At your service.
- it.zip build 2015-11-24 17:56 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511201210-alt1
- repocop cronbuild 20151123. At your service.
- it.zip build 2015-11-20 12:10 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511111029-alt1
- repocop cronbuild 20151116. At your service.
- it.zip build 2015-11-11 10:29 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510291204-alt1
- repocop cronbuild 20151102. At your service.
- it.zip build 2015-10-29 12:04 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510231704-alt1
- repocop cronbuild 20151026. At your service.
- it.zip build 2015-10-23 17:04 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510142125-alt1
- repocop cronbuild 20151019. At your service.
- it.zip build 2015-10-14 21:25 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510021753-alt1
- repocop cronbuild 20151005. At your service.
- it.zip build 2015-10-02 17:53 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201508311601-alt1
- repocop cronbuild 20150907. At your service.
- it.zip build 2015-08-31 16:01 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201508271133-alt1
- repocop cronbuild 20150831. At your service.
- it.zip build 2015-08-27 11:33 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507301744-alt1
- repocop cronbuild 20150823. At your service.
- it.zip build 2015-07-30 17:44 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507141410-alt1
- repocop cronbuild 20150716. At your service.
- it.zip build 2015-07-14 14:10 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507071144-alt1
- repocop cronbuild 20150709. At your service.
- it.zip build 2015-07-07 11:44 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505241649-alt1
- repocop cronbuild 20150604. At your service.
- it.zip build 2015-05-24 16:49 UTC

* Sat May 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505171546-alt1
- repocop cronbuild 20150523. At your service.
- it.zip build 2015-05-17 15:46 UTC

* Sat May 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505051211-alt1
- repocop cronbuild 20150509. At your service.
- it.zip build 2015-05-05 12:11 UTC

* Sat May 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504271054-alt1
- repocop cronbuild 20150502. At your service.
- it.zip build 2015-04-27 10:54 UTC

* Sat Apr 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504161408-alt1
- repocop cronbuild 20150418. At your service.
- it.zip build 2015-04-16 14:08 UTC

* Sat Apr 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504070809-alt1
- repocop cronbuild 20150411. At your service.
- it.zip build 2015-04-07 08:09 UTC

* Sat Mar 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201503121257-alt1
- repocop cronbuild 20150314. At your service.
- it.zip build 2015-03-12 12:57 UTC

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502230911-alt1
- repocop cronbuild 20150228. At your service.
- it.zip build 2015-02-23 09:11 UTC

* Sat Feb 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502101128-alt1
- repocop cronbuild 20150214. At your service.
- it.zip build 2015-02-10 11:28 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502042014-alt1
- repocop cronbuild 20150207. At your service.
- it.zip build 2015-02-04 20:14 UTC

* Sat Jan 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501291843-alt1
- repocop cronbuild 20150131. At your service.
- it.zip build 2015-01-29 18:43 UTC

* Sat Jan 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501121650-alt1
- repocop cronbuild 20150117. At your service.
- it.zip build 2015-01-12 16:50 UTC

* Sat Jan 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501081001-alt1
- repocop cronbuild 20150110. At your service.
- it.zip build 2015-01-08 10:01 UTC

* Sat Dec 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412161359-alt1
- repocop cronbuild 20141220. At your service.
- it.zip build 2014-12-16 13:59 UTC

* Sat Dec 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412051320-alt1
- repocop cronbuild 20141206. At your service.
- it.zip build 2014-12-05 13:20 UTC

* Sat Nov 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201411251305-alt1
- repocop cronbuild 20141129. At your service.
- it.zip build 2014-11-25 13:05 UTC

* Sat Nov 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201411121503-alt1
- repocop cronbuild 20141115. At your service.
- it.zip build 2014-11-12 15:03 UTC

* Sat Nov 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201411071437-alt1
- repocop cronbuild 20141108. At your service.
- it.zip build 2014-11-07 14:37 UTC

* Sat Oct 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201410201458-alt1
- repocop cronbuild 20141025. At your service.
- it.zip build 2014-10-20 14:58 UTC

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201410161418-alt1
- repocop cronbuild 20141018. At your service.
- it.zip build 2014-10-16 14:18 UTC

* Sat Oct 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201409300800-alt1
- repocop cronbuild 20141004. At your service.
- it.zip build 2014-09-30 08:00 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201409231324-alt1
- repocop cronbuild 20140927. At your service.
- it.zip build 2014-09-23 13:24 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201409121531-alt1
- repocop cronbuild 20140913. At your service.
- it.zip build 2014-09-12 15:31 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406261452-alt1
- repocop cronbuild 20140628. At your service.
- it.zip build 2014-06-26 14:52 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406112128-alt1
- repocop cronbuild 20140613. At your service.
- it.zip build 2014-06-11 21:28 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405281145-alt1
- repocop cronbuild 20140530. At your service.
- it.zip build 2014-05-28 11:45 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405171753-alt1
- repocop cronbuild 20140523. At your service.
- it.zip build 2014-05-17 17:53 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405121430-alt1
- repocop cronbuild 20140516. At your service.
- it.zip build 2014-05-12 14:30 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405051727-alt1
- repocop cronbuild 20140509. At your service.
- it.zip build 2014-05-05 17:27 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404301415-alt1
- repocop cronbuild 20140502. At your service.
- it.zip build 2014-04-30 14:15 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404241629-alt1
- repocop cronbuild 20140425. At your service.
- it.zip build 2014-04-24 16:29 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404171812-alt1
- repocop cronbuild 20140418. At your service.
- it.zip build 2014-04-17 18:12 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404110757-alt1
- repocop cronbuild 20140411. At your service.
- it.zip build 2014-04-11 07:57 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404031146-alt1
- repocop cronbuild 20140404. At your service.
- it.zip build 2014-04-03 11:46 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403221508-alt1
- repocop cronbuild 20140328. At your service.
- it.zip build 2014-03-22 15:08 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403190908-alt1
- repocop cronbuild 20140321. At your service.
- it.zip build 2014-03-19 09:08 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403131531-alt1
- repocop cronbuild 20140314. At your service.
- it.zip build 2014-03-13 15:31 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402271705-alt1
- repocop cronbuild 20140228. At your service.
- it.zip build 2014-02-27 17:05 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402201251-alt1
- repocop cronbuild 20140221. At your service.
- it.zip build 2014-02-20 12:51 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402131405-alt1
- repocop cronbuild 20140214. At your service.
- it.zip build 2014-02-13 14:05 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402011851-alt1
- repocop cronbuild 20140207. At your service.
- it.zip build 2014-02-01 18:51 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401251520-alt1
- repocop cronbuild 20140131. At your service.
- it.zip build 2014-01-25 15:20 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401222047-alt1
- repocop cronbuild 20140124. At your service.
- it.zip build 2014-01-22 20:47 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401141344-alt1
- repocop cronbuild 20140117. At your service.
- it.zip build 2014-01-14 13:44 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312191125-alt1
- repocop cronbuild 20131220. At your service.
- it.zip build 2013-12-19 11:25 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312101435-alt1
- repocop cronbuild 20131213. At your service.
- it.zip build 2013-12-10 14:35 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312051219-alt1
- repocop cronbuild 20131206. At your service.
- it.zip build 2013-12-05 12:19 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311251451-alt1
- repocop cronbuild 20131129. At your service.
- it.zip build 2013-11-25 14:51 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311151715-alt1
- repocop cronbuild 20131122. At your service.
- it.zip build 2013-11-15 17:15 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311120821-alt1
- repocop cronbuild 20131115. At your service.
- it.zip build 2013-11-12 08:21 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311071445-alt1
- repocop cronbuild 20131108. At your service.
- it.zip build 2013-11-07 14:45 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311010955-alt1
- repocop cronbuild 20131101. At your service.
- it.zip build 2013-11-01 09:55 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310231043-alt1
- repocop cronbuild 20131025. At your service.
- it.zip build 2013-10-23 10:43 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310170633-alt1
- repocop cronbuild 20131018. At your service.
- it.zip build 2013-10-17 06:33 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309271803-alt1
- repocop cronbuild 20131004. At your service.
- it.zip build 2013-09-27 18:03 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309241139-alt1
- repocop cronbuild 20130927. At your service.
- it.zip build 2013-09-24 11:39 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309161441-alt1
- repocop cronbuild 20130920. At your service.
- it.zip build 2013-09-16 14:41 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309051323-alt1
- repocop cronbuild 20130906. At your service.
- it.zip build 2013-09-05 13:23 UTC

* Fri Aug 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308191323-alt1
- repocop cronbuild 20130823. At your service.
- it.zip build 2013-08-19 13:23 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308010808-alt1
- repocop cronbuild 20130802. At your service.
- it.zip build 2013-08-01 08:08 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307181352-alt1
- repocop cronbuild 20130719. At your service.
- it.zip build 2013-07-18 13:52 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307091025-alt1
- repocop cronbuild 20130712. At your service.
- it.zip build 2013-07-09 10:25 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306261309-alt1
- repocop cronbuild 20130628. At your service.
- it.zip build 2013-06-26 13:09 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306200820-alt1
- repocop cronbuild 20130621. At your service.
- it.zip build 2013-06-20 08:20 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306131019-alt1
- repocop cronbuild 20130614. At your service.
- it.zip build 2013-06-13 10:19 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306060654-alt1
- repocop cronbuild 20130607. At your service.
- it.zip build 2013-06-06 06:54 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305301307-alt1
- repocop cronbuild 20130531. At your service.
- it.zip build 2013-05-30 13:07 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221013-alt1
- repocop cronbuild 20130524. At your service.
- it.zip build 2013-05-22 10:13 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305160843-alt1
- repocop cronbuild 20130517. At your service.
- it.zip build 2013-05-16 08:43 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305021315-alt1
- repocop cronbuild 20130509. At your service.
- it.zip build 2013-05-02 13:15 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304101622-alt1
- Rename package to moodle2.4-lang-it
- it.zip build 2013-04-10 16:22 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304051026-alt1
- repocop cronbuild 20130410. At your service.
- it.zip build 2013-04-05 10:26 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303291309-alt1
- repocop cronbuild 20130403. At your service.
- it.zip build 2013-03-29 13:09 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303251222-alt1
- repocop cronbuild 20130327. At your service.
- it.zip build 2013-03-25 12:22 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303151252-alt1
- repocop cronbuild 20130320. At your service.
- it.zip build 2013-03-15 12:52 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303111859-alt1
- repocop cronbuild 20130313. At your service.
- it.zip build 2013-03-11 18:59 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303011426-alt1
- repocop cronbuild 20130304. At your service.
- it.zip build 2013-03-01 14:26 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302211359-alt1
- repocop cronbuild 20130225. At your service.
- it.zip build 2013-02-21 13:59 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302151335-alt1
- repocop cronbuild 20130218. At your service.
- it.zip build 2013-02-15 13:35 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302081433-alt1
- repocop cronbuild 20130211. At your service.
- it.zip build 2013-02-08 14:33 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302011046-alt1
- repocop cronbuild 20130204. At your service.
- it.zip build 2013-02-01 10:46 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301231613-alt1
- repocop cronbuild 20130128. At your service.
- it.zip build 2013-01-23 16:13 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301181315-alt1
- repocop cronbuild 20130121. At your service.
- it.zip build 2013-01-18 13:15 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212311346-alt1
- repocop cronbuild 20130107. At your service.
- it.zip build 2012-12-31 13:46 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212190813-alt1
- repocop cronbuild 20121224. At your service.
- it.zip build 2012-12-19 08:13 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212071927-alt1
- repocop cronbuild 20121210. At your service.
- it.zip build 2012-12-07 19:27 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211060906-alt1
- repocop cronbuild 20121112. At your service.
- it.zip build 2012-11-06 09:06 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211021123-alt1
- repocop cronbuild 20121105. At your service.
- it.zip build 2012-11-02 11:23 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210261809-alt1
- repocop cronbuild 20121029. At your service.
- it.zip build 2012-10-26 18:09 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210191639-alt1
- repocop cronbuild 20121022. At your service.
- it.zip build 2012-10-19 16:39 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210110758-alt1
- repocop cronbuild 20121015. At your service.
- it.zip build 2012-10-11 07:58 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209281743-alt1
- repocop cronbuild 20121001. At your service.
- it.zip build 2012-09-28 17:43 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209071509-alt1
- repocop cronbuild 20120911. At your service.
- it.zip build 2012-09-07 15:09 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209031500-alt1
- repocop cronbuild 20120904. At your service.
- it.zip build 2012-09-03 15:00 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208271939-alt1
- repocop cronbuild 20120828. At your service.
- it.zip build 2012-08-27 19:39 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208031044-alt1
- repocop cronbuild 20120807. At your service.
- it.zip build 2012-08-03 10:44 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207181247-alt1
- repocop cronbuild 20120724. At your service.
- it.zip build 2012-07-18 12:47 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207111821-alt1
- repocop cronbuild 20120717. At your service.
- it.zip build 2012-07-11 18:21 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207060935-alt1
- repocop cronbuild 20120710. At your service.
- it.zip build 2012-07-06 09:35 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207031105-alt1
- repocop cronbuild 20120703. At your service.
- it.zip build 2012-07-03 11:05 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206221655-alt1
- repocop cronbuild 20120626. At your service.
- it.zip build 2012-06-22 16:55 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191525-alt1
- repocop cronbuild 20120619. At your service.
- it.zip build 2012-06-19 15:25 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121428-alt1
- repocop cronbuild 20120612. At your service.
- it.zip build 2012-06-12 14:28 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205301541-alt1
- repocop cronbuild 20120605. At your service.
- it.zip build 2012-05-30 15:41 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205290808-alt1
- repocop cronbuild 20120529. At your service.
- it.zip build 2012-05-29 08:08 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205191740-alt1
- repocop cronbuild 20120522. At your service.
- it.zip build 2012-05-19 17:40 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111113-alt1
- repocop cronbuild 20120515. At your service.
- it.zip build 2012-05-11 11:13 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205020921-alt1
- repocop cronbuild 20120508. At your service.
- it.zip build 2012-05-02 09:21 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- it.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204241332-alt1
- repocop cronbuild 20120424. At your service.
- it.zip build 2012-04-24 13:32 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204130750-alt1
- repocop cronbuild 20120417. At your service.
- it.zip build 2012-04-13 07:50 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204051529-alt1
- repocop cronbuild 20120410. At your service.
- it.zip build 2012-04-05 15:29 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203261748-alt1
- repocop cronbuild 20120327. At your service.
- it.zip build 2012-03-26 17:48 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203151213-alt1
- Rename package to moodle2.2-lang-it
- it.zip build 2012-03-15 12:13 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203151213-alt1
- repocop cronbuild 20120320. At your service.
- it.zip build 2012-03-15 12:13 UTC

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203071224-alt1
- repocop cronbuild 20120309. At your service.
- it.zip build 2012-03-07 12:24 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203021637-alt1
- repocop cronbuild 20120302. At your service.
- it.zip build 2012-03-02 16:37 UTC

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202171607-alt1
- repocop cronbuild 20120217. At your service.
- it.zip build 2012-02-17 16:07 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202091352-alt1
- repocop cronbuild 20120210. At your service.
- it.zip build 2012-02-09 13:52 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201301101-alt1
- repocop cronbuild 20120203. At your service.
- it.zip build 2012-01-30 11:01 UTC

* Fri Jan 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201271320-alt1
- repocop cronbuild 20120127. At your service.
- it.zip build 2012-01-27 13:20 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201201425-alt1
- repocop cronbuild 20120120. At your service.
- it.zip build 2012-01-20 14:25 UTC

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201131805-alt1
- repocop cronbuild 20120113. At your service.
- it.zip build 2012-01-13 18:05 UTC

* Fri Dec 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112281450-alt1
- repocop cronbuild 20111230. At your service.
- it.zip build 2011-12-28 14:50 UTC

* Fri Dec 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112231732-alt1
- repocop cronbuild 20111223. At your service.
- it.zip build 2011-12-23 17:32 UTC

* Fri Dec 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112151055-alt1
- repocop cronbuild 20111216. At your service.
- it.zip build 2011-12-15 10:55 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- it.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111231825-alt1
- Rename package to moodle2.1-lang-it
- it.zip build 2011-11-23 18:25

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
