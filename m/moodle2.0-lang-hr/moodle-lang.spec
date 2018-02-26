# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename hr
%define packagversion 2.0.0
%define packagedate 201205271027
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Croatian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-hr
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.0
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.0
Provides: %moodle_name-%packagetype-%packagename-version = %packagedate
Provides: %moodle_name-%packagetype-%packagename = %version-%release
Provides: %moodle_name-%packagetype-%oldpackagename = %version-%release
Conflicts: %moodle_name-%packagetype-%packagename < %version
Conflicts: %moodle_name-%packagetype-%oldpackagename < %version

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
* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205271027-alt1
- repocop cronbuild 20120528. At your service.
- hr.zip build 2012-05-27 10:27 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204141322-alt1
- repocop cronbuild 20120416. At your service.
- hr.zip build 2012-04-14 13:22 UTC

* Sat Mar 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202282102-alt1
- repocop cronbuild 20120303. At your service.
- hr.zip build 2012-02-28 21:02 UTC

* Sat Feb 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202231326-alt1
- repocop cronbuild 20120225. At your service.
- hr.zip build 2012-02-23 13:26 UTC

* Sat Feb 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202112139-alt1
- repocop cronbuild 20120218. At your service.
- hr.zip build 2012-02-11 21:39 UTC

* Sat Jan 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201091003-alt1
- repocop cronbuild 20120114. At your service.
- hr.zip build 2012-01-09 10:03 UTC

* Sat Dec 17 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112161240-alt1
- repocop cronbuild 20111217. At your service.
- hr.zip build 2011-12-16 12:40 UTC

* Sat Dec 10 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112101625-alt1
- repocop cronbuild 20111210. At your service.
- hr.zip build 2011-12-10 16:25 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- hr.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- hr.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-hr
- hr.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt2
- Fix Summary

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- Test build
- hr_utf8.zip build 2010-05-26
- initial build for ALT Linux Sisyphus
