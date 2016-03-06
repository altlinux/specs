# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename pt_br
%define packagversion 2.5.0
%define packagedate 201603061611
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Portuguese (Brazil)
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-pt_br
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
* Sun Mar 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201603061611-alt1
- repocop cronbuild 20160306. At your service.
- pt_br.zip build 2016-03-06 16:11 UTC

* Sun Feb 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602261854-alt1
- repocop cronbuild 20160228. At your service.
- pt_br.zip build 2016-02-26 18:54 UTC

* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602161838-alt1
- repocop cronbuild 20160221. At your service.
- pt_br.zip build 2016-02-16 18:38 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601121230-alt1
- repocop cronbuild 20160124. At your service.
- pt_br.zip build 2016-01-12 12:30 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201512061823-alt1
- repocop cronbuild 20151207. At your service.
- pt_br.zip build 2015-12-06 18:23 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511271158-alt1
- repocop cronbuild 20151130. At your service.
- pt_br.zip build 2015-11-27 11:58 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511191516-alt1
- repocop cronbuild 20151123. At your service.
- pt_br.zip build 2015-11-19 15:16 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511131605-alt1
- repocop cronbuild 20151116. At your service.
- pt_br.zip build 2015-11-13 16:05 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510242135-alt1
- repocop cronbuild 20151026. At your service.
- pt_br.zip build 2015-10-24 21:35 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510142344-alt1
- repocop cronbuild 20151019. At your service.
- pt_br.zip build 2015-10-14 23:44 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509281212-alt1
- repocop cronbuild 20151005. At your service.
- pt_br.zip build 2015-09-28 12:12 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509182014-alt1
- repocop cronbuild 20150921. At your service.
- pt_br.zip build 2015-09-18 20:14 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509021141-alt1
- repocop cronbuild 20150907. At your service.
- pt_br.zip build 2015-09-02 11:41 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508282013-alt1
- repocop cronbuild 20150831. At your service.
- pt_br.zip build 2015-08-28 20:13 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508111840-alt1
- repocop cronbuild 20150823. At your service.
- pt_br.zip build 2015-08-11 18:40 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507291328-alt1
- repocop cronbuild 20150730. At your service.
- pt_br.zip build 2015-07-29 13:28 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507201948-alt1
- repocop cronbuild 20150723. At your service.
- pt_br.zip build 2015-07-20 19:48 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507021817-alt1
- repocop cronbuild 20150709. At your service.
- pt_br.zip build 2015-07-02 18:17 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507020007-alt1
- repocop cronbuild 20150702. At your service.
- pt_br.zip build 2015-07-02 00:07 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506221835-alt1
- repocop cronbuild 20150625. At your service.
- pt_br.zip build 2015-06-22 18:35 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506151528-alt1
- repocop cronbuild 20150618. At your service.
- pt_br.zip build 2015-06-15 15:28 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506022020-alt1
- repocop cronbuild 20150604. At your service.
- pt_br.zip build 2015-06-02 20:20 UTC

* Sat May 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505182117-alt1
- repocop cronbuild 20150523. At your service.
- pt_br.zip build 2015-05-18 21:17 UTC

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505131923-alt1
- repocop cronbuild 20150515. At your service.
- pt_br.zip build 2015-05-13 19:23 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505061848-alt1
- repocop cronbuild 20150508. At your service.
- pt_br.zip build 2015-05-06 18:48 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504301412-alt1
- repocop cronbuild 20150501. At your service.
- pt_br.zip build 2015-04-30 14:12 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504231356-alt1
- repocop cronbuild 20150424. At your service.
- pt_br.zip build 2015-04-23 13:56 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504081652-alt1
- repocop cronbuild 20150410. At your service.
- pt_br.zip build 2015-04-08 16:52 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503301939-alt1
- repocop cronbuild 20150403. At your service.
- pt_br.zip build 2015-03-30 19:39 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503251331-alt1
- repocop cronbuild 20150327. At your service.
- pt_br.zip build 2015-03-25 13:31 UTC

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503181221-alt1
- repocop cronbuild 20150320. At your service.
- pt_br.zip build 2015-03-18 12:21 UTC

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503121352-alt1
- repocop cronbuild 20150313. At your service.
- pt_br.zip build 2015-03-12 13:52 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503042015-alt1
- repocop cronbuild 20150306. At your service.
- pt_br.zip build 2015-03-04 20:15 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502240031-alt1
- repocop cronbuild 20150227. At your service.
- pt_br.zip build 2015-02-24 00:31 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502050434-alt1
- repocop cronbuild 20150206. At your service.
- pt_br.zip build 2015-02-05 04:34 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501300122-alt1
- repocop cronbuild 20150130. At your service.
- pt_br.zip build 2015-01-30 01:22 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501191540-alt1
- repocop cronbuild 20150123. At your service.
- pt_br.zip build 2015-01-19 15:40 UTC

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501061149-alt1
- repocop cronbuild 20150109. At your service.
- pt_br.zip build 2015-01-06 11:49 UTC

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412301130-alt1
- repocop cronbuild 20150102. At your service.
- pt_br.zip build 2014-12-30 11:30 UTC

* Fri Dec 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412231225-alt1
- repocop cronbuild 20141226. At your service.
- pt_br.zip build 2014-12-23 12:25 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412081635-alt1
- repocop cronbuild 20141212. At your service.
- pt_br.zip build 2014-12-08 16:35 UTC

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412041516-alt1
- repocop cronbuild 20141205. At your service.
- pt_br.zip build 2014-12-04 15:16 UTC

* Fri Nov 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411271310-alt1
- repocop cronbuild 20141128. At your service.
- pt_br.zip build 2014-11-27 13:10 UTC

* Fri Nov 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411191944-alt1
- repocop cronbuild 20141121. At your service.
- pt_br.zip build 2014-11-19 19:44 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411121159-alt1
- repocop cronbuild 20141114. At your service.
- pt_br.zip build 2014-11-12 11:59 UTC

* Fri Oct 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410301921-alt1
- repocop cronbuild 20141031. At your service.
- pt_br.zip build 2014-10-30 19:21 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410231146-alt1
- repocop cronbuild 20141024. At your service.
- pt_br.zip build 2014-10-23 11:46 UTC

* Fri Oct 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410151401-alt1
- repocop cronbuild 20141017. At your service.
- pt_br.zip build 2014-10-15 14:01 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410032045-alt1
- repocop cronbuild 20141010. At your service.
- pt_br.zip build 2014-10-03 20:45 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409292357-alt1
- repocop cronbuild 20141003. At your service.
- pt_br.zip build 2014-09-29 23:57 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409111717-alt1
- repocop cronbuild 20140919. At your service.
- pt_br.zip build 2014-09-11 17:17 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406241356-alt1
- repocop cronbuild 20140628. At your service.
- pt_br.zip build 2014-06-24 13:56 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406201720-alt1
- repocop cronbuild 20140621. At your service.
- pt_br.zip build 2014-06-20 17:20 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406111623-alt1
- repocop cronbuild 20140613. At your service.
- pt_br.zip build 2014-06-11 16:23 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406051753-alt1
- repocop cronbuild 20140606. At your service.
- pt_br.zip build 2014-06-05 17:53 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405262339-alt1
- repocop cronbuild 20140530. At your service.
- pt_br.zip build 2014-05-26 23:39 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405181927-alt1
- repocop cronbuild 20140523. At your service.
- pt_br.zip build 2014-05-18 19:27 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405132038-alt1
- repocop cronbuild 20140516. At your service.
- pt_br.zip build 2014-05-13 20:38 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405060843-alt1
- repocop cronbuild 20140509. At your service.
- pt_br.zip build 2014-05-06 08:43 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404301934-alt1
- repocop cronbuild 20140502. At your service.
- pt_br.zip build 2014-04-30 19:34 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404121336-alt1
- repocop cronbuild 20140418. At your service.
- pt_br.zip build 2014-04-12 13:36 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404072344-alt1
- repocop cronbuild 20140411. At your service.
- pt_br.zip build 2014-04-07 23:44 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404041432-alt1
- repocop cronbuild 20140404. At your service.
- pt_br.zip build 2014-04-04 14:32 UTC

* Sat Mar 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403201919-alt1
- repocop cronbuild 20140322. At your service.
- pt_br.zip build 2014-03-20 19:19 UTC

* Sat Mar 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403101352-alt1
- repocop cronbuild 20140315. At your service.
- pt_br.zip build 2014-03-10 13:52 UTC

* Sat Mar 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403061757-alt1
- repocop cronbuild 20140308. At your service.
- pt_br.zip build 2014-03-06 17:57 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402261738-alt1
- repocop cronbuild 20140301. At your service.
- pt_br.zip build 2014-02-26 17:38 UTC

* Sat Feb 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402201806-alt1
- repocop cronbuild 20140222. At your service.
- pt_br.zip build 2014-02-20 18:06 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402121859-alt1
- repocop cronbuild 20140215. At your service.
- pt_br.zip build 2014-02-12 18:59 UTC

* Sat Feb 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402022101-alt1
- repocop cronbuild 20140208. At your service.
- pt_br.zip build 2014-02-02 21:01 UTC

* Sat Jan 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401231346-alt1
- repocop cronbuild 20140125. At your service.
- pt_br.zip build 2014-01-23 13:46 UTC

* Sat Jan 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401081604-alt1
- repocop cronbuild 20140111. At your service.
- pt_br.zip build 2014-01-08 16:04 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312201640-alt1
- repocop cronbuild 20131227. At your service.
- pt_br.zip build 2013-12-20 16:40 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312161654-alt1
- repocop cronbuild 20131220. At your service.
- pt_br.zip build 2013-12-16 16:54 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- pt_br.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312051738-alt1
- repocop cronbuild 20131206. At your service.
- pt_br.zip build 2013-12-05 17:38 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311261840-alt1
- repocop cronbuild 20131129. At your service.
- pt_br.zip build 2013-11-26 18:40 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311180123-alt1
- repocop cronbuild 20131122. At your service.
- pt_br.zip build 2013-11-18 01:23 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311121728-alt1
- repocop cronbuild 20131115. At your service.
- pt_br.zip build 2013-11-12 17:28 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311051758-alt1
- repocop cronbuild 20131108. At your service.
- pt_br.zip build 2013-11-05 17:58 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310311850-alt1
- repocop cronbuild 20131101. At your service.
- pt_br.zip build 2013-10-31 18:50 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310211518-alt1
- repocop cronbuild 20131025. At your service.
- pt_br.zip build 2013-10-21 15:18 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310151348-alt1
- repocop cronbuild 20131018. At your service.
- pt_br.zip build 2013-10-15 13:48 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310101759-alt1
- repocop cronbuild 20131011. At your service.
- pt_br.zip build 2013-10-10 17:59 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310011437-alt1
- repocop cronbuild 20131004. At your service.
- pt_br.zip build 2013-10-01 14:37 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309231448-alt1
- repocop cronbuild 20130927. At your service.
- pt_br.zip build 2013-09-23 14:48 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309191342-alt1
- repocop cronbuild 20130920. At your service.
- pt_br.zip build 2013-09-19 13:42 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309121356-alt1
- repocop cronbuild 20130913. At your service.
- pt_br.zip build 2013-09-12 13:56 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309060007-alt1
- repocop cronbuild 20130906. At your service.
- pt_br.zip build 2013-09-06 00:07 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308301402-alt1
- repocop cronbuild 20130831. At your service.
- pt_br.zip build 2013-08-30 14:02 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308211643-alt1
- repocop cronbuild 20130824. At your service.
- pt_br.zip build 2013-08-21 16:43 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308161506-alt1
- repocop cronbuild 20130817. At your service.
- pt_br.zip build 2013-08-16 15:06 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308082011-alt1
- repocop cronbuild 20130810. At your service.
- pt_br.zip build 2013-08-08 20:11 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308021335-alt1
- repocop cronbuild 20130803. At your service.
- pt_br.zip build 2013-08-02 13:35 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307270158-alt1
- repocop cronbuild 20130727. At your service.
- pt_br.zip build 2013-07-27 01:58 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307182237-alt1
- repocop cronbuild 20130720. At your service.
- pt_br.zip build 2013-07-18 22:37 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307121421-alt1
- repocop cronbuild 20130713. At your service.
- pt_br.zip build 2013-07-12 14:21 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307011552-alt1
- repocop cronbuild 20130706. At your service.
- pt_br.zip build 2013-07-01 15:52 UTC

* Sat Jun 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306251632-alt1
- repocop cronbuild 20130629. At your service.
- pt_br.zip build 2013-06-25 16:32 UTC

* Sat Jun 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306201514-alt1
- repocop cronbuild 20130622. At your service.
- pt_br.zip build 2013-06-20 15:14 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306141915-alt1
- repocop cronbuild 20130615. At your service.
- pt_br.zip build 2013-06-14 19:15 UTC

* Sat Jun 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306052030-alt1
- repocop cronbuild 20130608. At your service.
- pt_br.zip build 2013-06-05 20:30 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305292351-alt1
- Rename package to moodle2.5-lang-pt_br
- pt_br.zip build 2013-05-29 23:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221013-alt1
- repocop cronbuild 20130524. At your service.
- pt_br.zip build 2013-05-22 10:13 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305161450-alt1
- repocop cronbuild 20130517. At your service.
- pt_br.zip build 2013-05-16 14:50 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305062111-alt1
- repocop cronbuild 20130509. At your service.
- pt_br.zip build 2013-05-06 21:11 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304172005-alt1
- Rename package to moodle2.4-lang-pt_br
- pt_br.zip build 2013-04-17 20:05 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304040056-alt1
- repocop cronbuild 20130410. At your service.
- pt_br.zip build 2013-04-04 00:56 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303311321-alt1
- repocop cronbuild 20130403. At your service.
- pt_br.zip build 2013-03-31 13:21 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303250154-alt1
- repocop cronbuild 20130327. At your service.
- pt_br.zip build 2013-03-25 01:54 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303170018-alt1
- repocop cronbuild 20130320. At your service.
- pt_br.zip build 2013-03-17 00:18 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303110141-alt1
- repocop cronbuild 20130313. At your service.
- pt_br.zip build 2013-03-11 01:41 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303031115-alt1
- repocop cronbuild 20130304. At your service.
- pt_br.zip build 2013-03-03 11:15 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302181436-alt1
- repocop cronbuild 20130225. At your service.
- pt_br.zip build 2013-02-18 14:36 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302180141-alt1
- repocop cronbuild 20130218. At your service.
- pt_br.zip build 2013-02-18 01:41 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302101052-alt1
- repocop cronbuild 20130211. At your service.
- pt_br.zip build 2013-02-10 10:52 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261307-alt1
- repocop cronbuild 20130128. At your service.
- pt_br.zip build 2013-01-26 13:07 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301181855-alt1
- repocop cronbuild 20130121. At your service.
- pt_br.zip build 2013-01-18 18:55 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301140225-alt1
- repocop cronbuild 20130114. At your service.
- pt_br.zip build 2013-01-14 02:25 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301020129-alt1
- repocop cronbuild 20130107. At your service.
- pt_br.zip build 2013-01-02 01:29 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212201801-alt1
- repocop cronbuild 20121224. At your service.
- pt_br.zip build 2012-12-20 18:01 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212141431-alt1
- repocop cronbuild 20121217. At your service.
- pt_br.zip build 2012-12-14 14:31 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212071943-alt1
- repocop cronbuild 20121210. At your service.
- pt_br.zip build 2012-12-07 19:43 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211301902-alt1
- repocop cronbuild 20121203. At your service.
- pt_br.zip build 2012-11-30 19:02 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211191343-alt1
- repocop cronbuild 20121126. At your service.
- pt_br.zip build 2012-11-19 13:43 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211131910-alt1
- repocop cronbuild 20121119. At your service.
- pt_br.zip build 2012-11-13 19:10 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- pt_br.zip build 2012-11-01 07:00 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210221923-alt1
- repocop cronbuild 20121029. At your service.
- pt_br.zip build 2012-10-22 19:23 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210171546-alt1
- repocop cronbuild 20121022. At your service.
- pt_br.zip build 2012-10-17 15:46 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210102000-alt1
- repocop cronbuild 20121015. At your service.
- pt_br.zip build 2012-10-10 20:00 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210052033-alt1
- repocop cronbuild 20121008. At your service.
- pt_br.zip build 2012-10-05 20:33 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209300109-alt1
- repocop cronbuild 20121001. At your service.
- pt_br.zip build 2012-09-30 01:09 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209171854-alt1
- repocop cronbuild 20120918. At your service.
- pt_br.zip build 2012-09-17 18:54 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209112001-alt1
- repocop cronbuild 20120911. At your service.
- pt_br.zip build 2012-09-11 20:01 UTC

* Wed Sep 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208312048-alt1
- repocop cronbuild 20120905. At your service.
- pt_br.zip build 2012-08-31 20:48 UTC

* Wed Aug 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208271946-alt1
- repocop cronbuild 20120829. At your service.
- pt_br.zip build 2012-08-27 19:46 UTC

* Wed Aug 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208171315-alt1
- repocop cronbuild 20120822. At your service.
- pt_br.zip build 2012-08-17 13:15 UTC

* Wed Aug 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208132047-alt1
- repocop cronbuild 20120815. At your service.
- pt_br.zip build 2012-08-13 20:47 UTC

* Wed Aug 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208011438-alt1
- repocop cronbuild 20120808. At your service.
- pt_br.zip build 2012-08-01 14:38 UTC

* Wed Aug 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207301844-alt1
- repocop cronbuild 20120801. At your service.
- pt_br.zip build 2012-07-30 18:44 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207231809-alt1
- repocop cronbuild 20120724. At your service.
- pt_br.zip build 2012-07-23 18:09 UTC

* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206301742-alt1
- repocop cronbuild 20120704. At your service.
- pt_br.zip build 2012-06-30 17:42 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206222325-alt1
- repocop cronbuild 20120626. At your service.
- pt_br.zip build 2012-06-22 23:25 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206181525-alt1
- repocop cronbuild 20120619. At your service.
- pt_br.zip build 2012-06-18 15:25 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206120205-alt1
- repocop cronbuild 20120612. At your service.
- pt_br.zip build 2012-06-12 02:05 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206051613-alt1
- repocop cronbuild 20120605. At your service.
- pt_br.zip build 2012-06-05 16:13 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205292111-alt1
- repocop cronbuild 20120529. At your service.
- pt_br.zip build 2012-05-29 21:11 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205221523-alt1
- repocop cronbuild 20120522. At your service.
- pt_br.zip build 2012-05-22 15:23 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205141455-alt1
- repocop cronbuild 20120515. At your service.
- pt_br.zip build 2012-05-14 14:55 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205081915-alt1
- repocop cronbuild 20120508. At your service.
- pt_br.zip build 2012-05-08 19:15 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- pt_br.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204242057-alt1
- repocop cronbuild 20120424. At your service.
- pt_br.zip build 2012-04-24 20:57 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204162125-alt1
- repocop cronbuild 20120417. At your service.
- pt_br.zip build 2012-04-16 21:25 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204101350-alt1
- repocop cronbuild 20120410. At your service.
- pt_br.zip build 2012-04-10 13:50 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204031852-alt1
- repocop cronbuild 20120403. At your service.
- pt_br.zip build 2012-04-03 18:52 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203272132-alt1
- repocop cronbuild 20120327. At your service.
- pt_br.zip build 2012-03-27 21:32 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203201950-alt1
- repocop cronbuild 20120320. At your service.
- pt_br.zip build 2012-03-20 19:50 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203191345-alt1
- Rename package to moodle2.2-lang-pt_br
- pt_br.zip build 2012-03-19 13:45 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203191345-alt1
- repocop cronbuild 20120320. At your service.
- pt_br.zip build 2012-03-19 13:45 UTC

* Tue Mar 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203100221-alt1
- repocop cronbuild 20120313. At your service.
- pt_br.zip build 2012-03-10 02:21 UTC

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203091409-alt1
- repocop cronbuild 20120309. At your service.
- pt_br.zip build 2012-03-09 14:09 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011855-alt1
- repocop cronbuild 20120302. At your service.
- pt_br.zip build 2012-03-01 18:55 UTC

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202102348-alt1
- repocop cronbuild 20120217. At your service.
- pt_br.zip build 2012-02-10 23:48 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202102118-alt1
- repocop cronbuild 20120210. At your service.
- pt_br.zip build 2012-02-10 21:18 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201301754-alt1
- repocop cronbuild 20120203. At your service.
- pt_br.zip build 2012-01-30 17:54 UTC

* Fri Jan 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201261540-alt1
- repocop cronbuild 20120127. At your service.
- pt_br.zip build 2012-01-26 15:40 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201192114-alt1
- repocop cronbuild 20120120. At your service.
- pt_br.zip build 2012-01-19 21:14 UTC

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201111834-alt1
- repocop cronbuild 20120113. At your service.
- pt_br.zip build 2012-01-11 18:34 UTC

* Fri Dec 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112292030-alt1
- repocop cronbuild 20111230. At your service.
- pt_br.zip build 2011-12-29 20:30 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- pt_br.zip build 2011-12-09 16:00 UTC

* Sat Nov 26 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111222047-alt1
- Rename package to moodle2.1-lang-pt_br
- pt_br.zip build 2011-11-22 20:47 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-pt
- pt.zip build 2011-11-02 19:30

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
