Name: arandr
Version: 0.1.5
Release: alt1

Summary: Screen layout editor for xrandr 1.2 (Another XRandR gui)

Url: http://christian.amsuess.com/tools/arandr/
License: GPLv3
Group: System/X11

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://christian.amsuess.com/tools/arandr/files/%name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Sat Jan 14 2012
# optimized out: python-base python-devel python-module-docutils python-module-peak python-modules python-modules-compiler python-modules-encodings
BuildRequires: python-module-mwlib python-module-paste

%description
Provide a simple visual front end for XRandR 1.2, client
side X only (no xorg.conf involved, no pre-1.2 options).

Features

* Full controll over positioning (instead of plain "left of") with
  edge snapping

* Saving configurations as executable shell scripts (configurations
  can be loaded without using this program)

* Configuration files can be edited to include additional payload
  (like xsetwacom commands tablet PC users need when rotating), which
  is preserved when editing

* Metacity keybinding integration:

* Saved configurations can be bound to arbitrary keys via metacity
  custom commands.

* Several layouts can be bound to one key; they are cycled
  through. (Useful for "rotate" buttons on tablet PCs.)

* Main widget separated from packaged application (to facilitate
  integration with existing solutions)

%prep
%setup

%build
%python_build

%install
%python_install
%find_lang %name

%files -f %name.lang
%doc NEWS README TODO
%_bindir/%name
%_bindir/unxrandr
%python_sitelibdir/screenlayout
%python_sitelibdir/*.egg-info
%_desktopdir/arandr.desktop
%_man1dir/*

%changelog
* Sat Jan 14 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Wed Nov 16 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.1.5-1
+ Revision: 731184
- imported package arandr

