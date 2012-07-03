# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename he_utf8
%define packagversion 1.9.10
%define packagedate 20111205
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define langname Hebrew

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-lang-he_utf8
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
* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20111205-alt1
- repocop cronbuild 20111207. At your service.
- he_utf8.zip build 2011-12-05

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111003-alt5
- Use moodle-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111003-alt4
- Fix cronbuild use

* Fri Nov 04 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111003-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111003-alt2
- Update for cronbuild use

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111003-alt1
- he_utf8.zip build 2011-10-03

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110927-alt1
- he_utf8.zip build 2011-09-27

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110804-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110804-alt1
- he_utf8.zip build 2011-08-04
- initial build for ALT Linux Sisyphus
