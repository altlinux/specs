# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename es
%define packagversion 2.1.0
%define packagedate 201601201422
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Spanish
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-es
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.1
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.1
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
* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201601201422-alt1
- repocop cronbuild 20160124. At your service.
- es.zip build 2016-01-20 14:22 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201512020945-alt1
- repocop cronbuild 20151207. At your service.
- es.zip build 2015-12-02 09:45 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511261457-alt1
- repocop cronbuild 20151130. At your service.
- es.zip build 2015-11-26 14:57 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511111228-alt1
- repocop cronbuild 20151116. At your service.
- es.zip build 2015-11-11 12:28 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- es.zip build 2015-11-08 22:20 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201510010751-alt1
- repocop cronbuild 20151005. At your service.
- es.zip build 2015-10-01 07:51 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201508310823-alt1
- repocop cronbuild 20150907. At your service.
- es.zip build 2015-08-31 08:23 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201508281135-alt1
- repocop cronbuild 20150831. At your service.
- es.zip build 2015-08-28 11:35 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507290814-alt1
- repocop cronbuild 20150730. At your service.
- es.zip build 2015-07-29 08:14 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507080908-alt1
- repocop cronbuild 20150709. At your service.
- es.zip build 2015-07-08 09:08 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506301036-alt1
- repocop cronbuild 20150702. At your service.
- es.zip build 2015-06-30 10:36 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201506100816-alt1
- repocop cronbuild 20150611. At your service.
- es.zip build 2015-06-10 08:16 UTC

* Sat May 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504271306-alt1
- repocop cronbuild 20150502. At your service.
- es.zip build 2015-04-27 13:06 UTC

* Sat Apr 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504201100-alt1
- repocop cronbuild 20150425. At your service.
- es.zip build 2015-04-20 11:00 UTC

* Sat Apr 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504061310-alt1
- repocop cronbuild 20150411. At your service.
- es.zip build 2015-04-06 13:10 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503250958-alt1
- repocop cronbuild 20150327. At your service.
- es.zip build 2015-03-25 09:58 UTC

* Sat Mar 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503160949-alt1
- repocop cronbuild 20150321. At your service.
- es.zip build 2015-03-16 09:49 UTC

* Sat Mar 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201503131214-alt1
- repocop cronbuild 20150314. At your service.
- es.zip build 2015-03-13 12:14 UTC

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201502261505-alt1
- repocop cronbuild 20150228. At your service.
- es.zip build 2015-02-26 15:05 UTC

* Sat Jan 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201501130921-alt1
- repocop cronbuild 20150117. At your service.
- es.zip build 2015-01-13 09:21 UTC

* Sat Jan 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201501071030-alt1
- repocop cronbuild 20150110. At your service.
- es.zip build 2015-01-07 10:30 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201412091409-alt1
- repocop cronbuild 20141212. At your service.
- es.zip build 2014-12-09 14:09 UTC

* Sat Nov 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201411261350-alt1
- repocop cronbuild 20141129. At your service.
- es.zip build 2014-11-26 13:50 UTC

* Fri Oct 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201410301401-alt1
- repocop cronbuild 20141031. At your service.
- es.zip build 2014-10-30 14:01 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409240651-alt1
- repocop cronbuild 20140927. At your service.
- es.zip build 2014-09-24 06:51 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409191335-alt1
- repocop cronbuild 20140919. At your service.
- es.zip build 2014-09-19 13:35 UTC

* Fri Sep 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201409040824-alt1
- repocop cronbuild 20140912. At your service.
- es.zip build 2014-09-04 08:24 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406141212-alt1
- repocop cronbuild 20140621. At your service.
- es.zip build 2014-06-14 12:12 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406110935-alt1
- repocop cronbuild 20140613. At your service.
- es.zip build 2014-06-11 09:35 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201406021100-alt1
- repocop cronbuild 20140606. At your service.
- es.zip build 2014-06-02 11:00 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201405270953-alt1
- repocop cronbuild 20140530. At your service.
- es.zip build 2014-05-27 09:53 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201404291202-alt1
- repocop cronbuild 20140502. At your service.
- es.zip build 2014-04-29 12:02 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403280845-alt1
- repocop cronbuild 20140404. At your service.
- es.zip build 2014-03-28 08:45 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403131032-alt1
- repocop cronbuild 20140314. At your service.
- es.zip build 2014-03-13 10:32 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402281501-alt1
- repocop cronbuild 20140307. At your service.
- es.zip build 2014-02-28 15:01 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402151345-alt1
- repocop cronbuild 20140221. At your service.
- es.zip build 2014-02-15 13:45 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402131137-alt1
- repocop cronbuild 20140214. At your service.
- es.zip build 2014-02-13 11:37 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401130931-alt1
- repocop cronbuild 20140117. At your service.
- es.zip build 2014-01-13 09:31 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312281100-alt1
- repocop cronbuild 20140103. At your service.
- es.zip build 2013-12-28 11:00 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312122132-alt1
- repocop cronbuild 20131213. At your service.
- es.zip build 2013-12-12 21:32 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311261619-alt1
- repocop cronbuild 20131129. At your service.
- es.zip build 2013-11-26 16:19 UTC

* Thu Nov 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201311121336-alt1
- repocop cronbuild 20131114. At your service.
- es.zip build 2013-11-12 13:36 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310271020-alt1
- repocop cronbuild 20131101. At your service.
- es.zip build 2013-10-27 10:20 UTC

* Thu Oct 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310210824-alt1
- repocop cronbuild 20131024. At your service.
- es.zip build 2013-10-21 08:24 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310141129-alt1
- repocop cronbuild 20131018. At your service.
- es.zip build 2013-10-14 11:29 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310021155-alt1
- repocop cronbuild 20131004. At your service.
- es.zip build 2013-10-02 11:55 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309261151-alt1
- repocop cronbuild 20130927. At your service.
- es.zip build 2013-09-26 11:51 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309151651-alt1
- repocop cronbuild 20130920. At your service.
- es.zip build 2013-09-15 16:51 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307271811-alt1
- repocop cronbuild 20130802. At your service.
- es.zip build 2013-07-27 18:11 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307101128-alt1
- repocop cronbuild 20130712. At your service.
- es.zip build 2013-07-10 11:28 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306221635-alt1
- repocop cronbuild 20130628. At your service.
- es.zip build 2013-06-22 16:35 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306161332-alt1
- repocop cronbuild 20130621. At your service.
- es.zip build 2013-06-16 13:32 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306041808-alt1
- repocop cronbuild 20130607. At your service.
- es.zip build 2013-06-04 18:08 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305290546-alt1
- repocop cronbuild 20130531. At your service.
- es.zip build 2013-05-29 05:46 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305221223-alt1
- repocop cronbuild 20130524. At your service.
- es.zip build 2013-05-22 12:23 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305131121-alt1
- repocop cronbuild 20130517. At your service.
- es.zip build 2013-05-13 11:21 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305060958-alt1
- repocop cronbuild 20130509. At your service.
- es.zip build 2013-05-06 09:58 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201304121225-alt1
- repocop cronbuild 20130417. At your service.
- es.zip build 2013-04-12 12:25 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303191450-alt1
- repocop cronbuild 20130319. At your service.
- es.zip build 2013-03-19 14:50 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303121803-alt1
- repocop cronbuild 20130313. At your service.
- es.zip build 2013-03-12 18:03 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302270957-alt1
- repocop cronbuild 20130304. At your service.
- es.zip build 2013-02-27 09:57 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302200954-alt1
- repocop cronbuild 20130225. At your service.
- es.zip build 2013-02-20 09:54 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301262010-alt1
- repocop cronbuild 20130128. At your service.
- es.zip build 2013-01-26 20:10 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301151654-alt1
- repocop cronbuild 20130121. At your service.
- es.zip build 2013-01-15 16:54 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301090906-alt1
- repocop cronbuild 20130114. At your service.
- es.zip build 2013-01-09 09:06 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212301014-alt1
- repocop cronbuild 20121231. At your service.
- es.zip build 2012-12-30 10:14 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212170959-alt1
- repocop cronbuild 20121224. At your service.
- es.zip build 2012-12-17 09:59 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212141305-alt1
- repocop cronbuild 20121217. At your service.
- es.zip build 2012-12-14 13:05 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201212051126-alt1
- repocop cronbuild 20121210. At your service.
- es.zip build 2012-12-05 11:26 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211300843-alt1
- repocop cronbuild 20121203. At your service.
- es.zip build 2012-11-30 08:43 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211171308-alt1
- repocop cronbuild 20121119. At your service.
- es.zip build 2012-11-17 13:08 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211091427-alt1
- repocop cronbuild 20121112. At your service.
- es.zip build 2012-11-09 14:27 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211031423-alt1
- repocop cronbuild 20121105. At your service.
- es.zip build 2012-11-03 14:23 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210181259-alt1
- repocop cronbuild 20121022. At your service.
- es.zip build 2012-10-18 12:59 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201210020723-alt1
- repocop cronbuild 20121008. At your service.
- es.zip build 2012-10-02 07:23 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209212056-alt1
- repocop cronbuild 20121001. At your service.
- es.zip build 2012-09-21 20:56 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209151106-alt1
- repocop cronbuild 20120918. At your service.
- es.zip build 2012-09-15 11:06 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209081850-alt1
- repocop cronbuild 20120911. At your service.
- es.zip build 2012-09-08 18:50 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206032043-alt1
- repocop cronbuild 20120605. At your service.
- es.zip build 2012-06-03 20:43 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205231549-alt1
- repocop cronbuild 20120528. At your service.
- es.zip build 2012-05-23 15:49 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204271130-alt1
- repocop cronbuild 20120430. At your service.
- es.zip build 2012-04-27 11:30 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204011048-alt1
- repocop cronbuild 20120403. At your service.
- es.zip build 2012-04-01 10:48 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203190925-alt1
- repocop cronbuild 20120320. At your service.
- es.zip build 2012-03-19 09:25 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120306. At your service.
- es.zip build 2012-03-01 11:00 UTC

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112201840-alt1
- repocop cronbuild 20111220. At your service.
- es.zip build 2011-12-20 18:40 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112101156-alt1
- repocop cronbuild 20111213. At your service.
- es.zip build 2011-12-10 11:56 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112061030-alt1
- repocop cronbuild 20111206. At your service.
- es.zip build 2011-12-06 10:30 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-es
- es.zip build 2011-11-02 19:30 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111011736-alt4
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111011736-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111011736-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111011736-alt1
- repocop cronbuild 20111105. At your service.
- es.zip build 2011-11-01 17:36 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191503-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191503-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191503-alt1
- es.zip build 2011-10-19 15:03 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109212053-alt1
- es.zip build 2011-09-21 20:53 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- es.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108281454-alt1
- es.zip build 2011-08-28 14:54 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108241221-alt1
- es.zip build 2011-08-24 12:21 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108221159-alt1
- es.zip build 2011-08-22 11:59 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- es.zip build 2011-08-16 13:07 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-es
- es.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20101112-alt1
- es_utf8.zip build 2010-11-12

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101112
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081208
- new build for ALT Linux from cvs
