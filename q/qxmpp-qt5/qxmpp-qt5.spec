%define _name qxmpp

Name: %_name-qt5
Version: 0.9.3
Release: alt1

Summary: Qt XMPP library
License: LGPLv2+
Group: Development/KDE and QT
Url: https://github.com/%name-project/%name

#VCS: https://github.com/qxmpp-project/qxmpp.git
Source: %url/archive/%_name-%version.tar.gz

Conflicts: lib%_name

BuildRequires: gcc-c++ qt5-base-devel
BuildRequires: libspeex-devel libtheora-devel libvpx-devel doxygen

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
%qmake_qt5 PREFIX=%_prefix LIBDIR=%_lib \
	QXMPP_USE_SPEEX=1 \
	QXMPP_USE_THEORA=1 \
	QXMPP_USE_VPX=1 \
	QXMPP_USE_DOXYGEN=1
%make_build

%install
%make INSTALL_ROOT=%buildroot install

mkdir -p %buildroot%_defaultdocdir/%_name
install -m644 AUTHORS CHANGELOG README.md %buildroot%_defaultdocdir/%_name/

%files -n lib%name
%_libdir/lib%_name.so.*

%files -n lib%name-devel
%_includedir/%_name/
%_libdir/lib%_name.so
%_pkgconfigdir/%_name.pc

%files doc
%dir %_defaultdocdir/%_name
%_defaultdocdir/%_name/html/
%_defaultdocdir/%_name/AUTHORS
%_defaultdocdir/%_name/CHANGELOG
%_defaultdocdir/%_name/README.md

%changelog
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

