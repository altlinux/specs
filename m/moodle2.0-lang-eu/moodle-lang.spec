# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename eu
%define packagversion 2.0.0
%define packagedate 201601260805
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Basque
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-eu
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
* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601260805-alt1
- repocop cronbuild 20160131. At your service.
- eu.zip build 2016-01-26 08:05 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601191011-alt1
- repocop cronbuild 20160124. At your service.
- eu.zip build 2016-01-19 10:11 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512101524-alt1
- repocop cronbuild 20151214. At your service.
- eu.zip build 2015-12-10 15:24 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512021634-alt1
- repocop cronbuild 20151207. At your service.
- eu.zip build 2015-12-02 16:34 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511261605-alt1
- repocop cronbuild 20151130. At your service.
- eu.zip build 2015-11-26 16:05 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511160724-alt1
- repocop cronbuild 20151123. At your service.
- eu.zip build 2015-11-16 07:24 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511091553-alt1
- repocop cronbuild 20151116. At your service.
- eu.zip build 2015-11-09 15:53 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- eu.zip build 2015-11-08 22:20 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510290821-alt1
- repocop cronbuild 20151102. At your service.
- eu.zip build 2015-10-29 08:21 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510150658-alt1
- repocop cronbuild 20151019. At your service.
- eu.zip build 2015-10-15 06:58 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509250735-alt1
- repocop cronbuild 20150928. At your service.
- eu.zip build 2015-09-25 07:35 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509181026-alt1
- repocop cronbuild 20150921. At your service.
- eu.zip build 2015-09-18 10:26 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509070707-alt1
- repocop cronbuild 20150914. At your service.
- eu.zip build 2015-09-07 07:07 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508070810-alt1
- repocop cronbuild 20150823. At your service.
- eu.zip build 2015-08-07 08:10 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507020857-alt1
- repocop cronbuild 20150702. At your service.
- eu.zip build 2015-07-02 08:57 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506241357-alt1
- repocop cronbuild 20150625. At your service.
- eu.zip build 2015-06-24 13:57 UTC

* Fri Jun 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506190606-alt1
- repocop cronbuild 20150619. At your service.
- eu.zip build 2015-06-19 06:06 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505050853-alt1
- repocop cronbuild 20150508. At your service.
- eu.zip build 2015-05-05 08:53 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504221005-alt1
- repocop cronbuild 20150424. At your service.
- eu.zip build 2015-04-22 10:05 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504160953-alt1
- repocop cronbuild 20150417. At your service.
- eu.zip build 2015-04-16 09:53 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503251447-alt1
- repocop cronbuild 20150327. At your service.
- eu.zip build 2015-03-25 14:47 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503021613-alt1
- repocop cronbuild 20150306. At your service.
- eu.zip build 2015-03-02 16:13 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502241041-alt1
- repocop cronbuild 20150227. At your service.
- eu.zip build 2015-02-24 10:41 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502121454-alt1
- repocop cronbuild 20150213. At your service.
- eu.zip build 2015-02-12 14:54 UTC

* Thu Jan 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501290907-alt1
- repocop cronbuild 20150129. At your service.
- eu.zip build 2015-01-29 09:07 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501221127-alt1
- repocop cronbuild 20150123. At your service.
- eu.zip build 2015-01-22 11:27 UTC

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501151042-alt1
- repocop cronbuild 20150116. At your service.
- eu.zip build 2015-01-15 10:42 UTC

* Thu Jan 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501081613-alt1
- repocop cronbuild 20150108. At your service.
- eu.zip build 2015-01-08 16:13 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412171507-alt1
- repocop cronbuild 20141219. At your service.
- eu.zip build 2014-12-17 15:07 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412111624-alt1
- repocop cronbuild 20141211. At your service.
- eu.zip build 2014-12-11 16:24 UTC

* Thu Nov 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411271122-alt1
- repocop cronbuild 20141127. At your service.
- eu.zip build 2014-11-27 11:22 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411121551-alt1
- repocop cronbuild 20141114. At your service.
- eu.zip build 2014-11-12 15:51 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411060950-alt1
- repocop cronbuild 20141107. At your service.
- eu.zip build 2014-11-06 09:50 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410020824-alt1
- repocop cronbuild 20141003. At your service.
- eu.zip build 2014-10-02 08:24 UTC

* Thu Sep 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409250817-alt1
- repocop cronbuild 20140925. At your service.
- eu.zip build 2014-09-25 08:17 UTC

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409160902-alt1
- repocop cronbuild 20140918. At your service.
- eu.zip build 2014-09-16 09:02 UTC

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409111528-alt1
- repocop cronbuild 20140911. At your service.
- eu.zip build 2014-09-11 15:28 UTC

* Tue Jun 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406101524-alt1
- repocop cronbuild 20140617. At your service.
- eu.zip build 2014-06-10 15:24 UTC

* Sun May 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405201248-alt1
- repocop cronbuild 20140525. At your service.
- eu.zip build 2014-05-20 12:48 UTC

* Sun May 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404301508-alt1
- repocop cronbuild 20140504. At your service.
- eu.zip build 2014-04-30 15:08 UTC

* Sat Apr 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404161524-alt1
- repocop cronbuild 20140419. At your service.
- eu.zip build 2014-04-16 15:24 UTC

* Sun Apr 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404100819-alt1
- repocop cronbuild 20140413. At your service.
- eu.zip build 2014-04-10 08:19 UTC

* Sun Apr 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404031444-alt1
- repocop cronbuild 20140406. At your service.
- eu.zip build 2014-04-03 14:44 UTC

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403280828-alt1
- repocop cronbuild 20140329. At your service.
- eu.zip build 2014-03-28 08:28 UTC

* Sun Mar 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403131038-alt1
- repocop cronbuild 20140316. At your service.
- eu.zip build 2014-03-13 10:38 UTC

* Sat Mar 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403071012-alt1
- repocop cronbuild 20140308. At your service.
- eu.zip build 2014-03-07 10:12 UTC

* Sun Mar 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402271128-alt1
- repocop cronbuild 20140302. At your service.
- eu.zip build 2014-02-27 11:28 UTC

* Sun Feb 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402211001-alt1
- repocop cronbuild 20140223. At your service.
- eu.zip build 2014-02-21 10:01 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402121152-alt1
- repocop cronbuild 20140215. At your service.
- eu.zip build 2014-02-12 11:52 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201401311043-alt1
- repocop cronbuild 20140131. At your service.
- eu.zip build 2014-01-31 10:43 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312171659-alt1
- repocop cronbuild 20131220. At your service.
- eu.zip build 2013-12-17 16:59 UTC

* Sat Dec 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312110905-alt1
- repocop cronbuild 20131214. At your service.
- eu.zip build 2013-12-11 09:05 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311261628-alt1
- repocop cronbuild 20131129. At your service.
- eu.zip build 2013-11-26 16:28 UTC

* Sat Nov 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311211055-alt1
- repocop cronbuild 20131123. At your service.
- eu.zip build 2013-11-21 10:55 UTC

* Sat Nov 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311121517-alt1
- repocop cronbuild 20131116. At your service.
- eu.zip build 2013-11-12 15:17 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311061106-alt1
- repocop cronbuild 20131108. At your service.
- eu.zip build 2013-11-06 11:06 UTC

* Sat Nov 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310290942-alt1
- repocop cronbuild 20131102. At your service.
- eu.zip build 2013-10-29 09:42 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310221500-alt1
- repocop cronbuild 20131025. At your service.
- eu.zip build 2013-10-22 15:00 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310081459-alt1
- repocop cronbuild 20131011. At your service.
- eu.zip build 2013-10-08 14:59 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309250702-alt1
- repocop cronbuild 20130927. At your service.
- eu.zip build 2013-09-25 07:02 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309190822-alt1
- repocop cronbuild 20130920. At your service.
- eu.zip build 2013-09-19 08:22 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309061030-alt1
- repocop cronbuild 20130913. At your service.
- eu.zip build 2013-09-06 10:30 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309020617-alt1
- repocop cronbuild 20130906. At your service.
- eu.zip build 2013-09-02 06:17 UTC

* Fri Jul 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307192050-alt1
- repocop cronbuild 20130726. At your service.
- eu.zip build 2013-07-19 20:50 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307120654-alt1
- repocop cronbuild 20130719. At your service.
- eu.zip build 2013-07-12 06:54 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307080559-alt1
- repocop cronbuild 20130712. At your service.
- eu.zip build 2013-07-08 05:59 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306270836-alt1
- repocop cronbuild 20130628. At your service.
- eu.zip build 2013-06-27 08:36 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305301430-alt1
- repocop cronbuild 20130531. At your service.
- eu.zip build 2013-05-30 14:30 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305211153-alt1
- repocop cronbuild 20130524. At your service.
- eu.zip build 2013-05-21 11:53 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305150722-alt1
- repocop cronbuild 20130517. At your service.
- eu.zip build 2013-05-15 07:22 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305080959-alt1
- repocop cronbuild 20130509. At your service.
- eu.zip build 2013-05-08 09:59 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304120644-alt1
- repocop cronbuild 20130417. At your service.
- eu.zip build 2013-04-12 06:44 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302281138-alt1
- repocop cronbuild 20130304. At your service.
- eu.zip build 2013-02-28 11:38 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301250838-alt1
- repocop cronbuild 20130128. At your service.
- eu.zip build 2013-01-25 08:38 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301081449-alt1
- repocop cronbuild 20130114. At your service.
- eu.zip build 2013-01-08 14:49 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212181639-alt1
- repocop cronbuild 20121224. At your service.
- eu.zip build 2012-12-18 16:39 UTC

* Sun Dec 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212120947-alt1
- repocop cronbuild 20121216. At your service.
- eu.zip build 2012-12-12 09:47 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212051041-alt1
- repocop cronbuild 20121210. At your service.
- eu.zip build 2012-12-05 10:41 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211280957-alt1
- repocop cronbuild 20121203. At your service.
- eu.zip build 2012-11-28 09:57 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211201047-alt1
- repocop cronbuild 20121126. At your service.
- eu.zip build 2012-11-20 10:47 UTC

* Sun Nov 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211141042-alt1
- repocop cronbuild 20121118. At your service.
- eu.zip build 2012-11-14 10:42 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211081625-alt1
- repocop cronbuild 20121112. At your service.
- eu.zip build 2012-11-08 16:25 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210310749-alt1
- repocop cronbuild 20121105. At your service.
- eu.zip build 2012-10-31 07:49 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210240700-alt1
- repocop cronbuild 20121029. At your service.
- eu.zip build 2012-10-24 07:00 UTC

* Sun Oct 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210170933-alt1
- repocop cronbuild 20121021. At your service.
- eu.zip build 2012-10-17 09:33 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210020714-alt1
- repocop cronbuild 20121008. At your service.
- eu.zip build 2012-10-02 07:14 UTC

* Sun Sep 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209281049-alt1
- repocop cronbuild 20120930. At your service.
- eu.zip build 2012-09-28 10:49 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209121527-alt1
- repocop cronbuild 20120917. At your service.
- eu.zip build 2012-09-12 15:27 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209101029-alt1
- repocop cronbuild 20120910. At your service.
- eu.zip build 2012-09-10 10:29 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208301131-alt1
- repocop cronbuild 20120904. At your service.
- eu.zip build 2012-08-30 11:31 UTC

* Mon Jul 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207101021-alt1
- repocop cronbuild 20120716. At your service.
- eu.zip build 2012-07-10 10:21 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207040745-alt1
- repocop cronbuild 20120709. At your service.
- eu.zip build 2012-07-04 07:45 UTC

* Mon Jul 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206271359-alt1
- repocop cronbuild 20120702. At your service.
- eu.zip build 2012-06-27 13:59 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206190802-alt1
- repocop cronbuild 20120625. At your service.
- eu.zip build 2012-06-19 08:02 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206181450-alt1
- repocop cronbuild 20120618. At your service.
- eu.zip build 2012-06-18 14:50 UTC

* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206070800-alt1
- repocop cronbuild 20120611. At your service.
- eu.zip build 2012-06-07 08:00 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206041416-alt1
- repocop cronbuild 20120604. At your service.
- eu.zip build 2012-06-04 14:16 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231548-alt1
- repocop cronbuild 20120528. At your service.
- eu.zip build 2012-05-23 15:48 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205180742-alt1
- repocop cronbuild 20120521. At your service.
- eu.zip build 2012-05-18 07:42 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205141027-alt1
- repocop cronbuild 20120514. At your service.
- eu.zip build 2012-05-14 10:27 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205031412-alt1
- repocop cronbuild 20120507. At your service.
- eu.zip build 2012-05-03 14:12 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204270957-alt1
- repocop cronbuild 20120430. At your service.
- eu.zip build 2012-04-27 09:57 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204230812-alt1
- repocop cronbuild 20120423. At your service.
- eu.zip build 2012-04-23 08:12 UTC

* Mon Apr 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204041000-alt1
- repocop cronbuild 20120409. At your service.
- eu.zip build 2012-04-04 10:00 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204020952-alt1
- repocop cronbuild 20120402. At your service.
- eu.zip build 2012-04-02 09:52 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203070848-alt1
- repocop cronbuild 20120307. At your service.
- eu.zip build 2012-03-07 08:48 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202101055-alt1
- repocop cronbuild 20120215. At your service.
- eu.zip build 2012-02-10 10:55 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202081056-alt1
- repocop cronbuild 20120208. At your service.
- eu.zip build 2012-02-08 10:56 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202010850-alt1
- repocop cronbuild 20120201. At your service.
- eu.zip build 2012-02-01 08:50 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201240923-alt1
- repocop cronbuild 20120125. At your service.
- eu.zip build 2012-01-24 09:23 UTC

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201180848-alt1
- repocop cronbuild 20120118. At your service.
- eu.zip build 2012-01-18 08:48 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201110835-alt1
- repocop cronbuild 20120111. At your service.
- eu.zip build 2012-01-11 08:35 UTC

* Wed Dec 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112230802-alt1
- repocop cronbuild 20111228. At your service.
- eu.zip build 2011-12-23 08:02 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112161054-alt1
- repocop cronbuild 20111221. At your service.
- eu.zip build 2011-12-16 10:54 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112141638-alt1
- repocop cronbuild 20111214. At your service.
- eu.zip build 2011-12-14 16:38 UTC

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111301636-alt1
- repocop cronbuild 20111130. At your service.
- eu.zip build 2011-11-30 16:36 UTC

* Thu Nov 24 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111240814-alt1
- repocop cronbuild 20111124. At your service.
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
