%define _unpackaged_files_terminate_build 1

Name: mos-xdg
Summary: XDG desktop settings for M OS distros
Summary(ru): Настройки рабочего окружения дистрибутивов М ОС
License: GPL-3.0
Group: Graphical desktop/Other
Version: 2.4
Release: alt1
Source0: %name-%version.tar
Source1: COPYING
BuildArch: noarch
BuildRequires: rpm-macros-systemd

%description
XDG desktop settings for M OS distros
%description -l ru_RU.UTF-8
Настройки рабочего окружения дистрибутивов М ОС

#--------------------------------------------------------------

%package core
Summary: Engine to set distribution-specific desktop settings
Summary(ru): Движок установки дистрибутиво-специфичных настроек рабочего стола
Group: Graphical desktop/Other
Requires: sed
# package was renamed
Obsoletes: kometa-xdg-core < 2.0
# this package was dropped as a very complex trick;
# icons are replaced by a filetrigger more reliably
Obsoletes: kometa-xdg-pam-env < 2.0

%description core
Engine to set distribution-specific desktop settings.
Sets environmental variables $XDG_CONFIG_DIRS and $XDG_DATA_DIRS,
adding /etc/xdg/mos and /usr/share/mos into them.
Can be used separately from M OS.
%description -l ru_RU.UTF-8 core
Движок установки дистрибутиво-специфичных настроек рабочего стола.
Устонавливает переменные окружения $XDG_CONFIG_DIRS и $XDG_DATA_DIRS,
добавляя в них /etc/xdg/mos и /usr/share/mos.
Может быть использован вне М ОС.

%files core
%doc COPYING
%dir /etc/xdg/mos
%dir /etc/xdg/mos/autostart
%dir /usr/share/mos
%_bindir/mos-xdg-env
%_user_env_gen_dir/10-mos-xdg.sh
/etc/profile.d/10-mos-xdg.sh

#--------------------------------------------------------------

# alternatives between plasma5-classic, plasma5-foo etc. can be added later

%package plasma5-classic
Summary: KDE 5 desktop settings for classic variant of M OS
Summary(ru): Настройки KDE 5 для классического варианта М ОС
Group: Graphical desktop/KDE
Requires: %name-core = %EVR
Requires: mos-icons-theme-classic
# package was renamed
Obsoletes: kometa-xdg-plasma5-classic < 2.0

%description plasma5-classic
KDE 5 desktop settings for classic variant of M OS
%description -l ru_RU.UTF-8 plasma5-classic
Настройки KDE 5 для классического варианта М ОС

%files plasma5-classic
%doc COPYING
/etc/xdg/mos/dolphinrc
/etc/xdg/mos/kcminputrc
/etc/xdg/mos/kdeglobals
/etc/xdg/mos/kxkbrc
/etc/xdg/mos/mimeapps.list
%dir /usr/share/mos/kxmlgui5
%dir /usr/share/mos/kxmlgui5/dolphin
/usr/share/mos/kxmlgui5/dolphin/dolphinui.rc

#--------------------------------------------------------------

%prep
%setup -q
cp %SOURCE1 .

%build
:

%install

mkdir -p %buildroot%_bindir
mkdir -p %buildroot/etc/profile.d
mkdir -p %buildroot%_user_env_gen_dir
install -m0755 scripts/mos-xdg-env %buildroot%_bindir/mos-xdg-env
# for console
install -m0755 scripts/profile.sh %buildroot/etc/profile.d/10-mos-xdg.sh
# for dbus services
install -m0755 scripts/systemd.sh %buildroot%_user_env_gen_dir/10-mos-xdg.sh

mkdir -p %buildroot/etc/xdg/mos/autostart
cp -rv plasma5/XDG_CONFIG_DIRS/* %buildroot/etc/xdg/mos
mkdir -p %buildroot/usr/share/mos
cp -rv plasma5/XDG_DATA_DIRS/* %buildroot/usr/share/mos

%check
cd scripts
./test.sh

%changelog
* Thu Jan 26 2023 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.4-alt1
- Return the preview to the Dolphin panel (by tema@)
  After updating KDE, the button preview disappeared in the Dolphin

* Mon Nov 21 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3-alt1
- remove setAsWallpaper.desktop, it now exists in plasma5-workspace
  $ rpm -qf /usr/share/kservices5/ServiceMenus/setaswallpaper.desktop
  plasma5-workspace-5.24.6-alt6.x86_64

* Fri Nov 18 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.2-alt2
- Own directory /etc/xdg/mos/autostart (will be used in other packages)

* Mon Aug 08 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.2-alt1
- Prefer R7 Office / OnlyOffice Desktop Editors for Microsoft Office formats
- Do not duplicate MIME associations

* Tue Apr 26 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.1-alt1
- Delete power settings: not valid for newer KDE (by tema@)
- Add MIME associations (by tema@)

* Tue Apr 26 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0-alt1
- Rename from Kometa to M OS (Moscow OS)
- Drop pam-env hackery due to being useless (icons are reliably replaced by a filetrigger)
- Package /etc/xdg/mos/powermanagementprofilesrc
- Package /usr/share/mos/kservices5/ServiceMenus/setAsWallpaper.desktop

* Wed Feb 16 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.5-alt1.1
- Commit 1.5-alt1 by tema@

* Tue Feb 15 2022 Artem Proskurnev <tema@altlinux.org> 1.5-alt1
- Add power settings
- Add Dolphin filer panel
- Add "Set as wallpaper"
- Set Chromium as the default browser

* Fri Dec 24 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.4-alt1
- Add setting $XDG_DATA_DIRS, enable "Show Previews" button in Dolphin
- Tune description: note that mos-xdg-core can be used just to set env outside of Kometa

* Thu Dec 16 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.3-alt1
- Turn off NumLock by default in KDE 5

* Thu Dec 16 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.2-alt1
- Hack to make alterator use correct icons (new subpackage mos-xdg-pam-env)
- Use macro for directory with systemd user environment generators (thanks to ldv@)

* Tue Dec 14 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.1-alt1
- set default icon theme

* Tue Dec 14 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.0-alt1
- Init
