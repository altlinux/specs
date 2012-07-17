# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename eu
%define packagversion 2.0.0
%define packagedate 201207101021
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Basque
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-eu
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
* Mon Jul 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207101021-alt1
- repocop cronbuild 20120716. At your service.
- eu.zip build 2012-07-10 10:21 UTC

* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207040745-alt1
- repocop cronbuild 20120709. At your service.
- eu.zip build 2012-07-04 07:45 UTC

* Mon Jul 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206271359-alt1
- repocop cronbuild 20120702. At your service.
- eu.zip build 2012-06-27 13:59 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206190802-alt1
- repocop cronbuild 20120625. At your service.
- eu.zip build 2012-06-19 08:02 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206181450-alt1
- repocop cronbuild 20120618. At your service.
- eu.zip build 2012-06-18 14:50 UTC

* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206070800-alt1
- repocop cronbuild 20120611. At your service.
- eu.zip build 2012-06-07 08:00 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206041416-alt1
- repocop cronbuild 20120604. At your service.
- eu.zip build 2012-06-04 14:16 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231548-alt1
- repocop cronbuild 20120528. At your service.
- eu.zip build 2012-05-23 15:48 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205180742-alt1
- repocop cronbuild 20120521. At your service.
- eu.zip build 2012-05-18 07:42 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205141027-alt1
- repocop cronbuild 20120514. At your service.
- eu.zip build 2012-05-14 10:27 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205031412-alt1
- repocop cronbuild 20120507. At your service.
- eu.zip build 2012-05-03 14:12 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204270957-alt1
- repocop cronbuild 20120430. At your service.
- eu.zip build 2012-04-27 09:57 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204230812-alt1
- repocop cronbuild 20120423. At your service.
- eu.zip build 2012-04-23 08:12 UTC

* Mon Apr 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204041000-alt1
- repocop cronbuild 20120409. At your service.
- eu.zip build 2012-04-04 10:00 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204020952-alt1
- repocop cronbuild 20120402. At your service.
- eu.zip build 2012-04-02 09:52 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203070848-alt1
- repocop cronbuild 20120307. At your service.
- eu.zip build 2012-03-07 08:48 UTC

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202101055-alt1
- repocop cronbuild 20120215. At your service.
- eu.zip build 2012-02-10 10:55 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202081056-alt1
- repocop cronbuild 20120208. At your service.
- eu.zip build 2012-02-08 10:56 UTC

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202010850-alt1
- repocop cronbuild 20120201. At your service.
- eu.zip build 2012-02-01 08:50 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201240923-alt1
- repocop cronbuild 20120125. At your service.
- eu.zip build 2012-01-24 09:23 UTC

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201180848-alt1
- repocop cronbuild 20120118. At your service.
- eu.zip build 2012-01-18 08:48 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201110835-alt1
- repocop cronbuild 20120111. At your service.
- eu.zip build 2012-01-11 08:35 UTC

* Wed Dec 28 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112230802-alt1
- repocop cronbuild 20111228. At your service.
- eu.zip build 2011-12-23 08:02 UTC

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112161054-alt1
- repocop cronbuild 20111221. At your service.
- eu.zip build 2011-12-16 10:54 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112141638-alt1
- repocop cronbuild 20111214. At your service.
- eu.zip build 2011-12-14 16:38 UTC

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111301636-alt1
- repocop cronbuild 20111130. At your service.
- eu.zip build 2011-11-30 16:36 UTC

* Thu Nov 24 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111240814-alt1
- repocop cronbuild 20111124. At your service.
- eu.zip build 2011-11-24 08:14 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111231509-alt2
- Fix requires

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111231509-alt1
- repocop cronbuild 20111123. At your service.
- eu.zip build 2011-11-23 15:09 UTC

* Mon Nov 21 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111210921-alt1
- repocop cronbuild 20111121. At your service.
- eu.zip build 2011-11-21 09:21 UTC

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111180850-alt1
- repocop cronbuild 20111118. At your service.
- eu.zip build 2011-11-18 08:50 UTC

* Thu Nov 17 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111170831-alt1
- repocop cronbuild 20111117. At your service.
- eu.zip build 2011-11-17 08:31 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151637-alt1
- repocop cronbuild 20111116. At your service.
- eu.zip build 2011-11-15 16:37 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110191531-alt1
- eu.zip build 2011-10-19 15:31 UTC

* Wed Sep 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109281025-alt1
- eu.zip build 2011-09-28 10:25 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109271026-alt1
- eu.zip build 2011-09-27 10:26 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109221435-alt1
- eu.zip build 2011-09-22 14:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- eu.zip build 2011-09-21 15:30 UTC

* Mon Sep 19 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109191034-alt1
- eu.zip build 2011-09-19 10:34 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109150906-alt1
- eu.zip build 2011-09-15 09:06 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109141022-alt1
- eu.zip build 2011-09-14 10:22 UTC

* Wed Sep 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109140814-alt1
- eu.zip build 2011-09-14 08:14 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-eu
- eu.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110813-alt1
- eu_utf8.zip build 2011-08-13
- initial build for ALT Linux Sisyphus
