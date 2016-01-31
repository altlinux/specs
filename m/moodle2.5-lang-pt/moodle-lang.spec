# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename pt
%define packagversion 2.5.0
%define packagedate 201601282138
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Portuguese
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-pt
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
* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601282138-alt1
- repocop cronbuild 20160131. At your service.
- pt.zip build 2016-01-28 21:38 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601221351-alt1
- repocop cronbuild 20160124. At your service.
- pt.zip build 2016-01-22 13:51 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201512111843-alt1
- repocop cronbuild 20151214. At your service.
- pt.zip build 2015-12-11 18:43 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511161031-alt1
- repocop cronbuild 20151123. At your service.
- pt.zip build 2015-11-16 10:31 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511121316-alt1
- repocop cronbuild 20151116. At your service.
- pt.zip build 2015-11-12 13:16 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510261749-alt1
- repocop cronbuild 20151102. At your service.
- pt.zip build 2015-10-26 17:49 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509160759-alt1
- repocop cronbuild 20150921. At your service.
- pt.zip build 2015-09-16 07:59 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507211405-alt1
- repocop cronbuild 20150723. At your service.
- pt.zip build 2015-07-21 14:05 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505261150-alt1
- repocop cronbuild 20150604. At your service.
- pt.zip build 2015-05-26 11:50 UTC

* Mon May 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505211257-alt1
- repocop cronbuild 20150525. At your service.
- pt.zip build 2015-05-21 12:57 UTC

* Mon May 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504271246-alt1
- repocop cronbuild 20150504. At your service.
- pt.zip build 2015-04-27 12:46 UTC

* Mon Apr 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504231813-alt1
- repocop cronbuild 20150427. At your service.
- pt.zip build 2015-04-23 18:13 UTC

* Mon Apr 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504152059-alt1
- repocop cronbuild 20150420. At your service.
- pt.zip build 2015-04-15 20:59 UTC

* Mon Apr 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504011623-alt1
- repocop cronbuild 20150406. At your service.
- pt.zip build 2015-04-01 16:23 UTC

* Mon Mar 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503121120-alt1
- repocop cronbuild 20150316. At your service.
- pt.zip build 2015-03-12 11:20 UTC

* Mon Feb 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502121916-alt1
- repocop cronbuild 20150216. At your service.
- pt.zip build 2015-02-12 19:16 UTC

* Mon Dec 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412161717-alt1
- repocop cronbuild 20141222. At your service.
- pt.zip build 2014-12-16 17:17 UTC

* Sat Dec 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412051741-alt1
- repocop cronbuild 20141206. At your service.
- pt.zip build 2014-12-05 17:41 UTC

* Sat Nov 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411271009-alt1
- repocop cronbuild 20141129. At your service.
- pt.zip build 2014-11-27 10:09 UTC

* Sat Nov 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411201244-alt1
- repocop cronbuild 20141122. At your service.
- pt.zip build 2014-11-20 12:44 UTC

* Sat Nov 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411131153-alt1
- repocop cronbuild 20141115. At your service.
- pt.zip build 2014-11-13 11:53 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410100925-alt1
- repocop cronbuild 20141011. At your service.
- pt.zip build 2014-10-10 09:25 UTC

* Sat Oct 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409301545-alt1
- repocop cronbuild 20141004. At your service.
- pt.zip build 2014-09-30 15:45 UTC

* Sat Sep 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409171640-alt1
- repocop cronbuild 20140920. At your service.
- pt.zip build 2014-09-17 16:40 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409121632-alt1
- repocop cronbuild 20140913. At your service.
- pt.zip build 2014-09-12 16:32 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201407031418-alt1
- repocop cronbuild 20140705. At your service.
- pt.zip build 2014-07-03 14:18 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406241151-alt1
- repocop cronbuild 20140628. At your service.
- pt.zip build 2014-06-24 11:51 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406201711-alt1
- repocop cronbuild 20140621. At your service.
- pt.zip build 2014-06-20 17:11 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404021501-alt1
- repocop cronbuild 20140404. At your service.
- pt.zip build 2014-04-02 15:01 UTC

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403261607-alt1
- repocop cronbuild 20140329. At your service.
- pt.zip build 2014-03-26 16:07 UTC

* Sat Mar 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403191606-alt1
- repocop cronbuild 20140322. At your service.
- pt.zip build 2014-03-19 16:06 UTC

* Sat Mar 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403131148-alt1
- repocop cronbuild 20140315. At your service.
- pt.zip build 2014-03-13 11:48 UTC

* Sat Mar 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403051216-alt1
- repocop cronbuild 20140308. At your service.
- pt.zip build 2014-03-05 12:16 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402281703-alt1
- repocop cronbuild 20140301. At your service.
- pt.zip build 2014-02-28 17:03 UTC

* Sat Feb 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402171901-alt1
- repocop cronbuild 20140222. At your service.
- pt.zip build 2014-02-17 19:01 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402141841-alt1
- repocop cronbuild 20140215. At your service.
- pt.zip build 2014-02-14 18:41 UTC

* Sat Feb 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402041759-alt1
- repocop cronbuild 20140208. At your service.
- pt.zip build 2014-02-04 17:59 UTC

* Sat Feb 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401311747-alt1
- repocop cronbuild 20140201. At your service.
- pt.zip build 2014-01-31 17:47 UTC

* Sat Jan 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401231807-alt1
- repocop cronbuild 20140125. At your service.
- pt.zip build 2014-01-23 18:07 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- pt.zip build 2013-12-13 05:46 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311141130-alt1
- repocop cronbuild 20131115. At your service.
- pt.zip build 2013-11-14 11:30 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311051755-alt1
- repocop cronbuild 20131108. At your service.
- pt.zip build 2013-11-05 17:55 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310311450-alt1
- repocop cronbuild 20131101. At your service.
- pt.zip build 2013-10-31 14:50 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310180924-alt1
- repocop cronbuild 20131025. At your service.
- pt.zip build 2013-10-18 09:24 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310171012-alt1
- repocop cronbuild 20131018. At your service.
- pt.zip build 2013-10-17 10:12 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310101420-alt1
- repocop cronbuild 20131011. At your service.
- pt.zip build 2013-10-10 14:20 UTC

* Sat Oct 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310031523-alt1
- repocop cronbuild 20131005. At your service.
- pt.zip build 2013-10-03 15:23 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309251424-alt1
- repocop cronbuild 20130927. At your service.
- pt.zip build 2013-09-25 14:24 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309051619-alt1
- repocop cronbuild 20130906. At your service.
- pt.zip build 2013-09-05 16:19 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307181356-alt1
- repocop cronbuild 20130720. At your service.
- pt.zip build 2013-07-18 13:56 UTC

* Sat Jun 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306171136-alt1
- repocop cronbuild 20130622. At your service.
- pt.zip build 2013-06-17 11:36 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306141915-alt1
- repocop cronbuild 20130615. At your service.
- pt.zip build 2013-06-14 19:15 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305292351-alt1
- Rename package to moodle2.5-lang-pt
- pt.zip build 2013-05-29 23:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305231511-alt1
- repocop cronbuild 20130524. At your service.
- pt.zip build 2013-05-23 15:11 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305141419-alt1
- repocop cronbuild 20130517. At your service.
- pt.zip build 2013-05-14 14:19 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305081652-alt1
- repocop cronbuild 20130509. At your service.
- pt.zip build 2013-05-08 16:52 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304091614-alt1
- Rename package to moodle2.4-lang-pt
- pt.zip build 2013-04-09 16:14 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304041752-alt1
- repocop cronbuild 20130410. At your service.
- pt.zip build 2013-04-04 17:52 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302201441-alt1
- repocop cronbuild 20130225. At your service.
- pt.zip build 2013-02-20 14:41 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302041927-alt1
- repocop cronbuild 20130211. At your service.
- pt.zip build 2013-02-04 19:27 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301231625-alt1
- repocop cronbuild 20130128. At your service.
- pt.zip build 2013-01-23 16:25 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301161900-alt1
- repocop cronbuild 20130121. At your service.
- pt.zip build 2013-01-16 19:00 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301111926-alt1
- repocop cronbuild 20130114. At your service.
- pt.zip build 2013-01-11 19:26 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212102026-alt1
- repocop cronbuild 20121217. At your service.
- pt.zip build 2012-12-10 20:26 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212051940-alt1
- repocop cronbuild 20121210. At your service.
- pt.zip build 2012-12-05 19:40 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211021749-alt1
- repocop cronbuild 20121105. At your service.
- pt.zip build 2012-11-02 17:49 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210171754-alt1
- repocop cronbuild 20121022. At your service.
- pt.zip build 2012-10-17 17:54 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210081840-alt1
- repocop cronbuild 20121015. At your service.
- pt.zip build 2012-10-08 18:40 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210021619-alt1
- repocop cronbuild 20121008. At your service.
- pt.zip build 2012-10-02 16:19 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209201621-alt1
- repocop cronbuild 20121001. At your service.
- pt.zip build 2012-09-20 16:21 UTC

* Wed Sep 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209191559-alt1
- repocop cronbuild 20120919. At your service.
- pt.zip build 2012-09-19 15:59 UTC

* Wed Sep 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209111314-alt1
- repocop cronbuild 20120912. At your service.
- pt.zip build 2012-09-11 13:14 UTC

* Wed Sep 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120905. At your service.
- pt.zip build 2012-08-31 10:30 UTC

* Wed Aug 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208051809-alt1
- repocop cronbuild 20120808. At your service.
- pt.zip build 2012-08-05 18:09 UTC

* Wed Jul 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207161555-alt1
- repocop cronbuild 20120718. At your service.
- pt.zip build 2012-07-16 15:55 UTC

* Wed Jul 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207112119-alt1
- repocop cronbuild 20120711. At your service.
- pt.zip build 2012-07-11 21:19 UTC

* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207041132-alt1
- repocop cronbuild 20120704. At your service.
- pt.zip build 2012-07-04 11:32 UTC

* Wed Jun 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206271142-alt1
- repocop cronbuild 20120627. At your service.
- pt.zip build 2012-06-27 11:42 UTC

* Wed Jun 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206201555-alt1
- repocop cronbuild 20120620. At your service.
- pt.zip build 2012-06-20 15:55 UTC

* Wed Jun 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121218-alt1
- repocop cronbuild 20120613. At your service.
- pt.zip build 2012-06-12 12:18 UTC

* Wed Jun 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206042306-alt1
- repocop cronbuild 20120606. At your service.
- pt.zip build 2012-06-04 23:06 UTC

* Wed May 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120523. At your service.
- pt.zip build 2012-05-23 15:49 UTC

* Wed May 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120516. At your service.
- pt.zip build 2012-05-11 11:00 UTC

* Wed May 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120502. At your service.
- pt.zip build 2012-04-27 11:30 UTC

* Wed Apr 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204241426-alt1
- repocop cronbuild 20120425. At your service.
- pt.zip build 2012-04-24 14:26 UTC

* Wed Apr 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204181401-alt1
- repocop cronbuild 20120418. At your service.
- pt.zip build 2012-04-18 14:01 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204101704-alt1
- repocop cronbuild 20120410. At your service.
- pt.zip build 2012-04-10 17:04 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203291546-alt1
- repocop cronbuild 20120403. At your service.
- pt.zip build 2012-03-29 15:46 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203271717-alt1
- repocop cronbuild 20120327. At your service.
- pt.zip build 2012-03-27 17:17 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203201400-alt1
- repocop cronbuild 20120320. At your service.
- pt.zip build 2012-03-20 14:00 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203171452-alt1
- Rename package to moodle2.2-lang-pt
- pt.zip build 2012-03-17 14:52 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203171452-alt1
- repocop cronbuild 20120320. At your service.
- pt.zip build 2012-03-17 14:52 UTC

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203082202-alt1
- repocop cronbuild 20120309. At your service.
- pt.zip build 2012-03-08 22:02 UTC

* Fri Jan 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201251819-alt1
- repocop cronbuild 20120127. At your service.
- pt.zip build 2012-01-25 18:19 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- pt.zip build 2011-12-09 16:00 UTC

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
