# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ja
%define packagversion 2.0.0
%define packagedate 201602251232
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Japanese
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-ja
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
* Sun Feb 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602251232-alt1
- repocop cronbuild 20160228. At your service.
- ja.zip build 2016-02-25 12:32 UTC

* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602161426-alt1
- repocop cronbuild 20160221. At your service.
- ja.zip build 2016-02-16 14:26 UTC

* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602091221-alt1
- repocop cronbuild 20160214. At your service.
- ja.zip build 2016-02-09 12:21 UTC

* Sun Feb 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602041549-alt1
- repocop cronbuild 20160207. At your service.
- ja.zip build 2016-02-04 15:49 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601241207-alt1
- repocop cronbuild 20160131. At your service.
- ja.zip build 2016-01-24 12:07 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601221016-alt1
- repocop cronbuild 20160124. At your service.
- ja.zip build 2016-01-22 10:16 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512130610-alt1
- repocop cronbuild 20151214. At your service.
- ja.zip build 2015-12-13 06:10 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512061319-alt1
- repocop cronbuild 20151207. At your service.
- ja.zip build 2015-12-06 13:19 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511300438-alt1
- repocop cronbuild 20151130. At your service.
- ja.zip build 2015-11-30 04:38 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511220657-alt1
- repocop cronbuild 20151123. At your service.
- ja.zip build 2015-11-22 06:57 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511141540-alt1
- repocop cronbuild 20151116. At your service.
- ja.zip build 2015-11-14 15:40 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511080721-alt1
- repocop cronbuild 20151109. At your service.
- ja.zip build 2015-11-08 07:21 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511012320-alt1
- repocop cronbuild 20151102. At your service.
- ja.zip build 2015-11-01 23:20 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510251515-alt1
- repocop cronbuild 20151026. At your service.
- ja.zip build 2015-10-25 15:15 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510161536-alt1
- repocop cronbuild 20151019. At your service.
- ja.zip build 2015-10-16 15:36 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510061534-alt1
- repocop cronbuild 20151012. At your service.
- ja.zip build 2015-10-06 15:34 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509251621-alt1
- repocop cronbuild 20150928. At your service.
- ja.zip build 2015-09-25 16:21 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509201547-alt1
- repocop cronbuild 20150921. At your service.
- ja.zip build 2015-09-20 15:47 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509140034-alt1
- repocop cronbuild 20150914. At your service.
- ja.zip build 2015-09-14 00:34 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509061544-alt1
- repocop cronbuild 20150907. At your service.
- ja.zip build 2015-09-06 15:44 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508201608-alt1
- repocop cronbuild 20150823. At your service.
- ja.zip build 2015-08-20 16:08 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507291553-alt1
- repocop cronbuild 20150730. At your service.
- ja.zip build 2015-07-29 15:53 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507221546-alt1
- repocop cronbuild 20150723. At your service.
- ja.zip build 2015-07-22 15:46 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507150156-alt1
- repocop cronbuild 20150716. At your service.
- ja.zip build 2015-07-15 01:56 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507081558-alt1
- repocop cronbuild 20150709. At your service.
- ja.zip build 2015-07-08 15:58 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506301551-alt1
- repocop cronbuild 20150702. At your service.
- ja.zip build 2015-06-30 15:51 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506250103-alt1
- repocop cronbuild 20150625. At your service.
- ja.zip build 2015-06-25 01:03 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506161653-alt1
- repocop cronbuild 20150618. At your service.
- ja.zip build 2015-06-16 16:53 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506081602-alt1
- repocop cronbuild 20150611. At your service.
- ja.zip build 2015-06-08 16:02 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506040034-alt1
- repocop cronbuild 20150604. At your service.
- ja.zip build 2015-06-04 00:34 UTC

* Sat May 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505201651-alt1
- repocop cronbuild 20150523. At your service.
- ja.zip build 2015-05-20 16:51 UTC

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505141849-alt1
- repocop cronbuild 20150515. At your service.
- ja.zip build 2015-05-14 18:49 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505071439-alt1
- repocop cronbuild 20150508. At your service.
- ja.zip build 2015-05-07 14:39 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504301635-alt1
- repocop cronbuild 20150501. At your service.
- ja.zip build 2015-04-30 16:35 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504231832-alt1
- repocop cronbuild 20150424. At your service.
- ja.zip build 2015-04-23 18:32 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504161737-alt1
- repocop cronbuild 20150417. At your service.
- ja.zip build 2015-04-16 17:37 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504081541-alt1
- repocop cronbuild 20150410. At your service.
- ja.zip build 2015-04-08 15:41 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504012145-alt1
- repocop cronbuild 20150403. At your service.
- ja.zip build 2015-04-01 21:45 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503252013-alt1
- repocop cronbuild 20150327. At your service.
- ja.zip build 2015-03-25 20:13 UTC

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503192014-alt1
- repocop cronbuild 20150320. At your service.
- ja.zip build 2015-03-19 20:14 UTC

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503121559-alt1
- repocop cronbuild 20150313. At your service.
- ja.zip build 2015-03-12 15:59 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503052146-alt1
- repocop cronbuild 20150306. At your service.
- ja.zip build 2015-03-05 21:46 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502261326-alt1
- repocop cronbuild 20150227. At your service.
- ja.zip build 2015-02-26 13:26 UTC

* Fri Feb 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502190403-alt1
- repocop cronbuild 20150220. At your service.
- ja.zip build 2015-02-19 04:03 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502112152-alt1
- repocop cronbuild 20150213. At your service.
- ja.zip build 2015-02-11 21:52 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502051835-alt1
- repocop cronbuild 20150206. At your service.
- ja.zip build 2015-02-05 18:35 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501282308-alt1
- repocop cronbuild 20150130. At your service.
- ja.zip build 2015-01-28 23:08 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501221729-alt1
- repocop cronbuild 20150123. At your service.
- ja.zip build 2015-01-22 17:29 UTC

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501151608-alt1
- repocop cronbuild 20150116. At your service.
- ja.zip build 2015-01-15 16:08 UTC

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501080110-alt1
- repocop cronbuild 20150109. At your service.
- ja.zip build 2015-01-08 01:10 UTC

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501010823-alt1
- repocop cronbuild 20150102. At your service.
- ja.zip build 2015-01-01 08:23 UTC

* Fri Dec 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412211557-alt1
- repocop cronbuild 20141226. At your service.
- ja.zip build 2014-12-21 15:57 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412131435-alt1
- repocop cronbuild 20141219. At your service.
- ja.zip build 2014-12-13 14:35 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412080403-alt1
- repocop cronbuild 20141211. At your service.
- ja.zip build 2014-12-08 04:03 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411111634-alt1
- repocop cronbuild 20141114. At your service.
- ja.zip build 2014-11-11 16:34 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411050646-alt1
- repocop cronbuild 20141107. At your service.
- ja.zip build 2014-11-05 06:46 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410200609-alt1
- repocop cronbuild 20141024. At your service.
- ja.zip build 2014-10-20 06:09 UTC

* Thu Oct 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410151759-alt1
- repocop cronbuild 20141016. At your service.
- ja.zip build 2014-10-15 17:59 UTC

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409181352-alt1
- repocop cronbuild 20140918. At your service.
- ja.zip build 2014-09-18 13:52 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405170350-alt1
- repocop cronbuild 20140523. At your service.
- ja.zip build 2014-05-17 03:50 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405131347-alt1
- repocop cronbuild 20140516. At your service.
- ja.zip build 2014-05-13 13:47 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405051841-alt1
- repocop cronbuild 20140509. At your service.
- ja.zip build 2014-05-05 18:41 UTC

* Thu May 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404301458-alt1
- repocop cronbuild 20140501. At your service.
- ja.zip build 2014-04-30 14:58 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404160709-alt1
- repocop cronbuild 20140418. At your service.
- ja.zip build 2014-04-16 07:09 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404091730-alt1
- repocop cronbuild 20140411. At your service.
- ja.zip build 2014-04-09 17:30 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404030430-alt1
- repocop cronbuild 20140404. At your service.
- ja.zip build 2014-04-03 04:30 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403091330-alt1
- repocop cronbuild 20140314. At your service.
- ja.zip build 2014-03-09 13:30 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402281447-alt1
- repocop cronbuild 20140307. At your service.
- ja.zip build 2014-02-28 14:47 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402201544-alt1
- repocop cronbuild 20140221. At your service.
- ja.zip build 2014-02-20 15:44 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402101932-alt1
- repocop cronbuild 20140214. At your service.
- ja.zip build 2014-02-10 19:32 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311262144-alt1
- repocop cronbuild 20131129. At your service.
- ja.zip build 2013-11-26 21:44 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311171644-alt1
- repocop cronbuild 20131122. At your service.
- ja.zip build 2013-11-17 16:44 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311011354-alt1
- repocop cronbuild 20131108. At your service.
- ja.zip build 2013-11-01 13:54 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310310503-alt1
- repocop cronbuild 20131101. At your service.
- ja.zip build 2013-10-31 05:03 UTC

* Thu Oct 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310212227-alt1
- repocop cronbuild 20131024. At your service.
- ja.zip build 2013-10-21 22:27 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310010157-alt1
- repocop cronbuild 20131004. At your service.
- ja.zip build 2013-10-01 01:57 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309220612-alt1
- repocop cronbuild 20130927. At your service.
- ja.zip build 2013-09-22 06:12 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309090639-alt1
- repocop cronbuild 20130913. At your service.
- ja.zip build 2013-09-09 06:39 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305272240-alt1
- repocop cronbuild 20130531. At your service.
- ja.zip build 2013-05-27 22:40 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305200103-alt1
- repocop cronbuild 20130524. At your service.
- ja.zip build 2013-05-20 01:03 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305090117-alt1
- repocop cronbuild 20130509. At your service.
- ja.zip build 2013-05-09 01:17 UTC

* Tue Apr 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304090556-alt1
- repocop cronbuild 20130409. At your service.
- ja.zip build 2013-04-09 05:56 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303260003-alt1
- repocop cronbuild 20130327. At your service.
- ja.zip build 2013-03-26 00:03 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303082006-alt1
- repocop cronbuild 20130313. At your service.
- ja.zip build 2013-03-08 20:06 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302072122-alt1
- repocop cronbuild 20130211. At your service.
- ja.zip build 2013-02-07 21:22 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302030525-alt1
- repocop cronbuild 20130204. At your service.
- ja.zip build 2013-02-03 05:25 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301041636-alt1
- repocop cronbuild 20130107. At your service.
- ja.zip build 2013-01-04 16:36 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212090528-alt1
- repocop cronbuild 20121210. At your service.
- ja.zip build 2012-12-09 05:28 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211231905-alt1
- repocop cronbuild 20121126. At your service.
- ja.zip build 2012-11-23 19:05 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211122023-alt1
- repocop cronbuild 20121119. At your service.
- ja.zip build 2012-11-12 20:23 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211061911-alt1
- repocop cronbuild 20121112. At your service.
- ja.zip build 2012-11-06 19:11 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209141356-alt1
- repocop cronbuild 20120917. At your service.
- ja.zip build 2012-09-14 13:56 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209090827-alt1
- repocop cronbuild 20120910. At your service.
- ja.zip build 2012-09-09 08:27 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208311859-alt1
- repocop cronbuild 20120904. At your service.
- ja.zip build 2012-08-31 18:59 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208220409-alt1
- repocop cronbuild 20120828. At your service.
- ja.zip build 2012-08-22 04:09 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208031508-alt1
- repocop cronbuild 20120807. At your service.
- ja.zip build 2012-08-03 15:08 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207191042-alt1
- repocop cronbuild 20120724. At your service.
- ja.zip build 2012-07-19 10:42 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207030108-alt1
- repocop cronbuild 20120710. At your service.
- ja.zip build 2012-07-03 01:08 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206292034-alt1
- repocop cronbuild 20120703. At your service.
- ja.zip build 2012-06-29 20:34 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206251644-alt1
- repocop cronbuild 20120625. At your service.
- ja.zip build 2012-06-25 16:44 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206142054-alt1
- repocop cronbuild 20120618. At your service.
- ja.zip build 2012-06-14 20:54 UTC

* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206111753-alt1
- repocop cronbuild 20120611. At your service.
- ja.zip build 2012-06-11 17:53 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205271605-alt1
- repocop cronbuild 20120528. At your service.
- ja.zip build 2012-05-27 16:05 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205081813-alt1
- repocop cronbuild 20120514. At your service.
- ja.zip build 2012-05-08 18:13 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205020320-alt1
- repocop cronbuild 20120507. At your service.
- ja.zip build 2012-05-02 03:20 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204171536-alt1
- repocop cronbuild 20120423. At your service.
- ja.zip build 2012-04-17 15:36 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204111524-alt1
- repocop cronbuild 20120416. At your service.
- ja.zip build 2012-04-11 15:24 UTC

* Wed Feb 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202172005-alt1
- repocop cronbuild 20120222. At your service.
- ja.zip build 2012-02-17 20:05 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202131158-alt1
- repocop cronbuild 20120215. At your service.
- ja.zip build 2012-02-13 11:58 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201251804-alt1
- repocop cronbuild 20120125. At your service.
- ja.zip build 2012-01-25 18:04 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201062044-alt1
- repocop cronbuild 20120111. At your service.
- ja.zip build 2012-01-06 20:44 UTC

* Wed Dec 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112260047-alt1
- repocop cronbuild 20111228. At your service.
- ja.zip build 2011-12-26 00:47 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112211927-alt1
- repocop cronbuild 20111221. At your service.
- ja.zip build 2011-12-21 19:27 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112132222-alt1
- repocop cronbuild 20111214. At your service.
- ja.zip build 2011-12-13 22:22 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112011705-alt1
- repocop cronbuild 20111207. At your service.
- ja.zip build 2011-12-01 17:05 UTC

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111301536-alt1
- repocop cronbuild 20111130. At your service.
- ja.zip build 2011-11-30 15:36 UTC

* Mon Nov 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111280210-alt1
- repocop cronbuild 20111128. At your service.
- ja.zip build 2011-11-28 02:10 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111241342-alt1
- repocop cronbuild 20111125. At your service.
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
