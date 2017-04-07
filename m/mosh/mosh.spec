Name: mosh
Version: 1.3.0
Release: alt1
Summary: Mobile shell that supports roaming and intelligent local echo

License: GPLv3+
Group: Networking/Remote access
Url: http://mosh.org/
Source: https://github.com/downloads/keithw/mosh/mosh-%version.tar

BuildRequires: gcc-c++ protobuf-compiler libprotobuf-devel libutempter-devel zlib-devel ncurses-devel perl-IO-Tty libssl-devel

Requires: openssh-clients

%description
Mosh is a remote terminal application that supports:
  - intermittent network connectivity,
  - roaming to different IP address without dropping the connection, and
  - intelligent local echo and line editing to reduce the effects
    of "network lag" on high-latency connections.

%prep
%setup

%build
%autoreconf
%configure --enable-compile-warnings=error
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
