# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ja
%define packagversion 2.2.0
%define packagedate 201207021415
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Japanese
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-ja
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
BuildPreReq: rpm-macros-fonts

%description
%summary

%prep
%setup

%build

%install
mkdir -p  %buildroot%moodle_langdir/
cp -rp * %buildroot%moodle_langdir/

# Create symlink for default.ttf
install -d %buildroot%default_ttfdir
ln -s -f $(relative %buildroot%_ttffontsdir/sazanami/gothic/sazanami-gothic.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207021415-alt1
- repocop cronbuild 20120703. At your service.
- ja.zip build 2012-07-02 14:15 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206260057-alt1
- repocop cronbuild 20120626. At your service.
- ja.zip build 2012-06-26 00:57 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191841-alt1
- repocop cronbuild 20120619. At your service.
- ja.zip build 2012-06-19 18:41 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206122003-alt1
- repocop cronbuild 20120612. At your service.
- ja.zip build 2012-06-12 20:03 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205290230-alt1
- repocop cronbuild 20120529. At your service.
- ja.zip build 2012-05-29 02:30 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205220007-alt1
- repocop cronbuild 20120522. At your service.
- ja.zip build 2012-05-22 00:07 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205131609-alt1
- repocop cronbuild 20120515. At your service.
- ja.zip build 2012-05-13 16:09 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205081813-alt1
- repocop cronbuild 20120508. At your service.
- ja.zip build 2012-05-08 18:13 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204290553-alt1
- repocop cronbuild 20120501. At your service.
- ja.zip build 2012-04-29 05:53 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204200621-alt1
- repocop cronbuild 20120424. At your service.
- ja.zip build 2012-04-20 06:21 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204171536-alt1
- repocop cronbuild 20120417. At your service.
- ja.zip build 2012-04-17 15:36 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203291353-alt1
- repocop cronbuild 20120403. At your service.
- ja.zip build 2012-03-29 13:53 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203251650-alt1
- repocop cronbuild 20120327. At your service.
- ja.zip build 2012-03-25 16:50 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203151448-alt1
- Rename package to moodle2.2-lang-ja
- ja.zip build 2012-03-15 14:48 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203151449-alt1
- repocop cronbuild 20120320. At your service.
- ja.zip build 2012-03-15 14:49 UTC

* Tue Mar 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203091645-alt1
- repocop cronbuild 20120313. At your service.
- ja.zip build 2012-03-09 16:45 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120307. At your service.
- ja.zip build 2012-03-01 11:00 UTC

* Wed Feb 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202241819-alt1
- repocop cronbuild 20120229. At your service.
- ja.zip build 2012-02-24 18:19 UTC

* Wed Feb 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202172003-alt1
- repocop cronbuild 20120222. At your service.
- ja.zip build 2012-02-17 20:03 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202131205-alt1
- repocop cronbuild 20120215. At your service.
- ja.zip build 2012-02-13 12:05 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201280622-alt1
- repocop cronbuild 20120201. At your service.
- ja.zip build 2012-01-28 06:22 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201251804-alt1
- repocop cronbuild 20120125. At your service.
- ja.zip build 2012-01-25 18:04 UTC

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201121404-alt1
- repocop cronbuild 20120118. At your service.
- ja.zip build 2012-01-12 14:04 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201062040-alt1
- repocop cronbuild 20120111. At your service.
- ja.zip build 2012-01-06 20:40 UTC

* Wed Dec 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112260049-alt1
- repocop cronbuild 20111228. At your service.
- ja.zip build 2011-12-26 00:49 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112211928-alt1
- repocop cronbuild 20111221. At your service.
- ja.zip build 2011-12-21 19:28 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112142037-alt1
- repocop cronbuild 20111214. At your service.
- ja.zip build 2011-12-14 20:37 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112011705-alt1
- repocop cronbuild 20111207. At your service.
- ja.zip build 2011-12-01 17:05 UTC

* Thu Dec 01 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111301536-alt1
- repocop cronbuild 20111201. At your service.
- ja.zip build 2011-11-30 15:36 UTC

* Mon Nov 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111280210-alt1
- repocop cronbuild 20111128. At your service.
- ja.zip build 2011-11-28 02:10 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111241342-alt1
- Rename package to moodle2.1-lang-ja
- ja.zip build 2011-11-24 13:42 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111151726-alt2
- Fix requires

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151726-alt1
- repocop cronbuild 20111116. At your service.
- ja.zip build 2011-11-15 17:26 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031658-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031658-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111031658-alt1
- repocop cronbuild 20111105. At your service.
- ja.zip build 2011-11-03 16:58 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt2
- Update for cronbuild use

* Mon Oct 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241631-alt1
- ja.zip build 2011-10-24 16:31 UTC

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110202137-alt1
- ja.zip build 2011-10-20 21:37 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110041726-alt1
- ja.zip build 2011-10-04 17:26 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109272111-alt1
- ja.zip build 2011-09-27 21:11 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109261912-alt1
- ja.zip build 2011-09-26 19:12 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109222056-alt1
- ja.zip build 2011-09-22 20:56 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109212035-alt1
- ja.zip build 2011-09-21 20:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- ja.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109181907-alt1
- ja.zip build 2011-09-18 19:07 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109151910-alt1
- ja.zip build 2011-09-15 19:10 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141837-alt1
- ja.zip build 2011-09-14 18:37 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109131809-alt1
- ja.zip build 2011-09-13 18:09 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109121803-alt1
- ja.zip build 2011-09-12 18:03 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109111621-alt1
- ja.zip build 2011-09-11 16:21 UTC

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109090331-alt1
- ja.zip build 2011-09-09 03:31 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109070502-alt1
- ja.zip build 2011-09-07 05:02 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108231816-alt1
- ja.zip build 2011-08-23 18:16 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108222128-alt1
- ja.zip build 2011-08-22 21:28 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108220123-alt1
- ja.zip build 2011-08-22 01:23 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108191757-alt1
- ja.zip build 2011-08-19 17:57 UTC

* Fri Aug 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108181726-alt1
- ja.zip build 2011-08-18 17:26 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108171909-alt1
- ja.zip build 2011-08-17 19:09 UTC

* Wed Aug 17 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161743-alt1
- ja.zip build 2011-08-16 17:43 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108152131-alt1
- ja.zip build 2011-08-15 21:31 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108121459-alt1
- Rename package to moodle2.0-lang-ja
- ja.zip build 2011-08-12 14:59 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110809-alt1
- ja_utf8.zip build 2011-08-09
- Add %%moodle_langdir/ja_utf8/fonts/default.ttf

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081210
- new build for ALT Linux from cvs
