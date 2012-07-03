# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype mod
%define packagename journal
%define packagversion 1.3.0
%define packagedate 2012041900
%define packagemoodleversion 2012041900
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define moodlerequires 2010112400

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-mod-journal
Version: %packagversion.%packagedate
Release: %branch_release alt1
Epoch: 1

Summary: Module Journal for Moodle
License: %gpl3plus
Group: Networking/WWW

Url: http://docs.moodle.org/20/en/Journal_module
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base >= 2.0
Requires: %moodle_moddir
Requires: %moodle_name-version >= %moodlerequires
Provides: %moodle_name-appfor = 2.0
Provides: %moodle_name-%packagetype-%packagename-version = %packagemoodleversion
Provides: %moodle_name-%packagetype-%packagename-appfor = %moodlerequires
Conflicts: %moodle_name-%packagetype-%packagename-version < %packagemoodleversion

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses

%description
This module allows a teacher to ask students to reflect on a particular
topic. The students can edit and refine their answer over time.

%prep
%setup

%build

%install
mkdir -p %buildroot%moodle_moddir/%packagename/
cp -rp * %buildroot%moodle_moddir/%packagename/

%files
%moodle_moddir/%packagename/

%changelog
* Thu May 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1:1.3.0.2012041900-alt1
- repocop cronbuild 20120510. At your service.
- 1.3 (Build: 2012041900)

* Wed Mar 21 2012 Aleksey Avdeev <solo@altlinux.ru> 1:1.2.0.2012032001-alt1
- repocop cronbuild 20120321. At your service.
- 1.2 (Build: 2012032001)

* Thu Jan 12 2012 Aleksey Avdeev <solo@altlinux.ru> 1:1.1.0.2011110500-alt1
- Fix package version
- Fix cronbuild use

* Tue Dec 13 2011 Cronbuild Service <cronbuild@altlinux.org> 1:1.1.0.2011102100-alt1
- repocop cronbuild 20111213. At your service.
- 1.1 (Build: 2011110500)

* Tue Dec 13 2011 Aleksey Avdeev <solo@altlinux.ru> 1:1.0.0.2011102100-alt4
- Fix cronbuild use

* Sun Dec 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1:1.0.0.2011102100-alt3
- Fix cronbuild use

* Sat Dec 10 2011 Aleksey Avdeev <solo@altlinux.ru> 1:1.0.0.2011102100-alt2
- Fix cronbuild use

* Fri Dec 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1:1.0.0.2011102100-alt1
- 1.0 (Build: 2011102100)

* Tue Aug 30 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.2011072100-alt3
- Add provides: %%moodle_name-%%packagetype-%%packagename-appfor

* Sun Aug 28 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.2011072100-alt2
- Add provides: %%moodle_name-appfor

* Thu Aug 25 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.0.2011072100-alt1
- initial build for ALT Linux Sisyphus
