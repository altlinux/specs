# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename zh_tw
%define packagversion 2.4.0
%define packagedate 201312130546
%define moodlebranch 2.4
%define moodlepackagename %moodle_name%moodlebranch
%define langname Chinese (Traditional/Big5)
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.4-lang-zh_tw
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
ln -s -f $(relative %buildroot%_ttffontsdir/chinese-big5/bkai00mp.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- zh_tw.zip build 2013-12-13 05:46 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201312051555-alt1
- repocop cronbuild 20131206. At your service.
- zh_tw.zip build 2013-12-05 15:55 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311271509-alt1
- repocop cronbuild 20131129. At your service.
- zh_tw.zip build 2013-11-27 15:09 UTC

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311181559-alt1
- repocop cronbuild 20131122. At your service.
- zh_tw.zip build 2013-11-18 15:59 UTC

* Fri Nov 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311141315-alt1
- repocop cronbuild 20131115. At your service.
- zh_tw.zip build 2013-11-14 13:15 UTC

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201311071522-alt1
- repocop cronbuild 20131108. At your service.
- zh_tw.zip build 2013-11-07 15:22 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310270422-alt1
- repocop cronbuild 20131101. At your service.
- zh_tw.zip build 2013-10-27 04:22 UTC

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310230622-alt1
- repocop cronbuild 20131025. At your service.
- zh_tw.zip build 2013-10-23 06:22 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310170356-alt1
- repocop cronbuild 20131018. At your service.
- zh_tw.zip build 2013-10-17 03:56 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201310021109-alt1
- repocop cronbuild 20131004. At your service.
- zh_tw.zip build 2013-10-02 11:09 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309221601-alt1
- repocop cronbuild 20130927. At your service.
- zh_tw.zip build 2013-09-22 16:01 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309191102-alt1
- repocop cronbuild 20130920. At your service.
- zh_tw.zip build 2013-09-19 11:02 UTC

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309090538-alt1
- repocop cronbuild 20130913. At your service.
- zh_tw.zip build 2013-09-09 05:38 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201309061024-alt1
- repocop cronbuild 20130906. At your service.
- zh_tw.zip build 2013-09-06 10:24 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201308261615-alt1
- repocop cronbuild 20130830. At your service.
- zh_tw.zip build 2013-08-26 16:15 UTC

* Fri Jul 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201307030346-alt1
- repocop cronbuild 20130705. At your service.
- zh_tw.zip build 2013-07-03 03:46 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201306060511-alt1
- repocop cronbuild 20130607. At your service.
- zh_tw.zip build 2013-06-06 05:11 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305222323-alt1
- repocop cronbuild 20130524. At your service.
- zh_tw.zip build 2013-05-22 23:23 UTC

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305070819-alt1
- repocop cronbuild 20130509. At your service.
- zh_tw.zip build 2013-05-07 08:19 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304080842-alt1
- Rename package to moodle2.4-lang-zh_tw
- zh_tw.zip build 2013-04-08 08:42 UTC

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201303190756-alt1
- repocop cronbuild 20130320. At your service.
- zh_tw.zip build 2013-03-19 07:56 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- zh_tw.zip build 2013-01-26 15:39 UTC

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201212220847-alt1
- repocop cronbuild 20121224. At your service.
- zh_tw.zip build 2012-12-22 08:47 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211061331-alt1
- repocop cronbuild 20121112. At your service.
- zh_tw.zip build 2012-11-06 13:31 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211031752-alt1
- repocop cronbuild 20121105. At your service.
- zh_tw.zip build 2012-11-03 17:52 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- zh_tw.zip build 2012-05-23 15:49 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- zh_tw.zip build 2012-05-11 11:00 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201202260922-alt1
- Rename package to moodle2.2-lang-zh_tw
- zh_tw.zip build 2012-02-26 09:22 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201291011-alt1
- repocop cronbuild 20120203. At your service.
- zh_tw.zip build 2012-01-29 10:11 UTC

* Sat Dec 10 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111210. At your service.
- zh_tw.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-zh_tw
- zh_tw.zip build 2011-11-02 19:30 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use %%_ttffontsdir/chinese-big5/bkai00mp.ttf for
  %%moodle_langdir/zh_tw/fonts/default.ttf
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- zh_tw.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- zh_tw.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-zh_tw
- zh_tw.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- zh_tw_utf8.zip build 2010-05-26

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20080926
- new build for ALT Linux from cvs
