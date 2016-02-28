# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ja
%define packagversion 2.5.0
%define packagedate 201602240133
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Japanese
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-ja
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
ln -s -f $(relative %buildroot%_ttffontsdir/sazanami/gothic/sazanami-gothic.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Sun Feb 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602240133-alt1
- repocop cronbuild 20160228. At your service.
- ja.zip build 2016-02-24 01:33 UTC

* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602210745-alt1
- repocop cronbuild 20160221. At your service.
- ja.zip build 2016-02-21 07:45 UTC

* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602091221-alt1
- repocop cronbuild 20160214. At your service.
- ja.zip build 2016-02-09 12:21 UTC

* Sun Feb 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602041549-alt1
- repocop cronbuild 20160207. At your service.
- ja.zip build 2016-02-04 15:49 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601311205-alt1
- repocop cronbuild 20160131. At your service.
- ja.zip build 2016-01-31 12:05 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601241207-alt1
- repocop cronbuild 20160124. At your service.
- ja.zip build 2016-01-24 12:07 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201512140537-alt1
- repocop cronbuild 20151214. At your service.
- ja.zip build 2015-12-14 05:37 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201512061319-alt1
- repocop cronbuild 20151207. At your service.
- ja.zip build 2015-12-06 13:19 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511300438-alt1
- repocop cronbuild 20151130. At your service.
- ja.zip build 2015-11-30 04:38 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511220657-alt1
- repocop cronbuild 20151123. At your service.
- ja.zip build 2015-11-22 06:57 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511151411-alt1
- repocop cronbuild 20151116. At your service.
- ja.zip build 2015-11-15 14:11 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511080721-alt1
- repocop cronbuild 20151109. At your service.
- ja.zip build 2015-11-08 07:21 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511012320-alt1
- repocop cronbuild 20151102. At your service.
- ja.zip build 2015-11-01 23:20 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510251515-alt1
- repocop cronbuild 20151026. At your service.
- ja.zip build 2015-10-25 15:15 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510191012-alt1
- repocop cronbuild 20151019. At your service.
- ja.zip build 2015-10-19 10:12 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510091027-alt1
- repocop cronbuild 20151012. At your service.
- ja.zip build 2015-10-09 10:27 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509291130-alt1
- repocop cronbuild 20151005. At your service.
- ja.zip build 2015-09-29 11:30 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509251621-alt1
- repocop cronbuild 20150928. At your service.
- ja.zip build 2015-09-25 16:21 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509201547-alt1
- repocop cronbuild 20150921. At your service.
- ja.zip build 2015-09-20 15:47 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509140034-alt1
- repocop cronbuild 20150914. At your service.
- ja.zip build 2015-09-14 00:34 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509061544-alt1
- repocop cronbuild 20150907. At your service.
- ja.zip build 2015-09-06 15:44 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508301515-alt1
- repocop cronbuild 20150831. At your service.
- ja.zip build 2015-08-30 15:15 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508201608-alt1
- repocop cronbuild 20150823. At your service.
- ja.zip build 2015-08-20 16:08 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507291553-alt1
- repocop cronbuild 20150730. At your service.
- ja.zip build 2015-07-29 15:53 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507221546-alt1
- repocop cronbuild 20150723. At your service.
- ja.zip build 2015-07-22 15:46 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507150156-alt1
- repocop cronbuild 20150716. At your service.
- ja.zip build 2015-07-15 01:56 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507081558-alt1
- repocop cronbuild 20150709. At your service.
- ja.zip build 2015-07-08 15:58 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507012102-alt1
- repocop cronbuild 20150702. At your service.
- ja.zip build 2015-07-01 21:02 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506250103-alt1
- repocop cronbuild 20150625. At your service.
- ja.zip build 2015-06-25 01:03 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506180509-alt1
- repocop cronbuild 20150618. At your service.
- ja.zip build 2015-06-18 05:09 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506091500-alt1
- repocop cronbuild 20150611. At your service.
- ja.zip build 2015-06-09 15:00 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506041122-alt1
- repocop cronbuild 20150604. At your service.
- ja.zip build 2015-06-04 11:22 UTC

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505201651-alt1
- repocop cronbuild 20150522. At your service.
- ja.zip build 2015-05-20 16:51 UTC

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505141849-alt1
- repocop cronbuild 20150515. At your service.
- ja.zip build 2015-05-14 18:49 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505071439-alt1
- repocop cronbuild 20150508. At your service.
- ja.zip build 2015-05-07 14:39 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504301635-alt1
- repocop cronbuild 20150501. At your service.
- ja.zip build 2015-04-30 16:35 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504231832-alt1
- repocop cronbuild 20150424. At your service.
- ja.zip build 2015-04-23 18:32 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504161737-alt1
- repocop cronbuild 20150417. At your service.
- ja.zip build 2015-04-16 17:37 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504081541-alt1
- repocop cronbuild 20150410. At your service.
- ja.zip build 2015-04-08 15:41 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504012145-alt1
- repocop cronbuild 20150403. At your service.
- ja.zip build 2015-04-01 21:45 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503252013-alt1
- repocop cronbuild 20150327. At your service.
- ja.zip build 2015-03-25 20:13 UTC

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503200547-alt1
- repocop cronbuild 20150320. At your service.
- ja.zip build 2015-03-20 05:47 UTC

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503121559-alt1
- repocop cronbuild 20150313. At your service.
- ja.zip build 2015-03-12 15:59 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503052146-alt1
- repocop cronbuild 20150306. At your service.
- ja.zip build 2015-03-05 21:46 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502262107-alt1
- repocop cronbuild 20150227. At your service.
- ja.zip build 2015-02-26 21:07 UTC

* Fri Feb 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502190403-alt1
- repocop cronbuild 20150220. At your service.
- ja.zip build 2015-02-19 04:03 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502121204-alt1
- repocop cronbuild 20150213. At your service.
- ja.zip build 2015-02-12 12:04 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502051835-alt1
- repocop cronbuild 20150206. At your service.
- ja.zip build 2015-02-05 18:35 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501282308-alt1
- repocop cronbuild 20150130. At your service.
- ja.zip build 2015-01-28 23:08 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501221729-alt1
- repocop cronbuild 20150123. At your service.
- ja.zip build 2015-01-22 17:29 UTC

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501151608-alt1
- repocop cronbuild 20150116. At your service.
- ja.zip build 2015-01-15 16:08 UTC

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501080110-alt1
- repocop cronbuild 20150109. At your service.
- ja.zip build 2015-01-08 01:10 UTC

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501010823-alt1
- repocop cronbuild 20150102. At your service.
- ja.zip build 2015-01-01 08:23 UTC

* Fri Dec 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412251152-alt1
- repocop cronbuild 20141226. At your service.
- ja.zip build 2014-12-25 11:52 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412131435-alt1
- repocop cronbuild 20141219. At your service.
- ja.zip build 2014-12-13 14:35 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412080403-alt1
- repocop cronbuild 20141212. At your service.
- ja.zip build 2014-12-08 04:03 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411111634-alt1
- repocop cronbuild 20141114. At your service.
- ja.zip build 2014-11-11 16:34 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411050646-alt1
- repocop cronbuild 20141107. At your service.
- ja.zip build 2014-11-05 06:46 UTC

* Fri Oct 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410260926-alt1
- repocop cronbuild 20141031. At your service.
- ja.zip build 2014-10-26 09:26 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410200609-alt1
- repocop cronbuild 20141024. At your service.
- ja.zip build 2014-10-20 06:09 UTC

* Fri Oct 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410151759-alt1
- repocop cronbuild 20141017. At your service.
- ja.zip build 2014-10-15 17:59 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410082016-alt1
- repocop cronbuild 20141010. At your service.
- ja.zip build 2014-10-08 20:16 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409181352-alt1
- repocop cronbuild 20140919. At your service.
- ja.zip build 2014-09-18 13:52 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406112142-alt1
- repocop cronbuild 20140613. At your service.
- ja.zip build 2014-06-11 21:42 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405270857-alt1
- repocop cronbuild 20140530. At your service.
- ja.zip build 2014-05-27 08:57 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405170350-alt1
- repocop cronbuild 20140523. At your service.
- ja.zip build 2014-05-17 03:50 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405131346-alt1
- repocop cronbuild 20140516. At your service.
- ja.zip build 2014-05-13 13:46 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405090549-alt1
- repocop cronbuild 20140509. At your service.
- ja.zip build 2014-05-09 05:49 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405011752-alt1
- repocop cronbuild 20140502. At your service.
- ja.zip build 2014-05-01 17:52 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404231621-alt1
- repocop cronbuild 20140425. At your service.
- ja.zip build 2014-04-23 16:21 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404180044-alt1
- repocop cronbuild 20140418. At your service.
- ja.zip build 2014-04-18 00:44 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404091730-alt1
- repocop cronbuild 20140411. At your service.
- ja.zip build 2014-04-09 17:30 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404040621-alt1
- repocop cronbuild 20140404. At your service.
- ja.zip build 2014-04-04 06:21 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403270754-alt1
- repocop cronbuild 20140328. At your service.
- ja.zip build 2014-03-27 07:54 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403100722-alt1
- repocop cronbuild 20140314. At your service.
- ja.zip build 2014-03-10 07:22 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402281447-alt1
- repocop cronbuild 20140307. At your service.
- ja.zip build 2014-02-28 14:47 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402271348-alt1
- repocop cronbuild 20140228. At your service.
- ja.zip build 2014-02-27 13:48 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402201544-alt1
- repocop cronbuild 20140221. At your service.
- ja.zip build 2014-02-20 15:44 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401261505-alt1
- repocop cronbuild 20140131. At your service.
- ja.zip build 2014-01-26 15:05 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401240438-alt1
- repocop cronbuild 20140124. At your service.
- ja.zip build 2014-01-24 04:38 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401170529-alt1
- repocop cronbuild 20140117. At your service.
- ja.zip build 2014-01-17 05:29 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312271406-alt1
- repocop cronbuild 20140103. At your service.
- ja.zip build 2013-12-27 14:06 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312210403-alt1
- repocop cronbuild 20131227. At your service.
- ja.zip build 2013-12-21 04:03 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- ja.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312060256-alt1
- repocop cronbuild 20131206. At your service.
- ja.zip build 2013-12-06 02:56 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311262140-alt1
- repocop cronbuild 20131129. At your service.
- ja.zip build 2013-11-26 21:40 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311171644-alt1
- repocop cronbuild 20131122. At your service.
- ja.zip build 2013-11-17 16:44 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311131205-alt1
- repocop cronbuild 20131115. At your service.
- ja.zip build 2013-11-13 12:05 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311052351-alt1
- repocop cronbuild 20131108. At your service.
- ja.zip build 2013-11-05 23:51 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311010527-alt1
- repocop cronbuild 20131101. At your service.
- ja.zip build 2013-11-01 05:27 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310212226-alt1
- repocop cronbuild 20131025. At your service.
- ja.zip build 2013-10-21 22:26 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310170344-alt1
- repocop cronbuild 20131018. At your service.
- ja.zip build 2013-10-17 03:44 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310080437-alt1
- repocop cronbuild 20131011. At your service.
- ja.zip build 2013-10-08 04:37 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310010145-alt1
- repocop cronbuild 20131004. At your service.
- ja.zip build 2013-10-01 01:45 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309220612-alt1
- repocop cronbuild 20130927. At your service.
- ja.zip build 2013-09-22 06:12 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309151412-alt1
- repocop cronbuild 20130920. At your service.
- ja.zip build 2013-09-15 14:12 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309130557-alt1
- repocop cronbuild 20130913. At your service.
- ja.zip build 2013-09-13 05:57 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309060057-alt1
- repocop cronbuild 20130906. At your service.
- ja.zip build 2013-09-06 00:57 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308280521-alt1
- repocop cronbuild 20130831. At your service.
- ja.zip build 2013-08-28 05:21 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308080716-alt1
- repocop cronbuild 20130810. At your service.
- ja.zip build 2013-08-08 07:16 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307261541-alt1
- repocop cronbuild 20130727. At your service.
- ja.zip build 2013-07-26 15:41 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307121413-alt1
- repocop cronbuild 20130713. At your service.
- ja.zip build 2013-07-12 14:13 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307050615-alt1
- repocop cronbuild 20130706. At your service.
- ja.zip build 2013-07-05 06:15 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140511-alt1
- repocop cronbuild 20130615. At your service.
- ja.zip build 2013-06-14 05:11 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305292351-alt1
- Rename package to moodle2.5-lang-ja
- ja.zip build 2013-05-29 23:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305211301-alt1
- repocop cronbuild 20130524. At your service.
- ja.zip build 2013-05-21 13:01 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305110549-alt1
- repocop cronbuild 20130517. At your service.
- ja.zip build 2013-05-11 05:49 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305090117-alt1
- repocop cronbuild 20130509. At your service.
- ja.zip build 2013-05-09 01:17 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304172324-alt1
- Rename package to moodle2.4-lang-ja
- ja.zip build 2013-04-17 23:24 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304170448-alt1
- repocop cronbuild 20130417. At your service.
- ja.zip build 2013-04-17 04:48 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304090556-alt1
- repocop cronbuild 20130410. At your service.
- ja.zip build 2013-04-09 05:56 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303281553-alt1
- repocop cronbuild 20130403. At your service.
- ja.zip build 2013-03-28 15:53 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303260003-alt1
- repocop cronbuild 20130327. At your service.
- ja.zip build 2013-03-26 00:03 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303170425-alt1
- repocop cronbuild 20130320. At your service.
- ja.zip build 2013-03-17 04:25 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303082006-alt1
- repocop cronbuild 20130313. At your service.
- ja.zip build 2013-03-08 20:06 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302272115-alt1
- repocop cronbuild 20130304. At your service.
- ja.zip build 2013-02-27 21:15 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302231332-alt1
- repocop cronbuild 20130225. At your service.
- ja.zip build 2013-02-23 13:32 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302072122-alt1
- repocop cronbuild 20130211. At your service.
- ja.zip build 2013-02-07 21:22 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302030646-alt1
- repocop cronbuild 20130204. At your service.
- ja.zip build 2013-02-03 06:46 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301180541-alt1
- repocop cronbuild 20130121. At your service.
- ja.zip build 2013-01-18 05:41 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301111651-alt1
- repocop cronbuild 20130114. At your service.
- ja.zip build 2013-01-11 16:51 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301041636-alt1
- repocop cronbuild 20130107. At your service.
- ja.zip build 2013-01-04 16:36 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212300448-alt1
- repocop cronbuild 20121231. At your service.
- ja.zip build 2012-12-30 04:48 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212141527-alt1
- repocop cronbuild 20121217. At your service.
- ja.zip build 2012-12-14 15:27 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212090528-alt1
- repocop cronbuild 20121210. At your service.
- ja.zip build 2012-12-09 05:28 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211301916-alt1
- repocop cronbuild 20121203. At your service.
- ja.zip build 2012-11-30 19:16 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211250719-alt1
- repocop cronbuild 20121126. At your service.
- ja.zip build 2012-11-25 07:19 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211122023-alt1
- repocop cronbuild 20121119. At your service.
- ja.zip build 2012-11-12 20:23 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211061911-alt1
- repocop cronbuild 20121112. At your service.
- ja.zip build 2012-11-06 19:11 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211011615-alt1
- repocop cronbuild 20121105. At your service.
- ja.zip build 2012-11-01 16:15 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210182053-alt1
- repocop cronbuild 20121022. At your service.
- ja.zip build 2012-10-18 20:53 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210051552-alt1
- repocop cronbuild 20121008. At your service.
- ja.zip build 2012-10-05 15:52 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209271855-alt1
- repocop cronbuild 20121001. At your service.
- ja.zip build 2012-09-27 18:55 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209151147-alt1
- repocop cronbuild 20120918. At your service.
- ja.zip build 2012-09-15 11:47 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209090827-alt1
- repocop cronbuild 20120911. At your service.
- ja.zip build 2012-09-09 08:27 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311859-alt1
- repocop cronbuild 20120904. At your service.
- ja.zip build 2012-08-31 18:59 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208241912-alt1
- repocop cronbuild 20120828. At your service.
- ja.zip build 2012-08-24 19:12 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208102213-alt1
- repocop cronbuild 20120814. At your service.
- ja.zip build 2012-08-10 22:13 UTC

* Wed Aug 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208031508-alt1
- repocop cronbuild 20120808. At your service.
- ja.zip build 2012-08-03 15:08 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207261806-alt1
- repocop cronbuild 20120731. At your service.
- ja.zip build 2012-07-26 18:06 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207191042-alt1
- repocop cronbuild 20120724. At your service.
- ja.zip build 2012-07-19 10:42 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207130324-alt1
- repocop cronbuild 20120717. At your service.
- ja.zip build 2012-07-13 03:24 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207051747-alt1
- repocop cronbuild 20120710. At your service.
- ja.zip build 2012-07-05 17:47 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207021415-alt1
- repocop cronbuild 20120703. At your service.
- ja.zip build 2012-07-02 14:15 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206260057-alt1
- repocop cronbuild 20120626. At your service.
- ja.zip build 2012-06-26 00:57 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191841-alt1
- repocop cronbuild 20120619. At your service.
- ja.zip build 2012-06-19 18:41 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206122003-alt1
- repocop cronbuild 20120612. At your service.
- ja.zip build 2012-06-12 20:03 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205290230-alt1
- repocop cronbuild 20120529. At your service.
- ja.zip build 2012-05-29 02:30 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205220007-alt1
- repocop cronbuild 20120522. At your service.
- ja.zip build 2012-05-22 00:07 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205131609-alt1
- repocop cronbuild 20120515. At your service.
- ja.zip build 2012-05-13 16:09 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205081813-alt1
- repocop cronbuild 20120508. At your service.
- ja.zip build 2012-05-08 18:13 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204290553-alt1
- repocop cronbuild 20120501. At your service.
- ja.zip build 2012-04-29 05:53 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204200621-alt1
- repocop cronbuild 20120424. At your service.
- ja.zip build 2012-04-20 06:21 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204171536-alt1
- repocop cronbuild 20120417. At your service.
- ja.zip build 2012-04-17 15:36 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203291353-alt1
- repocop cronbuild 20120403. At your service.
- ja.zip build 2012-03-29 13:53 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203251650-alt1
- repocop cronbuild 20120327. At your service.
- ja.zip build 2012-03-25 16:50 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203151448-alt1
- Rename package to moodle2.2-lang-ja
- ja.zip build 2012-03-15 14:48 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203151449-alt1
- repocop cronbuild 20120320. At your service.
- ja.zip build 2012-03-15 14:49 UTC

* Tue Mar 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203091645-alt1
- repocop cronbuild 20120313. At your service.
- ja.zip build 2012-03-09 16:45 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120307. At your service.
- ja.zip build 2012-03-01 11:00 UTC

* Wed Feb 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202241819-alt1
- repocop cronbuild 20120229. At your service.
- ja.zip build 2012-02-24 18:19 UTC

* Wed Feb 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202172003-alt1
- repocop cronbuild 20120222. At your service.
- ja.zip build 2012-02-17 20:03 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202131205-alt1
- repocop cronbuild 20120215. At your service.
- ja.zip build 2012-02-13 12:05 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201280622-alt1
- repocop cronbuild 20120201. At your service.
- ja.zip build 2012-01-28 06:22 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201251804-alt1
- repocop cronbuild 20120125. At your service.
- ja.zip build 2012-01-25 18:04 UTC

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201121404-alt1
- repocop cronbuild 20120118. At your service.
- ja.zip build 2012-01-12 14:04 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201062040-alt1
- repocop cronbuild 20120111. At your service.
- ja.zip build 2012-01-06 20:40 UTC

* Wed Dec 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112260049-alt1
- repocop cronbuild 20111228. At your service.
- ja.zip build 2011-12-26 00:49 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112211928-alt1
- repocop cronbuild 20111221. At your service.
- ja.zip build 2011-12-21 19:28 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112142037-alt1
- repocop cronbuild 20111214. At your service.
- ja.zip build 2011-12-14 20:37 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112011705-alt1
- repocop cronbuild 20111207. At your service.
- ja.zip build 2011-12-01 17:05 UTC

* Thu Dec 01 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111301536-alt1
- repocop cronbuild 20111201. At your service.
- ja.zip build 2011-11-30 15:36 UTC

* Mon Nov 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111280210-alt1
- repocop cronbuild 20111128. At your service.
- ja.zip build 2011-11-28 02:10 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111241342-alt1
- Rename package to moodle2.1-lang-ja
- ja.zip build 2011-11-24 13:42 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111151726-alt2
- Fix requires

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151726-alt1
- repocop cronbuild 20111116. At your service.
- ja.zip build 2011-11-15 17:26 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031658-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031658-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111031658-alt1
- repocop cronbuild 20111105. At your service.
- ja.zip build 2011-11-03 16:58 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt2
- Update for cronbuild use

* Mon Oct 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt1
- ja.zip build 2011-10-24 16:31 UTC

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110202137-alt1
- ja.zip build 2011-10-20 21:37 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110041726-alt1
- ja.zip build 2011-10-04 17:26 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109272111-alt1
- ja.zip build 2011-09-27 21:11 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109261912-alt1
- ja.zip build 2011-09-26 19:12 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109222056-alt1
- ja.zip build 2011-09-22 20:56 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109212035-alt1
- ja.zip build 2011-09-21 20:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- ja.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109181907-alt1
- ja.zip build 2011-09-18 19:07 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109151910-alt1
- ja.zip build 2011-09-15 19:10 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141837-alt1
- ja.zip build 2011-09-14 18:37 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109131809-alt1
- ja.zip build 2011-09-13 18:09 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109121803-alt1
- ja.zip build 2011-09-12 18:03 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109111621-alt1
- ja.zip build 2011-09-11 16:21 UTC

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109090331-alt1
- ja.zip build 2011-09-09 03:31 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109070502-alt1
- ja.zip build 2011-09-07 05:02 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108231816-alt1
- ja.zip build 2011-08-23 18:16 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108222128-alt1
- ja.zip build 2011-08-22 21:28 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108220123-alt1
- ja.zip build 2011-08-22 01:23 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108191757-alt1
- ja.zip build 2011-08-19 17:57 UTC

* Fri Aug 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108181726-alt1
- ja.zip build 2011-08-18 17:26 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108171909-alt1
- ja.zip build 2011-08-17 19:09 UTC

* Wed Aug 17 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161743-alt1
- ja.zip build 2011-08-16 17:43 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108152131-alt1
- ja.zip build 2011-08-15 21:31 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108121459-alt1
- Rename package to moodle2.0-lang-ja
- ja.zip build 2011-08-12 14:59 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110809-alt1
- ja_utf8.zip build 2011-08-09
- Add %%moodle_langdir/ja_utf8/fonts/default.ttf

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081210
- new build for ALT Linux from cvs
