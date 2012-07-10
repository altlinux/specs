# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename zh_cn
%define packagversion 2.2.0
%define packagedate 201207061246
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Chinese (Simplified)
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-zh_cn
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
ln -s -f $(relative %buildroot%_ttffontsdir/chinese-gb2312/gbsn00lp.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207061246-alt1
- repocop cronbuild 20120710. At your service.
- zh_cn.zip build 2012-07-06 12:46 UTC

* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207030019-alt1
- repocop cronbuild 20120704. At your service.
- zh_cn.zip build 2012-07-03 00:19 UTC

* Wed Jun 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206231235-alt1
- repocop cronbuild 20120627. At your service.
- zh_cn.zip build 2012-06-23 12:35 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206190153-alt1
- repocop cronbuild 20120619. At your service.
- zh_cn.zip build 2012-06-19 01:53 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121321-alt1
- repocop cronbuild 20120612. At your service.
- zh_cn.zip build 2012-06-12 13:21 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206051408-alt1
- repocop cronbuild 20120605. At your service.
- zh_cn.zip build 2012-06-05 14:08 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205290000-alt1
- repocop cronbuild 20120529. At your service.
- zh_cn.zip build 2012-05-29 00:00 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205210759-alt1
- repocop cronbuild 20120522. At your service.
- zh_cn.zip build 2012-05-21 07:59 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205141128-alt1
- repocop cronbuild 20120515. At your service.
- zh_cn.zip build 2012-05-14 11:28 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205050157-alt1
- repocop cronbuild 20120508. At your service.
- zh_cn.zip build 2012-05-05 01:57 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204290138-alt1
- repocop cronbuild 20120501. At your service.
- zh_cn.zip build 2012-04-29 01:38 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204180710-alt1
- repocop cronbuild 20120424. At your service.
- zh_cn.zip build 2012-04-18 07:10 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204150051-alt1
- repocop cronbuild 20120417. At your service.
- zh_cn.zip build 2012-04-15 00:51 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204062353-alt1
- repocop cronbuild 20120410. At your service.
- zh_cn.zip build 2012-04-06 23:53 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204021057-alt1
- repocop cronbuild 20120403. At your service.
- zh_cn.zip build 2012-04-02 10:57 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203260300-alt1
- repocop cronbuild 20120327. At your service.
- zh_cn.zip build 2012-03-26 03:00 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203190057-alt1
- Rename package to moodle2.2-lang-zh_cn
- zh_cn.zip build 2012-03-19 00:57 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203190057-alt1
- repocop cronbuild 20120320. At your service.
- zh_cn.zip build 2012-03-19 00:57 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203050017-alt1
- repocop cronbuild 20120307. At your service.
- zh_cn.zip build 2012-03-05 00:17 UTC

* Wed Feb 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202291152-alt1
- repocop cronbuild 20120229. At your service.
- zh_cn.zip build 2012-02-29 11:52 UTC

* Wed Feb 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202180928-alt1
- repocop cronbuild 20120222. At your service.
- zh_cn.zip build 2012-02-18 09:28 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202130111-alt1
- repocop cronbuild 20120215. At your service.
- zh_cn.zip build 2012-02-13 01:11 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202061021-alt1
- repocop cronbuild 20120208. At your service.
- zh_cn.zip build 2012-02-06 10:21 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201301220-alt1
- repocop cronbuild 20120201. At your service.
- zh_cn.zip build 2012-01-30 12:20 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201230846-alt1
- repocop cronbuild 20120125. At your service.
- zh_cn.zip build 2012-01-23 08:46 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201080425-alt1
- repocop cronbuild 20120111. At your service.
- zh_cn.zip build 2012-01-08 04:25 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112160535-alt1
- repocop cronbuild 20111221. At your service.
- zh_cn.zip build 2011-12-16 05:35 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112121304-alt1
- repocop cronbuild 20111214. At your service.
- zh_cn.zip build 2011-12-12 13:04 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112041131-alt1
- repocop cronbuild 20111207. At your service.
- zh_cn.zip build 2011-12-04 11:31 UTC

* Thu Dec 01 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111290202-alt1
- repocop cronbuild 20111201. At your service.
- zh_cn.zip build 2011-11-29 02:02 UTC

* Sun Nov 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111270215-alt1
- repocop cronbuild 20111127. At your service.
- zh_cn.zip build 2011-11-27 02:15 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111251135-alt1
- Rename package to moodle2.1-lang-zh_cn
- zh_cn.zip build 2011-11-25 11:35 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111220133-alt2
- Fix requires

* Tue Nov 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111220133-alt1
- repocop cronbuild 20111122. At your service.
- zh_cn.zip build 2011-11-22 01:33 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111130433-alt1
- repocop cronbuild 20111116. At your service.
- zh_cn.zip build 2011-11-13 04:33 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111021307-alt3
- Use %%_ttffontsdir/chinese-gb2312/gbsn00lp.ttf for
  %%moodle_langdir/zh_cn/fonts/default.ttf
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111021307-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111021307-alt1
- repocop cronbuild 20111105. At your service.
- zh_cn.zip build 2011-11-02 13:07 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110251310-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110251310-alt2
- Update for cronbuild use

* Tue Oct 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110251310-alt1
- zh_cn.zip build 2011-10-25 13:10 UTC

* Mon Oct 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110241152-alt1
- zh_cn.zip build 2011-10-24 11:52 UTC

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110220330-alt1
- zh_cn.zip build 2011-10-22 03:30 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110050227-alt1
- zh_cn.zip build 2011-10-05 02:27 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109281117-alt1
- zh_cn.zip build 2011-09-28 11:17 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109270925-alt1
- zh_cn.zip build 2011-09-27 09:25 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231252-alt1
- zh_cn.zip build 2011-09-23 12:52 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- zh_cn.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109180903-alt1
- zh_cn.zip build 2011-09-18 09:03 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109160250-alt1
- zh_cn.zip build 2011-09-16 02:50 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109140833-alt1
- zh_cn.zip build 2011-09-14 08:33 UTC

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109120755-alt1
- zh_cn.zip build 2011-09-12 07:55 UTC

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109090955-alt1
- zh_cn.zip build 2011-09-09 09:55 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109081131-alt1
- zh_cn.zip build 2011-09-08 11:31 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109070725-alt1
- zh_cn.zip build 2011-09-07 07:25 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108240815-alt1
- zh_cn.zip build 2011-08-24 08:15 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108231110-alt1
- zh_cn.zip build 2011-08-23 11:10 UTC

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108221302-alt1
- zh_cn.zip build 2011-08-22 13:02 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108190203-alt1
- zh_cn.zip build 2011-08-19 02:03 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108150558-alt1
- zh_cn.zip build 2011-08-15 05:58 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108130645-alt1
- zh_cn.zip build 2011-08-13 06:45 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108120108-alt1
- Rename package to moodle2.0-lang-zh_cn
- zh_cn.zip build 2011-08-12 01:08 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- zh_cn_utf8.zip build 2010-05-26

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20080526
- new build for ALT Linux from cvs
