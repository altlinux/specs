# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(cairo) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0)
# END SourceDeps(oneline)
Summary(de): Logikpuzzle für GNOME
Summary(de): Logikpuzzle für GNOME
Summary(de): Logikpuzzle für GNOME
Name:		hitori
Version:	0.3.2
Release:	alt1_2
Summary:	Logic puzzle game for GNOME
Summary(de):	Logikpuzzle für GNOME

Group:		Games/Other
# The executable is licensed under GPLv3+, while the user manual is CC-BY-SA.
License:	GPLv3+ and CC-BY-SA
URL:		http://live.gnome.org/Hitori
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.3/%{name}-%{version}.tar.xz

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

It has full support for playing the game (i.e. it checks all three rules are
satisfied). It has undo/redo support, can give hints, and allows for cells
to be tagged with one of two different tags, to aid in solving the puzzle.
It has support for anything from 5A-5 to 10A-10 grids.

%description -l de
Ein kleines Programm zum Spielen des Hitori-Puzzles, das thematisch
populäreren Puzzlespielen wie beispielsweise Sudoku ähnelt.

Das Programm unterstützt die Spielregeln vollständig. Es wird in
jedem Fall überprüft, ob die drei Ausschlussregeln angewendet sind.
Das Zurücknehmen und Wiederholen von Zügen ist ebenso möglich wie das
Kennzeichnen von Feldern mit einer oder mehreren Markierungen, um den Weg zur
Lösung zu erleichtern. Mögliche Spielfeldgrößen reichen von 5x5 bis hin zu
10x10 Feldern. 

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi

%files -f %{name}.lang
%%doc AUTHORS ChangeLog COPYING COPYING-DOCS MAINTAINERS NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/%{name}.ui
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png


%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_2
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_4
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_1
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_3
- converted from Fedora by srpmconvert script

