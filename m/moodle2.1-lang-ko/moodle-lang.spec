# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ko
%define packagversion 2.1.0
%define packagedate 201601271115
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Korean
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-ko
Version: %packagversion.%packagedate
Release: %branch_release alt1.1

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
ln -s -f $(relative %buildroot%_ttffontsdir/naver-nanum/NanumGothic.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0.201601271115-alt1.1
- NMU: use naver-nanum fonts instead of nhn-nanum

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201601271115-alt1
- repocop cronbuild 20160131. At your service.
- ko.zip build 2016-01-27 11:15 UTC

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201410112209-alt1
- repocop cronbuild 20141018. At your service.
- ko.zip build 2014-10-11 22:09 UTC

* Fri Sep 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201408290548-alt1
- repocop cronbuild 20140912. At your service.
- ko.zip build 2014-08-29 05:48 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201310170248-alt1
- repocop cronbuild 20131018. At your service.
- ko.zip build 2013-10-17 02:48 UTC

* Fri Jul 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307211339-alt1
- repocop cronbuild 20130726. At your service.
- ko.zip build 2013-07-21 13:39 UTC

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307190203-alt1
- repocop cronbuild 20130719. At your service.
- ko.zip build 2013-07-19 02:03 UTC

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201307091148-alt1
- repocop cronbuild 20130712. At your service.
- ko.zip build 2013-07-09 11:48 UTC

* Fri May 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305300302-alt1
- repocop cronbuild 20130531. At your service.
- ko.zip build 2013-05-30 03:02 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201305211310-alt1
- repocop cronbuild 20130524. At your service.
- ko.zip build 2013-05-21 13:10 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201301231538-alt1
- repocop cronbuild 20130304. At your service.
- ko.zip build 2013-01-23 15:38 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209200452-alt1
- repocop cronbuild 20121001. At your service.
- ko.zip build 2012-09-20 04:52 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209060147-alt1
- repocop cronbuild 20120911. At your service.
- ko.zip build 2012-09-06 01:47 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201209020342-alt1
- repocop cronbuild 20120904. At your service.
- ko.zip build 2012-09-02 03:42 UTC

* Tue Aug 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201208280051-alt1
- repocop cronbuild 20120828. At your service.
- ko.zip build 2012-08-28 00:51 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- ko.zip build 2012-05-23 15:49 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- ko.zip build 2012-04-27 11:30 UTC

* Sun Mar 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120304. At your service.
- ko.zip build 2012-03-01 11:00 UTC

* Sun Dec 11 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111211. At your service.
- ko.zip build 2011-12-09 16:00 UTC

* Sun Dec 04 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112032253-alt1
- repocop cronbuild 20111204. At your service.
- ko.zip build 2011-12-03 22:53 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-ko
- ko.zip build 2011-11-02 19:30 UTC

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
- ko.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- ko.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-ko
- ko.zip build 2011-08-11 23:00 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- ko_utf8.zip build 2010-05-26
- Use %%_ttffontsdir/nhn-nanum/NanumGothic.ttf for
  %%moodle_langdir/ja_utf8/fonts/default.ttf
- initial build for ALT Linux Sisyphus
