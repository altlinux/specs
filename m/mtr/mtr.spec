Name: mtr
Version: 0.82
Release: alt2

Summary: Matt's Traceroute - network diagnostic tool
License: GPL
Group: Monitoring
Url: http://www.bitwizard.nl/mtr/
Packager: Michael Shigorin <mike@altlinux.org>

Source: ftp://ftp.bitwizard.nl/mtr/mtr-%version.tar.gz
Source1: gtk1.m4
Source2: mtr.8ru
Source3: mtr.desktop
Source4: mtr.xpm
Source5: mtr.control
Patch1: mtr-0.80-alt-droppriv.patch
Patch2: mtr-0.80-alt-bound.patch
Patch3: mtr-0.72-rh-underflow.patch
Patch4: mtr-0.80-fc-crash-in-xml-mode.patch
Patch5: mtr-0.80-fc-now-waits-for-last-response.patch
Patch6: mtr-0.80-fc-xml-format-fixes.patch

Requires: shadow-utils
Requires: /var/resolv

BuildRequires: libgtk+2-devel libncurses-devel

Summary(ru_RU.KOI8-R): Matt's Traceroute - утилита для диагностики сети
Summary(uk_UA.KOI8-U): Matt's Traceroute - утил╕та для д╕агностики мереж╕

%define _sbindir %_bindir

%package -n xmtr
Summary: Ping/Traceroute network diagnostic tool - GTK Interface
Summary(ru_RU.KOI8-R): Ping/Traceroute - утилита для диагностики сети - GTK интерфейс
Summary(uk_UA.KOI8-U): Ping/Traceroute - утил╕та для д╕агностики мереж╕ - GTK ╕нтерфейс
Group: Monitoring
Provides: %name-gtk = %version-%release
Obsoletes: %name-gtk
Requires: %name = %version-%release

%description
mtr combines the functionaly of the traceroute and ping programs in
a single network diagnostic tool.  As mtr starts, it investigates the
network connection between the host mtr runs on and the destination.
After it determines the address of each network hop between the machines,
it sends a sequence ICMP ECHO requests to each one to determine the
quality of the link to each machine.  As it does this, it prints running
statistics about each machine.

%description -l ru_RU.KOI8-R
mtr - это traceroute и ping в одном флаконе.  При старте программа
исследует сетевое соединение между машиной, на которой она запущена,
и машиной, заданной пользователем.  После того, как она определит
адреса каждого хопа между этими двумя машинами, программа посылает
последовательность ICMP ECHO запросов на каждый из хопов для определения
качества связи с каждой из машин.  По мере того, как она это делает,
выводится текущая статистика по каждой машине.

%description -l uk_UA.KOI8-U
mtr - це traceroute та ping в одному флакон╕.  При запуску mtr
досл╕джу╓ мережеве з'╓днання м╕ж машиною, на як╕й в╕н запущений та
заданою користувачем.  П╕сля визначення адрес кожного хопу м╕ж цими
двома машинами, mtr посила╓ посл╕довн╕сть ICMP ECHO запит╕в на кожний
з хоп╕в для визначення якост╕ л╕нка до кожно╖ з машин.  В ход╕ цього
процесу mtr виводить поточну статистику по кожн╕й машин╕.

%description -n xmtr
mtr is a network diagnostic tool which combines Ping and Traceroute
into one program.

This is the GTK interface for mtr.

%description -l ru_RU.KOI8-R -n xmtr
mtr - утилита для диагностики сети, сочетающая ping и traceroute
в одном "флаконе".

Этот пакет содержит GTK-интерфейс к mtr.

%description -l uk_UA.KOI8-U -n xmtr
mtr - утил╕та для д╕агностики мереж╕, що по╓дну╓ ping та traceroute
в одному "флакон╕".

Це GTK-╕нтерфейс до mtr.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
install -pm644 %_sourcedir/gtk1.m4 acinclude.m4
touch ChangeLog

%build
%autoreconf
%define _configure_script ../configure

mkdir -p build-xmtr
	pushd build-xmtr
	%configure --with-gtk --enable-gtk2 --enable-ipv6
	%make_build
popd

mkdir -p build-mtr
	pushd build-mtr
	%configure --without-gtk --enable-ipv6
	%make_build
popd

%install
%makeinstall -C build-mtr

install -pD -m700 build-mtr/mtr %buildroot%_bindir/mtr
install -pD -m700 build-xmtr/mtr %buildroot%_bindir/xmtr
ln -s mtr %buildroot%_bindir/mtr6
ln -s xmtr %buildroot%_bindir/mtr-gtk

install -pD -m644 %_sourcedir/mtr.desktop %buildroot%_desktopdir/mtr.desktop
install -pD -m644 %_sourcedir/mtr.xpm %buildroot%_niconsdir/mtr.xpm
for n in mtr xmtr; do
	install -pD -m755 %_sourcedir/mtr.control "%buildroot%_controldir/$n"
	subst -p "s/@NAME@/$n/" "%buildroot%_controldir/$n"
done

%pre
/usr/sbin/groupadd -r -f netadmin
/usr/sbin/groupadd -r -f mtruser
/usr/sbin/useradd -r -g mtruser -d /dev/null -s /dev/null -n mtruser >/dev/null 2>&1 ||:
%pre_control mtr

%post
%post_control -s netadmin mtr

%pre -n xmtr
%pre_control xmtr

%post -n xmtr
%post_control -s netadmin xmtr

%files
%_bindir/mtr
%_bindir/mtr6
%_man8dir/*
%config %_controldir/mtr
#attr(0644,root,man) %_mandir/ru_RU.KOI8-R/man8/*
%doc AUTHORS FORMATS NEWS README SECURITY TODO

%files -n xmtr
%_bindir/xmtr
%_bindir/mtr-gtk
%_desktopdir/*.desktop
%_niconsdir/*.xpm
%config %_controldir/xmtr

# TODO:
# - update russian manpage and get it back into the package?
# - change "mtruser" group to e.g. "_mtr"?
# FIXME:
# - netadmin group would get non-predictable gid if not pre-existed

%changelog
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
