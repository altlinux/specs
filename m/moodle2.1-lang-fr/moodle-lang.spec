# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename fr
%define packagversion 2.1.0
%define packagedate 201603181940
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname French
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-fr
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
* Mon Mar 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201603181940-alt1
- repocop cronbuild 20160321. At your service.
- fr.zip build 2016-03-18 19:40 UTC

* Sun Mar 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201603011007-alt1
- repocop cronbuild 20160306. At your service.
- fr.zip build 2016-03-01 10:07 UTC

* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201602161726-alt1
- repocop cronbuild 20160221. At your service.
- fr.zip build 2016-02-16 17:26 UTC

* Sun Feb 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201602041935-alt1
- repocop cronbuild 20160207. At your service.
- fr.zip build 2016-02-04 19:35 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201601182018-alt1
- repocop cronbuild 20160124. At your service.
- fr.zip build 2016-01-18 20:18 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201512110929-alt1
- repocop cronbuild 20151214. At your service.
- fr.zip build 2015-12-11 09:29 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201512051539-alt1
- repocop cronbuild 20151207. At your service.
- fr.zip build 2015-12-05 15:39 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511251513-alt1
- repocop cronbuild 20151130. At your service.
- fr.zip build 2015-11-25 15:13 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511201517-alt1
- repocop cronbuild 20151123. At your service.
- fr.zip build 2015-11-20 15:17 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511102030-alt1
- repocop cronbuild 20151116. At your service.
- fr.zip build 2015-11-10 20:30 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- fr.zip build 2015-11-08 22:20 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511011427-alt1
- repocop cronbuild 20151102. At your service.
- fr.zip build 2015-11-01 14:27 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201510221455-alt1
- repocop cronbuild 20151026. At your service.
- fr.zip build 2015-10-22 14:55 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201510131701-alt1
- repocop cronbuild 20151019. At your service.
- fr.zip build 2015-10-13 17:01 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201510081655-alt1
- repocop cronbuild 20151012. At your service.
- fr.zip build 2015-10-08 16:55 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201510031810-alt1
- repocop cronbuild 20151005. At your service.
- fr.zip build 2015-10-03 18:10 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201509101856-alt1
- repocop cronbuild 20150914. At your service.
- fr.zip build 2015-09-10 18:56 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201509011122-alt1
- repocop cronbuild 20150907. At your service.
- fr.zip build 2015-09-01 11:22 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201508181238-alt1
- repocop cronbuild 20150823. At your service.
- fr.zip build 2015-08-18 12:38 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507171445-alt1
- repocop cronbuild 20150723. At your service.
- fr.zip build 2015-07-17 14:45 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507091901-alt1
- repocop cronbuild 20150716. At your service.
- fr.zip build 2015-07-09 19:01 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507081406-alt1
- repocop cronbuild 20150709. At your service.
- fr.zip build 2015-07-08 14:06 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506191700-alt1
- repocop cronbuild 20150625. At your service.
- fr.zip build 2015-06-19 17:00 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506171644-alt1
- repocop cronbuild 20150618. At your service.
- fr.zip build 2015-06-17 16:44 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506101226-alt1
- repocop cronbuild 20150611. At your service.
- fr.zip build 2015-06-10 12:26 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201505291050-alt1
- repocop cronbuild 20150604. At your service.
- fr.zip build 2015-05-29 10:50 UTC

* Sat May 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201505221731-alt1
- repocop cronbuild 20150523. At your service.
- fr.zip build 2015-05-22 17:31 UTC

* Sat May 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201505151049-alt1
- repocop cronbuild 20150516. At your service.
- fr.zip build 2015-05-15 10:49 UTC

* Sat May 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504281816-alt1
- repocop cronbuild 20150502. At your service.
- fr.zip build 2015-04-28 18:16 UTC

* Sat Apr 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504240938-alt1
- repocop cronbuild 20150425. At your service.
- fr.zip build 2015-04-24 09:38 UTC

* Sat Apr 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504171333-alt1
- repocop cronbuild 20150418. At your service.
- fr.zip build 2015-04-17 13:33 UTC

* Sat Apr 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504101525-alt1
- repocop cronbuild 20150411. At your service.
- fr.zip build 2015-04-10 15:25 UTC

* Sat Apr 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504010845-alt1
- repocop cronbuild 20150404. At your service.
- fr.zip build 2015-04-01 08:45 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503261730-alt1
- repocop cronbuild 20150327. At your service.
- fr.zip build 2015-03-26 17:30 UTC

* Sat Mar 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503181746-alt1
- repocop cronbuild 20150321. At your service.
- fr.zip build 2015-03-18 17:46 UTC

* Sat Mar 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503121633-alt1
- repocop cronbuild 20150314. At your service.
- fr.zip build 2015-03-12 16:33 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503051223-alt1
- repocop cronbuild 20150306. At your service.
- fr.zip build 2015-03-05 12:23 UTC

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201502242123-alt1
- repocop cronbuild 20150228. At your service.
- fr.zip build 2015-02-24 21:23 UTC

* Sat Feb 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201502201224-alt1
- repocop cronbuild 20150221. At your service.
- fr.zip build 2015-02-20 12:24 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201502061740-alt1
- repocop cronbuild 20150207. At your service.
- fr.zip build 2015-02-06 17:40 UTC

* Sat Jan 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201501271706-alt1
- repocop cronbuild 20150131. At your service.
- fr.zip build 2015-01-27 17:06 UTC

* Sat Jan 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201501151836-alt1
- repocop cronbuild 20150117. At your service.
- fr.zip build 2015-01-15 18:36 UTC

* Sat Jan 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201501081832-alt1
- repocop cronbuild 20150110. At your service.
- fr.zip build 2015-01-08 18:32 UTC

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201412272211-alt1
- repocop cronbuild 20150102. At your service.
- fr.zip build 2014-12-27 22:11 UTC

* Sat Dec 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201412141328-alt1
- repocop cronbuild 20141220. At your service.
- fr.zip build 2014-12-14 13:28 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201412101552-alt1
- repocop cronbuild 20141212. At your service.
- fr.zip build 2014-12-10 15:52 UTC

* Sat Nov 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201411261746-alt1
- repocop cronbuild 20141129. At your service.
- fr.zip build 2014-11-26 17:46 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201411121550-alt1
- repocop cronbuild 20141114. At your service.
- fr.zip build 2014-11-12 15:50 UTC

* Sat Nov 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201411041655-alt1
- repocop cronbuild 20141108. At your service.
- fr.zip build 2014-11-04 16:55 UTC

* Fri Oct 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201410311655-alt1
- repocop cronbuild 20141031. At your service.
- fr.zip build 2014-10-31 16:55 UTC

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201410121255-alt1
- repocop cronbuild 20141018. At your service.
- fr.zip build 2014-10-12 12:55 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201410081107-alt1
- repocop cronbuild 20141011. At your service.
- fr.zip build 2014-10-08 11:07 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409281006-alt1
- repocop cronbuild 20141003. At your service.
- fr.zip build 2014-09-28 10:06 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409241618-alt1
- repocop cronbuild 20140927. At your service.
- fr.zip build 2014-09-24 16:18 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409171942-alt1
- repocop cronbuild 20140919. At your service.
- fr.zip build 2014-09-17 19:42 UTC

* Fri Sep 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409111636-alt1
- repocop cronbuild 20140912. At your service.
- fr.zip build 2014-09-11 16:36 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201407041435-alt1
- repocop cronbuild 20140705. At your service.
- fr.zip build 2014-07-04 14:35 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406201954-alt1
- repocop cronbuild 20140621. At your service.
- fr.zip build 2014-06-20 19:54 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406121638-alt1
- repocop cronbuild 20140613. At your service.
- fr.zip build 2014-06-12 16:38 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201405081822-alt1
- repocop cronbuild 20140509. At your service.
- fr.zip build 2014-05-08 18:22 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404261045-alt1
- repocop cronbuild 20140502. At your service.
- fr.zip build 2014-04-26 10:45 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404090950-alt1
- repocop cronbuild 20140411. At your service.
- fr.zip build 2014-04-09 09:50 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404031150-alt1
- repocop cronbuild 20140404. At your service.
- fr.zip build 2014-04-03 11:50 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403111720-alt1
- repocop cronbuild 20140314. At your service.
- fr.zip build 2014-03-11 17:20 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402241355-alt1
- repocop cronbuild 20140228. At your service.
- fr.zip build 2014-02-24 13:55 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401261237-alt1
- repocop cronbuild 20140131. At your service.
- fr.zip build 2014-01-26 12:37 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401230951-alt1
- repocop cronbuild 20140124. At your service.
- fr.zip build 2014-01-23 09:51 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401162024-alt1
- repocop cronbuild 20140117. At your service.
- fr.zip build 2014-01-16 20:24 UTC

* Fri Jan 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401041042-alt1
- repocop cronbuild 20140110. At your service.
- fr.zip build 2014-01-04 10:42 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312112023-alt1
- repocop cronbuild 20131213. At your service.
- fr.zip build 2013-12-11 20:23 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312011031-alt1
- repocop cronbuild 20131206. At your service.
- fr.zip build 2013-12-01 10:31 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311261619-alt1
- repocop cronbuild 20131129. At your service.
- fr.zip build 2013-11-26 16:19 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311162145-alt1
- repocop cronbuild 20131122. At your service.
- fr.zip build 2013-11-16 21:45 UTC

* Thu Nov 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311132017-alt1
- repocop cronbuild 20131114. At your service.
- fr.zip build 2013-11-13 20:17 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311010643-alt1
- repocop cronbuild 20131108. At your service.
- fr.zip build 2013-11-01 06:43 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310292034-alt1
- repocop cronbuild 20131101. At your service.
- fr.zip build 2013-10-29 20:34 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310170248-alt1
- repocop cronbuild 20131018. At your service.
- fr.zip build 2013-10-17 02:48 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310101302-alt1
- repocop cronbuild 20131011. At your service.
- fr.zip build 2013-10-10 13:02 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309141750-alt1
- repocop cronbuild 20130920. At your service.
- fr.zip build 2013-09-14 17:50 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308231112-alt1
- repocop cronbuild 20130830. At your service.
- fr.zip build 2013-08-23 11:12 UTC

* Fri Aug 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308221815-alt1
- repocop cronbuild 20130823. At your service.
- fr.zip build 2013-08-22 18:15 UTC

* Fri Aug 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308151627-alt1
- repocop cronbuild 20130816. At your service.
- fr.zip build 2013-08-15 16:27 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307101703-alt1
- repocop cronbuild 20130712. At your service.
- fr.zip build 2013-07-10 17:03 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307021726-alt1
- repocop cronbuild 20130705. At your service.
- fr.zip build 2013-07-02 17:26 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306261313-alt1
- repocop cronbuild 20130628. At your service.
- fr.zip build 2013-06-26 13:13 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306141603-alt1
- repocop cronbuild 20130621. At your service.
- fr.zip build 2013-06-14 16:03 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306131954-alt1
- repocop cronbuild 20130614. At your service.
- fr.zip build 2013-06-13 19:54 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305300956-alt1
- repocop cronbuild 20130531. At your service.
- fr.zip build 2013-05-30 09:56 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305221632-alt1
- repocop cronbuild 20130524. At your service.
- fr.zip build 2013-05-22 16:32 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305150858-alt1
- repocop cronbuild 20130517. At your service.
- fr.zip build 2013-05-15 08:58 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305040844-alt1
- repocop cronbuild 20130509. At your service.
- fr.zip build 2013-05-04 08:44 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201304121542-alt1
- repocop cronbuild 20130417. At your service.
- fr.zip build 2013-04-12 15:42 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303251657-alt1
- repocop cronbuild 20130327. At your service.
- fr.zip build 2013-03-25 16:57 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302271743-alt1
- repocop cronbuild 20130304. At your service.
- fr.zip build 2013-02-27 17:43 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302221221-alt1
- repocop cronbuild 20130225. At your service.
- fr.zip build 2013-02-22 12:21 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302151818-alt1
- repocop cronbuild 20130218. At your service.
- fr.zip build 2013-02-15 18:18 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302032132-alt1
- repocop cronbuild 20130204. At your service.
- fr.zip build 2013-02-03 21:32 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301261628-alt1
- repocop cronbuild 20130128. At your service.
- fr.zip build 2013-01-26 16:28 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212292101-alt1
- repocop cronbuild 20121231. At your service.
- fr.zip build 2012-12-29 21:01 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212211307-alt1
- repocop cronbuild 20121224. At your service.
- fr.zip build 2012-12-21 13:07 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212141605-alt1
- repocop cronbuild 20121217. At your service.
- fr.zip build 2012-12-14 16:05 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212062151-alt1
- repocop cronbuild 20121210. At your service.
- fr.zip build 2012-12-06 21:51 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211251634-alt1
- repocop cronbuild 20121126. At your service.
- fr.zip build 2012-11-25 16:34 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211151913-alt1
- repocop cronbuild 20121119. At your service.
- fr.zip build 2012-11-15 19:13 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211101918-alt1
- repocop cronbuild 20121112. At your service.
- fr.zip build 2012-11-10 19:18 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211041134-alt1
- repocop cronbuild 20121105. At your service.
- fr.zip build 2012-11-04 11:34 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210261733-alt1
- repocop cronbuild 20121029. At your service.
- fr.zip build 2012-10-26 17:33 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210190707-alt1
- repocop cronbuild 20121022. At your service.
- fr.zip build 2012-10-19 07:07 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210131448-alt1
- repocop cronbuild 20121015. At your service.
- fr.zip build 2012-10-13 14:48 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210012004-alt1
- repocop cronbuild 20121008. At your service.
- fr.zip build 2012-10-01 20:04 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209171957-alt1
- repocop cronbuild 20120918. At your service.
- fr.zip build 2012-09-17 19:57 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209061614-alt1
- repocop cronbuild 20120911. At your service.
- fr.zip build 2012-09-06 16:14 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208291442-alt1
- repocop cronbuild 20120904. At your service.
- fr.zip build 2012-08-29 14:42 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208161642-alt1
- repocop cronbuild 20120820. At your service.
- fr.zip build 2012-08-16 16:42 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207170802-alt1
- repocop cronbuild 20120724. At your service.
- fr.zip build 2012-07-17 08:02 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207161314-alt1
- repocop cronbuild 20120717. At your service.
- fr.zip build 2012-07-16 13:14 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207060642-alt1
- repocop cronbuild 20120710. At your service.
- fr.zip build 2012-07-06 06:42 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207021957-alt1
- repocop cronbuild 20120703. At your service.
- fr.zip build 2012-07-02 19:57 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206201454-alt1
- repocop cronbuild 20120626. At your service.
- fr.zip build 2012-06-20 14:54 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206161419-alt1
- repocop cronbuild 20120619. At your service.
- fr.zip build 2012-06-16 14:19 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206071356-alt1
- repocop cronbuild 20120612. At your service.
- fr.zip build 2012-06-07 13:56 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206031721-alt1
- repocop cronbuild 20120605. At your service.
- fr.zip build 2012-06-03 17:21 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205232031-alt1
- repocop cronbuild 20120529. At your service.
- fr.zip build 2012-05-23 20:31 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205200948-alt1
- repocop cronbuild 20120521. At your service.
- fr.zip build 2012-05-20 09:48 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205071515-alt1
- repocop cronbuild 20120507. At your service.
- fr.zip build 2012-05-07 15:15 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204271130-alt1
- repocop cronbuild 20120430. At your service.
- fr.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204231443-alt1
- repocop cronbuild 20120424. At your service.
- fr.zip build 2012-04-23 14:43 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204101256-alt1
- repocop cronbuild 20120417. At your service.
- fr.zip build 2012-04-10 12:56 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204061334-alt1
- repocop cronbuild 20120410. At your service.
- fr.zip build 2012-04-06 13:34 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204010956-alt1
- repocop cronbuild 20120403. At your service.
- fr.zip build 2012-04-01 09:56 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203201952-alt1
- repocop cronbuild 20120327. At your service.
- fr.zip build 2012-03-20 19:52 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203181809-alt1
- repocop cronbuild 20120320. At your service.
- fr.zip build 2012-03-18 18:09 UTC

* Thu Mar 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203061934-alt1
- repocop cronbuild 20120308. At your service.
- fr.zip build 2012-03-06 19:34 UTC

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120301. At your service.
- fr.zip build 2012-03-01 11:00 UTC

* Thu Feb 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202221009-alt1
- repocop cronbuild 20120223. At your service.
- fr.zip build 2012-02-22 10:09 UTC

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202111010-alt1
- repocop cronbuild 20120216. At your service.
- fr.zip build 2012-02-11 10:10 UTC

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202081935-alt1
- repocop cronbuild 20120209. At your service.
- fr.zip build 2012-02-08 19:35 UTC

* Thu Feb 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201302038-alt1
- repocop cronbuild 20120202. At your service.
- fr.zip build 2012-01-30 20:38 UTC

* Thu Jan 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201221740-alt1
- repocop cronbuild 20120126. At your service.
- fr.zip build 2012-01-22 17:40 UTC

* Thu Jan 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201121858-alt1
- repocop cronbuild 20120112. At your service.
- fr.zip build 2012-01-12 18:58 UTC

* Thu Jan 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201050916-alt1
- repocop cronbuild 20120105. At your service.
- fr.zip build 2012-01-05 09:16 UTC

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112192151-alt1
- repocop cronbuild 20111222. At your service.
- fr.zip build 2011-12-19 21:51 UTC

* Thu Dec 15 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091829-alt1
- repocop cronbuild 20111215. At your service.
- fr.zip build 2011-12-09 18:29 UTC

* Thu Dec 08 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112081249-alt1
- repocop cronbuild 20111208. At your service.
- fr.zip build 2011-12-08 12:49 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111251639-alt1
- repocop cronbuild 20111125. At your service.
- fr.zip build 2011-11-25 16:39 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111232006-alt1
- Rename package to moodle2.1-lang-fr
- fr.zip build 2011-11-23 20:06 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111232006-alt2
- Fix requires

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111232006-alt1
- repocop cronbuild 20111123. At your service.
- fr.zip build 2011-11-23 20:06 UTC

* Sun Nov 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111202140-alt1
- repocop cronbuild 20111120. At your service.
- fr.zip build 2011-11-20 21:40 UTC

* Sat Nov 19 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111191256-alt1
- repocop cronbuild 20111119. At your service.
- fr.zip build 2011-11-19 12:56 UTC

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111181223-alt1
- repocop cronbuild 20111118. At your service.
- fr.zip build 2011-11-18 12:23 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151942-alt1
- repocop cronbuild 20111116. At your service.
- fr.zip build 2011-11-15 19:42 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031917-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031917-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111031917-alt1
- repocop cronbuild 20111105. At your service.
- fr.zip build 2011-11-03 19:17 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt1
- fr.zip build 2011-10-12 18:40 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231534-alt1
- fr.zip build 2011-09-23 15:34 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109230935-alt1
- fr.zip build 2011-09-23 09:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109221808-alt1
- fr.zip build 2011-09-22 18:08 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- fr.zip build 2011-09-21 15:30 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109161112-alt1
- fr.zip build 2011-09-16 11:12 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109081534-alt1
- fr.zip build 2011-09-08 15:34 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109041828-alt1
- fr.zip build 2011-09-04 18:28 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108241508-alt1
- fr.zip build 2011-08-24 15:08 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108190836-alt1
- fr.zip build 2011-08-19 08:36 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- fr.zip build 2011-08-16 13:07 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108141034-alt1
- fr.zip build 2011-08-14 10:34 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-fr
- fr.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110718-alt1
- fr_utf8.zip build 2011-07-18

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081211
- new build for ALT Linux from cvs
