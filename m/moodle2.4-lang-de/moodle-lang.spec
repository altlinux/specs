# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename de
%define packagversion 2.4.0
%define packagedate 201602060910
%define moodlebranch 2.4
%define moodlepackagename %moodle_name%moodlebranch
%define langname German
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.4-lang-de
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
* Sun Feb 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201602060910-alt1
- repocop cronbuild 20160207. At your service.
- de.zip build 2016-02-06 09:10 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201601291541-alt1
- repocop cronbuild 20160131. At your service.
- de.zip build 2016-01-29 15:41 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201601221454-alt1
- repocop cronbuild 20160124. At your service.
- de.zip build 2016-01-22 14:54 UTC

* Mon Dec 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201512101043-alt1
- repocop cronbuild 20151214. At your service.
- de.zip build 2015-12-10 10:43 UTC

* Mon Dec 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201512070731-alt1
- repocop cronbuild 20151207. At your service.
- de.zip build 2015-12-07 07:31 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511291100-alt1
- repocop cronbuild 20151130. At your service.
- de.zip build 2015-11-29 11:00 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511221221-alt1
- repocop cronbuild 20151123. At your service.
- de.zip build 2015-11-22 12:21 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511151207-alt1
- repocop cronbuild 20151116. At your service.
- de.zip build 2015-11-15 12:07 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511090711-alt1
- repocop cronbuild 20151109. At your service.
- de.zip build 2015-11-09 07:11 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510300835-alt1
- repocop cronbuild 20151102. At your service.
- de.zip build 2015-10-30 08:35 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510230742-alt1
- repocop cronbuild 20151026. At your service.
- de.zip build 2015-10-23 07:42 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510171520-alt1
- repocop cronbuild 20151019. At your service.
- de.zip build 2015-10-17 15:20 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510081515-alt1
- repocop cronbuild 20151012. At your service.
- de.zip build 2015-10-08 15:15 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201509281727-alt1
- repocop cronbuild 20151005. At your service.
- de.zip build 2015-09-28 17:27 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201509240736-alt1
- repocop cronbuild 20150928. At your service.
- de.zip build 2015-09-24 07:36 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201509091700-alt1
- repocop cronbuild 20150914. At your service.
- de.zip build 2015-09-09 17:00 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201509040856-alt1
- repocop cronbuild 20150907. At your service.
- de.zip build 2015-09-04 08:56 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201508301127-alt1
- repocop cronbuild 20150831. At your service.
- de.zip build 2015-08-30 11:27 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201508191441-alt1
- repocop cronbuild 20150823. At your service.
- de.zip build 2015-08-19 14:41 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507281218-alt1
- repocop cronbuild 20150730. At your service.
- de.zip build 2015-07-28 12:18 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507222131-alt1
- repocop cronbuild 20150723. At your service.
- de.zip build 2015-07-22 21:31 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507050809-alt1
- repocop cronbuild 20150709. At your service.
- de.zip build 2015-07-05 08:09 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507020901-alt1
- repocop cronbuild 20150702. At your service.
- de.zip build 2015-07-02 09:01 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201506231521-alt1
- repocop cronbuild 20150625. At your service.
- de.zip build 2015-06-23 15:21 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201506151253-alt1
- repocop cronbuild 20150618. At your service.
- de.zip build 2015-06-15 12:53 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201506091306-alt1
- repocop cronbuild 20150611. At your service.
- de.zip build 2015-06-09 13:06 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201506020708-alt1
- repocop cronbuild 20150604. At your service.
- de.zip build 2015-06-02 07:08 UTC

* Sat May 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505201413-alt1
- repocop cronbuild 20150523. At your service.
- de.zip build 2015-05-20 14:13 UTC

* Sat May 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505130746-alt1
- repocop cronbuild 20150516. At your service.
- de.zip build 2015-05-13 07:46 UTC

* Sat May 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505072040-alt1
- repocop cronbuild 20150509. At your service.
- de.zip build 2015-05-07 20:40 UTC

* Sat May 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201505011203-alt1
- repocop cronbuild 20150502. At your service.
- de.zip build 2015-05-01 12:03 UTC

* Sat Apr 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504241400-alt1
- repocop cronbuild 20150425. At your service.
- de.zip build 2015-04-24 14:00 UTC

* Sat Apr 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504161835-alt1
- repocop cronbuild 20150418. At your service.
- de.zip build 2015-04-16 18:35 UTC

* Sat Apr 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504101131-alt1
- repocop cronbuild 20150411. At your service.
- de.zip build 2015-04-10 11:31 UTC

* Sat Apr 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201503311905-alt1
- repocop cronbuild 20150404. At your service.
- de.zip build 2015-03-31 19:05 UTC

* Sat Mar 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201503130923-alt1
- repocop cronbuild 20150314. At your service.
- de.zip build 2015-03-13 09:23 UTC

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502251955-alt1
- repocop cronbuild 20150228. At your service.
- de.zip build 2015-02-25 19:55 UTC

* Sat Feb 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502091522-alt1
- repocop cronbuild 20150214. At your service.
- de.zip build 2015-02-09 15:22 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502051440-alt1
- repocop cronbuild 20150207. At your service.
- de.zip build 2015-02-05 14:40 UTC

* Sat Jan 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501241236-alt1
- repocop cronbuild 20150131. At your service.
- de.zip build 2015-01-24 12:36 UTC

* Sat Jan 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501200924-alt1
- repocop cronbuild 20150124. At your service.
- de.zip build 2015-01-20 09:24 UTC

* Sat Jan 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501161403-alt1
- repocop cronbuild 20150117. At your service.
- de.zip build 2015-01-16 14:03 UTC

* Sat Jan 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501041046-alt1
- repocop cronbuild 20150110. At your service.
- de.zip build 2015-01-04 10:46 UTC

* Sat Jan 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412281233-alt1
- repocop cronbuild 20150103. At your service.
- de.zip build 2014-12-28 12:33 UTC

* Sat Dec 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412261829-alt1
- repocop cronbuild 20141227. At your service.
- de.zip build 2014-12-26 18:29 UTC

* Sat Dec 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412191457-alt1
- repocop cronbuild 20141220. At your service.
- de.zip build 2014-12-19 14:57 UTC

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412051625-alt1
- repocop cronbuild 20141205. At your service.
- de.zip build 2014-12-05 16:25 UTC

* Sat Nov 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201411190718-alt1
- repocop cronbuild 20141122. At your service.
- de.zip build 2014-11-19 07:18 UTC

* Sat Nov 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201411081456-alt1
- repocop cronbuild 20141115. At your service.
- de.zip build 2014-11-08 14:56 UTC

* Sat Nov 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201411061942-alt1
- repocop cronbuild 20141108. At your service.
- de.zip build 2014-11-06 19:42 UTC

* Sat Oct 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201410221416-alt1
- repocop cronbuild 20141025. At your service.
- de.zip build 2014-10-22 14:16 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201410091021-alt1
- repocop cronbuild 20141011. At your service.
- de.zip build 2014-10-09 10:21 UTC

* Sat Oct 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201409280513-alt1
- repocop cronbuild 20141004. At your service.
- de.zip build 2014-09-28 05:13 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201409230822-alt1
- repocop cronbuild 20140927. At your service.
- de.zip build 2014-09-23 08:22 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201409060720-alt1
- repocop cronbuild 20140913. At your service.
- de.zip build 2014-09-06 07:20 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201407011112-alt1
- repocop cronbuild 20140705. At your service.
- de.zip build 2014-07-01 11:12 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406271437-alt1
- repocop cronbuild 20140628. At your service.
- de.zip build 2014-06-27 14:37 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406201217-alt1
- repocop cronbuild 20140621. At your service.
- de.zip build 2014-06-20 12:17 UTC

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406112128-alt1
- repocop cronbuild 20140613. At your service.
- de.zip build 2014-06-11 21:28 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201406041954-alt1
- repocop cronbuild 20140606. At your service.
- de.zip build 2014-06-04 19:54 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405291555-alt1
- repocop cronbuild 20140530. At your service.
- de.zip build 2014-05-29 15:55 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405221321-alt1
- repocop cronbuild 20140523. At your service.
- de.zip build 2014-05-22 13:21 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405131651-alt1
- repocop cronbuild 20140516. At your service.
- de.zip build 2014-05-13 16:51 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405082304-alt1
- repocop cronbuild 20140509. At your service.
- de.zip build 2014-05-08 23:04 UTC

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201405011608-alt1
- repocop cronbuild 20140502. At your service.
- de.zip build 2014-05-01 16:08 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404241436-alt1
- repocop cronbuild 20140425. At your service.
- de.zip build 2014-04-24 14:36 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404150930-alt1
- repocop cronbuild 20140418. At your service.
- de.zip build 2014-04-15 09:30 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404081341-alt1
- repocop cronbuild 20140411. At your service.
- de.zip build 2014-04-08 13:41 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403301159-alt1
- repocop cronbuild 20140404. At your service.
- de.zip build 2014-03-30 11:59 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403201710-alt1
- repocop cronbuild 20140321. At your service.
- de.zip build 2014-03-20 17:10 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402241437-alt1
- repocop cronbuild 20140228. At your service.
- de.zip build 2014-02-24 14:37 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402181759-alt1
- repocop cronbuild 20140221. At your service.
- de.zip build 2014-02-18 17:59 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402122138-alt1
- repocop cronbuild 20140214. At your service.
- de.zip build 2014-02-12 21:38 UTC

* Fri Jan 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401281643-alt1
- repocop cronbuild 20140131. At your service.
- de.zip build 2014-01-28 16:43 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401210915-alt1
- repocop cronbuild 20140124. At your service.
- de.zip build 2014-01-21 09:15 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401100959-alt1
- repocop cronbuild 20140117. At your service.
- de.zip build 2014-01-10 09:59 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401021333-alt1
- repocop cronbuild 20140103. At your service.
- de.zip build 2014-01-02 13:33 UTC

* Fri Dec 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312260921-alt1
- repocop cronbuild 20131227. At your service.
- de.zip build 2013-12-26 09:21 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312181625-alt1
- repocop cronbuild 20131220. At your service.
- de.zip build 2013-12-18 16:25 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312101022-alt1
- repocop cronbuild 20131213. At your service.
- de.zip build 2013-12-10 10:22 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312011459-alt1
- repocop cronbuild 20131206. At your service.
- de.zip build 2013-12-01 14:59 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311241836-alt1
- repocop cronbuild 20131129. At your service.
- de.zip build 2013-11-24 18:36 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311211403-alt1
- repocop cronbuild 20131122. At your service.
- de.zip build 2013-11-21 14:03 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311142029-alt1
- repocop cronbuild 20131115. At your service.
- de.zip build 2013-11-14 20:29 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311072158-alt1
- repocop cronbuild 20131108. At your service.
- de.zip build 2013-11-07 21:58 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310311901-alt1
- repocop cronbuild 20131101. At your service.
- de.zip build 2013-10-31 19:01 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310170826-alt1
- repocop cronbuild 20131018. At your service.
- de.zip build 2013-10-17 08:26 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310051638-alt1
- repocop cronbuild 20131011. At your service.
- de.zip build 2013-10-05 16:38 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309280835-alt1
- repocop cronbuild 20131004. At your service.
- de.zip build 2013-09-28 08:35 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309241626-alt1
- repocop cronbuild 20130927. At your service.
- de.zip build 2013-09-24 16:26 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309050957-alt1
- repocop cronbuild 20130906. At your service.
- de.zip build 2013-09-05 09:57 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308262029-alt1
- repocop cronbuild 20130830. At your service.
- de.zip build 2013-08-26 20:29 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308231504-alt1
- repocop cronbuild 20130824. At your service.
- de.zip build 2013-08-23 15:04 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308151530-alt1
- repocop cronbuild 20130817. At your service.
- de.zip build 2013-08-15 15:30 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308071246-alt1
- repocop cronbuild 20130810. At your service.
- de.zip build 2013-08-07 12:46 UTC

* Sat Aug 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307301231-alt1
- repocop cronbuild 20130803. At your service.
- de.zip build 2013-07-30 12:31 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307261258-alt1
- repocop cronbuild 20130727. At your service.
- de.zip build 2013-07-26 12:58 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307190654-alt1
- repocop cronbuild 20130720. At your service.
- de.zip build 2013-07-19 06:54 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307121421-alt1
- repocop cronbuild 20130713. At your service.
- de.zip build 2013-07-12 14:21 UTC

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306301624-alt1
- repocop cronbuild 20130706. At your service.
- de.zip build 2013-06-30 16:24 UTC

* Sat Jun 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306191816-alt1
- repocop cronbuild 20130622. At your service.
- de.zip build 2013-06-19 18:16 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306131402-alt1
- repocop cronbuild 20130614. At your service.
- de.zip build 2013-06-13 14:02 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306060511-alt1
- repocop cronbuild 20130607. At your service.
- de.zip build 2013-06-06 05:11 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305300947-alt1
- repocop cronbuild 20130531. At your service.
- de.zip build 2013-05-30 09:47 UTC

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
