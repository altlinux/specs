# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ko
%define packagversion 2.5.0
%define packagedate 201601271115
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Korean
%define oldpackagename %{packagename}_utf8

# For sets default.ttf
%define default_ttfdir %moodle_langdir/%packagename/fonts
%define default_ttf %default_ttfdir/default.ttf

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-ko
Version: %packagversion.%packagedate
Release: %branch_release alt1.1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.5
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.5
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
* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.0.201601271115-alt1.1
- NMU: use naver-nanum fonts instead of nhn-nanum

* Sun Jan 31 2016 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201601271115-alt1
- repocop cronbuild 20160131. At your service.
- ko.zip build 2016-01-27 11:15 UTC

* Fri Oct 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410112209-alt1
- repocop cronbuild 20141017. At your service.
- ko.zip build 2014-10-11 22:09 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201408311123-alt1
- repocop cronbuild 20140919. At your service.
- ko.zip build 2014-08-31 11:23 UTC

* Sat Jan 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201401231346-alt1
- repocop cronbuild 20140125. At your service.
- ko.zip build 2014-01-23 13:46 UTC

* Fri Dec 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201312130546-alt1
- repocop cronbuild 20131213. At your service.
- ko.zip build 2013-12-13 05:46 UTC

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201308260649-alt1
- repocop cronbuild 20130831. At your service.
- ko.zip build 2013-08-26 06:49 UTC

* Sat Jul 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307240128-alt1
- repocop cronbuild 20130727. At your service.
- ko.zip build 2013-07-24 01:28 UTC

* Sat Jul 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307190406-alt1
- repocop cronbuild 20130720. At your service.
- ko.zip build 2013-07-19 04:06 UTC

* Sat Jul 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201307120656-alt1
- repocop cronbuild 20130713. At your service.
- ko.zip build 2013-07-12 06:56 UTC

* Sat Jun 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306251202-alt1
- repocop cronbuild 20130629. At your service.
- ko.zip build 2013-06-25 12:02 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140511-alt1
- repocop cronbuild 20130615. At your service.
- ko.zip build 2013-06-14 05:11 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201305300259-alt1
- Rename package to moodle2.5-lang-ko
- ko.zip build 2013-05-30 02:59 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.4.0.201305211315-alt1
- repocop cronbuild 20130524. At your service.
- ko.zip build 2013-05-21 13:15 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201304080843-alt1
- Rename package to moodle2.4-lang-ko
- ko.zip build 2013-04-08 08:43 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201301231538-alt1
- repocop cronbuild 20130304. At your service.
- ko.zip build 2013-01-23 15:38 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- ko.zip build 2012-11-01 07:00 UTC

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209200452-alt1
- repocop cronbuild 20121001. At your service.
- ko.zip build 2012-09-20 04:52 UTC

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209060149-alt1
- repocop cronbuild 20120911. At your service.
- ko.zip build 2012-09-06 01:49 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201209041326-alt1
- repocop cronbuild 20120904. At your service.
- ko.zip build 2012-09-04 13:26 UTC

* Wed Aug 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208280141-alt1
- repocop cronbuild 20120829. At your service.
- ko.zip build 2012-08-28 01:41 UTC

* Tue Aug 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201208200045-alt1
- repocop cronbuild 20120821. At your service.
- ko.zip build 2012-08-20 00:45 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- ko.zip build 2012-05-23 15:49 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- ko.zip build 2012-05-11 11:00 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204280906-alt1
- repocop cronbuild 20120501. At your service.
- ko.zip build 2012-04-28 09:06 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204240207-alt1
- repocop cronbuild 20120424. At your service.
- ko.zip build 2012-04-24 02:07 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204091512-alt1
- repocop cronbuild 20120410. At your service.
- ko.zip build 2012-04-09 15:12 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203100146-alt1
- Rename package to moodle2.2-lang-ko
- ko.zip build 2012-03-10 01:46 UTC

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
