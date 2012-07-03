# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: pysol.spec,v 1.6 2006/02/25 20:04:16 eugene Exp $

Name: pysol
Version: 4.82
Release: alt11.1.1

Summary: PySol provides several solitaire card games
Summary(ru_RU.UTF-8): PySol предлагает коллекцию карточных пасьянсов

License: GPL
Group: Games/Cards
Packager: Igor Vlasenko <viy@altlinux.ru>
URL: http://www.oberhumer.com/opensource/pysol/

Source0: %name-%version.tar.bz2
Source1: %name-%version-src.tar.bz2
Source2: icons-%name.tar.bz2
Source3: pysol.desktop

Patch0: %name-fix.patch
Patch1: %name-nosplash.patch
Patch2: %name-nosound.patch
Patch3: %name-colorchooser.patch

Conflicts: pysol-cardsets <= 4.40-alt1
Conflicts: pysol-music <= 4.40-alt1

BuildArchitectures: noarch

%add_python_req_skip acard actions gamedb help mfxtools mfxutil stats util pysolaudio
%add_python_req_skip pysolsoundserver
%add_python_compile_include %_gamesdatadir/%name

# Automatically added by buildreq on Wed Mar 30 2005 (-bi)
BuildRequires: python-base python-modules-compiler python-modules-encodings

%description
PySol has several solitaire card games, written in 100%% pure
Python. It has many features: unlimited undo and redo, load & save
games, player statistics, hint system, game plug-ins, and more!
Contains: klondike, freecel, spider, golf, etc.

%description -l ru_RU.UTF-8
PySol - коллекция свыше 200 пасьянсов, на 100%% написанных на Python.
Игра имеет большое количество возможностей: неограниченную отмену и повтор
хода, загрузку и сохранение игр, статистику игрока, систему подсказок,
подключаемые игры и так далее. Содержит игры klondike (косынка),
freecell, spider, golf и многие другие.

%prep
%setup -q -a 1
%patch0
%patch1
%patch2
%patch3

%install
%make_install \
    prefix=%buildroot%prefix \
    mandir=%buildroot%_mandir \
    pkgdatadir=%buildroot%_gamesdatadir/%name \
    install-bin install-data install-man

find %buildroot -type f -print0 |
	xargs -r0 fgrep -l "%buildroot" |
	xargs -r perl -pi -e "s|%buildroot||g"

cp -rf %name-%version/src/*  %buildroot%_gamesdatadir/%name

install -d %buildroot%_gamesbindir
cat >%buildroot%_gamesbindir/%name.sh <<EOF
#!/bin/sh -e
cd %_gamesdatadir/%name
PYTHON=python
\$PYTHON ./pysol.py
EOF
chmod 755 %buildroot%_gamesbindir/%name.sh

# Menu support - used desktop file
# mkdir -p %buildroot{%_menudir,%_iconsdir,%_liconsdir,%_miconsdir}
# cat >%buildroot%_menudir/%name <<EOF
# ?package(%name): \
# needs=x11 \
# section=Amusement/Cards \
# title=PySOL \
# command="soundwrapper %_gamesbindir/%name.sh" \
# icon=%name.xpm \
# longtitle="All solitaire cards games"
# EOF
install -d %buildroot%_desktopdir
install -m 644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

# icons
install -d %buildroot%_miconsdir
install -d %buildroot%_liconsdir
install -d %buildroot%_niconsdir
tar xjf %SOURCE2 
mv large/* %buildroot%_liconsdir
mv mini/* %buildroot%_miconsdir
mv pysol.xpm %buildroot%_niconsdir

(cd %buildroot%_gamesdatadir/%name
    find . -type f -name 'Makefile'  -print0|xargs -r0 rm -rfv
    find . -type f -name 'README*' -print0|xargs -r0 rm -rfv
    find . -type f -name '*.py?' -print0|xargs -r0 rm -rfv
)

%files
%_gamesbindir/%name.sh
%_gamesdatadir/%name
%_mandir/man?/*
%_desktopdir/%name.desktop
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%doc README
%exclude %_bindir/%name


%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.82-alt11.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.82-alt11.1
- Rebuilt with python 2.6

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 4.82-alt11
- fixed .desktop (closes: #22155)

* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 4.82-alt10
- fixed _niconsdir

* Mon Oct 12 2009 Igor Vlasenko <viy@altlinux.ru> 4.82-alt9
- resurrected from orphaned,
- moved to /usr/share/games

* Fri Jan 04 2008 Eugene Vlasov <eugvv@altlinux.ru> 4.82-alt8
- Menu file replaced by desktop entry
- Run application without soundwrapper (#13651)

* Sun Feb 26 2006 Eugene Vlasov <eugvv@altlinux.ru> 4.82-alt7
- Fixed build with new %%_liconsdir and %%_miconsdir values
- Fixed macros warnings
- Dropped requires on /usr/bin/python (python-strict)
- Fixed unpackaged files warning

* Tue Jun 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 4.82-alt6
- Removed requires on sound server (package python-module-pysol-sound)
- Fixed crash on tile color select

* Thu Mar 31 2005 Eugene Vlasov <eugvv@altlinux.ru> 4.82-alt5
- Rebuild with python2.4
- Fixed buildreq
- Removed annoying splash screen
- Byte-compile game sources

* Tue Jul 13 2004 Alexei Takaseev <taf@altlinux.ru> 4.82-alt4
- Fix #4688 bug (thanks to Eugene Vlasov)

* Thu May 20 2004 Alexei Takaseev <taf@altlinux.ru> 4.82-alt3
- Fix Buildrequire: python23 -> python
- Remove requires tkinter

* Sun Dec 07 2003 Alexei Takaseev <taf@altlinux.ru> 4.82-alt2
- Rebuild with python23
- Fix /usr/lib/menu/pysol (Inverted commas in parameter 'command' are missed)
- Remove Tkinter.py (fixed in new version Python)

* Thu Oct 30 2003 Alexei Takaseev <taf@altlinux.ru> 4.82-alt1
- 4.82
- Fix buildreq
- Moving from /usr/share to /usr/games

* Tue Aug 13 2002 Stanislav Ievlev <inger@altlinux.ru> 4.81-alt1
- 4.81

* Thu Jan 29 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.72-alt3
- Rebuilt with python-2.2

* Wed Jun 27 2001 Sergie Pugachev <fd_rag@altlinux.ru>  4.72-alt2
- Rebuilt with python-2.1

* Tue Jun 26 2001 Sergie Pugachev <fd_rag@altlinux.ru> 4.72-alt1
- new version

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations
- added _real_ source
- build with python 2.0
* Thu Dec  7 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.60-4mdk
- corrected menu entry.

* Thu Oct 05 2000 Daouda Lo <daouda@mandrakesoft.com> 4.60-3mdk
- provide ln icons
- macroz++

* Wed Sep 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.60-2mdk
- changed dependency from python to tkinter.

* Wed Aug 16 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.60-1mdk
- 4.60

* Tue Jul  4 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.41-1mdk
- 4.41

* Thu Apr 20 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.10-1mdk
- first mandrake version.

* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed a bug in the directory where the pixmap was being put

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 2.14

* Thu Mar 18 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations

* Fri Mar 12 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- initial package


