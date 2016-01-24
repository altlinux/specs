# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename zh_tw
%define packagversion 2.5.0
%define packagedate 201601190658
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Chinese (Traditional/Big5)
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-zh_tw
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
ln -s -f $(relative %buildroot%_ttffontsdir/chinese-big5/bkai00mp.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601190658-alt1
- repocop cronbuild 20160124. At your service.
- zh_tw.zip build 2016-01-19 06:58 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511251520-alt1
- repocop cronbuild 20151130. At your service.
- zh_tw.zip build 2015-11-25 15:20 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511220701-alt1
- repocop cronbuild 20151123. At your service.
- zh_tw.zip build 2015-11-22 07:01 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511142033-alt1
- repocop cronbuild 20151116. At your service.
- zh_tw.zip build 2015-11-14 20:33 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511081538-alt1
- repocop cronbuild 20151109. At your service.
- zh_tw.zip build 2015-11-08 15:38 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511020616-alt1
- repocop cronbuild 20151102. At your service.
- zh_tw.zip build 2015-11-02 06:16 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510171611-alt1
- repocop cronbuild 20151019. At your service.
- zh_tw.zip build 2015-10-17 16:11 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510101551-alt1
- repocop cronbuild 20151012. At your service.
- zh_tw.zip build 2015-10-10 15:51 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510050828-alt1
- repocop cronbuild 20151005. At your service.
- zh_tw.zip build 2015-10-05 08:28 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509171055-alt1
- repocop cronbuild 20150921. At your service.
- zh_tw.zip build 2015-09-17 10:55 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508241058-alt1
- repocop cronbuild 20150831. At your service.
- zh_tw.zip build 2015-08-24 10:58 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508031958-alt1
- repocop cronbuild 20150823. At your service.
- zh_tw.zip build 2015-08-03 19:58 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507091632-alt1
- repocop cronbuild 20150716. At your service.
- zh_tw.zip build 2015-07-09 16:32 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506120306-alt1
- repocop cronbuild 20150618. At your service.
- zh_tw.zip build 2015-06-12 03:06 UTC

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505131604-alt1
- repocop cronbuild 20150515. At your service.
- zh_tw.zip build 2015-05-13 16:04 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505071515-alt1
- repocop cronbuild 20150508. At your service.
- zh_tw.zip build 2015-05-07 15:15 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504291444-alt1
- repocop cronbuild 20150501. At your service.
- zh_tw.zip build 2015-04-29 14:44 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504191613-alt1
- repocop cronbuild 20150424. At your service.
- zh_tw.zip build 2015-04-19 16:13 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504170747-alt1
- repocop cronbuild 20150417. At your service.
- zh_tw.zip build 2015-04-17 07:47 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504080947-alt1
- repocop cronbuild 20150410. At your service.
- zh_tw.zip build 2015-04-08 09:47 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504011440-alt1
- repocop cronbuild 20150403. At your service.
- zh_tw.zip build 2015-04-01 14:40 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503270609-alt1
- repocop cronbuild 20150327. At your service.
- zh_tw.zip build 2015-03-27 06:09 UTC

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503171348-alt1
- repocop cronbuild 20150320. At your service.
- zh_tw.zip build 2015-03-17 13:48 UTC

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503120947-alt1
- repocop cronbuild 20150313. At your service.
- zh_tw.zip build 2015-03-12 09:47 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502250137-alt1
- repocop cronbuild 20150227. At your service.
- zh_tw.zip build 2015-02-25 01:37 UTC

* Fri Feb 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502170921-alt1
- repocop cronbuild 20150220. At your service.
- zh_tw.zip build 2015-02-17 09:21 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502120901-alt1
- repocop cronbuild 20150213. At your service.
- zh_tw.zip build 2015-02-12 09:01 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502051431-alt1
- repocop cronbuild 20150206. At your service.
- zh_tw.zip build 2015-02-05 14:31 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501260637-alt1
- repocop cronbuild 20150130. At your service.
- zh_tw.zip build 2015-01-26 06:37 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501201558-alt1
- repocop cronbuild 20150123. At your service.
- zh_tw.zip build 2015-01-20 15:58 UTC

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501081824-alt1
- repocop cronbuild 20150109. At your service.
- zh_tw.zip build 2015-01-08 18:24 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412171603-alt1
- repocop cronbuild 20141219. At your service.
- zh_tw.zip build 2014-12-17 16:03 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410310834-alt1
- repocop cronbuild 20141107. At your service.
- zh_tw.zip build 2014-10-31 08:34 UTC

* Fri Oct 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410131559-alt1
- repocop cronbuild 20141017. At your service.
- zh_tw.zip build 2014-10-13 15:59 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410100546-alt1
- repocop cronbuild 20141010. At your service.
- zh_tw.zip build 2014-10-10 05:46 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409271502-alt1
- repocop cronbuild 20141003. At your service.
- zh_tw.zip build 2014-09-27 15:02 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409140806-alt1
- repocop cronbuild 20140919. At your service.
- zh_tw.zip build 2014-09-14 08:06 UTC

* Fri Sep 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201408271634-alt1
- repocop cronbuild 20140912. At your service.
- zh_tw.zip build 2014-08-27 16:34 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406300221-alt1
- repocop cronbuild 20140705. At your service.
- zh_tw.zip build 2014-06-30 02:21 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406221543-alt1
- repocop cronbuild 20140628. At your service.
- zh_tw.zip build 2014-06-22 15:43 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406161549-alt1
- repocop cronbuild 20140621. At your service.
- zh_tw.zip build 2014-06-16 15:49 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406112142-alt1
- repocop cronbuild 20140613. At your service.
- zh_tw.zip build 2014-06-11 21:42 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406060723-alt1
- repocop cronbuild 20140606. At your service.
- zh_tw.zip build 2014-06-06 07:23 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405241212-alt1
- repocop cronbuild 20140530. At your service.
- zh_tw.zip build 2014-05-24 12:12 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405181909-alt1
- repocop cronbuild 20140523. At your service.
- zh_tw.zip build 2014-05-18 19:09 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405130130-alt1
- repocop cronbuild 20140516. At your service.
- zh_tw.zip build 2014-05-13 01:30 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405060843-alt1
- repocop cronbuild 20140509. At your service.
- zh_tw.zip build 2014-05-06 08:43 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404151633-alt1
- repocop cronbuild 20140418. At your service.
- zh_tw.zip build 2014-04-15 16:33 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404101738-alt1
- repocop cronbuild 20140411. At your service.
- zh_tw.zip build 2014-04-10 17:38 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403310334-alt1
- repocop cronbuild 20140404. At your service.
- zh_tw.zip build 2014-03-31 03:34 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403260534-alt1
- repocop cronbuild 20140328. At your service.
- zh_tw.zip build 2014-03-26 05:34 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403191726-alt1
- repocop cronbuild 20140321. At your service.
- zh_tw.zip build 2014-03-19 17:26 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403140136-alt1
- repocop cronbuild 20140314. At your service.
- zh_tw.zip build 2014-03-14 01:36 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403051706-alt1
- repocop cronbuild 20140307. At your service.
- zh_tw.zip build 2014-03-05 17:06 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402271701-alt1
- repocop cronbuild 20140228. At your service.
- zh_tw.zip build 2014-02-27 17:01 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402180734-alt1
- repocop cronbuild 20140221. At your service.
- zh_tw.zip build 2014-02-18 07:34 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402041244-alt1
- repocop cronbuild 20140207. At your service.
- zh_tw.zip build 2014-02-04 12:44 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401271555-alt1
- repocop cronbuild 20140131. At your service.
- zh_tw.zip build 2014-01-27 15:55 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401231731-alt1
- repocop cronbuild 20140124. At your service.
- zh_tw.zip build 2014-01-23 17:31 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401112139-alt1
- repocop cronbuild 20140117. At your service.
- zh_tw.zip build 2014-01-11 21:39 UTC

* Fri Jan 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401040325-alt1
- repocop cronbuild 20140110. At your service.
- zh_tw.zip build 2014-01-04 03:25 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312291709-alt1
- repocop cronbuild 20140103. At your service.
- zh_tw.zip build 2013-12-29 17:09 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312261738-alt1
- repocop cronbuild 20131227. At your service.
- zh_tw.zip build 2013-12-26 17:38 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312191650-alt1
- repocop cronbuild 20131220. At your service.
- zh_tw.zip build 2013-12-19 16:50 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- zh_tw.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312051557-alt1
- repocop cronbuild 20131206. At your service.
- zh_tw.zip build 2013-12-05 15:57 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311281517-alt1
- repocop cronbuild 20131129. At your service.
- zh_tw.zip build 2013-11-28 15:17 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311181559-alt1
- repocop cronbuild 20131122. At your service.
- zh_tw.zip build 2013-11-18 15:59 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311141315-alt1
- repocop cronbuild 20131115. At your service.
- zh_tw.zip build 2013-11-14 13:15 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311071522-alt1
- repocop cronbuild 20131108. At your service.
- zh_tw.zip build 2013-11-07 15:22 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310290415-alt1
- repocop cronbuild 20131101. At your service.
- zh_tw.zip build 2013-10-29 04:15 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310240625-alt1
- repocop cronbuild 20131025. At your service.
- zh_tw.zip build 2013-10-24 06:25 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310170357-alt1
- repocop cronbuild 20131018. At your service.
- zh_tw.zip build 2013-10-17 03:57 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310100657-alt1
- repocop cronbuild 20131011. At your service.
- zh_tw.zip build 2013-10-10 06:57 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310021109-alt1
- repocop cronbuild 20131004. At your service.
- zh_tw.zip build 2013-10-02 11:09 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309221601-alt1
- repocop cronbuild 20130927. At your service.
- zh_tw.zip build 2013-09-22 16:01 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309191102-alt1
- repocop cronbuild 20130920. At your service.
- zh_tw.zip build 2013-09-19 11:02 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309090532-alt1
- repocop cronbuild 20130913. At your service.
- zh_tw.zip build 2013-09-09 05:32 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309061024-alt1
- repocop cronbuild 20130906. At your service.
- zh_tw.zip build 2013-09-06 10:24 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308271449-alt1
- repocop cronbuild 20130831. At your service.
- zh_tw.zip build 2013-08-27 14:49 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308200818-alt1
- repocop cronbuild 20130824. At your service.
- zh_tw.zip build 2013-08-20 08:18 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308140759-alt1
- repocop cronbuild 20130817. At your service.
- zh_tw.zip build 2013-08-14 07:59 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308081238-alt1
- repocop cronbuild 20130810. At your service.
- zh_tw.zip build 2013-08-08 12:38 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308012119-alt1
- repocop cronbuild 20130803. At your service.
- zh_tw.zip build 2013-08-01 21:19 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307270158-alt1
- repocop cronbuild 20130727. At your service.
- zh_tw.zip build 2013-07-27 01:58 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307182237-alt1
- repocop cronbuild 20130720. At your service.
- zh_tw.zip build 2013-07-18 22:37 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307092248-alt1
- repocop cronbuild 20130713. At your service.
- zh_tw.zip build 2013-07-09 22:48 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307030346-alt1
- repocop cronbuild 20130706. At your service.
- zh_tw.zip build 2013-07-03 03:46 UTC

* Sat Jun 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306251624-alt1
- repocop cronbuild 20130629. At your service.
- zh_tw.zip build 2013-06-25 16:24 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140511-alt1
- repocop cronbuild 20130615. At your service.
- zh_tw.zip build 2013-06-14 05:11 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305292351-alt1
- Rename package to moodle2.5-lang-zh_tw
- zh_tw.zip build 2013-05-29 23:51 UTC

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
