# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagetype mod
%define packagename book
%define packagversion 1.9.1
%define packagedate 20111009
%define packagemoodleversion 2008081404
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch
%define moodlerequires 2007101512

#Name: %moodlepackagename-%packagetype-%packagename
Name: moodle-mod-book
Version: %packagversion.%packagedate
Release: %branch_release alt2

Summary: This module makes it easy to create multi-page resources with a book-like format
License: %gpl2plus
Group: Networking/WWW

Url: http://docs.moodle.org/19/en/Book_module
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: %moodle_name-base < 2.0
Requires: %moodle_moddir
Requires: %moodle_name-version >= %moodlerequires
Provides: %moodle_name-appfor = 1.9
Provides: %moodle_name-%packagetype-%packagename-version = %packagemoodleversion
Provides: %moodle_name-%packagetype-%packagename-appfor = %moodlerequires
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-base >= 2.0

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses

%description
This module can be used to build complete book-like websites inside of
your Moodle course.

Previously created websites can be imported directly into the Book module.
Books can be printed entirely or by chapter.

The book module allows you to have main chapters and sub chapters,
but it goes no deeper. In other words, sub chapters cannot have their
own sub chapters. This was an intentional decision by the creator of
the book module. He intended this to be a simple resource for teachers
and students.

%prep
%setup

%build

%install
mkdir -p %buildroot%moodle_moddir/%packagename/
cp -rp * %buildroot%moodle_moddir/%packagename/

%files
%moodle_moddir/%packagename/

%changelog
* Wed Mar 21 2012 Aleksey Avdeev <solo@altlinux.ru> 1.9.1.20111009-alt2
- Update cronbuild use

* Thu Jan 12 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.1.20111009-alt1
- repocop cronbuild 20120112. At your service.
- 1.9.1 (20111009)

* Wed Jan 11 2012 Aleksey Avdeev <solo@altlinux.ru> 1.9.0.20110115-alt5
- Add cronbuild use

* Tue Aug 30 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.0.20110115-alt4
- Add Provides: %%moodle_name-%%packagetype-%%packagename-appfor

* Sun Aug 28 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.0.20110115-alt3
- Add Provides: %%moodle_name-appfor

* Thu Aug 25 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.0.20110115-alt2
- Fix requires

* Tue Aug 23 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.0.20110115-alt1
- initial build for ALT Linux Sisyphus
