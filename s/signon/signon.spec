
%define _libexecdir %prefix/libexec
%define sover 1
%define libsignon_extension libsignon-extension%sover
%define libsignon_plugins_common libsignon-plugins-common%sover
%define libsignon_plugins libsignon-plugins%sover
%define libsignon_qt libsignon-qt6_%sover

Name: signon
Version: 8.61
Release: alt1

Group: System/Servers
Summary: Accounts framework for Linux and POSIX based platforms
Url: https://gitlab.com/accounts-sso/signond
License: LGPL-2.1-only

Requires: dbus

# https://drive.google.com/drive/#folders/0B8fX9XOwH_g4alFsYV8tZTI4VjQ
# https://groups.google.com/forum/#!topic/accounts-sso-announce/
Source: signon-%version.tar
# FC
Patch1: signon-8.57-no_static.patch
# SuSE
Patch5: 0001-Add-Qt6-support.patch
# ALT
Patch10: alt-fix-compile.patch

BuildRequires: qt6-base-devel qt6-tools doxygen graphviz libproxy-devel libdbus-devel

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package common
Summary: %name common package
Group: System/Configuration/Other
%description common
%name common package

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Headers, development libraries and documentation for %name.

%package -n %libsignon_extension
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libsignon_extension
%name library

%package -n %libsignon_plugins_common
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libsignon_plugins_common
%name library

%package -n %libsignon_plugins
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libsignon_plugins
%name library

%package -n %libsignon_qt
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libsignon_qt
%name library

%prep
%setup -n signon-%version
%patch1 -p1 -b .no_static
%patch5 -p1 -b .qt6
%patch10 -p1

sed -i '/^SUBDIRS/s|tests||'  signon.pro

find -type f \( -name \*.pc.in -o -name \*.h \) | \
while read f ; do
    sed -i 's|/usr/lib|%_libdir|' $f
done

find -type f \( -name \*.pro -o -name \*.pri \) | \
while read f ; do
    sed -i 's|-fno-rtti|-frtti|' $f
    sed -i 's|-fno-exceptions|-fexceptions|' $f
    sed -i 's|exceptions_off|exceptions|' $f
done

%build
export PATH=%_qt6_bindir:$PATH
%qmake_qt6 \
    signon.pro \
    CONFIG+="release nostrip enable-p2p" \
    PREFIX=%_prefix \
    QMF_INSTALL_ROOT=%_prefix \
    LIBDIR=%_libdir \
    LIBEXECDIR=%_libexecdir \
    #
%make_build

%install
export PATH=%_qt6_bindir:$PATH
%install_qt6

# create/own libdir/extensions
mkdir -p %buildroot/%_libdir/signon/extensions/

%files common
%doc README* TODO NOTES
%dir %_libdir/signon/
%dir %_libdir/signon/extensions/

%files
%config(noreplace) %_sysconfdir/signond.conf
%_bindir/signon*
%_libdir/signon/*
%_datadir/dbus-1/services/*.service

%files devel
%_includedir/signon*/
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/SignOnQt6/
#%_datadir/dbus-1/interfaces/*.xml
#
%_docdir/signon/
%_docdir/libsignon-qt/
%_docdir/signon-plugins/
%_docdir/signon-plugins-dev/

%files -n %libsignon_extension
%_libdir/libsignon-extension.so.%sover
%_libdir/libsignon-extension.so.*
%files -n %libsignon_plugins_common
%_libdir/libsignon-plugins-common.so.%sover
%_libdir/libsignon-plugins-common.so.*
%files -n %libsignon_plugins
%_libdir/libsignon-plugins.so.%sover
%_libdir/libsignon-plugins.so.*
%files -n %libsignon_qt
%_libdir/libsignon-qt?.so.%sover
%_libdir/libsignon-qt?.so.*

%changelog
* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 8.61-alt1
- new version
- build with Qt6

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 8.60-alt6
- relax requires

* Wed Mar 16 2022 Sergey V Turchin <zerg@altlinux.org> 8.60-alt4
- update compile flags

* Tue Sep 22 2020 Sergey V Turchin <zerg@altlinux.org> 8.60-alt3
- add upstream fix against deprecated QHash::unite

* Tue Sep 22 2020 Sergey V Turchin <zerg@altlinux.org> 8.60-alt2
- fix to build with debuginfo

* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 8.60-alt1
- new version

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 8.59-alt2
- dont use ubt macro

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 8.59-alt1
- new version

* Wed Sep 21 2016 Sergey V Turchin <zerg@altlinux.org> 8.58-alt1
- update to 8.58 20151106

* Fri Jan 22 2016 Sergey V Turchin <zerg@altlinux.org> 8.57-alt6
- enable dbus p2p

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 8.57-alt5
- redefine _libexecdir

* Mon Nov 02 2015 Sergey V Turchin <zerg@altlinux.org> 8.57-alt4
- fix .pc files

* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 8.57-alt3
- fix package shared directories

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 8.57-alt2
- own extensions directory

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 8.57-alt1
- initial build
