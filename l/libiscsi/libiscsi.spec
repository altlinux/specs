Name: libiscsi
Version: 1.6.0
Release: alt1

Summary: iSCSI client library
License: LGPLv2.1+
Group: System/Libraries

Url: https://github.com/sahlberg/libiscsi
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libpopt-devel

%description
libiscsi is a library for attaching to iSCSI resources
across a network.

%prep
%setup

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc COPYING README TODO
%_libdir/libiscsi.so.*

%package utils
Summary: iSCSI Client Utilities
Group: System/Configuration/Networking
License: GPLv2+

%description utils
This package provides a set of assorted utilities to connect to iSCSI
servers without having to set up the Linux iSCSI initiator.

%files utils
%_bindir/ld_iscsi.so
%_bindir/iscsi-ls
%_bindir/iscsi-inq

%package devel
Summary: iSCSI client development libraries
Group: Development/Other
Requires: libiscsi = %version-%release

%description devel
The libiscsi-devel package includes the header files for libiscsi.

%files devel
%_includedir/iscsi/iscsi.h
%_includedir/iscsi/scsi-lowlevel.h
%_libdir/libiscsi.so

%changelog
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
