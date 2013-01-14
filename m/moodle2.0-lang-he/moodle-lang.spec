# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename he
%define packagversion 2.0.0
%define packagedate 201301131914
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Hebrew
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-he
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
* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301131914-alt1
- repocop cronbuild 20130114. At your service.
- he.zip build 2013-01-13 19:14 UTC

* Tue Jan 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301052242-alt1
- repocop cronbuild 20130108. At your service.
- he.zip build 2013-01-05 22:42 UTC

* Tue Jan 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212292102-alt1
- repocop cronbuild 20130101. At your service.
- he.zip build 2012-12-29 21:02 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212231956-alt1
- repocop cronbuild 20121224. At your service.
- he.zip build 2012-12-23 19:56 UTC

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212171113-alt1
- repocop cronbuild 20121217. At your service.
- he.zip build 2012-12-17 11:13 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212101059-alt1
- repocop cronbuild 20121210. At your service.
- he.zip build 2012-12-10 10:59 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212032243-alt1
- repocop cronbuild 20121203. At your service.
- he.zip build 2012-12-03 22:43 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211251416-alt1
- repocop cronbuild 20121126. At your service.
- he.zip build 2012-11-25 14:16 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211152351-alt1
- repocop cronbuild 20121119. At your service.
- he.zip build 2012-11-15 23:51 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211071628-alt1
- repocop cronbuild 20121112. At your service.
- he.zip build 2012-11-07 16:28 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211041626-alt1
- repocop cronbuild 20121105. At your service.
- he.zip build 2012-11-04 16:26 UTC

* Mon Oct 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210282116-alt1
- repocop cronbuild 20121029. At your service.
- he.zip build 2012-10-28 21:16 UTC

* Sun Oct 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210142202-alt1
- repocop cronbuild 20121021. At your service.
- he.zip build 2012-10-14 22:02 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210142111-alt1
- repocop cronbuild 20121015. At your service.
- he.zip build 2012-10-14 21:11 UTC

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210071916-alt1
- repocop cronbuild 20121008. At your service.
- he.zip build 2012-10-07 19:16 UTC

* Sun Sep 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209301959-alt1
- repocop cronbuild 20120930. At your service.
- he.zip build 2012-09-30 19:59 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209141008-alt1
- repocop cronbuild 20120917. At your service.
- he.zip build 2012-09-14 10:08 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209091236-alt1
- repocop cronbuild 20120910. At your service.
- he.zip build 2012-09-09 12:36 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209021231-alt1
- repocop cronbuild 20120904. At your service.
- he.zip build 2012-09-02 12:31 UTC

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208150907-alt1
- repocop cronbuild 20120820. At your service.
- he.zip build 2012-08-15 09:07 UTC

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208071733-alt1
- repocop cronbuild 20120814. At your service.
- he.zip build 2012-08-07 17:33 UTC

* Mon Aug 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208061421-alt1
- repocop cronbuild 20120806. At your service.
- he.zip build 2012-08-06 14:21 UTC

* Mon Jul 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207241404-alt1
- repocop cronbuild 20120730. At your service.
- he.zip build 2012-07-24 14:04 UTC

* Tue Jul 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207231251-alt1
- repocop cronbuild 20120724. At your service.
- he.zip build 2012-07-23 12:51 UTC

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207151041-alt1
- repocop cronbuild 20120717. At your service.
- he.zip build 2012-07-15 10:41 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207050503-alt1
- repocop cronbuild 20120709. At your service.
- he.zip build 2012-07-05 05:03 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206211348-alt1
- repocop cronbuild 20120625. At your service.
- he.zip build 2012-06-21 13:48 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206181011-alt1
- repocop cronbuild 20120618. At your service.
- he.zip build 2012-06-18 10:11 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205291334-alt1
- repocop cronbuild 20120604. At your service.
- he.zip build 2012-05-29 13:34 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205241019-alt1
- repocop cronbuild 20120528. At your service.
- he.zip build 2012-05-24 10:19 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205150820-alt1
- repocop cronbuild 20120521. At your service.
- he.zip build 2012-05-15 08:20 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204301329-alt1
- repocop cronbuild 20120430. At your service.
- he.zip build 2012-04-30 13:29 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204151134-alt1
- repocop cronbuild 20120416. At your service.
- he.zip build 2012-04-15 11:34 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204021200-alt1
- repocop cronbuild 20120402. At your service.
- he.zip build 2012-04-02 12:00 UTC

* Mon Mar 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203221542-alt1
- repocop cronbuild 20120326. At your service.
- he.zip build 2012-03-22 15:42 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203191430-alt1
- repocop cronbuild 20120319. At your service.
- he.zip build 2012-03-19 14:30 UTC

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202161217-alt1
- repocop cronbuild 20120221. At your service.
- he.zip build 2012-02-16 12:17 UTC

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202141411-alt1
- repocop cronbuild 20120214. At your service.
- he.zip build 2012-02-14 14:11 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201261241-alt1
- repocop cronbuild 20120131. At your service.
- he.zip build 2012-01-26 12:41 UTC

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201191320-alt1
- repocop cronbuild 20120124. At your service.
- he.zip build 2012-01-19 13:20 UTC

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201171128-alt1
- repocop cronbuild 20120117. At your service.
- he.zip build 2012-01-17 11:28 UTC

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112190920-alt1
- repocop cronbuild 20111220. At your service.
- he.zip build 2011-12-19 09:20 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112061333-alt1
- repocop cronbuild 20111206. At your service.
- he.zip build 2011-12-06 13:33 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111201348-alt2
- Fix requires

* Sun Nov 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111201348-alt1
- repocop cronbuild 20111120. At your service.
- he.zip build 2011-11-20 13:48 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111101425-alt1
- repocop cronbuild 20111116. At your service.
- he.zip build 2011-11-10 14:25 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- he.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- he.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-he
- he.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110804-alt1
- he_utf8.zip build 2011-08-04
- initial build for ALT Linux Sisyphus
