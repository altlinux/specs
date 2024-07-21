%define _unpackaged_files_terminate_build 1

Name: mosh
Version: 1.4.0
Release: alt1.1

Summary: Mobile shell that supports roaming and intelligent local echo
License: GPLv3+
Group: Networking/Remote access
Url: https://mosh.org/
VCS: https://github.com/mobile-shell/mosh

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: gcc-c++ 
BuildRequires: libprotobuf-devel
BuildRequires: libssl-devel
BuildRequires: libutempter-devel
BuildRequires: ncurses-devel
BuildRequires: perl-devel
BuildRequires: perl-diagnostics
BuildRequires: protobuf-compiler
BuildRequires: zlib-devel

Requires: openssh-clients

%description
Mosh  is  a remote  terminal  application  that supports  intermittent
connectivity, allows roaming, and  provides speculative local echo and
line editing of user keystrokes.

%prep
%setup
%patch -p1
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.20
%add_optflags -std=c++11
%endif

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md COPYING ChangeLog
%_bindir/mosh
%_bindir/mosh-client
%_bindir/mosh-server
%_mandir/man1/mosh.1.*
%_mandir/man1/mosh-client.1.*
%_mandir/man1/mosh-server.1.*

%changelog
* Sun Jul 21 2024 Ivan A. Melnikov <iv@altlinux.org> 1.4.0-alt1.1
- Add BR: perl-diagnostics (fixes FTBFS).

* Thu Oct 27 2022 Egor Ignatov <egori@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt2.3
- NMU: disable -Werror

* Mon Sep 30 2019 Michael Shigorin <mike@altlinux.org> 1.3.2-alt2.2
- E2K: explicit -std=c++11

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Sat Jun 23 2018 Terechkov Evgenii <evg@altlinux.org> 1.3.2-alt2
- mosh-1.3.2-61-g60859e9

* Sat Jun 23 2018 Terechkov Evgenii <evg@altlinux.org> 1.3.2-alt1
- 1.3.2
- Rebuild with libprotobuf15

* Fri Apr  7 2017 Terechkov Evgenii <evg@altlinux.org> 1.3.0-alt1
- 1.3.0
- Update Url:

* Sun Apr 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.4-alt1
- version 1.2.4

* Mon Feb 18 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.3-alt1
- version 1.2.3

* Mon May 28 2012 Sergey Alembekov <rt@altlinux.ru> 1.2.1-alt1
- version 1.2.1

* Tue May 15 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- Build for ALT

* Sat Apr 28 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.2-2
- Add -g and -O2 CFLAGS

* Fri Apr 27 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.2-1
- Update to mosh 1.2.

* Mon Mar 26 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.1.1-1
- Update to mosh 1.1.1.

* Wed Mar 21 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.1-1
- Initial packaging for mosh.
