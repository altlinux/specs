# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename ru_utf8
%define packagversion 1.9.10
%define packagedate 20100617
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define langname Russian

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-lang-ru_utf8
Version: %packagversion.%packagedate
Release: %branch_release alt6

Summary: Moodle %langname localozation
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
* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100617-alt6
- Use moodle-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100617-alt5
- Fix cronbuild use

* Fri Nov 04 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100617-alt4
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100617-alt3
- Update for cronbuild use

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100617-alt2
- Fix requires

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20100617-alt1
- ru_utf8.zip build 2010-06-17

* Tue Nov 23 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt2.cvs20100617
- inheritance fixed

* Thu Nov 18 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20100617
- new version

* Tue Oct 27 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt2.cvs20091014
- rebuild with new Moodle

* Mon Oct 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20091014
- new build from cvs

* Sun Jul 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20090720
- new build from cvs

* Sat Apr 18 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.4-alt1.cvs20090416
- new build from cvs

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081106
- new build from cvs

* Mon Oct 13 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080926
- new build from cvs

* Mon Sep 08 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080802
- add build requires on rpm-build-webserver-common
- new build from cvs

* Thu Jun 26 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt2.cvs20080526
- change path moodle location

* Mon Jun 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.cvs20080526
- new build for ALT Linux
