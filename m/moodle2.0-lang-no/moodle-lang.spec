# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename no
%define packagversion 2.0.0
%define packagedate 201602120619
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Norwegian
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-no
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
* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201602120619-alt1
- repocop cronbuild 20160214. At your service.
- no.zip build 2016-02-12 06:19 UTC

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201511082220-alt1
- repocop cronbuild 20151109. At your service.
- no.zip build 2015-11-08 22:20 UTC

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201508071011-alt1
- repocop cronbuild 20150823. At your service.
- no.zip build 2015-08-07 10:11 UTC

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507122042-alt1
- repocop cronbuild 20150716. At your service.
- no.zip build 2015-07-12 20:42 UTC

* Thu Jul 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201507010757-alt1
- repocop cronbuild 20150702. At your service.
- no.zip build 2015-07-01 07:57 UTC

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201504140653-alt1
- repocop cronbuild 20150417. At your service.
- no.zip build 2015-04-14 06:53 UTC

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412050855-alt1
- repocop cronbuild 20141211. At your service.
- no.zip build 2014-12-05 08:55 UTC

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201412041127-alt1
- repocop cronbuild 20141205. At your service.
- no.zip build 2014-12-04 11:27 UTC

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201403291455-alt1
- repocop cronbuild 20140404. At your service.
- no.zip build 2014-03-29 14:55 UTC

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402241422-alt1
- repocop cronbuild 20140301. At your service.
- no.zip build 2014-02-24 14:22 UTC

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201402121641-alt1
- repocop cronbuild 20140215. At your service.
- no.zip build 2014-02-12 16:41 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310101252-alt1
- repocop cronbuild 20131011. At your service.
- no.zip build 2013-10-10 12:52 UTC

* Fri Sep 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201309031344-alt1
- repocop cronbuild 20130906. At your service.
- no.zip build 2013-09-03 13:44 UTC

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201308231151-alt1
- repocop cronbuild 20130830. At your service.
- no.zip build 2013-08-23 11:51 UTC

* Fri May 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201305211304-alt1
- repocop cronbuild 20130524. At your service.
- no.zip build 2013-05-21 13:04 UTC

* Tue Mar 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201303191348-alt1
- repocop cronbuild 20130319. At your service.
- no.zip build 2013-03-19 13:48 UTC

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201302221112-alt1
- repocop cronbuild 20130225. At your service.
- no.zip build 2013-02-22 11:12 UTC

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301261539-alt1
- repocop cronbuild 20130128. At your service.
- no.zip build 2013-01-26 15:39 UTC

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301112304-alt1
- repocop cronbuild 20130114. At your service.
- no.zip build 2013-01-11 23:04 UTC

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201301021341-alt1
- repocop cronbuild 20130107. At your service.
- no.zip build 2013-01-02 13:41 UTC

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201211150840-alt1
- repocop cronbuild 20121119. At your service.
- no.zip build 2012-11-15 08:40 UTC

* Mon Oct 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201210081253-alt1
- repocop cronbuild 20121015. At your service.
- no.zip build 2012-10-08 12:53 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231549-alt1
- repocop cronbuild 20120528. At your service.
- no.zip build 2012-05-23 15:49 UTC

* Thu Feb 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202231327-alt1
- repocop cronbuild 20120223. At your service.
- no.zip build 2012-02-23 13:27 UTC

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
