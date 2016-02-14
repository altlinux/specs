# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename no
%define packagversion 2.1.0
%define packagedate 201602120619
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Norwegian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-no
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.1
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.1
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
* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201602120619-alt1
- repocop cronbuild 20160214. At your service.
- no.zip build 2016-02-12 06:19 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- no.zip build 2015-11-08 22:20 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201508071011-alt1
- repocop cronbuild 20150823. At your service.
- no.zip build 2015-08-07 10:11 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507122042-alt1
- repocop cronbuild 20150716. At your service.
- no.zip build 2015-07-12 20:42 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201507010757-alt1
- repocop cronbuild 20150702. At your service.
- no.zip build 2015-07-01 07:57 UTC

* Sat Apr 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201504140653-alt1
- repocop cronbuild 20150418. At your service.
- no.zip build 2015-04-14 06:53 UTC

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201412050855-alt1
- repocop cronbuild 20141212. At your service.
- no.zip build 2014-12-05 08:55 UTC

* Fri Sep 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201408121222-alt1
- repocop cronbuild 20140912. At your service.
- no.zip build 2014-08-12 12:22 UTC

* Sat May 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201405020751-alt1
- repocop cronbuild 20140503. At your service.
- no.zip build 2014-05-02 07:51 UTC

* Sat Apr 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403291455-alt1
- repocop cronbuild 20140405. At your service.
- no.zip build 2014-03-29 14:55 UTC

* Sat Mar 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201403181153-alt1
- repocop cronbuild 20140322. At your service.
- no.zip build 2014-03-18 11:53 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402241422-alt1
- repocop cronbuild 20140301. At your service.
- no.zip build 2014-02-24 14:22 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201402121641-alt1
- repocop cronbuild 20140215. At your service.
- no.zip build 2014-02-12 16:41 UTC

* Sat Jan 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401231406-alt1
- repocop cronbuild 20140125. At your service.
- no.zip build 2014-01-23 14:06 UTC

* Sat Jan 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201401100731-alt1
- repocop cronbuild 20140111. At your service.
- no.zip build 2014-01-10 07:31 UTC

* Sat Jan 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201312311320-alt1
- repocop cronbuild 20140104. At your service.
- no.zip build 2013-12-31 13:20 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310170248-alt1
- repocop cronbuild 20131018. At your service.
- no.zip build 2013-10-17 02:48 UTC

* Sat Oct 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310101252-alt1
- repocop cronbuild 20131012. At your service.
- no.zip build 2013-10-10 12:52 UTC

* Sat Oct 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310011328-alt1
- repocop cronbuild 20131005. At your service.
- no.zip build 2013-10-01 13:28 UTC

* Sat Sep 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201309031344-alt1
- repocop cronbuild 20130907. At your service.
- no.zip build 2013-09-03 13:44 UTC

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308231151-alt1
- repocop cronbuild 20130824. At your service.
- no.zip build 2013-08-23 11:51 UTC

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201308111039-alt1
- repocop cronbuild 20130817. At your service.
- no.zip build 2013-08-11 10:39 UTC

* Sat Jun 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201306060914-alt1
- repocop cronbuild 20130608. At your service.
- no.zip build 2013-06-06 09:14 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305211302-alt1
- repocop cronbuild 20130524. At your service.
- no.zip build 2013-05-21 13:02 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303191348-alt1
- repocop cronbuild 20130320. At your service.
- no.zip build 2013-03-19 13:48 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201303091515-alt1
- repocop cronbuild 20130313. At your service.
- no.zip build 2013-03-09 15:15 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201302221112-alt1
- repocop cronbuild 20130225. At your service.
- no.zip build 2013-02-22 11:12 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- no.zip build 2013-01-26 15:39 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301051804-alt1
- repocop cronbuild 20130107. At your service.
- no.zip build 2013-01-05 18:04 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201211150841-alt1
- repocop cronbuild 20121119. At your service.
- no.zip build 2012-11-15 08:41 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- no.zip build 2012-05-23 15:49 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- no.zip build 2012-04-27 11:30 UTC

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
