# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename pt_br
%define packagversion 2.0.0
%define packagedate 201602261854
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Portuguese (Brazil)
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-pt_br
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
* Sun Feb 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602261854-alt1
- repocop cronbuild 20160228. At your service.
- pt_br.zip build 2016-02-26 18:54 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601061847-alt1
- repocop cronbuild 20160124. At your service.
- pt_br.zip build 2016-01-06 18:47 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512061823-alt1
- repocop cronbuild 20151207. At your service.
- pt_br.zip build 2015-12-06 18:23 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511171744-alt1
- repocop cronbuild 20151123. At your service.
- pt_br.zip build 2015-11-17 17:44 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- pt_br.zip build 2015-11-08 22:20 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510242135-alt1
- repocop cronbuild 20151026. At your service.
- pt_br.zip build 2015-10-24 21:35 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509281212-alt1
- repocop cronbuild 20151005. At your service.
- pt_br.zip build 2015-09-28 12:12 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509182014-alt1
- repocop cronbuild 20150921. At your service.
- pt_br.zip build 2015-09-18 20:14 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508311357-alt1
- repocop cronbuild 20150907. At your service.
- pt_br.zip build 2015-08-31 13:57 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508282013-alt1
- repocop cronbuild 20150831. At your service.
- pt_br.zip build 2015-08-28 20:13 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508111840-alt1
- repocop cronbuild 20150823. At your service.
- pt_br.zip build 2015-08-11 18:40 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507291322-alt1
- repocop cronbuild 20150730. At your service.
- pt_br.zip build 2015-07-29 13:22 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507201948-alt1
- repocop cronbuild 20150723. At your service.
- pt_br.zip build 2015-07-20 19:48 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507021817-alt1
- repocop cronbuild 20150709. At your service.
- pt_br.zip build 2015-07-02 18:17 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507020007-alt1
- repocop cronbuild 20150702. At your service.
- pt_br.zip build 2015-07-02 00:07 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506022015-alt1
- repocop cronbuild 20150604. At your service.
- pt_br.zip build 2015-06-02 20:15 UTC

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505182046-alt1
- repocop cronbuild 20150522. At your service.
- pt_br.zip build 2015-05-18 20:46 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505012007-alt1
- repocop cronbuild 20150508. At your service.
- pt_br.zip build 2015-05-01 20:07 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504301412-alt1
- repocop cronbuild 20150501. At your service.
- pt_br.zip build 2015-04-30 14:12 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504231356-alt1
- repocop cronbuild 20150424. At your service.
- pt_br.zip build 2015-04-23 13:56 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504081652-alt1
- repocop cronbuild 20150410. At your service.
- pt_br.zip build 2015-04-08 16:52 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503271525-alt1
- repocop cronbuild 20150403. At your service.
- pt_br.zip build 2015-03-27 15:25 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503251331-alt1
- repocop cronbuild 20150327. At your service.
- pt_br.zip build 2015-03-25 13:31 UTC

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503171334-alt1
- repocop cronbuild 20150320. At your service.
- pt_br.zip build 2015-03-17 13:34 UTC

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503121352-alt1
- repocop cronbuild 20150313. At your service.
- pt_br.zip build 2015-03-12 13:52 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503042015-alt1
- repocop cronbuild 20150306. At your service.
- pt_br.zip build 2015-03-04 20:15 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502201914-alt1
- repocop cronbuild 20150227. At your service.
- pt_br.zip build 2015-02-20 19:14 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501191539-alt1
- repocop cronbuild 20150123. At your service.
- pt_br.zip build 2015-01-19 15:39 UTC

* Fri Dec 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412191615-alt1
- repocop cronbuild 20141226. At your service.
- pt_br.zip build 2014-12-19 16:15 UTC

* Thu Nov 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411251207-alt1
- repocop cronbuild 20141127. At your service.
- pt_br.zip build 2014-11-25 12:07 UTC

* Thu Oct 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410301231-alt1
- repocop cronbuild 20141030. At your service.
- pt_br.zip build 2014-10-30 12:31 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410231146-alt1
- repocop cronbuild 20141024. At your service.
- pt_br.zip build 2014-10-23 11:46 UTC

* Thu Oct 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410151401-alt1
- repocop cronbuild 20141016. At your service.
- pt_br.zip build 2014-10-15 14:01 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410032044-alt1
- repocop cronbuild 20141010. At your service.
- pt_br.zip build 2014-10-03 20:44 UTC

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409111717-alt1
- repocop cronbuild 20140918. At your service.
- pt_br.zip build 2014-09-11 17:17 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406241356-alt1
- repocop cronbuild 20140628. At your service.
- pt_br.zip build 2014-06-24 13:56 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406181307-alt1
- repocop cronbuild 20140621. At your service.
- pt_br.zip build 2014-06-18 13:07 UTC

* Sat Jun 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406111552-alt1
- repocop cronbuild 20140614. At your service.
- pt_br.zip build 2014-06-11 15:52 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406061908-alt1
- repocop cronbuild 20140606. At your service.
- pt_br.zip build 2014-06-06 19:08 UTC

* Sat May 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405302234-alt1
- repocop cronbuild 20140531. At your service.
- pt_br.zip build 2014-05-30 22:34 UTC

* Sat May 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405132038-alt1
- repocop cronbuild 20140517. At your service.
- pt_br.zip build 2014-05-13 20:38 UTC

* Sat May 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405031425-alt1
- repocop cronbuild 20140510. At your service.
- pt_br.zip build 2014-05-03 14:25 UTC

* Sat May 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404301934-alt1
- repocop cronbuild 20140503. At your service.
- pt_br.zip build 2014-04-30 19:34 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404041432-alt1
- repocop cronbuild 20140404. At your service.
- pt_br.zip build 2014-04-04 14:32 UTC

* Sat Mar 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403201919-alt1
- repocop cronbuild 20140322. At your service.
- pt_br.zip build 2014-03-20 19:19 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403101352-alt1
- repocop cronbuild 20140314. At your service.
- pt_br.zip build 2014-03-10 13:52 UTC

* Sat Mar 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403061757-alt1
- repocop cronbuild 20140308. At your service.
- pt_br.zip build 2014-03-06 17:57 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402261738-alt1
- repocop cronbuild 20140301. At your service.
- pt_br.zip build 2014-02-26 17:38 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402181744-alt1
- repocop cronbuild 20140221. At your service.
- pt_br.zip build 2014-02-18 17:44 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402131251-alt1
- repocop cronbuild 20140215. At your service.
- pt_br.zip build 2014-02-13 12:51 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312161654-alt1
- repocop cronbuild 20131220. At your service.
- pt_br.zip build 2013-12-16 16:54 UTC

* Sat Dec 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312051738-alt1
- repocop cronbuild 20131207. At your service.
- pt_br.zip build 2013-12-05 17:38 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311261840-alt1
- repocop cronbuild 20131129. At your service.
- pt_br.zip build 2013-11-26 18:40 UTC

* Sat Nov 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311121121-alt1
- repocop cronbuild 20131116. At your service.
- pt_br.zip build 2013-11-12 11:21 UTC

* Sat Nov 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310312238-alt1
- repocop cronbuild 20131102. At your service.
- pt_br.zip build 2013-10-31 22:38 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310151349-alt1
- repocop cronbuild 20131018. At your service.
- pt_br.zip build 2013-10-15 13:49 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309171501-alt1
- repocop cronbuild 20130920. At your service.
- pt_br.zip build 2013-09-17 15:01 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309091901-alt1
- repocop cronbuild 20130913. At your service.
- pt_br.zip build 2013-09-09 19:01 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307292116-alt1
- repocop cronbuild 20130802. At your service.
- pt_br.zip build 2013-07-29 21:16 UTC

* Fri Jul 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307251540-alt1
- repocop cronbuild 20130726. At your service.
- pt_br.zip build 2013-07-25 15:40 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307152104-alt1
- repocop cronbuild 20130719. At your service.
- pt_br.zip build 2013-07-15 21:04 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306241459-alt1
- repocop cronbuild 20130628. At your service.
- pt_br.zip build 2013-06-24 14:59 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306201514-alt1
- repocop cronbuild 20130621. At your service.
- pt_br.zip build 2013-06-20 15:14 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305251456-alt1
- repocop cronbuild 20130531. At your service.
- pt_br.zip build 2013-05-25 14:56 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305211302-alt1
- repocop cronbuild 20130524. At your service.
- pt_br.zip build 2013-05-21 13:02 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305161450-alt1
- repocop cronbuild 20130517. At your service.
- pt_br.zip build 2013-05-16 14:50 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305030022-alt1
- repocop cronbuild 20130509. At your service.
- pt_br.zip build 2013-05-03 00:22 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304040056-alt1
- repocop cronbuild 20130410. At your service.
- pt_br.zip build 2013-04-04 00:56 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303311321-alt1
- repocop cronbuild 20130403. At your service.
- pt_br.zip build 2013-03-31 13:21 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303231852-alt1
- repocop cronbuild 20130327. At your service.
- pt_br.zip build 2013-03-23 18:52 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303170018-alt1
- repocop cronbuild 20130319. At your service.
- pt_br.zip build 2013-03-17 00:18 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303101747-alt1
- repocop cronbuild 20130313. At your service.
- pt_br.zip build 2013-03-10 17:47 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303031115-alt1
- repocop cronbuild 20130304. At your service.
- pt_br.zip build 2013-03-03 11:15 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302181634-alt1
- repocop cronbuild 20130225. At your service.
- pt_br.zip build 2013-02-18 16:34 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302180144-alt1
- repocop cronbuild 20130218. At your service.
- pt_br.zip build 2013-02-18 01:44 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302092037-alt1
- repocop cronbuild 20130211. At your service.
- pt_br.zip build 2013-02-09 20:37 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301261303-alt1
- repocop cronbuild 20130128. At your service.
- pt_br.zip build 2013-01-26 13:03 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301181855-alt1
- repocop cronbuild 20130121. At your service.
- pt_br.zip build 2013-01-18 18:55 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301140225-alt1
- repocop cronbuild 20130114. At your service.
- pt_br.zip build 2013-01-14 02:25 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301020129-alt1
- repocop cronbuild 20130107. At your service.
- pt_br.zip build 2013-01-02 01:29 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212201801-alt1
- repocop cronbuild 20121224. At your service.
- pt_br.zip build 2012-12-20 18:01 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212071943-alt1
- repocop cronbuild 20121210. At your service.
- pt_br.zip build 2012-12-07 19:43 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211301902-alt1
- repocop cronbuild 20121203. At your service.
- pt_br.zip build 2012-11-30 19:02 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211051358-alt1
- repocop cronbuild 20121112. At your service.
- pt_br.zip build 2012-11-05 13:58 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210221850-alt1
- repocop cronbuild 20121029. At your service.
- pt_br.zip build 2012-10-22 18:50 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210091839-alt1
- repocop cronbuild 20121015. At your service.
- pt_br.zip build 2012-10-09 18:39 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210052002-alt1
- repocop cronbuild 20121008. At your service.
- pt_br.zip build 2012-10-05 20:02 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209300109-alt1
- repocop cronbuild 20121001. At your service.
- pt_br.zip build 2012-09-30 01:09 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209112001-alt1
- repocop cronbuild 20120918. At your service.
- pt_br.zip build 2012-09-11 20:01 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209051804-alt1
- repocop cronbuild 20120910. At your service.
- pt_br.zip build 2012-09-05 18:04 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208271946-alt1
- repocop cronbuild 20120828. At your service.
- pt_br.zip build 2012-08-27 19:46 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208171315-alt1
- repocop cronbuild 20120820. At your service.
- pt_br.zip build 2012-08-17 13:15 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208132047-alt1
- repocop cronbuild 20120814. At your service.
- pt_br.zip build 2012-08-13 20:47 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208011438-alt1
- repocop cronbuild 20120807. At your service.
- pt_br.zip build 2012-08-01 14:38 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207301844-alt1
- repocop cronbuild 20120731. At your service.
- pt_br.zip build 2012-07-30 18:44 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207231815-alt1
- repocop cronbuild 20120724. At your service.
- pt_br.zip build 2012-07-23 18:15 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206301742-alt1
- repocop cronbuild 20120703. At your service.
- pt_br.zip build 2012-06-30 17:42 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206222325-alt1
- repocop cronbuild 20120626. At your service.
- pt_br.zip build 2012-06-22 23:25 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206181525-alt1
- repocop cronbuild 20120618. At your service.
- pt_br.zip build 2012-06-18 15:25 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206112038-alt1
- repocop cronbuild 20120612. At your service.
- pt_br.zip build 2012-06-11 20:38 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206041938-alt1
- repocop cronbuild 20120605. At your service.
- pt_br.zip build 2012-06-04 19:38 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205281447-alt1
- repocop cronbuild 20120528. At your service.
- pt_br.zip build 2012-05-28 14:47 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205182057-alt1
- repocop cronbuild 20120521. At your service.
- pt_br.zip build 2012-05-18 20:57 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205141455-alt1
- repocop cronbuild 20120514. At your service.
- pt_br.zip build 2012-05-14 14:55 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204251410-alt1
- repocop cronbuild 20120430. At your service.
- pt_br.zip build 2012-04-25 14:10 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204200243-alt1
- repocop cronbuild 20120423. At your service.
- pt_br.zip build 2012-04-20 02:43 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204162126-alt1
- repocop cronbuild 20120416. At your service.
- pt_br.zip build 2012-04-16 21:26 UTC

* Mon Apr 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204082324-alt1
- repocop cronbuild 20120409. At your service.
- pt_br.zip build 2012-04-08 23:24 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203301343-alt1
- repocop cronbuild 20120402. At your service.
- pt_br.zip build 2012-03-30 13:43 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203261714-alt1
- repocop cronbuild 20120327. At your service.
- pt_br.zip build 2012-03-26 17:14 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203191345-alt1
- repocop cronbuild 20120319. At your service.
- pt_br.zip build 2012-03-19 13:45 UTC

* Tue Mar 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203100221-alt1
- repocop cronbuild 20120313. At your service.
- pt_br.zip build 2012-03-10 02:21 UTC

* Thu Mar 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203061259-alt1
- repocop cronbuild 20120308. At your service.
- pt_br.zip build 2012-03-06 12:59 UTC

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203011855-alt1
- repocop cronbuild 20120301. At your service.
- pt_br.zip build 2012-03-01 18:55 UTC

* Thu Feb 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202231553-alt1
- repocop cronbuild 20120223. At your service.
- pt_br.zip build 2012-02-23 15:53 UTC

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202102340-alt1
- repocop cronbuild 20120216. At your service.
- pt_br.zip build 2012-02-10 23:40 UTC

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202071934-alt1
- repocop cronbuild 20120209. At your service.
- pt_br.zip build 2012-02-07 19:34 UTC

* Thu Jan 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201261540-alt1
- repocop cronbuild 20120126. At your service.
- pt_br.zip build 2012-01-26 15:40 UTC

* Thu Jan 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201192114-alt1
- repocop cronbuild 20120119. At your service.
- pt_br.zip build 2012-01-19 21:14 UTC

* Thu Jan 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201111834-alt1
- repocop cronbuild 20120112. At your service.
- pt_br.zip build 2012-01-11 18:34 UTC

* Thu Dec 29 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112291731-alt1
- repocop cronbuild 20111229. At your service.
- pt_br.zip build 2011-12-29 17:31 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111101730-alt1
- Rename package to moodle2.0-lang-pt_br
- pt_br.zip build 2011-11-10 17:30 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- pt.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- pt.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161557-alt2
- Fix requires

* Wed Aug 17 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161557-alt1
- pt.zip build 2011-08-16 15:57 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103221701-alt1
- Rename package to moodle2.0-lang-pt
- pt.zip build 2011-03-22 17:01 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100814-alt1
- pt_utf8.zip build 2010-08-14

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100814
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20080926
- new build for ALT Linux from cvs
