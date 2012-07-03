
Name:           onboard
Version:        0.96.2
Release:        alt2.1

Summary:        Simple on-screen Keyboard
License:        GPLv3
Group:          Graphical desktop/GNOME 
URL:            https://launchpad.net/onboard/

Source0:        http://launchpad.net/%name/0.96/%version/+download/%name-%version.tar.gz
# To build the .desktop files. This can be upstreamed:
Patch0:         onboard-setup.patch

Patch1:         onboard-no-appindicator.patch

Patch2:         onboard-startup-hackaround.patch

BuildRequires(pre): etersoft-build-utils libGConf-devel rpm-build-gnome python-devel
BuildRequires:  glibc-devel-static intltool libgtk+2-devel 
BuildRequires:  python-module-pygtk-devel python-module-vte
BuildRequires:  python-module-distutils-extra >= 2.12
BuildRequires:  python-module-virtkey
BuildRequires:  desktop-file-utils
BuildRequires:  libgtk+3-devel libXi-devel libXtst-devel libX11-devel

Requires:  GConf

%description
An on-screen keyboard useful on tablet PCs or for mobility impaired
users.

%prep
%setup -q
%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
%python_build

%install
%python_install
#fix wrong permissons
chmod a+x %buildroot%_datadir/onboard/layoutstrings.py
for file in %buildroot%python_sitelibdir/Onboard/{settings,IconPalette,KeyboardSVG,utils}.py; do
   chmod a+x $file
done

desktop-file-install --dir %buildroot%_desktopdir       \
    --remove-category="X-GNOME-PersonalSettings"        \
    --add-category="Utility;"                           \
    %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir       \
    --remove-category="X-GNOME-PersonalSettings"        \
    --add-category="Utility;"                           \
    %buildroot%_desktopdir/%name-settings.desktop

mkdir -p %buildroot%_datadir/locale
cp -a build/mo/* %buildroot%_datadir/locale
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README docs/
%_bindir/%name
%_bindir/%name-settings
%_datadir/%name/
%_sysconfdir/xdg/autostart/*
%_desktopdir/%name.desktop
%_desktopdir/%name-settings.desktop
%_datadir/glib-2.0/schemas/*
%_datadir/GConf/gsettings/*
%_datadir/icons/hicolor/scalable/apps/onboard.svg
%_datadir/icons/hicolor/scalable/apps/onboard2.svg
%python_sitelibdir/Onboard/
%python_sitelibdir/%{name}*.egg-info

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.96.2-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Jan 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.96.2-alt2
- hack around startup crash

* Wed Jan 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.96.2-alt1
- updated to 0.96.2
- now it is arch-dependent

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.95.1-alt1.1
- Rebuild with Python-2.7

* Sat Oct 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.95.1-alt1
- Initial build in Sisyphus (closes: #26220)
