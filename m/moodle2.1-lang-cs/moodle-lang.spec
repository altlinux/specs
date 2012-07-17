# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename cs
%define packagversion 2.1.0
%define packagedate 201207101844
%define moodlebranch 2.1
%define moodlepackagename %moodle_name%moodlebranch
%define langname Czech
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.1-lang-cs
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
* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207101844-alt1
- repocop cronbuild 20120717. At your service.
- cs.zip build 2012-07-10 18:44 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207091351-alt1
- repocop cronbuild 20120710. At your service.
- cs.zip build 2012-07-09 13:51 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201207021542-alt1
- repocop cronbuild 20120703. At your service.
- cs.zip build 2012-07-02 15:42 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205301304-alt1
- repocop cronbuild 20120605. At your service.
- cs.zip build 2012-05-30 13:04 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205281334-alt1
- repocop cronbuild 20120528. At your service.
- cs.zip build 2012-05-28 13:34 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205151414-alt1
- repocop cronbuild 20120521. At your service.
- cs.zip build 2012-05-15 14:14 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201205071107-alt1
- repocop cronbuild 20120507. At your service.
- cs.zip build 2012-05-07 11:07 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201204271130-alt1
- repocop cronbuild 20120430. At your service.
- cs.zip build 2012-04-27 11:30 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203161034-alt1
- repocop cronbuild 20120319. At your service.
- cs.zip build 2012-03-16 10:34 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011549-alt1
- repocop cronbuild 20120306. At your service.
- cs.zip build 2012-03-01 15:49 UTC

* Tue Feb 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202281017-alt1
- repocop cronbuild 20120228. At your service.
- cs.zip build 2012-02-28 10:17 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201311044-alt1
- repocop cronbuild 20120131. At your service.
- cs.zip build 2012-01-31 10:44 UTC

* Tue Dec 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112230839-alt1
- repocop cronbuild 20111227. At your service.
- cs.zip build 2011-12-23 08:39 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112131059-alt1
- repocop cronbuild 20111213. At your service.
- cs.zip build 2011-12-13 10:59 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112051734-alt1
- repocop cronbuild 20111206. At your service.
- cs.zip build 2011-12-05 17:34 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111151151-alt1
- Rename package to moodle2.1-lang-cs
- cs.zip build 2011-11-15 11:51 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111151153-alt2
- Fix requires

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151153-alt1
- repocop cronbuild 20111116. At your service.
- cs.zip build 2011-11-15 11:53 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- cs.zip build 2011-10-06 22:30 UTC

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110061223-alt1
- cs.zip build 2011-10-06 12:23 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109220241-alt1
- cs.zip build 2011-09-22 02:41 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- cs.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108232211-alt2
- Fix requires

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108232211-alt1
- cs.zip build 2011-08-23 22:11 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108170854-alt1
- cs.zip build 2011-08-17 08:54 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- cs.zip build 2011-08-16 13:07 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-cs
- cs.zip build 2011-08-11 23:00 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110730-alt1
- cs_utf8.zip build 2011-07-30
- initial build for ALT Linux Sisyphus
