# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename de
%define packagversion 2.0.0
%define packagedate 201601291541
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname German
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-de
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
* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601291541-alt1
- repocop cronbuild 20160131. At your service.
- de.zip build 2016-01-29 15:41 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601131452-alt1
- repocop cronbuild 20160124. At your service.
- de.zip build 2016-01-13 14:52 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511221014-alt1
- repocop cronbuild 20151123. At your service.
- de.zip build 2015-11-22 10:14 UTC

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510211914-alt1
- repocop cronbuild 20151026. At your service.
- de.zip build 2015-10-21 19:14 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510171520-alt1
- repocop cronbuild 20151019. At your service.
- de.zip build 2015-10-17 15:20 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509281725-alt1
- repocop cronbuild 20151005. At your service.
- de.zip build 2015-09-28 17:25 UTC

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509240736-alt1
- repocop cronbuild 20150928. At your service.
- de.zip build 2015-09-24 07:36 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509091700-alt1
- repocop cronbuild 20150914. At your service.
- de.zip build 2015-09-09 17:00 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509040856-alt1
- repocop cronbuild 20150907. At your service.
- de.zip build 2015-09-04 08:56 UTC

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508261254-alt1
- repocop cronbuild 20150831. At your service.
- de.zip build 2015-08-26 12:54 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508191441-alt1
- repocop cronbuild 20150823. At your service.
- de.zip build 2015-08-19 14:41 UTC

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507281218-alt1
- repocop cronbuild 20150730. At your service.
- de.zip build 2015-07-28 12:18 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507222131-alt1
- repocop cronbuild 20150723. At your service.
- de.zip build 2015-07-22 21:31 UTC

* Thu Jul 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507022127-alt1
- repocop cronbuild 20150709. At your service.
- de.zip build 2015-07-02 21:27 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507010612-alt1
- repocop cronbuild 20150702. At your service.
- de.zip build 2015-07-01 06:12 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506231521-alt1
- repocop cronbuild 20150625. At your service.
- de.zip build 2015-06-23 15:21 UTC

* Thu Jun 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506151253-alt1
- repocop cronbuild 20150618. At your service.
- de.zip build 2015-06-15 12:53 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506072140-alt1
- repocop cronbuild 20150611. At your service.
- de.zip build 2015-06-07 21:40 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506020708-alt1
- repocop cronbuild 20150604. At your service.
- de.zip build 2015-06-02 07:08 UTC

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505130746-alt1
- repocop cronbuild 20150515. At your service.
- de.zip build 2015-05-13 07:46 UTC

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505061639-alt1
- repocop cronbuild 20150508. At your service.
- de.zip build 2015-05-06 16:39 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504280854-alt1
- repocop cronbuild 20150501. At your service.
- de.zip build 2015-04-28 08:54 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504191329-alt1
- repocop cronbuild 20150424. At your service.
- de.zip build 2015-04-19 13:29 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504161835-alt1
- repocop cronbuild 20150417. At your service.
- de.zip build 2015-04-16 18:35 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504070907-alt1
- repocop cronbuild 20150410. At your service.
- de.zip build 2015-04-07 09:07 UTC

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503130923-alt1
- repocop cronbuild 20150320. At your service.
- de.zip build 2015-03-13 09:23 UTC

* Thu Mar 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503120759-alt1
- repocop cronbuild 20150312. At your service.
- de.zip build 2015-03-12 07:59 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502251955-alt1
- repocop cronbuild 20150227. At your service.
- de.zip build 2015-02-25 19:55 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502031258-alt1
- repocop cronbuild 20150206. At your service.
- de.zip build 2015-02-03 12:58 UTC

* Thu Jan 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501241236-alt1
- repocop cronbuild 20150129. At your service.
- de.zip build 2015-01-24 12:36 UTC

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501150829-alt1
- repocop cronbuild 20150116. At your service.
- de.zip build 2015-01-15 08:29 UTC

* Thu Jan 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501041046-alt1
- repocop cronbuild 20150108. At your service.
- de.zip build 2015-01-04 10:46 UTC

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412281233-alt1
- repocop cronbuild 20150102. At your service.
- de.zip build 2014-12-28 12:33 UTC

* Fri Dec 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412251449-alt1
- repocop cronbuild 20141226. At your service.
- de.zip build 2014-12-25 14:49 UTC

* Thu Dec 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412141527-alt1
- repocop cronbuild 20141218. At your service.
- de.zip build 2014-12-14 15:27 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412051625-alt1
- repocop cronbuild 20141211. At your service.
- de.zip build 2014-12-05 16:25 UTC

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412011332-alt1
- repocop cronbuild 20141205. At your service.
- de.zip build 2014-12-01 13:32 UTC

* Thu Nov 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411190718-alt1
- repocop cronbuild 20141120. At your service.
- de.zip build 2014-11-19 07:18 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411081456-alt1
- repocop cronbuild 20141114. At your service.
- de.zip build 2014-11-08 14:56 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411061942-alt1
- repocop cronbuild 20141107. At your service.
- de.zip build 2014-11-06 19:42 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410091021-alt1
- repocop cronbuild 20141010. At your service.
- de.zip build 2014-10-09 10:21 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409280509-alt1
- repocop cronbuild 20141003. At your service.
- de.zip build 2014-09-28 05:09 UTC

* Thu Sep 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409230822-alt1
- repocop cronbuild 20140925. At your service.
- de.zip build 2014-09-23 08:22 UTC

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409060720-alt1
- repocop cronbuild 20140911. At your service.
- de.zip build 2014-09-06 07:20 UTC

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406271437-alt1
- repocop cronbuild 20140628. At your service.
- de.zip build 2014-06-27 14:37 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406201217-alt1
- repocop cronbuild 20140621. At your service.
- de.zip build 2014-06-20 12:17 UTC

* Thu Jun 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406111245-alt1
- repocop cronbuild 20140612. At your service.
- de.zip build 2014-06-11 12:45 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406031246-alt1
- repocop cronbuild 20140606. At your service.
- de.zip build 2014-06-03 12:46 UTC

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405291542-alt1
- repocop cronbuild 20140530. At your service.
- de.zip build 2014-05-29 15:42 UTC

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405221321-alt1
- repocop cronbuild 20140523. At your service.
- de.zip build 2014-05-22 13:21 UTC

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405131651-alt1
- repocop cronbuild 20140516. At your service.
- de.zip build 2014-05-13 16:51 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405081820-alt1
- repocop cronbuild 20140509. At your service.
- de.zip build 2014-05-08 18:20 UTC

* Thu May 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405010834-alt1
- repocop cronbuild 20140501. At your service.
- de.zip build 2014-05-01 08:34 UTC

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404241436-alt1
- repocop cronbuild 20140425. At your service.
- de.zip build 2014-04-24 14:36 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404071302-alt1
- repocop cronbuild 20140411. At your service.
- de.zip build 2014-04-07 13:02 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403301156-alt1
- repocop cronbuild 20140404. At your service.
- de.zip build 2014-03-30 11:56 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403201710-alt1
- repocop cronbuild 20140321. At your service.
- de.zip build 2014-03-20 17:10 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402122138-alt1
- repocop cronbuild 20140214. At your service.
- de.zip build 2014-02-12 21:38 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312181625-alt1
- repocop cronbuild 20131220. At your service.
- de.zip build 2013-12-18 16:25 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312101022-alt1
- repocop cronbuild 20131213. At your service.
- de.zip build 2013-12-10 10:22 UTC

* Thu Dec 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312011459-alt1
- repocop cronbuild 20131205. At your service.
- de.zip build 2013-12-01 14:59 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311261620-alt1
- repocop cronbuild 20131129. At your service.
- de.zip build 2013-11-26 16:20 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311151533-alt1
- repocop cronbuild 20131122. At your service.
- de.zip build 2013-11-15 15:33 UTC

* Thu Nov 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311141515-alt1
- repocop cronbuild 20131114. At your service.
- de.zip build 2013-11-14 15:15 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311061358-alt1
- repocop cronbuild 20131108. At your service.
- de.zip build 2013-11-06 13:58 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310311901-alt1
- repocop cronbuild 20131101. At your service.
- de.zip build 2013-10-31 19:01 UTC

* Thu Oct 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310170826-alt1
- repocop cronbuild 20131017. At your service.
- de.zip build 2013-10-17 08:26 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310051638-alt1
- repocop cronbuild 20131011. At your service.
- de.zip build 2013-10-05 16:38 UTC

* Thu Oct 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309271221-alt1
- repocop cronbuild 20131003. At your service.
- de.zip build 2013-09-27 12:21 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309241626-alt1
- repocop cronbuild 20130927. At your service.
- de.zip build 2013-09-24 16:26 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309031005-alt1
- repocop cronbuild 20130906. At your service.
- de.zip build 2013-09-03 10:05 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308262029-alt1
- repocop cronbuild 20130830. At your service.
- de.zip build 2013-08-26 20:29 UTC

* Thu Aug 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308201411-alt1
- repocop cronbuild 20130822. At your service.
- de.zip build 2013-08-20 14:11 UTC

* Fri Aug 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308101212-alt1
- repocop cronbuild 20130816. At your service.
- de.zip build 2013-08-10 12:12 UTC

* Fri Aug 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308071246-alt1
- repocop cronbuild 20130809. At your service.
- de.zip build 2013-08-07 12:46 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307301231-alt1
- repocop cronbuild 20130802. At your service.
- de.zip build 2013-07-30 12:31 UTC

* Fri Jul 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307251706-alt1
- repocop cronbuild 20130726. At your service.
- de.zip build 2013-07-25 17:06 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307150800-alt1
- repocop cronbuild 20130719. At your service.
- de.zip build 2013-07-15 08:00 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306301624-alt1
- repocop cronbuild 20130705. At your service.
- de.zip build 2013-06-30 16:24 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306191816-alt1
- repocop cronbuild 20130621. At your service.
- de.zip build 2013-06-19 18:16 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306130851-alt1
- repocop cronbuild 20130614. At your service.
- de.zip build 2013-06-13 08:51 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306040946-alt1
- repocop cronbuild 20130607. At your service.
- de.zip build 2013-06-04 09:46 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305300941-alt1
- repocop cronbuild 20130531. At your service.
- de.zip build 2013-05-30 09:41 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305231534-alt1
- repocop cronbuild 20130524. At your service.
- de.zip build 2013-05-23 15:34 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305131323-alt1
- repocop cronbuild 20130517. At your service.
- de.zip build 2013-05-13 13:23 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305041814-alt1
- repocop cronbuild 20130509. At your service.
- de.zip build 2013-05-04 18:14 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304131040-alt1
- repocop cronbuild 20130417. At your service.
- de.zip build 2013-04-13 10:40 UTC

* Tue Apr 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304081100-alt1
- repocop cronbuild 20130409. At your service.
- de.zip build 2013-04-08 11:00 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304021934-alt1
- repocop cronbuild 20130403. At your service.
- de.zip build 2013-04-02 19:34 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303261937-alt1
- repocop cronbuild 20130327. At your service.
- de.zip build 2013-03-26 19:37 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303150711-alt1
- repocop cronbuild 20130319. At your service.
- de.zip build 2013-03-15 07:11 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303120840-alt1
- repocop cronbuild 20130313. At your service.
- de.zip build 2013-03-12 08:40 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302251122-alt1
- repocop cronbuild 20130304. At your service.
- de.zip build 2013-02-25 11:22 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302221755-alt1
- repocop cronbuild 20130225. At your service.
- de.zip build 2013-02-22 17:55 UTC

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302131009-alt1
- repocop cronbuild 20130218. At your service.
- de.zip build 2013-02-13 10:09 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301261054-alt1
- repocop cronbuild 20130128. At your service.
- de.zip build 2013-01-26 10:54 UTC

* Sun Jan 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301201254-alt1
- repocop cronbuild 20130120. At your service.
- de.zip build 2013-01-20 12:54 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301101111-alt1
- repocop cronbuild 20130114. At your service.
- de.zip build 2013-01-10 11:11 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212221454-alt1
- repocop cronbuild 20121224. At your service.
- de.zip build 2012-12-22 14:54 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211251702-alt1
- repocop cronbuild 20121126. At your service.
- de.zip build 2012-11-25 17:02 UTC

* Sun Nov 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211181000-alt1
- repocop cronbuild 20121118. At your service.
- de.zip build 2012-11-18 10:00 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211111644-alt1
- repocop cronbuild 20121112. At your service.
- de.zip build 2012-11-11 16:44 UTC

* Sun Nov 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211021541-alt1
- repocop cronbuild 20121104. At your service.
- de.zip build 2012-11-02 15:41 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210281116-alt1
- repocop cronbuild 20121029. At your service.
- de.zip build 2012-10-28 11:16 UTC

* Sun Oct 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210211721-alt1
- repocop cronbuild 20121021. At your service.
- de.zip build 2012-10-21 17:21 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210101233-alt1
- repocop cronbuild 20121015. At your service.
- de.zip build 2012-10-10 12:33 UTC

* Sun Oct 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210071600-alt1
- repocop cronbuild 20121007. At your service.
- de.zip build 2012-10-07 16:00 UTC

* Sun Sep 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209280635-alt1
- repocop cronbuild 20120930. At your service.
- de.zip build 2012-09-28 06:35 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209112155-alt1
- repocop cronbuild 20120917. At your service.
- de.zip build 2012-09-11 21:55 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209090651-alt1
- repocop cronbuild 20120910. At your service.
- de.zip build 2012-09-09 06:51 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208311647-alt1
- repocop cronbuild 20120904. At your service.
- de.zip build 2012-08-31 16:47 UTC

* Mon Aug 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208211202-alt1
- repocop cronbuild 20120827. At your service.
- de.zip build 2012-08-21 12:02 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208191759-alt1
- repocop cronbuild 20120820. At your service.
- de.zip build 2012-08-19 17:59 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208101908-alt1
- repocop cronbuild 20120814. At your service.
- de.zip build 2012-08-10 19:08 UTC

* Mon Aug 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208060813-alt1
- repocop cronbuild 20120806. At your service.
- de.zip build 2012-08-06 08:13 UTC

* Mon Jul 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207241613-alt1
- repocop cronbuild 20120730. At your service.
- de.zip build 2012-07-24 16:13 UTC

* Mon Jul 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207231124-alt1
- repocop cronbuild 20120723. At your service.
- de.zip build 2012-07-23 11:24 UTC

* Mon Jul 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207121522-alt1
- repocop cronbuild 20120716. At your service.
- de.zip build 2012-07-12 15:22 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207091555-alt1
- repocop cronbuild 20120709. At your service.
- de.zip build 2012-07-09 15:55 UTC

* Mon Jul 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206291744-alt1
- repocop cronbuild 20120702. At your service.
- de.zip build 2012-06-29 17:44 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206221811-alt1
- repocop cronbuild 20120625. At your service.
- de.zip build 2012-06-22 18:11 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206181719-alt1
- repocop cronbuild 20120618. At your service.
- de.zip build 2012-06-18 17:19 UTC

* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206080855-alt1
- repocop cronbuild 20120611. At your service.
- de.zip build 2012-06-08 08:55 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206041513-alt1
- repocop cronbuild 20120604. At your service.
- de.zip build 2012-06-04 15:13 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205280958-alt1
- repocop cronbuild 20120528. At your service.
- de.zip build 2012-05-28 09:58 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205201530-alt1
- repocop cronbuild 20120521. At your service.
- de.zip build 2012-05-20 15:30 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205101019-alt1
- repocop cronbuild 20120514. At your service.
- de.zip build 2012-05-10 10:19 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205072118-alt1
- repocop cronbuild 20120507. At your service.
- de.zip build 2012-05-07 21:18 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204280854-alt1
- repocop cronbuild 20120430. At your service.
- de.zip build 2012-04-28 08:54 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204161517-alt1
- repocop cronbuild 20120416. At your service.
- de.zip build 2012-04-16 15:17 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204021424-alt1
- repocop cronbuild 20120402. At your service.
- de.zip build 2012-04-02 14:24 UTC

* Mon Mar 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203220904-alt1
- repocop cronbuild 20120326. At your service.
- de.zip build 2012-03-22 09:04 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203181916-alt1
- repocop cronbuild 20120319. At your service.
- de.zip build 2012-03-18 19:16 UTC

* Thu Mar 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203041741-alt1
- repocop cronbuild 20120308. At your service.
- de.zip build 2012-03-04 17:41 UTC

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202261402-alt1
- repocop cronbuild 20120301. At your service.
- de.zip build 2012-02-26 14:02 UTC

* Thu Feb 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202201600-alt1
- repocop cronbuild 20120223. At your service.
- de.zip build 2012-02-20 16:00 UTC

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202161914-alt1
- repocop cronbuild 20120216. At your service.
- de.zip build 2012-02-16 19:14 UTC

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202091212-alt1
- repocop cronbuild 20120209. At your service.
- de.zip build 2012-02-09 12:12 UTC

* Thu Feb 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201291051-alt1
- repocop cronbuild 20120202. At your service.
- de.zip build 2012-01-29 10:51 UTC

* Thu Jan 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201261658-alt1
- repocop cronbuild 20120126. At your service.
- de.zip build 2012-01-26 16:58 UTC

* Thu Jan 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201180523-alt1
- repocop cronbuild 20120119. At your service.
- de.zip build 2012-01-18 05:23 UTC

* Thu Jan 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201101616-alt1
- repocop cronbuild 20120112. At your service.
- de.zip build 2012-01-10 16:16 UTC

* Thu Jan 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201052107-alt1
- repocop cronbuild 20120105. At your service.
- de.zip build 2012-01-05 21:07 UTC

* Thu Dec 29 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112291253-alt1
- repocop cronbuild 20111229. At your service.
- de.zip build 2011-12-29 12:53 UTC

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112171028-alt1
- repocop cronbuild 20111222. At your service.
- de.zip build 2011-12-17 10:28 UTC

* Thu Dec 15 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112151057-alt1
- repocop cronbuild 20111215. At your service.
- de.zip build 2011-12-15 10:57 UTC

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
