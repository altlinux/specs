%define _unpackaged_files_terminate_build 1

Name: howdy
Version: 3.0.0
Release: alt10.beta1.gitc5b1766
Summary: Windows Hello style authentication

License: MIT
Group: System/Kernel and hardware
Url: https://github.com/boltgolt/howdy

# dlib builds successfully but doesn't work properly for ppc
# https://github.com/davisking/dlib/issues/2711
ExcludeArch: ppc64le

Source: %url/archive/%version/%name-%version.tar.gz
Source1: https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2
Source2: https://github.com/davisking/dlib-models/raw/master/mmod_human_face_detector.dat.bz2
Source3: https://github.com/davisking/dlib-models/raw/master/shape_predictor_5_face_landmarks.dat.bz2
# There are no translations in upstream yet
# taken from https://crowdin.com/project/howdy
Source4: po.tar.gz
Source5: po-gtk.tar.gz

Patch: howdy-3.0.0-alt-fix-the-dublicates-in-the-man.patch
Patch3: howdy-pull-692-1.patch
Patch4: howdy-pull-692-2.patch
Patch5: howdy-pull-692-3.patch
Patch7: enable-detection-notice.patch
Patch8: pass-env-to-pkexec.patch
Patch9: pr853-connect-to-signals-of-the-shown-window.patch
Patch10: pr855-segfault-adding-a-model.patch
Patch11: pr857-fix-things-regarding-translations.patch
Patch12: integrate-translations.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-pam0

BuildRequires: gcc-c++ rpm-build-python3 meson rpm-build-ninja cmake gettext-tools
BuildRequires: libinih-devel libevdev-devel libpam0-devel

Requires: %name-pam = %EVR
Requires: libgtk+3-gir

%add_python3_path %_prefix/libexec/howdy/
%add_python3_path %_prefix/libexec/howdy-gtk/

%description
Howdy provides Windows Hello style authentication for Linux.
Use your built-in IR emitters and camera in combination
with facial recognition to prove who you are.

Using the central authentication system (PAM),
this works everywhere you would otherwise need
your password: Login, lock screen, sudo, su, etc.

%package pam
Summary: PAM module for howdy
Group: System/Base
Requires: %name = %EVR

%description pam
The package provides PAM module for %name.

%package gtk
Summary: Windows Hello style authentication - gtk interface
Group: System/Kernel and hardware
Requires: %name = %EVR

%description gtk
The package provides gtk interface for %name.

%prep
%setup -a 4 -a 5
%patch -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
cp -a %SOURCE1 %SOURCE2 %SOURCE3 .
bzip2 -dv *.bz2
sed -i 's|/usr/bin/env python3|%__python3|' \
  howdy-gtk/src/init.py \
  howdy/src/cli.py \
  howdy/src/compare.py
sed -i 's|/bin/nano|%_bindir/nano|' \
  howdy/src/cli/config.py

%build
%meson \
    -Dpam_dir=%_pam_modules_dir \
    -Dpy_sources_dir=%_prefix/libexec
%meson_build

%install
%meson_install

%find_lang %name
%find_lang %name-gtk

#dlib models
cp -a *.dat %buildroot%_datadir/dlib-data/

%files -f %name.lang
%doc LICENSE README.md
%config(noreplace) %_sysconfdir/howdy/config.ini
%_bindir/howdy
%_prefix/libexec/howdy/
%_datadir/howdy/
%_datadir/bash-completion/completions/howdy
%_datadir/dlib-data/
%_man1dir/howdy*

%files pam
%_pam_modules_dir/pam_howdy.so

%files gtk -f %name-gtk.lang
%_bindir/howdy-gtk
%_prefix/libexec/howdy-gtk/
%_datadir/howdy-gtk/

%changelog
* Fri Nov 17 2023 Anton Golubev <golubevan@altlinux.org> 3.0.0-alt10.beta1.gitc5b1766
- actually add translations

* Wed Nov 15 2023 Anton Golubev <golubevan@altlinux.org> 3.0.0-alt9.beta1.gitc5b1766
- add translations

* Tue Nov 07 2023 Anton Golubev <golubevan@altlinux.org> 3.0.0-alt8.beta1.gitc5b1766
- remove 'fix-startup' patch (ALT #46340)
- use pkexec in advance to pass some env values (ALT #44606)
- fix segfault when adding a model via howdy-gtk (ALT #46339)
- fixup window destroy signals
- explicit requires libgtk+3-gir

* Mon Sep 25 2023 Anton Golubev <golubevan@altlinux.org> 3.0.0-alt7.beta1.gitc5b1766
- more recent version including necessary changes/fixes:
  * do not show a message if the face model is not found
  * show a message if the user could not be recognized
  * show prompt if face model found (and enabled option detetion_notice)
  * ensure Model ID is unique
- update patches
- enable detection_notice by default via patch
- explicitly exclude ppc64le
- adapt spec to changes in build scripts

* Mon Jan 09 2023 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt6.beta1.git943f1e1
- Fixed howdy-gtk startup again instead howdy-gtk-auth (ALT #44775).

* Thu Dec 22 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt5.beta1.git943f1e1
- Fixed the dublicates in the man file (ALT #44609).
- Applied some improvements by community.
- Fixed howdy-gtk startup again (ALT #44606).

* Wed Dec 21 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt4.beta1.git943f1e1
- Fixed configuration file detection (ALT #44607).

* Thu Dec 08 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt3.beta1.git943f1e1
- Fixed howdy-gtk startup.

* Thu Dec 08 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt2.beta1.git943f1e1
- Fixed howdy startup (ALT #44558).

* Thu Dec 01 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt1.beta1.git943f1e1
- Packed source files.

* Wed Nov 30 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt0.beta1.git943f1e1
- Initial build for ALT Sisyphus (thanks archlinux for the spec) (ALT #44491).
