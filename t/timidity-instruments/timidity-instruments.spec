Name: timidity-instruments
Version: 1.0
Release: alt1

Serial: 1

Summary: Instruments for the timidity midi->wave converter/player
License: Free
Group: Sound

Source0: midia-instruments.tar.bz2
Source1: midia.cfg.bz2
Source2: gravis.cfg.bz2

BuildArch: noarch

%description
This package contains a set of instruments for the timidity midi->wave
converter/player.

%install
mkdir -p %buildroot%_datadir/timidity
cd %buildroot%_datadir/timidity
bzip2 -cd $RPM_SOURCE_DIR/midia-instruments.tar.bz2 | tar xf -
bzip2 -cd $RPM_SOURCE_DIR/midia.cfg.bz2 >midia.cfg
bzip2 -cd $RPM_SOURCE_DIR/gravis.cfg.bz2 >gravis.cfg

%define conf_string source midia.cfg

%post
if [ -f %_sysconfdir/timidity.cfg ]; then
        grep -qs '^%conf_string$' %_sysconfdir/timidity.cfg ||
        echo '%conf_string' >> %_sysconfdir/timidity.cfg
fi

%postun
[ $1 = 0 ] || exit 0
if [ -f %_sysconfdir/timidity.cfg ]; then
	sed '/%conf_string/d' < %_sysconfdir/timidity.cfg > %_sysconfdir/timidity.cfg.new
	mv %_sysconfdir/timidity.cfg.new %_sysconfdir/timidity.cfg
fi ||:

%triggerin -- TiMidity++
if [ -f %_sysconfdir/timidity.cfg ]; then
        grep -qs '^%conf_string$' %_sysconfdir/timidity.cfg ||
        echo '%conf_string' >> %_sysconfdir/timidity.cfg
fi

%triggerpostun -- %name < 1.0-ipl13mdk
[ $2 != 0 ] || exit 0
if [ -f %_sysconfdir/timidity.cfg ]; then
        grep -qs '^%conf_string$' %_sysconfdir/timidity.cfg ||
        echo '%conf_string' >> %_sysconfdir/timidity.cfg
fi

%files
%_datadir/timidity/instruments
%_datadir/timidity/midia.cfg
%_datadir/timidity/gravis.cfg

%changelog
* Wed Dec 20 2006 Michael Shigorin <mike@altlinux.org> 1:1.0-alt1
- spec cleanup (see also #4151)
- preferred Serial: to ancient Release:

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-ipl14mdk
- rebuild

* Fri May 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0-ipl13mdk
- Improvements in post* and trigger* sections.

* Sun May 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0-ipl12mdk
- Trigger to compensate lost dependence on TiMidity++.

* Wed Apr 10 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-ipl11mdk
- removed dependence on TimMidity (circle dependencies)
- we need it to correct update from Spring

* Tue Dec 25 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.0-ipl10mdk
- Adopted for Sisyphus
- timidity.cfg in TiMidity++ package now.

* Wed Jan 10 2001 AEN <aen@logic.ru>
- RE adaptations

* Fri Nov 24 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0-8mdk
- Use %_tmppath for BuildRoot
- Clean after build
- Macros
- Remove frech locales

* Mon Sep 25 2000 Maurizio De Cecco <maurizio@mandrakesoft.com> 1.0-7mdk
- Fixed rpmlint errors.

* Tue Apr 11 2000 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Fixed Distribution name

* Thu Mar 16 2000 Maurizio De Cecco  <maurizio@mandrakesoft.com>
- Adapted to the new Group structure

* Tue Oct 26 1999 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Modified for (and requiring) Timidity version 2.7
- Chmouel: Remove the chown -R 0.0 and a dd a %%defattr.

* Tue Jul 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- add french description

* Tue Jul 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- add french description
- fix spec
