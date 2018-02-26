Name: socat2
Version: 2.0.0
Release: alt2

Summary: 'socket cat' - multipurpose relay for bidirectional data transfer
License: GPL
Group: Networking/Other
Url: http://www.dest-unreach.org/socat/
Packager: Kirill A. Shutemov <kas@altlinux.org>

Source: socat.tar

Conflicts: socat

BuildRequires: /proc libreadline-devel libssl-devel libwrap-devel yodl

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
* Thu Nov 11 2010 Kirill A. Shutemov <kas@altlinux.org> 2.0.0-alt2
- 2.0.0-b4

* Wed Nov 10 2010 Kirill A. Shutemov <kas@altlinux.org> 2.0.0-alt1
- Initial build of socat2

