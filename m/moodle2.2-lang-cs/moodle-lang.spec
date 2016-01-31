# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename cs
%define packagversion 2.2.0
%define packagedate 201601251015
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Czech
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-cs
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
* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201601251015-alt1
- repocop cronbuild 20160131. At your service.
- cs.zip build 2016-01-25 10:15 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201601180749-alt1
- repocop cronbuild 20160124. At your service.
- cs.zip build 2016-01-18 07:49 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201512011145-alt1
- repocop cronbuild 20151207. At your service.
- cs.zip build 2015-12-01 11:45 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511251548-alt1
- repocop cronbuild 20151130. At your service.
- cs.zip build 2015-11-25 15:48 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511181441-alt1
- repocop cronbuild 20151123. At your service.
- cs.zip build 2015-11-18 14:41 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511111456-alt1
- repocop cronbuild 20151116. At your service.
- cs.zip build 2015-11-11 14:56 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511041404-alt1
- repocop cronbuild 20151109. At your service.
- cs.zip build 2015-11-04 14:04 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510292051-alt1
- repocop cronbuild 20151102. At your service.
- cs.zip build 2015-10-29 20:51 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201510051035-alt1
- repocop cronbuild 20151012. At your service.
- cs.zip build 2015-10-05 10:35 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201508181236-alt1
- repocop cronbuild 20150823. At your service.
- cs.zip build 2015-08-18 12:36 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201506080750-alt1
- repocop cronbuild 20150611. At your service.
- cs.zip build 2015-06-08 07:50 UTC

* Sat May 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201505060818-alt1
- repocop cronbuild 20150509. At your service.
- cs.zip build 2015-05-06 08:18 UTC

* Sat Apr 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201504200835-alt1
- repocop cronbuild 20150425. At your service.
- cs.zip build 2015-04-20 08:35 UTC

* Sat Mar 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201503242214-alt1
- repocop cronbuild 20150328. At your service.
- cs.zip build 2015-03-24 22:14 UTC

* Sat Mar 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201503122215-alt1
- repocop cronbuild 20150314. At your service.
- cs.zip build 2015-03-12 22:15 UTC

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502242055-alt1
- repocop cronbuild 20150228. At your service.
- cs.zip build 2015-02-24 20:55 UTC

* Sat Feb 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502162102-alt1
- repocop cronbuild 20150221. At your service.
- cs.zip build 2015-02-16 21:02 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412102351-alt1
- repocop cronbuild 20141212. At your service.
- cs.zip build 2014-12-10 23:51 UTC

* Sat Nov 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201411251401-alt1
- repocop cronbuild 20141129. At your service.
- cs.zip build 2014-11-25 14:01 UTC

* Fri Nov 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201411162104-alt1
- repocop cronbuild 20141121. At your service.
- cs.zip build 2014-11-16 21:04 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201410080715-alt1
- repocop cronbuild 20141011. At your service.
- cs.zip build 2014-10-08 07:15 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201409240718-alt1
- repocop cronbuild 20140927. At your service.
- cs.zip build 2014-09-24 07:18 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201408290655-alt1
- repocop cronbuild 20140913. At your service.
- cs.zip build 2014-08-29 06:55 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201406300738-alt1
- repocop cronbuild 20140705. At your service.
- cs.zip build 2014-06-30 07:38 UTC

* Sat Jun 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201406031239-alt1
- repocop cronbuild 20140607. At your service.
- cs.zip build 2014-06-03 12:39 UTC

* Sat May 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201405131842-alt1
- repocop cronbuild 20140517. At your service.
- cs.zip build 2014-05-13 18:42 UTC

* Sat May 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201405071018-alt1
- repocop cronbuild 20140510. At your service.
- cs.zip build 2014-05-07 10:18 UTC

* Sat Apr 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201404042012-alt1
- repocop cronbuild 20140405. At your service.
- cs.zip build 2014-04-04 20:12 UTC

* Sat Mar 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403141904-alt1
- repocop cronbuild 20140315. At your service.
- cs.zip build 2014-03-14 19:04 UTC

* Sat Mar 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403041011-alt1
- repocop cronbuild 20140308. At your service.
- cs.zip build 2014-03-04 10:11 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402271512-alt1
- repocop cronbuild 20140301. At your service.
- cs.zip build 2014-02-27 15:12 UTC

* Sat Feb 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402172046-alt1
- repocop cronbuild 20140222. At your service.
- cs.zip build 2014-02-17 20:46 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402130841-alt1
- repocop cronbuild 20140215. At your service.
- cs.zip build 2014-02-13 08:41 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201312030116-alt1
- repocop cronbuild 20131206. At your service.
- cs.zip build 2013-12-03 01:16 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311271051-alt1
- repocop cronbuild 20131129. At your service.
- cs.zip build 2013-11-27 10:51 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311212153-alt1
- repocop cronbuild 20131122. At your service.
- cs.zip build 2013-11-21 21:53 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201311060909-alt1
- repocop cronbuild 20131108. At your service.
- cs.zip build 2013-11-06 09:09 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309272107-alt1
- repocop cronbuild 20131004. At your service.
- cs.zip build 2013-09-27 21:07 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309230923-alt1
- repocop cronbuild 20130927. At your service.
- cs.zip build 2013-09-23 09:23 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309031914-alt1
- repocop cronbuild 20130906. At your service.
- cs.zip build 2013-09-03 19:14 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307311937-alt1
- repocop cronbuild 20130802. At your service.
- cs.zip build 2013-07-31 19:37 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201307030731-alt1
- repocop cronbuild 20130705. At your service.
- cs.zip build 2013-07-03 07:31 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201306141154-alt1
- repocop cronbuild 20130621. At your service.
- cs.zip build 2013-06-14 11:54 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201306070820-alt1
- repocop cronbuild 20130614. At your service.
- cs.zip build 2013-06-07 08:20 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201306040851-alt1
- repocop cronbuild 20130607. At your service.
- cs.zip build 2013-06-04 08:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305211149-alt1
- repocop cronbuild 20130524. At your service.
- cs.zip build 2013-05-21 11:49 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305071459-alt1
- repocop cronbuild 20130509. At your service.
- cs.zip build 2013-05-07 14:59 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304091439-alt1
- repocop cronbuild 20130410. At your service.
- cs.zip build 2013-04-09 14:39 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304020840-alt1
- repocop cronbuild 20130403. At your service.
- cs.zip build 2013-04-02 08:40 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303250745-alt1
- repocop cronbuild 20130327. At your service.
- cs.zip build 2013-03-25 07:45 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303110810-alt1
- repocop cronbuild 20130313. At your service.
- cs.zip build 2013-03-11 08:10 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301280856-alt1
- repocop cronbuild 20130204. At your service.
- cs.zip build 2013-01-28 08:56 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261214-alt1
- repocop cronbuild 20130128. At your service.
- cs.zip build 2013-01-26 12:14 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301200849-alt1
- repocop cronbuild 20130121. At your service.
- cs.zip build 2013-01-20 08:49 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212120952-alt1
- repocop cronbuild 20121217. At your service.
- cs.zip build 2012-12-12 09:52 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211200206-alt1
- repocop cronbuild 20121126. At your service.
- cs.zip build 2012-11-20 02:06 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211072316-alt1
- repocop cronbuild 20121112. At your service.
- cs.zip build 2012-11-07 23:16 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- cs.zip build 2012-11-01 07:00 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210080743-alt1
- repocop cronbuild 20121015. At your service.
- cs.zip build 2012-10-08 07:43 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209170807-alt1
- repocop cronbuild 20120918. At your service.
- cs.zip build 2012-09-17 08:07 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209101551-alt1
- repocop cronbuild 20120911. At your service.
- cs.zip build 2012-09-10 15:51 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120904. At your service.
- cs.zip build 2012-08-31 10:30 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208030940-alt1
- repocop cronbuild 20120807. At your service.
- cs.zip build 2012-08-03 09:40 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207271624-alt1
- repocop cronbuild 20120731. At your service.
- cs.zip build 2012-07-27 16:24 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207101853-alt1
- repocop cronbuild 20120717. At your service.
- cs.zip build 2012-07-10 18:53 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207091351-alt1
- repocop cronbuild 20120710. At your service.
- cs.zip build 2012-07-09 13:51 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207021542-alt1
- repocop cronbuild 20120703. At your service.
- cs.zip build 2012-07-02 15:42 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206242048-alt1
- repocop cronbuild 20120626. At your service.
- cs.zip build 2012-06-24 20:48 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205301304-alt1
- repocop cronbuild 20120605. At your service.
- cs.zip build 2012-05-30 13:04 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205281334-alt1
- repocop cronbuild 20120529. At your service.
- cs.zip build 2012-05-28 13:34 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205151829-alt1
- repocop cronbuild 20120521. At your service.
- cs.zip build 2012-05-15 18:29 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- cs.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205041102-alt1
- repocop cronbuild 20120508. At your service.
- cs.zip build 2012-05-04 11:02 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- cs.zip build 2012-04-27 11:30 UTC

* Mon Mar 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203161028-alt1
- Rename package to moodle2.2-lang-cs
- cs.zip build 2012-03-16 10:28 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011549-alt1
- repocop cronbuild 20120306. At your service.
- cs.zip build 2012-03-01 15:49 UTC

* Tue Feb 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202281017-alt1
- repocop cronbuild 20120228. At your service.
- cs.zip build 2012-02-28 10:17 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201311044-alt1
- repocop cronbuild 20120131. At your service.
- cs.zip build 2012-01-31 10:44 UTC

* Tue Dec 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112230839-alt1
- repocop cronbuild 20111227. At your service.
- cs.zip build 2011-12-23 08:39 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112131059-alt1
- repocop cronbuild 20111213. At your service.
- cs.zip build 2011-12-13 10:59 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112051734-alt1
- repocop cronbuild 20111206. At your service.
- cs.zip build 2011-12-05 17:34 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111151151-alt1
- Rename package to moodle2.1-lang-cs
- cs.zip build 2011-11-15 11:51 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111151153-alt2
- Fix requires

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151153-alt1
- repocop cronbuild 20111116. At your service.
- cs.zip build 2011-11-15 11:53 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- cs.zip build 2011-10-06 22:30 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110061223-alt1
- cs.zip build 2011-10-06 12:23 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109220241-alt1
- cs.zip build 2011-09-22 02:41 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- cs.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108232211-alt2
- Fix requires

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108232211-alt1
- cs.zip build 2011-08-23 22:11 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108170854-alt1
- cs.zip build 2011-08-17 08:54 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- cs.zip build 2011-08-16 13:07 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-cs
- cs.zip build 2011-08-11 23:00 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110730-alt1
- cs_utf8.zip build 2011-07-30
- initial build for ALT Linux Sisyphus
