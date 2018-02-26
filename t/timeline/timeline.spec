Name: timeline
Version: 0.13.0
Release: alt1.1
Group: Office
Summary: Displaying and navigating events on a timeline
License: GPLv3
Source: %name-%version.zip
Patch: fix-paths.patch
BuildArch: noarch
Url: http://thetimelineproj.sourceforge.net/
%setup_python_module timelinelib

# Automatically added by buildreq on Mon Jul 04 2011
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-logging python-modules-xml
BuildRequires: ctags python-module-markdown scons unzip

%description
Features

Organize events in hierarchical categories
Move and resize events with the mouse
Duplicate events
Search events
Go to a specific date
Scroll and zoom with mouse wheel
Different representation depending on zoom level
Export to image
Available in multiple languages

%package -n %packagename
Group: Office
Summary: Python module for %name, %summary
%description -n %packagename
Python module for %name, %summary

%prep
%setup

cat > %name.desktop <<@@@
[Desktop Entry]
Icon=%name
Name=Timeline
Comment=Display and navigate information on a timeline
Exec=%name
Terminal=false
Type=Application
Categories=Office;Calendar;
StartupNotify=false
@@@

cat > %name.bin <<@@@
#!/usr/bin/python

import gettext
import sys

from timelinelib.about import APPLICATION_NAME
from timelinelib.arguments import ApplicationArguments
from timelinelib.gui.setup import start_wx_application
from timelinelib.paths import LOCALE_DIR

gettext.install(APPLICATION_NAME.lower(), LOCALE_DIR, unicode=True)

application_arguments = ApplicationArguments()
application_arguments.parse_from(sys.argv[1:])

start_wx_application(application_arguments)
@@@

%build
scons mo

%install
mkdir -p %buildroot/%python_sitelibdir_noarch
find %modulename -name \*.py | cpio -pd %buildroot/%python_sitelibdir_noarch/
mkdir -p %buildroot%_datadir/%name/icons
install icons/*.png %buildroot%_datadir/%name/icons/
install -D -m755 %name.bin %buildroot%_bindir/%name
install -D man/man1/timeline.1 %buildroot/%_man1dir/%name.1
install -D %name.desktop %buildroot/%_desktopdir/%name.desktop
for D in 16 32 48; do
  install -D icons/$D.png %buildroot%_iconsdir/hicolor/${D}x${D}/apps/%name.png
done
( cd po 
for D in */*; do
  install -D $D %buildroot%datadir/locale/$D
done
)

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/%name.desktop
%_man1dir/*

%files -n %packagename
%python_sitelibdir_noarch/%modulename

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 0.13.0-alt1
- Autobuild version bump to 0.13.0

