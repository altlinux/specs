Name: mtr
Version: 0.95
Release: alt1

Summary: Matt's Traceroute - network diagnostic tool
License: GPLv2
Group: Monitoring

Url: http://www.bitwizard.nl/mtr/

Source: http://ftp.bitwizard.nl/mtr/mtr-%version.tar.gz
Source1: gtk1.m4
Source2: mtr.ru.UTF-8.8
Source3: mtr-packet.ru.UTF-8.8
Source4: mtr.desktop
Source5: mtr.xpm
Source6: mtr.control

Requires: mtr-packet = %EVR
Requires(pre): shadow-utils
Requires: /var/resolv

BuildRequires: libgtk+2-devel libncurses-devel

Summary(ru_RU.UTF-8): Matt's Traceroute - утилита для диагностики сети
Summary(uk_UA.UTF-8): Matt's Traceroute - утиліта для діагностики мережі

%package -n xmtr
Summary: Ping/Traceroute network diagnostic tool - GTK Interface
Summary(ru_RU.UTF-8): Ping/Traceroute - утилита для диагностики сети - GTK интерфейс
Summary(uk_UA.UTF-8): Ping/Traceroute - утиліта для діагностики мережі - GTK інтерфейс
Group: Monitoring
Provides: %name-gtk = %version-%release
Obsoletes: %name-gtk
Requires: mtr-packet = %EVR
Requires: %name = %version-%release

%package -n mtr-packet
Summary: Ping/Traceroute network diagnostic tool - packet sender
Summary(ru_RU.UTF-8): Ping/Traceroute - утилита для диагностики сети - отправитель пакетов
Group: Monitoring
# Starting with mtr 0.95-alt1, the `mtr' control facility has been moved
# from the `mtr' package to this package.
Conflicts: mtr < 0.95

%description
mtr combines the functionality of the traceroute and ping programs in
a single network diagnostic tool.  As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the machines,
it sends a sequence ICMP ECHO requests to each one to determine the
quality of the link to each machine.  As it does this, it prints running
statistics about each machine.

%description -l ru_RU.UTF-8
mtr - это traceroute и ping в одном флаконе.  При старте программа
исследует сетевое соединение между машиной, на которой она запущена,
и машиной, заданной пользователем.  После того, как она определит
адреса каждого хопа между этими двумя машинами, программа посылает
последовательность ICMP ECHO запросов на каждый из хопов для определения
качества связи с каждой из машин.  По мере того, как она это делает,
выводится текущая статистика по каждой машине.

%description -l uk_UA.UTF-8
mtr - це traceroute та ping в одному флаконі.  При запуску mtr
досліджує мережеве з'єднання між машиною, на якій він запущений та
заданою користувачем.  Після визначення адрес кожного хопу між цими
двома машинами, mtr посилає послідовність ICMP ECHO запитів на кожний
з хопів для визначення якості лінка до кожної з машин.  В ході цього
процесу mtr виводить поточну статистику по кожній машині.

%description -n xmtr
mtr is a network diagnostic tool which combines Ping and Traceroute
into one program.

This is the GTK interface for mtr.

%description -l ru_RU.UTF-8 -n xmtr
mtr - утилита для диагностики сети, сочетающая ping и traceroute
в одном "флаконе".

Этот пакет содержит GTK-интерфейс к mtr.

%description -l uk_UA.UTF-8 -n xmtr
mtr - утиліта для діагностики мережі, що поєднує ping та traceroute
в одному "флаконі".

Це GTK-інтерфейс до mtr.

%description -n mtr-packet
mtr is a network diagnostic tool which combines Ping and Traceroute
into one program.

This package contains the somewhat-privileged packet sender for mtr.

%prep
%setup
install -pm644 %_sourcedir/gtk1.m4 acinclude.m4
touch ChangeLog

%build
# setcap(8) does not work as builder, and the upstream
# make rule resorts to enabling set-uid in this case.
# Let's prevent that.
subst 's/|| chmod u+s/|| :/' Makefile.am
# It is not obvious how to pass the version of mtr to the build system. Let's
# patch Makefile.in directly.
subst 's/@PACKAGE_VERSION@/%version/' Makefile.in

%define _configure_script ../configure

mkdir -p build-xmtr
pushd build-xmtr
	%configure --sbindir=%_bindir --with-gtk --enable-gtk2 --enable-ipv6
	%make_build
popd

mkdir -p build-mtr
pushd build-mtr
	%configure --sbindir=%_bindir --without-gtk --enable-ipv6
	%make_build
popd

%install
%makeinstall_std -C build-mtr

install -pD -m755 build-mtr/mtr %buildroot%_bindir/mtr
install -pD -m755 build-xmtr/mtr %buildroot%_bindir/xmtr
ln -s mtr %buildroot%_bindir/mtr6
ln -s xmtr %buildroot%_bindir/mtr-gtk

# The rights on this directory are to be manipulated by a control(8) facility.
mkdir -p %buildroot%_libexecdir/mtr
mv %buildroot%_bindir/mtr-packet %buildroot%_libexecdir/mtr/
ln -sr %buildroot%_libexecdir/mtr/mtr-packet %buildroot%_bindir/mtr-packet

install -pD -m644 %_sourcedir/mtr.desktop %buildroot%_desktopdir/mtr.desktop
install -pD -m644 %_sourcedir/mtr.xpm %buildroot%_niconsdir/mtr.xpm
install -pD -m755 %_sourcedir/mtr.control "%buildroot%_controldir/mtr"
subst -p "s)@NAME@)mtr-packet); s)@LIBEXECDIR@)%_libexecdir)" "%buildroot%_controldir/mtr"

%pre -n mtr-packet
/usr/sbin/groupadd -r -f netadmin
%pre_control mtr
if [ ! -r /var/run/control/mtr-packet.preserved ]; then
# We're looking at pre-installed, pre-expanded content; hence absolute paths
# and values.
case "$(grep '^BINARY=' /etc/control.d/facilities/mtr)" in
*="'"/usr/bin/mtr"'")
# Compatibility measure: preserve admin setting from mtr < 0.95.
mkdir -p /var/run/control
%_sbindir/control mtr > /var/run/control/mtr-packet.preserved
;;
esac
fi

%post -n mtr-packet
%post_control -s netadmin mtr
if [ -r /var/run/control/mtr-packet.preserved ]; then
# Compatibility measure: reapply preserved setting from mtr < 0.95.
%_sbindir/control mtr $(cat /var/run/control/mtr-packet.preserved)
rm -f /var/run/control/mtr-packet.preserved
fi

%files
%_bindir/mtr
%_bindir/mtr6
%_man8dir/mtr.8*
%_datadir/bash-completion/completions/mtr
%doc AUTHORS NEWS SECURITY TODO

%files -n xmtr
%_bindir/xmtr
%_bindir/mtr-gtk
%_desktopdir/*.desktop
%_niconsdir/*.xpm
%doc AUTHORS NEWS SECURITY TODO

%files -n mtr-packet
%_libexecdir/mtr
%_bindir/mtr-packet
%_man8dir/mtr-packet.8*
%config %_controldir/mtr

# TODO:
# - update russian manpage and get it back into the package?
# FIXME:
# - netadmin group would get non-predictable gid if not pre-existed

%changelog
* Fri Oct 13 2023 Arseny Maslennikov <arseny@altlinux.org> 0.95-alt1
- 0.82 -> 0.95. (Closes: 47555)
- Nowadays the upstream ships a separate program, mtr-packet(8), to call
  privileged kernel APIs and to relieve the user interface programs from that
  burden. The mtr control facility is now repurposed to control access to this
  program; mtr and mtr-gtk will fail gracefully if not allowed to run it.

* Fri Mar 19 2021 Slava Aseev <ptrnine@altlinux.org> 0.82-alt4
- fixed build with gcc-10

* Mon Sep 10 2018 Michael Shigorin <mike@altlinux.org> 0.82-alt3
- recoded spec into UTF-8
- minor spec cleanup

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 0.82-alt2
- worked around file shortage for autoreconf

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 0.82-alt1
- 0.82

* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1.qa1
- NMU: converted menu to desktop file

* Sat Feb 26 2011 Afanasov Dmitry <ender@altlinux.org> 0.80-alt1
- New version (0.80)
- Updated alt patches
- Add xml fixes

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.72-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for xmtr
  * pixmap-in-deprecated-location for mtr
  * postclean-05-filetriggers for spec file

* Sat Mar 24 2007 Dmitry V. Levin <ldv@altlinux.org> 0.72-alt3
- Cleaned up specfile.
- Cleaned up droppriv patch.
- Imported mtr-0.72-rh-underflow patch.
- Fixed a few potential buffer overflows.

* Mon Dec 11 2006 Michael Shigorin <mike@altlinux.org> 0.72-alt2
- gratefully accepted update by Damir Shayhutdinov (damir@),
  who was asked to look at the patches
- spec cleanup

* Mon Dec 11 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.72-alt1
- NMU
- New version (0.72)
- Removed obsolete alt-autotools patch.
- Updated alt-droppriv.patch

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 0.65-alt1
- Updated to 0.65, updated patches.
- Changed first install control mode to "netadmin".
- Build xmtr with GTK2 interface.
- Added help to control.

* Fri Feb 27 2004 Dmitry V. Levin <ldv@altlinux.org> 0.54-alt2
- Fixed build with fresh autotools.
- Use control macros.

* Fri Aug 29 2003 Michael Shigorin <mike@altlinux.ru> 0.54-alt1
- 0.54

* Sun Dec 22 2002 Dmitry V. Levin <ldv@altlinux.org> 0.52-alt2
- Reimplemented droppriv like in ping/traceroute.
- Fixed package dependencies.
- Fixed control support.
- Fixed menu support.
- Fixed build.
- Renamed mtr-gtk to xmtr.
- Relocated programs to %_bindir/.

* Tue Nov 26 2002 Michael Shigorin <mike@altlinux.ru> 0.52-alt1
- 0.52
- added control support
- spec cleanup

* Mon Oct 28 2002 Michael Shigorin <mike@altlinux.ru> 0.51-alt1.9
- rebuilt with gcc 3.2

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.51-alt1.1
- fixed suid/sgid file permissions

* Thu Jul 11 2002 Michael Shigorin <mike@altlinux.ru> 0.51-alt1
- built for ALT Linux 
- spec adapted from KSI and PLD and heavily cleaned up
