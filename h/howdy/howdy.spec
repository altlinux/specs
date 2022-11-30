Name: howdy
Version: 3.0.0
Release: alt0.beta1.git943f1e1
Summary: Windows Hello style authentication

License: MIT
Group: System/Kernel and hardware
Url: https://github.com/boltgolt/howdy

# commit 943f1e14e2c05159c22fb5176db377c0c1610bba
Source: %url/archive/%version/%name-%version.tar.gz
Source1: https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2
Source2: https://github.com/davisking/dlib-models/raw/master/mmod_human_face_detector.dat.bz2
Source3: https://github.com/davisking/dlib-models/raw/master/shape_predictor_5_face_landmarks.dat.bz2

BuildRequires: gcc-c++ rpm-build-python3 meson rpm-build-ninja cmake gettext-tools
BuildRequires: libinih-devel libevdev-devel libpam0-devel
Requires: python3-module-opencv python3-module-h5py python3-module-PAM

%add_python3_req_skip i18n

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

%description pam
The package provides PAM module for %name.

%package gtk
Summary: Windows Hello style authentication - gtk interface
Group: System/Kernel and hardware
BuildArch: noarch

%description gtk
The package provides gtk interface for %name.

%prep
%setup
cp -a %SOURCE1 %SOURCE2 %SOURCE3 .
bzip2 -dv *.bz2
sed -i 's|/lib/security|/%_lib/security|' \
  howdy/src/pam/meson.build
sed -i 's|/usr/bin/env python3|%__python3|' \
  howdy-gtk/src/init.py \
  howdy/src/cli.py

%build
pushd howdy/src/pam
%meson
%meson_build
popd

%install
pushd howdy/src/pam
%meson_install
popd

mkdir -p %buildroot/%_lib/security/howdy
cp -a howdy/src/* %buildroot/%_lib/security/howdy
mkdir -p %buildroot/usr/libexec/howdy-gtk
cp -a howdy-gtk/src/* %buildroot/usr/libexec/howdy-gtk
cp -a dlib_face_recognition_resnet_model_v1.dat %buildroot/%_lib/security/howdy/dlib-data/
cp -a mmod_human_face_detector.dat %buildroot/%_lib/security/howdy/dlib-data/
cp -a shape_predictor_5_face_landmarks.dat %buildroot/%_lib/security/howdy/dlib-data/
mkdir -p %buildroot/usr/bin
ln -s /%_lib/security/howdy/cli.py %buildroot%_bindir/howdy
ln -s /usr/libexec/howdy-gtk/init.py %buildroot%_bindir/howdy-gtk
chmod +x %buildroot/%_lib/security/howdy/cli.py
mkdir -p %buildroot%_datadir/bash-completion/completions
cp -a howdy/src/autocomplete/howdy %buildroot%_datadir/bash-completion/completions/howdy
mkdir -p %buildroot%_man1dir
cp -a howdy/debian/howdy.1 %buildroot%_man1dir/
# already built
rm -rf %buildroot/%_lib/security/howdy/{dlib-data,pam}

%files
%doc LICENSE README.md
%_bindir/howdy
%_datadir/bash-completion/completions/howdy
%config(noreplace) /%_lib/security/howdy/config.ini
/%_lib/security/howdy/
%_man1dir/howdy*

%files pam
/%_lib/security/pam_howdy.so

%files gtk
%_bindir/howdy-gtk
/usr/libexec/howdy-gtk/

%changelog
* Wed Nov 30 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt0.beta1.git943f1e1
- Initial build for ALT Sisyphus (thanks archlinux for the spec) (ALT #44491).
