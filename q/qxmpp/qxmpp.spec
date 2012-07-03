
Name: qxmpp
Version: 0.3.45.1
Release: alt1.git4c91ebf

Summary: Qt XMPP library
License: LGPLv2+
Group: Development/KDE and QT
Url: https://github.com/0xd34df00d/qxmpp-dev

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source: %name-%version.tar
# Patch: qxmpp.patch

BuildRequires: gcc-c++ libqt4-devel libspeex-devel doxygen

%description
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

%package devel
Summary: Qt XMPP library development files
Group: Development/KDE and QT
PreReq: lib%{name}1 = %version-%release

%description devel
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

%package -n lib%{name}1
Summary: Qt XMPP library
Group: Development/KDE and QT

%description -n lib%{name}1
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
%setup -n %name-%version

%build
qmake-qt4 PREFIX=%_prefix LIBDIR=%_libdir \
     "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"
%make_build
%make_build docs

%install
%make_install install INSTALL_ROOT=%buildroot

install -Dm644 AUTHORS CHANGELOG README %buildroot%_defaultdocdir/%name/
cp -aRf examples %buildroot%_defaultdocdir/%name/

%files devel
%_includedir/%name
%_libdir/libqxmpp.so
%dir %_defaultdocdir/%name
%doc %_defaultdocdir/%name/AUTHORS
%doc %_defaultdocdir/%name/CHANGELOG
%doc %_defaultdocdir/%name/README

%files doc
%doc %_defaultdocdir/%name/html
%doc %_defaultdocdir/%name/examples

%files -n lib%{name}1
%_libdir/libqxmpp.so.*

%changelog
* Wed Jul 27 2011 Ivan A. Melnikov <iv@altlinux.org> 0.3.45.1-alt1.git4c91ebf
- initial build for ALT Linux Sisyphus

