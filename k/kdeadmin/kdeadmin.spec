%undefine __libtoolize
%define qtdir %_qt3dir
%define _optlevel s
%define _keep_libtool_files 1

%define unstable 0
%define lilo 0
%define kuser 0
%define kcmlinuz 0
%define kwuftpd 0
%define kpackage 0
%define kxconfig 0
%define knetworkconf 0

%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libdir/kde3

Name: kdeadmin
Version: 3.5.13
Release: alt2
Serial: 1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Administrative Tools
Url: http://www.kde.org/
License: GPL

Source: kdeadmin-%version.tar
Source10: kpackage.pam
Source11: kpackage.helper
Source12: kuser.pam
Source13: kuser.helper
Source14: kwuftpd.pam
Source15: kwuftpd.helper

# ALT patches
Patch1000: kdeadmin-3.1.1-ksysv-alt.patch

Requires: %name-kcron = %version-%release
Requires: %name-kdat = %version-%release
Requires: %name-kfile = %version-%release
Requires: %name-ksysv = %version-%release
Requires: %name-secpolicy = %version-%release
%if %lilo
Requires: %name-lilo = %version-%release
%endif
%if %kcmlinuz
Requires: %name-kcmlinuz = %version-%release
%endif
%if %kpackage
Requires: %name-kpackage = %version-%release
%endif
%if %kwuftpd
Requires: %name-kwuftpd = %version-%release
%endif
%if %kuser
Requires: %name-kuser = %version-%release
%endif
%if %kxconfig
Requires: %name-kxconfig = %version-%release
%endif
%if %knetworkconf
Requires: %name-knetworkconf = %version-%release
%endif


# Automatically added by buildreq on Mon Apr 08 2002
#BuildRequires: XFree86-devel XFree86-libs bzlib-devel freetype2 gcc-c++ kde-common kdebase kdelibs-devel kdemultimedia-aktion libarts-devel libbeecrypt-devel libdb1-devel libdb4-devel libjpeg-devel liblcms libmng libpam-devel libpng-devel libpopt-devel libqt3-devel librpm-devel libstdc++-devel lilo zlib-devel

BuildRequires: bzlib-devel
BuildRequires: gcc-c++ kde-common kdelibs-devel
BuildRequires: libbeecrypt-devel libart_lgpl-devel
BuildRequires: libjpeg-devel liblcms libmng libpam-devel
BuildRequires: libpng-devel libpopt-devel libqt3-devel libstdc++-devel zlib-devel
BuildRequires: libacl-devel libattr-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version
%if %lilo
BuildRequires: lilo
%endif
%if %kpackage
BuildRequires: librpm-devel
%endif

%description
Administrative tools for the K Desktop Environment.

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
Conflicts: kdeadmin <= 3.0.1
#
%description common
Common empty package for %name

%package kcron
Group: System/Configuration/Other
Summary: Crontab editor for KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kcron
KCron is a crontab editor for KDE - it helps you make your system run
commands periodically.

%package kdat
Group: Archiving/Backup
Summary: Tape backup tool for KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kdat
KDat is a KDE application for controlling tape backups.

%package kfile
Summary: KDE File dialog plugins for deb and rpm files
Group: File tools
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: %name-kfile-plugins = %serial:%version-%release
Obsoletes: %name-kfile-plugins
#
%description kfile
File dialog plugins for deb and rpm package files.

%package kpackage
Group: System/Configuration/Packaging
Summary: KDE package manager
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: consolehelper
#
%description kpackage
KPackage is a graphical frontend for RPM and other package managers.

%package ksysv
Group: System/Configuration/Boot and Init
Summary: System V startup editor
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksysv
KSysV is a graphical frontend for configuring your runlevels (system
startup/shutdown sequence).

%package kuser
Group: System/Configuration/Other
Summary: Frontend for configuring users and user groups
Requires: consolehelper
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kuser
KUser is a graphical frontend for managing the users and user groups on
your system.

%package kwuftpd
Group: System/Configuration/Networking
Summary: Graphical interface for configuring wu-ftpd
Requires: consolehelper
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kwuftpd
KWuftpd is a graphical frontend for configuring the wu-ftpd ftp server.

%package kcmlinuz
Group: System/Configuration/Other
Summary: Linux kernel configurator for KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kcmlinuz
kcmlinuz is a graphical frontend for creating configuration files for compiling
kernels.

%package lilo
Group: System/Configuration/Boot and Init
Summary: Graphical frontend for configuring the LILO bootloader
Requires: lilo
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description lilo
kdeadmin-lilo is a KDE frontend for configuring the LILO bootloader.

%package kxconfig
Summary: KDE display configuration tool
Group: System/Configuration/Hardware
Conflicts: %name < %version
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kxconfig
This program allows you to configure your X display.

%package secpolicy
Summary: KDE PAM security policy configuration tool
Group: System/Configuration/Other
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description secpolicy
This tool allows you to manipulate the PAM configuration files for each
"service" you have created to use PAM.

%prep
%setup -q -n %name-%version
cp -ar altlinux/admin ./
%patch1000 -p1

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
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lDCOP \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done

make -f admin/Makefile.common cvs ||:

%build
export QTDIR=%qtdir
export KDEDIR=%prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR%_lib:$KDEDIR%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%if !%kuser
DO_NOT_COMPILE="$DO_NOT_COMPILE kuser"
%endif
%if !%kwuftpd
DO_NOT_COMPILE="$DO_NOT_COMPILE kwuftpd"
%endif
%if !%kcmlinuz
DO_NOT_COMPILE="$DO_NOT_COMPILE kcmlinuz"
%endif
%if !%kpackage
DO_NOT_COMPILE="$DO_NOT_COMPILE kpackage"
%endif
%if !%kxconfig
DO_NOT_COMPILE="$DO_NOT_COMPILE kxconfig"
%endif
%if !%lilo
DO_NOT_COMPILE="$DO_NOT_COMPILE lilo-config"
%endif
%if !%knetworkconf
DO_NOT_COMPILE="$DO_NOT_COMPILE knetworkconf"
%endif

[ -n "$DO_NOT_COMPILE" ] && export DO_NOT_COMPILE

%K3configure \
%if %unstable
	    --enable-debug=full \
%else
	    --disable-debug \
%endif
            --enable-final \
            --with-rpm \
            --with-shadow \
            --without-quota \
	    --without-nis \
            --with-homeprefix=/home \
            --with-private-groups \
	    --with-first-uid=500 \
	    --with-first-gid=500 \
	    --with-mailbox-gid=8 \
%if !%kuser
	    --without-kuser \
%endif
%if !%kwuftpd
	    --without-kwuftpd \
%endif
%if !%kcmlinuz
	    --without-kcmlinuz \
%endif
%if !%kpackage
	    --without-kpackage \
%endif
%if !%kxconfig
	    --without-kxconfig \
%endif
%if !%lilo
	    --without-lilo-config \
%endif
%if !%knetworkconf
	    --without-knetworkconf \
%endif
            --with-pam=yes

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%if %unstable
%set_strip_method none
%endif

%K3install

mkdir -p %buildroot/%prefix/sbin \
         %buildroot/%_sysconfdir/pam.d \
         %buildroot/%_sysconfdir/security/console.apps

%if %kpackage
install -c -m 644 %SOURCE11 %buildroot/%_sysconfdir/security/console.apps/kpackage
install -c -m 644 %SOURCE10 %buildroot/%_sysconfdir/pam.d/kpackage
mv %buildroot/%_K3bindir/kpackage %buildroot/%_K3sbindir
(cd %buildroot/%_K3bindir && ln -fs consolehelper kpackage)
%endif

%if %kuser
install -c -m 644 %SOURCE13 %buildroot/%_sysconfdir/security/console.apps/kuser
install -c -m 644 %SOURCE12 %buildroot/%_sysconfdir/pam.d/kuser
mv %buildroot/%_K3bindir/kuser %buildroot/%_K3sbindir
(cd %buildroot/%_K3bindir && ln -fs consolehelper kuser)
%endif

%if %kwuftpd
install -c -m 644 %SOURCE15 %buildroot/%_sysconfdir/security/console.apps/kwuftpd
install -c -m 644 %SOURCE14 %buildroot/%_sysconfdir/pam.d/kwuftpd
mv %buildroot/%_K3bindir/kwuftpd %buildroot/%_K3sbindir
(cd %buildroot/%_K3bindir && ln -fs consolehelper kwuftpd)
%endif


%files
%files common
%files kcron
%_K3bindir/kcron
%_K3xdg_apps/kcron.desktop
%_K3apps/kcron/
%_kde3_iconsdir/*/*/apps/kcron*
%doc %_K3doc/en/kcron

%files kdat
%_K3bindir/kdat
%_K3apps/kdat
%_K3xdg_apps/kdat.desktop
%_kde3_iconsdir/*/*/*/kdat.png
%doc %_K3doc/en/kdat

%files kfile
%_K3lib/kfile_*.so*
%_K3srv/kfile_*.desktop

%if %kpackage
%files kpackage
%_K3bindir/kpackage
%_K3sbindir/kpackage
%_K3apps/kpackage
%_kde3_iconsdir/*/*/apps/kpackage.png
%_K3xdg_apps/kpackage.desktop
%_K3mimelnk/application/x-debian-package.desktop
%config(noreplace) %_sysconfdir/pam.d/kpackage
%config(noreplace) %_sysconfdir/security/console.apps/kpackage
%doc %_K3doc/en/kpackage
%endif

%files ksysv
%_K3bindir/ksysv
%_K3apps/ksysv
%_K3xdg_apps/ksysv.desktop
%_kde3_iconsdir/*/*/apps/ksysv*
%_K3mimelnk/application/x-ksysv.desktop
%_K3mimelnk/text/x-ksysv-log.desktop
%_K3iconsdir/crystalsvg/*/actions/toggle_log.*
%doc %_K3doc/en/ksysv

%if %kuser
%files kuser
#%config %_datadir/config/kuserrc
%_K3bindir/kuser
%_K3sbindir/kuser
%_K3apps/kuser
%_K3xdg_apps/kuser.desktop
%_kde3_iconsdir/*/*/apps/kuser*
%config(noreplace) %_sysconfdir/pam.d/kuser
%config(noreplace) %_sysconfdir/security/console.apps/kuser
%doc %_K3doc/en/kuser
%endif

%if %kwuftpd
%files kwuftpd
%_K3bindir/kwuftpd
%_K3sbindir/kwuftpd
%_K3xdg_apps/kwuftpd.desktop
%config(noreplace) %_sysconfdir/pam.d/kwuftpd
%config(noreplace) %_sysconfdir/security/console.apps/kwuftpd
%doc %_K3doc/en/kwuftpd
%endif

%if %kcmlinuz
%files kcmlinuz
%_K3apps/kcmlinuz
%_K3xdg_apps/linuz.desktop
%_K3lib/kcm_linuz*.so*
%endif

%if %lilo
%files lilo
%_K3xdg_apps/lilo.desktop
%_K3lib/kcm_lilo*.so*
%endif

%if %kxconfig
%files kxconfig
%_K3bindir/kxconfig
%_K3apps/kxconfig
%_kde3_iconsdir/*/*/*/kxconfig.png
%doc %_K3doc/en/kxconfig
#
%_K3xdg_apps/kxconfig.desktop
%endif

%files secpolicy
%_K3bindir/secpolicy

%changelog
* Fri Jun 15 2012 Roman Savochenko <rom_as@altlinux.ru> 1:3.5.13-alt2
- Automake version is fixed to 1.11.5 detect.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1:3.5.13-alt1
- TDE 3.5.13 release build

* Wed Feb 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.5.12-alt2.2
- Removed bad RPATH

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 1:3.5.12-alt2.1
- remove xorg-x11-devel requirement

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 1:3.5.12-alt2
- move to alternate place

* Mon Dec 27 2010 Sergey V Turchin <zerg@altlinux.org> 1:3.5.12-alt1
- new version

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.9-alt1
- new version

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.8-alt1
- new version

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.7-alt1
- new version

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.6-alt1
- new version

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.5-alt1
- new version

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.1-alt1
- new version

* Thu Dec 08 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.5.0-alt1
- new version

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.4.1-alt1
- new version

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.4.0-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 1:3.3.2-alt0.0.M24
- new version

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.1-alt1
- new version

* Mon Oct 04 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.3.0-alt1
- new version

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.3-alt1
- new version

* Thu Apr 15 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.2-alt1
- new version

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.1-alt1
- update code from KDE_3_2_BRANCH 

* Wed Mar 10 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Thu Feb 05 2004 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.4-alt3
- rebuild without /usr/lib/*.la files
- fix crash kuser when set password

* Tue Oct 14 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.4-alt2
- fix kuser to work with tcb

* Thu Sep 18 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.4-alt1
- update code from cvs

* Thu Aug 21 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.3-alt1
- update code from cvs

* Thu Jul 03 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.1.2-alt2
- update code from cvs

* Thu May 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 1:3.1.2-alt1
- update from cvs KDE_3_1_BRANCH

* Mon May 05 2003 Sergey V Turchin <zerg at altlinux dot ru> 1:3.1.1-alt2
- update from cvs KDE_3_1_BRANCH

* Tue Apr 01 2003 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.1-alt1
- update from cvs KDE_3_1_BRANCH

* Wed Feb 05 2003 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt2
- update from cvs
- build without kxconfig

* Thu Jan 09 2003 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt1
- update from cvs
- build without kpackage by security reason
  (it require siud program konsole_grantpty)

* Tue Nov 26 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.21
- update from cvs

* Sun Nov 10 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.20.rc2
- rc2

* Fri Nov 01 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.12
- fix provides

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.11
- update from cvs

* Tue Oct 15 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.1.0-alt0.10
- update from cvs
- increase %%release to upgrade Daedalus

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.0.3-alt2
- sync patches from cooker
- rebyuld with gcc 3.2

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.0.3-alt1
- update from cvs

* Mon Aug 05 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.0.2-alt1
- new version
- update from cvs

* Mon Jun 17 2002 Sergey V Turchin <zerg@altlinux.ru> 1:3.0.1-alt2
- add serial

* Mon Jun 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Thu Apr 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- disable kuser
- update from cvs
- move to /usr

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- build for ALT

* Thu Apr 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Fix update menu

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.2mdk
- RC3

* Fri Feb 08 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.2mdk
- fix spec file

* Sun Jan 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2
- Remove static package

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.1mdk
-

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-3mdk
- kde 3.0 beta1

* Thu Nov 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Improve spec file

* Fri Nov 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0 try

