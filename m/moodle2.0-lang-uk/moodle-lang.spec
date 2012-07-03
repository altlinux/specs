# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename uk
%define packagversion 2.0.0
%define packagedate 201206130921
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Ukrainian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-uk
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
* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206130921-alt1
- repocop cronbuild 20120619. At your service.
- uk.zip build 2012-06-13 09:21 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231549-alt1
- repocop cronbuild 20120528. At your service.
- uk.zip build 2012-05-23 15:49 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205100803-alt1
- repocop cronbuild 20120514. At your service.
- uk.zip build 2012-05-10 08:03 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205060617-alt1
- repocop cronbuild 20120507. At your service.
- uk.zip build 2012-05-06 06:17 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204241104-alt1
- repocop cronbuild 20120430. At your service.
- uk.zip build 2012-04-24 11:04 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204191849-alt1
- repocop cronbuild 20120424. At your service.
- uk.zip build 2012-04-19 18:49 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203162135-alt1
- repocop cronbuild 20120319. At your service.
- uk.zip build 2012-03-16 21:35 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt7
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt6
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt5
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt4
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt3
- Update for cronbuild use

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt2
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt1
- Rename package to moodle2.0-lang-uk
- uk.zip build 2011-03-03 17:30 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- uk_utf8.zip build 2010-05-26

* Tue Nov 23 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt2.cvs20100526
- inheritance fixed

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Tue Oct 27 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt2.1.cvs20091010
- rebuild with new Moodle

* Mon Oct 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20091010
- new build from cvs

* Sun Jul 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20090518
- new build from cvs

* Mon Oct 13 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080926
- new build from cvs

* Mon Sep 08 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080731
- add build requires on rpm-build-webserver-common
- new build from cvs

* Thu Jun 26 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt2.cvs20080526
- change path moodle location

* Mon Jun 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.cvs20080526
- new build for ALT Linux
