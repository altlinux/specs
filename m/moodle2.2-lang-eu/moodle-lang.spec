# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename eu
%define packagversion 2.2.0
%define packagedate 201601260806
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Basque
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-eu
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.2
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.2
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
* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201601260806-alt1
- repocop cronbuild 20160131. At your service.
- eu.zip build 2016-01-26 08:06 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201601191011-alt1
- repocop cronbuild 20160124. At your service.
- eu.zip build 2016-01-19 10:11 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201512101524-alt1
- repocop cronbuild 20151214. At your service.
- eu.zip build 2015-12-10 15:24 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201512021634-alt1
- repocop cronbuild 20151207. At your service.
- eu.zip build 2015-12-02 16:34 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511261605-alt1
- repocop cronbuild 20151130. At your service.
- eu.zip build 2015-11-26 16:05 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511191134-alt1
- repocop cronbuild 20151123. At your service.
- eu.zip build 2015-11-19 11:34 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511091553-alt1
- repocop cronbuild 20151116. At your service.
- eu.zip build 2015-11-09 15:53 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- eu.zip build 2015-11-08 22:20 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510290821-alt1
- repocop cronbuild 20151102. At your service.
- eu.zip build 2015-10-29 08:21 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510150658-alt1
- repocop cronbuild 20151019. At your service.
- eu.zip build 2015-10-15 06:58 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201509250735-alt1
- repocop cronbuild 20150928. At your service.
- eu.zip build 2015-09-25 07:35 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201509181040-alt1
- repocop cronbuild 20150921. At your service.
- eu.zip build 2015-09-18 10:40 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201509070707-alt1
- repocop cronbuild 20150907. At your service.
- eu.zip build 2015-09-07 07:07 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201508070810-alt1
- repocop cronbuild 20150823. At your service.
- eu.zip build 2015-08-07 08:10 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201507020857-alt1
- repocop cronbuild 20150702. At your service.
- eu.zip build 2015-07-02 08:57 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201506241357-alt1
- repocop cronbuild 20150625. At your service.
- eu.zip build 2015-06-24 13:57 UTC

* Sat May 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201505050853-alt1
- repocop cronbuild 20150509. At your service.
- eu.zip build 2015-05-05 08:53 UTC

* Sat Apr 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201504221005-alt1
- repocop cronbuild 20150425. At your service.
- eu.zip build 2015-04-22 10:05 UTC

* Sat Apr 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201504160953-alt1
- repocop cronbuild 20150418. At your service.
- eu.zip build 2015-04-16 09:53 UTC

* Sat Mar 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201503261055-alt1
- repocop cronbuild 20150328. At your service.
- eu.zip build 2015-03-26 10:55 UTC

* Sat Mar 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201503021613-alt1
- repocop cronbuild 20150307. At your service.
- eu.zip build 2015-03-02 16:13 UTC

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502270747-alt1
- repocop cronbuild 20150228. At your service.
- eu.zip build 2015-02-27 07:47 UTC

* Sat Feb 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502121454-alt1
- repocop cronbuild 20150214. At your service.
- eu.zip build 2015-02-12 14:54 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502061110-alt1
- repocop cronbuild 20150207. At your service.
- eu.zip build 2015-02-06 11:10 UTC

* Sat Jan 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501290907-alt1
- repocop cronbuild 20150131. At your service.
- eu.zip build 2015-01-29 09:07 UTC

* Sat Jan 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501231029-alt1
- repocop cronbuild 20150124. At your service.
- eu.zip build 2015-01-23 10:29 UTC

* Sat Jan 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501161119-alt1
- repocop cronbuild 20150117. At your service.
- eu.zip build 2015-01-16 11:19 UTC

* Sat Jan 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201501081613-alt1
- repocop cronbuild 20150110. At your service.
- eu.zip build 2015-01-08 16:13 UTC

* Sat Dec 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412171507-alt1
- repocop cronbuild 20141220. At your service.
- eu.zip build 2014-12-17 15:07 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412121024-alt1
- repocop cronbuild 20141212. At your service.
- eu.zip build 2014-12-12 10:24 UTC

* Sat Nov 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201411271122-alt1
- repocop cronbuild 20141129. At your service.
- eu.zip build 2014-11-27 11:22 UTC

* Sat Nov 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201411121551-alt1
- repocop cronbuild 20141115. At your service.
- eu.zip build 2014-11-12 15:51 UTC

* Sat Nov 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201411060950-alt1
- repocop cronbuild 20141108. At your service.
- eu.zip build 2014-11-06 09:50 UTC

* Sat Oct 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410020824-alt1
- repocop cronbuild 20141004. At your service.
- eu.zip build 2014-10-02 08:24 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409260714-alt1
- repocop cronbuild 20140927. At your service.
- eu.zip build 2014-09-26 07:14 UTC

* Sat Sep 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409160902-alt1
- repocop cronbuild 20140920. At your service.
- eu.zip build 2014-09-16 09:02 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409120857-alt1
- repocop cronbuild 20140913. At your service.
- eu.zip build 2014-09-12 08:57 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201406101524-alt1
- repocop cronbuild 20140613. At your service.
- eu.zip build 2014-06-10 15:24 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201405201250-alt1
- repocop cronbuild 20140530. At your service.
- eu.zip build 2014-05-20 12:50 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201404301508-alt1
- repocop cronbuild 20140502. At your service.
- eu.zip build 2014-04-30 15:08 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201404161524-alt1
- repocop cronbuild 20140418. At your service.
- eu.zip build 2014-04-16 15:24 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201404100819-alt1
- repocop cronbuild 20140411. At your service.
- eu.zip build 2014-04-10 08:19 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201404031456-alt1
- repocop cronbuild 20140404. At your service.
- eu.zip build 2014-04-03 14:56 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403271558-alt1
- repocop cronbuild 20140328. At your service.
- eu.zip build 2014-03-27 15:58 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403191042-alt1
- repocop cronbuild 20140321. At your service.
- eu.zip build 2014-03-19 10:42 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403131045-alt1
- repocop cronbuild 20140314. At your service.
- eu.zip build 2014-03-13 10:45 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403051543-alt1
- repocop cronbuild 20140307. At your service.
- eu.zip build 2014-03-05 15:43 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402271128-alt1
- repocop cronbuild 20140228. At your service.
- eu.zip build 2014-02-27 11:28 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402190855-alt1
- repocop cronbuild 20140221. At your service.
- eu.zip build 2014-02-19 08:55 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402121152-alt1
- repocop cronbuild 20140214. At your service.
- eu.zip build 2014-02-12 11:52 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402031058-alt1
- repocop cronbuild 20140207. At your service.
- eu.zip build 2014-02-03 10:58 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201401211028-alt1
- repocop cronbuild 20140124. At your service.
- eu.zip build 2014-01-21 10:28 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201401151119-alt1
- repocop cronbuild 20140117. At your service.
- eu.zip build 2014-01-15 11:19 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201312171659-alt1
- repocop cronbuild 20131220. At your service.
- eu.zip build 2013-12-17 16:59 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201312110905-alt1
- repocop cronbuild 20131213. At your service.
- eu.zip build 2013-12-11 09:05 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311261628-alt1
- repocop cronbuild 20131129. At your service.
- eu.zip build 2013-11-26 16:28 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311211055-alt1
- repocop cronbuild 20131122. At your service.
- eu.zip build 2013-11-21 10:55 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311121517-alt1
- repocop cronbuild 20131115. At your service.
- eu.zip build 2013-11-12 15:17 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311061106-alt1
- repocop cronbuild 20131108. At your service.
- eu.zip build 2013-11-06 11:06 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310290942-alt1
- repocop cronbuild 20131101. At your service.
- eu.zip build 2013-10-29 09:42 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310221504-alt1
- repocop cronbuild 20131025. At your service.
- eu.zip build 2013-10-22 15:04 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310081459-alt1
- repocop cronbuild 20131011. At your service.
- eu.zip build 2013-10-08 14:59 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309300953-alt1
- repocop cronbuild 20131004. At your service.
- eu.zip build 2013-09-30 09:53 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309250702-alt1
- repocop cronbuild 20130927. At your service.
- eu.zip build 2013-09-25 07:02 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309190826-alt1
- repocop cronbuild 20130920. At your service.
- eu.zip build 2013-09-19 08:26 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309061028-alt1
- repocop cronbuild 20130913. At your service.
- eu.zip build 2013-09-06 10:28 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309060858-alt1
- repocop cronbuild 20130906. At your service.
- eu.zip build 2013-09-06 08:58 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307120654-alt1
- repocop cronbuild 20130719. At your service.
- eu.zip build 2013-07-12 06:54 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307080559-alt1
- repocop cronbuild 20130712. At your service.
- eu.zip build 2013-07-08 05:59 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201306270837-alt1
- repocop cronbuild 20130628. At your service.
- eu.zip build 2013-06-27 08:37 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201306131418-alt1
- repocop cronbuild 20130614. At your service.
- eu.zip build 2013-06-13 14:18 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305301430-alt1
- repocop cronbuild 20130531. At your service.
- eu.zip build 2013-05-30 14:30 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305211253-alt1
- repocop cronbuild 20130524. At your service.
- eu.zip build 2013-05-21 12:53 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305150726-alt1
- repocop cronbuild 20130517. At your service.
- eu.zip build 2013-05-15 07:26 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305081012-alt1
- repocop cronbuild 20130509. At your service.
- eu.zip build 2013-05-08 10:12 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304120658-alt1
- repocop cronbuild 20130417. At your service.
- eu.zip build 2013-04-12 06:58 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302281139-alt1
- repocop cronbuild 20130304. At your service.
- eu.zip build 2013-02-28 11:39 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301291640-alt1
- repocop cronbuild 20130204. At your service.
- eu.zip build 2013-01-29 16:40 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301250841-alt1
- repocop cronbuild 20130128. At your service.
- eu.zip build 2013-01-25 08:41 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301180754-alt1
- repocop cronbuild 20130121. At your service.
- eu.zip build 2013-01-18 07:54 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301081510-alt1
- repocop cronbuild 20130114. At your service.
- eu.zip build 2013-01-08 15:10 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212181639-alt1
- repocop cronbuild 20121224. At your service.
- eu.zip build 2012-12-18 16:39 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212120947-alt1
- repocop cronbuild 20121217. At your service.
- eu.zip build 2012-12-12 09:47 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212051044-alt1
- repocop cronbuild 20121210. At your service.
- eu.zip build 2012-12-05 10:44 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211281059-alt1
- repocop cronbuild 20121203. At your service.
- eu.zip build 2012-11-28 10:59 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211201521-alt1
- repocop cronbuild 20121126. At your service.
- eu.zip build 2012-11-20 15:21 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211141043-alt1
- repocop cronbuild 20121119. At your service.
- eu.zip build 2012-11-14 10:43 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211081123-alt1
- repocop cronbuild 20121112. At your service.
- eu.zip build 2012-11-08 11:23 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- eu.zip build 2012-11-01 07:00 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210240700-alt1
- repocop cronbuild 20121029. At your service.
- eu.zip build 2012-10-24 07:00 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210170949-alt1
- repocop cronbuild 20121022. At your service.
- eu.zip build 2012-10-17 09:49 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210111450-alt1
- repocop cronbuild 20121015. At your service.
- eu.zip build 2012-10-11 14:50 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210020714-alt1
- repocop cronbuild 20121008. At your service.
- eu.zip build 2012-10-02 07:14 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209281049-alt1
- repocop cronbuild 20121001. At your service.
- eu.zip build 2012-09-28 10:49 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209140810-alt1
- repocop cronbuild 20120918. At your service.
- eu.zip build 2012-09-14 08:10 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209101029-alt1
- repocop cronbuild 20120911. At your service.
- eu.zip build 2012-09-10 10:29 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120904. At your service.
- eu.zip build 2012-08-31 10:30 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207101021-alt1
- repocop cronbuild 20120717. At your service.
- eu.zip build 2012-07-10 10:21 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207040746-alt1
- repocop cronbuild 20120710. At your service.
- eu.zip build 2012-07-04 07:46 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206271402-alt1
- repocop cronbuild 20120703. At your service.
- eu.zip build 2012-06-27 14:02 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206190802-alt1
- repocop cronbuild 20120626. At your service.
- eu.zip build 2012-06-19 08:02 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206181453-alt1
- repocop cronbuild 20120619. At your service.
- eu.zip build 2012-06-18 14:53 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206070800-alt1
- repocop cronbuild 20120612. At your service.
- eu.zip build 2012-06-07 08:00 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206041416-alt1
- repocop cronbuild 20120605. At your service.
- eu.zip build 2012-06-04 14:16 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205280920-alt1
- repocop cronbuild 20120529. At your service.
- eu.zip build 2012-05-28 09:20 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205181030-alt1
- repocop cronbuild 20120521. At your service.
- eu.zip build 2012-05-18 10:30 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205141019-alt1
- repocop cronbuild 20120515. At your service.
- eu.zip build 2012-05-14 10:19 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205031401-alt1
- repocop cronbuild 20120508. At your service.
- eu.zip build 2012-05-03 14:01 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- eu.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204230812-alt1
- repocop cronbuild 20120424. At your service.
- eu.zip build 2012-04-23 08:12 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204041000-alt1
- repocop cronbuild 20120410. At your service.
- eu.zip build 2012-04-04 10:00 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204020952-alt1
- repocop cronbuild 20120403. At your service.
- eu.zip build 2012-04-02 09:52 UTC

* Mon Mar 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203070848-alt1
- Rename package to moodle2.2-lang-eu
- eu.zip build 2012-03-07 08:48 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203070848-alt1
- repocop cronbuild 20120307. At your service.
- eu.zip build 2012-03-07 08:48 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202101101-alt1
- repocop cronbuild 20120215. At your service.
- eu.zip build 2012-02-10 11:01 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202081056-alt1
- repocop cronbuild 20120208. At your service.
- eu.zip build 2012-02-08 10:56 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202010850-alt1
- repocop cronbuild 20120201. At your service.
- eu.zip build 2012-02-01 08:50 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201240924-alt1
- repocop cronbuild 20120125. At your service.
- eu.zip build 2012-01-24 09:24 UTC

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201180848-alt1
- repocop cronbuild 20120118. At your service.
- eu.zip build 2012-01-18 08:48 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201110835-alt1
- repocop cronbuild 20120111. At your service.
- eu.zip build 2012-01-11 08:35 UTC

* Wed Dec 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112230805-alt1
- repocop cronbuild 20111228. At your service.
- eu.zip build 2011-12-23 08:05 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112161054-alt1
- repocop cronbuild 20111221. At your service.
- eu.zip build 2011-12-16 10:54 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112141638-alt1
- repocop cronbuild 20111214. At your service.
- eu.zip build 2011-12-14 16:38 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112011016-alt1
- repocop cronbuild 20111207. At your service.
- eu.zip build 2011-12-01 10:16 UTC

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111301637-alt1
- repocop cronbuild 20111130. At your service.
- eu.zip build 2011-11-30 16:37 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111240814-alt1
- Rename package to moodle2.1-lang-eu
- eu.zip build 2011-11-24 08:14 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111231509-alt2
- Fix requires

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111231509-alt1
- repocop cronbuild 20111123. At your service.
- eu.zip build 2011-11-23 15:09 UTC

* Mon Nov 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111210921-alt1
- repocop cronbuild 20111121. At your service.
- eu.zip build 2011-11-21 09:21 UTC

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111180850-alt1
- repocop cronbuild 20111118. At your service.
- eu.zip build 2011-11-18 08:50 UTC

* Thu Nov 17 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111170831-alt1
- repocop cronbuild 20111117. At your service.
- eu.zip build 2011-11-17 08:31 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151637-alt1
- repocop cronbuild 20111116. At your service.
- eu.zip build 2011-11-15 16:37 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt1
- eu.zip build 2011-10-19 15:31 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109281025-alt1
- eu.zip build 2011-09-28 10:25 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109271026-alt1
- eu.zip build 2011-09-27 10:26 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109221435-alt1
- eu.zip build 2011-09-22 14:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- eu.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109191034-alt1
- eu.zip build 2011-09-19 10:34 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109150906-alt1
- eu.zip build 2011-09-15 09:06 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141022-alt1
- eu.zip build 2011-09-14 10:22 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109140814-alt1
- eu.zip build 2011-09-14 08:14 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-eu
- eu.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110813-alt1
- eu_utf8.zip build 2011-08-13
- initial build for ALT Linux Sisyphus
