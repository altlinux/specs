# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename uz
%define packagversion 2.0.0
%define packagedate 201411180646
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname Uzbek
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-uz
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
* Fri Nov 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411180646-alt1
- repocop cronbuild 20141121. At your service.
- uz.zip build 2014-11-18 06:46 UTC

* Fri Nov 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201411100937-alt1
- repocop cronbuild 20141114. At your service.
- uz.zip build 2014-11-10 09:37 UTC

* Fri Oct 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410300547-alt1
- repocop cronbuild 20141031. At your service.
- uz.zip build 2014-10-30 05:47 UTC

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410241107-alt1
- repocop cronbuild 20141024. At your service.
- uz.zip build 2014-10-24 11:07 UTC

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410171017-alt1
- repocop cronbuild 20141018. At your service.
- uz.zip build 2014-10-17 10:17 UTC

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201410101130-alt1
- repocop cronbuild 20141011. At your service.
- uz.zip build 2014-10-10 11:30 UTC

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409300220-alt1
- repocop cronbuild 20141003. At your service.
- uz.zip build 2014-09-30 02:20 UTC

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409200744-alt1
- repocop cronbuild 20140927. At your service.
- uz.zip build 2014-09-20 07:44 UTC

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201409161858-alt1
- repocop cronbuild 20140919. At your service.
- uz.zip build 2014-09-16 18:58 UTC

* Sat Oct 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310260907-alt1
- repocop cronbuild 20131026. At your service.
- uz.zip build 2013-10-26 09:07 UTC

* Sat Oct 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201310090942-alt1
- repocop cronbuild 20131012. At your service.
- uz.zip build 2013-10-09 09:42 UTC

* Wed May 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231549-alt1
- repocop cronbuild 20120523. At your service.
- uz.zip build 2012-05-23 15:49 UTC

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
