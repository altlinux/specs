# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename fr_utf8
%define packagversion 1.9.10
%define packagedate 20120607
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define langname French

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-lang-fr_utf8
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: Moodle %langname localization
License: %gpl2plus
Group: Networking/WWW

Url: http://lang.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base < 2.0
Requires: %moodle_langdir
Provides: %moodle_name-appfor = 1.9
Provides: %moodle_name-%packagetype-%packagename-version = %packagedate
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-base >= 2.0

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
* Mon Jun 11 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120607-alt1
- repocop cronbuild 20120611. At your service.
- fr_utf8.zip build 2012-06-07

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120420-alt1
- repocop cronbuild 20120423. At your service.
- fr_utf8.zip build 2012-04-20

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120209-alt1
- repocop cronbuild 20120215. At your service.
- fr_utf8.zip build 2012-02-09

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120206-alt1
- repocop cronbuild 20120208. At your service.
- fr_utf8.zip build 2012-02-06

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120126-alt1
- repocop cronbuild 20120201. At your service.
- fr_utf8.zip build 2012-01-26

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110813-alt6
- Use moodle-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110813-alt5
- Fix cronbuild use

* Fri Nov 04 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110813-alt4
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110813-alt3
- Update for cronbuild use

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110813-alt2
- Fix requires

* Sat Aug 13 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110813-alt1
- fr_utf8.zip build 2011-08-13

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110718-alt1
- fr_utf8.zip build 2011-07-18

* Tue Nov 16 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081211
- new build for ALT Linux from cvs
