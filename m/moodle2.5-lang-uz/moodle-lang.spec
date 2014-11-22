# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename uz
%define packagversion 2.5.0
%define packagedate 201411180646
%define moodlebranch 2.5
%define moodlepackagename %moodle_name%moodlebranch
%define langname Uzbek
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.5-lang-uz
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl3plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.5
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 2.5
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
* Sat Nov 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411180646-alt1
- repocop cronbuild 20141122. At your service.
- uz.zip build 2014-11-18 06:46 UTC

* Sat Nov 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201411100937-alt1
- repocop cronbuild 20141115. At your service.
- uz.zip build 2014-11-10 09:37 UTC

* Sat Nov 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410300547-alt1
- repocop cronbuild 20141101. At your service.
- uz.zip build 2014-10-30 05:47 UTC

* Sat Oct 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410241107-alt1
- repocop cronbuild 20141025. At your service.
- uz.zip build 2014-10-24 11:07 UTC

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410171017-alt1
- repocop cronbuild 20141018. At your service.
- uz.zip build 2014-10-17 10:17 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201410101130-alt1
- repocop cronbuild 20141011. At your service.
- uz.zip build 2014-10-10 11:30 UTC

* Sat Oct 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409300220-alt1
- repocop cronbuild 20141004. At your service.
- uz.zip build 2014-09-30 02:20 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409200744-alt1
- repocop cronbuild 20140927. At your service.
- uz.zip build 2014-09-20 07:44 UTC

* Sat Sep 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409161858-alt1
- repocop cronbuild 20140920. At your service.
- uz.zip build 2014-09-16 18:58 UTC

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201409120552-alt1
- repocop cronbuild 20140913. At your service.
- uz.zip build 2014-09-12 05:52 UTC

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310260907-alt1
- repocop cronbuild 20131101. At your service.
- uz.zip build 2013-10-26 09:07 UTC

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201310090941-alt1
- repocop cronbuild 20131011. At your service.
- uz.zip build 2013-10-09 09:41 UTC

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.5.0.201306140511-alt1
- repocop cronbuild 20130615. At your service.
- uz.zip build 2013-06-14 05:11 UTC

* Fri May 31 2013 Aleksey Avdeev <solo@altlinux.ru> 2.5.0.201304250002-alt1
- Rename package to moodle2.5-lang-uz
- uz.zip build 2013-04-25 00:02 UTC

* Thu Apr 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.0.201301111216-alt1
- Rename package to moodle2.4-lang-uz
- uz.zip build 2013-01-11 12:16 UTC

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201211010700-alt1
- repocop cronbuild 20121105. At your service.
- uz.zip build 2012-11-01 07:00 UTC

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.2.0.201205231549-alt1
- repocop cronbuild 20120529. At your service.
- uz.zip build 2012-05-23 15:49 UTC

* Tue Mar 20 2012 Aleksey Avdeev <solo@altlinux.ru> 2.2.0.201112091600-alt1
- Rename package to moodle2.2-lang-uz
- uz.zip build 2011-12-09 16:00 UTC

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 2.1.0.201112091600-alt1
- repocop cronbuild 20111209. At your service.
- uz.zip build 2011-12-09 16:00 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1.0.201109211530-alt1
- Rename package to moodle2.1-lang-uz
- uz.zip build 2011-09-21 15:30 UTC

* Fri Nov 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt6
- Fix requires

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt5
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt4
- Fix cronbuild use

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt2
- Update for cronbuild use

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- uz.zip build 2011-09-21 15:30 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt2
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201103031730-alt1
- Rename package to moodle2.0-lang-uz
- uz.zip build 2011-03-03 17:30 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100526-alt1
- uz_utf8.zip build 2010-05-26

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100526
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081111
- new build for ALT Linux from cvs
