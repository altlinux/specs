# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ja_utf8
%define packagversion 1.9.10
%define packagedate 20120509
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define langname Japanese

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-lang-ja_utf8
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl2plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base < 2.0
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 1.9
Provides: %moodle_name-%packagetype-%packagename-version = %packagedate
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-base >= 2.0

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
* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120509-alt1
- repocop cronbuild 20120514. At your service.
- ja_utf8.zip build 2012-05-09

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120504-alt1
- repocop cronbuild 20120507. At your service.
- ja_utf8.zip build 2012-05-04

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120327-alt1
- repocop cronbuild 20120402. At your service.
- ja_utf8.zip build 2012-03-27

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120214-alt1
- repocop cronbuild 20120217. At your service.
- ja_utf8.zip build 2012-02-14

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120111-alt1
- repocop cronbuild 20120113. At your service.
- ja_utf8.zip build 2012-01-11

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20111110-alt1
- repocop cronbuild 20111116. At your service.
- ja_utf8.zip build 2011-11-10

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110910-alt5
- Use moodle-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110910-alt4
- Fix cronbuild use

* Fri Nov 04 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110910-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110910-alt2
- Update for cronbuild use

* Mon Sep 12 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110910-alt1
- ja_utf8.zip build 2011-09-10

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110809-alt2
- Fix requires

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110809-alt1
- ja_utf8.zip build 2011-08-09
- Add %%moodle_langdir/ja_utf8/fonts/default.ttf

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081210
- new build for ALT Linux from cvs
