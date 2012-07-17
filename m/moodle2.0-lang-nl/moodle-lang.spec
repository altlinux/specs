# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename nl
%define packagversion 2.0.0
%define packagedate 201207100841
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Dutch
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-nl
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
* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207100841-alt1
- repocop cronbuild 20120717. At your service.
- nl.zip build 2012-07-10 08:41 UTC

* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207091507-alt1
- repocop cronbuild 20120710. At your service.
- nl.zip build 2012-07-09 15:07 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206290713-alt1
- repocop cronbuild 20120703. At your service.
- nl.zip build 2012-06-29 07:13 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206171818-alt1
- repocop cronbuild 20120618. At your service.
- nl.zip build 2012-06-17 18:18 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206101949-alt1
- repocop cronbuild 20120612. At your service.
- nl.zip build 2012-06-10 19:49 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206031027-alt1
- repocop cronbuild 20120604. At your service.
- nl.zip build 2012-06-03 10:27 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231549-alt1
- repocop cronbuild 20120528. At your service.
- nl.zip build 2012-05-23 15:49 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205202016-alt1
- repocop cronbuild 20120521. At your service.
- nl.zip build 2012-05-20 20:16 UTC

* Mon May 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205102039-alt1
- repocop cronbuild 20120514. At your service.
- nl.zip build 2012-05-10 20:39 UTC

* Mon May 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205031134-alt1
- repocop cronbuild 20120507. At your service.
- nl.zip build 2012-05-03 11:34 UTC

* Mon Apr 30 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204241002-alt1
- repocop cronbuild 20120430. At your service.
- nl.zip build 2012-04-24 10:02 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204221206-alt1
- repocop cronbuild 20120423. At your service.
- nl.zip build 2012-04-22 12:06 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204162047-alt1
- repocop cronbuild 20120416. At your service.
- nl.zip build 2012-04-16 20:47 UTC

* Mon Apr 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204051550-alt1
- repocop cronbuild 20120409. At your service.
- nl.zip build 2012-04-05 15:50 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203281921-alt1
- repocop cronbuild 20120402. At your service.
- nl.zip build 2012-03-28 19:21 UTC

* Mon Mar 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203140945-alt1
- repocop cronbuild 20120319. At your service.
- nl.zip build 2012-03-14 09:45 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203071928-alt1
- repocop cronbuild 20120307. At your service.
- nl.zip build 2012-03-07 19:28 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202020910-alt1
- repocop cronbuild 20120208. At your service.
- nl.zip build 2012-02-02 09:10 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201250830-alt1
- repocop cronbuild 20120125. At your service.
- nl.zip build 2012-01-25 08:30 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201092126-alt1
- repocop cronbuild 20120111. At your service.
- nl.zip build 2012-01-09 21:26 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112020846-alt1
- repocop cronbuild 20111207. At your service.
- nl.zip build 2011-12-02 08:46 UTC

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111290736-alt1
- repocop cronbuild 20111130. At your service.
- nl.zip build 2011-11-29 07:36 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111161119-alt2
- Fix requires

* Thu Nov 17 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111161119-alt1
- repocop cronbuild 20111117. At your service.
- nl.zip build 2011-11-16 11:19 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111141719-alt1
- repocop cronbuild 20111116. At your service.
- nl.zip build 2011-11-14 17:19 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111102028-alt2
- Use moodle2.0-lang-cronbuild for cronbuild

* Sat Nov 12 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111102028-alt1
- repocop cronbuild 20111112. At your service.
- nl.zip build 2011-11-10 20:28 UTC

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110260752-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201110260752-alt1
- repocop cronbuild 20111105. At your service.
- nl.zip build 2011-10-26 07:52 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- nl.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- nl.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109071908-alt1
- nl.zip build 2011-09-07 19:08 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Fix package version

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.20110810-alt1
- Rename package to moodle2.0-lang-nl
- nl.zip build 2011-08-11 23:00 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110802-alt1
- nl_utf8.zip build 2011-08-02
- initial build for ALT Linux Sisyphus
