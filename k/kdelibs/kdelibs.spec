
%undefine __libtoolize
%define _keep_libtool_files 1
%define _optlevel s
%define versioning_hack 1
%define unstable 0
%define bad_doc 0
%define arts 0
%define cmake 1

%define qtdir %_qt3dir

%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_K3lib
#set_perl_req_method relaxed
%add_findreq_skiplist %_K3apps/dcopidlng/*
%add_findprov_skiplist %_K3apps/dcopidlng/*
%add_verify_elf_skiplist %_K3libdir/libkscreensaver.so*
%add_verify_elf_skiplist %_K3libdir/libkscreensaver.so.4.2.0
%add_findreq_skiplist %_K3bindir/fileshareset

%define major 3
%define minor 5
%define bugfix 13
%define rel alt2
Name: kdelibs
Version: %major.%minor.%bugfix
Release: %rel
#%define conflictver %major.%minor.%bugfix-alt0.0.1
%define conflictver 3.5.10-alt1
%define conflictver_kdevelop 3.5.3-alt0.0.1
%define reqver %major.%minor

Summary: K Desktop Environment - Libraries
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
URL: http://www.kde.org/

Provides: kde-settings = %version-%release
Obsoletes: kde-settings < %version-%release
Provides: kde-settings-lite = %version-%release
Obsoletes: kde-settings-lite < %version-%release

%if %unstable
Requires: gdb
%endif
PreReq: kde-common >= %reqver
Requires: ca-certificates
Requires: libart_lgpl >= %{get_version libart_lgpl}
#Requires: %{get_dep libqt3}
%if %arts
#Requires: %{get_dep libarts-qtmcop}
%endif

# Conflicts for Main
Conflicts: kaffeine <= 0.4.3b-alt3.1
Conflicts: kmplayer <= 0.9.0c-alt1
Conflicts: openoffice <= 1.0.2-alt5
Conflicts: sim-common <= 1:0.9.4-alt8
Conflicts: kile <= 1.7.1-alt1.1.1

# Conflicts for old KDE
#Conflicts: kde-i18n-de < %conflictver kde-i18n-fr < %conflictver kde-i18n-he < %conflictver
#Conflicts: kde-i18n-et < %conflictver kde-i18n-ru < %conflictver kde-i18n-uk < %conflictver
Conflicts: kdevelop-common < %conflictver_kdevelop
Conflicts: kdeaccessibility-common < %conflictver
Conflicts: kdeaddons-common < %conflictver
Conflicts: kdeadmin-common < 1:%conflictver
Conflicts: kdeartwork-common < %conflictver
#Conflicts: kdebase-common < %conflictver kdebase-common < %version
Conflicts: kdebase-common < %conflictver
Conflicts: kdebindings-common < %conflictver
Conflicts: kdeedu-common < %conflictver
Conflicts: kdegames-common < %conflictver
Conflicts: kdegraphics-common < %conflictver
Conflicts: kdemultimedia-common < %conflictver
Conflicts: kdenetwork-common < %conflictver
Conflicts: kdepim-common < 1:%conflictver
Conflicts: kdetoys-common < %conflictver
Conflicts: kdeutils-common < %conflictver
Conflicts: kdesdk-common < %conflictver
Conflicts: kdewebdev-common < %conflictver


Source: kdelibs-%version.tar
#Source: kdelibs-3.3.92.tar
#
Source122: x-toc.desktop
Source123: x-icq.desktop
Source124: x-mplayer2.desktop

# MDK -> ALT
Patch01: kdelibs-3.1.94-iconssearch.patch
Patch02: kdelibs-3.5.12-kfiledialogbox.patch
#
Patch04: kdelibs-3.5.12-fix-cups-by-default.patch
Patch05: kdelibs-3.5.12-fix-default-spell-checker.patch
#
Patch07: kdelibs-3.4.0-fix-kcmshell-list.patch

# Gentoo
Patch10: kdelibs-3.5.12-libutempter.patch

# MDK
Patch30: kdelibs-3.2-remove-debug.patch
Patch31: kdelibs-3.5-fix-kde-default-font-value.patch

# SuSE
Patch1003: show-distribution.diff
#
Patch1007: kdeXrc-alt.patch
#
Patch1010: disable-idn-support.diff
#
Patch1020: x-jar-desktop.diff


# RH
Patch3009: kdelibs-3.1-ssl-krb5.patch
Patch3010: kdelibs-3.2-ALT-flash.patch
Patch3011: kdelibs-3.5.2-pcre.patch

# Sergey A. Sukiyazov <corwin@micom.don.ru>
Patch4600: kdelibs-3.1.2-fix-kprocio-def-codec.patch
Patch4601: kdelibs-3.5.12-alt-fix-kdoctools-mime-charset.patch

# misc

# ALT patches
Patch5001: kdelibs-3.5.12-alt-versioning-hack.patch
Patch5002: kdelibs-3.5-exists_exe.patch
Patch5003: kdelibs-3.5.12-alt-defaults.patch
Patch5004: kdelibs-3.5.12-alt-htmldocdir.patch
Patch5005: kdelibs-3.4.1-alt-dont-change-group.patch
Patch5006: kdelibs-3.5.12-alt-fix-build.patch
Patch5007: kdelibs-3.5.12-alt-fix-compile.patch
Patch5008: kdelibs-3.5.2-alt-maccyrillic.patch
Patch5009: kdelibs-3.5.12-alt-fix-linking.patch
#
Patch5011: kdelibs-3.5.12-alt_la2so_load_module.patch
Patch5012: kdelibs-3.5.12-alt_la2so.patch
Patch5013: kdelibs-3.1.4-alt-ldl.patch
Patch5014: kdelibs-3.1.4-alt-no_ltdl.patch
#
Patch5016: kdelibs-3.5.12-lang.patch
Patch5017: kdelibs-3.5.10-alt-lua51.patch
Patch5018: kdelibs-3.5.10-alt-xdg-autostart.patch
#
Patch5022: kded-3.5.12-applications.menu.patch
Patch5023: kdelibs-3.5.10-alt-automake.patch
Patch5024: kdesu-3.5.3-fix-exec.patch
#
Patch5026: kdecore-3.5.12-crystalsvg-default-icontheme.patch
Patch5027: kdelibs-3.3.0-fix-build.patch
Patch5028: kssl-3.5.10-libssl-name.patch
Patch5029: kio-3.2.3-subfs.patch
Patch5030: kdelibs-3.5.12-xdg-dirs.patch
Patch5031: kdelibs-3.5.0-alt-etc-sysconfig.patch
Patch5032: kdelibs-3.5.0-alt-locale-placement.patch
Patch5033: kdelibs-3.5.5-mark-user-edited.patch
#
Patch5035: kdelibs-3.5.6-alt-kurl-encoding.patch
Patch5036: kdelibs-3.5.7-alt-html-copypaste.patch
Patch5037: kdelibs-3.5.7-alt-browser-mailer-env.patch
Patch5038: kdelibs-3.5.7-alt-zip-dont-embed.patch
Patch5039: kdelibs-3.5.8-alt-pdf-dont-embed.patch
Patch5040: kdelibs-3.5.9-alt-ltdl-use-so.patch
Patch5041: kdelibs-3.5.12-alt-add-translations.patch
Patch5042: kdelibs-3.5.12-alt-menu-prefix-kde3.patch
Patch5043: tde-3.5.13-build-defdir.patch
Patch5044: tdelibs-3.5.13-work-defdir.patch
Patch5045: tde-3.5.13-tray_icon_scale_dis.patch

# security patches
# end security patches

# Automatically added by buildreq on Thu Apr 08 2004 (-bi)
#BuildRequires: XFree86-devel XFree86-libs bzlib-devel doxygen fontconfig freetype2 gcc-c++ gcc-g77 glib2 kde-settings libalsa-devel libart_lgpl-devel libarts-devel libarts-qt-devel libcups-devel libjpeg-devel libldap-devel libpcre-devel libpcsclite-devel libpng-devel libqt3-devel libssl-devel libstdc++-devel libtiff-devel libutempter-devel libxml2-devel libxslt-devel netpbm qt3-designer qt3-doc su xml-utils zlib-devel
BuildRequires(pre): cmake kde-common-devel libtqt-devel libqt3-devel libart_lgpl-devel
BuildRequires: bzlib-devel doxygen aspell
BuildRequires: gcc-c++ libalsa-devel libcups-devel libltdl7-devel
BuildRequires: libjpeg-devel libldap-devel libpcre-devel
BuildRequires: libpng-devel libqt3-devel libssl-devel libstdc++-devel libtiff-devel
BuildRequires: libutempter-devel libxml2-devel libxslt-devel netpbm libnetpbm-devel
BuildRequires: qt3-doc xml-utils zlib-devel libkrb5-devel libidn-devel
BuildRequires: libkrb5-devel libaspell-devel libacl-devel libattr-devel
BuildRequires: libavahi-qt3-devel pkg-config liblua5-devel libjasper-devel
BuildRequires: glibc-utils glibc-devel glib2-devel
BuildRequires: openexr-devel libXdmcp-devel libXcomposite-devel
#BuildRequires: libqt3-devel-cxx = %__gcc_version_base
BuildRequires: libqt3 >= 3.2.0 libqt3-devel >= 3.2.0
BuildRequires: flex su sudo
%if %arts
BuildRequires: libarts-devel >= 1.5.8 libarts-qtmcop-devel >= 1.5.8
%endif
BuildRequires: djvu-common libgnutls-devel
# old
BuildRequires: openjade docbook-utils docbook-dtds
# hack against apt
#BuildRequires: libqt3-qsa > 3.0 libqt3-qsa-devel > 3.0

%description
Libraries for the K Desktop Environment.

%package devel
Group: Development/KDE and QT
Summary: Header files and documentation for compiling KDE applications
%if %arts
Requires: libarts-devel, libarts-qtmcop-devel
%endif
Requires: %name = %version-%release
Requires: libidn-devel libavahi-qt3-devel libart_lgpl-devel libpng-devel
Requires: kde-common-devel >= 0.2.0 libtqt-devel
Requires: libpcre-devel libacl-devel libattr-devel libutempter-devel
Requires: libXdmcp-devel libXcomposite-devel libXdamage-devel libxkbfile-devel libXtst-devel libXScrnSaver-devel
Requires: libXpm-devel libXxf86misc-devel libXxf86vm-devel libXt-devel imake xorg-cf-files
Provides: %name-devel-cxx = %__gcc_version_base

%description devel
This package includes the header files you will need to compile applications
for KDE. 

%package apidocs
Group: Development/KDE and QT
Summary: The KDE API Reference
Requires: %name-devel = %version

%description apidocs
This package included is the KDE %version API documentation
in HTML format for easy browsing.

%prep
%setup -q

%patch01 -p1
%patch02 -p1
#
%patch04 -p1
%patch05 -p1
#
%patch07 -p1
#
%patch10 -p1
#
%patch30 -p1
%patch31 -p1

%patch1003 -p0
#
# kderc
%patch1007 -p0
subst "s|kde@MAJOR@rc|kde%{major}rc|" kdecore/kconfigbackend.cpp
#
%patch1010 -p0
#
%patch1020 -p0

###%patch3009 -p1
%patch3010 -p1
###%patch3011 -p1

# corwin@micom.don.ru
%patch4600 -p1
%patch4601 -p1


# ALT
%patch5001 -p1
%patch5002 -p1 -b .exists_exe
%patch5003 -p1
%patch5004 -p1
%patch5005 -p1
%patch5006 -p1
%patch5007 -p1
%patch5008 -p1
%patch5009 -p1
#
%patch5011 -p1
%patch5012 -p1
#%patch5013 -p1
#%patch5014 -p1
#
%patch5016 -p1
%patch5017 -p1
%patch5018 -p1
#
%patch5022 -p1 -b .menu
###%patch5023 -p1
# su exec
%patch5024 -p1
#
%patch5026 -p1
%if %bad_doc
%patch5027 -p1
%endif
%patch5028 -p1
%patch5029 -p1
%patch5030 -p1
%patch5031 -p1
%patch5032 -p1
%patch5033 -p1
#
%patch5035 -p1
%patch5036 -p1
%patch5037 -p1
%patch5038 -p1
%patch5039 -p1
%patch5040 -p1
%patch5041 -p1
%patch5042 -p1
%patch5043
%patch5044
%patch5045

# security
# end security

%if %versioning_hack
cat > kdecore/libkdecore_add.map <<__EOF__
CXX3 {
    global:
	extern "C++"  {
	    KApplication::KApplication*;
	    KConfig::KConfig*;
	    KLocale::KLocale*;
	    KURL::KURL*;
	    KAppDCOPInterface::KAppDCOPInterface*;
	    KAudioPlayer::KAudioPlayer*;
	};
};
__EOF__
%if %cmake
%else
grep -q -elibkdecore_la_LDFLAGS.*version-script kdecore/Makefile.am || \
perl -pi -e "s/(^libkdecore_la_LDFLAGS.*)/\1 -Wl,--version-script=libkdecore_add.map/" kdecore/Makefile.am
%endif
%endif

%if %cmake
%else
sed -i '\|\${kdeinit}_LDFLAGS[[:space:]]=[[:space:]].*-no-undefined|s|-no-undefined|-no-undefined -Wl,--warn-unresolved-symbols|' admin/am_edit
for f in `find $PWD -type f -name Makefile.am`
do
    sed -i -e '\|_la_LDFLAGS.*[[:space:]]-module[[:space:]]|s|-module|-module \$(KDE_PLUGIN) -Wl,--warn-unresolved-symbols|' $f
    #sed -i -e '\|_la_LDFLAGS.*[[:space:]]-no-undefined|s|-no-undefined|-no-undefined -Wl,--allow-shlib-undefined|' $f
    grep -q -e 'lib.*SOURCES' $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
sed -i -e 's|\$USER_INCLUDES|-I%_includedir/tqtinterface \$USER_INCLUDES|' admin/acinclude.m4.in
make -f admin/Makefile.common cvs ||:
%endif

%build
%if %cmake
BD=%_builddir/%name-%version/BUILD

export LD_LIBRARY_PATH=$BD/kdecore:$BD/kdefx:$BD/kdeui:$BD/kio:$BD/dcop:$BD/kdesu:$BD/kwallet/client:$LD_LIBRARY_PATH
export PATH=%_K3bindir:$PATH
#add_optflags -DNEED_BZ2_PREFIX -DAVAHI_API_0_6 -I%_includedir/linux-libc-headers/include
export QTDIR=%qtdir
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%qtdir/lib"
export DESTDIR=%buildroot
# export LIBDIR=/%_libdir/kde3

%if %unstable
%define _K4buildtype RelWithDebInfo
%endif

if ! [ -f $BD/CMakeCache.txt ]
then
%K3cmake \
    -DKDE_MALLOC=OFF \
    -DKDE_MALLOC_DEBUG=OFF \
    -DKDE_MALLOC_FULL=OFF \
%if %arts
    -DWITH_ARTS=ON \
%else
    -DWITH_ARTS=OFF \
%endif
    -DWITH_ALSA=ON \
    -DWITH_LIBART=ON \
    -DWITH_LIBIDN=OFF \
    -DWITH_SSL=ON \
    -DWITH_CUPS=ON \
    -DWITH_LUA=OFF \
    -DWITH_TIFF=OFF \
    -DWITH_JASPER=OFF \
    -DWITH_OPENEXR=OFF \
    -DWITH_ASPELL=ON \
    -DASPELL_DATADIR=/usr/lib/aspell \
    -DWITH_HSPELL=OFF \
    -DKDE_DISTRIBUTION_TEXT="%distribution %_target_cpu"

#    -DDESTINATION="%distribution %_target_cpu" \

    # fix glibc functions detection
#    sed -i "s|.*#undef HAVE_STRLCAT_PROTO.*|#define HAVE_STRLCAT_PROTO 1|" $BD/config.h
#    sed -i "s|.*#undef HAVE_STRLCAT.*|#define HAVE_STRLCAT 1|" $BD/config.h
#    sed -i "s|.*#undef HAVE_STRLCPY_PROTO.*|#define HAVE_STRLCPY_PROTO 1|" $BD/config.h
#    sed -i "s|.*#undef HAVE_STRLCPY.*|#define HAVE_STRLCPY 1|" $BD/config.h
fi
%K3make

%else
# else if cmake

%add_optflags -I%_includedir/tqtinterface
export LD_LIBRARY_PATH=$QTDIR/%_lib:$LD_LIBRARY_PATH
export PATH=%_bindir:$PATH
#add_optflags -DNEED_BZ2_PREFIX -DAVAHI_API_0_6 -I%_includedir/linux-libc-headers/include
export QTDIR=%qtdir
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%qtdir/lib"

if true
then
%K3configure \
		    --disable-gcc-hidden-visibility \
%if %unstable
                    --enable-debug=full \
%else
    		    --disable-debug \
                    --enable-final \
%endif
%if %arts
		    --with-arts \
%else
		    --without-arts \
%endif
		    --enable-fast-malloc=no \
                    --enable-mitshm \
                    --enable-cups \
                    --disable-libfam \
		    --enable-dnotify \
		    --enable-inotify \
		    --enable-sendfile \
		    --enable-openpty \
                    --enable-pcre \
		    --enable-dnssd \
                    --with-distribution="%distribution %_target_cpu" \
                    --with-alsa \
		    --with-rgbfile=%_x11x11dir/rgb.txt \
                    --x-includes=%_x11includedir \
                    --x-libraries=%_x11libdir
#		    --with-sudo-kdesu-backend \
fi
%make

%endif
# end if cmake

%install
%if %unstable
%set_strip_method none
%endif

%if %cmake
#export DESTDIR=%buildroot
%K3install

install -d -m0755 %buildroot/%_K3applnk
install -m0644 kioslave/iso/kio_iso.desktop %buildroot/%_K3applnk/
install -d -m0755 %buildroot/%_K3i18n
install -m0644 kdecore/all_languages.desktop %buildroot/%_K3i18n/all_languages
install -d -m0755 %buildroot/%_K3emo/Default
install -m0644 pics/emoticons/*.{png,xml} %buildroot/%_K3emo/Default

install -d -m0755 %buildroot/%_K3datadir/cmake
install -m0644 BUILD/kdelibs.cmake %buildroot/%_K3datadir/cmake/

ln -fs ../common %buildroot/%_K3doc/en/kspell/common

%else
# else if cmake
%K3install
%endif
# end if cmake

# move l10n files
#mkdir -p %buildroot/%_datadir/kde/locale
# mv %buildroot/%_datadir/locale/* %buildroot/%_datadir/kde/locale ||:
#if [ -d %buildroot/%_datadir/kde/locale/all_languages ]; then
#    rm -rf %buildroot/%_datadir/kde/locale/all_languages
#    > %buildroot/%_datadir/kde/locale/all_languages
#fi

# menu
mkdir -p %buildroot/%_kdeconfdir/xdg/menus/applications-merged/
mv %buildroot/%_sysconfdir/xdg/menus/applications.menu %buildroot/%_kdeconfdir/xdg/menus/applications-merged/

#if ls -1 %buildroot/%_iconsdir/hicolor/*/*/*.png
#then
#    for f in %buildroot/%_iconsdir/hicolor/*/*/*.png
#    do
#	newplace=`echo "$f"| sed "s|/hicolor/|/crystalsvg/|"`
#	[ -f "$newplace" ] || mv "$f" "$newplace"
#    done
#fi

# CA certificates bundle
[ -f %buildroot/%_K3apps/kssl/ca-bundle.crt ] || exit 1
ln -sf `relative %_datadir/ca-certificates/ca-bundle.crt %_K3apps/kssl/ca-bundle.crt` %buildroot/%_K3apps/kssl/ca-bundle.crt

# install crystal cursors
cp -ar altlinux/crystalcursors/* %buildroot/%_K3iconsdir/crystalsvg/


[ -f %buildroot/%_K3mimelnk/application/x-toc.desktop ] && exit 1
install -m0644 %SOURCE122 %buildroot/%_K3mimelnk/application/x-toc.desktop
[ -f %buildroot/%_K3mimelnk/application/x-icq.desktop ] && exit 1
install -m0644 %SOURCE123 %buildroot/%_K3mimelnk/application/x-icq.desktop
# resolve conflict with old djvu-common
[ -f %_K3mimelnk/image/x-djvu.desktop ] \
    && rm -f %buildroot/%_K3mimelnk/image/x-djvu.desktop ||:
# fix xcf mimetype
cp -ar %buildroot/%_K3mimelnk/image/x-xcf-gimp.desktop %buildroot/%_K3mimelnk/image/x-xcf.desktop
sed -i "s|^MimeType=.*|MimeType=image/x-xcf|" %buildroot/%_K3mimelnk/image/x-xcf.desktop

mkdir -p %buildroot/%_bindir
# symlinks to standart place
for n in kbuildsycoca kcmshell kcookiejar kde-config kded kdeinit kshell kwrapper meinproc
do
    ln -s `relative %_K3bindir/$n %_bindir/$n` %buildroot/%_bindir/$n
done


%files
%exclude %_kdeconfdir/xdg/menus/applications-merged/*
#
%_K3conf/*
#
%dir %_K3doc/en/
%doc %_K3doc/en/common/
%if !%bad_doc
%doc %_K3doc/en/kspell/

%endif
#
#
#
%_bindir/*
%_K3bindir/*
%exclude %_K3bindir/kgrantpty
#
%_K3libdir/*.so*
%_K3lib/*.so
#
%dir %_K3lib/plugins/
%dir %_K3lib/plugins/styles/
%_K3lib/plugins/styles/*.so
#
#
#
%_K3xdg_apps/kresources.desktop
%_K3applnk/kio_iso.desktop
%_K3apps/dcopidlng/
%_K3apps/kabc/
%_K3apps/kcm_componentchooser/
%_K3apps/kconf_update/
%_K3apps/kdeprint/
%_K3apps/kjava/
%_K3apps/kdeui/
%_K3apps/kdewidgets/
%_K3apps/khtml/
%_K3apps/kio_uiserver/
%_K3apps/knewstuff/
%_K3apps/knotify/
%_K3apps/konqueror/servicemenus/isoservice.desktop
%_K3apps/ksgmltools2/
%_K3apps/kssl/
%_K3apps/kstyle/
%_K3apps/ktexteditor_*/
%_K3apps/kcertpart/
%_K3apps/katepart/
%_K3apps/proxyscout/
%_K3start/*.desktop
#
%_iconsdir/crystalsvg
#
%_K3i18n/all_languages
#
%_K3mimelnk/magic
%_K3mimelnk/*/*.desktop
#
%dir %_K3emo
%_K3emo/Default
#
%dir %_K3srv/
%_K3srv/*.desktop
%_K3srv/*.kimgio
%_K3srv/*.protocol
#
%dir %_K3srv/kded
%_K3srv/kded/*.desktop
#
%dir %_K3srv/kresources
%_K3srv/kresources/kabc_*.desktop
%dir %_K3srv/kresources/kabc
%_K3srv/kresources/kabc/*.desktop
#
%dir %_K3srvtyp
%_K3srvtyp/*.desktop

%files devel
%_K3libdir/libkdefakes_nonpic.a
%_K3libdir/libkdefakes_pic.a
%_K3libdir/*.la
%_K3lib/*.la
%dir %_K3lib/plugins/designer/
%_K3lib/plugins/designer/*.so
%_K3lib/plugins/designer/*.la
#
%_K3includedir/*.h
#_K3includedir/*.pot
%_K3includedir/*.tcc
#
%if %arts
%_K3includedir/arts/
%endif
%_K3includedir/dnssd/
%_K3includedir/dom/
%_K3includedir/kdeprint/
%_K3includedir/kdesu/
%_K3includedir/khexedit
%_K3includedir/kio/
%_K3includedir/kjs/
%_K3includedir/kmdi/
%_K3includedir/kmediaplayer/
%_K3includedir/knewstuff/
%_K3includedir/kparts/
%_K3includedir/kresources
%_K3includedir/ksettings
%_K3includedir/kspell2/
%_K3includedir/ktexteditor/
%_K3includedir/kabc/
%_K3includedir/kate/
%_K3includedir/kunittest/
%_K3includedir/libkmid/
%_K3includedir/libkrandr/
%_K3includedir/libkrsync/
#
%if %cmake
%dir %_K3datadir/cmake
%_K3datadir/cmake/*.cmake
%endif

%files apidocs
#%doc %_K3doc/en/%name-*-apidocs

%changelog
* Sat May 05 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- Icons resize into tray is disabled for aspect rate broke prevent.
- Path to make_driver_db_cups is fixed.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Mon Nov 28 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt13
- rebuilt

* Tue Nov 08 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt12
- fix to build

* Tue May 03 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt11
- fix requires

* Fri Apr 29 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt10
- fix requires

* Wed Apr 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.12-alt9
- changed built-in menu prefix from kde- to kde3-

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.12-alt8
- dropped altlinux-menus dependency

* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.12-alt7
- system freedesktop menu support

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt6
- fix conflict with kde-settings-lite (ALT#25412)

* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt5
- add kcmshell to standart PATH

* Fri Feb 18 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt4
- move to alternate place

* Tue Feb 15 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt3
- single-click by default

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- add libpng-devel to requires

* Thu Nov 11 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Fri Oct 30 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt9
- clean specfile

* Fri Oct 30 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt8
- update from lastest 3.5 branch

* Mon Oct 19 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt7
- fix to build with new lua

* Mon Sep 14 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt6
- add /etc/xdg/autostart support

* Tue Aug 25 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt5
- fix to build with new automake

* Fri May 08 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt4
- fix to build with gcc4.4
- fix build requires

* Wed Oct 22 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt3
- rebuilt with new gcc

* Wed Oct 01 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt2
- fix XCF mimetype

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Mon Jul 07 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt5
- translate desktop-files via desktop_translations.po

* Wed Mar 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt4
- fix internal libltdl to try load .so if .la not found

* Thu Mar 06 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt3
- add libgnutls-devel to build requires to detect libcups-devel

* Tue Mar 04 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt2
- rebuilt only

* Thu Feb 21 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Thu Jan 31 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt6
- don't embed pdf into konqueror by default

* Mon Jan 28 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt5
- override locale environment variables by KDE settings if configured
  (clean ~/.kde/share/config/kdeglobals::Locale or use $KDE_LANG)

* Mon Dec 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt4
- add SuSE patch to fix qxembed for new flash plugin

* Tue Nov 20 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt3
- remove switch language menu item from all applications

* Mon Nov 12 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt2
- fix UI language with POSIX and C locales

* Tue Oct 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Mon Oct 15 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt11
- add support for LANGUAGE environment variable
- get default country from environment variables

* Fri Oct 12 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt10
- add patch to fix compile with new cups

* Fri Oct 12 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt9
- save cache to /var/tmp by default

* Mon Aug 20 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt8
- add patches to fix CVE-2007-3820, CVE-2007-4224, CVE-2007-4225, kde#146105

* Thu Aug 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt7
- don't embed zip files into Konqueror by default

* Mon Jul 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt6
- small fix BROWSER and MAILER environment variables setup

* Fri Jul 13 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt5
- setup BROWSER and MAILER environment variables accordign KDE settings

* Mon Jun 18 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt4
- fix copy-paste text encoding from konqueror; thanks stanv@alt

* Wed Jun 13 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt3
- add alternate search path for configuration files

* Tue Jun 05 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- add requires to libart_lgpl version

* Wed May 23 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Wed May 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt9
- add libutempter-devel to requires

* Wed May 16 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt8
- sync with SuSE patches

* Mon May 14 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt7
- add patch for libutempter

* Mon Apr 09 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt6
- add patch to don't jump top on page before going to new URL

* Mon Apr 02 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt5
- add patch against utf8 bug

* Thu Mar 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt4
- remove patch for improved http caching

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt3
- use ca-bundle.crt from ca-certificates package

* Mon Mar 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- remove patch against text relocations
- add patch to improve http caching

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Fri Dec 29 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt6
- add patch for system tray and xgl

* Mon Dec 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt5
- rebuilt with new libjasper

* Mon Nov 20 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt4
- resolve conflict with old djvu-common
- add patch from KDE svn for kcupsmanager timeout

* Thu Nov 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt3
- don't use sudo as default backend for kdesu
- mark desktop-files when user change mime type 
- fix load kde.so libraries

* Wed Oct 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt2
- fix load kde.so libraries
- make spec compat with 3.0

* Fri Oct 13 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Mon Sep 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt5
- update kdnssd_avahi from cvs
- fix path to temporary files in file open dialog

* Fri Sep 15 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt4
- rebuilt with disabled fast malloc

* Thu Sep 14 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt3
- add patch from RH to fix konqueror perfomance

* Thu Sep 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt2
- fix ALT Linux settings menu section

* Wed Aug 30 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version
- add patches from RH

* Thu Jun 08 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt2
- fix text relocations; thanks Alexey Morozov

* Fri Jun 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version
- add patch for MacCyrillic encoding; thanks Alexey Morozov

* Mon May 15 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt3
- rebuilt with new gcc
- search /etc/kde/xdg, /var/cache without exporting XDG_* variables

* Wed May 03 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt2
- fix path to X11/rgb.txt
- don't force moving password dialogs on top

* Wed Mar 29 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Mar 23 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt7
- built with INOTIFY

* Fri Mar 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt6
- add image/x-raw.desktop file

* Fri Feb 10 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt5
- update kdnssd-avahi to 0.1.2

* Wed Feb 08 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt4
- fix requires

* Tue Feb 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt3
- fix build with linux-libc-headers

* Tue Jan 31 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt2
- fix build options

* Tue Jan 31 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Tue Jan 31 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt8
- fix build requires

* Thu Jan 26 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt7
- built with linux-libc-headers
- build with libacl, liblua

* Mon Jan 23 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt6
- add patch for kjs

* Thu Jan 12 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt5
- fix default path to ~/Documents

* Fri Dec 30 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt4
- fix conflict with kdevelop

* Thu Dec 22 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt3
- add la-files

* Mon Dec 19 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt2
- workaround to compile with new binutils

* Mon Nov 28 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Mon Oct 31 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt3
- don't change group when create temp file

* Thu Aug 25 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt2
- add mimelnk/application/x-mplayer2.desktop
- built with openexr

* Wed Jun 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version
- disable fast malloc

* Fri May 20 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt5
- add fixed version of patch for kimgio

* Thu May 05 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt4
- change "do not stat on /mnt" patch to /media

* Tue May 03 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt3
- fix modules list in kcmshell

* Tue Apr 19 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt2
- add patch for kimgio

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Mon Feb 14 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt5
- add patch for dcopidlng

* Thu Jan 20 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt4
- don't use KDEVARTMP variable, use TMPDIR

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt3
- rebuild

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- add patch to fix html tokenizer on javascript
- rebuild with gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- add patch for ftp kioslave

* Mon Jan 03 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Mon Dec 20 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt5
- add fixes for java

* Tue Dec 14 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt4
- add patch to fix http://secunia.com/secunia_research/2004-10/advisory/

* Fri Dec 10 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt3
- add patch to remove password from URL

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt2
- fix workable with envirinment variables LC_*=C or LC_*=POSIX
- fix conflicts

* Wed Oct 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Mon Sep 27 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Mon Aug 09 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt6
- apply new version of patch for html frames
- fix -apidocs requires

* Fri Aug 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt5
- add patches for html frames and KCookieJar::KCookieJar
- add patch for subfs for get_mount_info()

* Mon Aug 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt4
- add patches for KStandardDirs::createSpecialResource and dcopserver

* Thu Jul 01 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt3
- add patch from RH for freedesktop/Gnome docking

* Tue Jun 08 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- fix kdesu execution

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- remove provides gcc_compiled

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt11
- add patch to compile with libidn

* Fri May 14 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt10
- add fix for KApplication::invokeMailer

* Fri May 14 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt9
- fix libssl file name to open

* Wed May 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt8
- reapply patch for cp866
- add patches from SuSE for subfs
- fix open terminal in kpty
- add patch for ktelnetservice

* Wed May 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt7
- fix requires

* Thu Apr 29 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt6
- rebuild

* Thu Apr 29 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt5
- remove warning message from kicontheme

* Wed Apr 21 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt4
- update patch for kdesu execution

* Fri Apr 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt3
- release 3.2.2

* Wed Apr 14 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt2
- patch from MDK for remove some warning messages

* Thu Apr 08 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- apidocs package

* Fri Apr 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt5
- update code from KDE_3_2_BRANCH
- fix kbuildsycoca crash when reading absent
  /etc/xdg/menus-alt/applications-kde.menu on first kde3.2 install

* Tue Mar 23 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt4
- update code from KDE_3_2_BRANCH
- optimize patch for finding service by desktop name
- add patch to encode filenames for ftp:/
- add more mimetypes for OO.o
- fix conflicts

* Sat Mar 20 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt3
- update code from KDE_3_2_BRANCH
- fix kdesu execution

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt2
- fix find service by desktop name when customized menu

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- temporary provide kdelibs-gcc_compiled
- update code from KDE_3_2_BRANCH

* Fri Feb 27 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Mon Dec 29 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt10
- disable fast malloc (in Qt was disabled)
- rebuild with gcc3.3

* Thu Dec 11 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt9
- remove kbuildsycoca_speedup.patch

* Thu Dec 11 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt8
- disable fast malloc
- remove patch fix-kdirwatch-with-read-only-file.patch

* Wed Dec 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt7
- dont'apply patch changed lt_dlopen to dlopen

* Mon Dec 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt6
- remove *.la from package

* Fri Nov 28 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt5
- rebuild

* Fri Nov 14 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt4
- rebuild

* Tue Nov 11 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt3
- rebuild

* Thu Oct 30 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- prefer Xlinsans font when not configured
- add patches from Sergey A. Sukiyazov <corwin at micom.don.ru>
- add some MDK && RH patches

* Wed Sep 17 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update from cvs

* Fri Aug 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt4
- update code from cvs
- improve patch 5010
- fix conflicts

* Wed Aug 20 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt3
- fix result of KLocale::isLanguageInstalled()
  when C or POSIX locale

* Mon Aug 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt2
- update code from cvs

* Fri Aug 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Mon Jul 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.3
- update code from cvs
- turn strict ansi off

* Fri Jul 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.2
- update code from cvs

* Wed Jul 16 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.1
- update code from cvs

* Mon Jul 14 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt8
- update code from cvs
- fix urls to floppy and cdrom on speedbar in filedialog

* Wed Jul 09 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt7
- update code from cvs
- don't apply *resize-icons* patch

* Fri Jul 04 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt6
- update code from cvs
- don't apply *fix-invokehelp* patch

* Tue Jul 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt5
- update code from cvs

* Wed Jun 25 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt4
- update code from cvs
- remove old patches

* Tue Jun 10 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt3
- fix doubleclick in kfiledialog

* Mon Jun 02 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt2
- update code from cvs KDE_3_1_BRANCH
- remove *click* patches

* Thu May 22 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update code from cvs KDE_3_1_BRANCH
- add xine-arts-plugin patches
- move kcmrandr utils to kdebase

* Tue Apr 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt6
- add kcmrandr utils

* Mon Apr 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt5
- update code from cvs KDE_3_1_BRANCH
- add MDK patches
- add xrandr patch

* Tue Apr 08 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt4
- update code from cvs KDE_3_1_BRANCH
- apply ghostscript security fix patch

* Tue Apr 01 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt3
- drop /usr/bin/xmlizer (may be found in .src.rpm)

* Fri Mar 28 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt2
- update code from cvs KDE_3_1_BRANCH
- fix conflicts

* Thu Mar 20 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update code from cvs KDE_3_1_BRANCH

* Thu Mar 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt0.1
- update code from cvs KDE_3_1_BRANCH
- add MDK patches

* Tue Feb 25 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt14
- update code from cvs KDE_3_1_BRANCH

* Mon Feb 17 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt13
- update code from cvs KDE_3_1_BRANCH

* Wed Feb 12 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt12
- update code from cvs KDE_3_1_BRANCH

* Thu Feb 06 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt11
- update code from cvs (khtml fixes)

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt10
- update code from cvs
- add RH patches

* Tue Jan 28 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt9
- update code from cvs 3_1_0_RELASE
- move slick icons to icons-slick package

* Mon Jan 20 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt8
- update from cvs 
- add MDK patches

* Wed Jan 08 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt7
- update from cvs 
- add MDK patches

* Thu Dec 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt6
- add patch to use ibm866 encoding

* Wed Dec 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt5
- fix ~/Desktop/Trash catalog name
  add creation ~/Documents catalog

* Fri Dec 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt4
- disable patch5000 add patch5006

* Wed Dec 18 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update code from cvs 3_1_0_RELASE

* Thu Dec 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update from 3_1_0_RELASE

* Wed Nov 27 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from 3_1_0_RELASE

* Thu Nov 21 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.22
- rebuild with new libxml2

* Thu Nov 21 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.21
- update from cvs 3_1_0_RELASE
- add patches from MDK

* Tue Nov 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Tue Oct 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Mon Oct 28 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.16
- remove symlink from /usr/share/icons/slick/

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.15
- fix requires

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.14
- fix requires

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.13
- fix menu item

* Tue Oct 22 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.12
- add patches from MDK
- build with libpcsclite

* Tue Oct 15 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.11
- update code from cvs
- increase %%release to upgrade Daedalus

* Wed Oct 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.10
- update code from cvs

* Thu Oct 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt9
- fix requires && provides

* Wed Oct 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt8
- fix conflicts

* Wed Oct 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt7
- fix requires, provides

* Fri Sep 27 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt6
- fix requires, provides
- update keramik from kdelibs-3.1-beta2
- build without fam

* Tue Sep 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt5
- rebuild with new XFree

* Mon Sep 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt4
- rebuild with objprelink
- update from cvs

* Thu Sep 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt3
- update from cvs
- update keramik from cvs
- rebuild with gcc 3.2
- add patches from cooker

* Fri Aug 23 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- update from cvs
- sync patches with cooker

* Fri Aug 16 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update from cvs
- sync patches with cooker
- add filter to poster program

* Wed Aug 07 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt5
- update code from cvs
- build with fam
- Requires libqt3 >= 3.0.5

* Wed Jul 31 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt4
- update code from cvs
- update keramik style code
- build with libqt-3.0.5
- sync with cooker (patches)

* Tue Jul 23 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt3
- sync with cooker (patches)
- update keramik style code
- build really i586

* Fri Jul 12 2002 ZerG <zerg@altlinux.ru> 3.0.2-alt2
- fix lnusertmp to $TMPDIR from $KDETMP
  if don't run KDE programs through startkde

* Wed Jul 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version
- add default encoding request via kioslave/http
  (workaround for Russian Apache)
- add kde.*sh to /etc/profile.d

* Fri Jun 14 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt5
- update from cvs
- drop Provides: kdelibs3

* Wed Jun 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt3
- update from cvs
- add support for GenericName to kdedesktop2mdkmenu.pl

* Thu May 23 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- fix icons search while add kdeprint applet to kicker or menu
- update kermamik from cvs

* Sat May 18 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- cvs snapshot
- update kermamik from cvs

* Wed May 15 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt6
- add Conflicts with old kde packages

* Wed May 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt5
- sync with cooker (update from cvs)
- sync with rawhide (patches)

* Tue Apr 30 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt4
- update from cvs

* Fri Apr 19 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0
- move to /usr
- add keramik theme

* Thu Apr 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- add exists_exe patch

* Wed Apr 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- build without debug with menu support

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- release

* Mon Apr 01 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.2.cvs20020401
- update from cvs

* Thu Mar 28 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1.rc3
- build for Sisyphus

* Fri Feb 08 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.3mdk
- Fix spec

* Tue Feb 05 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.2mdk
- update beta2

* Fri Jan 25 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Sat Jan 12 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.8mdk
- Fix build on 8.1

* Sun Dec 30 2001 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.7mdk
- Allow KDE 2 and KDE 3 to be installed in same time (lot of modifications,
  see CVS for details)
- Don't build static libraries
- Remove KDE 2's changelogs (KDE 2 and KDE 3 spec files have a separate life
  now)
- Fix previous changelog
- Remove 7.2 support (too old to be easily supported)

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.6mdk
- Rename to allow KDE 2 and KDE 3 to be installed in same time

* Sun Dec 09 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-6mdk
- Reapply some patch

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-5mdk
- kde 3.0 beta1

* Sat Dec 01 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-4mdk
- Clean spec file

* Wed Nov 28 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-3mdk
- Fix

* Wed Nov 21 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Some fix

* Mon Nov 19 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0
