%define _libexecdir %_prefix/libexec

Name: gphotoframe
Version: 2.0.1
Release: alt1

Summary: Gnome Photo Frame
License: GPLv3
Group: Graphics

Url: http://code.google.com/p/%name/
Source: http://gphotoframe.googlecode.com/files/%name-%version-b1.tar.gz

%_python_set_noarch
BuildArch: noarch

BuildRequires: rpm-build-gnome rpm-build-gir intltool gnome-doc-utils
BuildRequires: python-module-distutils-extra python-module-pyxdg

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
%setup -n %name-%version-b1

%build
# Fix installation path
subst 's#lib/gnome-screensaver/gnome-screensaver#libexec/gnome-screensaver#' setup.py
# Fix mode
chmod 755 gphotoframe-screensaver
# Note, separate build and install (with --skip-build) will not install some files.

%install
%python_build_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%python_sitelibdir/gphotoframe/
%_datadir/%name/
%_desktopdir/*.desktop
%_datadir/glib-2.0/schemas/com.googlecode.%name.gschema.xml
%_iconsdir/hicolor/*/apps/*

%files gss
%_libexecdir/gnome-screensaver/%name-screensaver
%_desktopdir/screensavers/%name-screensaver.desktop

%changelog
* Sat Nov 29 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1-b1

* Sun Oct 26 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- 2.0

* Sat Feb 25 2012 Victor Forsiuk <force@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 1.5-alt1
- 1.5

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.1
- Rebuild with Python-2.7

* Sat Jul 16 2011 Victor Forsiuk <force@altlinux.org> 1.4-alt1
- Initial build.
