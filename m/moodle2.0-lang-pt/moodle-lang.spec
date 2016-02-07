# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename pt
%define packagversion 2.0.0
%define packagedate 201602031515
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Portuguese
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-pt
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
* Sun Feb 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602031515-alt1
- repocop cronbuild 20160207. At your service.
- pt.zip build 2016-02-03 15:15 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601282136-alt1
- repocop cronbuild 20160131. At your service.
- pt.zip build 2016-01-28 21:36 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601221351-alt1
- repocop cronbuild 20160124. At your service.
- pt.zip build 2016-01-22 13:51 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512111833-alt1
- repocop cronbuild 20151214. At your service.
- pt.zip build 2015-12-11 18:33 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511121316-alt1
- repocop cronbuild 20151116. At your service.
- pt.zip build 2015-11-12 13:16 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510261749-alt1
- repocop cronbuild 20151102. At your service.
- pt.zip build 2015-10-26 17:49 UTC

* Mon Sep 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509160759-alt1
- repocop cronbuild 20150921. At your service.
- pt.zip build 2015-09-16 07:59 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505261150-alt1
- repocop cronbuild 20150604. At your service.
- pt.zip build 2015-05-26 11:50 UTC

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505211257-alt1
- repocop cronbuild 20150522. At your service.
- pt.zip build 2015-05-21 12:57 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504231813-alt1
- repocop cronbuild 20150424. At your service.
- pt.zip build 2015-04-23 18:13 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504152059-alt1
- repocop cronbuild 20150417. At your service.
- pt.zip build 2015-04-15 20:59 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504011623-alt1
- repocop cronbuild 20150403. At your service.
- pt.zip build 2015-04-01 16:23 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412161059-alt1
- repocop cronbuild 20141219. At your service.
- pt.zip build 2014-12-16 10:59 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412101302-alt1
- repocop cronbuild 20141211. At your service.
- pt.zip build 2014-12-10 13:02 UTC

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412031311-alt1
- repocop cronbuild 20141205. At your service.
- pt.zip build 2014-12-03 13:11 UTC

* Thu Nov 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411271009-alt1
- repocop cronbuild 20141127. At your service.
- pt.zip build 2014-11-27 10:09 UTC

* Fri Nov 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411171812-alt1
- repocop cronbuild 20141121. At your service.
- pt.zip build 2014-11-17 18:12 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411131153-alt1
- repocop cronbuild 20141114. At your service.
- pt.zip build 2014-11-13 11:53 UTC

* Thu Oct 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410100925-alt1
- repocop cronbuild 20141016. At your service.
- pt.zip build 2014-10-10 09:25 UTC

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409171640-alt1
- repocop cronbuild 20140918. At your service.
- pt.zip build 2014-09-17 16:40 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201407041700-alt1
- repocop cronbuild 20140705. At your service.
- pt.zip build 2014-07-04 17:00 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406241151-alt1
- repocop cronbuild 20140628. At your service.
- pt.zip build 2014-06-24 11:51 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406181831-alt1
- repocop cronbuild 20140621. At your service.
- pt.zip build 2014-06-18 18:31 UTC

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403261607-alt1
- repocop cronbuild 20140329. At your service.
- pt.zip build 2014-03-26 16:07 UTC

* Sat Mar 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403191606-alt1
- repocop cronbuild 20140322. At your service.
- pt.zip build 2014-03-19 16:06 UTC

* Sat Mar 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403051121-alt1
- repocop cronbuild 20140308. At your service.
- pt.zip build 2014-03-05 11:21 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402281703-alt1
- repocop cronbuild 20140301. At your service.
- pt.zip build 2014-02-28 17:03 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402171901-alt1
- repocop cronbuild 20140221. At your service.
- pt.zip build 2014-02-17 19:01 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402141841-alt1
- repocop cronbuild 20140215. At your service.
- pt.zip build 2014-02-14 18:41 UTC

* Sat Feb 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402041759-alt1
- repocop cronbuild 20140208. At your service.
- pt.zip build 2014-02-04 17:59 UTC

* Sat Dec 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312111357-alt1
- repocop cronbuild 20131214. At your service.
- pt.zip build 2013-12-11 13:57 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311051217-alt1
- repocop cronbuild 20131108. At your service.
- pt.zip build 2013-11-05 12:17 UTC

* Sat Nov 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310311450-alt1
- repocop cronbuild 20131102. At your service.
- pt.zip build 2013-10-31 14:50 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310180927-alt1
- repocop cronbuild 20131018. At your service.
- pt.zip build 2013-10-18 09:27 UTC

* Sat Oct 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310101420-alt1
- repocop cronbuild 20131012. At your service.
- pt.zip build 2013-10-10 14:20 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310031523-alt1
- repocop cronbuild 20131004. At your service.
- pt.zip build 2013-10-03 15:23 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309250931-alt1
- repocop cronbuild 20130927. At your service.
- pt.zip build 2013-09-25 09:31 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309051619-alt1
- repocop cronbuild 20130906. At your service.
- pt.zip build 2013-09-05 16:19 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305231744-alt1
- repocop cronbuild 20130524. At your service.
- pt.zip build 2013-05-23 17:44 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305081644-alt1
- repocop cronbuild 20130509. At your service.
- pt.zip build 2013-05-08 16:44 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302201439-alt1
- repocop cronbuild 20130225. At your service.
- pt.zip build 2013-02-20 14:39 UTC

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302041927-alt1
- repocop cronbuild 20130211. At your service.
- pt.zip build 2013-02-04 19:27 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301231625-alt1
- repocop cronbuild 20130128. At your service.
- pt.zip build 2013-01-23 16:25 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301161900-alt1
- repocop cronbuild 20130121. At your service.
- pt.zip build 2013-01-16 19:00 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301091800-alt1
- repocop cronbuild 20130114. At your service.
- pt.zip build 2013-01-09 18:00 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212102026-alt1
- repocop cronbuild 20121217. At your service.
- pt.zip build 2012-12-10 20:26 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212051940-alt1
- repocop cronbuild 20121210. At your service.
- pt.zip build 2012-12-05 19:40 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210081840-alt1
- repocop cronbuild 20121015. At your service.
- pt.zip build 2012-10-08 18:40 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210021619-alt1
- repocop cronbuild 20121008. At your service.
- pt.zip build 2012-10-02 16:19 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209201621-alt1
- repocop cronbuild 20121001. At your service.
- pt.zip build 2012-09-20 16:21 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209171758-alt1
- repocop cronbuild 20120917. At your service.
- pt.zip build 2012-09-17 17:58 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208051809-alt1
- repocop cronbuild 20120807. At your service.
- pt.zip build 2012-08-05 18:09 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207171304-alt1
- repocop cronbuild 20120724. At your service.
- pt.zip build 2012-07-17 13:04 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207161555-alt1
- repocop cronbuild 20120717. At your service.
- pt.zip build 2012-07-16 15:55 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207092036-alt1
- repocop cronbuild 20120710. At your service.
- pt.zip build 2012-07-09 20:36 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207021443-alt1
- repocop cronbuild 20120703. At your service.
- pt.zip build 2012-07-02 14:43 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206251431-alt1
- repocop cronbuild 20120626. At your service.
- pt.zip build 2012-06-25 14:31 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206151013-alt1
- repocop cronbuild 20120618. At your service.
- pt.zip build 2012-06-15 10:13 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206042302-alt1
- repocop cronbuild 20120612. At your service.
- pt.zip build 2012-06-04 23:02 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206012236-alt1
- repocop cronbuild 20120604. At your service.
- pt.zip build 2012-06-01 22:36 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231549-alt1
- repocop cronbuild 20120528. At your service.
- pt.zip build 2012-05-23 15:49 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204260657-alt1
- repocop cronbuild 20120430. At your service.
- pt.zip build 2012-04-26 06:57 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204192250-alt1
- repocop cronbuild 20120423. At your service.
- pt.zip build 2012-04-19 22:50 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204161243-alt1
- repocop cronbuild 20120416. At your service.
- pt.zip build 2012-04-16 12:43 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203291546-alt1
- repocop cronbuild 20120402. At your service.
- pt.zip build 2012-03-29 15:46 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203261439-alt1
- repocop cronbuild 20120327. At your service.
- pt.zip build 2012-03-26 14:39 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203171452-alt1
- repocop cronbuild 20120319. At your service.
- pt.zip build 2012-03-17 14:52 UTC

* Mon Mar 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203082202-alt1
- repocop cronbuild 20120312. At your service.
- pt.zip build 2012-03-08 22:02 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203071939-alt1
- repocop cronbuild 20120307. At your service.
- pt.zip build 2012-03-07 19:39 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201251818-alt1
- repocop cronbuild 20120125. At your service.
- pt.zip build 2012-01-25 18:18 UTC

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
