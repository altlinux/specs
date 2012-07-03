# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename pt_br
%define packagversion 2.0.0
%define packagedate 201206301742
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Portuguese (Brazil)
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-pt_br
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
* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206301742-alt1
- repocop cronbuild 20120703. At your service.
- pt_br.zip build 2012-06-30 17:42 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206222325-alt1
- repocop cronbuild 20120626. At your service.
- pt_br.zip build 2012-06-22 23:25 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206181525-alt1
- repocop cronbuild 20120618. At your service.
- pt_br.zip build 2012-06-18 15:25 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206112038-alt1
- repocop cronbuild 20120612. At your service.
- pt_br.zip build 2012-06-11 20:38 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206041938-alt1
- repocop cronbuild 20120605. At your service.
- pt_br.zip build 2012-06-04 19:38 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205281447-alt1
- repocop cronbuild 20120528. At your service.
- pt_br.zip build 2012-05-28 14:47 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205182057-alt1
- repocop cronbuild 20120521. At your service.
- pt_br.zip build 2012-05-18 20:57 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205141455-alt1
- repocop cronbuild 20120514. At your service.
- pt_br.zip build 2012-05-14 14:55 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204251410-alt1
- repocop cronbuild 20120430. At your service.
- pt_br.zip build 2012-04-25 14:10 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204200243-alt1
- repocop cronbuild 20120423. At your service.
- pt_br.zip build 2012-04-20 02:43 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204162126-alt1
- repocop cronbuild 20120416. At your service.
- pt_br.zip build 2012-04-16 21:26 UTC

* Mon Apr 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204082324-alt1
- repocop cronbuild 20120409. At your service.
- pt_br.zip build 2012-04-08 23:24 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203301343-alt1
- repocop cronbuild 20120402. At your service.
- pt_br.zip build 2012-03-30 13:43 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203261714-alt1
- repocop cronbuild 20120327. At your service.
- pt_br.zip build 2012-03-26 17:14 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203191345-alt1
- repocop cronbuild 20120319. At your service.
- pt_br.zip build 2012-03-19 13:45 UTC

* Tue Mar 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203100221-alt1
- repocop cronbuild 20120313. At your service.
- pt_br.zip build 2012-03-10 02:21 UTC

* Thu Mar 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203061259-alt1
- repocop cronbuild 20120308. At your service.
- pt_br.zip build 2012-03-06 12:59 UTC

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203011855-alt1
- repocop cronbuild 20120301. At your service.
- pt_br.zip build 2012-03-01 18:55 UTC

* Thu Feb 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202231553-alt1
- repocop cronbuild 20120223. At your service.
- pt_br.zip build 2012-02-23 15:53 UTC

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202102340-alt1
- repocop cronbuild 20120216. At your service.
- pt_br.zip build 2012-02-10 23:40 UTC

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202071934-alt1
- repocop cronbuild 20120209. At your service.
- pt_br.zip build 2012-02-07 19:34 UTC

* Thu Jan 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201261540-alt1
- repocop cronbuild 20120126. At your service.
- pt_br.zip build 2012-01-26 15:40 UTC

* Thu Jan 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201192114-alt1
- repocop cronbuild 20120119. At your service.
- pt_br.zip build 2012-01-19 21:14 UTC

* Thu Jan 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201111834-alt1
- repocop cronbuild 20120112. At your service.
- pt_br.zip build 2012-01-11 18:34 UTC

* Thu Dec 29 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112291731-alt1
- repocop cronbuild 20111229. At your service.
- pt_br.zip build 2011-12-29 17:31 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111101730-alt1
- Rename package to moodle2.0-lang-pt_br
- pt_br.zip build 2011-11-10 17:30 UTC

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
