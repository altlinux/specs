# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename no
%define packagversion 2.2.0
%define packagedate 201602120619
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Norwegian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-no
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.2
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.2
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
* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201602120619-alt1
- repocop cronbuild 20160214. At your service.
- no.zip build 2016-02-12 06:19 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- no.zip build 2015-11-08 22:20 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201508132110-alt1
- repocop cronbuild 20150823. At your service.
- no.zip build 2015-08-13 21:10 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201507122042-alt1
- repocop cronbuild 20150716. At your service.
- no.zip build 2015-07-12 20:42 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201507010757-alt1
- repocop cronbuild 20150702. At your service.
- no.zip build 2015-07-01 07:57 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201504140653-alt1
- repocop cronbuild 20150417. At your service.
- no.zip build 2015-04-14 06:53 UTC

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201502021151-alt1
- repocop cronbuild 20150206. At your service.
- no.zip build 2015-02-02 11:51 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412050855-alt1
- repocop cronbuild 20141212. At your service.
- no.zip build 2014-12-05 08:55 UTC

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201412050759-alt1
- repocop cronbuild 20141205. At your service.
- no.zip build 2014-12-05 07:59 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201408121222-alt1
- repocop cronbuild 20140919. At your service.
- no.zip build 2014-08-12 12:22 UTC

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201405020751-alt1
- repocop cronbuild 20140509. At your service.
- no.zip build 2014-05-02 07:51 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403291455-alt1
- repocop cronbuild 20140404. At your service.
- no.zip build 2014-03-29 14:55 UTC

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201403181153-alt1
- repocop cronbuild 20140321. At your service.
- no.zip build 2014-03-18 11:53 UTC

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402241422-alt1
- repocop cronbuild 20140228. At your service.
- no.zip build 2014-02-24 14:22 UTC

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201402121641-alt1
- repocop cronbuild 20140214. At your service.
- no.zip build 2014-02-12 16:41 UTC

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201401231406-alt1
- repocop cronbuild 20140124. At your service.
- no.zip build 2014-01-23 14:06 UTC

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201401100731-alt1
- repocop cronbuild 20140117. At your service.
- no.zip build 2014-01-10 07:31 UTC

* Fri Jan 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201312311320-alt1
- repocop cronbuild 20140103. At your service.
- no.zip build 2013-12-31 13:20 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310101252-alt1
- repocop cronbuild 20131011. At your service.
- no.zip build 2013-10-10 12:52 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201310011328-alt1
- repocop cronbuild 20131004. At your service.
- no.zip build 2013-10-01 13:28 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201309031344-alt1
- repocop cronbuild 20130906. At your service.
- no.zip build 2013-09-03 13:44 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308231151-alt1
- repocop cronbuild 20130830. At your service.
- no.zip build 2013-08-23 11:51 UTC

* Fri Aug 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201308111039-alt1
- repocop cronbuild 20130816. At your service.
- no.zip build 2013-08-11 10:39 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201306060914-alt1
- repocop cronbuild 20130607. At your service.
- no.zip build 2013-06-06 09:14 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201305211303-alt1
- repocop cronbuild 20130524. At your service.
- no.zip build 2013-05-21 13:03 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303191348-alt1
- repocop cronbuild 20130320. At your service.
- no.zip build 2013-03-19 13:48 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303121119-alt1
- repocop cronbuild 20130313. At your service.
- no.zip build 2013-03-12 11:19 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201302221112-alt1
- repocop cronbuild 20130225. At your service.
- no.zip build 2013-02-22 11:12 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- no.zip build 2013-01-26 15:39 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301112305-alt1
- repocop cronbuild 20130114. At your service.
- no.zip build 2013-01-11 23:05 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301051804-alt1
- repocop cronbuild 20130107. At your service.
- no.zip build 2013-01-05 18:04 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212041448-alt1
- repocop cronbuild 20121210. At your service.
- no.zip build 2012-12-04 14:48 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211260945-alt1
- repocop cronbuild 20121203. At your service.
- no.zip build 2012-11-26 09:45 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211221501-alt1
- repocop cronbuild 20121126. At your service.
- no.zip build 2012-11-22 15:01 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211161143-alt1
- repocop cronbuild 20121119. At your service.
- no.zip build 2012-11-16 11:43 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211091311-alt1
- repocop cronbuild 20121112. At your service.
- no.zip build 2012-11-09 13:11 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- no.zip build 2012-11-01 07:00 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210261222-alt1
- repocop cronbuild 20121029. At your service.
- no.zip build 2012-10-26 12:22 UTC

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210191253-alt1
- repocop cronbuild 20121022. At your service.
- no.zip build 2012-10-19 12:53 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210101350-alt1
- repocop cronbuild 20121015. At your service.
- no.zip build 2012-10-10 13:50 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201210041240-alt1
- repocop cronbuild 20121008. At your service.
- no.zip build 2012-10-04 12:40 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209261134-alt1
- repocop cronbuild 20121001. At your service.
- no.zip build 2012-09-26 11:34 UTC

* Wed Sep 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208311030-alt1
- repocop cronbuild 20120905. At your service.
- no.zip build 2012-08-31 10:30 UTC

* Wed Aug 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208280731-alt1
- repocop cronbuild 20120829. At your service.
- no.zip build 2012-08-28 07:31 UTC

* Wed Aug 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208161144-alt1
- repocop cronbuild 20120822. At your service.
- no.zip build 2012-08-16 11:44 UTC

* Wed Aug 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208031301-alt1
- repocop cronbuild 20120808. At your service.
- no.zip build 2012-08-03 13:01 UTC

* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206270526-alt1
- repocop cronbuild 20120704. At your service.
- no.zip build 2012-06-27 05:26 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191249-alt1
- repocop cronbuild 20120619. At your service.
- no.zip build 2012-06-19 12:49 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121129-alt1
- repocop cronbuild 20120612. At your service.
- no.zip build 2012-06-12 11:29 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206050632-alt1
- repocop cronbuild 20120605. At your service.
- no.zip build 2012-06-05 06:32 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- no.zip build 2012-05-23 15:49 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205210658-alt1
- repocop cronbuild 20120522. At your service.
- no.zip build 2012-05-21 06:58 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- no.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205041400-alt1
- repocop cronbuild 20120508. At your service.
- no.zip build 2012-05-04 14:00 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204300617-alt1
- repocop cronbuild 20120501. At your service.
- no.zip build 2012-04-30 06:17 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204190725-alt1
- repocop cronbuild 20120424. At your service.
- no.zip build 2012-04-19 07:25 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204161306-alt1
- repocop cronbuild 20120417. At your service.
- no.zip build 2012-04-16 13:06 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203141206-alt1
- Rename package to moodle2.2-lang-no
- no.zip build 2012-03-14 12:06 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120302. At your service.
- no.zip build 2012-03-01 11:00 UTC

* Fri Feb 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202231327-alt1
- repocop cronbuild 20120224. At your service.
- no.zip build 2012-02-23 13:27 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202041314-alt1
- repocop cronbuild 20120210. At your service.
- no.zip build 2012-02-04 13:14 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201171357-alt1
- repocop cronbuild 20120120. At your service.
- no.zip build 2012-01-17 13:57 UTC

* Fri Jan 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201031234-alt1
- repocop cronbuild 20120106. At your service.
- no.zip build 2012-01-03 12:34 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- no.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111081406-alt1
- Rename package to moodle2.1-lang-no
- no.zip build 2011-11-08 14:06

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
- no.zip build 2011-10-06 22:30 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109251618-alt1
- no.zip build 2011-09-25 16:18 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- no.zip build 2011-09-21 15:30 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109151708-alt1
- no.zip build 2011-09-15 17:08 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108151942-alt2
- Fix requires

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108151942-alt1
- Rename package to moodle2.0-lang-no
- no.zip build 2011-08-15 19:42 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110630-alt1
- no_utf8.zip build 20110630
- initial build for ALT Linux Sisyphus
