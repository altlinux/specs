# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename cs
%define packagversion 2.0.0
%define packagedate 201210301355
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Czech
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-cs
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
* Sun Nov 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210301355-alt1
- repocop cronbuild 20121104. At your service.
- cs.zip build 2012-10-30 13:55 UTC

* Sun Oct 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210080743-alt1
- repocop cronbuild 20121014. At your service.
- cs.zip build 2012-10-08 07:43 UTC

* Mon Sep 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209170751-alt1
- repocop cronbuild 20120917. At your service.
- cs.zip build 2012-09-17 07:51 UTC

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201209101551-alt1
- repocop cronbuild 20120910. At your service.
- cs.zip build 2012-09-10 15:51 UTC

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208290930-alt1
- repocop cronbuild 20120904. At your service.
- cs.zip build 2012-08-29 09:30 UTC

* Mon Aug 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201208030940-alt1
- repocop cronbuild 20120806. At your service.
- cs.zip build 2012-08-03 09:40 UTC

* Mon Jul 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207271624-alt1
- repocop cronbuild 20120730. At your service.
- cs.zip build 2012-07-27 16:24 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207091351-alt1
- repocop cronbuild 20120709. At your service.
- cs.zip build 2012-07-09 13:51 UTC

* Mon Jul 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207021542-alt1
- repocop cronbuild 20120702. At your service.
- cs.zip build 2012-07-02 15:42 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205281310-alt1
- repocop cronbuild 20120528. At your service.
- cs.zip build 2012-05-28 13:10 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205071107-alt1
- repocop cronbuild 20120507. At your service.
- cs.zip build 2012-05-07 11:07 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203161034-alt1
- repocop cronbuild 20120319. At your service.
- cs.zip build 2012-03-16 10:34 UTC

* Mon Mar 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203011549-alt1
- repocop cronbuild 20120305. At your service.
- cs.zip build 2012-03-01 15:49 UTC

* Mon Feb 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201311044-alt1
- repocop cronbuild 20120206. At your service.
- cs.zip build 2012-01-31 10:44 UTC

* Mon Jan 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201301125-alt1
- repocop cronbuild 20120130. At your service.
- cs.zip build 2012-01-30 11:25 UTC

* Mon Dec 26 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112230839-alt1
- repocop cronbuild 20111226. At your service.
- cs.zip build 2011-12-23 08:39 UTC

* Mon Dec 19 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112131059-alt1
- repocop cronbuild 20111219. At your service.
- cs.zip build 2011-12-13 10:59 UTC

* Mon Dec 12 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112080945-alt1
- repocop cronbuild 20111212. At your service.
- cs.zip build 2011-12-08 09:45 UTC

* Mon Dec 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112051734-alt1
- repocop cronbuild 20111205. At your service.
- cs.zip build 2011-12-05 17:34 UTC

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
