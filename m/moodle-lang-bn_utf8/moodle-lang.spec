# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename bn_utf8
%define packagversion 1.9.10
%define packagedate 20100526
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define langname Bangla

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-lang-bn_utf8
Version: %packagversion.%packagedate
Release: %branch_release alt7

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
* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt7
- Use moodle-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt6
- Fix cronbuild use

* Fri Nov 04 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt5
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt4
- Update for cronbuild use

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt3
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt2
- Fix Summary

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- bn_utf8.zip build 2010-05-26
- initial build for ALT Linux Sisyphus
