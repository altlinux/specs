Name: tpb
Version: 0.6.5
# Subversion revision 318
# see svn://svn.savannah.nongnu.org/tpb
Release: alt1.r318
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: IBM ThinkPad button support utility
Summary(ru_RU.KOI8-R): Поддержка дополнительных кнопок IBM ThinkPad
License: GPL
Group: System/Configuration/Other
Url: http://www.nongnu.org/tpb/

Source0: http://savannah.nongnu.org/download/tpb/%name-%version.tar
Source1: tpb-0.6.0-alt-tpb.xinit
Patch0: %name-%version-alt.patch

# Automatically added by buildreq on Thu Dec 11 2008
BuildRequires: imake libSM-devel libX11-devel libXext-devel libXinerama-devel libxosd-devel

%description
With TPB it is possible to bind a program to the ThinkPad, Mail, Home
and Search buttons. TPB can also run a callback program on each state
change with the changed state and the new state as options.  So it is
possible to trigger several actions on different events.  TPB has a
on-screen display (OSD) to show volume, mute, brightness and some
other information.  Furthermore TPB supports a software mixer, as the
R series ThinkPads have no hardware mixer to change the volume.

%description -l ru_RU.KOI8-R
TPB позволяет привязать к клавишам ThinkPad, Mail, Home и Search
соответствующие программы. TPB также может запускать обработчик
событий при каждом измененении состояния клавиши, передавая старое
и новое состояния в качестве аргументов. Это даёт возможность выполнять
несколько действий при разных событиях. TPB использует OSD (экран
в экране) для отображения установок громкости, яркости и другой
информации. Кроме того, TPB поддерживает программный микшер, поскольку
ноутбуки ThinkPad серии R не содержат встроенного аппаратного микшера,
громкость которого можно было бы регулировать.

%prep
%setup -q

%patch0 -p1

%build
aclocal -I m4
autoheader
automake --foreign --copy --add-missing --include-deps
autoconf
touch ChangeLog
chmod a+x configure

%configure
%make_build

%install
%makeinstall mkinstalldirs='./install-sh -d'
install -D %SOURCE1 %buildroot%_sysconfdir/X11/xinit.d/tbp
subst 's!__BINDIR__!%_bindir!' %buildroot%_sysconfdir/X11/xinit.d/tbp

%find_lang %name

%files -f %name.lang
%doc CREDITS README doc/callback_example.sh doc/nvram.txt
%config(noreplace) %_sysconfdir/tpbrc
%config %_sysconfdir/X11/xinit.d/*
%_bindir/*
%_man1dir/*

%changelog
* Fri Dec 12 2008 Grigory Batalov <bga@altlinux.ru> 0.6.5-alt1.r318
- Build requirements were updated.

* Thu Sep 11 2008 Grigory Batalov <bga@altlinux.ru> 0.6.5-alt0.r318
- SVN revision 318:
  + some new laptops supported.

* Thu Dec 29 2005 Grigory Batalov <bga@altlinux.ru> 0.6.4-alt1
- Update to 0.6.4.

* Wed Oct 13 2004 Grigory Batalov <bga@altlinux.ru> 0.6.3-alt1
- Update to 0.6.3.
- Recent ru.po.

* Sun Feb 29 2004 Grigory Batalov <bga@altlinux.ru> 0.6.1-alt1
- Update to 0.6.1.

* Fri Nov 28 2003 Grigory Batalov <bga@altlinux.ru> 0.6.0-alt1
- Built for ALTLinux.

* Mon Aug 11 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.6.0-0.fdr.1
- Update to 0.6.0.

* Tue May 27 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.5.1-0.fdr.4
- Make /dev/nvram readable again (#296).

* Sun May 18 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.5.1-0.fdr.3
- Use MAKEDEV for creating the nvram device node and own it.
- Mark xinit file as config to make rpmlint happy.
- %%{buildroot} -> $RPM_BUILD_ROOT.
- Make the build honor $RPM_OPT_FLAGS.

* Sat Apr 19 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.5.1-0.fdr.2
- Don't require tpctl (#177).

* Fri Apr 11 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.5.1-0.fdr.1
- Update to 0.5.1.

* Sun Apr  6 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.5.0-0.fdr.1
- Update to 0.5.0.
- Save .spec in UTF-8.

* Sun Mar 30 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.4.2-0.fdr.1
- Rebuild according to Fedora RC3 guidelines.

* Sat Feb  8 2003 Ville Skytta <ville.skytta at iki.fi> - 0.4.2-1.fedora.1
- First Fedora release.
