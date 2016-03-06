# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename no
%define packagversion 2.5.0
%define packagedate 201603051140
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Norwegian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-no
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
* Sun Mar 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201603051140-alt1
- repocop cronbuild 20160306. At your service.
- no.zip build 2016-03-05 11:40 UTC

* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201602120619-alt1
- repocop cronbuild 20160214. At your service.
- no.zip build 2016-02-12 06:19 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508071011-alt1
- repocop cronbuild 20150823. At your service.
- no.zip build 2015-08-07 10:11 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507122042-alt1
- repocop cronbuild 20150716. At your service.
- no.zip build 2015-07-12 20:42 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507010757-alt1
- repocop cronbuild 20150702. At your service.
- no.zip build 2015-07-01 07:57 UTC

* Sat Apr 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504140653-alt1
- repocop cronbuild 20150418. At your service.
- no.zip build 2015-04-14 06:53 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502021151-alt1
- repocop cronbuild 20150207. At your service.
- no.zip build 2015-02-02 11:51 UTC

* Sat Jan 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501120832-alt1
- repocop cronbuild 20150117. At your service.
- no.zip build 2015-01-12 08:32 UTC

* Sat Jan 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501081245-alt1
- repocop cronbuild 20150110. At your service.
- no.zip build 2015-01-08 12:45 UTC

* Sat Jan 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412271536-alt1
- repocop cronbuild 20150103. At your service.
- no.zip build 2014-12-27 15:36 UTC

* Sat Dec 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412050855-alt1
- repocop cronbuild 20141206. At your service.
- no.zip build 2014-12-05 08:55 UTC

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410131157-alt1
- repocop cronbuild 20141018. At your service.
- no.zip build 2014-10-13 11:57 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410081253-alt1
- repocop cronbuild 20141011. At your service.
- no.zip build 2014-10-08 12:53 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201408252217-alt1
- repocop cronbuild 20140913. At your service.
- no.zip build 2014-08-25 22:17 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406241320-alt1
- repocop cronbuild 20140628. At your service.
- no.zip build 2014-06-24 13:20 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405020751-alt1
- repocop cronbuild 20140509. At your service.
- no.zip build 2014-05-02 07:51 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404261139-alt1
- repocop cronbuild 20140502. At your service.
- no.zip build 2014-04-26 11:39 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404250343-alt1
- repocop cronbuild 20140425. At your service.
- no.zip build 2014-04-25 03:43 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404041955-alt1
- repocop cronbuild 20140411. At your service.
- no.zip build 2014-04-04 19:55 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403291455-alt1
- repocop cronbuild 20140404. At your service.
- no.zip build 2014-03-29 14:55 UTC

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403231252-alt1
- repocop cronbuild 20140329. At your service.
- no.zip build 2014-03-23 12:52 UTC

* Sat Mar 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403181153-alt1
- repocop cronbuild 20140322. At your service.
- no.zip build 2014-03-18 11:53 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402242003-alt1
- repocop cronbuild 20140301. At your service.
- no.zip build 2014-02-24 20:03 UTC

* Sat Feb 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402182050-alt1
- repocop cronbuild 20140222. At your service.
- no.zip build 2014-02-18 20:50 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402121641-alt1
- repocop cronbuild 20140215. At your service.
- no.zip build 2014-02-12 16:41 UTC

* Sat Jan 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401241535-alt1
- repocop cronbuild 20140125. At your service.
- no.zip build 2014-01-24 15:35 UTC

* Sat Jan 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401151337-alt1
- repocop cronbuild 20140118. At your service.
- no.zip build 2014-01-15 13:37 UTC

* Sat Jan 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401100731-alt1
- repocop cronbuild 20140111. At your service.
- no.zip build 2014-01-10 07:31 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312311316-alt1
- repocop cronbuild 20140103. At your service.
- no.zip build 2013-12-31 13:16 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- no.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312051232-alt1
- repocop cronbuild 20131206. At your service.
- no.zip build 2013-12-05 12:32 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311271056-alt1
- repocop cronbuild 20131129. At your service.
- no.zip build 2013-11-27 10:56 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311101943-alt1
- repocop cronbuild 20131115. At your service.
- no.zip build 2013-11-10 19:43 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311070806-alt1
- repocop cronbuild 20131108. At your service.
- no.zip build 2013-11-07 08:06 UTC

* Sat Oct 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310101236-alt1
- repocop cronbuild 20131012. At your service.
- no.zip build 2013-10-10 12:36 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310011309-alt1
- repocop cronbuild 20131004. At your service.
- no.zip build 2013-10-01 13:09 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309061135-alt1
- repocop cronbuild 20130913. At your service.
- no.zip build 2013-09-06 11:35 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309031932-alt1
- repocop cronbuild 20130906. At your service.
- no.zip build 2013-09-03 19:32 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308271913-alt1
- repocop cronbuild 20130831. At your service.
- no.zip build 2013-08-27 19:13 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308231158-alt1
- repocop cronbuild 20130824. At your service.
- no.zip build 2013-08-23 11:58 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308161547-alt1
- repocop cronbuild 20130817. At your service.
- no.zip build 2013-08-16 15:47 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308071547-alt1
- repocop cronbuild 20130810. At your service.
- no.zip build 2013-08-07 15:47 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307301117-alt1
- repocop cronbuild 20130803. At your service.
- no.zip build 2013-07-30 11:17 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307201617-alt1
- repocop cronbuild 20130727. At your service.
- no.zip build 2013-07-20 16:17 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307100500-alt1
- repocop cronbuild 20130713. At your service.
- no.zip build 2013-07-10 05:00 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140652-alt1
- repocop cronbuild 20130615. At your service.
- no.zip build 2013-06-14 06:52 UTC

* Sat Jun 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306071323-alt1
- repocop cronbuild 20130608. At your service.
- no.zip build 2013-06-07 13:23 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305300658-alt1
- Rename package to moodle2.5-lang-no
- no.zip build 2013-05-30 06:58 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221013-alt1
- repocop cronbuild 20130524. At your service.
- no.zip build 2013-05-22 10:13 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201304231305-alt1
- repocop cronbuild 20130509. At your service.
- no.zip build 2013-04-23 13:05 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304150925-alt1
- Rename package to moodle2.4-lang-no
- no.zip build 2013-04-15 09:25 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303191348-alt1
- repocop cronbuild 20130320. At your service.
- no.zip build 2013-03-19 13:48 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303121119-alt1
- repocop cronbuild 20130313. At your service.
- no.zip build 2013-03-12 11:19 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302221112-alt1
- repocop cronbuild 20130225. At your service.
- no.zip build 2013-02-22 11:12 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- no.zip build 2013-01-26 15:39 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301112305-alt1
- repocop cronbuild 20130114. At your service.
- no.zip build 2013-01-11 23:05 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301051804-alt1
- repocop cronbuild 20130107. At your service.
- no.zip build 2013-01-05 18:04 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212041448-alt1
- repocop cronbuild 20121210. At your service.
- no.zip build 2012-12-04 14:48 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211260945-alt1
- repocop cronbuild 20121203. At your service.
- no.zip build 2012-11-26 09:45 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211221501-alt1
- repocop cronbuild 20121126. At your service.
- no.zip build 2012-11-22 15:01 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211161143-alt1
- repocop cronbuild 20121119. At your service.
- no.zip build 2012-11-16 11:43 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211091311-alt1
- repocop cronbuild 20121112. At your service.
- no.zip build 2012-11-09 13:11 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- no.zip build 2012-11-01 07:00 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210261222-alt1
- repocop cronbuild 20121029. At your service.
- no.zip build 2012-10-26 12:22 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210191253-alt1
- repocop cronbuild 20121022. At your service.
- no.zip build 2012-10-19 12:53 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210101350-alt1
- repocop cronbuild 20121015. At your service.
- no.zip build 2012-10-10 13:50 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210041240-alt1
- repocop cronbuild 20121008. At your service.
- no.zip build 2012-10-04 12:40 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209261134-alt1
- repocop cronbuild 20121001. At your service.
- no.zip build 2012-09-26 11:34 UTC

* Wed Sep 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120905. At your service.
- no.zip build 2012-08-31 10:30 UTC

* Wed Aug 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208280731-alt1
- repocop cronbuild 20120829. At your service.
- no.zip build 2012-08-28 07:31 UTC

* Wed Aug 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208161144-alt1
- repocop cronbuild 20120822. At your service.
- no.zip build 2012-08-16 11:44 UTC

* Wed Aug 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208031301-alt1
- repocop cronbuild 20120808. At your service.
- no.zip build 2012-08-03 13:01 UTC

* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206270526-alt1
- repocop cronbuild 20120704. At your service.
- no.zip build 2012-06-27 05:26 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191249-alt1
- repocop cronbuild 20120619. At your service.
- no.zip build 2012-06-19 12:49 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121129-alt1
- repocop cronbuild 20120612. At your service.
- no.zip build 2012-06-12 11:29 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206050632-alt1
- repocop cronbuild 20120605. At your service.
- no.zip build 2012-06-05 06:32 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- no.zip build 2012-05-23 15:49 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205210658-alt1
- repocop cronbuild 20120522. At your service.
- no.zip build 2012-05-21 06:58 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- no.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205041400-alt1
- repocop cronbuild 20120508. At your service.
- no.zip build 2012-05-04 14:00 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204300617-alt1
- repocop cronbuild 20120501. At your service.
- no.zip build 2012-04-30 06:17 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204190725-alt1
- repocop cronbuild 20120424. At your service.
- no.zip build 2012-04-19 07:25 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204161306-alt1
- repocop cronbuild 20120417. At your service.
- no.zip build 2012-04-16 13:06 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203141206-alt1
- Rename package to moodle2.2-lang-no
- no.zip build 2012-03-14 12:06 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120302. At your service.
- no.zip build 2012-03-01 11:00 UTC

* Fri Feb 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202231327-alt1
- repocop cronbuild 20120224. At your service.
- no.zip build 2012-02-23 13:27 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202041314-alt1
- repocop cronbuild 20120210. At your service.
- no.zip build 2012-02-04 13:14 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201171357-alt1
- repocop cronbuild 20120120. At your service.
- no.zip build 2012-01-17 13:57 UTC

* Fri Jan 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201031234-alt1
- repocop cronbuild 20120106. At your service.
- no.zip build 2012-01-03 12:34 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- no.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111081406-alt1
- Rename package to moodle2.1-lang-no
- no.zip build 2011-11-08 14:06

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
- no.zip build 2011-10-06 22:30 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109251618-alt1
- no.zip build 2011-09-25 16:18 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- no.zip build 2011-09-21 15:30 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109151708-alt1
- no.zip build 2011-09-15 17:08 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108151942-alt2
- Fix requires

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108151942-alt1
- Rename package to moodle2.0-lang-no
- no.zip build 2011-08-15 19:42 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110630-alt1
- no_utf8.zip build 20110630
- initial build for ALT Linux Sisyphus
