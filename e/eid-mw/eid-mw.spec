%define mainline_ver 4.4.1

Name: eid-mw
Version: %mainline_ver
Release: alt1
Summary: low-level support for Belgian Electronic Identity Card
License: LGPLv3
Group: Office
Url: https://github.com/Fedict/eid-mw/

Packager: Pavel Nakonechnyi <zorg@altlinux.org>

Source: %name.tar

Patch0: alt-fix-pkg-check-var.patch
Patch1: alt-fix-underlinked.patch

BuildRequires(pre): rpm-build-firefox
BuildRequires: gcc-c++
BuildRequires: libpcsclite-devel, libgtk+3-devel, libssl-devel, libxml2-devel
BuildRequires: libcurl-devel, libproxy-devel, libp11-kit-devel
# for /usr/bin/c_rehash
BuildRequires: openssl
# for browser extension
BuildRequires: unzip

Requires: libbeidpkcs11-bin, firefox-beid

%description
This metapackage depends on a PKCS#11 module and a Firefox plugin for
the Belgian electronic identity card. You should install it if you wish
to use your electronic identity card to log on to online websites, or
to sign your mail and documents with it.

Consider installing eid-viewer to explore your eID card content.

%package -n libbeidpkcs11
Summary: PKCS#11 library for Belgian Electronic Identity Card
Group: System/Configuration/Hardware

%description -n libbeidpkcs11
This package contains the PKCS#11 module for the Belgian Electronic
Identity card, and a few helper libraries. It handles all low-level
access to the eID card.

%package -n libbeidpkcs11-devel
Summary: PKCS#11 library for Belgian Electronic Identity Card - development files
Group: Development/Other

%description -n libbeidpkcs11-devel
This package contains the static libraries and the development headers
to develop applications for the Belgian Electronic Identity Card.
Install it if you wish to develop applications that want to access the
Belgian Electronic Identity Card.

%package -n libbeidpkcs11-bin
Group: System/Configuration/Hardware
Summary: helper programs for libbeidpkcs11

%description -n libbeidpkcs11-bin
The libbeidpkcs11 library sometimes needs to pop up a few dialog boxes
to ask the user to perform some action (e.g., enter a pin code). This
package contains a few helper programs to allow the library to do so.

%package -n firefox-beid
Group: Networking/WWW
Summary: Belgian Electronic Identity Card - Mozilla plugin
BuildArch: noarch

%define cid belgiumeid@eid.belgium.be
%define ciddir %firefox_noarch_extensionsdir/%cid

%description -n firefox-beid
This package contains the mozilla plugin for the Belgian Electronic
Identity Card. Install it if you wish to log on to websites using your
electronic identity card from within iceweasel or any other gecko-based
browser.

%package -n eid-viewer
Group: System/Configuration/Hardware
Summary: Graphical interface to Belgian Electronic Identity Card
Requires: libbeidpkcs11-bin

%description -n eid-viewer
This package contains a graphical application to read data from the
Belgian electronic identity card.

%package -n libeidviewer
Group: System/Configuration/Hardware
Summary: eid-viewer library

%description -n libeidviewer
The eid-viewer library is a high-level, event-based library written
originally for use by the official eID-viewer program. It is a simple
to use library to access a Belgian eID, and can be used as an
alternative for the PKCS#11 API for projects that don't have high
performance requirements and don't need to do cryptographic operations.

%package -n libeidviewer-devel
Group: Development/Other
Summary: eid-viewer library - development files

%description -n libeidviewer-devel
The eid-viewer library is a high-level, event-based library written
originally for use by the official eID-viewer program. It is a simple
to use library to access a Belgian eID, and can be used as an
alternative for the PKCS#11 API for projects that don't have high
performance requirements and don't need to do cryptographic operations.

This package contains the static libraries and the development headers
for libeidviewer.

%prep
%setup -n %name
%patch0 -p1
%patch1 -p1

echo "#\!/bin/sh" > scripts/build-aux/genver.sh
echo "echo %mainline_ver" >> scripts/build-aux/genver.sh
echo "echo %mainline_ver" > .version

%build
%autoreconf
%configure
%make_build -j1

%install
%makeinstall_std

pushd %buildroot%firefox_noarch_extensionsdir
mkdir -p %cid
pushd %cid
unzip ../%cid.xpi
popd
rm -f *.xpi
popd

%find_lang eid-viewer
%find_lang dialogs-beid
cat eid-viewer.lang dialogs-beid.lang > all.lang

%postun -n firefox-beid
if [ "$1" = 0 ]; then
    [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files

%files -n libbeidpkcs11
%_libdir/libbeidpkcs11.so.*
%_libdir/pkcs11/*.so
%_datadir/p11-kit/modules/beid.module

%files -n libbeidpkcs11-devel
%_includedir/beid
%_libdir/pkgconfig/libbeidpkcs11.pc
%_libdir/libbeidpkcs11.so

%files -n libbeidpkcs11-bin
%_libexecdir/beid*
%_bindir/about-eid-mw

%files -n firefox-beid
%ciddir

%files -n eid-viewer -f all.lang
%_bindir/eid-viewer
%_desktopdir/eid-viewer.desktop
%_datadir/eid-mw
%_datadir/glib-2.0/schemas/eid-viewer.gschema.xml
%_iconsdir/hicolor/*/apps/eid-viewer.png

%files -n libeidviewer
%_libdir/libeidviewer.so.*

%files -n libeidviewer-devel
%_includedir/eid-viewer
%_includedir/eid-util
%_libdir/libeidviewer.so

%changelog
* Sat May 05 2018 Pavel Nakonechnyi <zorg@altlinux.org> 4.4.1-alt1
- updated to version 4.4.1

* Sun Apr 08 2018 Pavel Nakonechnyi <zorg@altlinux.org> 4.3.8-alt1
- updated to version 4.3.8

* Sun Oct 29 2017 Pavel Nakonechnyi <zorg@altlinux.org> 4.3.3-alt1
- updated to version 4.3.3

* Sat Sep 02 2017 Pavel Nakonechnyi <zorg@altlinux.org> 4.2.10-alt1
- updated to version 4.2.10

* Sun May 14 2017 Pavel Nakonechnyi <zorg@altlinux.org> 4.2.8-alt1
- updated to version 4.2.8
- add localized messages for dialogs
- fix sharedlibs policy draft violation

* Sun Apr 08 2017 Pavel Nakonechnyi <zorg@altlinux.org> 4.2.5-alt1
- updated to version 4.2.5

* Sun Mar 18 2017 Pavel Nakonechnyi <zorg@altlinux.org> 4.2.4-alt1
- updated to version 4.2.4

* Mon Jan 9 2017 Pavel Nakonechnyi <zorg@altlinux.org> 4.1.9.git.d14efb36-alt1
- initial build from https://github.com/Fedict/eid-mw.git
