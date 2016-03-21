# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename nl
%define packagversion 2.4.0
%define packagedate 201603150841
%define moodlebranch 2.4
%define moodlepackagename %moodle_name%moodlebranch
%define langname Dutch
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.4-lang-nl
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
* Mon Mar 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201603150841-alt1
- repocop cronbuild 20160321. At your service.
- nl.zip build 2016-03-15 08:41 UTC

* Sun Mar 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201602291035-alt1
- repocop cronbuild 20160306. At your service.
- nl.zip build 2016-02-29 10:35 UTC

* Mon Feb 29 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201602281836-alt1
- repocop cronbuild 20160229. At your service.
- nl.zip build 2016-02-28 18:36 UTC

* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201602171652-alt1
- repocop cronbuild 20160221. At your service.
- nl.zip build 2016-02-17 16:52 UTC

* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201602081335-alt1
- repocop cronbuild 20160214. At your service.
- nl.zip build 2016-02-08 13:35 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201601281313-alt1
- repocop cronbuild 20160131. At your service.
- nl.zip build 2016-01-28 13:13 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201512301736-alt1
- repocop cronbuild 20160124. At your service.
- nl.zip build 2015-12-30 17:36 UTC

* Tue Nov 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511061701-alt1
- repocop cronbuild 20151110. At your service.
- nl.zip build 2015-11-06 17:01 UTC

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201511011129-alt1
- repocop cronbuild 20151102. At your service.
- nl.zip build 2015-11-01 11:29 UTC

* Mon Oct 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201510151445-alt1
- repocop cronbuild 20151019. At your service.
- nl.zip build 2015-10-15 14:45 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201509041315-alt1
- repocop cronbuild 20150907. At your service.
- nl.zip build 2015-09-04 13:15 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201508112027-alt1
- repocop cronbuild 20150823. At your service.
- nl.zip build 2015-08-11 20:27 UTC

* Thu Jul 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507211128-alt1
- repocop cronbuild 20150723. At your service.
- nl.zip build 2015-07-21 11:28 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201507120655-alt1
- repocop cronbuild 20150716. At your service.
- nl.zip build 2015-07-12 06:55 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201506081153-alt1
- repocop cronbuild 20150611. At your service.
- nl.zip build 2015-06-08 11:53 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201506041227-alt1
- repocop cronbuild 20150604. At your service.
- nl.zip build 2015-06-04 12:27 UTC

* Sun Apr 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201504071652-alt1
- repocop cronbuild 20150412. At your service.
- nl.zip build 2015-04-07 16:52 UTC

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502230816-alt1
- repocop cronbuild 20150228. At your service.
- nl.zip build 2015-02-23 08:16 UTC

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201502041930-alt1
- repocop cronbuild 20150207. At your service.
- nl.zip build 2015-02-04 19:30 UTC

* Sun Feb 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201501261454-alt1
- repocop cronbuild 20150201. At your service.
- nl.zip build 2015-01-26 14:54 UTC

* Sun Jan 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412301436-alt1
- repocop cronbuild 20150104. At your service.
- nl.zip build 2014-12-30 14:36 UTC

* Sat Dec 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201412051655-alt1
- repocop cronbuild 20141206. At your service.
- nl.zip build 2014-12-05 16:55 UTC

* Sat Nov 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201411011103-alt1
- repocop cronbuild 20141108. At your service.
- nl.zip build 2014-11-01 11:03 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201408212036-alt1
- repocop cronbuild 20140913. At your service.
- nl.zip build 2014-08-21 20:36 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201407011319-alt1
- repocop cronbuild 20140705. At your service.
- nl.zip build 2014-07-01 13:19 UTC

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201404161026-alt1
- repocop cronbuild 20140418. At your service.
- nl.zip build 2014-04-16 10:26 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403311923-alt1
- repocop cronbuild 20140404. At your service.
- nl.zip build 2014-03-31 19:23 UTC

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403230838-alt1
- repocop cronbuild 20140328. At your service.
- nl.zip build 2014-03-23 08:38 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201403190745-alt1
- repocop cronbuild 20140321. At your service.
- nl.zip build 2014-03-19 07:45 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402272109-alt1
- repocop cronbuild 20140228. At your service.
- nl.zip build 2014-02-27 21:09 UTC

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402120753-alt1
- repocop cronbuild 20140221. At your service.
- nl.zip build 2014-02-12 07:53 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201402012050-alt1
- repocop cronbuild 20140207. At your service.
- nl.zip build 2014-02-01 20:50 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401210941-alt1
- repocop cronbuild 20140124. At your service.
- nl.zip build 2014-01-21 09:41 UTC

* Fri Jan 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201401052013-alt1
- repocop cronbuild 20140110. At your service.
- nl.zip build 2014-01-05 20:13 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312301424-alt1
- repocop cronbuild 20140103. At your service.
- nl.zip build 2013-12-30 14:24 UTC

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312160827-alt1
- repocop cronbuild 20131220. At your service.
- nl.zip build 2013-12-16 08:27 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312111848-alt1
- repocop cronbuild 20131213. At your service.
- nl.zip build 2013-12-11 18:48 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312041417-alt1
- repocop cronbuild 20131206. At your service.
- nl.zip build 2013-12-04 14:17 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311082123-alt1
- repocop cronbuild 20131115. At your service.
- nl.zip build 2013-11-08 21:23 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310281324-alt1
- repocop cronbuild 20131101. At your service.
- nl.zip build 2013-10-28 13:24 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310231913-alt1
- repocop cronbuild 20131025. At your service.
- nl.zip build 2013-10-23 19:13 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310091758-alt1
- repocop cronbuild 20131011. At your service.
- nl.zip build 2013-10-09 17:58 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310031430-alt1
- repocop cronbuild 20131004. At your service.
- nl.zip build 2013-10-03 14:30 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309110656-alt1
- repocop cronbuild 20130913. At your service.
- nl.zip build 2013-09-11 06:56 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309011622-alt1
- repocop cronbuild 20130906. At your service.
- nl.zip build 2013-09-01 16:22 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308280610-alt1
- repocop cronbuild 20130830. At your service.
- nl.zip build 2013-08-28 06:10 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308182247-alt1
- repocop cronbuild 20130824. At your service.
- nl.zip build 2013-08-18 22:47 UTC

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308061215-alt1
- repocop cronbuild 20130810. At your service.
- nl.zip build 2013-08-06 12:15 UTC

* Fri Jul 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307251219-alt1
- repocop cronbuild 20130726. At your service.
- nl.zip build 2013-07-25 12:19 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306192137-alt1
- repocop cronbuild 20130621. At your service.
- nl.zip build 2013-06-19 21:37 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306131350-alt1
- repocop cronbuild 20130614. At your service.
- nl.zip build 2013-06-13 13:50 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306060511-alt1
- repocop cronbuild 20130607. At your service.
- nl.zip build 2013-06-06 05:11 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305291516-alt1
- repocop cronbuild 20130531. At your service.
- nl.zip build 2013-05-29 15:16 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305221539-alt1
- repocop cronbuild 20130524. At your service.
- nl.zip build 2013-05-22 15:39 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305151953-alt1
- repocop cronbuild 20130517. At your service.
- nl.zip build 2013-05-15 19:53 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305081356-alt1
- repocop cronbuild 20130509. At your service.
- nl.zip build 2013-05-08 13:56 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304141811-alt1
- Rename package to moodle2.4-lang-nl
- nl.zip build 2013-04-14 18:11 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201304141811-alt1
- repocop cronbuild 20130417. At your service.
- nl.zip build 2013-04-14 18:11 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303172012-alt1
- repocop cronbuild 20130320. At your service.
- nl.zip build 2013-03-17 20:12 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302221108-alt1
- repocop cronbuild 20130225. At your service.
- nl.zip build 2013-02-22 11:08 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- nl.zip build 2013-01-26 15:39 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301132028-alt1
- repocop cronbuild 20130114. At your service.
- nl.zip build 2013-01-13 20:28 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301041825-alt1
- repocop cronbuild 20130107. At your service.
- nl.zip build 2013-01-04 18:25 UTC

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212292201-alt1
- repocop cronbuild 20121231. At your service.
- nl.zip build 2012-12-29 22:01 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212170759-alt1
- repocop cronbuild 20121224. At your service.
- nl.zip build 2012-12-17 07:59 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211281359-alt1
- repocop cronbuild 20121203. At your service.
- nl.zip build 2012-11-28 13:59 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211011708-alt1
- repocop cronbuild 20121105. At your service.
- nl.zip build 2012-11-01 17:08 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210211823-alt1
- repocop cronbuild 20121022. At your service.
- nl.zip build 2012-10-21 18:23 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210072108-alt1
- repocop cronbuild 20121008. At your service.
- nl.zip build 2012-10-07 21:08 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209272035-alt1
- repocop cronbuild 20121001. At your service.
- nl.zip build 2012-09-27 20:35 UTC

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209180804-alt1
- repocop cronbuild 20120918. At your service.
- nl.zip build 2012-09-18 08:04 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209080701-alt1
- repocop cronbuild 20120911. At your service.
- nl.zip build 2012-09-08 07:01 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209022011-alt1
- repocop cronbuild 20120904. At your service.
- nl.zip build 2012-09-02 20:11 UTC

* Wed Aug 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208281842-alt1
- repocop cronbuild 20120829. At your service.
- nl.zip build 2012-08-28 18:42 UTC

* Tue Aug 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208181548-alt1
- repocop cronbuild 20120821. At your service.
- nl.zip build 2012-08-18 15:48 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208130831-alt1
- repocop cronbuild 20120814. At your service.
- nl.zip build 2012-08-13 08:31 UTC

* Wed Aug 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208061142-alt1
- repocop cronbuild 20120808. At your service.
- nl.zip build 2012-08-06 11:42 UTC

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207310935-alt1
- repocop cronbuild 20120731. At your service.
- nl.zip build 2012-07-31 09:35 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207241221-alt1
- repocop cronbuild 20120724. At your service.
- nl.zip build 2012-07-24 12:21 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207100841-alt1
- repocop cronbuild 20120710. At your service.
- nl.zip build 2012-07-10 08:41 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206282216-alt1
- repocop cronbuild 20120703. At your service.
- nl.zip build 2012-06-28 22:16 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206232109-alt1
- repocop cronbuild 20120626. At your service.
- nl.zip build 2012-06-23 21:09 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191609-alt1
- repocop cronbuild 20120619. At your service.
- nl.zip build 2012-06-19 16:09 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206101946-alt1
- repocop cronbuild 20120612. At your service.
- nl.zip build 2012-06-10 19:46 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206031341-alt1
- repocop cronbuild 20120605. At your service.
- nl.zip build 2012-06-03 13:41 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231817-alt1
- repocop cronbuild 20120529. At your service.
- nl.zip build 2012-05-23 18:17 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205202015-alt1
- repocop cronbuild 20120522. At your service.
- nl.zip build 2012-05-20 20:15 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- nl.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205062035-alt1
- repocop cronbuild 20120508. At your service.
- nl.zip build 2012-05-06 20:35 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- nl.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204241002-alt1
- repocop cronbuild 20120424. At your service.
- nl.zip build 2012-04-24 10:02 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204162047-alt1
- repocop cronbuild 20120417. At your service.
- nl.zip build 2012-04-16 20:47 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204101400-alt1
- repocop cronbuild 20120410. At your service.
- nl.zip build 2012-04-10 14:00 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204031417-alt1
- repocop cronbuild 20120403. At your service.
- nl.zip build 2012-04-03 14:17 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203140944-alt1
- Rename package to moodle2.2-lang-nl
- nl.zip build 2012-03-14 09:44 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203140945-alt1
- repocop cronbuild 20120320. At your service.
- nl.zip build 2012-03-14 09:45 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203071928-alt1
- repocop cronbuild 20120307. At your service.
- nl.zip build 2012-03-07 19:28 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202041537-alt1
- repocop cronbuild 20120208. At your service.
- nl.zip build 2012-02-04 15:37 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201250830-alt1
- repocop cronbuild 20120125. At your service.
- nl.zip build 2012-01-25 08:30 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201092126-alt1
- repocop cronbuild 20120111. At your service.
- nl.zip build 2012-01-09 21:26 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111214. At your service.
- nl.zip build 2011-12-09 16:00 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112020845-alt1
- repocop cronbuild 20111207. At your service.
- nl.zip build 2011-12-02 08:45 UTC

* Thu Dec 01 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111292023-alt1
- repocop cronbuild 20111201. At your service.
- nl.zip build 2011-11-29 20:23 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111161404-alt1
- Rename package to moodle2.1-lang-nl
- nl.zip build 2011-11-16 14:04

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
