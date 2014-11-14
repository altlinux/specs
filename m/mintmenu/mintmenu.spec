# TODO: fix urls and install icons like
#/usr/share/linuxmint/mintMenu/search_engines/dictionary.png
# see /usr/share/linuxmint/mintMenu/plugins/applications.py
%define l10n_ver 2014.11.11

Name:           mintmenu
Version:        5.6.0
Release:        alt1
# MIT is needed for keybinding.py
License:        GPLv2+ and MIT
Summary:        Advanced Menu for the MATE Desktop

Group:          Graphical desktop/GNOME
Url:            http://packages.linuxmint.com/pool/main/m/mintmenu/
# VCS:		https://github.com/linuxmint/mintmenu.git
Source0:        http://packages.linuxmint.com/pool/main/m/mintmenu/%{name}_%{version}.tar.gz
Source1:        http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%l10n_ver.tar.gz
Source33:	mintmenu_test.sh
Source34:	list-mintmenu.conf
Source35:	list-mintmenu.lua
Source36:	list-mintmenu.ignore

Source50:	mintmenu.watch

# SUSE patches from http://download.opensuse.org/repositories/home:/unamanic/Fedora_14/src/
# PATCH-FIX-OPENSUSE mintmenu-suse_branding.patch william@witt-famiylnet: Suse branding
Patch2:         mintmenu-alt_branding.patch
# PATCH-FIX-OPENSUSE mintmenu-datadir.patch william@witt-famiylnet: move from /usr/lib to /usr/share
Patch3:         mintmenu-5.5.8-alt-datadir.patch
# PATCH-FIX-OPENSUSE mintmenu-run_as_superuser.patch william@witt-famiylnet: fix run as superuser
Patch4:         mintmenu-run_as_superuser.patch
# PATCH-FIX-OPENSUSE mintmenu-mintmenu_executables.patch william@witt-famiylnet: update paths for executable and bonobo server
Patch9:         mintmenu-change_locale_directory.patch

# alt patches
Patch34:	mintmenu-5.5.1-alt-drop-mintinstall-check.patch
Patch35:	mintmenu-5.2.1-alt-apt-cache.patch
Patch36:	mintmenu-5.2.1-alt-no-mintengines.patch
Patch37:	mintmenu-5.2.1-alt-GPL-path.patch
Patch38:	mintmenu-5.5.1-alt-use-rpminstall.patch
#Patch39:	mintmenu-5.2.1-alt-cyrillic.patch
Patch40:	mintmenu-5.5.1-alt-xfce-logout.patch
# Use Synaptic via consolehelper intead of gksu
Patch41:	mintmenu-alt-fix-package-manager.patch

Requires: GConf2 alacarte gnome-search-tool
Requires: python-module-gnome-menus
Requires: python-module-pygnome-desktop
Requires: python-module-pyxdg
Requires: python-module-configobj
Requires: python-module-apt

Requires: apt
BuildRequires: apt

# due to apt: protocol
Requires: rpminstall >= 1.1.1
# Recommends:( due to inode/directory preferences
Requires: altlinux-mime-defaults > 0.17

# TODO:
#Requires:       tracker-search-tool

BuildArch:      noarch

%description
An advanced "slab" style menu for Linux. MintMenu supports filtering,
favorites, autosession, and many other features.  MintMenu can either be
added to your gnome-panel or launched in its own window.

%prep
%setup -q -n mintmenu
tar -xf %{SOURCE1}

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch9 -p1
%patch34 -p1
%if_with apthack
%patch56 -p1
%else
%patch35 -p1
%endif
#%%patch36 -p1
%patch37 -p1
%patch38 -p1
#%%patch39 -p1
%patch40 -p1
%patch41 -p1

# drop deprecated plugins
rm -f usr/lib/linuxmint/mintMenu/plugins/easygconf.py

%build
#pure python

%install
#clean out questionably liscensed files.
#rm -rf %{buildroot}%{_prefix}/lib/linuxmint/mintMenu/mint*.png
#rm -rf %{buildroot}%{_prefix}/lib/linuxmint/mintMenu/mint*.svg
find . -name '*.orig' -exec rm -f {} ';'
find . -name '*.pyc' -exec rm -f {} ';'
find . -name '*.pot' -exec rm -f {} ';'
find mint-translations-%l10n_ver -not -name 'mintmenu.mo' -type f -exec rm -f {} ';'

mkdir -p %buildroot%prefix
cp -av usr/bin usr/share %buildroot%prefix

cp -av usr/lib/linuxmint %buildroot%_datadir

# Make utilites executable
chmod +x %buildroot%_datadir/linuxmint/mintMenu/*.py

cp -r mint-translations-%l10n_ver/usr/share/linuxmint/* %buildroot%_datadir
chmod -R u+rw,g-w,g+r,o+r,o-w %buildroot%_datadir/locale/*

%find_lang %name --with-gnome

install -Dm644 %SOURCE34 %buildroot/etc/apt/apt.conf.d/list-mintmenu.conf
install -Dm755 %SOURCE35 %buildroot/usr/share/apt/scripts/list-mintmenu.lua
install -Dm644 %SOURCE36 %buildroot/etc/buildreqs/files/ignore.d/list-mintmenu

# check patches
sh -v %SOURCE33

%files -f %{name}.lang
%_bindir/mintmenu
%_datadir/linuxmint/*
%_datadir/mate-panel/*
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.xml

# list-mintmenu
/usr/share/apt
%config /etc/apt/apt.conf.d/*
%config /etc/buildreqs/files/ignore.d/*

%changelog
* Fri Nov 14 2014 Andrey Cherepanov <cas@altlinux.org> 5.6.0-alt1
- New version
- Update translations to 2014.11.11

* Thu Oct 02 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.9-alt1
- New version

* Mon Jul 28 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.8-alt1
- New version
- Add .watch file
- Update translations to 2014.05.25
- Fix Package manager open
- Fix Preferences open (ALT #30118)

* Wed Apr 30 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.3-alt1.git6a7cf3f
- New version

* Wed Mar 19 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1.git0feb06e
- New version (ALT #29878)
- Drop deprecated plugin easygconf
- Simplify spec

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1.M60P.4
- bugfixes (thanks to Aleksey Novodvorsky):
  * detectDE restored
  * xfce logout use -l and -h respectively

* Fri Aug 05 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1.M60P.3
- support for cyrillic in search

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1.M60P.2
- added requires on gnome-search-tool

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1.M60P.1
- use rpminstall directly instead of relying on apt:// protocol.

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt0.M60T.5
- use rpminstall directly instead of relying on apt:// protocol.

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt0.M60T.4
- accurate requires on rpminstall

* Sat Jul 30 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt0.M60T.3
- apt support

* Tue Jul 12 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt0.M60T.2
- apt demo support

* Tue Jul 12 2011 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt0.M60T.1
- new version

* Mon Jul 11 2011 Igor Vlasenko <viy@altlinux.ru> 5.1.9-alt0.1
- first build
