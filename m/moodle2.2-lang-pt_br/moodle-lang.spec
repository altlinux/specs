# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename pt_br
%define packagversion 2.2.0
%define packagedate 201206301742
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Portuguese (Brazil)
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-pt_br
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.2
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.2
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
* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206301742-alt1
- repocop cronbuild 20120704. At your service.
- pt_br.zip build 2012-06-30 17:42 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206222325-alt1
- repocop cronbuild 20120626. At your service.
- pt_br.zip build 2012-06-22 23:25 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206181525-alt1
- repocop cronbuild 20120619. At your service.
- pt_br.zip build 2012-06-18 15:25 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206120205-alt1
- repocop cronbuild 20120612. At your service.
- pt_br.zip build 2012-06-12 02:05 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206051613-alt1
- repocop cronbuild 20120605. At your service.
- pt_br.zip build 2012-06-05 16:13 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205292111-alt1
- repocop cronbuild 20120529. At your service.
- pt_br.zip build 2012-05-29 21:11 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205221523-alt1
- repocop cronbuild 20120522. At your service.
- pt_br.zip build 2012-05-22 15:23 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205141455-alt1
- repocop cronbuild 20120515. At your service.
- pt_br.zip build 2012-05-14 14:55 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205081915-alt1
- repocop cronbuild 20120508. At your service.
- pt_br.zip build 2012-05-08 19:15 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- pt_br.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204242057-alt1
- repocop cronbuild 20120424. At your service.
- pt_br.zip build 2012-04-24 20:57 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204162125-alt1
- repocop cronbuild 20120417. At your service.
- pt_br.zip build 2012-04-16 21:25 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204101350-alt1
- repocop cronbuild 20120410. At your service.
- pt_br.zip build 2012-04-10 13:50 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204031852-alt1
- repocop cronbuild 20120403. At your service.
- pt_br.zip build 2012-04-03 18:52 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203272132-alt1
- repocop cronbuild 20120327. At your service.
- pt_br.zip build 2012-03-27 21:32 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203201950-alt1
- repocop cronbuild 20120320. At your service.
- pt_br.zip build 2012-03-20 19:50 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203191345-alt1
- Rename package to moodle2.2-lang-pt_br
- pt_br.zip build 2012-03-19 13:45 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203191345-alt1
- repocop cronbuild 20120320. At your service.
- pt_br.zip build 2012-03-19 13:45 UTC

* Tue Mar 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203100221-alt1
- repocop cronbuild 20120313. At your service.
- pt_br.zip build 2012-03-10 02:21 UTC

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203091409-alt1
- repocop cronbuild 20120309. At your service.
- pt_br.zip build 2012-03-09 14:09 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011855-alt1
- repocop cronbuild 20120302. At your service.
- pt_br.zip build 2012-03-01 18:55 UTC

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202102348-alt1
- repocop cronbuild 20120217. At your service.
- pt_br.zip build 2012-02-10 23:48 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202102118-alt1
- repocop cronbuild 20120210. At your service.
- pt_br.zip build 2012-02-10 21:18 UTC

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201301754-alt1
- repocop cronbuild 20120203. At your service.
- pt_br.zip build 2012-01-30 17:54 UTC

* Fri Jan 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201261540-alt1
- repocop cronbuild 20120127. At your service.
- pt_br.zip build 2012-01-26 15:40 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201192114-alt1
- repocop cronbuild 20120120. At your service.
- pt_br.zip build 2012-01-19 21:14 UTC

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201111834-alt1
- repocop cronbuild 20120113. At your service.
- pt_br.zip build 2012-01-11 18:34 UTC

* Fri Dec 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112292030-alt1
- repocop cronbuild 20111230. At your service.
- pt_br.zip build 2011-12-29 20:30 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- pt_br.zip build 2011-12-09 16:00 UTC

* Sat Nov 26 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111222047-alt1
- Rename package to moodle2.1-lang-pt_br
- pt_br.zip build 2011-11-22 20:47 UTC

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
