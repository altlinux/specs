# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename hr
%define packagversion 2.0.0
%define packagedate 201601121412
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
* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201601121412-alt1
- repocop cronbuild 20160124. At your service.
- hr.zip build 2016-01-12 14:12 UTC

* Thu Dec 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511270748-alt1
- repocop cronbuild 20151203. At your service.
- hr.zip build 2015-11-27 07:48 UTC

* Thu Oct 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201510061114-alt1
- repocop cronbuild 20151008. At your service.
- hr.zip build 2015-10-06 11:14 UTC

* Thu Oct 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410261902-alt1
- repocop cronbuild 20141030. At your service.
- hr.zip build 2014-10-26 19:02 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409281131-alt1
- repocop cronbuild 20141003. At your service.
- hr.zip build 2014-09-28 11:31 UTC

* Fri Sep 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409212014-alt1
- repocop cronbuild 20140926. At your service.
- hr.zip build 2014-09-21 20:14 UTC

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409180530-alt1
- repocop cronbuild 20140918. At your service.
- hr.zip build 2014-09-18 05:30 UTC

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409081921-alt1
- repocop cronbuild 20140911. At your service.
- hr.zip build 2014-09-08 19:21 UTC

* Sat May 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201405290733-alt1
- repocop cronbuild 20140531. At your service.
- hr.zip build 2014-05-29 07:33 UTC

* Fri Dec 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201312031620-alt1
- repocop cronbuild 20131206. At your service.
- hr.zip build 2013-12-03 16:20 UTC

* Fri Nov 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201311261620-alt1
- repocop cronbuild 20131129. At your service.
- hr.zip build 2013-11-26 16:20 UTC

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310150952-alt1
- repocop cronbuild 20131018. At your service.
- hr.zip build 2013-10-15 09:52 UTC

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309292049-alt1
- repocop cronbuild 20131004. At your service.
- hr.zip build 2013-09-29 20:49 UTC

* Fri Sep 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309231808-alt1
- repocop cronbuild 20130927. At your service.
- hr.zip build 2013-09-23 18:08 UTC

* Fri Sep 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309151315-alt1
- repocop cronbuild 20130920. At your service.
- hr.zip build 2013-09-15 13:15 UTC

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201306052010-alt1
- repocop cronbuild 20130607. At your service.
- hr.zip build 2013-06-05 20:10 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305211303-alt1
- repocop cronbuild 20130524. At your service.
- hr.zip build 2013-05-21 13:03 UTC

* Wed Apr 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201304121334-alt1
- repocop cronbuild 20130417. At your service.
- hr.zip build 2013-04-12 13:34 UTC

* Wed Mar 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303071004-alt1
- repocop cronbuild 20130313. At your service.
- hr.zip build 2013-03-07 10:04 UTC

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303011657-alt1
- repocop cronbuild 20130304. At your service.
- hr.zip build 2013-03-01 16:57 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302230150-alt1
- repocop cronbuild 20130225. At your service.
- hr.zip build 2013-02-23 01:50 UTC

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201212032117-alt1
- repocop cronbuild 20121210. At your service.
- hr.zip build 2012-12-03 21:17 UTC

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211301744-alt1
- repocop cronbuild 20121203. At your service.
- hr.zip build 2012-11-30 17:44 UTC

* Mon Nov 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211231510-alt1
- repocop cronbuild 20121126. At your service.
- hr.zip build 2012-11-23 15:10 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211151005-alt1
- repocop cronbuild 20121119. At your service.
- hr.zip build 2012-11-15 10:05 UTC

* Mon Nov 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211101743-alt1
- repocop cronbuild 20121112. At your service.
- hr.zip build 2012-11-10 17:43 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210291508-alt1
- repocop cronbuild 20121105. At your service.
- hr.zip build 2012-10-29 15:08 UTC

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
