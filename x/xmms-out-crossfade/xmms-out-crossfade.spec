%define origname xmms-crossfade

Name: xmms-out-crossfade
Version: 0.3.14
Release: alt2

Epoch: 20091213

Summary: Crossfade output plugin for XMMS
License: GPL
Group: Sound

Url: http://www.eisenlohr.org/xmms-crossfade
Source: %url/%origname-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.ru>

Obsoletes: xmms-crossfade

Summary(ru_RU.KOI8-R): "Мягкий переход" для XMMS
Summary(uk_UA.KOI8-U): "М'який перех╕д" для XMMS

# Automatically added by buildreq on Sun Dec 13 2009 (-bi)
BuildRequires: id3lib-devel libgtk+2-devel libsamplerate-devel libxmms-devel xmms

# need new macros
BuildRequires: libxmms-devel >= 1.2.8-alt2

# applied recommended patch there
Requires: libxmms >= 1.2.10-alt11

%description
XMMS Output Plugin for Crossfading and Continuous Output

Features:
  * Crossfading
  * Continuous output
  * Gap-Killer: Some mp3-encoders produce small gaps of silence at the
    beginning or end of the stream. They can automatically be detected
    and removed.

%description -l ru_RU.KOI8-R
Дополнение к XMMS для кроссфейдинга и непрерывного звука

Функции:
  * Кроссфейдинг
  * Непрерывное звучание (без пауз)
  * Удаление пустых участков: некоторые mp3-кодеки оставляют в начале
    или конце записи участки тишины, которые могут быть обнаружены и
    пропущены.

%description -l uk_UA.KOI8-U
Додаток до XMMS для кроссфейдингу та безперервного звуку

Функц╕╖:
  * Кроссфейдин╜
  * Безперервне в╕дтворення (без павз)
  * Видалення пустих фрагмент╕в: деяк╕ mp3-кодеки залишають напочатку
    чи наприк╕нц╕ запису трохи тиш╕, яку може бути знайдено да оминено.

%prep
%setup -n %origname-%version
subst 's,PLAYER_BIN="\$XMMS,&-bin,' configure.in

%build
%autoreconf
%configure --enable-samplerate --enable-id3
%make

%install
%makeinstall libdir=%buildroot%xmms_outputdir

%files
%doc AUTHORS README ChangeLog
%xmms_outputdir/libcrossfade.*

%changelog
* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 20091213:0.3.14-alt2
- enabled id3lib support
- buildreq (thx repocop)

* Mon Nov 26 2007 Michael Shigorin <mike@altlinux.org> 20071126:0.3.14-alt1
- 0.3.14

* Sun Nov 25 2007 Michael Shigorin <mike@altlinux.org> 20071125:0.3.13-alt1
- 0.3.13

* Mon Mar 05 2007 Michael Shigorin <mike@altlinux.org> 20070305:0.3.12-alt1
- 0.3.12

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 20061109:0.3.11-alt1
- 0.3.11
- no more TODO

* Mon Jun 05 2006 Michael Shigorin <mike@altlinux.org> 20060520:0.3.10-alt1
- tossed out and rebuilt (gcc4 is finally here)
- thanks vsu@ for unbraking my head on gtk2/glib2 autoconf macros
- tweaked configure.in to reflect that %_bindir/xmms is actually
  a shell wrapper in current ALT Linux package

* Wed Jan 25 2006 Michael Shigorin <mike@altlinux.org> 20060125:0.3.10-alt0
- 0.3.10
  + 0.3.9 missed due to upstream recommendation

* Wed Jul 06 2005 Michael Shigorin <mike@altlinux.org> 20050706:0.3.8-alt1
- 0.3.8
- should fix #7251 (skipping to the next song randomly)
- updated buildrequires

* Tue Dec 23 2003 Michael Shigorin <mike@altlinux.ru> 20031223:0.3.4-alt2
- rebuilt for Sisyphus

* Sat Nov 22 2003 Michael Shigorin <mike@altlinux.ru> 20031122:0.3.4-alt1
- updated for new plugin policy                                
- renamed to %name
- spec cleanup

* Thu Oct 23 2003 Michael Shigorin <mike@altlinux.ru> 0.3.4-alt1
- 0.3.4 (major bugfixes)

* Tue Oct 07 2003 Michael Shigorin <mike@altlinux.ru> 0.3.3-alt1
- 0.3.3 (minor bugfixes)

* Fri Apr 25 2003 Michael Shigorin <mike@altlinux.ru> 0.3.2-alt1
- 0.3.2 (minor bugfixes)

* Wed Mar 12 2003 Michael Shigorin <mike@altlinux.ru> 0.3.1-alt1
- 0.3.1
- now processes Pause, thanks Peter!
- usual spec cleanup

* Fri Nov 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.2.9-alt2
- Rebuilt in new environment
- Some spec cleanup
- Added buildrequires

* Wed Jun 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.2.9-alt1
- New version - 0.2.9

* Thu Feb 22 2001 Kostya Timoshenko <kt@petr.kz> 0.2.3-ipl1mdk
- build for RE

* Mon Jan 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2.3-1mdk
- used srpm from  GЖtz Waschk <waschk@linux-mandrake.com> :
- 0.2.3
- %%configure macro

* Mon Dec 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.2.2-1mdk
- updated to 0.2.2 by GЖtz Waschk <waschk@linux-mandrake.com> 

* Wed Nov 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.2.1-1mdk
- used srpm from GЖtz Waschk <waschk@linux-mandrake.com> :
- 0.2.1
- changed BuildReq for libxmms-devel

* Mon Nov 20 2000 GЖtz Waschk <waschk@linux-mandrake.com> 0.2-1mdk
- 0.2
- don't use configure macro
- fix installation

* Tue Oct  3 2000 GЖtz Waschk <waschk@linux-mandrake.com> 0.1.1-1mdk
- initial Mandrake build
