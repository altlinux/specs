# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename nl
%define packagversion 2.0.0
%define packagedate 201602171652
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Dutch
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-nl
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
* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602171652-alt1
- repocop cronbuild 20160221. At your service.
- nl.zip build 2016-02-17 16:52 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601281313-alt1
- repocop cronbuild 20160131. At your service.
- nl.zip build 2016-01-28 13:13 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511051952-alt1
- repocop cronbuild 20151109. At your service.
- nl.zip build 2015-11-05 19:52 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511011129-alt1
- repocop cronbuild 20151102. At your service.
- nl.zip build 2015-11-01 11:29 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510151445-alt1
- repocop cronbuild 20151019. At your service.
- nl.zip build 2015-10-15 14:45 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509041315-alt1
- repocop cronbuild 20150907. At your service.
- nl.zip build 2015-09-04 13:15 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508112027-alt1
- repocop cronbuild 20150823. At your service.
- nl.zip build 2015-08-11 20:27 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507211128-alt1
- repocop cronbuild 20150723. At your service.
- nl.zip build 2015-07-21 11:28 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507120655-alt1
- repocop cronbuild 20150716. At your service.
- nl.zip build 2015-07-12 06:55 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506041204-alt1
- repocop cronbuild 20150611. At your service.
- nl.zip build 2015-06-04 12:04 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506012001-alt1
- repocop cronbuild 20150604. At your service.
- nl.zip build 2015-06-01 20:01 UTC

* Sat Apr 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504071652-alt1
- repocop cronbuild 20150411. At your service.
- nl.zip build 2015-04-07 16:52 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502041930-alt1
- repocop cronbuild 20150207. At your service.
- nl.zip build 2015-02-04 19:30 UTC

* Sat Jan 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501261416-alt1
- repocop cronbuild 20150131. At your service.
- nl.zip build 2015-01-26 14:16 UTC

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412301436-alt1
- repocop cronbuild 20150102. At your service.
- nl.zip build 2014-12-30 14:36 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412051655-alt1
- repocop cronbuild 20141211. At your service.
- nl.zip build 2014-12-05 16:55 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411011103-alt1
- repocop cronbuild 20141107. At your service.
- nl.zip build 2014-11-01 11:03 UTC

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201408011354-alt1
- repocop cronbuild 20140918. At your service.
- nl.zip build 2014-08-01 13:54 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403311923-alt1
- repocop cronbuild 20140404. At your service.
- nl.zip build 2014-03-31 19:23 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403230838-alt1
- repocop cronbuild 20140328. At your service.
- nl.zip build 2014-03-23 08:38 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403190745-alt1
- repocop cronbuild 20140321. At your service.
- nl.zip build 2014-03-19 07:45 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402120753-alt1
- repocop cronbuild 20140214. At your service.
- nl.zip build 2014-02-12 07:53 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312141005-alt1
- repocop cronbuild 20131220. At your service.
- nl.zip build 2013-12-14 10:05 UTC

* Thu Dec 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312041417-alt1
- repocop cronbuild 20131205. At your service.
- nl.zip build 2013-12-04 14:17 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310281017-alt1
- repocop cronbuild 20131101. At your service.
- nl.zip build 2013-10-28 10:17 UTC

* Thu Oct 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310201929-alt1
- repocop cronbuild 20131024. At your service.
- nl.zip build 2013-10-20 19:29 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310091757-alt1
- repocop cronbuild 20131011. At your service.
- nl.zip build 2013-10-09 17:57 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309281354-alt1
- repocop cronbuild 20131004. At your service.
- nl.zip build 2013-09-28 13:54 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309110652-alt1
- repocop cronbuild 20130913. At your service.
- nl.zip build 2013-09-11 06:52 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308280610-alt1
- repocop cronbuild 20130830. At your service.
- nl.zip build 2013-08-28 06:10 UTC

* Fri Aug 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308061215-alt1
- repocop cronbuild 20130809. At your service.
- nl.zip build 2013-08-06 12:15 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305151953-alt1
- repocop cronbuild 20130517. At your service.
- nl.zip build 2013-05-15 19:53 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305081245-alt1
- repocop cronbuild 20130509. At your service.
- nl.zip build 2013-05-08 12:45 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303172012-alt1
- repocop cronbuild 20130319. At your service.
- nl.zip build 2013-03-17 20:12 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302221108-alt1
- repocop cronbuild 20130225. At your service.
- nl.zip build 2013-02-22 11:08 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- nl.zip build 2013-01-26 15:39 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301041825-alt1
- repocop cronbuild 20130107. At your service.
- nl.zip build 2013-01-04 18:25 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212292201-alt1
- repocop cronbuild 20121231. At your service.
- nl.zip build 2012-12-29 22:01 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209272035-alt1
- repocop cronbuild 20121001. At your service.
- nl.zip build 2012-09-27 20:35 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209051358-alt1
- repocop cronbuild 20120910. At your service.
- nl.zip build 2012-09-05 13:58 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208290900-alt1
- repocop cronbuild 20120904. At your service.
- nl.zip build 2012-08-29 09:00 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208250941-alt1
- repocop cronbuild 20120828. At your service.
- nl.zip build 2012-08-25 09:41 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208181548-alt1
- repocop cronbuild 20120820. At your service.
- nl.zip build 2012-08-18 15:48 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208130831-alt1
- repocop cronbuild 20120814. At your service.
- nl.zip build 2012-08-13 08:31 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208061839-alt1
- repocop cronbuild 20120807. At your service.
- nl.zip build 2012-08-06 18:39 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207211732-alt1
- repocop cronbuild 20120724. At your service.
- nl.zip build 2012-07-21 17:32 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207100841-alt1
- repocop cronbuild 20120717. At your service.
- nl.zip build 2012-07-10 08:41 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207091507-alt1
- repocop cronbuild 20120710. At your service.
- nl.zip build 2012-07-09 15:07 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206290713-alt1
- repocop cronbuild 20120703. At your service.
- nl.zip build 2012-06-29 07:13 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206171818-alt1
- repocop cronbuild 20120618. At your service.
- nl.zip build 2012-06-17 18:18 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206101949-alt1
- repocop cronbuild 20120612. At your service.
- nl.zip build 2012-06-10 19:49 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206031027-alt1
- repocop cronbuild 20120604. At your service.
- nl.zip build 2012-06-03 10:27 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231549-alt1
- repocop cronbuild 20120528. At your service.
- nl.zip build 2012-05-23 15:49 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205202016-alt1
- repocop cronbuild 20120521. At your service.
- nl.zip build 2012-05-20 20:16 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205102039-alt1
- repocop cronbuild 20120514. At your service.
- nl.zip build 2012-05-10 20:39 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205031134-alt1
- repocop cronbuild 20120507. At your service.
- nl.zip build 2012-05-03 11:34 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204241002-alt1
- repocop cronbuild 20120430. At your service.
- nl.zip build 2012-04-24 10:02 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204221206-alt1
- repocop cronbuild 20120423. At your service.
- nl.zip build 2012-04-22 12:06 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204162047-alt1
- repocop cronbuild 20120416. At your service.
- nl.zip build 2012-04-16 20:47 UTC

* Mon Apr 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204051550-alt1
- repocop cronbuild 20120409. At your service.
- nl.zip build 2012-04-05 15:50 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203281921-alt1
- repocop cronbuild 20120402. At your service.
- nl.zip build 2012-03-28 19:21 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203140945-alt1
- repocop cronbuild 20120319. At your service.
- nl.zip build 2012-03-14 09:45 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203071928-alt1
- repocop cronbuild 20120307. At your service.
- nl.zip build 2012-03-07 19:28 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202020910-alt1
- repocop cronbuild 20120208. At your service.
- nl.zip build 2012-02-02 09:10 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201250830-alt1
- repocop cronbuild 20120125. At your service.
- nl.zip build 2012-01-25 08:30 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201092126-alt1
- repocop cronbuild 20120111. At your service.
- nl.zip build 2012-01-09 21:26 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112020846-alt1
- repocop cronbuild 20111207. At your service.
- nl.zip build 2011-12-02 08:46 UTC

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111290736-alt1
- repocop cronbuild 20111130. At your service.
- nl.zip build 2011-11-29 07:36 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111161119-alt2
- Fix requires

* Thu Nov 17 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111161119-alt1
- repocop cronbuild 20111117. At your service.
- nl.zip build 2011-11-16 11:19 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111141719-alt1
- repocop cronbuild 20111116. At your service.
- nl.zip build 2011-11-14 17:19 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111102028-alt2
- Use moodle2.0-lang-cronbuild for cronbuild

* Sat Nov 12 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111102028-alt1
- repocop cronbuild 20111112. At your service.
- nl.zip build 2011-11-10 20:28 UTC

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110260752-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201110260752-alt1
- repocop cronbuild 20111105. At your service.
- nl.zip build 2011-10-26 07:52 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- nl.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- nl.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109071908-alt1
- nl.zip build 2011-09-07 19:08 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Fix package version

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.20110810-alt1
- Rename package to moodle2.0-lang-nl
- nl.zip build 2011-08-11 23:00 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110802-alt1
- nl_utf8.zip build 2011-08-02
- initial build for ALT Linux Sisyphus
