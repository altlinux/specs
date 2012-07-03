Name: e2tools
Version: 0.0.16
Release: alt2

Summary: Manipulate files in unmounted ext2/ext3 filesystems
License: GPL+
Group: File tools
Url: http://home.earthlink.net/~k_sheff/sw/e2tools/
Packager: Kirill A. Shutemov <kas@altlinux.org>
# http://home.earthlink.net/~k_sheff/sw/e2tools/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: e2tools-test.sh
# Thank you very much for the man pages from Debian package.
Source2: e2cp.1
Source3: e2ln.1
Source4: e2ls.1
Source5: e2mkdir.1
Source6: e2mv.1
Source7: e2rm.1
Source8: e2tail.1
Source9: e2tools.7
Patch1: e2tools-fedora-fixes.patch
Patch2: e2tools-printf-lld-64bit.patch

BuildRequires: e2fsprogs libcom_err-devel libe2fs-devel

%description
A simple set of utilities to read, write, and manipulate files in an
ext2/ext3 filesystem directly using the ext2fs library. This works

  - without root access
  - without the filesystem being mounted
  - without kernel ext2/ext3 support

The utilities are: e2cp e2ln e2ls e2mkdir e2mv e2rm e2tail

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_man1dir %buildroot%_man7dir
install -pm644 \
    %SOURCE2 \
    %SOURCE3 \
    %SOURCE4 \
    %SOURCE5 \
    %SOURCE6 \
    %SOURCE7 \
    %SOURCE8 \
    %buildroot%_man1dir/
install -pm644 %SOURCE9 %buildroot%_man7dir/

%check
for e in e2ln e2ls e2mkdir e2mv e2rm e2tail; do
	ln -s e2cp $e
done
sh %SOURCE1

%files
%doc README COPYING ChangeLog TODO AUTHORS
%_bindir/*
%_mandir/man?/*

%changelog
* Tue Apr 26 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.16-alt2
- Fixed build, cleaned up specfile.
- Synced with Fedora e2tools-0.0.16-17.

* Sat Oct 13 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.0.16-alt1
- First build for ALT Linux

* Mon Jul 31 2006 Andreas Thienemann <andreas@bawue.net> - 0.0.16-5
- fix broken cast in rm.c:248 (exhibited on x86_64, but buggy everywhere)
  from Hans Ulrich Niedermann

* Mon Jul 17 2006 Andreas Thienemann <andreas@bawue.net> - 0.0.16-4
- Introduced %%check

* Mon Jul 17 2006 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-3
- initial package for fedora extras

