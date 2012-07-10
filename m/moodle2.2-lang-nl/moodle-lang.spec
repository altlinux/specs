# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename nl
%define packagversion 2.2.0
%define packagedate 201207100841
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Dutch
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-nl
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
* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207100841-alt1
- repocop cronbuild 20120710. At your service.
- nl.zip build 2012-07-10 08:41 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206282216-alt1
- repocop cronbuild 20120703. At your service.
- nl.zip build 2012-06-28 22:16 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206232109-alt1
- repocop cronbuild 20120626. At your service.
- nl.zip build 2012-06-23 21:09 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191609-alt1
- repocop cronbuild 20120619. At your service.
- nl.zip build 2012-06-19 16:09 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206101946-alt1
- repocop cronbuild 20120612. At your service.
- nl.zip build 2012-06-10 19:46 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206031341-alt1
- repocop cronbuild 20120605. At your service.
- nl.zip build 2012-06-03 13:41 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231817-alt1
- repocop cronbuild 20120529. At your service.
- nl.zip build 2012-05-23 18:17 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205202015-alt1
- repocop cronbuild 20120522. At your service.
- nl.zip build 2012-05-20 20:15 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- nl.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205062035-alt1
- repocop cronbuild 20120508. At your service.
- nl.zip build 2012-05-06 20:35 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204271130-alt1
- repocop cronbuild 20120501. At your service.
- nl.zip build 2012-04-27 11:30 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204241002-alt1
- repocop cronbuild 20120424. At your service.
- nl.zip build 2012-04-24 10:02 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204162047-alt1
- repocop cronbuild 20120417. At your service.
- nl.zip build 2012-04-16 20:47 UTC

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204101400-alt1
- repocop cronbuild 20120410. At your service.
- nl.zip build 2012-04-10 14:00 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204031417-alt1
- repocop cronbuild 20120403. At your service.
- nl.zip build 2012-04-03 14:17 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203140944-alt1
- Rename package to moodle2.2-lang-nl
- nl.zip build 2012-03-14 09:44 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203140945-alt1
- repocop cronbuild 20120320. At your service.
- nl.zip build 2012-03-14 09:45 UTC

* Wed Mar 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203071928-alt1
- repocop cronbuild 20120307. At your service.
- nl.zip build 2012-03-07 19:28 UTC

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202041537-alt1
- repocop cronbuild 20120208. At your service.
- nl.zip build 2012-02-04 15:37 UTC

* Wed Jan 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201250830-alt1
- repocop cronbuild 20120125. At your service.
- nl.zip build 2012-01-25 08:30 UTC

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201092126-alt1
- repocop cronbuild 20120111. At your service.
- nl.zip build 2012-01-09 21:26 UTC

* Wed Dec 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111214. At your service.
- nl.zip build 2011-12-09 16:00 UTC

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112020845-alt1
- repocop cronbuild 20111207. At your service.
- nl.zip build 2011-12-02 08:45 UTC

* Thu Dec 01 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201111292023-alt1
- repocop cronbuild 20111201. At your service.
- nl.zip build 2011-11-29 20:23 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111161404-alt1
- Rename package to moodle2.1-lang-nl
- nl.zip build 2011-11-16 14:04

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
