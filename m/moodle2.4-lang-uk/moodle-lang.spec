# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename uk
%define packagversion 2.4.0
%define packagedate 201602201337
%define moodlebranch 2.4
%define moodlepackagename %moodle_name%moodlebranch
%define langname Ukrainian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.4-lang-uk
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
* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201602201337-alt1
- repocop cronbuild 20160221. At your service.
- uk.zip build 2016-02-20 13:37 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511261717-alt1
- repocop cronbuild 20151130. At your service.
- uk.zip build 2015-11-26 17:17 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507221729-alt1
- repocop cronbuild 20150723. At your service.
- uk.zip build 2015-07-22 17:29 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504021734-alt1
- repocop cronbuild 20150403. At your service.
- uk.zip build 2015-04-02 17:34 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201503211928-alt1
- repocop cronbuild 20150327. At your service.
- uk.zip build 2015-03-21 19:28 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501211206-alt1
- repocop cronbuild 20150123. At your service.
- uk.zip build 2015-01-21 12:06 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412180907-alt1
- repocop cronbuild 20141219. At your service.
- uk.zip build 2014-12-18 09:07 UTC

* Fri Nov 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201411271727-alt1
- repocop cronbuild 20141128. At your service.
- uk.zip build 2014-11-27 17:27 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201410091558-alt1
- repocop cronbuild 20141010. At your service.
- uk.zip build 2014-10-09 15:58 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201409100947-alt1
- repocop cronbuild 20140919. At your service.
- uk.zip build 2014-09-10 09:47 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402161645-alt1
- repocop cronbuild 20140221. At your service.
- uk.zip build 2014-02-16 16:45 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312130546-alt1
- repocop cronbuild 20131220. At your service.
- uk.zip build 2013-12-13 05:46 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310091141-alt1
- repocop cronbuild 20131011. At your service.
- uk.zip build 2013-10-09 11:41 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308151936-alt1
- repocop cronbuild 20130817. At your service.
- uk.zip build 2013-08-15 19:36 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306060511-alt1
- repocop cronbuild 20130607. At your service.
- uk.zip build 2013-06-06 05:11 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305281943-alt1
- repocop cronbuild 20130531. At your service.
- uk.zip build 2013-05-28 19:43 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221013-alt1
- repocop cronbuild 20130524. At your service.
- uk.zip build 2013-05-22 10:13 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304081928-alt1
- Rename package to moodle2.4-lang-uk
- uk.zip build 2013-04-08 19:28 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304081928-alt1
- repocop cronbuild 20130410. At your service.
- uk.zip build 2013-04-08 19:28 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303180719-alt1
- repocop cronbuild 20130320. At your service.
- uk.zip build 2013-03-18 07:19 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303111907-alt1
- repocop cronbuild 20130313. At your service.
- uk.zip build 2013-03-11 19:07 UTC

* Tue Mar 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303042140-alt1
- repocop cronbuild 20130305. At your service.
- uk.zip build 2013-03-04 21:40 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302242043-alt1
- repocop cronbuild 20130225. At your service.
- uk.zip build 2013-02-24 20:43 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301030535-alt1
- repocop cronbuild 20130107. At your service.
- uk.zip build 2013-01-03 05:35 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210250337-alt1
- repocop cronbuild 20121029. At your service.
- uk.zip build 2012-10-25 03:37 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210101341-alt1
- repocop cronbuild 20121015. At your service.
- uk.zip build 2012-10-10 13:41 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210041908-alt1
- repocop cronbuild 20121008. At your service.
- uk.zip build 2012-10-04 19:08 UTC

* Wed Aug 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207310815-alt1
- repocop cronbuild 20120801. At your service.
- uk.zip build 2012-07-31 08:15 UTC

* Wed Jun 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206130920-alt1
- repocop cronbuild 20120613. At your service.
- uk.zip build 2012-06-13 09:20 UTC

* Wed May 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120530. At your service.
- uk.zip build 2012-05-23 15:49 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205091839-alt1
- repocop cronbuild 20120515. At your service.
- uk.zip build 2012-05-09 18:39 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205051809-alt1
- repocop cronbuild 20120508. At your service.
- uk.zip build 2012-05-05 18:09 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204241104-alt1
- repocop cronbuild 20120424. At your service.
- uk.zip build 2012-04-24 11:04 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203162136-alt1
- Rename package to moodle2.2-lang-uk
- uk.zip build 2012-03-16 21:36 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203152118-alt1
- repocop cronbuild 20120320. At your service.
- uk.zip build 2012-03-15 21:18 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- uk.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201106210100-alt1
- Rename package to moodle2.1-lang-uk
- uk.zip build 2011-06-21 01:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt7
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt6
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt5
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt4
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt3
- Update for cronbuild use

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt2
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt1
- Rename package to moodle2.0-lang-uk
- uk.zip build 2011-03-03 17:30 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- uk_utf8.zip build 2010-05-26

* Tue Nov 23 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt2.cvs20100526
- inheritance fixed

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Tue Oct 27 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt2.1.cvs20091010
- rebuild with new Moodle

* Mon Oct 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20091010
- new build from cvs

* Sun Jul 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20090518
- new build from cvs

* Mon Oct 13 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080926
- new build from cvs

* Mon Sep 08 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080731
- add build requires on rpm-build-webserver-common
- new build from cvs

* Thu Jun 26 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt2.cvs20080526
- change path moodle location

* Mon Jun 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.cvs20080526
- new build for ALT Linux
