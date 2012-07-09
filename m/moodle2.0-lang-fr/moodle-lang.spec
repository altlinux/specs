# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename fr
%define packagversion 2.0.0
%define packagedate 201207051203
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define langname French
%define oldpackagename %{packagename}_utf8

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-lang-fr
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
* Mon Jul 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201207051203-alt1
- repocop cronbuild 20120709. At your service.
- fr.zip build 2012-07-05 12:03 UTC

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206201443-alt1
- repocop cronbuild 20120625. At your service.
- fr.zip build 2012-06-20 14:43 UTC

* Mon Jun 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206142032-alt1
- repocop cronbuild 20120618. At your service.
- fr.zip build 2012-06-14 20:32 UTC

* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206071356-alt1
- repocop cronbuild 20120611. At your service.
- fr.zip build 2012-06-07 13:56 UTC

* Mon Jun 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201206031721-alt1
- repocop cronbuild 20120604. At your service.
- fr.zip build 2012-06-03 17:21 UTC

* Mon May 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201205231746-alt1
- repocop cronbuild 20120528. At your service.
- fr.zip build 2012-05-23 17:46 UTC

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204231443-alt1
- repocop cronbuild 20120423. At your service.
- fr.zip build 2012-04-23 14:43 UTC

* Mon Apr 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201204101256-alt1
- repocop cronbuild 20120416. At your service.
- fr.zip build 2012-04-10 12:56 UTC

* Mon Apr 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203271536-alt1
- repocop cronbuild 20120402. At your service.
- fr.zip build 2012-03-27 15:36 UTC

* Mon Mar 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203201952-alt1
- repocop cronbuild 20120326. At your service.
- fr.zip build 2012-03-20 19:52 UTC

* Thu Mar 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201203061934-alt1
- repocop cronbuild 20120308. At your service.
- fr.zip build 2012-03-06 19:34 UTC

* Thu Feb 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202220948-alt1
- repocop cronbuild 20120223. At your service.
- fr.zip build 2012-02-22 09:48 UTC

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202111010-alt1
- repocop cronbuild 20120216. At your service.
- fr.zip build 2012-02-11 10:10 UTC

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201202081935-alt1
- repocop cronbuild 20120209. At your service.
- fr.zip build 2012-02-08 19:35 UTC

* Thu Feb 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201302034-alt1
- repocop cronbuild 20120202. At your service.
- fr.zip build 2012-01-30 20:34 UTC

* Thu Jan 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201072150-alt1
- repocop cronbuild 20120112. At your service.
- fr.zip build 2012-01-07 21:50 UTC

* Thu Jan 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201201042116-alt1
- repocop cronbuild 20120105. At your service.
- fr.zip build 2012-01-04 21:16 UTC

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112192151-alt1
- repocop cronbuild 20111222. At your service.
- fr.zip build 2011-12-19 21:51 UTC

* Thu Dec 15 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112091829-alt1
- repocop cronbuild 20111215. At your service.
- fr.zip build 2011-12-09 18:29 UTC

* Thu Dec 08 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201112081249-alt1
- repocop cronbuild 20111208. At your service.
- fr.zip build 2011-12-08 12:49 UTC

* Fri Nov 25 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111251639-alt1
- repocop cronbuild 20111125. At your service.
- fr.zip build 2011-11-25 16:39 UTC

* Thu Nov 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111232006-alt2
- Fix requires

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111232006-alt1
- repocop cronbuild 20111123. At your service.
- fr.zip build 2011-11-23 20:06 UTC

* Sun Nov 20 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111202140-alt1
- repocop cronbuild 20111120. At your service.
- fr.zip build 2011-11-20 21:40 UTC

* Sat Nov 19 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111191256-alt1
- repocop cronbuild 20111119. At your service.
- fr.zip build 2011-11-19 12:56 UTC

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111181223-alt1
- repocop cronbuild 20111118. At your service.
- fr.zip build 2011-11-18 12:23 UTC

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111151942-alt1
- repocop cronbuild 20111116. At your service.
- fr.zip build 2011-11-15 19:42 UTC

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031917-alt3
- Use moodle2.0-lang-cronbuild for cronbuild

* Sun Nov 06 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201111031917-alt2
- Fix cronbuild use

* Sat Nov 05 2011 Cronbuild Service <cronbuild@altlinux.org> 2.0.0.201111031917-alt1
- repocop cronbuild 20111105. At your service.
- fr.zip build 2011-11-03 19:17 UTC

* Sat Nov 05 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt2
- Update for cronbuild use

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201110121840-alt1
- fr.zip build 2011-10-12 18:40 UTC

* Tue Sep 27 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109231534-alt1
- fr.zip build 2011-09-23 15:34 UTC

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109230935-alt1
- fr.zip build 2011-09-23 09:35 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109221808-alt1
- fr.zip build 2011-09-22 18:08 UTC

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109211530-alt1
- fr.zip build 2011-09-21 15:30 UTC

* Fri Sep 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109161112-alt1
- fr.zip build 2011-09-16 11:12 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109081534-alt1
- fr.zip build 2011-09-08 15:34 UTC

* Thu Sep 08 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201109041828-alt1
- fr.zip build 2011-09-04 18:28 UTC

* Wed Aug 24 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108241508-alt1
- fr.zip build 2011-08-24 15:08 UTC

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108190836-alt1
- fr.zip build 2011-08-19 08:36 UTC

* Tue Aug 16 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108161307-alt1
- fr.zip build 2011-08-16 13:07 UTC

* Mon Aug 15 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108141034-alt1
- fr.zip build 2011-08-14 10:34 UTC

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.201108112300-alt1
- Rename package to moodle2.0-lang-fr
- fr.zip build 2011-08-11 23:00 UTC

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110718-alt1
- fr_utf8.zip build 2011-07-18

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081211
- new build for ALT Linux from cvs
