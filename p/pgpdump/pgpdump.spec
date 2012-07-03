Name: pgpdump
Version: 0.26
Release: alt1

Summary: PGP packet visualizer
License:  %bsd
Group: File tools 
Url: http://www.mew.org/~kazu/proj/pgpdump/

Packager: Yury Yurevich <anarresti@altlinux.org>
Source: %name-%version.tar

BuildPreReq: bzlib-devel zlib-devel
BuildRequires(pre): rpm-build-licenses

%description
pgpdump displays the sequence of OpenPGP or PGP version 2 packets from 
a file.

The output of this command is similar to the one of GnuPG's `list
packets' command, however, pgpdump produces a more detailed and easier
to understand.
 
%prep
%setup

%build
%configure
%make

%install
install -D pgpdump %buildroot%_bindir/pgpdump
install -D pgpdump.1 %buildroot%_man1dir/pgpdump.1

%files
%doc CHANGES COPYRIGHT README
%_bindir/pgpdump
%_man1dir/pgpdump.*

%changelog
* Sun May 24 2009 Yury Yurevich <anarresti@altlinux.org> 0.26-alt1
- initial build
