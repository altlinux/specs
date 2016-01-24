# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename de
%define packagversion 2.5.0
%define packagedate 201601221454
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname German
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-de
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
* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601221454-alt1
- repocop cronbuild 20160124. At your service.
- de.zip build 2016-01-22 14:54 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201512101043-alt1
- repocop cronbuild 20151214. At your service.
- de.zip build 2015-12-10 10:43 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201512070731-alt1
- repocop cronbuild 20151207. At your service.
- de.zip build 2015-12-07 07:31 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511291100-alt1
- repocop cronbuild 20151130. At your service.
- de.zip build 2015-11-29 11:00 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511221224-alt1
- repocop cronbuild 20151123. At your service.
- de.zip build 2015-11-22 12:24 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511151207-alt1
- repocop cronbuild 20151116. At your service.
- de.zip build 2015-11-15 12:07 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201511090711-alt1
- repocop cronbuild 20151109. At your service.
- de.zip build 2015-11-09 07:11 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510300835-alt1
- repocop cronbuild 20151102. At your service.
- de.zip build 2015-10-30 08:35 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510230742-alt1
- repocop cronbuild 20151026. At your service.
- de.zip build 2015-10-23 07:42 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510171520-alt1
- repocop cronbuild 20151019. At your service.
- de.zip build 2015-10-17 15:20 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510081515-alt1
- repocop cronbuild 20151012. At your service.
- de.zip build 2015-10-08 15:15 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201510022118-alt1
- repocop cronbuild 20151005. At your service.
- de.zip build 2015-10-02 21:18 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509240736-alt1
- repocop cronbuild 20150928. At your service.
- de.zip build 2015-09-24 07:36 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509091700-alt1
- repocop cronbuild 20150914. At your service.
- de.zip build 2015-09-09 17:00 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201509040856-alt1
- repocop cronbuild 20150907. At your service.
- de.zip build 2015-09-04 08:56 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508301127-alt1
- repocop cronbuild 20150831. At your service.
- de.zip build 2015-08-30 11:27 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201508191441-alt1
- repocop cronbuild 20150823. At your service.
- de.zip build 2015-08-19 14:41 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507281218-alt1
- repocop cronbuild 20150730. At your service.
- de.zip build 2015-07-28 12:18 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507222131-alt1
- repocop cronbuild 20150723. At your service.
- de.zip build 2015-07-22 21:31 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507050809-alt1
- repocop cronbuild 20150709. At your service.
- de.zip build 2015-07-05 08:09 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201507020918-alt1
- repocop cronbuild 20150702. At your service.
- de.zip build 2015-07-02 09:18 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506231521-alt1
- repocop cronbuild 20150625. At your service.
- de.zip build 2015-06-23 15:21 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506180950-alt1
- repocop cronbuild 20150618. At your service.
- de.zip build 2015-06-18 09:50 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506091306-alt1
- repocop cronbuild 20150611. At your service.
- de.zip build 2015-06-09 13:06 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201506020708-alt1
- repocop cronbuild 20150604. At your service.
- de.zip build 2015-06-02 07:08 UTC

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505201413-alt1
- repocop cronbuild 20150522. At your service.
- de.zip build 2015-05-20 14:13 UTC

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505130746-alt1
- repocop cronbuild 20150515. At your service.
- de.zip build 2015-05-13 07:46 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201505072040-alt1
- repocop cronbuild 20150508. At your service.
- de.zip build 2015-05-07 20:40 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504301531-alt1
- repocop cronbuild 20150501. At your service.
- de.zip build 2015-04-30 15:31 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504240930-alt1
- repocop cronbuild 20150424. At your service.
- de.zip build 2015-04-24 09:30 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504161835-alt1
- repocop cronbuild 20150417. At your service.
- de.zip build 2015-04-16 18:35 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201504101131-alt1
- repocop cronbuild 20150410. At your service.
- de.zip build 2015-04-10 11:31 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503311916-alt1
- repocop cronbuild 20150403. At your service.
- de.zip build 2015-03-31 19:16 UTC

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503130923-alt1
- repocop cronbuild 20150320. At your service.
- de.zip build 2015-03-13 09:23 UTC

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201503120759-alt1
- repocop cronbuild 20150313. At your service.
- de.zip build 2015-03-12 07:59 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502261937-alt1
- repocop cronbuild 20150227. At your service.
- de.zip build 2015-02-26 19:37 UTC

* Fri Feb 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502192228-alt1
- repocop cronbuild 20150220. At your service.
- de.zip build 2015-02-19 22:28 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502120723-alt1
- repocop cronbuild 20150213. At your service.
- de.zip build 2015-02-12 07:23 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201502051440-alt1
- repocop cronbuild 20150206. At your service.
- de.zip build 2015-02-05 14:40 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501241236-alt1
- repocop cronbuild 20150130. At your service.
- de.zip build 2015-01-24 12:36 UTC

* Fri Jan 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501221435-alt1
- repocop cronbuild 20150123. At your service.
- de.zip build 2015-01-22 14:35 UTC

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501150829-alt1
- repocop cronbuild 20150116. At your service.
- de.zip build 2015-01-15 08:29 UTC

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201501041046-alt1
- repocop cronbuild 20150109. At your service.
- de.zip build 2015-01-04 10:46 UTC

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412281432-alt1
- repocop cronbuild 20150102. At your service.
- de.zip build 2014-12-28 14:32 UTC

* Fri Dec 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412251530-alt1
- repocop cronbuild 20141226. At your service.
- de.zip build 2014-12-25 15:30 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412141527-alt1
- repocop cronbuild 20141219. At your service.
- de.zip build 2014-12-14 15:27 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412051625-alt1
- repocop cronbuild 20141212. At your service.
- de.zip build 2014-12-05 16:25 UTC

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201412011644-alt1
- repocop cronbuild 20141205. At your service.
- de.zip build 2014-12-01 16:44 UTC

* Fri Nov 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411190718-alt1
- repocop cronbuild 20141121. At your service.
- de.zip build 2014-11-19 07:18 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411140812-alt1
- repocop cronbuild 20141114. At your service.
- de.zip build 2014-11-14 08:12 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411061954-alt1
- repocop cronbuild 20141107. At your service.
- de.zip build 2014-11-06 19:54 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410221415-alt1
- repocop cronbuild 20141024. At your service.
- de.zip build 2014-10-22 14:15 UTC

* Fri Oct 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410100857-alt1
- repocop cronbuild 20141017. At your service.
- de.zip build 2014-10-10 08:57 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410091018-alt1
- repocop cronbuild 20141010. At your service.
- de.zip build 2014-10-09 10:18 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409280511-alt1
- repocop cronbuild 20141003. At your service.
- de.zip build 2014-09-28 05:11 UTC

* Fri Sep 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409230822-alt1
- repocop cronbuild 20140926. At your service.
- de.zip build 2014-09-23 08:22 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409170823-alt1
- repocop cronbuild 20140919. At your service.
- de.zip build 2014-09-17 08:23 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201407011112-alt1
- repocop cronbuild 20140705. At your service.
- de.zip build 2014-07-01 11:12 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406271330-alt1
- repocop cronbuild 20140628. At your service.
- de.zip build 2014-06-27 13:30 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406201217-alt1
- repocop cronbuild 20140621. At your service.
- de.zip build 2014-06-20 12:17 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406112142-alt1
- repocop cronbuild 20140613. At your service.
- de.zip build 2014-06-11 21:42 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201406041954-alt1
- repocop cronbuild 20140606. At your service.
- de.zip build 2014-06-04 19:54 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405291607-alt1
- repocop cronbuild 20140530. At your service.
- de.zip build 2014-05-29 16:07 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405221321-alt1
- repocop cronbuild 20140523. At your service.
- de.zip build 2014-05-22 13:21 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405131651-alt1
- repocop cronbuild 20140516. At your service.
- de.zip build 2014-05-13 16:51 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405082304-alt1
- repocop cronbuild 20140509. At your service.
- de.zip build 2014-05-08 23:04 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201405011622-alt1
- repocop cronbuild 20140502. At your service.
- de.zip build 2014-05-01 16:22 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404241436-alt1
- repocop cronbuild 20140425. At your service.
- de.zip build 2014-04-24 14:36 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404150930-alt1
- repocop cronbuild 20140418. At your service.
- de.zip build 2014-04-15 09:30 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404081341-alt1
- repocop cronbuild 20140411. At your service.
- de.zip build 2014-04-08 13:41 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201404032046-alt1
- repocop cronbuild 20140404. At your service.
- de.zip build 2014-04-03 20:46 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403231627-alt1
- repocop cronbuild 20140328. At your service.
- de.zip build 2014-03-23 16:27 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201403201710-alt1
- repocop cronbuild 20140321. At your service.
- de.zip build 2014-03-20 17:10 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402241437-alt1
- repocop cronbuild 20140228. At your service.
- de.zip build 2014-02-24 14:37 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201402181759-alt1
- repocop cronbuild 20140221. At your service.
- de.zip build 2014-02-18 17:59 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401292000-alt1
- repocop cronbuild 20140131. At your service.
- de.zip build 2014-01-29 20:00 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401231346-alt1
- repocop cronbuild 20140124. At your service.
- de.zip build 2014-01-23 13:46 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401100959-alt1
- repocop cronbuild 20140117. At your service.
- de.zip build 2014-01-10 09:59 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401021333-alt1
- repocop cronbuild 20140103. At your service.
- de.zip build 2014-01-02 13:33 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312260921-alt1
- repocop cronbuild 20131227. At your service.
- de.zip build 2013-12-26 09:21 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312181625-alt1
- repocop cronbuild 20131220. At your service.
- de.zip build 2013-12-18 16:25 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- de.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312051021-alt1
- repocop cronbuild 20131206. At your service.
- de.zip build 2013-12-05 10:21 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311261450-alt1
- repocop cronbuild 20131129. At your service.
- de.zip build 2013-11-26 14:50 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311200955-alt1
- repocop cronbuild 20131122. At your service.
- de.zip build 2013-11-20 09:55 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311141516-alt1
- repocop cronbuild 20131115. At your service.
- de.zip build 2013-11-14 15:16 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311072158-alt1
- repocop cronbuild 20131108. At your service.
- de.zip build 2013-11-07 21:58 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201311011015-alt1
- repocop cronbuild 20131101. At your service.
- de.zip build 2013-11-01 10:15 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310170825-alt1
- repocop cronbuild 20131018. At your service.
- de.zip build 2013-10-17 08:25 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310102235-alt1
- repocop cronbuild 20131011. At your service.
- de.zip build 2013-10-10 22:35 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309280849-alt1
- repocop cronbuild 20131004. At your service.
- de.zip build 2013-09-28 08:49 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309241626-alt1
- repocop cronbuild 20130927. At your service.
- de.zip build 2013-09-24 16:26 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201309050954-alt1
- repocop cronbuild 20130906. At your service.
- de.zip build 2013-09-05 09:54 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308262028-alt1
- repocop cronbuild 20130831. At your service.
- de.zip build 2013-08-26 20:28 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308231503-alt1
- repocop cronbuild 20130824. At your service.
- de.zip build 2013-08-23 15:03 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308151529-alt1
- repocop cronbuild 20130817. At your service.
- de.zip build 2013-08-15 15:29 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308071245-alt1
- repocop cronbuild 20130810. At your service.
- de.zip build 2013-08-07 12:45 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308010958-alt1
- repocop cronbuild 20130803. At your service.
- de.zip build 2013-08-01 09:58 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307261257-alt1
- repocop cronbuild 20130727. At your service.
- de.zip build 2013-07-26 12:57 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307190654-alt1
- repocop cronbuild 20130720. At your service.
- de.zip build 2013-07-19 06:54 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307121421-alt1
- repocop cronbuild 20130713. At your service.
- de.zip build 2013-07-12 14:21 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307011604-alt1
- repocop cronbuild 20130706. At your service.
- de.zip build 2013-07-01 16:04 UTC

* Sat Jun 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306261349-alt1
- repocop cronbuild 20130629. At your service.
- de.zip build 2013-06-26 13:49 UTC

* Sat Jun 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306191824-alt1
- repocop cronbuild 20130622. At your service.
- de.zip build 2013-06-19 18:24 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140511-alt1
- repocop cronbuild 20130615. At your service.
- de.zip build 2013-06-14 05:11 UTC

* Sat Jun 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306040946-alt1
- repocop cronbuild 20130608. At your service.
- de.zip build 2013-06-04 09:46 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305300946-alt1
- Rename package to moodle2.5-lang-de
- de.zip build 2013-05-30 09:46 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305231534-alt1
- repocop cronbuild 20130524. At your service.
- de.zip build 2013-05-23 15:34 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305131700-alt1
- repocop cronbuild 20130517. At your service.
- de.zip build 2013-05-13 17:00 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305041513-alt1
- repocop cronbuild 20130509. At your service.
- de.zip build 2013-05-04 15:13 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304171317-alt1
- Rename package to moodle2.4-lang-de
- de.zip build 2013-04-17 13:17 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304131040-alt1
- repocop cronbuild 20130417. At your service.
- de.zip build 2013-04-13 10:40 UTC

* Wed Apr 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304090659-alt1
- repocop cronbuild 20130410. At your service.
- de.zip build 2013-04-09 06:59 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304021956-alt1
- repocop cronbuild 20130403. At your service.
- de.zip build 2013-04-02 19:56 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303261937-alt1
- repocop cronbuild 20130327. At your service.
- de.zip build 2013-03-26 19:37 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303150711-alt1
- repocop cronbuild 20130320. At your service.
- de.zip build 2013-03-15 07:11 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303121021-alt1
- repocop cronbuild 20130313. At your service.
- de.zip build 2013-03-12 10:21 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302251122-alt1
- repocop cronbuild 20130304. At your service.
- de.zip build 2013-02-25 11:22 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302221755-alt1
- repocop cronbuild 20130225. At your service.
- de.zip build 2013-02-22 17:55 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302151036-alt1
- repocop cronbuild 20130218. At your service.
- de.zip build 2013-02-15 10:36 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261243-alt1
- repocop cronbuild 20130128. At your service.
- de.zip build 2013-01-26 12:43 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301201421-alt1
- repocop cronbuild 20130121. At your service.
- de.zip build 2013-01-20 14:21 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301101111-alt1
- repocop cronbuild 20130114. At your service.
- de.zip build 2013-01-10 11:11 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212300823-alt1
- repocop cronbuild 20121231. At your service.
- de.zip build 2012-12-30 08:23 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212221501-alt1
- repocop cronbuild 20121224. At your service.
- de.zip build 2012-12-22 15:01 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212131616-alt1
- repocop cronbuild 20121217. At your service.
- de.zip build 2012-12-13 16:16 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211280924-alt1
- repocop cronbuild 20121203. At your service.
- de.zip build 2012-11-28 09:24 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211251702-alt1
- repocop cronbuild 20121126. At your service.
- de.zip build 2012-11-25 17:02 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211181000-alt1
- repocop cronbuild 20121119. At your service.
- de.zip build 2012-11-18 10:00 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211111645-alt1
- repocop cronbuild 20121112. At your service.
- de.zip build 2012-11-11 16:45 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211021541-alt1
- repocop cronbuild 20121105. At your service.
- de.zip build 2012-11-02 15:41 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210281116-alt1
- repocop cronbuild 20121029. At your service.
- de.zip build 2012-10-28 11:16 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210211721-alt1
- repocop cronbuild 20121022. At your service.
- de.zip build 2012-10-21 17:21 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210101233-alt1
- repocop cronbuild 20121015. At your service.
- de.zip build 2012-10-10 12:33 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210071633-alt1
- repocop cronbuild 20121008. At your service.
- de.zip build 2012-10-07 16:33 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209280635-alt1
- repocop cronbuild 20121001. At your service.
- de.zip build 2012-09-28 06:35 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209112324-alt1
- repocop cronbuild 20120918. At your service.
- de.zip build 2012-09-11 23:24 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209090651-alt1
- repocop cronbuild 20120911. At your service.
- de.zip build 2012-09-09 06:51 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311647-alt1
- repocop cronbuild 20120904. At your service.
- de.zip build 2012-08-31 16:47 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208211159-alt1
- repocop cronbuild 20120828. At your service.
- de.zip build 2012-08-21 11:59 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208191759-alt1
- repocop cronbuild 20120820. At your service.
- de.zip build 2012-08-19 17:59 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208111045-alt1
- repocop cronbuild 20120814. At your service.
- de.zip build 2012-08-11 10:45 UTC

* Tue Aug 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208060813-alt1
- repocop cronbuild 20120807. At your service.
- de.zip build 2012-08-06 08:13 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207301716-alt1
- repocop cronbuild 20120731. At your service.
- de.zip build 2012-07-30 17:16 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207231150-alt1
- repocop cronbuild 20120724. At your service.
- de.zip build 2012-07-23 11:50 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207121607-alt1
- repocop cronbuild 20120717. At your service.
- de.zip build 2012-07-12 16:07 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207091555-alt1
- repocop cronbuild 20120710. At your service.
- de.zip build 2012-07-09 15:55 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207021842-alt1
- repocop cronbuild 20120703. At your service.
- de.zip build 2012-07-02 18:42 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206241901-alt1
- repocop cronbuild 20120626. At your service.
- de.zip build 2012-06-24 19:01 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206181719-alt1
- repocop cronbuild 20120619. At your service.
- de.zip build 2012-06-18 17:19 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206080854-alt1
- repocop cronbuild 20120612. At your service.
- de.zip build 2012-06-08 08:54 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206041513-alt1
- repocop cronbuild 20120605. At your service.
- de.zip build 2012-06-04 15:13 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205280958-alt1
- repocop cronbuild 20120529. At your service.
- de.zip build 2012-05-28 09:58 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205211742-alt1
- repocop cronbuild 20120521. At your service.
- de.zip build 2012-05-21 17:42 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205120821-alt1
- repocop cronbuild 20120515. At your service.
- de.zip build 2012-05-12 08:21 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205072118-alt1
- repocop cronbuild 20120508. At your service.
- de.zip build 2012-05-07 21:18 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204280914-alt1
- repocop cronbuild 20120501. At your service.
- de.zip build 2012-04-28 09:14 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204161516-alt1
- repocop cronbuild 20120417. At your service.
- de.zip build 2012-04-16 15:16 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204060624-alt1
- repocop cronbuild 20120410. At your service.
- de.zip build 2012-04-06 06:24 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204021424-alt1
- repocop cronbuild 20120403. At your service.
- de.zip build 2012-04-02 14:24 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203230604-alt1
- repocop cronbuild 20120327. At your service.
- de.zip build 2012-03-23 06:04 UTC

* Mon Mar 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203181916-alt1
- Rename package to moodle2.2-lang-de
- de.zip build 2012-03-18 19:16 UTC

* Tue Mar 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203100131-alt1
- repocop cronbuild 20120313. At your service.
- de.zip build 2012-03-10 01:31 UTC

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203041741-alt1
- repocop cronbuild 20120309. At your service.
- de.zip build 2012-03-04 17:41 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203012147-alt1
- repocop cronbuild 20120302. At your service.
- de.zip build 2012-03-01 21:47 UTC

* Fri Feb 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202201600-alt1
- repocop cronbuild 20120224. At your service.
- de.zip build 2012-02-20 16:00 UTC

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202171612-alt1
- repocop cronbuild 20120217. At your service.
- de.zip build 2012-02-17 16:12 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202102121-alt1
- repocop cronbuild 20120210. At your service.
- de.zip build 2012-02-10 21:21 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201291051-alt1
- repocop cronbuild 20120203. At your service.
- de.zip build 2012-01-29 10:51 UTC

* Fri Jan 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201271719-alt1
- repocop cronbuild 20120127. At your service.
- de.zip build 2012-01-27 17:19 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201180523-alt1
- repocop cronbuild 20120120. At your service.
- de.zip build 2012-01-18 05:23 UTC

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201101616-alt1
- repocop cronbuild 20120113. At your service.
- de.zip build 2012-01-10 16:16 UTC

* Fri Jan 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201052228-alt1
- repocop cronbuild 20120106. At your service.
- de.zip build 2012-01-05 22:28 UTC

* Fri Dec 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112291253-alt1
- repocop cronbuild 20111230. At your service.
- de.zip build 2011-12-29 12:53 UTC

* Fri Dec 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112232118-alt1
- repocop cronbuild 20111223. At your service.
- de.zip build 2011-12-23 21:18 UTC

* Fri Dec 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112161557-alt1
- repocop cronbuild 20111216. At your service.
- de.zip build 2011-12-16 15:57 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- de.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111252051-alt1
- repocop cronbuild 20111125. At your service.
- de.zip build 2011-11-25 20:51 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-de
- de.zip build 2011-11-02 19:30 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110210507-alt1
- de.zip build 2011-10-21 05:07 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- de.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109181008-alt1
- de.zip build 2011-09-18 10:08 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109111520-alt1
- de.zip build 2011-09-11 15:20 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108220638-alt2
- Fix requires

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108220638-alt1
- de.zip build 2011-08-22 06:38 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108191519-alt1
- de.zip build 2011-08-19 15:19 UTC

* Fri Aug 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108181355-alt1
- de.zip build 2011-08-18 13:55 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- de.zip build 2011-08-16 13:07

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-de
- de.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110705-alt1
- de_utf8.zip build 2011-07-05

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081028
- new build for ALT Linux from cvs
