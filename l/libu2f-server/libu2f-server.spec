BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# spec file for package libu2f-server
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define soname  0
Name:           libu2f-server
Version:        1.1.0
Release:        alt2_3.2
Summary:        Yubico Universal 2nd Factor (U2F) Server C Library
License:        BSD-2-Clause
Group:          Security/Networking
URL:            https://developers.yubico.com/
Source0:        https://developers.yubico.com/libu2f-server/Releases/%{name}-%{version}.tar.xz
Source1:        https://developers.yubico.com/libu2f-server/Releases/%{name}-%{version}.tar.xz.sig
Patch0:         json-c-update.patch
BuildRequires:  gengetopt
BuildRequires:  help2man
BuildRequires:  libhidapi-devel
BuildRequires:  libtool
BuildRequires:  libzip-utils
BuildRequires:  libssl-devel
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(json-c) >= 0.10
BuildRequires:  pkgconfig(openssl)
Source44: import.info

%description
This is a C library that implements the server-side of the U2F protocol.
More precisely, it provides an API for generating the JSON blobs required
by U2F devices to perform the U2F Registration and U2F Authentication
operations, and functionality for verifying the cryptographic operations.

%package     -n %{name}%{soname}
Summary:        Library for Universal 2nd Factor (U2F)
Group:          Security/Networking

%description -n %{name}%{soname}
Libu2f-server provide a C library that implements
the server-side of the U2F protocol. There are APIs to talk to a U2F
device and perform the U2F Register and U2F Authenticate operations.

%package     -n %{name}-devel
Summary:        Development files for Universal 2nd Factor (U2F)
Group:          Development/C
Requires:       %{name}%{soname} = %{version}

%description -n %{name}-devel
This package contains the header file needed to develop applications that
use Universal 2nd Factor (U2F).

%package     -n u2f-server
Summary:        Tool to support Yubico's Universal 2nd Factor (U2F)
Group:          Security/Networking
Requires:       %{name}%{soname} = %{version}

%description -n u2f-server

Command line tool that implements the server-side of the Universal 2nd Factor (U2F) protocol

%prep
%setup -q
%patch0 -p1


%build
%configure --disable-static
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -type f -name "*.la" -delete -print
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin,/usr/games} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%files -n %{name}%{soname}
%{_libdir}/%{name}.so.%{soname}
%{_libdir}/%{name}.so.%{soname}.1.0

%files -n %{name}-devel
%dir %{_includedir}/u2f-server
%{_includedir}/u2f-server/u2f-server.h
%{_includedir}/u2f-server/u2f-server-version.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*

%files -n u2f-server
%doc AUTHORS NEWS ChangeLog README
%doc --no-dereference COPYING
%{_bindir}/u2f-server
%{_mandir}/man1/u2f-server.1*

%changelog
* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_3.2
- updated patch from suse

* Sun May 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt2_2.5
- fixed build with json-c-0.14.0

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2.5
- update by suseimport

* Wed Apr 10 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2.2
- new version

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Nov 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1-alt1
- Initial build.
