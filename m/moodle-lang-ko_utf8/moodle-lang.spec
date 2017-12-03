# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ko_utf8
%define packagversion 1.9.10
%define packagedate 20100526
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define langname Korean

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-lang-ko_utf8
Version: %packagversion.%packagedate
Release: %branch_release alt6.1

Summary: Moodle %langname localozation
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
BuildPreReq: rpm-macros-fonts
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

%define default_ttf %moodle_langdir/%packagename/fonts/default.ttf
ln -s -f $(relative %buildroot%_ttffontsdir/naver-nanum/NanumGothic.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

%files
%moodle_langdir/*

%changelog
* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.10.20100526-alt6.1
- NMU: use naver-nanum fonts instead of nhn-nanum

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt6
- Use moodle-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt5
- Fix cronbuild use

* Fri Nov 04 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt4
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt3
- Update for cronbuild use

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt2
- Fix requires

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- ko_utf8.zip build 2010-05-26
- Use %%_ttffontsdir/nhn-nanum/NanumGothic.ttf for
  %%moodle_langdir/ja_utf8/fonts/default.ttf
- initial build for ALT Linux Sisyphus
