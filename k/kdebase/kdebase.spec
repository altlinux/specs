%undefine __libtoolize
%define _optlevel s
%define glibc_core_ver %{get_version glibc-core}
%define _keep_libtool_files 1

%define unstable 0
%define with_kdm 1
%define with_hal 1
%define with_smb 1

%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_K3lib
%add_findreq_skiplist %_K3apps/ksplash/Themes/Default
%add_findreq_skiplist %_K3apps/kicker/pics/kside.png
%add_findreq_skiplist %_K3apps/kicker/pics/kside_tile.png
%if %with_kdm
%add_findreq_skiplist %_K3apps/kdisplay/color-schemes/kdm_default_scheme.kcsrc
%endif
%add_findreq_skiplist %_K3apps/kdewizard/pics/wizard_small.png
%add_findreq_skiplist %_K3wall/default_blue.jpg

%define qtdir %_qt3dir
%define x11confdir %_sysconfdir/X11

%define req_design_graphics design-graphics >= 3.1.4


%define with_new_hal 1
%define int_qt_dbus 1
%def_disable userpasswd

%define major 3
%define minor 5
%define bugfix 13
Name: kdebase
Version: %major.%minor.%bugfix
Release: alt5
%define reqver %major.%minor

Summary: Trinity Desktop Environment - Core files
Group: Graphical desktop/KDE
License: GPL
URL: http://www.trinitydesktop.org/

Requires: %name-libkonq = %version-%release
Requires: %name-libs = %version-%release
%if %with_kdm
Requires: %name-kdm = %version-%release
%endif
Requires: %name-wm = %version-%release
Requires: %name-konqueror = %version-%release
Requires: %name-kcontrol = %version-%release
Requires: %name-kdeprint = %version-%release
Requires: %name-kio = %version-%release
Requires: %name-kwrite = %version-%release

Source: kdebase-%version.tar
Source1: file_lists.sh
Source2: kdebase-ksysguardd-init
Source3: kdm_firstime
#
Source5: cr16-app-package_games_kids.png
Source6: cr32-app-package_games_kids.png
Source7: cr48-app-package_games_kids.png
#
Source10: kdebase-3.0-kde.pam
Source11: kdm.logrotate
Source12: kicker-default1.png
Source13: kdebase-3.0-kde-np.pam

# add servicemenu entry (compress/uncompress action )
Source2001:	kdebase-3.1-convertpdftops.desktop
Source2002:	kdebase-3.1-convertpstopdf.desktop
# autostart menu entry
Source2003: Autostart.desktop

# RH
Source4000: kdebase-3.0-mailsettings.cc

# ALT
Source5002: kdebase-3.0-kscreensaver.pamd

###             ###
### Patch party ###
###             ###
# MDK
Patch03: kdebase-3.5.8-alt-kicker-icons.patch
Patch04: kdebase-3.5-ALT-kdm-config.patch
Patch05: keditfiletype-3.5.5-mark-user-edited.patch
Patch06: kdebase-3.5.5-ALT-kcmenergy-enable-energy-saving.patch
Patch07: kdebase-3.4-fix-up-button.patch
Patch08: kdebase-3.1-add-ctrl-w-to-konq-combo.patch
Patch09: kdebase-3.5.5-fix-ssl-default-path.patch
Patch10: kdebase-3.5-ALT-fix-kicker-clock-applet-default-value.patch
Patch11: kdebase-3.1-fix-kioslave-thimbnail-creator.patch
Patch12: kcmaccount-3.4.0-facedir.patch
#
Patch14: kdebase-3.5.12-fix-kfmclient-launch.patch
Patch15: kdebase-kdm-syscfg.diff

# TDE
Patch100: r1227273.diff

# RH patches
Patch500: kdebase-3.5.5-vroot.patch
Patch501: kdebase-3.5.8-consolekit-kdm.patch
Patch502: kdebase-3.1-ssl-krb5.patch
Patch503: kdebase-3.5.8-kdesktop_open_terminal-ALT.patch
Patch504: kdebase-3.1.3-konsole-double-esc.patch
Patch505: kdebase-3.5.1-xdg.patch
%if %int_qt_dbus
Patch506: kdebase-3.5.5-dbus.patch
%endif
Patch507: kdebase-3.5.4-htdig-ALT.patch

# SuSE
Patch601: fix-kio-smb-auth.diff
#
Patch603: kdesud-security.diff
Patch604: hide-only-showin-entries.diff
Patch605: mach_blass_legacy.diff
Patch606: non-fast-malloc.diff
Patch607: nsplugin-Preference.diff
Patch608: kcmsamba_log.diff
Patch609: kdeeject.diff
Patch610: use-full-hinting-by-default.diff
#
Patch612: fix-lockup-from-gnome-apps.diff
Patch613: kdm-mark_autologin.diff
Patch614: kdm-wordbreak.diff
Patch615: khelpcenter-gnome-support-ALT.patch
Patch616: khelpcenter-localindices.patch
Patch617: kio-media-errorhandling.diff
Patch618: konsole_keytab.diff
Patch619: media-cryptosupport.diff
Patch620: ksmserver-defaulttohalt.diff
Patch621: rotate-wacom-pointers.diff
Patch622: spellcheck-default-utf8.diff
Patch623: workaround-pdf-on64bit-nsplugin-bug.diff
Patch624: xinerama.patch
Patch625: kmenu-search-fs20060627-fixed.diff
Patch626: kmenu-search-slowdown-fix.diff

# Pardus
Patch700: kdebase_audit.patch

# MDK && RH -> ALT patches
Patch900: kdebase-3.4.1-shortcuts-alt.patch
Patch901: kdebase-3.0.0-staticlesstif-alt.patch

# ALT patches
Patch1001: kdebase-3.2-fix_kz_locale.patch
Patch1002: kdebase-3.5.8-alt-default-no-desktop-trash.patch
Patch1003: kdebase-3.5.8-alt-hide-menu-home.patch
Patch1004: kdebase-3.5.10-alt-automake.patch
Patch1005: kdebase-3.5-alt-startkde.patch
Patch1006: kdebase-3.0-indexhtml.patch
Patch1007: kdebase-3.5.10-kfontinst.patch
Patch1008: kdebase-3.5.8-alt-kdesktop-lock-kkbswitch-support.patch
Patch1009: kdebase-3.5.10-alt-kicker-minipager-defaults.patch
Patch1010: kdebase-3.5.12-alt-vfat-shortname.patch
Patch1011: kdebase-3.5.12-alt-fix-linking.patch
Patch1012: kdebase-3.5.12-konsole_su.patch
Patch1013: kdebase-3.5.12-alt-gcc45.patch
Patch1014: kdebase-3.5.12-alt-fix-compile.patch
Patch1015: kdebase-3.5.12-alt-nohal.patch
Patch1016: kdebase-3.2-konsolefont-alt.patch
Patch1018: kdebase-3.5-select_background_dir.patch
#
Patch1023: kdebase-3.5.12-smb-auth.patch
Patch1024: kdebase-3.5.12-alt-def-session-apps.patch
Patch1025: kdebase-3.3-kdesu_dont_decode_command.patch
Patch1026: kcontrol-3.5.12-xcursor-exclude-symlinks.patch
Patch1027: kdm-3.5.12-genkdmconf.patch
Patch1028: kdm-3.5.12-select-faces-directory.patch
Patch1029: kdm-3.3.0-wmsession.patch
Patch1030: kmenuedit-3.2.0-menueditor.patch
Patch1031: 3.5.12-find-screensaver.patch
Patch1032: kdm-3.5.0-save-qtrc.patch
Patch1033: konqueror-3.2.2-fix-launch.patch
Patch1034: clock-3.5-desktop.patch
Patch1035: kdm-3.5-desktop.patch
Patch1036: kdebase-3.5-default-font-value.patch
Patch1037: konsole-3.5.12-default-add-to-utmp.patch
Patch1038: kdepasswd-3.5.8-userpasswd.patch
Patch1039: kdepasswd-3.5.8-chfn.patch
Patch1040: kappfinder-3.5.0-fix-linking.patch
Patch1041: kdebase-3.5.12-export-gtk-apply-style.patch
Patch1042: kdepasswd-3.3.1-truncate.patch
Patch1043: kde-unknown.directory.patch
Patch1044: kdebase-3.5.12-alt-def-background.patch
Patch1045: kdm-3.5.12-fix-alternate-background-color.patch
#
Patch1048: kdebase-3.5.2-alt-dont-mount-cd.patch
Patch1049: 3.5.12-alt-documents-desktop.patch
Patch1050: kdebase-3.5.2-alt-hal-mount-root.patch
Patch1051: kdebase-3.5.8-alt-searchproviders.patch
Patch1052: kdebase-3.5.7-alt-media-baseurl-encoding.patch
Patch1053: kdebase-3.5.5-fix_khotkeys.patch
Patch1054: kdebase-3.5.8-alt-launcherapplet-defaults.patch
Patch1055: kdebase-3.5.6-alt-desktop-categories.patch
Patch1056: kdebase-SuSE-alt-clean.patch
Patch1057: kryptomedia-alt-int-qt-dbus.patch
Patch1058: kdebase-3.5.12-alt-kfind-select-remote.patch
Patch1059: kicker-3.5.7-alt-add-default-menuext.patch
Patch1060: kdm-3.5.12-alt-dont-show-nologin-users.patch
Patch1061: kdebase-3.5.9-alt-mediamanager-floppy-list-fallback.patch
Patch1062: mediamanager-3.5.12-alt-fuser-path.patch
Patch1063: kdebase-3.5.7-alt-kio-man.patch
Patch1064: kdebase-3.5.12-alt-default-utf8-mount-option.patch
Patch1065: kcontrol-3.5.12-alt-desktop.patch
Patch1066: kdebase-3.5.7-alt-kdesktop-symlink.patch
Patch1067: kdebase-3.5.7-alt-ksplashsimple-colors.patch
Patch1068: kdebase-3.6.7-alt-kdm-add-en-lang.patch
Patch1069: kdebase-3.5.12-alt-default-floppy-sync-mount-option.patch
Patch1070: kdebase-3.5.12-alt-lang.patch
Patch1071: kdebase-3.5.7-alt-l10n-ru-desktop.patch
Patch1072: kdebase-3.5.12-alt-kickoff-no-searchplugins.patch
Patch1073: kdebase-3.5.9-alt-conf-path-to-krb5-fix.patch
Patch1074: kdebase-3.5.10-konq-sidebar-system-proto.patch
Patch1075: kdebase-3.5.12-alt-kdesktop-lock-show-layout-chnange.patch
Patch1076: kdebase-3.5.10-alt-usb_close.patch
Patch1077: tde-3.5.13-build-defdir.patch
Patch1078: kdm-3.5.13-greeter.patch
Patch1079: kdm-3.5.13-noPAMuse.patch
Patch1080: kdm-3.5.13-SAK_disable_CtrlAltDel-FullCPUusage_SAK_Std.patch
Patch1081: kdebase-3.5.13-kwin-keramic-pics-emb.patch
Patch1082: tde-3.5.13-kxdglauncher_locale.patch
Patch1083: tde-3.5.13-SmoothScrolling-save.patch

# Sergey A. Sukiyazov <corwin@micom.don.ru>
Patch2000: kdebase-3.5.0-man_recode.patch
Patch2001: kdebase-3.5.6-kioslave_media_dbus.patch

# misc
Patch2100: 40_use_hal_mountoptions.diff
Patch2101: kdebase-3.5.10-alt-nonhal_backend_options_fix.patch

# security
# end security

# Automatically added by buildreq on Mon Apr 12 2004 (-bi)
#BuildRequires: XFree86-devel XFree86-libs XFree86-utils arts bzlib-devel doxygen eject fontconfig-devel freetype2-devel gcc-c++ gcc-g77 glib2 kde-settings kdelibs-apidocs kdelibs-devel lesstif-devel libart_lgpl-devel libarts-devel libjpeg-devel libldap-devel libncurses-devel libpam-devel libpng-devel libqt3-devel libraw1394-devel libssl-devel libstdc++-devel libtiff-devel libtinfo-devel libutempter-devel pkgconfig qt3-designer qt3-doc samba-client-devel xinitrc xml-utils zlib-devel
BuildRequires(pre): kdelibs kdelibs-devel cmake libqt3-devel libcups
BuildRequires: libgtk+2-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: bzlib-devel doxygen eject fontconfig-devel freetype2-devel
#BuildRequires: gcc-c++ kdelibs-apidocs kdelibs-devel
BuildRequires: gcc-c++ kdelibs-devel bdftopcf
BuildRequires: libart_lgpl-devel libjpeg-devel openexr-devel
BuildRequires: openmotif-devel libusb-compat-devel libattr-devel
BuildRequires: libldap-devel libncurses-devel libpam-devel libpng-devel
BuildRequires: libraw1394-devel libssl-devel libstdc++-devel libdbus-tqt-devel
BuildRequires: libtiff-devel libtinfo-devel libutempter-devel
BuildRequires: pkg-config qt3-designer qt3-doc xinitrc
%if %with_smb
BuildRequires: libsmbclient-devel
%endif
BuildRequires: xml-utils zlib-devel glibc-utils glibc-devel
BuildRequires: flex libalternatives-devel libsasl2-devel libsensors3-devel
BuildRequires: libdbus-devel
%if %with_hal
BuildRequires: libhal-devel
%if %int_qt_dbus
%else
BuildRequires: libdbus-qt-devel
%endif
%endif
BuildRequires: libalsa-devel
BuildRequires: perl(Encode.pm) libaudit-devel
BuildRequires: kdelibs = %version kdelibs-devel = %version libqt3-devel >= 3.0.3
BuildRequires: desktop-file-utils

%description
Core applications for the K Desktop Environment.
Here is an overview of the directories:

	- drkonqi: if ever an app crashes (heaven forbid!) then Dr.Konqi will be so
          kind and make a stack trace. This is a great help for the
          developers to fix the bug.
	- kappfinder: searches your hard disk for non-KDE applications, e.g. Acrobat
             Reader (tm) and installs those apps under the K start button
	- kate: a fast and advanced text editor with nice plugins
	- kcheckpass: small program to enter and check passwords, only to be used by
             other programs
	- kcontrol: the KDE Control Center allows you to tweak the KDE settings
	- kdcop: GUI app to browse for DCOP interfaces, can also execute them
	- kdebugdialog: allows you to specify which debug messages you want to see
	- kdeprint: the KDE printing system
	- kdesktop: you guessed it: the desktop above the panel
	- kdesu: a graphical front end to "su"
%if %with_kdm
	- kdm: replacement for XDM, for those people that like graphical logins
%endif
	- kfind: find files
	- khelpcenter: the app to read all great documentation about KDE
	- khotkeys: intercepts keys and can call applications
	- kicker: the panel at the botton with the K start button and the 
				taskbar etc
	- kioslave: infrastructure that helps make every application internet 
				enabled e.g. to directly save a 
				file to ftp://place.org/dir/file.txt
	- klipper: enhances and extenses the X clipboard
	- kmenuedit: edit for the menu below the K start button
	- konqueror: the file manager and web browser you get easily used to
	- konsole: a shell program similar to xterm
	- kpager: applet to show the contents of the virtual desktops
	- kpersonalizer: the customization wizard you get when you first start KDE
	- kreadconfig: a tool for shell scripts to get info from KDE's config files
	- kscreensaver: the KDE screensaver environment and lot's of savers
	- ksmserver: the KDE session manager (saves program status on login, 
				restarts those program at the next login)
	- ksplash: the screen displayed while KDE starts
	- kstart: to launch applications with special window properties
         such as iconified etc
	- ksysguard: task manager and system monitor, even for remote systems
	- ksystraycmd: allows to run any application in the system tray
	- ktip: gives you tips how to use KDE
	- kwin: the KDE window manager
	- kxkb: a keyboard map tool
	- libkonq: some libraries needed by Konqueror
	- nsplugins: together with OSF/Motif or Lesstif allows you to use Netscape
			(tm) plugins in Konqueror

%package devel
Summary: Devel stuff for kdebase
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: kdelibs-devel >= %version
Requires: %name-konqueror = %version-%release
Requires: %name-libkonq = %version-%release
Requires: %name-wm = %version-%release
Requires: %name-kate = %version-%release
#
%description devel
This package contains header files needed if you wish to build applications
based on kdebase.

%package common
Summary: Common files for %name package
Group: Graphical desktop/KDE
Conflicts: kdebase <= 3.1.1-alt0.1
PreReq: /etc/tcb
Requires: kde-common >= %reqver
%if %with_kdm
Provides: kde-settings-kdm = %version-%release
%endif
Obsoletes: kde-settings-kdm < %version-%release
%description common
Common files for %name package

%package libs
Summary: Basic libraries for kdebase package
Group: System/Libraries
Requires: %req_design_graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description libs
Basic libraries for kdebase package

%package kwrite
Summary: Advanced text editor
Group: Editors
#Requires: kdebase-libs >= %version-%release
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kdebase-kate = %version-%release
Obsoletes: kdebase-kate < %version-%release
#
%description kwrite
Package contains KWrite a simple text editor and
Kate a fast and advanced text editor with nice plugins

%package kcontrol
Summary: The KDE Control Center
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: %name-konqueror = %version-%release
Requires: pciutils
#
%description kcontrol
The KDE Control Center allows you to tweak the KDE settings

%package kdm
Summary: KDE Display Manager
Group: Graphical desktop/KDE
PreReq(post,preun): alternatives >= 0.2
#Requires: %name-libs >= %version-%release
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: xinitrc
Requires: %req_design_graphics
#
%description kdm
KDE Display Manager - is the replacement for XDM,
for those people that like graphical logins

%package konqueror
Summary: The file manager and web browser for KDE
Group: Networking/WWW
PreReq(post,preun): alternatives >= 0.2
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: indexhtml
Requires: %req_design_graphics
Provides: webclient, /usr/bin/xbrowser
#
%description konqueror
The file manager and web browser easy for use.

%package libkonq
Summary: Libraries needed by Konqueror
Group: Networking/WWW
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description libkonq
Some libraries needed by Konqueror

%package kio
Summary: Internet protocol plugins for KDE
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
%if %with_hal
#Requires: hal dbus
%endif
Provides: %name-kio-samba = %version-%release
Obsoletes: %name-kio-samba < %version-%release
#
%description kio
Infrastructure that helps make every application
internet enabled e.g. to directly save a file
to ftp://place.org/dir/file.txt

%package kdeprint
Summary: The KDE printing system
Group: System/Configuration/Printing
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: poster
Requires: libcups >= %{get_version libcups} cups
#
%description kdeprint
The KDE printing system

%package wm
Summary: KDE Window Manager basic programs
Group: Graphical desktop/KDE
PreReq: libutempter
PreReq(post,preun): alternatives >= 0.2
Requires: sound_handler
Requires: shadow-change
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
Requires: kde3-freedesktop-menu
Requires: wm-common-freedesktop
%if_enabled userpasswd
Requires: userpasswd
%else
Requires: passwd
%endif
Provides: xvt, %_x11bindir/xvt
Provides: ksplashml = %version-%release
Obsoletes: ksplashml
#
%description wm
KDE Window Manager basic programs

%package -n kde3-menu-resources
Summary: menu resources for the original KDE menu
Group: Graphical desktop/KDE
BuildArch: noarch

%description -n kde3-menu-resources
Menu resources for the original KDE menu.

%prep
%setup -q
%if %with_hal
#patch1056 -p1
#if %int_qt_dbus
#patch1057 -p1
#endif
#    install -m 0644 ../altlinux/kryptomedia-ru.po po/kryptomedia/ru.po
#    mv kryptomedia po ../
#popd
#rm -rf kdebase-SuSE
%endif
#
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
#
%patch14 -p1
%patch15 -p1

# TDE patches
#%patch100 -p1

# RH patches
%patch500 -p1
#%patch501 -p1
%patch502 -p1
#%patch503 -p1
%patch504 -p1
%patch505 -p1
#%if %int_qt_dbus
#%patch506 -p1
#%endif
#%patch507 -p1

# ->ALT
%patch900 -p1
# static lesstif
#%patch901 -p1

# SuSE
#%patch601 -p0
#
#%patch603 -p0
%patch604 -p0
#%patch605 -p0
%patch606 -p0
#%patch607 -p0
%patch608 -p0
#%patch609 -p0
#%patch610 -p0
#
###%patch612 -p0
###%patch613 -p0
#%patch614 -p0
#%patch615 -p0
#%patch616 -p0
#%patch617 -p0
#%patch618 -p0
###%patch619 -p0
#%patch620 -p0
#%patch621 -p0
#%patch622 -p0
###%patch623 -p0
#%patch624 -p0
###%patch625 -p0
###%patch626 -p0

# Pardus
###%patch700 -p1

# ALT
%patch1001 -p1
#%patch1002 -p1
%patch1003 -p1
#%patch1004 -p1
%patch1005 -p1 -b .orig
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1
%patch1010 -p1
%patch1011 -p1
%patch1012 -p1
#%patch1013 -p1
%patch1014 -p1
%if %with_hal
%else
%patch1015 -p1
%endif
#
# konsole font
###%patch1016 -p1
#
%patch1018 -p1
#
# smb auth
%patch1023 -p1
%patch1024 -p1
%patch1025 -p1
%patch1026 -p1
%patch1027 -p1
%patch1028 -p1
%patch1029 -p1
%patch1030 -p1
%patch1031 -p1
%patch1032 -p1
# konq launch
#%patch1033 -p1
%patch1034 -p1
%patch1035 -p1
%patch1036 -p1
%patch1037 -p1
%if_enabled userpasswd
%patch1038 -p1
%endif
%patch1039 -p1
%patch1040 -p1
%patch1041 -p1
%patch1042 -p1
%patch1043 -p1
%patch1044 -p1
%patch1045 -p1
#
%patch1049 -p1
%patch1051 -p1
###%patch1052 -p1
%patch1053 -p1
%patch1054 -p1
%patch1055 -p1
# ^^^ upper
%patch1058 -p1
%patch1059 -p1
%patch1060 -p1
###%patch1061 -p1
%patch1062 -p1
%patch1063 -p1
%patch1064 -p1
%patch1065 -p1
%patch1066 -p1
#%patch1067 -p1
%patch1068 -p1
%patch1069 -p1
%patch1070 -p1
%patch1071 -p1
%patch1072 -p1
%patch1073 -p1
%patch1074 -p1
%patch1075 -p1
%patch1076 -p1
%patch1077
%patch1078 -p1
%patch1079 -p1
%patch1080
%patch1081 -p1
%patch1082
%patch1083

# Sergey A. Sukiyazov <corwin@micom.don.ru>
###%patch2000 -p1
#%patch2001 -p1

###%patch2100 -p1
###%patch2101 -p1

# security
# end security

# add missing icons for package_games_kids
install -m 0644 %SOURCE5 %SOURCE6 %SOURCE7 pics/crystalsvg/

# remove to regenerate
rm -f kioslave/nfs/*_xdr.c

#sed -i "s|^Name\(.*\)\=\(.*\)|Name\1=\2 [KDE]|" khelpcenter/Help.desktop
sed -i "s|Country/Region|Country-Region|g" kcontrol/locale/language.desktop
#sed -i "s|Icon=kded|Icon=kcmpartitions|" kcontrol/kded/kcmkded.desktop

cat >kde3 <<__EOF__
#!/bin/sh
#  Script for launching KDE3 applications from outside of the KDE3 desktop

PATH="%_K3bindir:\$PATH" exec "\$@"
__EOF__

%build
export QTDIR=%qtdir
export KDEDIR=%_K3prefix
BD=%_builddir/%name-%version/BUILD

export PATH=$QTDIR/bin:%_K3bindir:$PATH

export LD_LIBRARY_PATH=$QTDIR/lib:%_K3libdir:$BD/libkonq:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_K3lib -L%_K3lib -L%_libdir"
export CPPFLAGS="%optflags"

%add_optflags -DHAVE_LONG_LONG -DX11CONFDIR='\\\"%x11confdir\\\"'

if ! [ -f $BD/CMakeCache.txt ]
then
%K3cmake \
    -DBUILD_ALL=ON \
    -DWITH_SASL=ON \
    -DWITH_LDAP=ON \
    -DWITH_OPENEXR=ON \
    -DWITH_XCOMPOSITE=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XFIXES=ON \
    -DWITH_XDAMAGE=ON \
    -DWITH_XRANDR=ON \
    -DWITH_XEXT=ON \
    -DWITH_LIBRAW1394=ON \
    -DWITH_LIBUSB=ON \
    -DWITH_PAM=ON \
    -DWITH_SHADOW=OFF \
    -DWITH_XDMCP=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_ARTS=OFF \
    -DWITH_I8K=ON \
%if %with_smb
    -DWITH_SAMBA=ON \
%endif
%if %with_hal
    -DWITH_HAL=ON \
%endif
    -DKDE_DISTRIBUTION_TEXT="%distribution %_target_cpu"
fi
%K3make

g++ $RPM_OPT_FLAGS -o mailsettings %SOURCE4000

#######################  Install  ###########################
%install
%if %unstable
%set_strip_method none
%endif

%__mkdir_p %buildroot/%_K3apps/konqueror/dirtree/remote
mkdir -p %buildroot/%_bindir


%K3install

install -m 0755 kde3 %buildroot/%_bindir
install -m 0755 trinity %buildroot/%_bindir

install -d -m0755 %buildroot/%_K3datadir/cmake
install -m0644 BUILD/kwin/kwin.cmake %buildroot/%_K3datadir/cmake/

install -dm 0755 %buildroot/%_kde3_iconsdir/
mv %buildroot/%_iconsdir/hicolor %buildroot/%_kde3_iconsdir/hicolor/

install -dm 0755 %buildroot/%_K3applnk/.hidden/
install -m 0644 applnk/compat/*.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kcontrol/energy/energy.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kcontrol/performance/kcmkonqyperformance.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kcontrol/kicker/*.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kcontrol/kio/smb.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kcontrol/xinerama/xinerama.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kcontrol/randr/randr.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 konqueror/konqueror.desktop %buildroot/%_K3applnk/
install -m 0644 konqueror/konqfilemgr.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kcontrol/konq/file*.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kcontrol/konsole/kcmkonsole.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kwin/kcmkwin/kwinoptions/*.desktop %buildroot/%_K3applnk/.hidden/

install -dm 0755  %buildroot/%_K3applnk/System/ScreenSavers/
install -m 0644 kscreensaver/*.desktop %buildroot/%_K3applnk/System/ScreenSavers/

install -m 0644 kappfinder/kappfinder.desktop %buildroot/%_K3applnk/System/
install -m 0644 kmenuedit/kmenuedit.desktop %buildroot/%_K3applnk/System/
install -m 0644 kpersonalizer/kpersonalizer.desktop %buildroot/%_K3applnk/System/

install -dm 0755  %buildroot/%_K3applnk/Settings/LookNFeel/
install -m 0644 kcontrol/taskbar/kcmtaskbar.desktop %buildroot/%_K3applnk/Settings/LookNFeel/
install -m 0644 kcontrol/kicker/panel.desktop %buildroot/%_K3applnk/Settings/LookNFeel/

install -dm 0755 %buildroot/%_K3applnk/Toys/
install -m 0644 ktip/ktip.desktop %buildroot/%_K3applnk/Toys/

install -dm 0755 %buildroot/%_K3applnk/Utilities/
install -m 0644 kpager/kpager.desktop %buildroot/%_K3applnk/Utilities/

install -dm 0755 %buildroot/%_K3apps/kconf_update/
install -m 0644 khotkeys/data/konqueror_gestures_trinity21_update.upd %buildroot/%_K3apps/kconf_update/

#install -dm 0755 %buildroot/%_K3srv/
install -m 0644 kioslave/ldap/ldap*.protocol %buildroot/%_K3srv/

install -m 0755 mailsettings %buildroot/%_K3bindir

# Install kde pam configuration files
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE10 %buildroot/%_sysconfdir/pam.d/kde
install -m 0644 %SOURCE13 %buildroot/%_sysconfdir/pam.d/kde-np

# Install kscreensaver pam configuration file
install -m 0644 %SOURCE5002 %buildroot/%_sysconfdir/pam.d/kscreensaver

# Install ksysguardd initscript
install -d -m 0755 %buildroot/%_sysconfdir/rc.d/init.d/
install -m 0755 %SOURCE2 %buildroot/%_sysconfdir/rc.d/init.d/ksysguardd

#
install -m0644 %SOURCE12 %buildroot/%_K3apps/kicker/wallpapers/default1.png

# Service menus
install -m644 %SOURCE2001 %buildroot/%_K3apps/konqueror/servicemenus/convertpdftops.desktop
install -m644 %SOURCE2002 %buildroot/%_K3apps/konqueror/servicemenus/convertpstopdf.desktop
# Autostart menu
install -m644 %SOURCE2003 %buildroot/%_K3xdg_apps/Autostart.desktop

# Add chksession support
install -d -m 0755 %buildroot/%x11confdir/wmsession.d/
%_K_if_ver_gteq %glibc_core_ver 2.10
cat <<__EOF__ > %buildroot/%x11confdir/wmsession.d/02KDE3
NAME=KDE3
%else
cat <<__EOF__ > %buildroot/%x11confdir/wmsession.d/01KDE3
NAME=KDE
%endif
ICON=%_iconsdir/crystalsvg/64x64/apps/kmenu.png
DESC=The K Desktop Environment
EXEC=%_bindir/startkde3
SCRIPT:
exec %_bindir/startkde3
__EOF__

mkdir -p %buildroot/%_bindir
ln -s `relative %_K3bindir/startkde %_bindir/startkde3` %buildroot/%_bindir/startkde3
ln -s startkde3 %buildroot/%_bindir/startkde

# Create menu directories
install -d %buildroot/%_menudir/

#perl -pi -e "s|^NoDisplay.*$||g" %buildroot/%_K3applnk/KControl.desktop
perl -pi -e "s|^Exec\=kcmshell.*printmgr.*$|Exec=kcmshell printers|g" %_bKmenudir/printers.desktop
perl -pi -e "s|^Exec\=kcmshell.*printmgr.*$|Exec=kcmshell printers|g"  %_bKapplnk/Settingsmenu/printmgr.desktop

cat <<__EOF__ > %buildroot/%_menudir/%name-session
?package(%name-wm): needs=wm \
                        section="Session/Windowmanagers" \
			title="KDE3" \
			longtitle="K Desktop Environment" \
			command="%_bindir/startkde3" \
			icon="go.png"
__EOF__

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_x11bindir/xvt	%_K3bindir/konsole	15
__EOF__
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name-konqueror <<__EOF__
%_bindir/xbrowser	%_K3bindir/konqueror	50
__EOF__
mv %buildroot/%_K3bindir/kdesu %buildroot/%_K3bindir/kdesu-kde
ln -s kdesu-kde %buildroot/%_K3bindir/kdesu
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde-kdesu <<__EOF__
%_K3bindir/kdesu %_K3bindir/kdesu-kde	10
__EOF__

mkdir %buildroot/%_K3exec/
%if %with_kdm
mv %buildroot/%_K3bindir/kdm %buildroot/%_K3exec/kdm
mv %buildroot/%_K3bindir/kdm_config %buildroot/%_K3exec/kdm_config
mv %buildroot/%_K3bindir/kdmctl %buildroot/%_K3exec/kdmctl
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde-kdm <<__EOF__
%_bindir/kdm	%_K3exec/kdm	10
%_bindir/kdm_config	%_K3exec/kdm_config	%_K3exec/kdm
%_bindir/kdmctl	%_K3exec/kdmctl	%_K3exec/kdm
__EOF__
ln -s %_K3bindir/kdm_greet %buildroot/%_K3exec/kdm_greet
ln -s %_K3bindir/krootimage %buildroot/%_K3exec/krootimage

%__mkdir_p %buildroot/%x11confdir/kdm
cp kdm/syscfg/* %buildroot/%x11confdir/kdm

%endif
#
rm -fr %buildroot/%_K3apps/kdm/pics/users %buildroot/%_K3apps/kdm/faces
mkdir -p %buildroot/%_localstatedir/kdm/faces

# Sync with design
rm -f %buildroot/%_K3datadir/apps/kdewizard/pics/wizard_small.png
ln -s %_datadir/design/current/kde/ktip-wizard_small.png %buildroot/%_K3datadir/apps/kdewizard/pics/wizard_small.png
#
mv %buildroot/%_K3apps/ksplash/Themes/Default %buildroot/%_K3apps/ksplash/Themes/Default-kde
subst "s|^.*KSplash.*Theme.*\:.*efault.*].*$|[KSplash Theme: Default-kde]|" \
    %buildroot/%_K3apps/ksplash/Themes/Default-kde/Theme.rc
ln -s `relative %_datadir/design/current/kde/splash/pics %_K3apps/ksplash/Themes/Default` %buildroot/%_K3apps/ksplash/Themes/Default
#
mv -f %buildroot/%_K3wall/default_blue.jpg %buildroot/%_K3wall/kde_blue.jpg
ln -s `relative %_datadir/design/current/backgrounds/default.png %_K3wall/default_blue.jpg` %buildroot/%_K3wall/default_blue.jpg
#
%if %with_kdm
ln -sf `relative %_datadir/design/current/kde/kdm/color-scheme.kcsrc %_K3apps/kdisplay/color-schemes/kdm_default_scheme.kcsrc` \
    %buildroot/%_K3apps/kdisplay/color-schemes/kdm_default_scheme.kcsrc
%endif
#
pushd %buildroot/%_K3apps/kicker/pics
for n in kside*.png
do
    rm -f $n ; ln -s %_datadir/design/current/kde/kicker/pics/"$n" $n
done
popd
#
[ -f %buildroot/%_K3apps/konqueror/tiles/default.png ] \
    && mv %buildroot/%_K3apps/konqueror/tiles/default.png %buildroot/%_K3apps/konqueror/tiles/default_kde.png
#ln -sf %_datadir/design/current/kde/konqueror/tile.png %buildroot/%_K3apps/konqueror/tiles/default.png

install -d -m 0755 %buildroot/%_sysconfdir/profile.d/

ln -s kde3/libkfontviewpart.so %buildroot/%_K3libdir/libkfontviewpart.so

mkdir -p %buildroot/%_sysconfdir/logrotate.d
%if %with_kdm
install -m 0644 %SOURCE11 %buildroot/%_sysconfdir/logrotate.d/kdm
%endif

mkdir -p %buildroot/%_sysconfdir/firsttime.d
%if %with_kdm
install -m 0755 %SOURCE3 %buildroot/%_sysconfdir/firsttime.d/kdm
%endif

if [ -n "`find %buildroot/%_K3datadir/share -type f`" ]; then
    mv %buildroot/%_K3datadir/share/* %buildroot/%_K3datadir/
    rm -rf %buildroot/%_K3datadir/share
fi

mkdir -p %buildroot%_datadir/desktop-directories/kde3/
find %buildroot%_K3datadir/desktop-directories -type f | while read f; do
     newname=`basename $f | sed -e 's,^kde-,,'`
     mv $f %buildroot%_datadir/desktop-directories/kde3/$newname
done

# add desktop categories
#desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=TextTools %buildroot%_K3xdg_apps/klipper.desktop
#desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Documentation %buildroot%_K3xdg_apps/ktip.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Printing --add-category=HardwareSettings %buildroot%_K3xdg_apps/kdeprintfax.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Printing --add-category=HardwareSettings %buildroot%_K3xdg_apps/kjobviewer.desktop

desktop-file-install --dir %buildroot%_K3xdg_apps \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/tab-separated-values \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	--add-category=Utility \
	%buildroot%_K3xdg_apps/kwrite.desktop

desktop-file-install --dir %buildroot%_K3xdg_apps \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/tab-separated-values \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	--add-category=Utility \
	%buildroot%_K3xdg_apps/kate.desktop

%find_lang --output=kryptomedia.lang kryptomedia

#ALT settings
cp altlinux/bookmarks/* %buildroot/%_K3datadir
install -dm 0755 %buildroot/%_K3apps/kdisplay/color-schemes/
install -m 0644 altlinux/kde-settings-Default-alt.kcsrc %buildroot/%_K3apps/kdisplay/color-schemes/ALT_Default.kcsrc
install -dm 0755 %buildroot/%_Kconfig
cp -ar altlinux/set/* %buildroot/%_Kconfig
install -dm 0755 %buildroot/%_K3cfg
cp -ar altlinux/kcfg/* %buildroot/%_K3cfg

%post kdm
if [ -d %_localstatedir/kdm/faces -a -f %_datadir/design/current/faces/default.png -a ! -e %_localstatedir/kdm/faces/.default.face.icon ]
then
    %__cp -af %_datadir/design/current/faces/default.png %_localstatedir/kdm/faces/.default.face.icon ||:
    for f in `/bin/ls %_K3apps/kdm/faces/* 2>/dev/null`
    do
        %__cp -au $f %_localstatedir/kdm/faces/ ||:
    done
fi
%triggerpostun kdm -- kdebase-kdm < %major.%minor
%_K3bindir/genkdmconf --old-confs --old-scripts --in %x11confdir/kdm ||:


%files

%files common
%config(noreplace) %_Kconfig/*
%config(noreplace) %_sysconfdir/pam.d/kde
%config(noreplace) %_sysconfdir/pam.d/kde-np
%config %_sysconfdir/ksysguarddrc
%_datadir/kde/*bookmarks*
%_bindir/kde3
%_bindir/trinity
%_bindir/startkde
%_bindir/startkde3
%dir %_K3apps/kdisplay/
%_K3apps/kdisplay/color-schemes/
%_K3iconsdir/*/*/*/*.*
%_kde3_iconsdir/*/*/*/*.*
%_K3conf/*
%_K3cfg/*

%files kwrite
%_K3bindir/kate
%_K3bindir/kwrite
%_K3libdir/libkdeinit_kate.so*
%_K3libdir/libkateinterfaces.so*
%_K3libdir/libkateutils.so*
%_K3libdir/libkdeinit_kwrite.so*
%_K3lib/kate.so
%_K3lib/kwrite.so
%_K3xdg_apps/kate.desktop
%_K3xdg_apps/kwrite.desktop
%_K3apps/kate
%_K3apps/kwrite
%_K3srvtyp/kateplugin.desktop
%doc %_K3doc/en/kate
%doc %_K3doc/en/kwrite

%files libkonq
%_K3bindir/klocaldomainurifilterhelper
#
%_K3libdir/libkonq.so*
%_K3libdir/libkonqsidebarplugin.so*
#
%_K3lib/kded_favicons.so*
%_K3lib/libkshorturifilter.so*
%_K3lib/libkuriikwsfilter.so*
%_K3lib/libkurisearchfilter.so*
%_K3lib/liblocaldomainurifilter.so*
%_K3apps/kbookmark/directory_bookmarkbar.desktop
%_K3apps/kconf_update/favicons.upd
%_K3apps/kconf_update/kuriikwsfilter.upd
%_K3apps/kconf_update/move_favicons.sh
%_K3apps/konqueror/pics/
%_K3srv/kded/favicons.desktop
%_K3srv/kshorturifilter.desktop
%_K3srv/kuriikwsfilter.desktop
%_K3srv/kurisearchfilter.desktop
%_K3srv/localdomainurifilter.desktop
%_K3srvtyp/konqpopupmenuplugin.desktop

%files kio
%_K3bindir/kio_media_mounthelper
%_K3lib/kded_mediamanager.so*
%_K3lib/kfile_media.so*
%_K3srv/kded/mediamanager.desktop
%_K3mimelnk/media/
%_K3srv/kfile_media.desktop
%_K3srv/media.protocol
%_K3lib/kded_medianotifier.so*
%_K3srv/kded/medianotifier.desktop
%if %with_hal
#%_K3bindir/kryptomedia
%_K3lib/media_propsdlgplugin.so*
%_K3srv/media_propsdlgplugin.desktop
%endif
%_K3lib/kcm_media.so*
%_K3xdg_apps/media.desktop
#
%_K3bindir/ktrash
#
%_K3lib/cursorthumbnail.so*
%_K3lib/djvuthumbnail.so*
%_K3lib/exrthumbnail.so*
%_K3lib/htmlthumbnail.so*
%_K3lib/imagethumbnail.so*
%_K3lib/kcm_cgi.so*
#
%_K3lib/kded_remotedirnotify.so*
%_K3lib/kded_systemdirnotify.so*
%_K3lib/kded_kdeintegration.so*
%_K3lib/kfile_trash.so*
%_K3lib/kio_*.so*
%exclude %_K3lib/kio_print.so*
%_K3lib/libkmanpart.so*
%_K3lib/textthumbnail.so*
#
%_K3xdg_apps/kcmcgi.desktop
#
%_K3apps/kio_man/
%_K3apps/kio_finger/
%_K3apps/kio_info/
%if %with_smb
%_K3apps/konqueror/dirtree/remote/smb-network.desktop
%_K3apps/remoteview/smb-network.desktop
%endif
%_K3apps/systemview/
%exclude %_K3apps/systemview/users.desktop
#
%if %with_smb
%_K3mimelnk/application/x-smb-server.desktop
%_K3mimelnk/application/x-smb-workgroup.desktop
%endif
%_K3mimelnk/inode/system_directory.desktop
#
%_K3srv/about.protocol
%_K3srv/applications.protocol
%_K3srv/ar.protocol
%_K3srv/bzip.protocol
%_K3srv/bzip2.protocol
%_K3srv/cgi.protocol
%_K3srv/cursorthumbnail.desktop
%_K3srv/djvuthumbnail.desktop
%_K3srv/exrthumbnail.desktop
%_K3srv/finger.protocol
%_K3srv/fish.protocol
%_K3srv/floppy.protocol
%_K3srv/gzip.protocol
%_K3srv/htmlthumbnail.desktop
%_K3srv/imagethumbnail.desktop
%_K3srv/info.protocol
%_K3srv/kded/remotedirnotify.desktop
%_K3srv/kded/systemdirnotify.desktop
%_K3srv/kfile_trash.desktop
%_K3srv/kmanpart.desktop
%_K3srv/ldap.protocol
%_K3srv/ldaps.protocol
%_K3srv/mac.protocol
%_K3srv/man.protocol
%_K3srv/nfs.protocol
%_K3srv/nntp.protocol
%_K3srv/pop3.protocol
%_K3srv/pop3s.protocol
%_K3srv/programs.protocol
%_K3srv/remote.protocol
%_K3srv/settings.protocol
%_K3srv/sftp.protocol
%if %with_smb
%_K3srv/smb.protocol
%endif
%_K3srv/smtp.protocol
%_K3srv/smtps.protocol
%_K3srv/system.protocol
%_K3srv/tar.protocol
%_K3srv/textthumbnail.desktop
%_K3srv/thumbnail.protocol
%_K3srv/trash.protocol
%_K3srv/zip.protocol
%_K3srv/home.protocol
%_K3srv/nntps.protocol
%_K3srv/nxfish.protocol
%_K3srv/kfile_trash_system.desktop
#
%_K3srvtyp/thumbcreator.desktop
#
%doc %_K3doc/en/kioslave

%files libs -f kryptomedia.lang
%exclude %_sysconfdir/xdg/menus/applications-merged/*.menu
%exclude %_sysconfdir/xdg/menus/*.menu
#
%attr(2711,root,chkpwd) %_K3bindir/kcheckpass
%attr(2711,root,nobody) %_K3bindir/kdesud
%_K3bindir/drkonqi
%_K3bindir/kcminit
%_K3bindir/kdcop
%_K3bindir/kdebugdialog
%_K3bindir/kdesu
%_K3bindir/kdesu-kde
%_K3bindir/kdialog
%_K3bindir/khotkeys
%_K3bindir/knetattach
%_K3bindir/kreadconfig
%_K3bindir/kstart
%_K3bindir/ksystraycmd
%_K3bindir/kwriteconfig
%_K3bindir/kxkb
%_K3bindir/kcminit_startup
%_K3bindir/kxdglauncher
%_K3bindir/krootbacking
%_K3bindir/tsak
#
%dir %_K3libdir/kconf_update_bin
%_K3libdir/kconf_update_bin/khotkeys_update
%_K3libdir/libkdeinit_kcminit.so*
%_K3libdir/libkdeinit_khotkeys.so*
%_K3libdir/libkdeinit_kxkb.so*
%_K3libdir/libkdeinit_kcminit_startup.so*
%_K3libdir/libkhotkeys_shared.so*
#
%_K3lib/kcminit_startup.so*
%_K3lib/kcm_keyboard.so*
%_K3lib/kcm_displayconfig.so*
%_K3lib/kcm_khotkeys.so*
%_K3lib/kcminit.so*
%_K3lib/kded_khotkeys.so*
%_K3lib/khotkeys.so*
%_K3lib/kxkb.so*
#
%_K3xdg_apps/keyboard.desktop
%_K3xdg_apps/keyboard_layout.desktop
%_K3xdg_apps/khotkeys.desktop
%_K3xdg_apps/knetattach.desktop
#
#%_K3applnk/.hidden/.directory
%_K3applnk/.hidden/battery.desktop
%_K3applnk/.hidden/bwarning.desktop
%_K3applnk/.hidden/cwarning.desktop
%_K3applnk/.hidden/email.desktop
%_K3applnk/.hidden/kcmkxmlrpcd.desktop
%_K3applnk/.hidden/passwords.desktop
%_K3applnk/.hidden/power.desktop
%_K3applnk/.hidden/socks.desktop
%_K3applnk/.hidden/userinfo.desktop
%_K3applnk/.hidden/virtualdesktops.desktop
%_K3applnk/System/ScreenSavers/KBlankscreen.desktop
%_K3applnk/System/ScreenSavers/KRandom.desktop
#
%_K3apps/drkonqi/debuggers/gdbrc
%_K3apps/drkonqi/pics/konqi.png
%_K3apps/drkonqi/presets/developerrc
%_K3apps/drkonqi/presets/enduserrc
%_K3apps/kconf_update/khotkeys_printscreen.upd
%_K3apps/kconf_update/khotkeys_32b1_update.upd
%_K3apps/kdcop/kdcopui.rc
%_K3apps/khotkeys/
%_K3start/khotkeys.desktop
%_K3srv/kded/khotkeys.desktop
%_K3srv/kded/kdeintegration.desktop
%_K3srv/kxkb.desktop
%_K3apps/kconf_update/convertShortcuts.pl
%_K3apps/kconf_update/kaccel.upd
%_K3apps/kconf_update/kcmdisplayrc.upd
%_K3apps/kconf_update/socks.upd
#
%_K3i18n/*
%if %with_smb
%dir %_K3apps/remoteview/
%endif
#
%doc %_K3doc/en/kdebugdialog/
%doc %_K3doc/en/kdcop/
%doc %_K3doc/en/knetattach/
#
%_K3lib/kcm_crypto.so*
%_K3lib/kcm_css.so*
%_K3lib/kcm_filetypes.so*
%_K3lib/kcm_kio.so*
%_K3lib/kcm_konq.so*
%_K3lib/kcm_kurifilt.so*
%_K3lib/kcm_konqhtml.so*
%_K3lib/plugins/integration/libqtkde.so*
%_K3xdg_apps/cache.desktop
%_K3xdg_apps/cookies.desktop
%_K3xdg_apps/crypto.desktop
%_K3xdg_apps/ebrowsing.desktop
%_K3xdg_apps/filetypes.desktop
%_K3xdg_apps/kcmcss.desktop
%_K3xdg_apps/khtml_behavior.desktop
%_K3xdg_apps/khtml_fonts.desktop
%_K3xdg_apps/khtml_java_js.desktop
%_K3xdg_apps/netpref.desktop
%_K3xdg_apps/proxy.desktop
%_K3xdg_apps/useragent.desktop
#%_K3applnk/Settings/WebBrowsing/khtml_appearance.desktop
#%_K3applnk/Settings/WebBrowsing/nsplugin.desktop
#%_K3applnk/Settings/WebBrowsing/smb.desktop
%_K3apps/kcmcss/template.css
%_K3xdg_apps/lanbrowser.desktop
%_K3apps/kconf_update/konqueror_gestures_trinity21_update.upd

%files -n kde3-menu-resources
%_datadir/desktop-directories/kde3

%files wm
%config %_sysconfdir/alternatives/packages.d/kde-kdesu
%config %_sysconfdir/alternatives/packages.d/%name
%config %_sysconfdir/rc.d/init.d/ksysguardd
%config(noreplace) %x11confdir/wmsession.d/*KDE*
%config(noreplace) %_sysconfdir/pam.d/kscreensaver
#
%attr(2711,root,utempter) %_K3bindir/konsole
#%attr(2711,root,utempter) %_K3bindir/kwrited
%if_enabled userpasswd
%else
%_K3bindir/kdepasswd
%_K3xdg_apps/kdepasswd.desktop
%endif
%_K3bindir/khc_beagle_*.pl
%_K3bindir/mailsettings
%_K3bindir/startkde
%_K3bindir/kwin_rules_dialog
%_K3bindir/kapplymousetheme
#%_K3bindir/kio_system_documenthelper
%_K3bindir/kompmgr
%_K3bindir/krandrtray
%_K3bindir/appletproxy
%_K3bindir/extensionproxy
%_K3bindir/kappfinder
%_K3bindir/kasbar
%_K3bindir/kblankscrn.kss
%_K3bindir/krandom.kss
%_K3bindir/kcheckrunning
%_K3bindir/kcontroledit
%_K3bindir/kdeeject
%_K3bindir/kdesktop
%_K3bindir/kdesktop_lock
%_K3bindir/kfind
%_K3bindir/khc_docbookdig.pl
%_K3bindir/khc_htdig.pl
%_K3bindir/khc_htsearch.pl
%_K3bindir/khc_indexbuilder
%_K3bindir/khc_mansearch.pl
%_K3bindir/khelpcenter
%_K3bindir/kicker
%_K3bindir/klipper
%_K3bindir/kmenuedit
%_K3bindir/kpager
%_K3bindir/kpersonalizer
%_K3bindir/kpm
%_K3bindir/ksmserver
%_K3bindir/ksplash
%_K3bindir/ksplashsimple
%_K3bindir/ksysguard
%_K3bindir/ksysguardd
%_K3bindir/ktip
%_K3bindir/kwebdesktop
%_K3bindir/kwin
%_K3bindir/kwin_killer_helper
#
%_K3libdir/kconf_update_bin/kicker-3.4-reverseLayout
%_K3libdir/kconf_update_bin/kwin_*
%_K3libdir/libkasbar.so*
%_K3libdir/libkdecorations.so*
%_K3libdir/libkdeinit_appletproxy.so*
%_K3libdir/libkdeinit_extensionproxy.so*
%_K3libdir/libkdeinit_kcontroledit.so*
%_K3libdir/libkdeinit_kdesktop.so*
%_K3libdir/libkdeinit_khelpcenter.so*
%_K3libdir/libkdeinit_kicker.so*
%_K3libdir/libkdeinit_klipper.so*
%_K3libdir/libkdeinit_kmenuedit.so*
%_K3libdir/libkdeinit_konsole.so*
%_K3libdir/libkdeinit_ksmserver.so*
%_K3libdir/libkdeinit_kwin.so*
%_K3libdir/libkdeinit_kwin_rules_dialog.so*
%_K3libdir/libkickoffsearch_interfaces.so*
%_K3libdir/libkickermain.so*
%_K3libdir/libksgrd.so*
%_K3libdir/libksplashthemes.so*
%_K3libdir/libtaskbar.so*
%_K3libdir/libtaskmanager.so*
#
%_K3lib/kcm_randr.so*
%_K3lib/kded_homedirnotify.so*
%_K3lib/appletproxy.so*
%_K3lib/clock_panelapplet.so*
%_K3lib/dockbar_panelextension.so*
%_K3lib/extensionproxy.so*
%_K3lib/kasbar_panelextension.so*
%_K3lib/kcm_konsole.so*
%_K3lib/kcm_ksplashthemes.so*
%_K3lib/kcm_kwindecoration.so*
%_K3lib/kcm_kwinoptions.so*
%_K3lib/kcm_kwinrules.so*
%_K3lib/kcm_useraccount.so*
%_K3lib/kcontroledit.so*
%_K3lib/kded_kwrited.so*
%_K3lib/kdesktop.so*
%_K3lib/kgreet_*.so*
%_K3lib/khelpcenter.so*
%_K3lib/kicker.so*
%_K3lib/kickermenu_kate.so
%_K3lib/kickermenu_find.so*
%_K3lib/kickermenu_kdeprint.so*
%_K3lib/kickermenu_konqueror.so*
%_K3lib/kickermenu_konsole.so*
%_K3lib/kickermenu_prefmenu.so*
%_K3lib/kickermenu_recentdocs.so*
%_K3lib/kickermenu_remotemenu.so*
%_K3lib/kickermenu_systemmenu.so*
%_K3lib/klipper.so*
%_K3lib/klipper_panelapplet.so*
%_K3lib/kmenuedit.so*
%_K3lib/konsole.so*
%_K3lib/ksmserver.so*
%_K3lib/ksplashdefault.so*
%_K3lib/ksplashredmond.so*
%_K3lib/ksplashstandard.so*
%_K3lib/ksplashunified.so*
%_K3lib/kwin.so*
%_K3lib/kwin3_b2.so*
%_K3lib/kwin3_default.so*
%_K3lib/kwin3_keramik.so*
%_K3lib/kwin3_laptop.so*
%_K3lib/kwin3_modernsys.so*
%_K3lib/kwin3_plastik.so*
%_K3lib/kwin3_quartz.so*
%_K3lib/kwin3_redmond.so*
%_K3lib/kwin3_web.so*
%_K3lib/kwin_b2_config.so*
%_K3lib/kwin_default_config.so*
%_K3lib/kwin_keramik_config.so*
%_K3lib/kwin_modernsys_config.so*
%_K3lib/kwin_plastik_config.so*
%_K3lib/kwin_quartz_config.so*
%_K3lib/kwin_rules_dialog.so*
%_K3lib/launcher_panelapplet.so*
%_K3lib/libkfindpart.so*
%_K3lib/libkonsolepart.so*
%_K3lib/lockout_panelapplet.so*
%_K3lib/media_panelapplet.so*
%_K3lib/menu_panelapplet.so*
%_K3lib/minipager_panelapplet.so*
%_K3lib/naughty_panelapplet.so*
%_K3lib/run_panelapplet.so*
%_K3lib/sidebar_panelextension.so*
%_K3lib/sysguard_panelapplet.so*
%_K3lib/systemtray_panelapplet.so*
%_K3lib/taskbar_panelapplet.so*
%_K3lib/taskbar_panelextension.so*
%_K3lib/trash_panelapplet.so*
#
%_K3xdg_apps/Help.desktop
%_K3xdg_apps/Kfind.desktop
%_K3xdg_apps/kappfinder.desktop
%_K3xdg_apps/kcm_useraccount.desktop
%_K3xdg_apps/kcmkicker.desktop
%_K3xdg_apps/klipper.desktop
%_K3xdg_apps/kmenuedit.desktop
%_K3xdg_apps/konsole.desktop
%_K3xdg_apps/konsolesu.desktop
%_K3xdg_apps/kpager.desktop
%_K3xdg_apps/kpersonalizer.desktop
%_K3xdg_apps/ksplashthememgr.desktop
%_K3xdg_apps/ksysguard.desktop
%_K3xdg_apps/ktip.desktop
%_K3xdg_apps/kwindecoration.desktop
%_K3xdg_apps/kwinoptions.desktop
%_K3xdg_apps/kwinrules.desktop
%_K3xdg_apps/krandrtray.desktop
%_K3xdg_apps/showdesktop.desktop
#
%_K3applnk/.hidden/kicker_config_arrangement.desktop
%_K3applnk/.hidden/kicker_config_hiding.desktop
%_K3applnk/.hidden/kicker_config_menus.desktop
%_K3applnk/.hidden/kcmkonsole.desktop
%_K3applnk/.hidden/kwinactions.desktop
%_K3applnk/.hidden/kwinadvanced.desktop
%_K3applnk/.hidden/kwinfocus.desktop
%_K3applnk/.hidden/kwinmoving.desktop
%_K3applnk/.hidden/kwintranslucency.desktop
%_K3applnk/System/kappfinder.desktop
%_K3applnk/System/kmenuedit.desktop
%_K3applnk/System/kpersonalizer.desktop
%_K3applnk/Toys/ktip.desktop
%_K3applnk/Utilities/kpager.desktop
#
%_K3apps/clockapplet/
%_K3apps/kaccess/
%_K3apps/kappfinder/
%_K3apps/kconf_update/kate-2.4.upd
%_K3apps/kconf_update/kicker-3.1-properSizeSetting.pl
%_K3apps/kconf_update/kickerrc.upd
%_K3apps/kconf_update/klipper-1-2.pl
%_K3apps/kconf_update/klipper-trinity1.sh
%_K3apps/kconf_update/klipperrc.upd
%_K3apps/kconf_update/klippershortcuts.upd
%_K3apps/kconf_update/konsole.upd
%_K3apps/kconf_update/ksmserver.upd
%_K3apps/kconf_update/kwin.upd
%_K3apps/kconf_update/kwin3_*
%_K3apps/kconf_update/kwin_*
%_K3apps/kconf_update/kwiniconify.upd
%_K3apps/kconf_update/kwinsticky.upd
%_K3apps/kconf_update/kwinupdatewindowsettings.upd
%_K3apps/kconf_update/move_session_config.sh
%_K3apps/kconf_update/pluginlibFix.pl
%_K3apps/kconf_update/schemaStrip.pl
%_K3apps/kconf_update/kicker-3.5-kconfigXTize.pl
%_K3apps/kconf_update/kicker-3.5-taskbarEnums.pl
%_K3apps/kconf_update/mouse_cursor_theme.upd
%_K3apps/kcontroledit/
%_K3apps/kdesktop/
%exclude %_K3apps/kdesktop/DesktopLinks/*
%_K3apps/kdewizard/
%_K3apps/kicker/
%exclude %_K3apps/kicker/default-apps
%_K3apps/kfindpart/
%_K3apps/khelpcenter/
%_K3apps/kmenuedit/
%_K3apps/konsole/
%_K3apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%_K3apps/konqueror/servicemenus/konsolehere.desktop
%_K3apps/kpersonalizer/
%_K3apps/ksmserver/
%_K3apps/ksplash/
%_K3apps/ksysguard/
%_K3apps/kwin/
%_K3apps/naughtyapplet/
#
%_K3start/kdesktop.desktop
%_K3start/klipper.desktop
%_K3start/ktip.desktop
%_K3start/panel.desktop
%_K3start/krandrtray-autostart.desktop
#
%_K3mimelnk/application/x-konsole.desktop
%_K3mimelnk/application/x-ksysguard.desktop
%_K3mimelnk/fonts/package.desktop
#
%_K3srv/kded/kwrited.desktop
%_K3srv/kfindpart.desktop
%_K3srv/khelpcenter.desktop
%_K3srv/konsole-script.desktop
%_K3srv/konsolepart.desktop
%_K3srv/ksplash.desktop
%_K3srv/ksplashdefault.desktop
%_K3srv/ksplashredmond.desktop
%_K3srv/ksplashstandard.desktop
%_K3srv/ksplashunified.desktop
%_K3srv/kwrited.desktop
%_K3srv/kded/homedirnotify.desktop
#
%_K3srvtyp/findpart.desktop
%_K3srvtyp/ksplashplugins.desktop
%_K3srvtyp/terminalemulator.desktop
%_K3srvtyp/kickoffsearchplugin.desktop
#
%_K3snd/pop.wav
%_K3snd/KDE_*.*
%_K3tmpl
%_K3wall/*
#
%_menudir/%name-session
#
#%doc %_K3doc/en/kappfinder
%doc %_K3doc/en/kdesu
%doc %_K3doc/en/kfind
%doc %_K3doc/en/kicker
%doc %_K3doc/en/klipper
%doc %_K3doc/en/kmenuedit
%doc %_K3doc/en/kompmgr
%doc %_K3doc/en/konsole
%doc %_K3doc/en/kpager
%doc %_K3doc/en/ksplashml
%doc %_K3doc/en/kxkb
%doc %_K3doc/en/khelpcenter
%doc %_K3doc/en/ksysguard


%files kdeprint
%_K3bindir/kdeprintfax
%_K3bindir/kjobviewer
%_K3bindir/kprinter
#
%_K3libdir/libkdeinit_kjobviewer.so*
%_K3libdir/libkdeinit_kprinter.so*
#
%_K3lib/kcm_printmgr.so*
%_K3lib/kio_print.so*
%_K3lib/kjobviewer.so*
%_K3lib/kprinter.so*
%_K3lib/libkdeprint_part.so*
#
%_K3xdg_apps/kdeprintfax.desktop
%_K3xdg_apps/kjobviewer.desktop
%_K3xdg_apps/printers.desktop
#%_K3applnk/Settingsmenu/printmgr.desktop
#
%_K3apps/kdeprint/
%_K3apps/kdeprint_part/
%_K3apps/kdeprintfax/
%_K3apps/kjobviewer/
%_K3mimelnk/print/
%_K3srv/kdeprint_part.desktop
%_K3srv/print.protocol
%_K3srv/printdb.protocol
#
%doc %_K3doc/en/kdeprint


%files konqueror
%config /%_sysconfdir/alternatives/packages.d/%name-konqueror
#
%_K3bindir/kbookmarkmerger
%_K3bindir/keditbookmarks
%_K3bindir/kfmclient
%_K3bindir/konqueror
%_K3bindir/nspluginscan
%_K3bindir/nspluginviewer
#
%_K3libdir/libkdeinit_keditbookmarks.so*
%_K3libdir/libkdeinit_kfmclient.so*
%_K3libdir/libkdeinit_konqueror.so*
#
%_K3lib/kcm_history.so*
%_K3lib/kcm_nsplugins.so*
%_K3lib/kded_konqy_preloader.so*
%_K3lib/keditbookmarks.so*
%_K3lib/kfmclient.so*
%_K3lib/konq_aboutpage.so*
%_K3lib/konq_iconview.so*
%_K3lib/konq_listview.so*
%_K3lib/konq_remoteencoding.so*
%_K3lib/konq_shellcmdplugin.so*
%_K3lib/konq_sidebar.so*
%_K3lib/konq_sidebartree_bookmarks.so*
%_K3lib/konq_sidebartree_dirtree.so*
%_K3lib/konq_sidebartree_history.so*
%_K3lib/konqsidebar_tree.so*
%_K3lib/konqsidebar_web.so*
%_K3lib/konqueror.so*
%_K3lib/libkhtmlkttsdplugin.so*
%_K3lib/libnsplugin.so*
#
%_K3xdg_apps/Autostart.desktop
%_K3xdg_apps/Home.desktop
%_K3xdg_apps/kcmhistory.desktop
%_K3xdg_apps/kfmclient.desktop
%_K3xdg_apps/kfmclient_dir.desktop
%_K3xdg_apps/kfmclient_html.desktop
%_K3xdg_apps/kfmclient_war.desktop
%_K3xdg_apps/khtml_plugins.desktop
%_K3xdg_apps/konqbrowser.desktop
%_K3xdg_apps/konquerorsu.desktop
%_K3xdg_apps/khtml_filter.desktop
#
#%_K3applnk/Internet/keditbookmarks.desktop
%_K3applnk/konqueror.desktop
%_K3applnk/.hidden/konqfilemgr.desktop
%_K3applnk/.hidden/filebehavior.desktop
%_K3applnk/.hidden/fileappearance.desktop
%_K3applnk/.hidden/filepreviews.desktop
%_K3applnk/.hidden/kcmkonq.desktop
%_K3applnk/.hidden/konqhtml.desktop
#
%_K3apps/kconf_update/kfmclient_3_2.upd
%_K3apps/kconf_update/kfmclient_3_2_update.sh
%_K3apps/kconf_update/konqsidebartng.upd
%_K3apps/kconf_update/move_konqsidebartng_entries.sh
%_K3apps/keditbookmarks/keditbookmarks-genui.rc
%_K3apps/keditbookmarks/keditbookmarksui.rc
%_K3apps/khtml/kpartplugins/khtmlkttsd.desktop
%_K3apps/khtml/kpartplugins/khtmlkttsd.rc
%_K3apps/konqiconview/konq_iconview.rc
%_K3apps/konqiconview/konq_multicolumnview.rc
%_K3apps/konqiconview/kpartplugins/kremoteencodingplugin.rc
%_K3apps/konqiconview/kpartplugins/kshellcmdplugin.rc
%_K3apps/konqiconview/kpartplugins/kshellcmdplugin.desktop
%_K3apps/konqiconview/kpartplugins/kremoteencodingplugin.desktop
%_K3apps/konqlistview/kpartplugins/kshellcmdplugin.desktop
%_K3apps/konqlistview/kpartplugins/kremoteencodingplugin.desktop
%_K3apps/konqlistview/konq_detailedlistview.rc
%_K3apps/konqlistview/konq_infolistview.rc
%_K3apps/konqlistview/konq_textview.rc
%_K3apps/konqlistview/konq_treeview.rc
%_K3apps/konqlistview/kpartplugins/kremoteencodingplugin.rc
%_K3apps/konqlistview/kpartplugins/kshellcmdplugin.rc
%_K3apps/konqsidebartng/add/virtualfolderadd.desktop
%_K3apps/konqsidebartng/add/webmodule_add.desktop
%_K3apps/konqsidebartng/dirtree/bookmarks_module.desktop
%_K3apps/konqsidebartng/dirtree/dirtree_module.desktop
%_K3apps/konqsidebartng/dirtree/history_module.desktop
%_K3apps/konqsidebartng/entries/.version
%_K3apps/konqsidebartng/entries/bookmarks.desktop
%_K3apps/konqsidebartng/entries/history.desktop
%_K3apps/konqsidebartng/entries/home.desktop
%_K3apps/konqsidebartng/entries/remote.desktop
%_K3apps/konqsidebartng/entries/root.desktop
%_K3apps/konqsidebartng/entries/services.desktop
%_K3apps/konqsidebartng/kicker_entries/
%_K3apps/konqsidebartng/virtual_folders/
%_K3apps/konqsidebartng/websidebar/websidebar.html
%_K3apps/konqsidebartng/entries/system.desktop
%dir %_K3apps/konqueror/
%_K3apps/konqueror/konq-simplebrowser.rc
%_K3apps/konqueror/konqueror.rc
%_K3apps/konqueror/profiles/
%_K3apps/konqueror/about/
%_K3apps/konqueror/icons/
%dir %_K3apps/konqueror/servicemenus/
%_K3apps/konqueror/servicemenus/media_*.desktop
%_K3apps/konqueror/servicemenus/text-*.desktop
%_K3apps/konqueror/servicemenus/convertpdftops.desktop
%_K3apps/konqueror/servicemenus/convertpstopdf.desktop
%dir %_K3apps/konqueror/tiles/
#%_K3apps/konqueror/tiles/default.png
%_K3apps/konqueror/tiles/bluemorning.png
%_K3apps/konqueror/tiles/canvas.png
%_K3apps/konqueror/tiles/kde4ever.png
%_K3apps/konqueror/tiles/kenwimer.png
%_K3apps/konqueror/tiles/noise.png
%_K3apps/konqueror/tiles/paper_flieder.png
%_K3apps/konqueror/tiles/redfiber.png
%_K3apps/plugin
#
%_K3start/konqy_preload.desktop
#
%_K3srv/kded/konqy_preloader.desktop
%_K3srv/konq_*.desktop
%_K3srv/searchproviders/
%_K3srv/useragentstrings/
%_K3srvtyp/searchprovider.desktop
%_K3srvtyp/uasprovider.desktop
#
%_K3srvtyp/konqaboutpage.desktop
#
%doc %_K3doc/en/konqueror

%if %with_kdm
%files kdm
%dir %x11confdir/kdm
%config %x11confdir/kdm/*
%config %_sysconfdir/alternatives/packages.d/kde-kdm
%config %_sysconfdir/firsttime.d/kdm
%config %_sysconfdir/logrotate.d/kdm
#%_K3lib/kgreet_*.so
#
%_K3bindir/genkdmconf
%dir %_K3exec/
%_K3exec/kdm
%_K3exec/kdm_config
%_K3exec/kdmctl
%_K3bindir/kdmtsak
%_K3bindir/kdm_greet
%_K3exec/kdm_greet
%_K3bindir/krootimage
%_K3exec/krootimage
#
%_K3apps/kdm/
%exclude %_K3apps/kdm/sessions/*
#
%_localstatedir/kdm/
#
%doc %_K3doc/en/kdm
%endif

%files kcontrol
%_K3bindir/kaccess
%_K3bindir/kcontrol
%_K3bindir/kdeinstallktheme
%_K3bindir/keditfiletype
%_K3bindir/kfontinst
%_K3bindir/kfontview
%_K3bindir/kinfocenter
%_K3bindir/krdb
%_K3libdir/libkdeinit_kaccess.so*
%_K3libdir/libkdeinit_kcontrol.so*
%_K3libdir/libkfontinst.so*
%_K3libdir/libkfontviewpart.so*
#
%_K3lib/fontthumbnail.so*
%_K3lib/kaccess.so*
%_K3lib/kcm_access.so*
%_K3lib/kcm_arts.so*
%_K3lib/kcm_background.so*
%_K3lib/kcm_bell.so*
%_K3lib/kcm_clock.so*
%_K3lib/kcm_colors.so*
%_K3lib/kcm_componentchooser.so*
%_K3lib/kcm_display.so*
%_K3lib/kcm_energy.so*
%_K3lib/kcm_fontinst.so*
%_K3lib/kcm_fonts.so*
%_K3lib/kcm_iccconfig.so*
%_K3lib/kcm_icons.so*
%_K3lib/kcm_info.so*
%_K3lib/kcm_input.so*
%_K3lib/kcm_ioslaveinfo.so*
%_K3lib/kcm_joystick.so*
%_K3lib/kcm_kded.so*
%_K3lib/kcm_kdm.so*
%_K3lib/kcm_keys.so*
%_K3lib/kcm_kicker.so*
%_K3lib/kcm_knotify.so*
%_K3lib/kcm_kthememanager.so*
%_K3lib/kcm_launch.so*
%_K3lib/kcm_locale.so*
%_K3lib/kcm_nic.so*
%_K3lib/kcm_performance.so*
%_K3lib/kcm_privacy.so*
%_K3lib/kcm_samba.so*
%_K3lib/kcm_screensaver.so*
%_K3lib/kcm_smserver.so*
%_K3lib/kcm_spellchecking.so*
%_K3lib/kcm_style.so*
%_K3lib/kcm_taskbar.so*
%_K3lib/kcm_usb.so*
%_K3lib/kcm_view1394.so*
%_K3lib/kcm_xinerama.so*
%_K3lib/kcontrol.so*
%_K3lib/kcm_kdnssd.so*
%_K3lib/kcm_khotkeys_init.so*
%_K3lib/kfile_font.so*
%_K3lib/kstyle_keramik_config.so*
%_K3lib/libkfontviewpart.so*
%_K3xdg_apps/KControl.desktop
%_K3xdg_apps/arts.desktop
%_K3xdg_apps/background.desktop
%_K3xdg_apps/bell.desktop
%_K3xdg_apps/cdinfo.desktop
%_K3xdg_apps/clock.desktop
%_K3xdg_apps/colors.desktop
%_K3xdg_apps/componentchooser.desktop
%_K3xdg_apps/desktop.desktop
%_K3xdg_apps/desktopbehavior.desktop
%_K3xdg_apps/desktoppath.desktop
%_K3xdg_apps/devices.desktop
%_K3xdg_apps/display.desktop
%_K3xdg_apps/dma.desktop
%_K3xdg_apps/filebrowser.desktop
%_K3xdg_apps/fonts.desktop
%_K3xdg_apps/icons.desktop
%_K3xdg_apps/installktheme.desktop
%_K3xdg_apps/interrupts.desktop
%_K3xdg_apps/ioports.desktop
%_K3xdg_apps/ioslaveinfo.desktop
%_K3xdg_apps/joystick.desktop
%_K3xdg_apps/kcmaccess.desktop
%_K3xdg_apps/kcmfontinst.desktop
%_K3xdg_apps/kcmkded.desktop
%_K3xdg_apps/kcmlaunch.desktop
%_K3xdg_apps/kcmnotify.desktop
%_K3xdg_apps/kcmperformance.desktop
%_K3xdg_apps/kcmsmserver.desktop
%_K3xdg_apps/kcmtaskbar.desktop
%_K3xdg_apps/kcmusb.desktop
%_K3xdg_apps/kcmview1394.desktop
%_K3xdg_apps/kdm.desktop
%_K3xdg_apps/keys.desktop
%_K3xdg_apps/kfontview.desktop
%_K3xdg_apps/kinfocenter.desktop
%_K3xdg_apps/kthememanager.desktop
%_K3xdg_apps/language.desktop
%_K3xdg_apps/memory.desktop
%_K3xdg_apps/mouse.desktop
%_K3xdg_apps/nic.desktop
%_K3xdg_apps/opengl.desktop
%_K3xdg_apps/panel.desktop
%_K3xdg_apps/panel_appearance.desktop
%_K3xdg_apps/partitions.desktop
%_K3xdg_apps/pci.desktop
%_K3xdg_apps/privacy.desktop
%_K3xdg_apps/processor.desktop
%_K3xdg_apps/screensaver.desktop
%_K3xdg_apps/scsi.desktop
%_K3xdg_apps/smbstatus.desktop
%_K3xdg_apps/sound.desktop
%_K3xdg_apps/spellchecking.desktop
%_K3xdg_apps/style.desktop
%_K3xdg_apps/xserver.desktop
%_K3xdg_apps/displayconfig.desktop
%_K3applnk/.hidden/energy.desktop
%_K3applnk/.hidden/kcmkonqyperformance.desktop
%_K3applnk/.hidden/kicker_config.desktop
%_K3applnk/.hidden/kicker_config_appearance.desktop
%_K3applnk/.hidden/randr.desktop
%_K3applnk/.hidden/smb.desktop
%_K3applnk/.hidden/xinerama.desktop
#%_K3applnk/Settings/LookNFeel/Themes/iconthemes.desktop
%_K3applnk/Settings/LookNFeel/kcmtaskbar.desktop
%_K3applnk/Settings/LookNFeel/panel.desktop
#%_K3applnk/Settings/LookNFeel/panel_appearance.desktop
%_K3apps/kcm_componentchooser/
%_K3apps/kcminput/
%_K3apps/kcmkeys/
%_K3apps/kcmlocale/
#%_K3apps/kcmusb/
%_K3apps/kcmview1394/
%_K3apps/kcontrol/
%_K3apps/kdisplay/
%exclude %_K3apps/kdisplay/color-schemes/*
%_K3apps/kfontview/
%_K3apps/kinfocenter/
%_K3apps/konqueror/servicemenus/installfont.desktop
%_K3apps/kthememanager/
%_K3mimelnk/application/x-ktheme.desktop
%_K3mimelnk/fonts/folder.desktop
%_K3mimelnk/fonts/system-folder.desktop
%_K3srv/fonts.protocol
%_K3srv/fontthumbnail.desktop
%_K3srv/kaccess.desktop
%_K3srv/kfile_font.desktop
%_K3srv/kfontviewpart.desktop

%doc %_K3doc/en/kcontrol
%doc %_K3doc/en/kinfocenter
%_K3xdg_apps/kcm_kdnssd.desktop
%_K3xdg_apps/iccconfig.desktop


%files devel
%if %_keep_libtool_files
%_K3libdir/*.la
%_K3lib/*.la
%endif
#
%_K3includedir/kate/
%_K3includedir/ksgrd/
%_K3includedir/ksplash/
%_K3includedir/kwin/
%_K3includedir/K*.h
%_K3includedir/k*.h
%_K3includedir/libkonq_*.h
#%doc %_K3doc/en/kdebase-%version-apidocs
%dir %_K3datadir/cmake
%_K3datadir/cmake/*.cmake


%changelog
* Mon May 14 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt5
- SmoothScrolling store fix.

* Fri May 04 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt4
- ~/.kde/env creation is added to startkde for work some configurations.
- Default ALT configurations for KDE3 is placed from old package kde-settings.
- kxdglauncher is fixed for locale process on access to variable "DOCUMENTS", detected on cyrillic.
- /etc/pam.d/kde is fixed for "root" login from kdm and other allow.
- startkde is adapted for start from "root".

* Wed Mar 14 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt3
- KWin decoration "Keramik" is fixed for pictures embed to binary module.

* Sun Mar 11 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- Memory info display is fixed by define -DHAVE_LONG_LONG

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Thu May 12 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.12-alt12
- added text mimetypes to kate/kwrite

* Tue May 03 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt11
- fix build requires

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.12-alt10
- menu resources renamed to kde3-menu-resources
- added desktop categories

* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.12-alt9
- system freedesktop menu support

* Thu Apr 07 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt8
- add upstream fix against kdesktop startup crash (ALT#25175)

* Fri Mar 25 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt7
- don't save kmix,synaptic and apt-indicator with session

* Thu Mar 24 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt6
- built with hal again
- fix default background and startup splash

* Tue Mar 22 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt5
- built without hal

* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt4
- remove requires to menu package

* Mon Feb 21 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt3
- move to alternate place

* Tue Jan 25 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- fix desktop locking

* Mon Nov 15 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version
- don't package kdm

* Fri Jul 02 2010 Dmitry V. Levin <ldv@altlinux.org> 3.5.10-alt22
- Rewritten PAM config files using common-login; in /etc/pam.d/kde,
  added pam_shells and a non-root check to the auth stack.

* Thu May 20 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt20.M51.1
- build for M51

* Thu May 20 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt21
- fix requires

* Mon May 17 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt19.M51.1
- build for M51

* Mon May 17 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt20
- turn off userpasswd support

* Tue Mar 16 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt18.M51.1
- built for M51

* Tue Mar 16 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt19
- allow to start kde when ~/ path contain spaces (ALT#23136)

* Thu Feb 25 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt17.M51.1
- built for M51

* Thu Feb 25 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt18
- slight libcups requires

* Fri Feb 19 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt16.M41.1
- built for M41

* Fri Feb 19 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt16.M51.1
- built for M51

* Fri Feb 19 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt17
- fix pam-files to use pam_console (ALT#22876)

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt15.M41.1
- built for M41

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt15.M51.1
- built for M51

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt16
- move wmsession upper

* Tue Feb 09 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt14.M41.1
- built for M41

* Tue Feb 09 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt14.M51.1
- built for M51

* Mon Feb 08 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt15
- fix compile with new autoconf
- set pam_console.so optional

* Mon Feb 08 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt13.M41.1
- built for M41

* Thu Nov 12 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt13.M51.1
- built for M51

* Tue Nov 03 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt14
- update from lastest 3.5 branch

* Wed Oct 14 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt13
- rebuilt with libsensors3
- rename wmsession to KDE3

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt12
- rebuilt with libldap2.4

* Mon Jul 06 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt11
- fix to build with new automake
- using shortname=mixed for ms filesystems by default (ALT#19087)
- add patch to compile with gcc-4.4

* Mon Apr 27 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt10
- remove requires to KDE4

* Fri Apr 03 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt9
- fix to build with libusb-compat
- fix pam_loginuid placement in pam-file

* Fri Mar 27 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt8
- add pam_loginuid support (fixes #19361)
- don't use deprecarted macroses
- built kdm with audit support

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt7
- rebuilt

* Thu Oct 02 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt6
- check pointer when usb_close() in `kcmshell mouse`

* Wed Sep 24 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt5
- fix find custom Konqueror bookmarks at first kde start

* Wed Sep 17 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt4
- change kdesktop lock keyboard layout name when changed by keyboard

* Wed Sep 17 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt3
- set proper kdmrc Language at firststart to fix type nonlatin symbols at login
- don't allow fonts:/System

* Fri Sep 05 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt2
- fix view system:/ in konqueror side bar

* Mon Aug 25 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Aug 19 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt11
- remove requires to design-graphics-*, require only design-graphics

* Thu Aug 14 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt10
- fix some directories ownership

* Wed Aug 13 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt9
- fix file conflicts between subpackages
- fix to compile with ssl+krb5; thanks kipruss@alt

* Wed Aug 13 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt8
- use real paths for root system:/ entries

* Fri Apr 18 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt7
- add alternatives support for kdm_config and kdmctl

* Tue Apr 08 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt5
- fix kdm alternatives support

* Tue Apr 08 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt4
- add alternatives support to kdm

* Mon Mar 31 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt3
- add patch from FC for consolekit support

* Wed Mar 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt2
- add alternatives support for kdesu
- remove check for freespace in startkde

* Thu Feb 21 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Tue Feb 12 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt12
- possible to select remote folder in kfind "browse" dialog
- add cups to kdeprint requirements

* Mon Dec 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt11
- fix build requires

* Fri Dec 21 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt10
- udpate patch for new flash to add workaround for gtk_init

* Mon Dec 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt9
- add patch from SuSE to add xembed support to nsplugins for new flash
- update SuSE patches

* Fri Dec 07 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt8
- add Autostart menu entry
- hide Home menu entry
- support distribution-specific Konqueror bookmarks
- don't create trash on desktop by default
- exclude kicker/default-apps to non't override distribution-specific

* Fri Nov 30 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt7
- add icon for kids games menu section

* Wed Nov 28 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt6
- fix minipager applet defaults
- don't show frame in clock applet by default

* Mon Nov 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt5
- don't use LCD style for clock applet by default

* Mon Nov 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt4
- show keyboard layout in kscreensaver dialog with kkbswitch
- clock applet don't blink by default

* Tue Nov 20 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt3
- redesign default panel applets
- exclude default desktop links

* Thu Oct 18 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt2
- start configured terminal application by Ctrl+T on desktop
- remove /usr/share/wallpapers directory ownership

* Tue Oct 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Mon Oct 15 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt17
- use default language from environment variables in `kcmshell locale`
- fix default Russian locale settings; thanks cas@alt

* Mon Sep 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt16
- mount floppy with sync by default

* Wed Sep 12 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt15
- add patch to fix CVS-2007-4569

* Thu Aug 23 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt14
- add pam file for autologin
- add English to `kcmshell kdm` languages list

* Mon Aug 20 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt13
- add patch to fix CVE-2007-3820, CVE-2007-4224, CVE-2007-4225

* Wed Aug 15 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt12
- add kde colors to ksplashml theme 'simple'

* Mon Aug 06 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt11
- fix non-latin symlinks on kdesktop

* Mon Jul 30 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt10
- fix clock applet default settings
- move kcontrol to Settings submenu

* Tue Jul 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt9
- don't set "utf8" media mount option by default on non-utf8 locales

* Mon Jul 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt8
- add patch to fix SA26091
- don't setup BROWSER environment variable in startkde

* Wed Jun 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt7
- add patch to fix kio_man \N'num' sequence handling; thanks stanv@alt

* Mon Jun 25 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt6
- fix path to fuser

* Thu Jun 14 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt5
- fix hal media non-latin mountpoints
- fallback oldstyle floppy drives listing mode in mediamanager hal backend
- add patch to change "halt" to "poweroff" in some places in kdm
- add patch to fix konsole real transparency

* Tue Jun 05 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt4
- don't show hasher sattelite users in kdm

* Thu May 31 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt3
- add path to binary in $BROWSER

* Wed May 30 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- add desktop hiding button to kicker by default
- turn on/off some k-menu extensions by default
- add patch to fix #11682; thanks Alexey Morozov

* Wed May 23 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Wed May 23 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt12
- fix linking

* Tue May 22 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt11
- add kryptosetup utility from SuSE for encrypted starage media

* Mon May 21 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt10
- make QtCurve as default for gtk-2 apps

* Fri May 18 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt9
- update patches from SuSE

* Mon Apr 23 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt8
- add patch to fix media:/ baseURL encoding

* Fri Apr 20 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt7
- add workaround for flash plugin bug

* Thu Mar 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt6
- remove patch for improved http caching

* Mon Mar 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt5
- remove patch against text relocations
- add patch to setup improved http caching
- add patch for mediamanager to take mount options from hal

* Thu Feb 08 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt4
- fix kate opening session with non-latin name; thanks corwin@alt

* Thu Feb 08 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt3
- fix dekstop categories
- don't apply patch for custom mount options

* Mon Feb 05 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- built with hinternal libqt-dbus

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Mon Dec 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt5
- rebuilt with new dbus

* Mon Nov 20 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt4
- fix default kicker icons
- set clock default is digital

* Thu Nov 16 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt3
- don't export KDEHOME KDETMP KDEVARTMP, export KDEROOTHOME
  variables from startkde;

* Wed Oct 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt2
- fix hotkeys kcontrol module crash; thanks corwin@alt
- make spec 3.0 compatable
- add design-graphics background color support for startkde

* Fri Oct 13 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Fri Sep 22 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt4
- fix patch for media mount options; thanks corwin@alt

* Tue Sep 19 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt3
- fix patch for media mount options; thanks corwin@alt

* Mon Sep 18 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt2
- add patch for media mount options; thanks corwin@alt

* Wed Aug 30 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- apply patch for kdeeject
- built with libsmbclient
- add patches from RH

* Fri Jul 14 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt3
- don't apply patch for kdeeject

* Mon Jul 10 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt2
- built without libsmbclient
- add patch form SuSE to search in menu
- fix text relocations; thanks Alexey Morozov

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Thu May 18 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt4
- rebuilt with new gcc
- improve kioslave_media_dbus.patch; thanks Sergey A. Sukiyazov
- don't automount CD/DVD by default

* Tue Apr 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt3
- add patches from FC for dbus/hal

* Thu Apr 13 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt2
- apply Patch1048

* Wed Mar 29 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Mar 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt2
- push incoming@ to build on x86_64

* Tue Jan 31 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new verion

* Thu Jan 12 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt3
- fix watching hal messages

* Tue Jan 10 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt2
- fix window managers list in kdm
- fix man recoding; thanks Sergey A. Sukiyazov

* Fri Dec 02 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Thu Sep 29 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt12
- add support for design-graphics's color scheme for KDM

* Thu Sep 15 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt11
- rebuilt

* Tue Sep 06 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt10
- add one more patch for kcheckpass

* Tue Aug 30 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt9
- add patch for kcheckpass

* Mon Aug 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt8
- fix path to faces in kdm kcontrol module

* Mon Aug 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt7
- forget to apply patch for settings:/ :-(

* Thu Aug 04 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt6
- setup kdm language in firsttime.d

* Wed Aug 03 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt5
- fix updating devices state from HAL in media:/

* Mon Jul 25 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt4
- fix system:/
- fix build requires 

* Thu Jul 21 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt3
- fix requires
- fix alternate background color in kdm user list

* Wed Jul 13 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt2
- rebuilt with new hal
- add patch from FC for default konsole keytab

* Wed Jun 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version
- merge patches from SuSE

* Wed May 04 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt3
- fix %%post
- set default gtk theme to Industrial

* Tue May 03 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt2
- fix modules list in kcontrol and settings:/
- kcmshell userinfo save gecos in utf8
- fix kcmshell devices
- fix kio-fish linking with libutils
- try to usb.ids from hwdatabase first
- mark menus edited by kmenuedit

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Mar 22 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt0.1
- thanks darkstar@alt for patches

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt3
- rebuild

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- don't check 25Mb freespace on /tmp in startkde
- rebuild with gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Tue Jan 04 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Tue Dec 14 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt6
- add patch to fix http://secunia.com/secunia_research/2004-10/advisory/

* Fri Dec 10 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt5
- add patch to remove password from smb URL
- fix path to xvt in alternative
- don't start konqueror via kfmclient from menu
- disable scaling panel icons by default
- fix path to kdm backroundrc in kcontrol
- fix trigger to run genkdmconf when upgrade kdebase-kdm < %%major.%%minor

* Fri Nov 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt4
- fix alternatives files
- fix konsole su session options
- fix konsole default keytabs
- reapply panel-icons-scale-alt.patch

* Tue Oct 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt3
- post_register_alternatives for konqueror

* Fri Oct 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt2
- remove noreplace flag from alternatives files

* Wed Oct 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Thu Sep 30 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Mon Aug 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt9
- fix zip eject on desktop

* Fri Aug 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt8
- add patch for html frames
- add intscript for ksysguardd (disabled by default)

* Wed Jul 14 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt7
- rebuild with openmotif

* Tue Jul 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt6
- add Eject action for Zip on desktop

* Fri Jul 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt5
- apply losted patch for gtk theme
- wrap start-here:/ to programs:/ in konqueror

* Wed Jun 30 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt4
- fix manpage encoding in man:/anything
- remove shadow patch

* Thu Jun 10 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt3
- add update_wms to %%post in %%name-wm

* Tue Jun 08 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- add patch from Bernardo Hung <deciare@gta.igs.net> to kwin dropping shadow

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Thu May 27 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt9
- make panel icons scaling configurable via kcontrol

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt8
- add xbrowser alternative for konqueror

* Fri May 21 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt7
- fix panel-icons-scale patch
- rebuild startkde without -funroll-all-loops :-)
- change icon for wmsession
- remove requires kkbswitch because it present in kde-virtual
- add requires sound_handler
- reapply samba authorization patch
- add requires urw-fonts

* Thu May 13 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt6
- fix open /dev/console in kdm

* Wed May 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt5
- fix requires
- fix %%files
- add quick startkde wmsession

* Thu Apr 29 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt4
- fix menu sections for kdm, clock
- add startkde_quick

* Fri Apr 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt3
- release 3.2.2

* Wed Apr 14 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt2
- remove %%update_wms from %%post because not needed
- remove gnupg-agent startup from startkde
  because /etc/X11/xinit.d/gnupg-agent.sh
- fix loop when search cursor themes

* Fri Apr 09 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- update code from KDE_3_2_BRANCH
- fix storage on desktop
- build apidocs

* Tue Mar 23 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt5
- update code from KDE_3_2_BRANCH
- fix menu files to execute konqueror by clicking urls in programs

* Fri Mar 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt4
- fix screensaver execution

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt3
- fix screeensavers & information modules showing

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt2
- fix menu-method to prevent kbuildsucoca crash

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH

* Tue Mar 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH
- add menu-method for new menu format (http://freedesktop.org)
- don't build old samba readonly plugin

* Wed Dec 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt8
- rename Help menuitem
- add patch for scrollkeeper docs from SuSE
- don't build khelpcenter kcontrol module, build khelpcenter from cvs

* Tue Dec 02 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt7
- remove *.la files from package

* Tue Nov 11 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt6
- add
    RH patches to:
	fix default keys for konsole
	fix double Esc in konsole if metaspecified
	launch konsole by Ctrl+T on kdesktop
	quote URL when nonKDE application button on panel
	resize icons in panel by panel setting
    MDK patches to:
	exclude "gzip file" on gzipped file popup menu
	fix appletproxy memleak
	fix fullscreen for gtk applications
    Sergey A. Sukiyazov <corwin at micom.don.ru> patches:
	fix losted focus on desktop
	fix order of reading locale names in kxkb

* Tue Oct 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt5
- fix showing "Mobile Disk" on desktop
- fix man encoding by Sergey A. Sukiyazov <corwin at micom.don.ru>

* Mon Oct 20 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt4
- cleanup startkde

* Fri Oct 17 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt3
- fix requires
- turn off artsd from startkde when alsa sound driver using

* Wed Oct 15 2003 Rider <rider@altlinux.ru> 3.1.4-alt2.2
- changed flash mount point to storage mount point (patch 1025)

* Mon Sep 29 2003 Alexander Bokovoy <ab@altlinux.ru> 3.1.4-alt2.1
- Rebuild against krb5-1.3.1-alt2
- Use libpam0-devel (stick to LinuxPAM)

* Wed Sep 24 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- fix d'n'd files from desktop to Trash
- add requires to poster from %name-kdeprint

* Wed Sep 17 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Fri Aug 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt3
- update code from cvs
- any fix kio-samba, thanks Alexey Morozov <morozov at novosoft.ru>

* Mon Aug 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt2
- update code from cvs

* Fri Aug 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs
- requires new design-graphics >= 3.1.0

* Tue Jul 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.3
- update code from cvs
- fix url to index.html

* Fri Jul 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.2
- update code from cvs
- setup default cursors, if not configured
  see in ~/.Xresources

* Wed Jul 16 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.1
- update code from cvs

* Thu Jul 10 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt7
- update code from cvs
- add patch for usbflash on kdesktop
- add workaround against running automount

* Fri Jul 04 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt6
- update code from cvs
- don't apply kdebase-add-khelpcenter-dcopinterface.patch

* Tue Jul 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt5
- update code from cvs

* Thu Jun 26 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt4
- update code from cvs
- add MDK patches
- remove old patches

* Mon Jun 02 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt3
- update code from cvs KDE_3_1_BRANCH
- repackage with rpm-build-4.0.4-alt20
- remove /etc/bashrc.d/su_may_be_easy.sh
- don't apply patch which cut "file:" when paste in konsole
- fix convertpstopdf.desktop, thanks  arling at sniip.ru

* Wed May 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt2
- fix menus to generate all /usr/share/applnk-mdk/{kfmcilent,konqueror}*.desktop

* Thu May 22 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update code from cvs KDE_3_1_BRANCH
- add xine-arts-plugin patches
- move kcmrandr utils from kdelibs

* Tue Apr 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt6
- update code from cvs KDE_3_1_BRANCH

* Mon Apr 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt5
- add MDK patches
- add xrandr patches

* Tue Apr 15 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt4
- fix alternatives

* Tue Apr 08 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt3
- update code from cvs KDE_3_1_BRANCH
- apply ghostscript security fix patch

* Mon Mar 31 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt2
- split
- add MDK patches

* Fri Mar 28 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1.1
- update code from cvs KDE_3_1_BRANCH

* Thu Mar 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update code from cvs KDE_3_1_BRANCH
- add MDK patches
- fix search netscape plugins in startkde

* Wed Feb 26 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt16
- update code from cvs KDE_3_1_BRANCH

* Wed Feb 26 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt15
- add russian bookmarks

* Mon Feb 17 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt14
- update code from cvs KDE_3_1_BRANCH

* Wed Feb 12 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt13
- update code from cvs KDE_3_1_BRANCH

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt12
- fix su_may_be_easy.sh thanks ldv@altlinux.org

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt11
- update code from cvs
- integrate startkde with kmail-aegypten-plugins

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt10
- fix su_may_be_easy.sh thanks ldv@altlinux.org
- update code from cvs

* Thu Jan 30 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt9
- update from cvs
- fix konqueror.desktop
- add MDK patches

* Thu Jan 23 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt8
- fix kcontrol/kdm to use /etc/X11/kdm/kdmrc

* Mon Jan 20 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt7
- update from cvs KDE_3_1_0_RELEASE

* Fri Jan 10 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt6
- fix startkde (about '~/$HOME')

* Thu Jan 09 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt5
- fix startkde

* Wed Jan 08 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt4
- update from cvs
- add MDK patches
- fix startkde

* Wed Dec 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- fix menu-method for short lang names in .desktop files
- restore kfontinst

* Thu Dec 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update code from cvs 3_1_0_RELASE

* Thu Nov 28 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs 3_1_0_RELASE

* Mon Nov 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.22
- improve Patch1015

* Thu Nov 21 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.21
- update from cvs 3_1_0_RELASE
- add patches from MDK

* Wed Nov 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2
- add patch30 from MDK

* Thu Oct 31 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.12
- sync with kde-settings and design-graphics

* Tue Oct 22 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.11
- update code from cvs
- add MDK patches
- rewrite ALT patches

* Wed Oct 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.10
- update code from cvs
- increase %%release to upgrade Daedalus

* Tue Oct 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt10
- turn off XFT in konsole

* Thu Oct 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt9
- fix requires && provides

* Wed Oct 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt8
- fix requires && provides

* Mon Sep 30 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt7
- fix requires

* Tue Sep 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt6
- update from cvs

* Mon Sep 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt5
- rebuild with objprelink

* Mon Sep 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt4
- don't force scan netscape plugins from /usr/bin/startkde

* Fri Sep 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt3
- rebuild with gcc 3.2
- update code from cvs

* Tue Aug 27 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- update code from cvs
- move smbclient source to %name-smbclient-source

* Fri Aug 16 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update code from cvs
- build with samba3

* Wed Aug 07 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt6
- rebuild with fam

* Mon Aug 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt5
- update code from cvs
- update Keramik theme code
- move kdmrc to kde-config

* Wed Jul 31 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt4
- add patches from Sergey A. Sukiyazov <corwin@micom.don.ru>
- add patches from cooker and rawhide
- update code from cvs

* Thu Jul 11 2002 ZerG <zerg@altlinux.ru> 3.0.2-alt3
- move configs to kde-configs package
- add Requires kde-design

* Mon Jul 08 2002 ZerG <zerg@altlinux.ru> 3.0.2-alt2
- improve startkde to
  write temp files to $TMPDIR vis expoer $KDETMP
  restore ~/Desktop/* and ~/.kde/*
  from /usr/share/alt/kde/desktoplnk
  (kde-desktoplnk package)

* Wed Jul 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version
- fix path to /etc/skel* in startkde
- add default encoding request via kioslave/http
  (workaround for Russian Apache)

* Wed Jun 19 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt8
- fix kdmrc

* Wed Jun 19 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt7
- make alternatives for %name-smbclient-*

* Fri Jun 14 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt6
- split kio_smb's to %name-smbclient-*

* Tue Jun 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt5
- update from cvs
- build with libsmbclient

* Fri Jun 07 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt4
- fix permissions in %_datadir/config

* Wed Jun 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt3
- update from cvs
- add keramik theme for kwin
- add support for GenericName to menu-method
- fix execute "su -" in root-konsole

* Thu May 23 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- fix icons search while add kdeprint applet to kicker or menu

* Sat May 18 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- cvs snapshot
- rebuild with new kdelibs

* Wed May 15 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt8
- update from cvs
- kickout konsole_grantpty
- improved kdmrc (hide root, look, etc)
- kdm execute kdmdesktop
- fix a lot of spam from update-menus
- fix showing icons for groups in menu Configuration/KDE/*

* Wed May 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt7
- update from cvs
- sync patches (rawhide && cooker)

* Mon Apr 22 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt6
- move to /usr
- update from cvs

* Wed Apr 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt5
- fix user menu clean

* Tue Apr 16 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt4
- fix requires

* Thu Apr 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- fix launch .desktops

* Thu Apr 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- build without debug
- hack to launch KDE2 programs from menu

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- release

* Mon Apr 01 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.2.cvs20020401
- update from cvs

* Thu Mar 28 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.1.rc3
- build for ALT

* Thu Mar 21 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.2mdk
- Fix spec file

* Thu Mar 21 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Thu Mar 14 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc2.1mdk
- RC2

* Sat Jan 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Mon Jan 14 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.10mdk
- Fix /etc/profile.d/kde3.sh
- Enhance %%post message
- Use ~/.kde3 instead ~/.kde

* Sun Jan 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.9mdk
- Fix problems with %%_datadir/faces on installations/upgrades

* Sun Dec 30 2001 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.8mdk
- Fix previous changelog
- Allow KDE 2 and KDE 3 to be installed in same time (lot of changes, see CVS
  for details)
- Don't build static libraries
- Remove KDE 2's changelogs (KDE 2 and KDE 3 spec files have a separate life
  now)
- Remove 7.2 support
- Don't own standard directories
- Clean %%files section (make them readable again using alphabetic order)

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.7mdk
- Rename to allow KDE 2 and KDE 3 to be installed in same time

* Tue Dec 18 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-7mdk
- Add startkde3

* Fri Dec 14 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-6mdk
- Remove requires krootwarning

* Thu Dec 13 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-5mdk
- fix mdk menu

* Sun Dec 09 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-4mdk
- Reapply some patch

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-3mdk
- kde 3.0beta1

* Wed Nov 28 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Some fix

* Thu Nov 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0

