%define sover 17

Name: libgloox
Version: 1.0.23
Release: alt1

Summary: A full-featured Jabber/XMPP client library
License: GPLv3
Group: System/Libraries

URL: http://camaya.net/gloox
Source: http://camaya.net/download/gloox-%version.tar.bz2

# Automatically added by buildreq on Sun Nov 05 2017
BuildRequires: gcc-c++ libssl-devel zlib-devel

%package -n libgloox%sover
Summary: A full-featured Jabber/XMPP client library
Group: System/Libraries

%package devel
Summary: A full-featured Jabber/XMPP client library
Group: Development/C++
Requires: libgloox%sover = %version-%release

%description
gloox is a rock-solid, full-featured Jabber/XMPP client library, written in
C++. It makes writing spec-compliant clients easy and allows for hassle-free
integration of Jabber/XMPP functionality into existing applications.

%description -n libgloox%sover
gloox is a rock-solid, full-featured Jabber/XMPP client library, written in
C++. It makes writing spec-compliant clients easy and allows for hassle-free
integration of Jabber/XMPP functionality into existing applications.

%description devel
gloox is a rock-solid, full-featured Jabber/XMPP client library, written in
C++. It makes writing spec-compliant clients easy and allows for hassle-free
integration of Jabber/XMPP functionality into existing applications.

%prep
%setup -n gloox-%version

mv AUTHORS AUTHORS.old
iconv -f iso8859-1 -t UTF-8 AUTHORS.old >AUTHORS

%build
export PTHREAD_LIBS="-lpthread"
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n libgloox%sover
%doc AUTHORS ChangeLog README
%_libdir/libgloox.so.%sover
%_libdir/libgloox.so.%sover.*

%files devel
%_bindir/gloox-config
%_pkgconfigdir/gloox.pc
%dir %_includedir/gloox
%_includedir/gloox/*
%_libdir/libgloox.so

%changelog
* Tue Dec 17 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.23-alt1
- Build new version.

* Thu Dec 06 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.20-alt2
- NMU: Rebuild without libidn.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.20-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sun Nov 05 2017 Alexey Tourbin <at@altlinux.ru> 1.0.20-alt1
- 1.0 -> 1.0.20
- License changed from GPLv2 to GPLv3 in 1.0.3.

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt1.2.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 1.0-alt1.2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt for soname set-versions

* Wed Jun 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- initial build for ALT Linux from FC3 package
