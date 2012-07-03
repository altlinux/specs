Name: gphotoframe
Version: 1.5.1
Release: alt1

Summary: Gnome Photo Frame
License: GPLv3
Group: Graphics

Url: http://code.google.com/p/gphotoframe/
Source: http://gphotoframe.googlecode.com/files/gphotoframe-%version.tar.gz

%_python_set_noarch
BuildArch: noarch

# Automatically added by buildreq on Sat Jul 16 2011 (-bi)
BuildRequires: gnome-doc-utils intltool python-module-distutils-extra python-module-pyxdg rpm-build-gir time

# Contains macro definition for %%_omfdir
BuildRequires: rpm-build-gnome

%description
Gnome Photo Frame is a photo frame gadget for the GNOME Desktop.

%package gss
Summary: Compatibility package of %name for gnome-screensaver
Group: Graphical desktop/Other
Requires: %name = %version-%release
Requires: gnome-screensaver

%description gss
This package contains scripts and desktop files of %name for
gnome-screensaver compatibility.

%prep
%setup

%build
# Fix installation path
subst 's#lib/gnome-screensaver/gnome-screensaver#libexec/gnome-screensaver#' setup.py
# Fix mode
chmod 755 gphotoframe-screensaver
# Note, separate build and install (with --skip-build) will not install some files.

%install
%python_build_install

mkdir -p %buildroot%gconf_schemasdir
mv %buildroot%_datadir/gconf/schemas/%name.schemas %buildroot%gconf_schemasdir

%find_lang %name

%files -f %name.lang
%_bindir/*
%python_sitelibdir/gphotoframe
%_datadir/gphotoframe
%_desktopdir/*.desktop
%gconf_schemasdir/*
%_datadir/gnome/help/%name/
%_omfdir/%name/
%_iconsdir/hicolor/*/apps/*

%files gss
/usr/libexec/gnome-screensaver/*
%_desktopdir/screensavers/*

%changelog
* Sat Feb 25 2012 Victor Forsiuk <force@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 1.5-alt1
- 1.5

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.1
- Rebuild with Python-2.7

* Sat Jul 16 2011 Victor Forsiuk <force@altlinux.org> 1.4-alt1
- Initial build.
