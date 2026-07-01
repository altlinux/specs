Name: cryptmount
Version: 6.4.0
Release: alt1
Group: File tools
License: GPL-2.0
Summary: Let ordinary users mount an encrypted file system
Summary(ru_RU.UTF-8): Монтирование зашифрованной файловой системы с правами обычного пользователя
Url: http://cryptmount.sourceforge.net
Source: %name-%version.tar
Patch1: cryptmount-6.4.0-remove-chown.patch

BuildRequires: libdevmapper-devel libgcrypt-devel libuuid-devel
BuildRequires: doxygen libudev-devel libcryptsetup-devel

Requires(post): %post_service
Requires(preun): %preun_service

%filter_from_requires /^\/etc\/default\/cryptmount/d

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
%autopatch -p2

%build
%__aclocal
%autoreconf
%__autoconf
%configure --enable-delegation --enable-fsck
%make_build

%install
mkdir -p %buildroot{%_initdir,%_unitdir,%_modulesloaddir}

%makeinstall_std
install -m0644 sysinit/cryptmount.service %buildroot%_unitdir/
mv %buildroot%_sysconfdir/modules-load.d/cryptmount.conf %buildroot%_modulesloaddir/
rm -r -- %buildroot%_mandir/fr

%find_lang --with-man %name
%find_lang --with-man --append --output=%name.lang cmtab

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING README* RELNOTES
%_man5dir/cmtab.5*
%_man8dir/cryptmount*.8*
%_docdir/%name

%config(noreplace) %_sysconfdir/cryptmount/
%_modulesloaddir/cryptmount.conf
%_initdir/cryptmount
%_unitdir/cryptmount.service
%_sbindir/cryptmount-setup

%attr(4711, root, root) %_bindir/cryptmount

%changelog
* Tue Jun 30 2026 Andrew A. Vasilyev <andy@altlinux.org> 6.4.0-alt1
- NMU: new version - fix FTBFS with gettext 1.0

* Wed Apr 26 2023 Pavel Isopenko <pauli@altlinux.org> 6.2.0-alt1
- new version 6.2.0
- init script (ALT #37128)

* Tue Aug 20 2019 Alexey Shabalin <shaba@altlinux.org> 5.3.1-alt2
- fixed BR:
- move config from /etc/modules-load.d to /lib/modules-load.d
- add systemd unit
- drop /etc/default/cryptmount dir

* Sun Mar 03 2019 Pavel Isopenko <pauli@altlinux.org> 5.3.1-alt1
- new version 5.3.1

* Fri May 11 2018 Pavel Isopenko <pauli@altlinux.org> 5.3-alt1
- version 5.3

* Wed Mar 23 2016 Pavel Isopenko <pauli@altlinux.org> 5.2-alt1
- new version 5.2
- add BuildRequires: doxygen libudev-devel libcryptsetup


* Wed Jan 07 2015 Pavel Isopenko <pauli@altlinux.org> 5.0-alt1
- new version cryptmount 5.0

* Tue Jun 05 2012 Pavel Isopenko <pauli@altlinux.org> 4.3-alt1
- update to 4.3

* Fri Jan 06 2012 Pavel Isopenko <pauli@altlinux.org> 4.2.1-alt1
- update to 4.2.1
- added missed luks/debug.c from cryptsetup


* Tue Feb 01 2011 Pavel Isopenko <pauli@altlinux.org> 4.1-alt2
- preun/postun fix

* Tue Nov 16 2010 Pavel Isopenko <pauli@altlinux.org> 4.1-alt1
- initial build for Sisyphus
