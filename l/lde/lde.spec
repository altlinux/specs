Name: lde
Version: 2.6.1
Release: alt0.1

Summary: Linux Disk Editor
Summary(ru_RU.KOI8-R): Редактор диска для Linux

License: LGPL
Group: System/Configuration/Hardware

Url: http://lde.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/lde/%name-%version.tar.bz2
Patch: %name-fixes.patch

# Automatically added by buildreq on Wed Feb 18 2004
BuildRequires: hostinfo libgpm-devel libncurses-devel libtinfo-devel

%description
Note: it is usually malfunction utility, see testdisk instead.

This is lde, the Linux disk editor, for Minix/Linux
partitions. It currently supports what were once the three most
popular file systems under Linux: ext2fs, minix, and xiafs (there is
also a "nofs" system under which lde will function as a binary
editor).  There is also minimal support for msdos/fat filesytems and
very minimal support for ISO9660 cdrom based filesystems.
lde allows you to view and edit disk blocks as hex and/or
ASCII, view/navigate directory entries, and view and edit formatted
inodes. It has text interface with ncurses.

%prep
%setup -q -n %name
%patch

%build
./autogen.sh
%configure
%__subst "s|\${INSTALL}|\${INSTALL} -D|" Makefile
#%__subst "s|getdate.o||g" src/swiped/Makefile

%make

%install
%makeinstall
mkdir %buildroot%_mandir/man8
mv -f %buildroot%_mandir/%{name}* %buildroot%_mandir/man8/
mkdir -p %buildroot%_menudir
cat >%buildroot%_menudir/%name <<EOF
?package(%name): command="%name" needs="text"\\
section="Configuration/Hardware" \\
title="LDE" \\
longtitle="Linux Disk Editor" \\
genericname="Editor" \\
EOF

%files
%doc INSTALL INSTALL.LDE README TODO doc/UNERASE
%_sbindir/*
#%_datadir/%name
%_mandir/man8/*
#%_docdir/%name
#%_menudir/%name

%changelog
* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt0.1
- new version (2.6.1)

* Tue Jun 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt2cvs20040218
- remove broken menu entry

* Wed Feb 18 2004 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1cvs20040218
- first build for Sisyphus

