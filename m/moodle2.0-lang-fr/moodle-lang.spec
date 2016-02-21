# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename fr
%define packagversion 2.0.0
%define packagedate 201602161726
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname French
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-fr
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
* Sun Feb 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602161726-alt1
- repocop cronbuild 20160221. At your service.
- fr.zip build 2016-02-16 17:26 UTC

* Sun Feb 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602041935-alt1
- repocop cronbuild 20160207. At your service.
- fr.zip build 2016-02-04 19:35 UTC

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601182012-alt1
- repocop cronbuild 20160124. At your service.
- fr.zip build 2016-01-18 20:12 UTC

* Tue Dec 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512141542-alt1
- repocop cronbuild 20151215. At your service.
- fr.zip build 2015-12-14 15:42 UTC

* Tue Dec 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201512031037-alt1
- repocop cronbuild 20151208. At your service.
- fr.zip build 2015-12-03 10:37 UTC

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511251513-alt1
- repocop cronbuild 20151130. At your service.
- fr.zip build 2015-11-25 15:13 UTC

* Tue Nov 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511201517-alt1
- repocop cronbuild 20151124. At your service.
- fr.zip build 2015-11-20 15:17 UTC

* Tue Nov 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511082220-alt1
- repocop cronbuild 20151110. At your service.
- fr.zip build 2015-11-08 22:20 UTC

* Tue Nov 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511011427-alt1
- repocop cronbuild 20151103. At your service.
- fr.zip build 2015-11-01 14:27 UTC

* Tue Oct 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510131701-alt1
- repocop cronbuild 20151020. At your service.
- fr.zip build 2015-10-13 17:01 UTC

* Tue Oct 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510081655-alt1
- repocop cronbuild 20151013. At your service.
- fr.zip build 2015-10-08 16:55 UTC

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510031810-alt1
- repocop cronbuild 20151005. At your service.
- fr.zip build 2015-10-03 18:10 UTC

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509101856-alt1
- repocop cronbuild 20150914. At your service.
- fr.zip build 2015-09-10 18:56 UTC

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201509011122-alt1
- repocop cronbuild 20150907. At your service.
- fr.zip build 2015-09-01 11:22 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508181238-alt1
- repocop cronbuild 20150823. At your service.
- fr.zip build 2015-08-18 12:38 UTC

* Sat Jul 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507171445-alt1
- repocop cronbuild 20150725. At your service.
- fr.zip build 2015-07-17 14:45 UTC

* Fri Jul 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507091901-alt1
- repocop cronbuild 20150710. At your service.
- fr.zip build 2015-07-09 19:01 UTC

* Thu Jun 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506191700-alt1
- repocop cronbuild 20150625. At your service.
- fr.zip build 2015-06-19 17:00 UTC

* Fri Jun 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506171644-alt1
- repocop cronbuild 20150619. At your service.
- fr.zip build 2015-06-17 16:44 UTC

* Thu Jun 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201506101226-alt1
- repocop cronbuild 20150611. At your service.
- fr.zip build 2015-06-10 12:26 UTC

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505221731-alt1
- repocop cronbuild 20150604. At your service.
- fr.zip build 2015-05-22 17:31 UTC

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505151049-alt1
- repocop cronbuild 20150522. At your service.
- fr.zip build 2015-05-15 10:49 UTC

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201505120945-alt1
- repocop cronbuild 20150515. At your service.
- fr.zip build 2015-05-12 09:45 UTC

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504281816-alt1
- repocop cronbuild 20150501. At your service.
- fr.zip build 2015-04-28 18:16 UTC

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504231612-alt1
- repocop cronbuild 20150424. At your service.
- fr.zip build 2015-04-23 16:12 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504101525-alt1
- repocop cronbuild 20150417. At your service.
- fr.zip build 2015-04-10 15:25 UTC

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504081937-alt1
- repocop cronbuild 20150410. At your service.
- fr.zip build 2015-04-08 19:37 UTC

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503302025-alt1
- repocop cronbuild 20150403. At your service.
- fr.zip build 2015-03-30 20:25 UTC

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503172141-alt1
- repocop cronbuild 20150320. At your service.
- fr.zip build 2015-03-17 21:41 UTC

* Thu Mar 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503111236-alt1
- repocop cronbuild 20150312. At your service.
- fr.zip build 2015-03-11 12:36 UTC

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201503051223-alt1
- repocop cronbuild 20150306. At your service.
- fr.zip build 2015-03-05 12:23 UTC

* Fri Feb 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502242123-alt1
- repocop cronbuild 20150227. At your service.
- fr.zip build 2015-02-24 21:23 UTC

* Thu Feb 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502192147-alt1
- repocop cronbuild 20150219. At your service.
- fr.zip build 2015-02-19 21:47 UTC

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502061740-alt1
- repocop cronbuild 20150213. At your service.
- fr.zip build 2015-02-06 17:40 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201502031615-alt1
- repocop cronbuild 20150206. At your service.
- fr.zip build 2015-02-03 16:15 UTC

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501271706-alt1
- repocop cronbuild 20150130. At your service.
- fr.zip build 2015-01-27 17:06 UTC

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501151836-alt1
- repocop cronbuild 20150116. At your service.
- fr.zip build 2015-01-15 18:36 UTC

* Thu Jan 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201501081832-alt1
- repocop cronbuild 20150108. At your service.
- fr.zip build 2015-01-08 18:32 UTC

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412272211-alt1
- repocop cronbuild 20150102. At your service.
- fr.zip build 2014-12-27 22:11 UTC

* Fri Dec 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412141328-alt1
- repocop cronbuild 20141219. At your service.
- fr.zip build 2014-12-14 13:28 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412101552-alt1
- repocop cronbuild 20141211. At your service.
- fr.zip build 2014-12-10 15:52 UTC

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412041925-alt1
- repocop cronbuild 20141205. At your service.
- fr.zip build 2014-12-04 19:25 UTC

* Thu Nov 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411261746-alt1
- repocop cronbuild 20141127. At your service.
- fr.zip build 2014-11-26 17:46 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411121550-alt1
- repocop cronbuild 20141114. At your service.
- fr.zip build 2014-11-12 15:50 UTC

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411041655-alt1
- repocop cronbuild 20141107. At your service.
- fr.zip build 2014-11-04 16:55 UTC

* Thu Oct 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410291704-alt1
- repocop cronbuild 20141030. At your service.
- fr.zip build 2014-10-29 17:04 UTC

* Thu Oct 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410121255-alt1
- repocop cronbuild 20141016. At your service.
- fr.zip build 2014-10-12 12:55 UTC

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410081107-alt1
- repocop cronbuild 20141010. At your service.
- fr.zip build 2014-10-08 11:07 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409281006-alt1
- repocop cronbuild 20141003. At your service.
- fr.zip build 2014-09-28 10:06 UTC

* Fri Sep 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409241618-alt1
- repocop cronbuild 20140926. At your service.
- fr.zip build 2014-09-24 16:18 UTC

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409091845-alt1
- repocop cronbuild 20140911. At your service.
- fr.zip build 2014-09-09 18:45 UTC

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201407041435-alt1
- repocop cronbuild 20140705. At your service.
- fr.zip build 2014-07-04 14:35 UTC

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406201954-alt1
- repocop cronbuild 20140621. At your service.
- fr.zip build 2014-06-20 19:54 UTC

* Sat Jun 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201406121638-alt1
- repocop cronbuild 20140614. At your service.
- fr.zip build 2014-06-12 16:38 UTC

* Sat May 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405081822-alt1
- repocop cronbuild 20140510. At your service.
- fr.zip build 2014-05-08 18:22 UTC

* Sat May 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404261045-alt1
- repocop cronbuild 20140503. At your service.
- fr.zip build 2014-04-26 10:45 UTC

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404090950-alt1
- repocop cronbuild 20140411. At your service.
- fr.zip build 2014-04-09 09:50 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201404031150-alt1
- repocop cronbuild 20140404. At your service.
- fr.zip build 2014-04-03 11:50 UTC

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403281019-alt1
- repocop cronbuild 20140329. At your service.
- fr.zip build 2014-03-28 10:19 UTC

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403111720-alt1
- repocop cronbuild 20140314. At your service.
- fr.zip build 2014-03-11 17:20 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402241355-alt1
- repocop cronbuild 20140301. At your service.
- fr.zip build 2014-02-24 13:55 UTC

* Sat Dec 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312112023-alt1
- repocop cronbuild 20131214. At your service.
- fr.zip build 2013-12-11 20:23 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312061043-alt1
- repocop cronbuild 20131206. At your service.
- fr.zip build 2013-12-06 10:43 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311261620-alt1
- repocop cronbuild 20131129. At your service.
- fr.zip build 2013-11-26 16:20 UTC

* Sat Nov 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311221911-alt1
- repocop cronbuild 20131123. At your service.
- fr.zip build 2013-11-22 19:11 UTC

* Sat Nov 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311132017-alt1
- repocop cronbuild 20131116. At your service.
- fr.zip build 2013-11-13 20:17 UTC

* Sat Nov 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311010643-alt1
- repocop cronbuild 20131102. At your service.
- fr.zip build 2013-11-01 06:43 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310121229-alt1
- repocop cronbuild 20131018. At your service.
- fr.zip build 2013-10-12 12:29 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310111815-alt1
- repocop cronbuild 20131011. At your service.
- fr.zip build 2013-10-11 18:15 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309141750-alt1
- repocop cronbuild 20130920. At your service.
- fr.zip build 2013-09-14 17:50 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308231112-alt1
- repocop cronbuild 20130830. At your service.
- fr.zip build 2013-08-23 11:12 UTC

* Thu Aug 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308221815-alt1
- repocop cronbuild 20130822. At your service.
- fr.zip build 2013-08-22 18:15 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307101703-alt1
- repocop cronbuild 20130712. At your service.
- fr.zip build 2013-07-10 17:03 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201307021726-alt1
- repocop cronbuild 20130705. At your service.
- fr.zip build 2013-07-02 17:26 UTC

* Fri Jun 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306261313-alt1
- repocop cronbuild 20130628. At your service.
- fr.zip build 2013-06-26 13:13 UTC

* Fri Jun 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306141603-alt1
- repocop cronbuild 20130621. At your service.
- fr.zip build 2013-06-14 16:03 UTC

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306131954-alt1
- repocop cronbuild 20130614. At your service.
- fr.zip build 2013-06-13 19:54 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305300956-alt1
- repocop cronbuild 20130531. At your service.
- fr.zip build 2013-05-30 09:56 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305221632-alt1
- repocop cronbuild 20130524. At your service.
- fr.zip build 2013-05-22 16:32 UTC

* Fri May 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305150858-alt1
- repocop cronbuild 20130517. At your service.
- fr.zip build 2013-05-15 08:58 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305040844-alt1
- repocop cronbuild 20130509. At your service.
- fr.zip build 2013-05-04 08:44 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304121542-alt1
- repocop cronbuild 20130417. At your service.
- fr.zip build 2013-04-12 15:42 UTC

* Wed Mar 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303201701-alt1
- repocop cronbuild 20130327. At your service.
- fr.zip build 2013-03-20 17:01 UTC

* Tue Mar 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302271743-alt1
- repocop cronbuild 20130305. At your service.
- fr.zip build 2013-02-27 17:43 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302220914-alt1
- repocop cronbuild 20130225. At your service.
- fr.zip build 2013-02-22 09:14 UTC

* Tue Feb 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302151818-alt1
- repocop cronbuild 20130219. At your service.
- fr.zip build 2013-02-15 18:18 UTC

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302032132-alt1
- repocop cronbuild 20130204. At your service.
- fr.zip build 2013-02-03 21:32 UTC

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301261628-alt1
- repocop cronbuild 20130129. At your service.
- fr.zip build 2013-01-26 16:28 UTC

* Tue Jan 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212292101-alt1
- repocop cronbuild 20130101. At your service.
- fr.zip build 2012-12-29 21:01 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212211307-alt1
- repocop cronbuild 20121224. At your service.
- fr.zip build 2012-12-21 13:07 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212141605-alt1
- repocop cronbuild 20121217. At your service.
- fr.zip build 2012-12-14 16:05 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212062151-alt1
- repocop cronbuild 20121210. At your service.
- fr.zip build 2012-12-06 21:51 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211251634-alt1
- repocop cronbuild 20121126. At your service.
- fr.zip build 2012-11-25 16:34 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211191107-alt1
- repocop cronbuild 20121119. At your service.
- fr.zip build 2012-11-19 11:07 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211101918-alt1
- repocop cronbuild 20121112. At your service.
- fr.zip build 2012-11-10 19:18 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210312208-alt1
- repocop cronbuild 20121105. At your service.
- fr.zip build 2012-10-31 22:08 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210291122-alt1
- repocop cronbuild 20121029. At your service.
- fr.zip build 2012-10-29 11:22 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210190707-alt1
- repocop cronbuild 20121022. At your service.
- fr.zip build 2012-10-19 07:07 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210131448-alt1
- repocop cronbuild 20121015. At your service.
- fr.zip build 2012-10-13 14:48 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210012004-alt1
- repocop cronbuild 20121008. At your service.
- fr.zip build 2012-10-01 20:04 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209171957-alt1
- repocop cronbuild 20120917. At your service.
- fr.zip build 2012-09-17 19:57 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209061614-alt1
- repocop cronbuild 20120910. At your service.
- fr.zip build 2012-09-06 16:14 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208291928-alt1
- repocop cronbuild 20120904. At your service.
- fr.zip build 2012-08-29 19:28 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208161642-alt1
- repocop cronbuild 20120820. At your service.
- fr.zip build 2012-08-16 16:42 UTC

* Mon Jul 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207170801-alt1
- repocop cronbuild 20120723. At your service.
- fr.zip build 2012-07-17 08:01 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207051203-alt1
- repocop cronbuild 20120709. At your service.
- fr.zip build 2012-07-05 12:03 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206201443-alt1
- repocop cronbuild 20120625. At your service.
- fr.zip build 2012-06-20 14:43 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206142032-alt1
- repocop cronbuild 20120618. At your service.
- fr.zip build 2012-06-14 20:32 UTC

* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206071356-alt1
- repocop cronbuild 20120611. At your service.
- fr.zip build 2012-06-07 13:56 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206031721-alt1
- repocop cronbuild 20120604. At your service.
- fr.zip build 2012-06-03 17:21 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231746-alt1
- repocop cronbuild 20120528. At your service.
- fr.zip build 2012-05-23 17:46 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204231443-alt1
- repocop cronbuild 20120423. At your service.
- fr.zip build 2012-04-23 14:43 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204101256-alt1
- repocop cronbuild 20120416. At your service.
- fr.zip build 2012-04-10 12:56 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203271536-alt1
- repocop cronbuild 20120402. At your service.
- fr.zip build 2012-03-27 15:36 UTC

* Mon Mar 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203201952-alt1
- repocop cronbuild 20120326. At your service.
- fr.zip build 2012-03-20 19:52 UTC

* Thu Mar 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203061934-alt1
- repocop cronbuild 20120308. At your service.
- fr.zip build 2012-03-06 19:34 UTC

* Thu Feb 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202220948-alt1
- repocop cronbuild 20120223. At your service.
- fr.zip build 2012-02-22 09:48 UTC

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202111010-alt1
- repocop cronbuild 20120216. At your service.
- fr.zip build 2012-02-11 10:10 UTC

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202081935-alt1
- repocop cronbuild 20120209. At your service.
- fr.zip build 2012-02-08 19:35 UTC

* Thu Feb 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201302034-alt1
- repocop cronbuild 20120202. At your service.
- fr.zip build 2012-01-30 20:34 UTC

* Thu Jan 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201072150-alt1
- repocop cronbuild 20120112. At your service.
- fr.zip build 2012-01-07 21:50 UTC

* Thu Jan 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201042116-alt1
- repocop cronbuild 20120105. At your service.
- fr.zip build 2012-01-04 21:16 UTC

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112192151-alt1
- repocop cronbuild 20111222. At your service.
- fr.zip build 2011-12-19 21:51 UTC

* Thu Dec 15 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112091829-alt1
- repocop cronbuild 20111215. At your service.
- fr.zip build 2011-12-09 18:29 UTC

* Thu Dec 08 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112081249-alt1
- repocop cronbuild 20111208. At your service.
- fr.zip build 2011-12-08 12:49 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111251639-alt1
- repocop cronbuild 20111125. At your service.
- fr.zip build 2011-11-25 16:39 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111232006-alt2
- Fix requires

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111232006-alt1
- repocop cronbuild 20111123. At your service.
- fr.zip build 2011-11-23 20:06 UTC

* Sun Nov 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111202140-alt1
- repocop cronbuild 20111120. At your service.
- fr.zip build 2011-11-20 21:40 UTC

* Sat Nov 19 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111191256-alt1
- repocop cronbuild 20111119. At your service.
- fr.zip build 2011-11-19 12:56 UTC

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111181223-alt1
- repocop cronbuild 20111118. At your service.
- fr.zip build 2011-11-18 12:23 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151942-alt1
- repocop cronbuild 20111116. At your service.
- fr.zip build 2011-11-15 19:42 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031917-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031917-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111031917-alt1
- repocop cronbuild 20111105. At your service.
- fr.zip build 2011-11-03 19:17 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt1
- fr.zip build 2011-10-12 18:40 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231534-alt1
- fr.zip build 2011-09-23 15:34 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109230935-alt1
- fr.zip build 2011-09-23 09:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109221808-alt1
- fr.zip build 2011-09-22 18:08 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- fr.zip build 2011-09-21 15:30 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109161112-alt1
- fr.zip build 2011-09-16 11:12 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109081534-alt1
- fr.zip build 2011-09-08 15:34 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109041828-alt1
- fr.zip build 2011-09-04 18:28 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108241508-alt1
- fr.zip build 2011-08-24 15:08 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108190836-alt1
- fr.zip build 2011-08-19 08:36 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- fr.zip build 2011-08-16 13:07 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108141034-alt1
- fr.zip build 2011-08-14 10:34 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-fr
- fr.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110718-alt1
- fr_utf8.zip build 2011-07-18

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081211
- new build for ALT Linux from cvs
