# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename zh_tw
%define packagversion 2.4.0
%define packagedate 201601250354
%define moodlebranch 2.4
%define moodlepackagename %moodle_name%moodlebranch
%define langname Chinese (Traditional/Big5)
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.4-lang-zh_tw
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
ln -s -f $(relative %buildroot%_ttffontsdir/chinese-big5/bkai00mp.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201601250354-alt1
- repocop cronbuild 20160131. At your service.
- zh_tw.zip build 2016-01-25 03:54 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201601190658-alt1
- repocop cronbuild 20160124. At your service.
- zh_tw.zip build 2016-01-19 06:58 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511251520-alt1
- repocop cronbuild 20151130. At your service.
- zh_tw.zip build 2015-11-25 15:20 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511220701-alt1
- repocop cronbuild 20151123. At your service.
- zh_tw.zip build 2015-11-22 07:01 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511142033-alt1
- repocop cronbuild 20151116. At your service.
- zh_tw.zip build 2015-11-14 20:33 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511081538-alt1
- repocop cronbuild 20151109. At your service.
- zh_tw.zip build 2015-11-08 15:38 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511020616-alt1
- repocop cronbuild 20151102. At your service.
- zh_tw.zip build 2015-11-02 06:16 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510171611-alt1
- repocop cronbuild 20151019. At your service.
- zh_tw.zip build 2015-10-17 16:11 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510101551-alt1
- repocop cronbuild 20151012. At your service.
- zh_tw.zip build 2015-10-10 15:51 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510050828-alt1
- repocop cronbuild 20151005. At your service.
- zh_tw.zip build 2015-10-05 08:28 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201509171055-alt1
- repocop cronbuild 20150921. At your service.
- zh_tw.zip build 2015-09-17 10:55 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201508241100-alt1
- repocop cronbuild 20150831. At your service.
- zh_tw.zip build 2015-08-24 11:00 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507091632-alt1
- repocop cronbuild 20150716. At your service.
- zh_tw.zip build 2015-07-09 16:32 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201506120306-alt1
- repocop cronbuild 20150618. At your service.
- zh_tw.zip build 2015-06-12 03:06 UTC

* Sat May 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505131603-alt1
- repocop cronbuild 20150516. At your service.
- zh_tw.zip build 2015-05-13 16:03 UTC

* Sat May 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505071515-alt1
- repocop cronbuild 20150509. At your service.
- zh_tw.zip build 2015-05-07 15:15 UTC

* Sat May 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504291444-alt1
- repocop cronbuild 20150502. At your service.
- zh_tw.zip build 2015-04-29 14:44 UTC

* Sat Apr 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504241520-alt1
- repocop cronbuild 20150425. At your service.
- zh_tw.zip build 2015-04-24 15:20 UTC

* Sat Apr 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504170747-alt1
- repocop cronbuild 20150418. At your service.
- zh_tw.zip build 2015-04-17 07:47 UTC

* Sat Apr 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504110424-alt1
- repocop cronbuild 20150411. At your service.
- zh_tw.zip build 2015-04-11 04:24 UTC

* Sat Apr 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504011344-alt1
- repocop cronbuild 20150404. At your service.
- zh_tw.zip build 2015-04-01 13:44 UTC

* Sat Mar 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201503270609-alt1
- repocop cronbuild 20150328. At your service.
- zh_tw.zip build 2015-03-27 06:09 UTC

* Sat Mar 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201503120947-alt1
- repocop cronbuild 20150314. At your service.
- zh_tw.zip build 2015-03-12 09:47 UTC

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502250137-alt1
- repocop cronbuild 20150228. At your service.
- zh_tw.zip build 2015-02-25 01:37 UTC

* Sat Feb 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502130912-alt1
- repocop cronbuild 20150214. At your service.
- zh_tw.zip build 2015-02-13 09:12 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502061543-alt1
- repocop cronbuild 20150207. At your service.
- zh_tw.zip build 2015-02-06 15:43 UTC

* Sat Jan 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501201558-alt1
- repocop cronbuild 20150124. At your service.
- zh_tw.zip build 2015-01-20 15:58 UTC

* Sat Jan 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501081824-alt1
- repocop cronbuild 20150110. At your service.
- zh_tw.zip build 2015-01-08 18:24 UTC

* Sat Dec 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412171603-alt1
- repocop cronbuild 20141220. At your service.
- zh_tw.zip build 2014-12-17 16:03 UTC

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201410131559-alt1
- repocop cronbuild 20141018. At your service.
- zh_tw.zip build 2014-10-13 15:59 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201410110106-alt1
- repocop cronbuild 20141011. At your service.
- zh_tw.zip build 2014-10-11 01:06 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201408271634-alt1
- repocop cronbuild 20140913. At your service.
- zh_tw.zip build 2014-08-27 16:34 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406300221-alt1
- repocop cronbuild 20140705. At your service.
- zh_tw.zip build 2014-06-30 02:21 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406221543-alt1
- repocop cronbuild 20140628. At your service.
- zh_tw.zip build 2014-06-22 15:43 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406161549-alt1
- repocop cronbuild 20140621. At your service.
- zh_tw.zip build 2014-06-16 15:49 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406112128-alt1
- repocop cronbuild 20140613. At your service.
- zh_tw.zip build 2014-06-11 21:28 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406060723-alt1
- repocop cronbuild 20140606. At your service.
- zh_tw.zip build 2014-06-06 07:23 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405241212-alt1
- repocop cronbuild 20140530. At your service.
- zh_tw.zip build 2014-05-24 12:12 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405181713-alt1
- repocop cronbuild 20140523. At your service.
- zh_tw.zip build 2014-05-18 17:13 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405130130-alt1
- repocop cronbuild 20140516. At your service.
- zh_tw.zip build 2014-05-13 01:30 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405011702-alt1
- repocop cronbuild 20140509. At your service.
- zh_tw.zip build 2014-05-01 17:02 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404151633-alt1
- repocop cronbuild 20140418. At your service.
- zh_tw.zip build 2014-04-15 16:33 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404101738-alt1
- repocop cronbuild 20140411. At your service.
- zh_tw.zip build 2014-04-10 17:38 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403310334-alt1
- repocop cronbuild 20140404. At your service.
- zh_tw.zip build 2014-03-31 03:34 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403260535-alt1
- repocop cronbuild 20140328. At your service.
- zh_tw.zip build 2014-03-26 05:35 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403191726-alt1
- repocop cronbuild 20140321. At your service.
- zh_tw.zip build 2014-03-19 17:26 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403140136-alt1
- repocop cronbuild 20140314. At your service.
- zh_tw.zip build 2014-03-14 01:36 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403022033-alt1
- repocop cronbuild 20140307. At your service.
- zh_tw.zip build 2014-03-02 20:33 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402271701-alt1
- repocop cronbuild 20140228. At your service.
- zh_tw.zip build 2014-02-27 17:01 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402180734-alt1
- repocop cronbuild 20140221. At your service.
- zh_tw.zip build 2014-02-18 07:34 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402041244-alt1
- repocop cronbuild 20140207. At your service.
- zh_tw.zip build 2014-02-04 12:44 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401271555-alt1
- repocop cronbuild 20140131. At your service.
- zh_tw.zip build 2014-01-27 15:55 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401231731-alt1
- repocop cronbuild 20140124. At your service.
- zh_tw.zip build 2014-01-23 17:31 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401112139-alt1
- repocop cronbuild 20140117. At your service.
- zh_tw.zip build 2014-01-11 21:39 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312291709-alt1
- repocop cronbuild 20140103. At your service.
- zh_tw.zip build 2013-12-29 17:09 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312261738-alt1
- repocop cronbuild 20131227. At your service.
- zh_tw.zip build 2013-12-26 17:38 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312191656-alt1
- repocop cronbuild 20131220. At your service.
- zh_tw.zip build 2013-12-19 16:56 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- zh_tw.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312051555-alt1
- repocop cronbuild 20131206. At your service.
- zh_tw.zip build 2013-12-05 15:55 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311271509-alt1
- repocop cronbuild 20131129. At your service.
- zh_tw.zip build 2013-11-27 15:09 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311181559-alt1
- repocop cronbuild 20131122. At your service.
- zh_tw.zip build 2013-11-18 15:59 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311141315-alt1
- repocop cronbuild 20131115. At your service.
- zh_tw.zip build 2013-11-14 13:15 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311071522-alt1
- repocop cronbuild 20131108. At your service.
- zh_tw.zip build 2013-11-07 15:22 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310270422-alt1
- repocop cronbuild 20131101. At your service.
- zh_tw.zip build 2013-10-27 04:22 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310230622-alt1
- repocop cronbuild 20131025. At your service.
- zh_tw.zip build 2013-10-23 06:22 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310170356-alt1
- repocop cronbuild 20131018. At your service.
- zh_tw.zip build 2013-10-17 03:56 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310021109-alt1
- repocop cronbuild 20131004. At your service.
- zh_tw.zip build 2013-10-02 11:09 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309221601-alt1
- repocop cronbuild 20130927. At your service.
- zh_tw.zip build 2013-09-22 16:01 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309191102-alt1
- repocop cronbuild 20130920. At your service.
- zh_tw.zip build 2013-09-19 11:02 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309090538-alt1
- repocop cronbuild 20130913. At your service.
- zh_tw.zip build 2013-09-09 05:38 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309061024-alt1
- repocop cronbuild 20130906. At your service.
- zh_tw.zip build 2013-09-06 10:24 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308261615-alt1
- repocop cronbuild 20130830. At your service.
- zh_tw.zip build 2013-08-26 16:15 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307030346-alt1
- repocop cronbuild 20130705. At your service.
- zh_tw.zip build 2013-07-03 03:46 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306060511-alt1
- repocop cronbuild 20130607. At your service.
- zh_tw.zip build 2013-06-06 05:11 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305222323-alt1
- repocop cronbuild 20130524. At your service.
- zh_tw.zip build 2013-05-22 23:23 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305070819-alt1
- repocop cronbuild 20130509. At your service.
- zh_tw.zip build 2013-05-07 08:19 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304080842-alt1
- Rename package to moodle2.4-lang-zh_tw
- zh_tw.zip build 2013-04-08 08:42 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303190756-alt1
- repocop cronbuild 20130320. At your service.
- zh_tw.zip build 2013-03-19 07:56 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- zh_tw.zip build 2013-01-26 15:39 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212220847-alt1
- repocop cronbuild 20121224. At your service.
- zh_tw.zip build 2012-12-22 08:47 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211061331-alt1
- repocop cronbuild 20121112. At your service.
- zh_tw.zip build 2012-11-06 13:31 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211031752-alt1
- repocop cronbuild 20121105. At your service.
- zh_tw.zip build 2012-11-03 17:52 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- zh_tw.zip build 2012-05-23 15:49 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- zh_tw.zip build 2012-05-11 11:00 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201202260922-alt1
- Rename package to moodle2.2-lang-zh_tw
- zh_tw.zip build 2012-02-26 09:22 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201291011-alt1
- repocop cronbuild 20120203. At your service.
- zh_tw.zip build 2012-01-29 10:11 UTC

* Sat Dec 10 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111210. At your service.
- zh_tw.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-zh_tw
- zh_tw.zip build 2011-11-02 19:30 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use %%_ttffontsdir/chinese-big5/bkai00mp.ttf for
  %%moodle_langdir/zh_tw/fonts/default.ttf
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- zh_tw.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- zh_tw.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-zh_tw
- zh_tw.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- zh_tw_utf8.zip build 2010-05-26

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20080926
- new build for ALT Linux from cvs
