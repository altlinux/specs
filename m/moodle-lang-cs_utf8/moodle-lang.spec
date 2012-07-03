# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename cs_utf8
%define packagversion 1.9.10
%define packagedate 20120126
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define langname Czech

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-lang-cs_utf8
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
* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120126-alt1
- repocop cronbuild 20120201. At your service.
- cs_utf8.zip build 2012-01-26

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20111125-alt1
- repocop cronbuild 20111130. At your service.
- cs_utf8.zip build 2011-11-25

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110730-alt6
- Use moodle-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110730-alt5
- Fix cronbuild use

* Fri Nov 04 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110730-alt4
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110730-alt3
- Update for cronbuild use

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110730-alt2
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110730-alt1
- cs_utf8.zip build 2011-07-30
- initial build for ALT Linux Sisyphus
