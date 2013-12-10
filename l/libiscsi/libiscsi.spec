Name: libiscsi
Version: 1.10.0
Release: alt1

Summary: iSCSI client library
License: LGPLv2.1+
Group: System/Libraries

Url: https://github.com/sahlberg/libiscsi
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Michael Shigorin <mike@altlinux.org>
BuildRequires: bc
BuildRequires: libgcrypt-devel
BuildRequires: docbook-style-xsl xsltproc

%description
libiscsi is a library for attaching to iSCSI resources
across a network.

%package utils
Summary: iSCSI Client Utilities
Group: System/Configuration/Networking
License: GPLv2+

%description utils
This package provides a set of assorted utilities to connect to iSCSI
servers without having to set up the Linux iSCSI initiator.

%package devel
Summary: iSCSI client development libraries
Group: Development/Other
Requires: libiscsi = %version-%release

%description devel
The libiscsi-devel package includes the header files for libiscsi.

%prep
%setup
%patch -p1

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc COPYING README TODO
%_libdir/%name.so.*

%files utils
%_bindir/*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Dec 10 2013 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Wed May 22 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0
- add pkgconfig file to devel package

* Mon Sep 10 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Feb 28 2012 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- initial build for ALT Linux Sisyphus (based on upstream spec)

* Sun Dec 25 2011 : 1.1.0
- Fix TaskManagement AbortTask/AbortTaskSet to send to correct LUN

* Fri Oct 28 2011 Paolo Bonzini <pbonzini@redhat.com> - 1.0.0-2
- Fixed rpmlint problems

* Sat Dec 4 2010 Ronnie Sahlberg <ronniesahlberg@gmail.com> - 1.0.0-1
- Initial version
