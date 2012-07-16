# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype lang
%define packagename no_utf8
%define packagversion 1.9.10
%define packagedate 20120714
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define langname Norwegian

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-lang-no_utf8
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
* Mon Jul 16 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120714-alt1
- repocop cronbuild 20120716. At your service.
- no_utf8.zip build 2012-07-14

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20120205-alt1
- repocop cronbuild 20120209. At your service.
- no_utf8.zip build 2012-02-05

* Thu Jan 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.10.20111227-alt1
- repocop cronbuild 20120105. At your service.
- no_utf8.zip build 2011-12-27

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111025-alt5
- Use moodle-lang-cronbuild for cronbuild

* Mon Nov 07 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111025-alt4
- Fix cronbuild use

* Fri Nov 04 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111025-alt3
- Fix cronbuild use

* Thu Nov 03 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111025-alt2
- Update for cronbuild use

* Tue Oct 25 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111025-alt1
- no_utf8.zip build 2011-10-25

* Sat Oct 22 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20111021-alt1
- no_utf8.zip build 2011-10-21

* Thu Sep 22 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110921-alt1
- no_utf8.zip build 2011-09-21

* Fri Sep 09 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110630-alt2
- Fix requires

* Thu Aug 18 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.10.20110630-alt1
- no_utf8.zip build 20110630
- initial build for ALT Linux Sisyphus
