# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename he
%define packagversion 2.2.0
%define packagedate 201207101258
%define moodlebranch 2.2
%define moodlepackagename %moodle_name%moodlebranch
%define langname Hebrew
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.2-lang-he
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
* Tue Jul 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207101258-alt1
- repocop cronbuild 20120710. At your service.
- he.zip build 2012-07-10 12:58 UTC

* Tue Jul 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201207030834-alt1
- repocop cronbuild 20120703. At your service.
- he.zip build 2012-07-03 08:34 UTC

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206211345-alt1
- repocop cronbuild 20120626. At your service.
- he.zip build 2012-06-21 13:45 UTC

* Tue Jun 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201206180928-alt1
- repocop cronbuild 20120619. At your service.
- he.zip build 2012-06-18 09:28 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205291333-alt1
- repocop cronbuild 20120529. At your service.
- he.zip build 2012-05-29 13:33 UTC

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205150820-alt1
- repocop cronbuild 20120521. At your service.
- he.zip build 2012-05-15 08:20 UTC

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205111100-alt1
- repocop cronbuild 20120515. At your service.
- he.zip build 2012-05-11 11:00 UTC

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204301327-alt1
- repocop cronbuild 20120501. At your service.
- he.zip build 2012-04-30 13:27 UTC

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204151134-alt1
- repocop cronbuild 20120417. At your service.
- he.zip build 2012-04-15 11:34 UTC

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201204021157-alt1
- repocop cronbuild 20120403. At your service.
- he.zip build 2012-04-02 11:57 UTC

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203221535-alt1
- repocop cronbuild 20120327. At your service.
- he.zip build 2012-03-22 15:35 UTC

* Tue Mar 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201203191429-alt1
- repocop cronbuild 20120320. At your service.
- he.zip build 2012-03-19 14:29 UTC

* Mon Mar 19 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201203181546-alt1
- Rename package to moodle2.2-lang-he
- he.zip build 2012-03-18 15:46 UTC

* Tue Mar 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201203060922-alt1
- repocop cronbuild 20120306. At your service.
- he.zip build 2012-03-06 09:22 UTC

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202161217-alt1
- repocop cronbuild 20120221. At your service.
- he.zip build 2012-02-16 12:17 UTC

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202141443-alt1
- repocop cronbuild 20120214. At your service.
- he.zip build 2012-02-14 14:43 UTC

* Tue Feb 07 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201202061439-alt1
- repocop cronbuild 20120207. At your service.
- he.zip build 2012-02-06 14:39 UTC

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201261241-alt1
- repocop cronbuild 20120131. At your service.
- he.zip build 2012-01-26 12:41 UTC

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201191327-alt1
- repocop cronbuild 20120124. At your service.
- he.zip build 2012-01-19 13:27 UTC

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201201171128-alt1
- repocop cronbuild 20120117. At your service.
- he.zip build 2012-01-17 11:28 UTC

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112190920-alt1
- repocop cronbuild 20111220. At your service.
- he.zip build 2011-12-19 09:20 UTC

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111213. At your service.
- he.zip build 2011-12-09 16:00 UTC

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112061435-alt1
- repocop cronbuild 20111206. At your service.
- he.zip build 2011-12-06 14:35 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201111241405-alt1
- Rename package to moodle2.1-lang-he
- he.zip build 2011-11-24 14:05

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111201348-alt2
- Fix requires

* Sun Nov 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111201348-alt1
- repocop cronbuild 20111120. At your service.
- he.zip build 2011-11-20 13:48 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111101425-alt1
- repocop cronbuild 20111116. At your service.
- he.zip build 2011-11-10 14:25 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110062230-alt1
- he.zip build 2011-10-06 22:30 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- he.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt2
- Fix requires

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-he
- he.zip build 2011-08-11 23:00 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110804-alt1
- he_utf8.zip build 2011-08-04
- initial build for ALT Linux Sisyphus
