# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(cairo) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0)
# END SourceDeps(oneline)
Summary(de): Logikpuzzle für GNOME
Summary(de): Logikpuzzle für GNOME
Name:		hitori
Version:	0.3.1
Release:	alt2_4
Summary:	Logic puzzle game for GNOME
Summary(de):	Logikpuzzle für GNOME

Group:		Games/Other
# The executable is licensed under GPLv3+, while the user manual is CC-BY-SA.
License:	GPLv3+ and CC-BY-SA
URL:		http://live.gnome.org/Hitori
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.3/%{name}-%{version}.tar.xz
Patch0:		hitori-fixdso.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gnome-doc-utils
BuildRequires:	libgtk+3-devel
BuildRequires:	intltool

Requires:	icon-theme-hicolor
Source44: import.info

%description
A small application written to allow one to play the Hitori puzzle game,
which is similar in theme to more popular puzzles such as Sudoku.

It depends on GTK+ 2.13 and Cairo 1.4, and has full support for playing the
game (i.e. it checks all three rules are satisfied). It has undo/redo support,
can give hints, and allows for cells to be tagged with one of two different
tags, to aid in solving the puzzle. It has support for anything from
5A-5 to 10A-10 grids.

%description -l de
Ein kleines Programm zum Spielen des Hitori-Puzzles, das thematisch
populäreren Puzzlespielen wie beispielsweise Sudoku ähnelt.

Das Programm basiert auf GTK+ 2.13 und Cairo 1.4 und unterstützt die
Spielregeln vollständig. Es wird in jedem Fall überprüft, ob die drei
Ausschlussregeln angewendet sind. Das Zurücknehmen und Wiederholen von Zügen
ist ebenso möglich wie das Kennzeichnen von Feldern mit einer oder mehreren
Markierungen, um den Weg zur Lösung zu erleichtern. Mögliche Spielfeldgrößen
reichen von 5x5 bis hin zu 10x10 Feldern. 

%prep
%setup -q
%patch0 -p1 -b .fixdso


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%%doc AUTHORS ChangeLog COPYING COPYING-DOCS MAINTAINERS NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/%{name}.ui
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_4
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_1
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_3
- converted from Fedora by srpmconvert script

