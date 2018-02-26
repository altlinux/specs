%define _build_lang en_US
%undefine __libtoolize
%define _optlevel s
%define _keep_libtool_files 1

%define qtdir %_qt3dir
%define unstable 0
%define etc_kppp_allow 0
%define jingle 1
%define cmake 1

%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libdir/kde3
%add_findreq_skiplist %_bindir/kopete_*.sh
%add_findreq_skiplist %_bindir/winpopup-*.sh
# Undefined symbols
#add_verify_elf_skiplist %_libdir/libkopete_videodevice.so*


Name: kdenetwork
Version: 3.5.13
Release: alt4

Group: Graphical desktop/KDE
Summary: KDE - Network Applications
Url: http://www.kde.org/
License: GPL

Requires: %name-filesharing = %version-%release
Requires: %name-kdict = %version-%release
Requires: %name-kdnssd = %version-%release
Requires: %name-kfile = %version-%release
Requires: %name-kget = %version-%release
Requires: %name-knewsticker = %version-%release
Requires: %name-kopete = %version-%release
Requires: %name-kpf = %version-%release
Requires: %name-kppp = %version-%release
Requires: %name-krdc = %version-%release
Requires: %name-krfb = %version-%release
Requires: %name-ksirc = %version-%release
Requires: %name-ktalkd = %version-%release
Requires: %name-lisa = %version-%release
Requires: %name-rss = %version-%release
#Requires: %name-file = %version-%release
Requires: %name-kwifimanager = %version-%release
#Requires: %name-kxmlrpcd = %version-%release


Source: kdenetwork-%version.tar
#
Source10: kdenetwork-ktalk
Source11: kdenetwork-kotalk
Source12: kdenetwork-lisa-init
Source13: kdenetwork-lisa-sysconf
Source14: kdenetwork-kppp.control

# SuSE
Patch30: kopete_stop_doubled_irc_status_changes.diff
Patch31: kpf-slp.diff
Patch32: krdc-eintr.diff
Patch33: krdc-threadsafe.diff
Patch34: wifi-without-arts.patch

# RH
Patch50: kdenetwork-3.1-desktop.patch

# ALT
Patch5000: kdenetwork-3.5.12-alt-fix-linking.patch
Patch5001: kdenetwork-3.5.10-alt-fix-libjingle-compile.patch
Patch5002: kppp-3.5.0-fix-crtscts-option.patch
Patch5003: kdenetwork-3.0-kppp_lock.patch
Patch5004: kdenetwork-3.1.0-kppp.allow.patch
Patch5005: kdenetwork-3.1.1-kppp-warn.patch
Patch5006: kdenetwork-3.1.2-kget-settings.patch
Patch5007: kppp-3.5.12-redial-on-nodialtone.patch
Patch5008: kdenetwork-3.5.12-alt-fix-compile.patch
Patch5009: kdenetwork-3.5.4-lisa_drop_privileges.patch
Patch5010: kdenetwork-3.5.12-alt-kppp-add-devices.patch
Patch5011: kcmwifi.desktop.patch
Patch5012: kppp-3.2.3-dock-resize.patch
#
Patch5014: external-sqlite.patch
#
Patch5016: 3.5.0-ktalkdlg-fix-linking.patch
#
Patch5019: kopete-0.12-alt-yahoo-build.patch
Patch5020: kopete-3.5.7-alt-external-qca.patch
Patch5021: kopete-0.12.0-alt-default-encoding-ru.patch
Patch5022: kopete-0.12-iLBC_re-enable.patch
#
Patch5025: kopete-3.5.5-alt-fix-complie.patch
#
Patch5028: kdenetwork-3.5.7-alt-zeroconf-services.patch
Patch5029: kdenetwork-3.5.7-alt-kopete-jingle.patch
Patch5030: kpf-3.5.7-alt-defaults.patch
Patch5031: kinetd-3.5.12-alt-optimize.patch
Patch5032: kinetd-3.5.12-alt-resolve.patch
Patch5033: kppp-3.5.12-alt-new-modem-device.patch
Patch5034: kdenetwork-3.5.12-kppp-use-search-in-resolv-conf.patch
Patch5035: kdenetwork-3.5.12-alt-etsnet-resolv-mods.patch
Patch5036: tde-3.5.13-build-defdir.patch
Patch5037: tdenetwork-3.5.13-cmake-build.patch

# Automatically added by buildreq on Thu Mar 18 2004 (-bi)
#BuildRequires: XFree86-devel XFree86-libs control fontconfig freetype2 gcc-c++ glib2 gzip-utils kdelibs-devel libarts-devel libjpeg-devel libpam-devel libqt3-devel libssl-devel libstdc++-devel libxml2-devel libxslt-devel qt3-designer wireless-tools zlib-devel

BuildRequires(pre): kdelibs-devel cmake
BuildRequires: gcc4.5-c++
BuildRequires: glib2 gzip-utils libjpeg-devel libpng-devel libv4l-devel
BuildRequires: libpam0-devel libqt3-devel libssl-devel libstdc++-devel libxml2-devel
BuildRequires: libxslt-devel qt3-designer zlib-devel libopenslp libopenslp-devel
BuildRequires: texinfo libpcre-devel libpam0-devel libssl-devel libXtst-devel
#libqca-devel
#BuildRequires: libxmms-devel
BuildRequires: xml-utils wireless-tools-devel libidn-devel libsqlite3-devel
BuildRequires: libacl-devel libattr-devel libspeex-devel libgadu-devel libmeanwhile-devel
%if %jingle
BuildRequires: gsmlib-devel
BuildRequires: libilbc-devel libexpat-devel libspeex-devel glib2-devel
BuildRequires: libortp0.7-devel
%endif
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
Networking applications for the K Desktop Environment.
This is empty package for compatibility. You don't need them.

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Conflicts: kdenetwork < 3.0.1-alt1
Requires: kde-common >= 3.2
#
%description common
Common empty package for %name

%package devel
Summary: Header files for %name
Group: Development/KDE and QT
Requires: %name = %version-%release
#
%description devel
Header files needed for developing kdemultimedia applications.

%package filesharing
Summary: File sharing
Group: Networking/Remote access
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description filesharing
This package contains tool allowing files sharing via
Networking File System (NFS) and Microsoft(R) Network (Samba)

%package kdnssd
Summary: DNS-SD Services Watcher for KDE
Group: Networking/Other
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: avahi-daemon libnss-mdns
#
%description kdnssd
This package contains DNS-SD Services Watcher for KDE.
It keeps track of DNS-SD services and updates directory listings.

%package rss
Summary: RSS support for KDE
Group: Networking/WWW
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description rss
This package contains RSS support for KDE.
RSS is the name given to a simple and well-established XML format used to
syndicate headlines. Once a website creates an RSS file they have created
a means to allow others to syndicate their headlines.

%package kwifimanager
Summary: A wireless LAN connection monitor
Group: Monitoring
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: wireless-tools
#
%description kwifimanager
A wireless LAN connection monitor

%package kfile
Summary:	Kfile plugin for Bit Torrent Info
Group:		Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: %name-kfile-plugins = %version-%release
Obsoletes: %name-kfile-plugins
#
%description kfile
Plugin to allow the standard KDE file dialog to display
information about Bit Torrent Info files.

%package kget
Summary:	KDE Download Manager
Group:		Networking/File transfer
Conflicts: 	%name < %version
Requires: %{get_dep kdelibs}
Requires: kdebase-wm
Requires: %name-common = %version-%release
#
%description kget
KDE Download Manager

%package kppp
Summary: K Desktop Environment - PPP Network Applications
Group: Networking/Remote access
Requires: ppp, control
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kppp
PPP Networking applications for the K Desktop Environment.
Install kppp if you intend to use KDE on a machine using
PPP networking.

%package krdc
Summary:	KDE Remote Desktop Client
Group:		Networking/Remote access
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: rdesktop
#
%description krdc
krdc is an KDE graphical client for the rfb Protocol,
used by VNC.

%package krfb
Summary:	KDE Remote Screen Server
Group:		Networking/Remote access
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description krfb
KRfb is a small server for the RFB protocol,
better known as VNC.  Unlike most RFB servers,
KRfb allows you to share your X11 session.

%package ksirc
License: Artistic
Summary: IRC client for KDE
Group: Networking/IRC
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksirc
An IRC (Internet Relay Chat) client for KDE.

%package kdict
License: Artistic
Summary: A DICT (net dictionary) client for KDE
Group: Text tools
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kdict
A DICT (net dictionary) client for KDE.

%package kopete
Summary: Instant Messaging client
Group: Networking/Instant messaging
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: qca-tls
Provides: kopete = %version-%release
Obsoletes: kopete
#
%description kopete
Kopete is an Instant Messaging client
designed to be modular and plugin based.

%package knewsticker
License: BSD derivative
Summary: A News Ticker for KDE
Group: Networking/Other
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description knewsticker
KNewsticker is a KDE applet that will display current news from Internet
sites of your choice.

%package ktalkd
License: BSD derivative
Summary: Talk (chat) protocol implementation for KDE
Group: Networking/Chat
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: talk
#
%description ktalkd
An implementation of the Talk protocol for KDE.

%package kxmlrpcd
License: BSD derivative
Summary: Remote scripting capability for KDE
Group: Networking/Other
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kxmlrpcd
KXmlRpcD allows you to execute DCOP calls from other machines using
the XmlRpc protocol.

%package lisa
Summary: LAN browser
Group: Networking/Other
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description lisa
LISa is intended to provide a kind of "network neighbourhood" but only
relying on the TCP/IP protocol stack, no smb or whatever.

%package kpf
License: BSD derivative
Summary: KDE Public Fileserver
Group: Networking/Remote access
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kpf
KPF is an easy to use public file server controlled from the KDE panel.
Simply drag a file or directory to the KPF button to share it.

%prep
%setup -q -n kdenetwork-%version
# cp -ar altlinux/admin ./

%patch30 -p0
%patch31 -p0
%patch32 -p0
%patch33 -p0
#%patch34 -p0

%patch50 -p1

%patch5000 -p1
%patch5001 -p1
%patch5002 -p1
%patch5003 -p1
%patch5004 -p1
%patch5005 -p1
%patch5006 -p1
%patch5007 -p1
#%patch5008 -p1
%patch5009 -p1
%patch5010 -p1
%patch5011 -p1
%patch5012 -p1
#
#%patch5014 -p1
#
#%patch5016 -p1
#
%patch5019 -p1
###%patch5020 -p1
%patch5021 -p1
%patch5022 -p1
#
%patch5025 -p1
#
%patch5028 -p1
%patch5029 -p1
%patch5030 -p1
%patch5031 -p1
%patch5032 -p1
%patch5033 -p1
%patch5034 -p1
%patch5035 -p1 -b .resolv_mods
%patch5036
%patch5037 -p1

#perl -pi -e "s|^X-KDE-StartupNotify.*||" kppp/Kppp.desktop
#perl -pi -e "s|^X-DCOP-ServiceType.*||" kppp/Kppp.desktop

%if %cmake
%else
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
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lkdeinit_kded -lkresources -lDCOP -lkdefx \$(LIB_KPARTS) \$(LIB_KSPELL) \$(LIB_KDEPRINT) \$(LIB_KABC) \$(LIB_KUTILS) \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done

make -f admin/Makefile.common cvs ||:
%endif

%build
#add_optflags
export QTDIR=%qtdir
export KDEDIR=%_K3prefix
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L/%_qt3dir/lib -L%_libdir -L/%_lib"
export LC_ALL=C LANG=C LANGUAGE=C

%if %cmake
BD=%_builddir/%name-%version/BUILD

%add_optflags -DHAVE_LIBV4L1_VIDEODEV_H

if ! [ -f $BD/CMakeCache.txt ]
then
%K3cmake \
%if %jingle
    -DWITH_JINGLE=ON \
%endif
    -DBUILD_KOPETE_PROTOCOL_ALL=ON \
    -DBUILD_KOPETE_PROTOCOL_MSN=OFF \
    -DBUILD_KOPETE_PLUGIN_ALL=ON \
    -DBUILD_KOPETE_PLUGIN_NETMEETING=OFF \
    -DWITH_SPEEX=ON \
    -DWITH_WEBCAM=ON \
    -DWITH_GSM=ON \
    -DWITH_ARTS=OFF \
    -DBUILD_ALL=ON 
fi
%K3make

%else
# else if cmake

%K3configure \
    --disable-gcc-hidden-visibility \
    --sysconfdir=%_sysconfdir \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-final \
%if %jingle
    --enable-jingle \
%endif
    --without-arts \
    --with-speex \
    --enable-jingle \
    --with-wifi \
    --enable-slp

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make
#make -C kopete/plugins/motionautoaway

%endif
# end if cmake

%install
export PATH=%_bindir:$PATH
%if %unstable
%set_strip_method none
%endif

%K3install
#K3install -C kopete/plugins/motionautoaway

%if %cmake
install -dm 0755 %buildroot/%_kde3_iconsdir/
mv %buildroot/%_iconsdir/hicolor %buildroot/%_kde3_iconsdir/hicolor/
mv %buildroot/%_iconsdir/locolor %buildroot/%_kde3_iconsdir/locolor/

install -dm 0755 %buildroot/%_K3applnk/.hidden/
install -m 0644 knewsticker/knewstickerstub/*.desktop %buildroot/%_K3applnk/.hidden/
install -m 0644 lanbrowsing/kcmlisa/*.desktop %buildroot/%_K3applnk/.hidden/

%endif

%if %etc_kppp_allow
>%buildroot/%_sysconfdir/kppp.allow
chmod 0644 %buildroot/%_sysconfdir/kppp.allow
%endif

mkdir -p %buildroot/%_K3sbindir

install -pD -m755 %SOURCE14 %buildroot/etc/control.d/facilities/kppp

mkdir -p %buildroot/%_sysconfdir/xinetd.d
install -m 644 %SOURCE10 %buildroot/%_sysconfdir/xinetd.d/ktalk
#install -m 644 %SOURCE11 %buildroot/%_sysconfdir/xinetd.d/kotalk

mkdir -p %buildroot/%_sysconfdir/rc.d/init.d
install -m 755 %SOURCE12 %buildroot/%_sysconfdir/rc.d/init.d/lisa
#mkdir -p %buildroot/%_sysconfdir/sysconfig
#install -m 644 %SOURCE13 %buildroot/%_sysconfdir/sysconfig/lisa
rm -f %buildroot/%_K3apps/lisa/README

# lisa
mv %buildroot/%_K3bindir/lisa %buildroot/%_K3sbindir

# install kppp icons
cp -ar altlinux/kppp-new-icons/* %buildroot/%_K3apps/kppp/pics/


%pre kppp
/usr/sbin/groupadd -r -f netadmin >/dev/null 2>&1
[ $1 -eq 1 ] || /usr/sbin/control-dump kppp
%post kppp
[ $1 -eq 1 ] || /usr/sbin/control-restore kppp

%pre lisa
useradd -s /dev/null -r _kdelisa >/dev/null 2>&1 ||:
%post lisa
%post_service lisa
%preun lisa
%preun_service lisa

%files
%files common
%_K3conf/*
%_K3cfg/*

%files kdnssd
%_K3lib/kded_dnssdwatcher.so*
%_K3lib/kio_zeroconf.so*
%_K3apps/khtml/kpartplugins/kget_plug_in.desktop
%_K3apps/konqueror/servicemenus/smb2rdc.desktop
%_K3apps/remoteview/zeroconf.desktop
%_K3apps/zeroconf/
%exclude %_K3apps/zeroconf/_rfb._tcp
%_K3srv/kded/dnssdwatcher.desktop
%_K3srv/invitation.protocol
%_K3srv/zeroconf.protocol

%files kfile
%_K3lib/kfile_torrent.so*
%_K3srv/kfile_torrent.desktop

%files filesharing
%_K3lib/fileshare_propsdlgplugin.so*
%_K3lib/kcm_fileshare.so*
%_K3lib/kcm_kcmsambaconf.so*
%_K3srv/fileshare_propsdlgplugin.desktop
%_kde3_iconsdir/*/*/apps/kcmsambaconf.*
%_K3xdg_apps/fileshare.desktop
%_K3xdg_apps/kcmsambaconf.desktop

%files kwifimanager
%_K3bindir/kwifimanager
%_K3lib/libkwireless.so*
%_K3lib/kcm_wifi.so*
%_K3apps/kicker/applets/kwireless.desktop
%_K3apps/kwifimanager
%_kde3_iconsdir/*/*/apps/kwifimanager.*
%_K3doc/en/kwifimanager
%_K3xdg_apps/kcmwifi.desktop
%_K3xdg_apps/kwifimanager.desktop

%files kget
%_K3bindir/kget
%_K3lib/khtml_kget.so*
%_K3apps/kget
%_K3apps/konqueror/servicemenus/kget_download.desktop
%_K3apps/khtml/kpartplugins/kget_plug_in.rc
%_K3mimelnk/application/x-kgetlist.desktop
%_K3snd/KGet_*.ogg
%_K3iconsdir/*/*/*/*kget*.*
%doc %_K3doc/en/kget
%_K3xdg_apps/kget.desktop

%files kppp
%attr(4711, root, root) %_K3bindir/kppp
%_K3bindir/kppplogview
%config %_sysconfdir/control.d/facilities/kppp
%_K3xdg_apps/*ppp*.desktop
%_K3apps/kppp
%_kde3_iconsdir/*/*/apps/kppp.*
%doc %_K3doc/en/kppp
%if %etc_kppp_allow
%config(noreplace) %_sysconfdir/kppp.allow
%endif

%files krdc
%_K3bindir/krdc
%_K3apps/krdc/
%_iconsdir/*/*/*/krdc.png
%_K3apps/zeroconf/_rfb._tcp
%_K3srv/vnc.protocol
%_K3xdg_apps/krdc.desktop
%_K3srv/rdp.protocol
%doc %_K3doc/en/krdc

%files krfb
%_K3bindir/krfb*
%_K3lib/kcm_krfb.so*
%_K3lib/kded_kinetd*.so*
%_K3apps/kinetd
%_K3apps/krfb
%_K3iconsdir/crystalsvg/*/apps/krfb.*
%_kde3_iconsdir/*/*/apps/krfb.*
%_K3srv/kded/kinetd.desktop
%_K3srv/kinetd_krfb*.desktop
%_K3srvtyp/kinetdmodule.desktop
%doc %_K3doc/en/krfb
#
%_K3xdg_apps/*krfb.desktop

%files ksirc
%_K3bindir/?sirc
%_K3libdir/*irc*.so*
%_K3lib/ksirc.so*
%_K3xdg_apps/ksirc.desktop
%_K3apps/ksirc
%doc %_K3doc/en/ksirc
%_kde3_iconsdir/*/*/apps/ksirc*

%files kdict
%_K3bindir/kdict
%_K3libdir/libkdeinit_kdict.so*
%_K3lib/*dict*.so*
%_K3apps/kdict
%_K3apps/kicker/applets/kdictapplet.desktop
%_kde3_iconsdir/*/*/apps/kdict.*
%doc %_K3doc/en/kdict
%_K3xdg_apps/kdict.desktop

%files kopete
%if %jingle
%exclude %_K3bindir/relayserver
%exclude %_K3bindir/stunserver
%endif
%_K3bindir/winpopup-*.sh
%_K3bindir/kopete_latexconvert.sh
%_K3bindir/kopete
%_K3libdir/kconf_update_bin/kopete*
%_K3libdir/libkopete*.so*
%_K3lib/kopete_*.so*
%_K3lib/kcm_kopete_*.so*
%_K3lib/libkrichtexteditpart.so*
%_K3xdg_apps/kopete.desktop
%_K3apps/kopete*
%_K3apps/kconf_update/kopete-*
%_K3srv/kopete_*
%_K3srv/kconfiguredialog/kopete_*
%_K3srv/chatwindow.desktop
%_K3srv/emailwindow.desktop
%_K3srvtyp/kopete*
%_K3snd/Kopete*
%_kde3_iconsdir/*/*/*/kopete*.*
%_K3iconsdir/*/*/*/kopete*.*
%_kde3_iconsdir/*/*/*/jabber*.*
%_K3iconsdir/*/*/*/jabber*
%doc %_K3doc/en/kopete
#
%_K3lib/kio_jabberdisco.so*
%_K3srv/jabberdisco.protocol
%_K3srv/aim.protocol
%_K3srv/irc.protocol
#
%_K3iconsdir/*/*/actions/voicecall.*
%_K3iconsdir/*/*/actions/webcamreceive.*
%_K3iconsdir/*/*/actions/webcamsend.*
%_K3iconsdir/*/*/actions/account_offline_overlay.*
%_K3iconsdir/*/*/actions/add_user.*
%_K3iconsdir/*/*/actions/contact_*_overlay.*
%_K3iconsdir/*/*/actions/delete_user.*
%_K3iconsdir/*/*/actions/edit_user.*
%_K3iconsdir/*/*/actions/emoticon.*
%_kde3_iconsdir/*/*/actions/emoticon.*
%_K3iconsdir/*/*/actions/metacontact_*.*
%_K3iconsdir/*/*/actions/newmsg.*
%_kde3_iconsdir/*/*/actions/newmsg.*
# %_K3iconsdir/*/*/actions/newmessage.*
# %_kde3_iconsdir/*/*/actions/newmessage.*
%_K3iconsdir/*/*/actions/search_user.*
%_K3iconsdir/*/*/actions/show_offliners.*
%_K3iconsdir/*/*/actions/status*.*
%_kde3_iconsdir/*/*/actions/status*.*

%files knewsticker
%_K3bindir/knewsticker*
%_K3lib/*newsticker*.so*
%_K3lib/*kntsrcfilepropsdlg.so*
%_K3applnk/.hidden/knewsticker*
%_K3xdg_apps/knewsticker-standalone.desktop
%_K3apps/kconf_update/knewsticker.upd
%_K3apps/kicker/applets/knewsticker.desktop
%_K3apps/knewsticker
%_kde3_iconsdir/*/*/apps/knewsticker.*
%_K3apps/kconf_update/knt*
%_K3mimelnk/application/x-kopete-emoticons.desktop
%_K3srv/kntsrcfilepropsdlg.desktop
%doc %_K3doc/en/knewsticker

%files ktalkd
%_K3bindir/mail.local
%_K3bindir/*talk*
%_K3lib/kcm_ktalkd.so*
%_iconsdir/*/*/apps/ktalkd*
%_K3snd/ktalkd.wav
%doc %_K3doc/en/ktalkd
%doc %_K3doc/en/kcontrol/kcmtalkd
%config(noreplace) %_sysconfdir/xinetd.d/ktalk
#%config(noreplace) %_sysconfdir/xinetd.d/kotalk
%_K3xdg_apps/kcmktalkd.desktop

%files lisa
%doc lanbrowsing/lisa/README
#%config(noreplace) %_sysconfdir/sysconfig/lisa
%config %_sysconfdir/rc.d/init.d/lisa
%_K3bindir/reslisa
%_K3sbindir/lisa
%_K3lib/kcm_lanbrowser*.so*
%_K3lib/kio_lan*.so*
%_K3apps/konqueror/dirtree/remote/lan.desktop
%_K3apps/konqsidebartng/virtual_folders/services/lisa.desktop
%_K3apps/lisa
%_K3apps/remoteview/lan.desktop
%_K3srv/*lan.protocol
%doc %_K3doc/en/lisa
%doc %_K3doc/en/kcontrol/lanbrowser
%_K3applnk/.hidden/*lisa.desktop
%_K3applnk/.hidden/kcmkiolan.desktop

%files kpf
#%doc debian/copyright
%_K3lib/kpf*.so*
%_K3apps/kicker/applets/kpfapplet.desktop
%_iconsdir/*/*/*/kpf.png
%_K3srv/kpf*
%doc %_K3doc/en/kpf

%files rss
%_K3bindir/feedbrowser
%_K3bindir/rssclient
%_K3bindir/rssservice
%_K3libdir/librss.so*
%_K3srv/rssservice.desktop

%files devel
%_K3libdir/*.la
%_K3lib/*.la
#%_K3lib/plugins/designer/libkopetewidgets.*
%_K3includedir/*

%changelog
* Sat Jun 02 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt4
- Fixes from GIT http://www.trinitydesktop.org from 3.5.13 to 01.06.2012 is backported.

* Fri Jun 01 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt3
- Dependency direct set to GCC C++ version 4.5, for hook bugs into 4.6.

* Sun May 13 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- Build with new linux/videodev.h place.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Wed Feb 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt2.2
- Removed bad RPATH

* Mon Apr 25 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.12-alt2.1
- Remove xorg-devel requirement

* Thu Feb 24 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Tue Dec 07 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Wed Feb 10 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt5
- update to lastest 3.5 branch
- fix compile with new autoconf
- remove old consolehelper stuff

* Tue Aug 25 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt4
- fix compile with new automake and gcc

* Wed Dec 03 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt3
- don't package libjingle's relayserver and stunserver with kopete

* Tue Dec 02 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt2
- remove deprecated macroses from specfile
- fix compile with new gcc
- add patches from SuSE to fix krdc/krfb

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Thu Jan 17 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt5
- fix to check empty RESOLV_MODS variable in kppp

* Wed Jan 16 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt4
- modify /etc/resolv.conf according /etc/sysconfig/network::RESOLV_MODS

* Mon Dec 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt3
- use 'search' instead 'domain' for resolv.conf in kppp

* Tue Nov 20 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt2
- don't include default Desktop link for lan:/

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Tue Sep 25 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt11
- fix modem device name when configure new modem in kppp
- add various kopete upstream fixes

* Mon Sep 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt10
- resolve hostname when publish dnssd service

* Fri Sep 14 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt9
- increase default bandwidth limit of kpf applet

* Mon Sep 03 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt8
- move remoteview/lan.desktop to lisa subpackage
- fix _https._tcp type for kdnssd

* Fri Aug 31 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt7
- built with libortp0.7

* Wed Aug 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt6
- fix build kopete with new libortp; thanks shrek@alt

* Tue Aug 28 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt5
- update kdnssd requires
- built kopete with jingle
- add _https._tcp; add Russian translation of kdnssd instances

* Mon Aug 06 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt4
- fix default ICQ encoding when create account in Kopete

* Wed Jul 04 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt3
- added kdenetwork-3.5.7-alt-msdfsProxyType.patch to fix the problem
  described in https://bugs.launchpad.net/ubuntu/+source/kdenetwork/+bug/95452
- add small kopete fixes from KUbuntu
- thanks morozov@alt
- dropped kdenetwork-3.5.3-alt-textrel.patch

* Thu Jun 21 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- add /dev/ttyLTM0,/dev/ttySM0 to kppp devices list

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version
- apply patch for using external libqca

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt4
- remove patch against text relocations
- don't apply patch for using external libqca

* Fri Feb 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt3
- show unnamed hosts in lan:/ by default
- move lisa/README to %_docdir

* Thu Feb 08 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- fix desktop categories

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Thu Jan 25 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt3
- built without arts to fix crash kwifimanager

* Fri Oct 20 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt2
- fix compile kopete motionaway plugin

* Mon Oct 16 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version
- turn on ktalkd on localhost by default

* Fri Sep 01 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version
- update to kopete-0.12.2
- add patches from RH

* Wed Jul 12 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt2
- remove requires to samba-client
- fix text relocations; thanks Alexey Morozov
- add patches for jingle (don't compile) from Alexey Morozov
- add patch to fix "Your ICQ is old"

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Wed May 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt2
- rebuilt with new gcc
- apply libjingle/encoding fixed for kopete; 10x Alexey Morozov

* Thu Mar 30 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Mon Mar 27 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt5
- add patch to default cp1251 for be,ru,uk in kopete

* Fri Mar 24 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt4
- move services/emailwindow.desktop to kopete subpackage

* Thu Mar 23 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt3
- update kopete to 0.12-beta2

* Wed Mar 15 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt2
- update kopete to 0.12-beta1

* Wed Feb 01 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Wed Dec 07 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt2
- add patch for external libqca

* Wed Dec 07 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Mon Oct 31 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt4
- fix wifi compile

* Thu Sep 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt3
- export RESOLV_MODS=no in kppp before start pppd
- built kopete without libxmms

* Mon Aug 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt2
- add patch for libgadu from kopete

* Mon Jun 06 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Wed May 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt2
- add patch for kopete encoding by Oleksandr Shneyder AKA nCryer
- fix move network_neighborhood.desktop to %%_datadir/apps/kdesktop/DesktopLinks/

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt4
- rebuild

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt3
- add /dev/mobile to kppp devices list
- rebuild with gcc3.4

* Fri Jan 14 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- add patch for redial on no dial tone

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Tue Jan 04 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Thu Dec 09 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt2
- rebuild

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Fri Oct 01 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Thu Aug 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt4
- remove requires to vnc*

* Mon Jul 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt3
- fix kppp dock width in icewm
- fix knewsticker menu section

* Tue Jul 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- fix menu-files

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Thu Apr 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version
- add kppp-callback.patch thanks droid_ภา_terem.kiev.ua

* Fri Mar 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt2
- fix requires, fix kwifimanager menufile

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH

* Wed Mar 03 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt0.1
- new version
- update code from KDE_3_2_BRANCH

* Wed Jan 28 2004 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt4
- fix starting knode
- fix service lisa stop/condrestart
- fix requires to vnc*
- add /dev/modem1 for select in kppp
- remove /usr/lib/*.la files

* Mon Nov 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt3
- fix lisa drop privileges
- add %_datadir/alt/kde/desktoplnk/network_neighborhood.desktop

* Fri Oct 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- fix service lisa start
- add new icons for kppp (thanks berndzimmer at gmx.de)
- move ktalkdrc,kdictrc,ksircrc to kde-settings

* Thu Sep 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update from cvs

* Fri Sep 05 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt2
- update from cvs
- return kmail to 3.1.3_release

* Wed Aug 20 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs
- don't apply passwordfd.patch

* Mon Jul 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.2
- update code from cvs
- turn strict ansi off
- remove /etc/kppp.allow from package

* Thu Jul 17 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.1
- update code from cvs
- set default server to mova.org in kdict
- fix wait cursor in kmail

* Fri Jul 04 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt4
- update code from cvs

* Thu Jun 26 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt3
- update code from cvs
- add MDK patches
- add SuSE passwordfd.patch for kppp

* Thu May 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt2
- fix /etc/control.d/facilities/kppp

* Mon May 26 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update code from cvs KDE_3_1_BRANCH

* Tue Apr 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt2
- update code from cvs KDE_3_1_BRANCH
- add MDK patches

* Mon Mar 31 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update code from cvs KDE_3_1_BRANCH
- kmail: quoteprintable filenames in attaches

* Fri Mar 14 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt0.1
- update code from cvs KDE_3_1_BRANCH
- apply Patch5004
- add MDK patches

* Tue Feb 25 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt5.junior
- don't include /etc/kppp.allow for Junior

* Tue Feb 18 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt5
- update code from cvs KDE_3_1_BRANCH

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt4
- update from cvs

* Thu Jan 30 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update from cvs

* Tue Jan 21 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update from cvs

* Wed Jan 08 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs

* Tue Nov 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.21
- update from cvs

* Wed Nov 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2
- fix control file for kppp

* Thu Oct 31 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.11
- update from cvs

* Fri Oct 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.10
- update from cvs
- increase %%release to updarede Daedalus

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt3
- rebuild with objprelink

* Fri Sep 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- rebuild with gcc 3.2
- update from cvs
- add patches from cooker

* Fri Aug 16 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update from cvs

* Mon Jul 08 2002 ZerG <zerg@altlinux.ru> 3.0.2-alt2
- fix normal startup of kppp from menu via consolehelper

* Thu Jul 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version
- add service lisa to /etc/rc.d
- remove suid for kppp, now via consolehelper

* Mon Jun 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- fix menu items

* Sun May 26 2002 ZerG <zerg@altlinux.ru> 3.0.1-alt1
- new version
- split

* Thu May 16 2002 ZerG <zerg@altlinux.ru> 3.0-alt4
- update from cvs
- fix kmailcvt menu entry

* Mon Apr 22 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- move to /usr
- update from cvs

* Fri Apr 12 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- build without debug

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- release

* Mon Apr 01 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.2.cvs20020401
- update from cvs

* Fri Mar 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.1.rc3
- build for ALT

* Thu Mar 21 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Sat Mar 16 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc2.1mdk
- RC2

* Sat Jan 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Sun Dec 30 2001 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.4mdk
- Fix previous changelog
- Allow KDE 2 and KDE 3 to be installed in same time (lot of changes, see CVS
  for details)
- Don't build static libraries
- Remove KDE 2's changelogs (KDE 2 and KDE 3 spec files have a separate life
  now)
- Remove 7.2 support

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.3mdk
- Rename to allow KDE 2 and KDE 3 to be installed in same time

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-3mdk
- kde 3.0 beta1

* Thu Nov 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Improve spec

* Fri Nov 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0
