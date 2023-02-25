%define _name qxmpp

# tst_qxmppiceconnection timed out in hasher
%def_disable check

Name: %_name-qt5
Version: 1.5.2
Release: alt1

Summary: Qt XMPP library
License: LGPL-2.1-or-later
Group: Development/KDE and QT
Url: https://github.com/%_name-project/%_name

Vcs: https://github.com/qxmpp-project/qxmpp.git
Source: %url/archive/v%version/%_name-%version.tar.gz

Conflicts: lib%_name

%define qt_ver 5.7

BuildRequires(pre): cmake
BuildRequires: gcc-c++ qt5-base-devel >= %qt_ver
BuildRequires: libspeex-devel libtheora-devel libvpx-devel libopus-devel doxygen
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
Requires: lib%name = %version-%release
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
%setup -n %_name-%version

%build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DWITH_SPEEX=TRUE \
	-DWITH_THEORA=TRUE \
	-DWITH_VPX=TRUE \
	-DWITH_OPUS=TRUE \
	-DBUILD_DOCUMENTATION=TRUE
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_defaultdocdir/%_name
install -m644 AUTHORS CHANGELOG.md README.md %buildroot%_defaultdocdir/%_name/

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%cmake_build -t test

%files -n lib%name
%_libdir/lib%_name.so.*

%files -n lib%name-devel
%_includedir/%_name/
%_libdir/lib%_name.so
%_pkgconfigdir/%_name.pc
%_libdir/cmake/%_name/

%files doc
%dir %_defaultdocdir/%_name
%_defaultdocdir/%_name/html/
%_defaultdocdir/%_name/AUTHORS
%_defaultdocdir/%_name/CHANGELOG.md
%_defaultdocdir/%_name/README.md

%changelog
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

