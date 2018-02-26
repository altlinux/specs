%undefine __libtoolize
%define _optlevel s
%define unstable 0
%define _keep_libtool_files 1

%define with_kdepasswd 0
%define with_userinfo 0

%define qtdir %_qt3dir
%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libdir/kde3
%add_python_req_skip - karamba

Name: kdeutils
Version: 3.5.13
Release: alt4

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Utilities
License: GPL
URL: http://www.kde.org

Requires: %name-ark = %version-%release
Requires: %name-irkick = %version-%release
Requires: %name-kcalc = %version-%release
#Requires: %name-kcardchooser = %version-%release
Requires: %name-kcharselect = %version-%release
Requires: %name-kdessh = %version-%release
Requires: %name-kdf = %version-%release
Requires: %name-kedit = %version-%release
Requires: %name-kfloppy = %version-%release
Requires: %name-kgpg = %version-%release
Requires: %name-khexedit = %version-%release
Requires: %name-kjots = %version-%release
Requires: %name-kregexpeditor = %version-%release
Requires: %name-ksim = %version-%release
Requires: %name-ktimer = %version-%release
Requires: %name-kwallet = %version-%release
Requires: %name-laptop = %version-%release
Requires: %name-superkaramba = %version-%release
%if %with_userinfo
Requires: %name-userinfo = %version-%release
%endif
%if %with_kdepasswd
Requires: %name-kdepasswd = %version-%release
%endif

Source: kdeutils-%version.tar
Source10: klaptop_acpi_helper.control
Patch0: kdeutils-3.0-ktimer_icons.patch
Patch1: kdf-3.0.2-label.patch
#
# ALT
Patch101: kcharselect-3.5.0-fix-linking.patch
Patch103: kdeutils-3.5.1-alt-ksim-configure.patch
Patch104: kdeutils-3.5.1-alt-ksim-configure_snmp.patch
Patch105: kdeutils-3.5.13-Ark-Combained.patch

# Automatically added by buildreq on Mon Apr 08 2002
#BuildRequires: XFree86-devel XFree86-libs freetype2 gcc-c++ kde-common kdebase kdelibs-devel libarts-devel libjpeg-devel liblcms libmng libpng-devel libqt3-devel libstdc++-devel libtiff-devel zlib-devel

BuildRequires(pre): kdelibs-devel
BuildRequires: xorg-xproto-devel libXext-devel libX11-devel libICE-devel libXtst-devel
BuildRequires: gcc-c++ kde-common
BuildRequires: libjpeg-devel libpng-devel libqt3-devel libstdc++-devel
BuildRequires: libtiff-devel zlib-devel libart_lgpl-devel libgmp-devel python-devel
BuildRequires: libpcre-devel flex kdebase-devel
#BuildRequires: libpcsclite-devel
BuildRequires: libacl-devel libattr-devel
BuildRequires: libnet-snmp-devel libssl-devel
BuildRequires: doxygen qt3-doc desktop-file-utils
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
Utilities for the K Desktop Environment.

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
Conflicts: kdeutils <= 3.0.1
#
%description common
Common empty package for %name


%package superkaramba
Summary: Interactive eye-candy themes on your KDE desktop
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: superkaramba = 0.37-%release
Obsoletes: superkaramba < 0.37
#
%description superkaramba
SuperKaramba is, in simple terms, a tool that allows you to easily
create interactive eye-candy on your KDE desktop. Theme writers create
themes, or text files that define their widget. Then, they can
optionally add python scripting to make their widget interactive. The
possibilities are endless!

%package irkick
Summary: KDE LIRC server
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: lirc
#
%description irkick
This package contains KDE LIRC server and
configure modules of your remote controls
for use with applications.

%package kwallet
Summary: Wallet Management Tool
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kwallet
Wallet Management Tool

%package kgpg
Summary: Simple graphical interface for GnuPG
Group: File tools
Requires: gnupg
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kgpg = %version-%release
Obsoletes: kgpg
#
%description kgpg
Kgpg is a simple interface for GnuPG,
a powerful encryption utility.

%package ark
Summary: GUI frontend for handling archive files
Group: Archiving/Compression
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: zip unzip tar unrar bzip2 gzip ncompress p7zip arj
#
%description ark
Ark is a KDE tool for handling archive files.
It supports the following file formats:
  zip
  plain tar and tar with compressors lzop, gzip, bzip2, bzip, compress
  lha
  zoo
  single files compressed with compressors lzop, gzip, bzip2, bzip, compress
  rar
  ar

%package kcalc
Summary: KDE pocket calculator
Group: Office
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kcalc
A KDE pocket calculator.

%package kcardchooser
Summary: Smartcard Chooser
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: pcsc-lite, opensc, openct
#
%description kcardchooser
Smartcard Chooser

%package kcharselect
Summary: Character Selector
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kcharselect
KDE Character Selector - allows you to enter characters not found on your
keyboard.

%package kdepasswd
Summary: KDE frontend to changing your password
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kdepasswd
KDE frontend to changing your password

%package userinfo
Summary: KControl module showing user account information
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: kdebase-kcontrol
Requires: shadow-change
Requires: %name-common = %version-%release
%if ! %with_kdepasswd
Requires: userpasswd
%endif
#
%description userinfo
KControl module showing user account information

%package kdessh
Summary: KDE frontend to ssh
Group: Networking/Remote access
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: openssh-clients
#
%description kdessh
KDE frontend to ssh (Secure Shell, an application to remotely control a
different Linux or Linux-like system securely).

%package kdf
Summary: Application and KDE applet to monitor available diskspace
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kdf = %version-%release
Obsoletes: kdf
#
%description kdf
kdeutils-kdf contains the kdf, kwikdisk and kcmdf tools for monitoring
available diskspace.

%package kedit
Summary: An easy to use text editor
Group: Editors
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kedit
An easy to use text editor

%package kfloppy
Summary: Floppy disk formatter
Group: System/Configuration/Hardware
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: dosfstools
#
%description kfloppy
KFloppy formats floppy disks and creates ext2 or DOS filesystems on them.

%package khexedit
Summary: Hex editor
Group: Editors
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description khexedit
A KDE hex editor. It allows you to edit binary files.

%package kjots
Summary: Virtual notepad
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: kdebase-wm
Requires: %name-common = %version-%release
#
%description kjots
KJots is a virtual notepad - you can put notes on your desktop.

%package laptop
Summary: Laptop utilities for KDE
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: kdebase-wm, control
Requires: %name-common = %version-%release
#Requires: powersave
%description laptop
Various laptop-related utilities for KDE.
kdeutils-laptop adds battery monitoring to kicker (the KDE panel) and allows
you to manage power management and PCMCIA cards from the KDE control center.

%package ksim
Summary: K System Information Monitor
Group: Monitoring
Requires: %{get_dep kdelibs}
Requires: kdebase-wm
Requires: %name-common = %version-%release
Provides: ksim =  %version-%release
Obsoletes: ksim
#
%description ksim
KSim is a plugin based system monitor that has
support for GKrellm (www.gkrellm.net) themes.

KSim can currently monitor these types:
  * Cpu usage (plugin)
  * Net (eth0, ppp0 etc) usage (plugin)
  * Filesystem usage (plugin)
  * Sensors information (plugin)
  * Disk information (plugin)
  * Mail monitor (plugin)
  * Clock & Date display
  * Hostname display
  * Uptime display
  * Memory/Free Memory display
  * Swap/Free Swap display
		    
%package kregexpeditor
Summary: Regular Expressions Editor
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kregexpeditor
A Regular Expressions Editor.

%package ktimer
Summary: A timer (stop watch)
Group: Office
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ktimer
A timer (stop watch).

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: %name = %version-%release
Provides: kdeutils-kregexpeditor-devel = %version-%release
Obsoletes: kdeutils-kregexpeditor-devel
#
%description devel
Development files for %name

%prep
%setup -q -n %name-%version
cp -ar altlinux/admin ./
#%patch0 -p1
%patch1 -p1
#
%patch101 -p1
%patch103 -p1
#%patch104 -p1
%patch105

sed -i '\|\${kdeinit}_LDFLAGS[[:space:]]=[[:space:]].*-no-undefined|s|-no-undefined|-no-undefined -Wl,--warn-unresolved-symbols|' admin/am_edit
for f in `find $PWD -type f -name Makefile.am`
do
    sed -i -e '\|_la_LDFLAGS.*[[:space:]]-module[[:space:]]|s|-module|-module \$(KDE_PLUGIN)|' $f
    #sed -i -e '\|_la_LDFLAGS.*[[:space:]]-no-undefined|s|-no-undefined|-no-undefined -Wl,--allow-shlib-undefined|' $f
    grep -q -e 'lib.*SOURCES' $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
sed -i -e 's|\$USER_INCLUDES|-I%_includedir/tqtinterface \$USER_INCLUDES|' admin/acinclude.m4.in

find ./ -type f -name Makefile.am | \
while read f
do
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lkdeinit_kded -lDCOP \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done

make -f admin/Makefile.common cvs ||:

%build
%if %unstable
%add_optflags -DDEBUG
%endif

export QTDIR=%qtdir
export KDEDIR=%_K3prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%K3configure \
    --disable-gcc-hidden-visibility \
%if %unstable
    --enable-debug=full \
    --disable-final \
%else
    --disable-debug \
    --enable-final \
%endif
    --without-kdepasswd

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%if %unstable
%set_strip_method none
%endif
export PATH=%_K3bindir:$PATH

%K3install

install -pD -m755 %SOURCE10 %buildroot/etc/control.d/facilities/klaptop_acpi_helper

%__mkdir_p  %buildroot/%_K3apps/superkaramba/themes/
cp -a superkaramba/examples/{taskBar/cleanbar,popupMenu,autoHide,richtext,unicode} \
    %buildroot/%_K3apps/superkaramba/themes/
[ -f %buildroot/%_K3xdg_apps/superkaramba.desktop ] \
  || install -m 0644 superkaramba/src/superkaramba.desktop %buildroot/%_K3xdg_apps/superkaramba.desktop

# fix categories
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Archiving --add-category=Compression %buildroot%_K3xdg_apps/ark.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Calculator %buildroot%_K3xdg_apps/kcalc.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Accessibility %buildroot%_K3xdg_apps/KCharSelect.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Filesystem %buildroot%_K3xdg_apps/kcmdf.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Filesystem %buildroot%_K3xdg_apps/kdf.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Filesystem %buildroot%_K3xdg_apps/kwikdisk.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Utility %buildroot%_K3xdg_apps/KEdit.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Clock %buildroot%_K3xdg_apps/ktimer.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Settings --add-category=X-PersonalSettings %buildroot%_K3xdg_apps/kgpg.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Settings --add-category=X-PersonalSettings %buildroot%_K3xdg_apps/kwalletmanager.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=TextTools %buildroot%_K3xdg_apps/Kjots.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Development %buildroot%_K3xdg_apps/kregexpeditor.desktop

#X-KDE-Utilities-File
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=FileTools %buildroot%_K3xdg_apps/khexedit.desktop

# X-KDE-Utilities-Peripherals
#desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Settings --add-category=HardwareSettings %buildroot%_K3xdg_apps/irkick.desktop
#desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=Settings --add-category=HardwareSettings %buildroot%_K3xdg_apps/KFloppy.desktop

%pre laptop
/usr/sbin/groupadd -r laptop 2> /dev/null || :
[ $1 -eq 1 ] || /usr/sbin/control-dump klaptop_acpi_helper
%post laptop
[ $1 -eq 1 ] || /usr/sbin/control-restore klaptop_acpi_helper



%files
%files common
%_K3cfg/*
%_K3conf/*

%files superkaramba
%_K3bindir/superkaramba
%_K3applnk/Utilities/superkaramba.desktop
%_K3apps/superkaramba/
%doc %_K3doc/en/superkaramba/
%_K3iconsdir/*/*/apps/superkaramba.*
%_K3iconsdir/*/*/mimetypes/superkaramba_*.*
%_K3mimelnk/application/x-superkaramba.desktop
%_K3xdg_apps/superkaramba.desktop

%files kwallet
%_K3bindir/kwalletmanager
%_K3libdir/kde3/kcm_kwallet.so*
%_K3apps/kwalletmanager
%_K3srv/kwalletmanager_show.desktop
%_K3srv/kwallet_config.desktop
%_kde3_iconsdir/*/*/apps/kwalletmanager.png
%doc %_K3doc/en/kwallet/
%_K3xdg_apps/kwalletconfig.desktop
%_K3xdg_apps/kwalletmanager.desktop
%_K3xdg_apps/kwalletmanager-kwalletd.desktop

%files irkick
%_K3bindir/irkick
%_K3libdir/libkdeinit_irkick.so*
%_K3libdir/kde3/irkick.so*
%_K3libdir/kde3/kcm_kcmlirc.so*
%_K3start/irkick.desktop
%_K3apps/remotes
%_K3apps/profiles/profile.dtd
%_K3apps/profiles/noatun.profile.xml
%_K3apps/profiles/klauncher.profile.xml
%_K3apps/profiles/konqueror.profile.xml
%_K3apps/irkick
%_kde3_iconsdir/*/*/apps/irkick.png
%doc %_K3doc/en/irkick
%doc %_K3doc/en/kcmlirc
%_K3xdg_apps/irkick.desktop
%_K3xdg_apps/kcmlirc.desktop

%files kgpg
%_K3bindir/kgpg
%_K3apps/konqueror/servicemenus/encrypt*.desktop
%_K3apps/kgpg/
%_K3start/kgpg.desktop
%_kde3_iconsdir/*/*/apps/kgpg.png
%doc %_K3doc/en/kgpg
%_K3xdg_apps/kgpg.desktop

%files ark
%_K3bindir/ark
%_K3libdir/libkdeinit_ark.*so*
%_K3lib/*ark*.so*
%_K3apps/ark
#%_K3apps/konqueror/servicemenus/*
%_kde3_iconsdir/*/*/apps/ark.*
%_K3xdg_apps/ark.desktop
%_K3srv/ark_part.desktop
%doc %_K3doc/en/ark

%files kcalc
%_K3bindir/kcalc
%_K3libdir/libkdeinit_kcalc.*so*
%_K3lib/kcalc.so*
%_kde3_iconsdir/*/*/apps/kcalc.*
%_K3apps/kcalc
%_K3apps/kconf_update/kcalcrc.upd
%doc %_K3doc/en/kcalc
%_K3xdg_apps/kcalc.desktop

%files kcharselect
%_K3bindir/kcharselect
%_K3lib/kcharselect_panelapplet.so*
%_K3apps/kcharselect/
%_K3apps/kconf_update/kcharselect.upd
%_kde3_iconsdir/*/*/*/kcharselect.png
%_K3xdg_apps/KCharSelect.desktop
%doc %_K3doc/en/kcharselect
%_K3apps/kicker/applets/kcharselectapplet.desktop

#%files kcardchooser
#%_K3bindir/kcardchooser
#%_K3xdg_apps/kcardchooser.desktop

%files ksim
#%_K3bindir/ksim
#%_K3libdir/ksim.*
%_K3libdir/libksimcore.so*
%_K3lib/ksim_*.so*
%_K3apps/ksim
%_K3apps/kicker/extensions/ksim.desktop
%_K3iconsdir/*/*/*/ksim*.png
%doc %_K3doc/en/ksim
#%_K3xdg_apps/ksim.desktop

%if %with_kdepasswd
%files kdepasswd
%_K3bindir/kdepasswd
%_K3xdg_apps/kdepasswd.desktop
%endif

%if %with_userinfo
%files userinfo
%_K3lib/kcm_userinfo.so*
%_K3xdg_apps/userinfo.desktop
%endif

%files kdessh
%_K3bindir/kdessh

%files kdf
%_K3bindir/kdf
%_K3bindir/kwikdisk
%_K3lib/kcm_kdf*.so*
%_K3iconsdir/*/*/*/kcmdf.png
%_kde3_iconsdir/*/*/*/kdf.png
%_kde3_iconsdir/*/*/*/kwikdisk.png
%_K3apps/kdf
%_K3xdg_apps/kdf.desktop
%_K3xdg_apps/kwikdisk.desktop
%_K3xdg_apps/kcmdf.desktop
%doc %_K3doc/en/kdf
%doc %_K3doc/en/kinfocenter/blockdevices

%files kedit
%_K3bindir/kedit
%_K3libdir/libkdeinit_kedit.so*
%_K3lib/kedit.so*
%_kde3_iconsdir/*/*/*/kedit.png
%_K3xdg_apps/KEdit.desktop
%_K3apps/kedit
%doc %_K3doc/en/kedit

%files kfloppy
%_K3bindir/kfloppy
%_K3apps/konqueror/servicemenus/floppy_format.desktop
%_kde3_iconsdir/*/*/*/kfloppy.png
%_K3xdg_apps/KFloppy.desktop
%doc %_K3doc/en/kfloppy

%files khexedit
%_K3bindir/khexedit
%_K3libdir/libkhexeditcommon.so*
%_K3lib/libkbyteseditwidget.so*
%_K3lib/libkhexedit2part.so*
%_K3apps/khexedit/
%_K3apps/khexedit2part/
%_kde3_iconsdir/*/*/*/khexedit.png
%_K3srv/kbyteseditwidget.desktop
%_K3srv/khexedit2part.desktop
%_K3xdg_apps/khexedit.desktop
%doc %_K3doc/en/khexedit

%files kjots
%_K3bindir/kjots
%_kde3_iconsdir/*/*/*/kjots.png
%_K3apps/kjots
%_K3xdg_apps/Kjots.desktop
%doc %_K3doc/en/kjots

%files laptop
%config %_sysconfdir/control.d/facilities/klaptop_acpi_helper
#%_K3bindir/klaptopdaemon
%_K3bindir/klaptop_*
%_K3libdir/libkcmlaptop.so*
%_K3lib/kcm_laptop*.so*
%_K3lib/kded_klaptopdaemon.so*
%_K3apps/klaptopdaemon
#%_K3iconsdir/*/*/*/klaptopdaemon.png
%_K3iconsdir/*/*/apps/laptop_battery.*
%_K3iconsdir/*/*/*/laptop_pcmcia.png
%_K3xdg_apps/pcmcia.desktop
%_K3xdg_apps/laptop.desktop
%_K3srv/kded/klaptopdaemon.desktop
%doc %_K3doc/en/kcontrol/kcmlowbatcrit
%doc %_K3doc/en/kcontrol/kcmlowbatwarn
%doc %_K3doc/en/kcontrol/laptop
%doc %_K3doc/en/kcontrol/powerctrl
#
%_K3libdir/libkmilo.so*
%_K3lib/kmilo_*.so*
%_K3lib/kded_kmilod.so*
%_K3lib/kcm_kvaio.so*
%_K3srv/kmilo/
%_K3srv/kded/kmilod.desktop
%_K3srvtyp/kmilo/kmilopluginsvc.desktop
%_K3xdg_apps/kvaio.desktop
# kcm_thinkpad
%_K3lib/kcm_thinkpad.so*
%_K3xdg_apps/thinkpad.desktop

%files kregexpeditor
%_K3bindir/kregexpeditor
%_K3libdir/*kregexpeditor*.so*
%_K3lib/libkregexpeditorgui*.so*
%_K3apps/kregexpeditor
%_K3srv/kregexpeditorgui.desktop
%_kde3_iconsdir/*/*/apps/kregexpeditor.png
%doc %_K3doc/en/KRegExpEditor
%_K3xdg_apps/kregexpeditor.desktop

%files ktimer
%_K3bindir/ktimer
%_kde3_iconsdir/*/*/apps/ktimer.png
%doc %_K3doc/en/ktimer
%_K3xdg_apps/ktimer.desktop

%files devel
%if %_keep_libtool_files
%_K3libdir/*.la
%endif
%_includedir/*

%changelog
* Tue Jun 19 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt4
- klaptop_acpi_helper search path is fixed to /usr/lib/kde3/bin on facilities.

* Sat Jun 16 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt3
- ARK: LHA checking utilite for unpack and 7Z single directories hide is added.
- All Ark patches have combined and merged to main tree TDE.

* Thu Jun 14 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- ARK: archives filename encode and ZIP archive UTF filename's processing is fixed.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt3.2
- Removed bad RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.12-alt3.1
- Rebuild with Python-2.7

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.12-alt3
- fixed desktop categories

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Tue Dec 28 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Mon Dec 20 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt7
- rebuilt with new net-snmp

* Wed Mar 10 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt6
- update from lastest 3.5 branch
- fix to build with new autotools

* Wed Mar 10 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt5
- remove requies to tpctl

* Tue Aug 25 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt4
- fix to build with new automake

* Mon Sep 22 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt3
- add more settings for klaptop_acpi_helper control facility

* Wed Sep 10 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt2
- add control support for klaptop_acpi_helper

* Wed Aug 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Thu Feb 14 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt7
- rebuilt with new python

* Wed Jan 16 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt6
- fix 7zip filenames encoding (#13420); thanks lav@alt

* Fri Nov 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt5
- add test integrity support to ark

* Thu Nov 08 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt4
- add to ark unarchive arj support

* Thu Nov 01 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt3
- add support for creation encrypted zip, rar, 7zip archives in ark

* Wed Oct 31 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt2
- fix ark to ask for password on encrypted rar archives

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Thu Aug 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt3
- fix zip and rar filenames encoding in Ark; thanks stanv@alt

* Mon May 28 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- fix kded_klaptopdaemon linking; thanks shrek@alt

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Mon Dec 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt2
- rebuilt with new libnet-snmp

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version
- add patches from Alexey Morozov

* Tue Apr 04 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Tue Mar 28 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt3
- rebuilt

* Mon Feb 20 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt2
- fix #4920

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Wed Feb 01 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt4
- fix build requires

* Fri Jan 27 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt3
- fix build on x86_64

* Fri Dec 30 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt2
- fix requires

* Mon Dec 12 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Wed Jun 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Tue Oct 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Thu Jul 22 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt3
- fix kfloppy format progress

* Wed Jul 21 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- dont reset kfloppy after fdformat before mkfs

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Thu May 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt3
- build userinfo package
- disable changing password and real user name in userinfo,
  but add requires to shadow-change

* Wed May 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt2
- fix kgpg menu

* Thu Apr 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH

* Wed Mar 03 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Tue Nov 04 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- fix provides/requires
- add patch to kdf skip labels

* Mon Sep 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Thu Aug 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Thu Jul 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt2
- update code from cvs

* Mon Jun 02 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update from cvs KDE_3_1_BRANCH

* Tue May 06 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt2
- update from cvs KDE_3_1_BRANCH

* Tue Apr 01 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update from cvs KDE_3_1_BRANCH

* Wed Feb 05 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt4
- update from cvs
- fix kcalc Error message in utf8

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update from cvs
- add MDK patches

* Thu Dec 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update from cvs

* Fri Nov 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs

* Sun Nov 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1. Increase %release to easy check dependencies

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.11
- fix provides

* Mon Oct 21 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.10
- update from cvs

* Wed Sep 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt3
- rebuild with gcc 3.2 && objprelink
- sync patches with cooker

* Thu Aug 22 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- add losted kfloppy binary

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update from cvs

* Tue Aug 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version
- split

* Mon Jun 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Tue May 14 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- fix kcalc menu entry
- fix kdepasswd truncate password to 8 chars

* Fri Apr 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- move to /usr

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- build for ALT

* Thu Apr 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Fix update menu

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde3.0

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Sat Mar 16 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc2.1mdk
- RC2

* Sun Jan 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Sat Jan 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.5mdk
- Oops, fix previous changelogs

* Sat Jan 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.4mdk
- Allow KDE 2 and KDE 3 to be installed in same time
- Don't build static libraries
- Remove KDE 2's changelogs (KDE 2 and KDE 3 spec files have a separate life
  now)
- Fix previous changelog

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.1mdk
- Rename to allow KDE 2 and KDE 3 to be installed in same time

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-3mdk
- kde 3.0 beta1

* Thu Nov 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Improve spec file

* Fri Nov 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0
