Name: socat
Version: 1.7.2.1
Release: alt1

Summary: 'socket cat' - multipurpose relay for bidirectional data transfer
License: GPLv2
Group: Networking/Other
Url: http://www.dest-unreach.org/socat/
# %url/download/%name-%version.tar.bz2
Source: %name-%version.tar

BuildRequires: libe2fs-devel libreadline-devel libssl-devel libwrap-devel

%description
socat is a relay for bidirectional data transfer between two independent
data channels. Each of these data channels may be a file, pipe, device
(serial line etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw,
UDP, TCP), an SSL socket, proxy CONNECT connection, a file descriptor
(stdin etc.), the GNU line editor (readline), a program, or a
combination of two of these.  These modes include generation of
"listening" sockets, named pipes, and pseudo terminals.

%prep
%setup
iconv -f iso8859-1 -t utf8 < CHANGES > CHANGES.utf8
mv CHANGES.utf8 CHANGES
find -maxdepth 1 -type f -print0 |
	xargs -r0 grep -FZl linux/ext2_fs.h -- |
	xargs -r0 sed -i 's,linux/ext2_fs\.h,ext2fs/ext2_fs.h,g' --
find -maxdepth 1 -type f -print0 |
	xargs -r0 grep -FZl HAVE_LINUX_EXT2_FS_H -- |
	xargs -r0 sed -i 's,HAVE_LINUX_EXT2_FS_H,HAVE_EXT2FS_EXT2_FS_H,g' --

%build
%add_optflags -fno-strict-aliasing
%configure
for n in HAVE_DEV_PTMX HAVE_PROC_DIR_FD; do
	sed -i "/$n/ s/.*/#define $n 1/" config.h
done
%make_build

%install
%makeinstall_std
ln -s socat.1 %buildroot%_man1dir/filan.1
ln -s socat.1 %buildroot%_man1dir/procan.1

%files
%_bindir/filan
%_bindir/procan
%_bindir/socat
%_man1dir/*
%doc doc/*.html doc/*.css
%doc BUGREPORTS CHANGES EXAMPLES FAQ README SECURITY

%changelog
* Mon May 14 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.1-alt1
- Updated to 1.7.2.1.

* Sat May 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.0-alt1
- Updated to 1.7.2.0.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.1.3-alt2
- Rebuilt with libssl.so.10.

* Wed Aug 04 2010 Alexander Myltsev <avm@altlinux.ru> 1.7.1.3-alt1
- New version: CVE-2010-2799 fixed (closes #23839).

* Sun Apr 04 2010 Alexander Myltsev <avm@altlinux.ru> 1.7.1.2-alt3
- Still trying to appease the Almighty Changelog Checking Robot.

* Sat Apr 03 2010 Alexander Myltsev <avm@altlinux.ru> 1.7.1.2-alt2
- Useless changelog merge.

* Sat Apr 03 2010 Alexander Myltsev <avm@altlinux.ru> 1.7.1.2-alt1
- New version.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.0.0.patched-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Wed Jul 02 2008 Alex V. Myltsev <avm@altlinux.ru> 1.6.0.1-alt1
- New version: lots of bugs fixed.
- HTML documentation now packaged.

* Tue May 08 2007 Alex V. Myltsev <avm@altlinux.ru> 1.6.0.0.patched-alt1
- Applied servicenames patch (fixes name resolution problems).

* Sun Apr 08 2007 Alex V. Myltsev <avm@altlinux.ru> 1.6.0.0.maxfds-alt1
- Applied maxfds patch (fixes hangups with many open files).

* Tue Mar 27 2007 Alex V. Myltsev <avm@altlinux.ru> 1.6.0.0-alt1
- New version: broadcast/multicast, TUN/TAP, abstract UNIX domain sockets, bug fixes.

* Fri Jul 21 2006 Alex V. Myltsev <avm@altlinux.ru> 1.5.0.0-alt1
- New version: datagrams, IPv6, resolver options, many minor fixes.

* Mon Feb 06 2006 Alex V. Myltsev <avm@altlinux.ru> 1.4.3.1-alt1
- 1.4.3.1, bug fixes.

* Tue Sep 13 2005 Alex V. Myltsev <avm@altlinux.ru> 1.4.3.0-alt1
- Initial build for ALT Linux.

