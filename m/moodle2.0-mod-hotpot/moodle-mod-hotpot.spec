# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype mod
%define packagename hotpot
%define packagversion 3.0.31
%define packagedate 2010080331
%define packagemoodleversion %packagedate
%define moodlebranch 2.0
%define moodlepackagename %moodle_name%moodlebranch
%define moodlerequires 2010112400

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle2.0-mod-hotpot
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: HotPot module for Moodle
License: %gpl3plus
Group: Networking/WWW

Url: http://docs.moodle.org/20/en/Hotpot_module
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source0: %name-mod-%version.tar
Source1: %name-qformat-%version.tar

Requires: %moodle_name-base >= 2.0
Requires: %moodle_moddir
Requires: %moodle_questionformatdir
Requires: %moodle_name-version >= %moodlerequires
Provides: %moodle_name-appfor = 2.0
Provides: %moodle_name-%packagetype-%packagename-version = %packagemoodleversion
Provides: %moodle_name-%packagetype-%packagename-appfor = %moodlerequires
Conflicts: %moodle_name-%packagetype-%packagename-version < %packagemoodleversion

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle >= 2.3
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses

%description
The Hotpot activity module allows teachers to administer Hot Potatoes
and TexToys quizzes via Moodle. These quizzes are created on
the teacher's computer and then uploaded to the Moodle course. After
students have attempted the quizzes, a number of reports are available
which show how individual questions were answered and some statistical
trends in the scores.

%prep
%setup -c -n %name-%version
%setup -T -D -a 1 -n %name-%version

%build

%install
mkdir -p %buildroot%moodle_moddir/%packagename/
cp -rp mod/* %buildroot%moodle_moddir/%packagename/
mkdir -p %buildroot%moodle_questionformatdir/%packagename/
cp -rp qformat/* %buildroot%moodle_questionformatdir/%packagename/

%files
%moodle_moddir/%packagename/
%moodle_questionformatdir/%packagename/

%changelog
* Wed Mar 21 2012 Aleksey Avdeev <solo@altlinux.ru> 3.0.31.2010080331-alt1
- 3.0.31 (Build: 2010080331)
- Add Conflicts: moodle-mod-hotpot-version < %%packagemoodleversion

* Tue Sep 06 2011 Aleksey Avdeev <solo@altlinux.ru> 3.0.25.2010080325-alt1
- initial build for ALT Linux Sisyphus
