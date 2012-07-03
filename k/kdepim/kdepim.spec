%define libopensync libopensync0
%define opensync_ver %{get_version %libopensync}

%undefine __libtoolize
%define unstable 0
%define _optlevel s
%define	pilot 0
%define _keep_libtool_files 1
%define cmake 1

%define qtdir %_qt3dir
%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_K3lib
%add_findreq_skiplist %_K3bindir/kmail_*.sh
%set_verify_elf_method no
#add_verify_elf_skiplist %_K3libdir/libindex.so*

%define with_gnokii 1

Name: kdepim
Version: 3.5.13
Release: alt3
Serial: 1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Personal Information Management
Icon: kde-icon.xpm
License: GPL
URL: http://www.kde.org/

Source: kdepim-%version.tar
Source1: cr16-app-kandy.png
Source2: cr32-app-kandy.png
Source3: cr48-app-kandy.png

# RH
Patch1: kdepim-3.4.92-libz.patch
Patch2: kdepim-3.5.3-gcc-4.1.1-8.patch
Patch3: kdepim-3.4.0-kandy-icons.patch

# MDK
Patch40: kdepim-3.5.9-kitchensync-handle-synce.patch
Patch41: kdepim-3.5.12-kitchensync-synce-config.patch

# ALT
Patch100: kdepim-3.5.8-alt-fix-new-kitchensync-linking.patch
Patch101: 3.4-kandy_var_lock.patch
Patch102: 3.1.12-alt-kmail-deflock.patch
Patch103: 3.2.0-kmobile-var-lock.patch
Patch104: 3.5.0-libkalarm-fix-linking.patch
Patch105: kdepim-3.5.8-alt-desktop-categories.patch
Patch106: kdepim-3.5.12-alt-fix-linking.patch
Patch107: kaddressbook-3.4.1-fix-linking.patch
Patch108: kmail-3.5.7-alt-dont-disregard-umask.patch
Patch109: kmail-3.5.6-alt-def-compose-encoding.patch
Patch110: kdepim-3.5.12-alt-kmail-searchjob.patch
Patch111: kdepim-3.5.10-alt-gcc4.4.patch
Patch112: tde-3.5.13-build-defdir.patch
Patch113: kdepim-3.5.13-cmake-build.patch
Patch114: kdepim-3.5.13-kpilot-add.patch

Requires: %name-akregator = %version-%release
Requires: %name-kaddressbook = %version-%release
Requires: %name-kandy = %version-%release
Requires: %name-karm = %version-%release
Requires: %name-kfile = %version-%release
Requires: %name-kleopatra = %version-%release
Requires: %name-kio = %version-%release
Requires: %name-kmail = %version-%release
Requires: %name-kmobile = %version-%release
Requires: %name-knode = %version-%release
Requires: %name-knotes = %version-%release
Requires: %name-kontact = %version-%release
Requires: %name-korganizer = %version-%release
Requires: %name-kode = %version-%release
Requires: %name-korn = %version-%release
%if %pilot
Requires: %name-kpilot = %version-%release
%endif
Requires: %name-ksync = %version-%release
Requires: %name-ktnef = %version-%release
Requires: %name-libs = %version-%release


# Automatically added by buildreq on Mon Apr 12 2004 (-bi)
#BuildRequires: XFree86-devel XFree86-libs doxygen flex fontconfig freetype2 gcc-c++ gcc-g77 glib2 kde-settings kdelibs-devel libarts-devel libarts-qt libbluez-devel libgnokii-devel libjpeg-devel liblockdev-devel libmal-devel libpilot-link-devel libpng-devel libqt3-devel libstdc++-devel qt3-designer qt3-doc xml-utils xpm-devel zlib-devel
BuildRequires(pre): cmake kdelibs-devel
BuildRequires: doxygen flex gcc-c++ desktop-file-utils chrpath
#BuildRequires: libbluez-devel
BuildRequires: libacl-devel libattr-devel libical-devel
%if %with_gnokii
BuildRequires: libgnokii-devel
%endif
BuildRequires: libjpeg-devel liblockdev-devel %libopensync-devel boost-devel
BuildRequires: libmal-devel libpilot-link-devel libpng-devel libqt3-devel
BuildRequires: xml-utils zlib-devel libstdc++-devel libsasl2-devel
BuildRequires: libgpgme-devel >= 1.0.0 libgpg-error-devel >= 1.0
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
# hack for apt in hasher
#BuildRequires: libarts-devel > 1.0.0 libarts-qtmcop-devel > 1.0.0
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
Information Management applications for the K Desktop Environment.

%package common
Summary: Common empty package for %name
Group:	Graphical desktop/KDE
BuildArch: noarch
Requires: kde-common >= 3.2
Conflicts: kdepim <= 3.0
#
%description common
Common empty package for %name

%package akregator
Summary: RSS/Atom feed reader for KDE
Group: Networking/News
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
Provides: akregator = %version-%release
Obsoletes: akregator < %version-%release
#
%description akregator
Akregator allows you to browse through thousands of internet feeds without
the hassle of using a web browser.

%package kio
Summary: Protocol plugins for KDE
Group: Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description kio
This package contains imap4 and sieve kio plugins

%package kleopatra
Summary:	KDE Certificate Manager
Group:		Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
Provides: kdenetwork-kgpgcertmanager = %version-%release
Obsoletes: kdenetwork-kgpgcertmanager < %version-%release
Provides: kdepim-kgpgcertmanager = %version-%release
Obsoletes: kdepim-kgpgcertmanager < %version-%release
#
%description kleopatra
Certificate manager used by %name for encrypted email

%package kmail
Summary: A mail client for KDE
Group: Networking/Mail
Requires: %name-common = %serial:%version-%release
Requires: %name-libs = %version-%release
Requires: kdebase-kio kdepim-kio
#Requires:  MTA
#Requires: gnupg2 >= 1.9.6
Provides: kdenetwork-kmail = %version-%release
Obsoletes: kdenetwork-kmail
Provides: kdepim-kmailcvt = %version-%release
Obsoletes: kdepim-kmailcvt
#
%description kmail
A mail client for KDE.
KMail supports local mail spools as well as all commonly used
Internet mail protocols (POP3, IMAP, SMTP, ...)

%package knode
Summary: A newsgroup (NNTP) reader for KDE
Group: Networking/News
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
Provides: kdenetwork-knode = %version-%release
Obsoletes: kdenetwork-knode
#
%description knode
A newsgroup (NNTP) reader for KDE.

%package korn
Summary: Multi-folder new mail monitor for KDE
Group: Networking/Mail
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
Provides: kdenetwork-korn = %version-%release
Obsoletes: kdenetwork-korn
#
%description korn
A multi-folder new mail monitor for KDE.
KOrn will display the number of new messages in your mail
folders in kicker (the KDE panel).

%package kode
Summary: Generation of C++ classes representing XML data
Group: Development/C++
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description kode
libkode is a helper library for programmatic generation of C++ code. It includes
a program kode for generation of C++ template files and kxml_compiler for
generation of C++ classes representing XML data described by RelaxNG schemes.

%package kontact
Summary: Integrated solution to your PIM
Group: Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description kontact
Kontact is the integrated solution to your personal
information management PIM needs. It combines well-known KDE
applications like KMail, KOrganizer and KAaddressbook into a
single interface to provide easy access to mail, scheduling,
address book and other PIM functionality.

%package ktnef
Summary: TNEF File Viewer
Group: Networking/Mail
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description ktnef
This package contains Microsoft MS-TNEF MIME
attachments viewer for KDE.

%package kmobile
Summary: Manage Mobile Devices
Group: Communications
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description kmobile
Mobile Devices manager

%package devel
Summary: Devel stuff for kdepim
Group: Development/KDE and QT
Requires: %name-common = %serial:%version-%release
Requires: %name = %version-%release
Requires: %{get_dep kdelibs-devel}
#
%description devel
This package contains header files needed if you wish to build applications
based on kdepim.

%package libs
Summary:	Base libraries for kdepim
Group:		Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description libs
Base libraries for kdepim

%package kaddressbook
Summary:	Addressbook for KDE
Group:		Graphical desktop/KDE
License: BSD
#
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description kaddressbook
Addressbook for KDE

%package kfile
Summary:	Kfile plugins
Group:		Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description kfile
Plugin to allow the standard KDE file dialog to display
information about vCard files and email messages.

%package korganizer
Summary: Electronic organizer for KDE.
Group: Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
Requires: kdemultimedia-kmix
#
%description korganizer
Information Management applications for the K Desktop Environment.
  - korganizer: a calendar-of-events and todo-list manager
  - kalarm: gui for setting up personal alarm/reminder messages
  - kalarmd: personal alarm/reminder messages daemon,
    shared by korganizer and kalarm.
  - konsolecalendar: Command line tool for accessing calendar files.

%if %pilot
%package kpilot
Summary: KDE support for synchronizing data with a Palm(tm) or compatible PDA
Group: Communications
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}

%description kpilot
KDE support for synchronizing data with a Palm(tm) or compatible PDA.
%endif

%package kandy
Summary: KDE support for synchronizing data with cellphones
Group: Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description kandy
KDE support for synchronizing data with cellphones.
Install %name-kandy if you want to use %name and have a cellphone.
("kandy" comes from "Handy", the german word used for a cellular)

%package karm
Summary: Time tracking tool
Group: Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
#
%description karm
KArm - Punjambi language for "work" - tracks time spent on various tasks.
It is useful for tracking hours to be billed to different clients.

%package knotes
Summary: Post-It notes on the desktop
Group: Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}

%description knotes
KNotes allows you to place Post-It notes on your desktop.
In addition to serving as a reminder, KNotes can mail and print your notes,
and accept drag and drop even from remote sites.

%package ksync
Summary:	Syncing collections of data entries
Group:		Graphical desktop/KDE
Requires: %name-common = %serial:%version-%release
Requires: %{get_dep kdelibs}
Provides: kdepim-kitchensync = %version-%release
Obsoletes: kdepim-kitchensync < %version-%release

%description ksync
Syncing collections of data entries like
calenders, bookmarks, contacts, mail folders etc.

%prep
%setup -q -n %name-%version
# cp -ar altlinux/admin ./
install -m 0644 %SOURCE1 %SOURCE2 %SOURCE3 kandy/src
# %_K_if_ver_gteq %opensync_ver 0.30
# rm -rf kitchensync
# cp -ar altlinux/kitchensync ./
# %patch100 -p1
# %endif

# RH
%patch1 -p1
#%patch2 -p1
%patch3 -p1

# MDK
%patch40 -p1
%patch41 -p1

# ALT
%patch101 -p1
%patch102 -p1
%patch103 -p1
#%patch104 -p1
%patch105 -p1
#%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p0
#%patch111 -p1
%patch112
%patch113 -p1
#%patch114

%if %cmake
%else
rm -rf indexlib

rm -rf altlinux
sed -i '\|\${kdeinit}_LDFLAGS[[:space:]]=[[:space:]].*-no-undefined|s|-no-undefined|-no-undefined -Wl,--warn-unresolved-symbols|' admin/am_edit
for f in `find $PWD -type f -name Makefile.am`
do
    sed -i -e '\|_la_LDFLAGS.*[[:space:]]-module[[:space:]]|s|-module|-module \$(KDE_PLUGIN)|' $f
    #sed -i -e '\|_la_LDFLAGS.*[[:space:]]-no-undefined|s|-no-undefined|-no-undefined -Wl,--allow-shlib-undefined|' $f
    grep -q -e 'lib.*SOURCES' $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
#sed -i -e '\|LIBTQT_CXXFLAGS=|s|LIBTQT_CXXFLAGS=.*|LIBTQT_CXXFLAGS="-I%_includedir/tqtinterface -include tqt.h"|' admin/acinclude.m4.in
sed -i -e 's|\$USER_INCLUDES|-I%_includedir/tqtinterface \$USER_INCLUDES|' admin/acinclude.m4.in
make -f admin/Makefile.common cvs ||:
%endif

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%_K3prefix
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L/%_qt3dir/lib -L%_libdir -L/%_lib"

%if %cmake
BD=%_builddir/%name-%version/BUILD

# Kode library search path on build
export LD_LIBRARY_PATH=$BD/kode:$BD/wizards:$LD_LIBRARY_PATH

if ! [ -f $BD/CMakeCache.txt ]
then
%K3cmake \
    -DWITH_ARTS=OFF \
    -DWITH_SASL=ON \
    -DWITH_NEWDISTRLISTS=ON  \
%if %with_gnokii
    -DWITH_GNOKII=ON \
%else
    -DWITH_GNOKII=OFF \
%endif
    -DWITH_EXCHANGE=ON \
    -DWITH_EGROUPWARE=ON \
    -DWITH_KOLAB=ON \
    -DWITH_SLOX=ON \
    -DWITH_GROUPWISE=ON \
    -DWITH_FEATUREPLAN=ON \
    -DWITH_GROUPDAV=ON \
    -DWITH_BIRTHDAYS=ON \
    -DWITH_NEWEXCHANGE=ON \
    -DWITH_SCALIX=ON \
    -DWITH_CALDAV=OFF \
    -DWITH_CARDDAV=OFF \
    -DWITH_INDEXLIB=ON \
    -DBUILD_KITCHENSYNC=ON \
    -DBUILD_ALL=ON
fi
%K3make

%else
# else if cmake

export CXXFLAGS="-I%_includedir/libical"
%K3configure \
%if %unstable
	--enable-debug=full \
%else
	--disable-debug \
%endif
	--enable-exchange \
%if %with_gnokii
	--with-gnokii \
%else
	--without-gnokii \
%endif
	--with-sasl \
        --with-gpg=%_bindir/gpg2 \
	--with-gpgsm=%_bindir/gpgsm \
	--enable-newdistrlists
#	--disable-indexlib \
#        --enable-final \

%make_build
%make_build -C kmobile
# %make_build -C kitchensync
%make_build -C kfile-plugins/rfc822
#make_build apidox

%endif
# end if cmake

%install
%if %unstable
%set_strip_method none
%endif

%if %cmake
%K3install

install -dm 0755 %buildroot/%_kde3_iconsdir/
mv %buildroot/%_iconsdir/hicolor %buildroot/%_kde3_iconsdir/hicolor/
mv %buildroot/%_iconsdir/locolor %buildroot/%_kde3_iconsdir/locolor/

install -dm 0755 %buildroot/%_K3applnk/.hidden/
install -dm 0755 %buildroot/%_K3applnk/Applications/
install -dm 0755 %buildroot/%_K3applnk/Utilities/
install -m 0644 kalarm/*.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 kalarm/*.desktop %buildroot/%_K3applnk/Applications/
install -m 0644 kandy/src/*.desktop %buildroot/%_K3applnk/Utilities/
install -m 0644 karm/support/*.desktop %buildroot/%_K3applnk/Utilities/

install -dm 0755 %buildroot/%_K3srvtyp/
install -m 0644 kitchensync/src/kitchensync.desktop %buildroot/%_K3srvtyp/

# install -m 0644 kitchensync/src/kitchensync.desktop %buildroot/%_K3xdg_apps

%else
# else if cmake

export PATH=%_bindir:$PATH
%K3install
%K3install -C kmobile
%K3install -C kfile-plugins/rfc822

%endif
# end if cmake

# fix icons placement
mkdir -p %buildroot/%_K3iconsdir/crystalsvg/32x32/devices
mv %buildroot/%_K3iconsdir/default.kde/32x32/devices/* %buildroot/%_K3iconsdir/crystalsvg/32x32/devices
rm -rf %buildroot/%_K3iconsdir/default.kde

# fix categories
desktop-file-install --dir %buildroot%_K3xdg_apps --add-category=TelephonyTools %buildroot%_K3xdg_apps/kmobile.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --remove-category=Utility --add-category=Office --add-category=Calendar %buildroot%_K3xdg_apps/knotes.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --remove-category=Utilities --add-category=Utility %buildroot%_K3xdg_apps/groupwarewizard.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --remove-category=Utilities --add-category=Utility %buildroot%_K3xdg_apps/ktnef.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --remove-category=Network --remove-category=Email --add-category=Office --add-category=ContactManagement %buildroot%_K3xdg_apps/Kontact.desktop
# desktop-file-install --dir %buildroot%_K3xdg_apps --remove-category=Utility --add-category=Office --add-category=ContactManagement %buildroot%_K3xdg_apps/kitchensync.desktop
desktop-file-install --dir %buildroot%_K3xdg_apps --remove-category=Utility --add-category=Office --add-category=Email %buildroot%_K3xdg_apps/ktnef.desktop

for i in %buildroot%_K3bindir/*
do
	chrpath -r %_K3lib $i || chrpath -d $i ||:
done
for i in %buildroot%_libdir/*.so %buildroot%_K3lib/*.so \
	%buildroot%_K3plug/designer/*.so
do
	chrpath -d $i
done

%files
%files common
%_K3conf/*
%_K3cfg/*

%files akregator
%_K3bindir/akregator
%_K3libdir/libakregatorprivate.so*
%_K3lib/libakregatorpart.so*
%_K3lib/libakregator_mk4storage_plugin.so*
%_K3apps/akregator/
%_K3srv/feed.protocol
%_K3srv/akregator_part.desktop
%_K3srv/akregator_mk4storage_plugin.desktop
%_K3srvtyp/akregator_plugin.desktop
%_K3iconsdir/crystalsvg/*/apps/akregator*
%_kde3_iconsdir/*/*/apps/akregator*
%_K3iconsdir/crystalsvg/*/actions/button_fewer.png
%_K3iconsdir/crystalsvg/*/actions/button_more.png
%_K3iconsdir/crystalsvg/*/actions/rss_tag.png
%doc %_K3doc/en/akregator/
%_K3xdg_apps/akregator.desktop

%files kandy
%_K3bindir/kandy*
%_K3applnk/Utilities/kandy*
%_K3xdg_apps/kandy*
%_K3apps/kandy
# %_K3iconsdir/crystalsvg/*/apps/kandy.*
%doc %_K3doc/en/kandy

%files kaddressbook
%_K3bindir/kabc2mutt
%_K3bindir/kabcdistlistupdater
%_K3bindir/kaddressbook
%_K3libdir/libkabinterfaces.so*
%_K3libdir/libkaddressbook.so*
%_K3libdir/libkabcscalix.so*
%_K3lib/libkaddressbookpart.so*
%_K3lib/kabc_*.so*
%_K3lib/kcm_kabconfig.so*
%_K3lib/kcm_kabcustomfields.so*
%_K3lib/kcm_kabldapconfig.so*
%_K3lib/ldifvcardthumbnail.so*
%_K3lib/libkaddrbk_*.so*
%_K3apps/kaddressbook
%_K3srv/kabconfig.desktop
%_K3srv/kabcustomfields.desktop
%_K3srv/kabldapconfig.desktop
%_K3srv/kaddressbook/
%_K3srv/kresources/kabc
%_K3srv/ldifvcardthumbnail.desktop
%_K3srvtyp/dcopaddressbook.desktop
%_K3srvtyp/kaddressbook*.desktop
%_K3start/kabcdistlistupdater.desktop
%_kde3_iconsdir/*/*/apps/kaddressbook.png
%doc %_K3doc/en/kaddressbook
%_K3xdg_apps/kaddressbook.desktop

%files kio
%_K3lib/kio_imap4.so*
%_K3srv/imap4.protocol
%_K3srv/imaps.protocol
#%_K3srv/overview.desktop
%_K3lib/kio_sieve.so*
%_K3srv/sieve.protocol
%_K3lib/kio_mbox.so*
%_K3srv/mbox.protocol
%_K3lib/kio_groupwise.so*
%_K3srv/groupwise.protocol
%_K3srv/groupwises.protocol

%files kmail
#%_K3bindir/indexlib-config
%_K3bindir/kmail
%_K3bindir/kmail_*.sh
%_K3bindir/kmailcvt
%_K3libdir/libkmailprivate.so*
%_K3lib/kcm_kmail.so*
%_K3lib/libkmailpart.so*
%_K3lib/libkmail_bodypartformatter_*.so*
%_K3apps/kconf_update/kmail*
%_K3apps/kconf_update/kpgp.upd
%_K3apps/kconf_update/upgrade-signature.pl
%_K3apps/kconf_update/upgrade-transport.pl
%_K3apps/kmail
%_K3apps/kmailcvt
%_K3srv/kmail_config_*.desktop
%_K3srvtyp/dcopimap.desktop
%_K3srvtyp/dcopmail.desktop
%_kde3_iconsdir/*/*/apps/kmail.*
%_K3iconsdir/crystalsvg/*/apps/kmaillight.*
%_K3iconsdir/crystalsvg/*/*/kmailcvt.*
%doc %_K3doc/en/kmail
%_K3xdg_apps/KMail.desktop
%_K3xdg_apps/kmail_view.desktop
# %_K3applnk/Utilities/kmailcvt.desktop

%files knode
%_K3bindir/knode
%_K3libdir/libknodecommon.so*
%_K3lib/kcm_knode.so*
%_K3lib/libknodepart.so*
%_K3apps/knode
%_K3srv/knode_config_*.desktop
%_K3srv/knewsservice.protocol
%_kde3_iconsdir/*/*/apps/knode*
%_K3xdg_apps/KNode.desktop
%doc %_K3doc/en/knode

%files korn
%_K3bindir/korn
%_K3apps/kconf_update/korn-3-5-metadata-update.pl
%_K3apps/kconf_update/korn-3-5-ssl-update.pl
%_K3apps/kconf_update/korn-3-5-update.upd
%_K3libdir/kconf_update_bin/korn-3-4-config_change
%_K3apps/kconf_update/korn-3-4-config_change.upd
%_kde3_iconsdir/*/*/apps/korn*
%_K3xdg_apps/KOrn.desktop
%doc %_K3doc/en/korn

%files kode
%doc kode/README
%_K3bindir/kode
%_K3bindir/kxml_compiler
%_K3libdir/libkode.so*

%files kontact
%_K3bindir/scalixadmin
%_K3bindir/scalixwizard
%_K3lib/kio_scalix.so*
%_K3lib/libscalixwizard.so*
%_K3srv/scalix.protocol
%_K3srv/scalixs.protocol
#
%_K3bindir/egroupwarewizard
%_K3bindir/groupwarewizard
%_K3bindir/exchangewizard
%_K3bindir/groupwisewizard
%_K3bindir/kolabwizard
%_K3bindir/sloxwizard
%_K3bindir/kontact
%_K3libdir/libkontact.so*
%_K3libdir/libkpinterfaces.so*
%_K3lib/libexchangewizard.so*
%_K3lib/libgroupwisewizard.so*
%_K3lib/libegroupwarewizard.so*
%_K3lib/libkolabwizard.so*
%_K3lib/libsloxwizard.so*
%_K3lib/kcm_kontact.so*
#%_K3lib/kcm_kabsummary.so*
%_K3lib/kcm_kmailsummary.so*
%_K3lib/kcm_kontactknt.so*
%_K3lib/kcm_kontactsummary.so*
%_K3lib/kcm_korgsummary.so*
%_K3lib/kcm_sdsummary.so*
%_K3lib/libkontact_*.so*
%_K3apps/kontact/
%_K3apps/kontactsummary/
%_K3iconsdir/crystalsvg/*/actions/kontact_*
%_kde3_iconsdir/*/*/apps/kontact.png
#%_kde3_iconsdir/*/*/apps/korganizer_todo.png
%_K3srv/kontact*
%_K3srv/kcmsdsummary.desktop
#%_K3srv/kcmkabsummary.desktop
%_K3srv/kcmkmailsummary.desktop
%_K3srv/kcmkontactknt.desktop
%_K3srv/kcmkontactsummary.desktop
%_K3srv/kcmkorgsummary.desktop
%_K3srvtyp/kontactplugin.desktop
%_K3xdg_apps/Kontact.desktop
%_K3xdg_apps/groupwarewizard.desktop
%_K3xdg_apps/kontactdcop.desktop
%_K3doc/en/kontact/
%doc README.Kolab

%files ktnef
%_K3bindir/ktnef
%_K3xdg_apps/ktnef.desktop
%_K3apps/ktnef
%_kde3_iconsdir/*/*/apps/ktnef.png
%_K3mimelnk/application/ms-tnef.desktop
%doc %_K3doc/en/ktnef

%files ksync
%_K3bindir/kitchensync
%_K3libdir/libkitchensync.so*
%_K3libdir/libqopensync.so*
%_K3lib/libkitchensyncpart.so*
%_K3apps/kitchensync
%_kde3_iconsdir/*/*/*/kitchensync.*
%_K3xdg_apps/kitchensync.desktop
#%_K3bindir/multisynk
#%_K3libdir/libdummykonnector.so*
#%_K3libdir/libkabckonnector.so*
#%_K3libdir/libkcalkonnector.so*
#%_K3libdir/libmultisynk.so*
#%_K3libdir/libksharedfile.so*
#%_K3libdir/libkitchensyncui.so*
#%_K3libdir/libkonnector.so*
#%_K3libdir/liblocalkonnector.so*
#%_K3libdir/libqtopiakonnector.so*
#%_K3libdir/libremotekonnector.so*
#%_K3lib/libksfilter_addressbook.so*
#%_K3lib/libksfilter_calendar.so*
#%_K3lib/liboverviewpart.so*
#%_K3lib/libmultisynkpart.so*
#%_K3lib/libkded_ksharedfile.*
#%_K3lib/libksync_*.so*
#%_K3apps/konqueror/servicemenus/kitchensync*
#%_K3apps/multisynk
#%_K3srvtyp/filter.desktop
%_K3srvtyp/kitchensync.desktop
#%_K3srvtyp/konnector.desktop
#%_K3srv/kitchensync/
#%_K3srv/kded/ksharedfile.desktop
#%_K3srv/overview.desktop
#%_K3srv/kresources/konnector/
#%_K3srv/kresources/konnector_*.desktop
#%_K3mimelnk/kdedevice/cellphone.desktop
#%_K3mimelnk/kdedevice/pda.desktop
#%_kde3_iconsdir/*/*/*/multisynk.*
#%doc %_K3doc/en/multisynk
#%_K3xdg_apps/multisynk.desktop

%files kleopatra
%_K3bindir/kleopatra
%_K3bindir/kwatchgnupg
%_K3lib/kcm_kleopatra.so*
%_K3xdg_apps/kleopatra_import.desktop
%_K3apps/kleopatra
%_K3apps/kwatchgnupg
%_K3srv/kleopatra_config_*.desktop
%doc %_K3doc/en/kleopatra
%doc %_K3doc/en/kwatchgnupg

%files kmobile
%_K3bindir/kmobile
%_K3libdir/libkmobileclient.so*
%_K3libdir/libkmobiledevice.so*
#%_K3lib/kio_mobile.so*
%_K3lib/libkmobile*.so*
%_K3xdg_apps/kmobile.desktop
%_K3apps/kmobile/
%_kde3_iconsdir/*/*/apps/kmobile.png
%_K3iconsdir/crystalsvg/*/devices/mobile_*.png
#%_K3mimelnk/inode/mobile_*.desktop
#%_K3srv/cellphone.protocol
%_K3srv/*kmobile_*.desktop
#%_K3srv/mobile.protocol
#%_K3srv/organizer.protocol
#%_K3srv/pda.protocol
%_K3srvtyp/libkmobile.desktop


%files libs
#%_K3bindir/networkstatustestservice
#%_K3libdir/libgwsoap.so*
#%_K3libdir/libindex.so*
#%_K3lib/kded_networkstatus.so*
#%_K3srv/kded/networkstatus.desktop
#
#
%_K3libdir/libkcalscalix.so*
%_K3libdir/libgwsoap.so*
%_K3libdir/libkholidays.so*
%_K3apps/libkholidays/
%_K3apps/kdepim/
#
%_K3libdir/libkabc_*.so*
%_K3libdir/libkabckolab.so*
%_K3libdir/libkgroupwarebase.so*
%_K3libdir/libkgroupwaredav.so*
%_K3libdir/libkgantt.so*
#%_K3libdir/libkcalsystem.so*
%_K3libdir/libkcal.so*
%_K3libdir/libkcal_*.so*
%_K3libdir/libkcalkolab.so*
%_K3libdir/libkdepim.so*
#%_K3libdir/libknewstuff.so*
%_K3libdir/libknoteskolab.so*
%_K3libdir/libknotes_*.so*
%_K3libdir/libkpimidentities.so*
%_K3libdir/libksieve.so*
#%_K3libdir/libksync.so*
%_K3libdir/libktnef.so*
#%_K3libdir/libkdenetwork.so*
#%_K3libdir/libkdgantt.so*
%_K3libdir/libmimelib.so*
%_K3libdir/libkmime.so*
%_K3libdir/libkslox.so*
%_K3lib/kcal_*.so*
#%_K3apps/libical/
%_K3apps/kconf_update/kpgp-3.1-upgrade-address-data.pl
%_K3apps/kconf_update/kolab-resource.upd
%_K3apps/kconf_update/upgrade-resourcetype.pl
%_K3apps/kgantt/
%_K3apps/libkdepim/
%_K3apps/kdepimwidgets
%_K3srv/kresources/kcal/
%_K3srv/kresources/kcal_manager.desktop
%_K3srvtyp/dcopcalendar.desktop
# libkleopatra
%_K3libdir/libgpgme++.so*
%_K3libdir/libkpgp.so*
%_K3libdir/libkleopatra.so*
%_K3libdir/libqgpgme.so*
%_K3apps/libkleopatra
%_K3iconsdir/crystalsvg/*/apps/gpg.png
%_K3iconsdir/crystalsvg/*/apps/gpgsm.png
# libkpimexchange
%_K3libdir/libkpimexchange.so*
%_K3lib/resourcecalendarexchange.so*

%_K3bindir/indexlib-config
%_K3libdir/libindex.so*
%_K3libdir/libkarm.so*
%_K3libdir/libknotes.so*

%files kfile
%_K3lib/kfile_vcf.so*
%_K3srv/kfile_vcf.desktop
# %_K3lib/kfile_palm.so*
# %_K3srv/kfile_palm.desktop
# %_K3lib/kfile_rfc822.so*
# %_K3srv/kfile_rfc822.desktop
%_K3lib/kfile_ics.so*
%_K3srv/kfile_ics.desktop

%files korganizer
#%_K3bindir/ghns
#%_K3bindir/khotnewstuff
%_K3bindir/korga*
%_K3bindir/konsolekalendar
%_K3bindir/*alarm*
#%_K3bindir/kabcfrontend
%_K3bindir/ical2vcal
#%_K3libdir/libkalarmd*.so*
%_K3libdir/libkocorehelper.so*
%_K3libdir/libkorganizer*.so*
%_K3libdir/libkorg_*.so*
#%_K3lib/libkcm_alarmdaemon*.so*
%_K3lib/libkorg_*.so*
%_K3lib/kcm_korganizer.so*
%_K3lib/libkorganizerpart.so*
#%_K3apps/kalarmdgui
%_K3apps/kalarm/
%_K3apps/korganizer/
#%_K3apps/knewstuff/
%_K3apps/korgac/
#%_K3applnk/Settings/System/alarmdaemon*
%_K3applnk/.hidden/kalarm*
%_K3applnk/Applications/kalarm*
%_K3xdg_apps/kalarm*
%_K3xdg_apps/korganizer*
%_K3xdg_apps/konsolekalendar*
%_K3start/kalarm*
%_K3start/korgac*
%_K3apps/kconf_update/korganizer.upd
%_K3srv/korganizer
%_K3srv/korganizer_config*.desktop
%_K3srv/webcal*
#%_K3srv/configcolors.desktop
#%_K3srv/configfonts.desktop
#%_K3srv/configfreebusy.desktop
#%_K3srv/configgroupautomation.desktop
#%_K3srv/configgroupscheduling.desktop
#%_K3srv/configmain.desktop
#%_K3srv/configtime.desktop
#%_K3srv/configviews.desktop
%_K3srvtyp/calendar*
%_K3srvtyp/korganizer*
%_K3srvtyp/korgprintplugin.desktop
%_kde3_iconsdir/*/*/*/korganizer.png
%_K3iconsdir/*/*/actions/kalarm.png
%_kde3_iconsdir/*/*/apps/kalarm.png
%_K3iconsdir/crystalsvg/*/apps/konsolekalendar.png
#%_kde3_iconsdir/*/*/actions/knewstuff.png
%doc %_K3doc/en/kalarm
%doc %_K3doc/en/korganizer
%doc %_K3doc/en/konsolekalendar

%files knotes
%_K3bindir/knotes
%_K3libdir/libknotesscalix.so*
%_K3lib/knotes_*.so*
%_K3apps/knotes
%_K3srv/kresources/knotes/
%_K3srv/kresources/knotes_*
%_kde3_iconsdir/*/*/*/knotes.png
%_K3xdg_apps/knotes.desktop
%doc %_K3doc/en/knotes

%files karm
%_K3bindir/karm
%_K3lib/libkarmpart.so*
%_K3apps/karm/
%_K3apps/karmpart/
%_K3xdg_apps/karm.desktop
%_K3applnk/Utilities/karm.desktop
%_K3srv/karm_part.desktop
%_kde3_iconsdir/*/*/*/karm.png
%doc %_K3doc/en/karm
#%doc %_K3doc/en/kcontrol/kalarmd

%if %pilot
%files kpilot
%_K3bindir/*pilot*
%_K3bindir/kpalmdoc
%_K3libdir/libkpilot.so*
%_K3lib/*conduit_*.so*
%_K3lib/kcm_kpilot.so*
%_K3apps/kconf_update/kpalmdoc.upd
%_K3apps/kconf_update/kpilot.upd
%_K3apps/kpilot
%_K3xdg_apps/*pilot*
%_K3xdg_apps/kpalmdoc.desktop
%_K3iconsdir/crystalsvg/*/*/kpilot*
%_kde3_iconsdir/*/*/*/kpilot*
%_K3iconsdir/crystalsvg/*/*/kpalmdoc.png
%_K3srv/*conduit*
%_K3srv/kpilot_config*.desktop
%_K3srvtyp/*conduit*
%doc %_K3doc/en/kpilot/
%endif

%files devel
%if %_keep_libtool_files
%_K3libdir/*.la
%_K3lib/*.la
%endif
%_K3lib/plugins/designer/
%_K3includedir/*.h
%_K3includedir/akregator/
#%_K3includedir/index/
%_K3includedir/calendar
%_K3includedir/gpgme++
%_K3includedir/kabc
%_K3includedir/kaddressbook
%_K3includedir/kdepim
%_K3includedir/kgantt
#%_K3includedir/kitchensync
%_K3includedir/kleo
%_K3includedir/kmail
#%_K3includedir/knewstuff
%_K3includedir/kontact
%_K3includedir/korganizer
# %_K3includedir/kpilot
%_K3includedir/ksieve
%_K3includedir/ktnef
%_K3includedir/libkcal
%_K3includedir/mimelib
%_K3includedir/qgpgme
%_K3includedir/libemailfunctions
#%doc %_K3doc/en/kdepim-%version-apidocs/
%_K3includedir/index

%changelog
* Tue Jun 12 2012 Roman Savochenko <rom_as@altlinux.ru> 1:3.5.13-alt3
- Fixes from GIT http://www.trinitydesktop.org from 3.5.13 to 12.06.2012 is backported.

* Tue May 08 2012 Roman Savochenko <rom_as@altlinux.ru> 1:3.5.13-alt2
- More fixes after through renaming from QT to TQT, KMail fix for Base64 code.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1:3.5.13-alt1
- TDE 3.5.13 release build

* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.5.12-alt3.1
- Removed bad RPATH

* Thu Apr 21 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.5.12-alt3
- fixed desktop categories

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 1:3.5.12-alt2.1
- Remove requires of xorg-x11-devel

* Fri Mar 04 2011 Sergey V Turchin <zerg@altlinux.org> 1:3.5.12-alt2
- move to alternate place

* Tue Nov 30 2010 Sergey V Turchin <zerg@altlinux.org> 1:3.5.12-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 1:3.5.10-alt4
- udpate to lastest 3.5 branch
- fix compile with new autotools

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 1:3.5.10-alt3
- fix to build
- don't use deprecated macroses in specfile

* Tue Oct 21 2008 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.10-alt2
- built kitchensync with stable libopensync0

* Mon Aug 25 2008 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.10-alt1
- new version

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.9-alt1
- new version
- update kitchensync tarball to svn r775024

* Tue Jan 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.8-alt6
- build kitchensync svn snapshot if new opensync >= 0.30 detected

* Thu Jan 10 2008 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.8-alt5
- fix KMail.desktop categories

* Thu Jan 10 2008 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.8-alt4
- return to originag kdepim-3.5.8
- built without indexlib

* Wed Dec 19 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.8-alt3
- update from enterprise branch r744693

* Tue Dec 18 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.8-alt2
- use kdepim enterprise branch r742984

* Tue Oct 16 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.8-alt1
- new version

* Fri Jul 06 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.7-alt4
- add patch to fix templates when forward in kmail

* Mon Jul 02 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.7-alt3
- add UTF-8 encoding to search request via IMAP; thanks lav@alt

* Fri Jun 15 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.7-alt2
- don't disregard umask by default when save mail from KMail

* Wed May 23 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.7-alt1
- new version

* Sat Apr 28 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.6-alt4
- fix kmail multipart compose encoding; thanks stanv@alt
- sync patches from FC

* Fri Apr 13 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.6-alt3
- add patch from upstream to compile with new libpilot-link

* Thu Feb 08 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.6-alt2
- fix desktop categories

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.6-alt1
- new version

* Wed Dec 20 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.5-alt2
- add patch to update kpilot from svn (apply if libpilot-link >= 0.12.0)

* Mon Oct 16 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.5-alt1
- new version

* Tue Sep 19 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.4-alt2
- disable indexlib in KMail

* Fri Sep 01 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.4-alt1
- new version
- add patches from RH

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.3-alt2
- bump release to push incoming@ALT

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.3-alt1
- new version

* Thu May 18 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.2-alt2
- rebuilt with new gcc

* Thu Mar 30 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.2-alt1
- new version

* Thu Mar 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.1-alt2
- built without full-text indexing in KMail

* Wed Feb 01 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.1-alt1
- new version

* Mon Dec 05 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.0-alt1
- new version
- built without libgnokii

* Mon Oct 31 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.4.1-alt5
- dont chmod when save attachment from KMail

* Fri Sep 16 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.4.1-alt4
- fix libkaddressbook linking

* Thu Sep 08 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.4.1-alt3
- remove requires MTA from kmail

* Wed Jul 20 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.4.1-alt2
- fix requires

* Mon Jun 06 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.4.1-alt1
- new version

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.4.0-alt1
- new version

* Thu Jan 20 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.2-alt4
- move libktnef to %%name-libs package

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.2-alt3
- rebuild

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.2-alt2
- rebuild with gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.2-alt1
- rebuild

* Tue Jan 04 2005 ZerG <zerg@altlinux.ru> 1:3.3.2-alt0.0.M24
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.1-alt2
- rebuild with external libgpgme

* Wed Oct 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.1-alt1
- new version

* Thu Sep 30 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.0-alt1
- new version

* Tue Jul 13 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.3-alt2
- add fix from cvs for searching in non-latin mail bodies

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.3-alt1
- new version

* Fri May 14 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.2-alt3
- fix kmobile description

* Thu Apr 22 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.2-alt2
- rebuild with new gnokii

* Mon Apr 12 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.2-alt1
- new version
- add patch to smaller KMail settings dialog
  thanks Sergey Shilov <hsv@dstszi.gov.ua>
- add holidays_ru
  thanks Dmitri Drozdov <ddv@altonika.ru>

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.1-alt1
- update code from KDE_3_2_BRANCH

* Wed Mar 03 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Fri Dec 26 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.4-alt2
- removed *.la files

* Thu Sep 18 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.4-alt1
- update code from cvs

* Thu Aug 21 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.3-alt1
- update code from cvs

* Thu Jul 03 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.2-alt3
- update code from cvs

* Wed Jun 11 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.2-alt2
- fix %post,%postun
- remove alternatives

* Fri May 30 2003 Sergey V Turchin <zerg at altlinux dot ru> 1:3.1.2-alt1
- update code from cvs KDE_3_1_BRANCH

* Mon May 05 2003 Sergey V Turchin <zerg at altlinux dot ru> 1:3.1.1-alt2
- update code from cvs KDE_3_1_BRANCH
- add MDK patches

* Tue Apr 01 2003 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.1-alt1
- update code from cvs KDE_3_1_BRANCH

* Mon Feb 10 2003 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt4
- update code from cvs
- apply Patch100

* Wed Feb 05 2003 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt3
- update code from cvs

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt2
- update code from cvs
- add MDK patches

* Thu Nov 28 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt1
- update from cvs

* Sun Nov 10 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.20.rc2
- rc2

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.20.rc1
- rc1. Increase %release to easy check dependencies

* Wed Oct 16 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.2
- update from cvs

* Wed Sep 11 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.0.3-alt2
- rebuild with gcc 3.2 && objprelink

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.0.3-alt1
- update from cvs

* Fri Aug 09 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.0.2-alt1
- new version

* Mon Jun 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- add serial
- fix menu items

* Sun May 26 2002 ZerG <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Fri May 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- fix kandy to use /var/lock/serial
  thanks Artem Pastuchov <past@yam.ru>

* Mon Apr 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- move to /usr

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- build for ALT

* Thu Apr 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Fix update menu

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Sat Mar 16 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc2.2mdk
- RC2

* Fri Feb 08 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.2mdk
- Fix spec file

* Sun Jan 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Sun Jan 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.2mdk
- Allow KDE 2 and KDE 3 to be installed in same time
- Don't build static libraries
- Remove KDE 2's changelogs (KDE 2 and KDE 3 spec files have a separate life
  now)
- Fix previous changelog
- Fix ./configure
- Clean %%files (i.e. respect alphabetic order and make it readable)

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.1mdk
- Rename to allow KDE 2 and KDE 3 to be installed in same time

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-1mdk
- kde 3.0 beta1

* Fri Nov 30 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Improve spec file

* Fri Nov 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0 try
