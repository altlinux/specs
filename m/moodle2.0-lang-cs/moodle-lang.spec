# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename cs
%define packagversion 2.0.0
%define packagedate 201602291437
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Czech
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-cs
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
* Sun Mar 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602291437-alt1
- repocop cronbuild 20160306. At your service.
- cs.zip build 2016-02-29 14:37 UTC

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601251015-alt1
- repocop cronbuild 20160131. At your service.
- cs.zip build 2016-01-25 10:15 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601180748-alt1
- repocop cronbuild 20160124. At your service.
- cs.zip build 2016-01-18 07:48 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511251430-alt1
- repocop cronbuild 20151130. At your service.
- cs.zip build 2015-11-25 14:30 UTC

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511181032-alt1
- repocop cronbuild 20151123. At your service.
- cs.zip build 2015-11-18 10:32 UTC

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511111250-alt1
- repocop cronbuild 20151116. At your service.
- cs.zip build 2015-11-11 12:50 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511041404-alt1
- repocop cronbuild 20151109. At your service.
- cs.zip build 2015-11-04 14:04 UTC

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510051035-alt1
- repocop cronbuild 20151012. At your service.
- cs.zip build 2015-10-05 10:35 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508181236-alt1
- repocop cronbuild 20150823. At your service.
- cs.zip build 2015-08-18 12:36 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506080750-alt1
- repocop cronbuild 20150611. At your service.
- cs.zip build 2015-06-08 07:50 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504200835-alt1
- repocop cronbuild 20150424. At your service.
- cs.zip build 2015-04-20 08:35 UTC

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503242214-alt1
- repocop cronbuild 20150327. At your service.
- cs.zip build 2015-03-24 22:14 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502242055-alt1
- repocop cronbuild 20150227. At your service.
- cs.zip build 2015-02-24 20:55 UTC

* Thu Feb 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502162102-alt1
- repocop cronbuild 20150219. At your service.
- cs.zip build 2015-02-16 21:02 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412102351-alt1
- repocop cronbuild 20141211. At your service.
- cs.zip build 2014-12-10 23:51 UTC

* Thu Nov 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411251401-alt1
- repocop cronbuild 20141127. At your service.
- cs.zip build 2014-11-25 14:01 UTC

* Thu Nov 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411162054-alt1
- repocop cronbuild 20141120. At your service.
- cs.zip build 2014-11-16 20:54 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410070801-alt1
- repocop cronbuild 20141010. At your service.
- cs.zip build 2014-10-07 08:01 UTC

* Thu Sep 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409240718-alt1
- repocop cronbuild 20140925. At your service.
- cs.zip build 2014-09-24 07:18 UTC

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201408290655-alt1
- repocop cronbuild 20140911. At your service.
- cs.zip build 2014-08-29 06:55 UTC

* Fri Jul 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406300738-alt1
- repocop cronbuild 20140704. At your service.
- cs.zip build 2014-06-30 07:38 UTC

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406031239-alt1
- repocop cronbuild 20140606. At your service.
- cs.zip build 2014-06-03 12:39 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403141904-alt1
- repocop cronbuild 20140321. At your service.
- cs.zip build 2014-03-14 19:04 UTC

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403041011-alt1
- repocop cronbuild 20140307. At your service.
- cs.zip build 2014-03-04 10:11 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402271512-alt1
- repocop cronbuild 20140228. At your service.
- cs.zip build 2014-02-27 15:12 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402130841-alt1
- repocop cronbuild 20140214. At your service.
- cs.zip build 2014-02-13 08:41 UTC

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402031440-alt1
- repocop cronbuild 20140207. At your service.
- cs.zip build 2014-02-03 14:40 UTC

* Thu Dec 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312030116-alt1
- repocop cronbuild 20131205. At your service.
- cs.zip build 2013-12-03 01:16 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311271051-alt1
- repocop cronbuild 20131129. At your service.
- cs.zip build 2013-11-27 10:51 UTC

* Thu Oct 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309272107-alt1
- repocop cronbuild 20131003. At your service.
- cs.zip build 2013-09-27 21:07 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309230914-alt1
- repocop cronbuild 20130927. At your service.
- cs.zip build 2013-09-23 09:14 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309031914-alt1
- repocop cronbuild 20130906. At your service.
- cs.zip build 2013-09-03 19:14 UTC

* Fri Aug 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307311937-alt1
- repocop cronbuild 20130802. At your service.
- cs.zip build 2013-07-31 19:37 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307030731-alt1
- repocop cronbuild 20130705. At your service.
- cs.zip build 2013-07-03 07:31 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306141035-alt1
- repocop cronbuild 20130621. At your service.
- cs.zip build 2013-06-14 10:35 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306040851-alt1
- repocop cronbuild 20130607. At your service.
- cs.zip build 2013-06-04 08:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305211151-alt1
- repocop cronbuild 20130524. At your service.
- cs.zip build 2013-05-21 11:51 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305071459-alt1
- repocop cronbuild 20130509. At your service.
- cs.zip build 2013-05-07 14:59 UTC

* Tue Apr 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304091439-alt1
- repocop cronbuild 20130409. At your service.
- cs.zip build 2013-04-09 14:39 UTC

* Wed Apr 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304020840-alt1
- repocop cronbuild 20130403. At your service.
- cs.zip build 2013-04-02 08:40 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303250744-alt1
- repocop cronbuild 20130327. At your service.
- cs.zip build 2013-03-25 07:44 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303110810-alt1
- repocop cronbuild 20130313. At your service.
- cs.zip build 2013-03-11 08:10 UTC

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301280856-alt1
- repocop cronbuild 20130129. At your service.
- cs.zip build 2013-01-28 08:56 UTC

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301200832-alt1
- repocop cronbuild 20130121. At your service.
- cs.zip build 2013-01-20 08:32 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211200206-alt1
- repocop cronbuild 20121126. At your service.
- cs.zip build 2012-11-20 02:06 UTC

* Sun Nov 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210301355-alt1
- repocop cronbuild 20121104. At your service.
- cs.zip build 2012-10-30 13:55 UTC

* Sun Oct 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210080743-alt1
- repocop cronbuild 20121014. At your service.
- cs.zip build 2012-10-08 07:43 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209170751-alt1
- repocop cronbuild 20120917. At your service.
- cs.zip build 2012-09-17 07:51 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209101551-alt1
- repocop cronbuild 20120910. At your service.
- cs.zip build 2012-09-10 15:51 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208290930-alt1
- repocop cronbuild 20120904. At your service.
- cs.zip build 2012-08-29 09:30 UTC

* Mon Aug 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208030940-alt1
- repocop cronbuild 20120806. At your service.
- cs.zip build 2012-08-03 09:40 UTC

* Mon Jul 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207271624-alt1
- repocop cronbuild 20120730. At your service.
- cs.zip build 2012-07-27 16:24 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207091351-alt1
- repocop cronbuild 20120709. At your service.
- cs.zip build 2012-07-09 13:51 UTC

* Mon Jul 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207021542-alt1
- repocop cronbuild 20120702. At your service.
- cs.zip build 2012-07-02 15:42 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205281310-alt1
- repocop cronbuild 20120528. At your service.
- cs.zip build 2012-05-28 13:10 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205071107-alt1
- repocop cronbuild 20120507. At your service.
- cs.zip build 2012-05-07 11:07 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203161034-alt1
- repocop cronbuild 20120319. At your service.
- cs.zip build 2012-03-16 10:34 UTC

* Mon Mar 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203011549-alt1
- repocop cronbuild 20120305. At your service.
- cs.zip build 2012-03-01 15:49 UTC

* Mon Feb 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201311044-alt1
- repocop cronbuild 20120206. At your service.
- cs.zip build 2012-01-31 10:44 UTC

* Mon Jan 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201301125-alt1
- repocop cronbuild 20120130. At your service.
- cs.zip build 2012-01-30 11:25 UTC

* Mon Dec 26 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112230839-alt1
- repocop cronbuild 20111226. At your service.
- cs.zip build 2011-12-23 08:39 UTC

* Mon Dec 19 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112131059-alt1
- repocop cronbuild 20111219. At your service.
- cs.zip build 2011-12-13 10:59 UTC

* Mon Dec 12 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112080945-alt1
- repocop cronbuild 20111212. At your service.
- cs.zip build 2011-12-08 09:45 UTC

* Mon Dec 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112051734-alt1
- repocop cronbuild 20111205. At your service.
- cs.zip build 2011-12-05 17:34 UTC

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
