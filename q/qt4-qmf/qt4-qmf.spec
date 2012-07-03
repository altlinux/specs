%define qt4ver {%get_version libqt4-devel}
%define qt4_docdir %_docdir/qt-%qt4ver

%define sover 1
Name: qt4-qmf
Version: 1.0.0
Release: alt2

Group: System/Libraries
Summary: Qt Messaging Framework
License: LGPL-2.1 / GPL-3.0
Url: http://qt.gitorious.org/qt-labs/messagingframework

# http://qt.gitorious.org/qt-labs/messagingframework/archive-tarball/%version
Source: qt-labs-messagingframework-%version.tar
# SuSE
Patch1: add_headers.patch
# ALT
Patch100: qmf-alt-rpath.patch

# Automatically added by buildreq on Mon Feb 06 2012 (-bi)
# optimized out: elfutils fontconfig glibc-devel-static libqt4-clucene libqt4-core libqt4-devel libqt4-gui libqt4-help libqt4-network libqt4-sql libqt4-sql-sqlite libqt4-test libqt4-xml libstdc++-devel pkg-config python-base ruby zlib-devel
#BuildRequires: gcc-c++ libicu-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel python-module-distribute qt4-qmf-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): libqt4-devel
BuildRequires: gcc-c++ libicu-devel phonon-devel zlib-devel

%description
The Qt Messaging Framework, QMF, consists of a C++ library and daemon
server process that can be used to build email clients, and more
generally software that interacts with email and mail servers.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package devel
Summary: Development files for using QMF
License: LGPLv2
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description devel
This package contains the files necessary to develop QMF applications

%package doc
Summary: API documentation for QMF
License: LGPLv2
Group: Development/Documentation
BuildArch: noarch
Requires: %name-common = %version-%release
%description doc
This package provides API documentation for QMF.

%package -n libqmfclient%sover
Summary: %name library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libqmfclient%sover
%name library

%package -n libqmfmessageserver%sover
Summary: %name library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libqmfmessageserver%sover
%name library

%package -n libqmfutil%sover
Summary: %name library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libqmfutil%sover
%name library


%prep
%setup -n qt-labs-messagingframework-%version
%patch1 -p1
%patch100 -p1
# fix installation for lib64
find -name '*.pr[oi]' -exec sed -i 's|$$QMF_INSTALL_ROOT/lib/qmf|__X_ALTLINUX_QT4DIR__|g' {} ";"
find -name '*.pr[oi]' -exec sed -i 's|$$QMF_INSTALL_ROOT/lib|%_libdir|g' {} ";"
find -name '*.pr[oi]' -exec sed -i 's|__X_ALTLINUX_QT4DIR__|%_qt4dir|g' {} ";"
find -name '*.pr[oi]' -exec sed -i 's|$$QMF_INSTALL_ROOT/plugins|%_qt4dir/plugins|g' {} ";"
find -name '*.pr[oi]' -exec sed -i 's|$$QMF_INSTALL_ROOT/tests|%_qt4dir/tests|g' {} ";"

%build
export PATH=%_qt4dir/bin:$PATH
export QMF_INSTALL_ROOT=%prefix
qmake-qt4 -config release QMF_INSTALL_ROOT=$QMF_INSTALL_ROOT QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags"
%make_build
%make_build docs


%install
%make install INSTALL_ROOT=%buildroot

# install docs
install -p -m644 -D doc/html/qmf.qch %buildroot/%qt4_docdir/qch/qmf.qch
mkdir -p %buildroot/%qt4_docdir/html/qmf
cp -ar doc/html/* %buildroot/%qt4_docdir/html/qmf/


%files common
%files
%doc CHANGES LGPL_EXCEPTION.txt LICENSE.PREVIEW.COMMERCIAL README
%_bindir/messageserver
%_bindir/messagingaccounts
%_bindir/qtmail
%_bindir/serverobserver
%dir %_qt4dir/plugins/composers
%_qt4dir/plugins/composers/*.so
%dir %_qt4dir/plugins/contentmanagers
%_qt4dir/plugins/contentmanagers/*.so
%dir %_qt4dir/plugins/messageservices
%_qt4dir/plugins/messageservices/*.so
%dir %_qt4dir/plugins/viewers
%_qt4dir/plugins/viewers/*.so

%files devel
%_includedir/qmfclient/
%_includedir/qmfmessageserver/
%_libdir/libqmfclient.prl
%_libdir/libqmfclient.so
%_libdir/libqmfmessageserver.prl
%_libdir/libqmfmessageserver.so
%_libdir/libqmfutil.so
%_libdir/pkgconfig/qmfclient.pc
%_libdir/pkgconfig/qmfmessageserver.pc
%exclude %_qt4dir/tests/

%files doc
%qt4_docdir/qch/qmf.qch
%qt4_docdir/html/qmf/

%files -n libqmfclient%sover
%_libdir/libqmfclient.so.%sover
%_libdir/libqmfclient.so.%sover.*
%files -n libqmfmessageserver%sover
%_libdir/libqmfmessageserver.so.%sover
%_libdir/libqmfmessageserver.so.%sover.*
%files -n libqmfutil%sover
%_libdir/libqmfutil.so.%sover
%_libdir/libqmfutil.so.%sover.*

%changelog
* Tue Feb 07 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2
- revert to 2011W47

* Mon Feb 06 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- initial specfile
- use 2012W04 sorces
