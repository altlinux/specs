Name: arandr
Version: 0.1.11
Release: alt1

Summary: Screen layout editor for xrandr 1.4 (Another XRandR gui)

Url: http://christian.amsuess.com/tools/arandr/
License: GPLv3
Group: System/X11

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://christian.amsuess.com/tools/arandr/files/%name-%version.tar

BuildArch: noarch


BuildRequires: rpm-build-python3
BuildRequires: python3-module-paste
BuildRequires: python3-module-docutils

%description
Provide a simple visual front end for XRandR 1.4, client
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
%python3_build

%install
%python3_install
%find_lang %name
rm -rv %buildroot/usr/share/locale/zh_Hant/

%files -f %name.lang
%doc NEWS README TODO
%_bindir/%name
%_bindir/unxrandr
%python3_sitelibdir/screenlayout
%python3_sitelibdir/*.egg-info
%_desktopdir/arandr.desktop
%_man1dir/*

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 0.1.11-alt1
- new version 0.1.11 (with rpmrb script)

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt1
- new version 0.1.10 (with rpmrb script)
- switch to python3

* Sat May 14 2016 Terechkov Evgenii <evg@altlinux.org> 0.1.9-alt1
- 0.1.9

* Thu Nov 26 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.8-alt1
- Updated to 0.1.8.

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7.1-alt1.1
- Fixed build

* Sun Mar 10 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.7.1-alt1
- New version 0.1.7.1

* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt1
- new version 0.1.6 (with rpmrb script)

* Sat Jan 14 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Wed Nov 16 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.1.5-1
+ Revision: 731184
- imported package arandr

