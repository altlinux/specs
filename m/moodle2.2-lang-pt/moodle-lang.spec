# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename pt
%define packagversion 2.2.0
%define packagedate 201207112119
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Portuguese
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-pt
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
* Wed Jul 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207112119-alt1
- repocop cronbuild 20120711. At your service.
- pt.zip build 2012-07-11 21:19 UTC

* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207041132-alt1
- repocop cronbuild 20120704. At your service.
- pt.zip build 2012-07-04 11:32 UTC

* Wed Jun 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206271142-alt1
- repocop cronbuild 20120627. At your service.
- pt.zip build 2012-06-27 11:42 UTC

* Wed Jun 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206201555-alt1
- repocop cronbuild 20120620. At your service.
- pt.zip build 2012-06-20 15:55 UTC

* Wed Jun 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121218-alt1
- repocop cronbuild 20120613. At your service.
- pt.zip build 2012-06-12 12:18 UTC

* Wed Jun 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206042306-alt1
- repocop cronbuild 20120606. At your service.
- pt.zip build 2012-06-04 23:06 UTC

* Wed May 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120523. At your service.
- pt.zip build 2012-05-23 15:49 UTC

* Wed May 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120516. At your service.
- pt.zip build 2012-05-11 11:00 UTC

* Wed May 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120502. At your service.
- pt.zip build 2012-04-27 11:30 UTC

* Wed Apr 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204241426-alt1
- repocop cronbuild 20120425. At your service.
- pt.zip build 2012-04-24 14:26 UTC

* Wed Apr 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204181401-alt1
- repocop cronbuild 20120418. At your service.
- pt.zip build 2012-04-18 14:01 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204101704-alt1
- repocop cronbuild 20120410. At your service.
- pt.zip build 2012-04-10 17:04 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203291546-alt1
- repocop cronbuild 20120403. At your service.
- pt.zip build 2012-03-29 15:46 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203271717-alt1
- repocop cronbuild 20120327. At your service.
- pt.zip build 2012-03-27 17:17 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203201400-alt1
- repocop cronbuild 20120320. At your service.
- pt.zip build 2012-03-20 14:00 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203171452-alt1
- Rename package to moodle2.2-lang-pt
- pt.zip build 2012-03-17 14:52 UTC

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
