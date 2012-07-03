# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename pt
%define packagversion 2.1.0
%define packagedate 201207021515
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Portuguese
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-pt
Version: %packagversion.%packagedate
Release: %branch_release alt1

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
* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207021515-alt1
- repocop cronbuild 20120703. At your service.
- pt.zip build 2012-07-02 15:15 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206251431-alt1
- repocop cronbuild 20120626. At your service.
- pt.zip build 2012-06-25 14:31 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206151013-alt1
- repocop cronbuild 20120619. At your service.
- pt.zip build 2012-06-15 10:13 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206042306-alt1
- repocop cronbuild 20120612. At your service.
- pt.zip build 2012-06-04 23:06 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201206012236-alt1
- repocop cronbuild 20120605. At your service.
- pt.zip build 2012-06-01 22:36 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- pt.zip build 2012-05-23 15:49 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- pt.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204192250-alt1
- repocop cronbuild 20120424. At your service.
- pt.zip build 2012-04-19 22:50 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204161243-alt1
- repocop cronbuild 20120417. At your service.
- pt.zip build 2012-04-16 12:43 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203291546-alt1
- repocop cronbuild 20120403. At your service.
- pt.zip build 2012-03-29 15:46 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203261439-alt1
- repocop cronbuild 20120327. At your service.
- pt.zip build 2012-03-26 14:39 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203171452-alt1
- repocop cronbuild 20120320. At your service.
- pt.zip build 2012-03-17 14:52 UTC

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203082202-alt1
- repocop cronbuild 20120309. At your service.
- pt.zip build 2012-03-08 22:02 UTC

* Fri Jan 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201251819-alt1
- repocop cronbuild 20120127. At your service.
- pt.zip build 2012-01-25 18:19 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- pt.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111021930-alt1
- Rename package to moodle2.1-lang-pt
- pt.zip build 2011-11-02 19:30

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
- pt.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- pt.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161557-alt2
- Fix requires

* Wed Aug 17 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161557-alt1
- pt.zip build 2011-08-16 15:57 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103221701-alt1
- Rename package to moodle2.0-lang-pt
- pt.zip build 2011-03-22 17:01 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100814-alt1
- pt_utf8.zip build 2010-08-14

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100814
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20080926
- new build for ALT Linux from cvs
