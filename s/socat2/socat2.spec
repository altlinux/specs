Name: socat2
Version: 2.0.0
Release: alt7

Summary: 'socket cat' - multipurpose relay for bidirectional data transfer
License: GPL-2.0-only
Group: Networking/Other
Url: http://www.dest-unreach.org/socat/

Source: socat.tar
Patch:	socat2-libssl1.1.patch
Patch1: socat2-make-j.patch

Conflicts: socat

BuildRequires: /proc libreadline-devel libssl-devel yodl

%description
socat is a relay for bidirectional data transfer between two independent
data channels. Each of these data channels may be a file, pipe, device
(serial line etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw,
UDP, TCP), an SSL socket, proxy CONNECT connection, a file descriptor
(stdin etc.), the GNU line editor (readline), a program, or a combination
of two of these.  These modes include generation of "listening" sockets,
named pipes, and pseudo terminals.

%prep
%setup -q -n socat
%patch -p1
%patch1 -p1

%build
autoconf
%configure

# We don't have /dev/ptmx in hasher.
echo '#define HAVE_DEV_PTMX 1' >> config.h

%make_build

%install
%makeinstall_std

%files
%_bindir/filan
%_bindir/procan
%_bindir/socat
%_man1dir/socat.*
%doc README* EXAMPLES FAQ SECURITY CHANGES doc/*.html doc/*.css

%changelog
* Wed Dec 18 2019 Fr. Br. George <george@altlinux.ru> 2.0.0-alt7
- Fix parallel build

* Wed Oct 10 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt6
- Rebuild without libwrap.

* Tue Oct 02 2018 Fr. Br. George <george@altlinux.ru> 2.0.0-alt5
- 2.0.0-b9
- Build with libopenssl-1.1

* Thu Jul 03 2014 Fr. Br. George <george@altlinux.ru> 2.0.0-alt4
- Restore libwrap dependency

* Tue Apr 22 2014 Fr. Br. George <george@altlinux.ru> 2.0.0-alt3
- 2.0.0-b7
- Remove libwrap dependency

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Thu Nov 11 2010 Kirill A. Shutemov <kas@altlinux.org> 2.0.0-alt2
- 2.0.0-b4

* Wed Nov 10 2010 Kirill A. Shutemov <kas@altlinux.org> 2.0.0-alt1
- Initial build of socat2

