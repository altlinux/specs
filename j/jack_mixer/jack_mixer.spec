Name: jack_mixer
Version: 18
Release: alt1
Summary: Jack Audio Mixer
License: GPL-2.0
Group: Sound
Url: https://rdio.space/jackmixer/
Vcs: https://github.com/jack-mixer/jack_mixer

Source0: %name-%version.tar

Requires: libgtk+3-gir

BuildRequires: meson ninja-build
BuildRequires: glib2-devel
BuildRequires: python3-dev
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-pyxdg
BuildRequires: python3-module-Cython
BuildRequires: libjack-devel
BuildRequires: python3-module-docutils
BuildRequires: python3-module-appdirs
BuildRequires: libgtk+3

%description
%name is a GTK+  JACK audio mixer app with a look similar to its hardware
counterpart. It has lot of useful features, apart from being able to mix
multiple JACK audio streams.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.*
%_bindir/*
%python3_sitelibdir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/*

%changelog
* Tue Dec 19 2023 Anton Vyatkin <toni@altlinux.org> 18-alt1
- New version 18

* Wed Apr 14 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 15.1-alt1
- Version 15.1
- buildsystem changed to meson
- python changed to python3

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10-alt1.git20140427
- Version 10

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 9-alt1.1.qa1
- NMU: rebuilt for updated dependencies.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9-alt1.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Egor Glukhov <kaman@altlinux.org> 9-alt1
- Initial build for Sisyphus

