%define _unpackaged_files_terminate_build 1

Name: tqftpserv
Version: 1.2
Release: alt1
Summary: Trivial File Transfer Protocol server over AF_QIPCRTR
License: BSD-3-Clause
Group: System/Kernel and hardware
Url: https://github.com/linux-msm/tqftpserv
VCS: https://github.com/linux-msm/tqftpserv.git
ExclusiveArch: aarch64

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: meson
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(qrtr)

%description
The tqftpserv software is an implementation of a TFTP (Trivial File Transfer
Protocol) server which runs on top of the AF_QIPCRTR (a.k.a QRTR) socket type.
The main purpose of tqftpserv is to serve files from the Linux file system to
other processors on the Qualcomm SoCs as requested.

The protocol implemented here is (loosely) based on RFC 1350 including some
extensions to the protocol. In basic terms, the protocol supports RRQ (Read
Request) and WRQ (Write Request) messages which read and write files.

%prep
%setup

%build
%meson -Dsystemd-unit-prefix=%_unitdir
%meson_build -v

%install
%meson_install

%files
%doc README.md
%_bindir/tqftpserv
%_unitdir/*.service

%changelog
* Sat Aug 15 2026 Vasiliy Doylov <neko@altlinux.org> 1.2-alt1
- Sanity checks and cleanups
- TFTP: ACK short DATA packets in WRQ window mode
- Translate: add persistent path for read-write and fix read-only search path
- Translate: verify asprintf return value
- Translate: support /readonly/vendor/firmware/ paths
- Fix: add path validation in tqftpserv.c

* Tue Apr 14 2026 Vasiliy Doylov <neko@altlinux.org> 1.1.1-alt1
- Initial package
