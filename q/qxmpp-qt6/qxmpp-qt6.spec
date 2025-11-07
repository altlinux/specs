%define _name qxmpp
%define _Name QXmpp
%define suff Qt6
%define libname lib%_Name%suff

%def_enable omemo
%def_with gstreamer
%def_with qca
%def_enable docs
# tst_qxmppiceconnection timed out in hasher
%def_disable check

Name: %_name-qt6
Version: 1.11.3
Release: alt1

Summary: Qt XMPP library
License: LGPL-2.1-or-later
Group: Development/KDE and QT
Url: https://invent.kde.org/libraries/qxmpp

Vcs: https://invent.kde.org/libraries/qxmpp.git

Source: %url/-/archive/v%version/%_name-v%version.tar.gz

Conflicts: lib%_name

%define qt_ver 6.1
%define gst_ver 1.20

%{?_with_qca:Requires: qca-qt6}

BuildRequires(pre): cmake
BuildRequires: gcc-c++ qt6-base-devel >= %qt_ver
BuildRequires: libspeex-devel libtheora-devel libvpx-devel libopus-devel
%{?_enable_omemo:BuildRequires: pkgconfig(libomemo-c)}
%{?_with_qca:BuildRequires: qca-qt6-devel}
%{?_with_gstreamer:BuildRequires: gst-plugins1.0-devel} >= %gst_ver
%{?_enable_docs:BuildRequires:doxygen graphviz}
%{?_enable_check:BuildRequires: /proc ctest}

%description
Xmpp is a cross-platform C++ XMPP client and server library. It is written
in C++ and uses Qt framework.

QXmpp strives to be as easy to use as possible, the underlying TCP
socket, the core XMPP RFCs (RFC3920 and RFC3921) and XMPP extensions have
been nicely encapsulated into classes. QXmpp comes with full API
documentation, automatic tests and many examples.

%package -n lib%name-devel
Summary: Qt XMPP library development files
Group: Development/KDE and QT
Requires: lib%name = %EVR
Conflicts: lib%_name-devel

%description -n lib%name-devel
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and
C++. This package's the fork of QXmpp for Leechcraft Internet Client.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt
is the only third party library it is dependent on. Users need to a
have working knowledge of C++ and Qt basics (Signals and Slots and Qt
data types). The underlying TCP socket and the XMPP RFCs (RFC3920 and
RFC3921) have been encapsulated into classes and functions. Therefore
the user would not be bothered with these details. But it is always
recommended to the advanced users to read and enjoy the low level
details.

This package contains files needed for development.

%package doc
Summary: Qt XMPP library documentation
Group: Development/KDE and QT
Conflicts: lib%name < %version
Conflicts: lib%_name

%description doc
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and
C++. This package's the fork of QXmpp for Leechcraft Internet Client.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt
is the only third party library it is dependent on. Users need to a
have working knowledge of C++ and Qt basics (Signals and Slots and Qt
data types). The underlying TCP socket and the XMPP RFCs (RFC3920 and
RFC3921) have been encapsulated into classes and functions. Therefore
the user would not be bothered with these details. But it is always
recommended to the advanced users to read and enjoy the low level
details.

This package contains library documentation.

%package -n lib%name
Summary: Qt XMPP library
Group: Development/KDE and QT

%description -n lib%name
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and
C++. This package's the fork of QXmpp for Leechcraft Internet Client.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt
is the only third party library it is dependent on. Users need to a
have working knowledge of C++ and Qt basics (Signals and Slots and Qt
data types). The underlying TCP socket and the XMPP RFCs (RFC3920 and
RFC3921) have been encapsulated into classes and functions. Therefore
the user would not be bothered with these details. But it is always
recommended to the advanced users to read and enjoy the low level
details.

%prep
%setup -n %_name-v%version

%build
%cmake \
    -DCMAKE_BUILD_TYPE="Release" \
    %{?_enable_omemo:-DBUILD_OMEMO=TRUE} \
    %{?_with_gstreamer:-DWITH_GSTREAMER=TRUE} \
    %{?_with_qca:-DWITH_QCA=TRUE} \
    %{?_enable_docs:-DBUILD_DOCUMENTATION=TRUE} \
%nil
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_defaultdocdir/%_name
install -m644 AUTHORS CHANGELOG.md README.md %buildroot%_defaultdocdir/%_name/

%check
%cmake_build -t test

%files -n lib%name
%_libdir/%libname.so.*
%{?_enable_omemo:%_libdir/libQXmppOmemo%suff.so.*}

%files -n lib%name-devel
%_includedir/%_Name%suff/
%_libdir/%libname.so
%{?_enable_omemo:%_libdir/libQXmppOmemo%suff.so}
%_pkgconfigdir/%_Name%suff.pc
%_libdir/cmake/%_Name%suff/
%{?_enable_omemo:%_libdir/cmake/QXmppOmemo%suff/}

%files doc
%dir %_defaultdocdir/%_name
%{?_enable_docs:%_defaultdocdir/%_name/html/}
%_defaultdocdir/%_name/AUTHORS
%_defaultdocdir/%_name/CHANGELOG.md
%_defaultdocdir/%_name/README.md

%changelog
* Fri Nov 07 2025 Yuri N. Sedunov <aris@altlinux.org> 1.11.3-alt1
- 1.11.3

* Sun Jun 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

* Tue May 13 2025 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3 with Qt6

* Mon May 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

* Sat Mar 11 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sat Feb 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Sun Feb 05 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Tue May 11 2021 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1.1
- rebuild with new cmake macros

* Thu Mar 18 2021 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jan 11 2021 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Tue Jun 02 2020 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Wed Apr 01 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sun Feb 09 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0
- enabled check
- fixed License tag

* Wed Oct 30 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Tue Jan 15 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sat Dec 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Wed Sep 02 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sat Apr 18 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Mon Jan 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.6-alt1
- 0.7.6

* Wed Jul 27 2011 Ivan A. Melnikov <iv@altlinux.org> 0.3.45.1-alt1.git4c91ebf
- initial build for ALT Linux Sisyphus

