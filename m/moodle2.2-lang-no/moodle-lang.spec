# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename no
%define packagversion 2.2.0
%define packagedate 201206191249
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Norwegian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-no
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
* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206191249-alt1
- repocop cronbuild 20120619. At your service.
- no.zip build 2012-06-19 12:49 UTC

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206121129-alt1
- repocop cronbuild 20120612. At your service.
- no.zip build 2012-06-12 11:29 UTC

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206050632-alt1
- repocop cronbuild 20120605. At your service.
- no.zip build 2012-06-05 06:32 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- no.zip build 2012-05-23 15:49 UTC

* Tue May 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205210658-alt1
- repocop cronbuild 20120522. At your service.
- no.zip build 2012-05-21 06:58 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- no.zip build 2012-05-11 11:00 UTC

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205041400-alt1
- repocop cronbuild 20120508. At your service.
- no.zip build 2012-05-04 14:00 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204300617-alt1
- repocop cronbuild 20120501. At your service.
- no.zip build 2012-04-30 06:17 UTC

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204190725-alt1
- repocop cronbuild 20120424. At your service.
- no.zip build 2012-04-19 07:25 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204161306-alt1
- repocop cronbuild 20120417. At your service.
- no.zip build 2012-04-16 13:06 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203141206-alt1
- Rename package to moodle2.2-lang-no
- no.zip build 2012-03-14 12:06 UTC

* Fri Mar 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203011100-alt1
- repocop cronbuild 20120302. At your service.
- no.zip build 2012-03-01 11:00 UTC

* Fri Feb 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202231327-alt1
- repocop cronbuild 20120224. At your service.
- no.zip build 2012-02-23 13:27 UTC

* Fri Feb 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202041314-alt1
- repocop cronbuild 20120210. At your service.
- no.zip build 2012-02-04 13:14 UTC

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201171357-alt1
- repocop cronbuild 20120120. At your service.
- no.zip build 2012-01-17 13:57 UTC

* Fri Jan 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201031234-alt1
- repocop cronbuild 20120106. At your service.
- no.zip build 2012-01-03 12:34 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- no.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111081406-alt1
- Rename package to moodle2.1-lang-no
- no.zip build 2011-11-08 14:06

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
- no.zip build 2011-10-06 22:30 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109251618-alt1
- no.zip build 2011-09-25 16:18 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- no.zip build 2011-09-21 15:30 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109151708-alt1
- no.zip build 2011-09-15 17:08 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108151942-alt2
- Fix requires

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108151942-alt1
- Rename package to moodle2.0-lang-no
- no.zip build 2011-08-15 19:42 UTC

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110630-alt1
- no_utf8.zip build 20110630
- initial build for ALT Linux Sisyphus
