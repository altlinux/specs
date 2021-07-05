%define oname usrsctp
Name: libusrsctp
Version: 0.9.5.0
Release: alt1

Summary: Portable SCTP userland stack

License: BSD
Group: System/Libraries
Url: https://github.com/sctplab/usrsctp

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %url/archive/%version/usrsctp-%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: meson ninja-build

%description
SCTP is a message oriented, reliable transport protocol with direct support
for multihoming that runs on top of IP or UDP, and supports both v4 and v6
versions.

Like TCP, SCTP provides reliable, connection oriented data delivery with
congestion control. Unlike TCP, SCTP also provides message boundary
preservation, ordered and unordered message delivery, multi-streaming and
multi-homing. Detection of data corruption, loss of data and duplication
of data is achieved by using checksums and sequence numbers. A selective
retransmission mechanism is applied to correct loss or corruption of data.

In this manual the socket API for the SCTP User-land implementation will be
described. It is based on RFC 6458. The main focus of this document is on
pointing out the differences to the SCTP Sockets API. For all aspects of the
sockets API that are not mentioned in this document, please refer to RFC
6458. Questions about SCTP itself can hopefully be answered by RFC 4960.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
%summary.

%prep
%setup

%build
%meson \
    -Dwerror=false \
    -Dsctp_debug=false \
    -Dsctp_inet=true \
    -Dsctp_inet6=true \
    -Dsctp_build_programs=false
%meson_build

%check
%meson_test

%install
%meson_install

%files
%doc README.md Manual.md
%doc LICENSE.md
%_libdir/%name.so.2*

%files devel
%_includedir/%oname.h
%_libdir/%name.so
%_pkgconfigdir/%oname.pc

%changelog
* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.5.0-alt1
- initial build for ALT Sisyphus

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1:0.9.5.0-1
- Updated to version 0.9.5.0.

* Mon Jan 11 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-0.2.20210110gitf1de842
- Updated to f1de842 snapshot (upstream release 0.9.4.0).

* Fri Oct 30 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-0.1.20201017gitf4925bd
- Initial SPEC release.
