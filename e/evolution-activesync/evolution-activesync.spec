%define _libexecdir %_prefix/libexec

Name: evolution-activesync
Version: 0.92
Release: alt1
Summary: ActiveSync client support for Evolution
Group: Networking/Mail
License: LGPLv2.1
Url: http://git.infradead.org/activesyncd.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: libeasclient = %version-%release

BuildRequires: intltool gcc-c++
BuildRequires: libcheck-devel
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: evolution-data-server-devel evolution-devel
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: libwbxml2-devel > 0.11
BuildRequires: pkgconfig(libical)
BuildRequires: pkgconfig(gconf-2.0)

%description
Implementing the ActiveSync protocol, along with a
daemon which exposes all necessary functionality via DBus.

%package -n activesyncd
Summary: ActiveSync DBus daemon
License: LGPLv2.1 Apache
Group: Networking/Mail
Requires: libeasclient = %version-%release
Requires: libeasaccount = %version-%release

%description -n activesyncd
ActiveSync DBus daemon

%package -n libeasaccount
Summary: ActiveSync account management library
Group: System/Libraries

%description -n libeasaccount
ActiveSync account management library.

%package -n libeasaccount-devel
Summary: Development files for ActiveSync account management library
Group: Development/C
Requires: libeasaccount = %version-%release

%description -n libeasaccount-devel
Development files for ActiveSync account management library.

%package -n libeasclient
Summary: ActiveSync client library
Group: System/Libraries

%description -n libeasclient
ActiveSync client library for calendar/addressbook synchronisation and email access.

%package -n libeasclient-devel
Summary: Development files for ActiveSync client library
Group: Development/C
Requires: libeasclient = %version-%release

%description -n libeasclient-devel
Development files for ActiveSync client library for calendar/addressbook synchronisation and email access.

%prep
%setup
%patch -p1

%build
./autogen.sh
%configure			\
	--disable-silent-rules	\
	--disable-static

%make_build

%install
%make_install DESTDIR=%buildroot install
find %buildroot%_libdir -name '*.la' -exec rm {} \;
%find_lang activesyncd

%files
%doc COPYING README
%_libdir/evolution/*/plugins/*
%_libdir/evolution-data-server/camel-providers/*
%_libdir/libevoeas.so.*

%files -n activesyncd -f activesyncd.lang
%_libexecdir/activesyncd
%_datadir/dbus-1/services/*.service
%_libdir/libeas.so.*

%files -n libeasaccount
%_libdir/libeasaccount.so.*

%files -n libeasaccount-devel
%_libdir/libeasaccount.so
%_includedir/eas-daemon/eas-account
%_pkgconfigdir/libeasaccount.pc

%files -n libeasclient
%_libdir/libeasclient.so.*

%files -n libeasclient-devel
%_libdir/libeasclient.so
%_includedir/eas-daemon/eas-client
%_pkgconfigdir/libeasclient.pc

%changelog
* Fri Aug 31 2012 Alexey Shabalin <shaba@altlinux.ru> 0.92-alt1
- initial build for ALT Linux Sisyphus
