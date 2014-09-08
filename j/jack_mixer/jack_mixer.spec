Name: jack_mixer
Version: 10
Release: alt1.git20140427
Summary: Jack Audio Mixer
License: GPLv2+
Group: Sound
Url: http://home.gna.org/jackmixer/
# git://repo.or.cz/jack_mixer.git
Source0: %name-%version.tar
Requires: python-module-pygnome-gconf
BuildPreReq: libGConf-devel
BuildRequires(pre): rpm-build-gnome
BuildRequires: GConf glib2-devel jackit-devel python-devel
BuildRequires: python-module-fpconst python-module-pygtk
BuildRequires: python-modules-encodings

%description
%name is a GTK+  JACK audio mixer app with a look similar to its hardware
counterpart. It has lot of useful features, apart from being able to mix
multiple JACK audio streams.

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std pythondir=%python_sitelibdir
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%files
%config %gconf_schemasdir/%name.schemas
%doc AUTHORS NEWS README
%_bindir/*
%python_sitelibdir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name

%changelog
* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10-alt1.git20140427
- Version 10

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 9-alt1.1.qa1
- NMU: rebuilt for updated dependencies.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9-alt1.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Egor Glukhov <kaman@altlinux.org> 9-alt1
- Initial build for Sisyphus

