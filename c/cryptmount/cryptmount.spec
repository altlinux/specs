Name: cryptmount
Version: 4.3
Release: alt1
Group: File tools
Packager: Pavel Isopenko <pauli@altlinux.org>
License: GPL
Summary: Let ordinary users mount an encrypted file system
Summary(ru_RU.UTF-8): Монтирование зашифрованной файловой системы с правами обычного пользователя
Url: http://cryptmount.sourceforge.net
Source: %name-%version.tar

# Patch1: Makefile.in.patch

# Automatically added by buildreq on Tue Jan 03 2012
# optimized out: libgpg-error libgpg-error-devel pkg-config
BuildRequires: libdevmapper-devel libgcrypt-devel libuuid-devel

Requires(post): %post_service
Requires(preun): %preun_service

%description
cryptmount is a utility for the GNU/Linux operating system which allows
an ordinary user to mount an encrypted filing system without requiring
superuser privileges. Filesystems can reside on raw disk partitions or
ordinary files, with cryptmount automatically configuring
device-mapper and loopback devices before mounting.
%description -l ru_RU.UTF-8
cryptmount - утилита для операционной системы GNU/Linux, позволяющая
обычному пользователю монтировать зашифрованные файловые системы без
требования привилегий суперпользователя. Файловые системы могут находиться
на дисковых разделах или в обычных файлах, cruptmount автоматически
настраивает device-mapper и loopback устройства перед монтированием.

%prep
%setup
perl -pi.orig -e 's|^(\s*)chown(\s*root)|\1#chown\2|g;
s|%_sysconfdir/init.d|%_initdir|g;
' Makefile.am Makefile.in
# %patch1 -p1

%build
%configure --enable-delegation --enable-fsck

%make_build

%install
install -d -m0755 %buildroot%_initdir
install -d -m0755 %buildroot%_sbindir
install -d -m0755 %buildroot%_sysconfdir/default/

%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README* RELNOTES ToDo
%_mandir/man5/cmtab.5*
%_mandir/man8/cryptmount*.8*
%_mandir/*/man5/cmtab.5*
%_mandir/*/man8/cryptmount*.8*


%config(noreplace) %_sysconfdir/cryptmount/
%config %_initdir/cryptmount
%config %_initdir/cryptmount-early
%config %_sysconfdir/default/cryptmount
%_sbindir/cryptmount-setup
%_libdir/cryptmount/

%attr(4711, root, root) %_bindir/cryptmount

%changelog
* Tue Jun 05 2012 Pavel Isopenko <pauli@altlinux.org> 4.3-alt1
- update to 4.3

* Fri Jan 06 2012 Pavel Isopenko <pauli@altlinux.org> 4.2.1-alt1
- update to 4.2.1
- added missed luks/debug.c from cryptsetup


* Tue Feb 01 2011 Pavel Isopenko <pauli@altlinux.org> 4.1-alt2
- preun/postun fix

* Tue Nov 16 2010 Pavel Isopenko <pauli@altlinux.org> 4.1-alt1
- initial build for Sisyphus
