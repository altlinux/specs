# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
Summary(de): Lösen und Erstellen von Sudoku-Puzzles mit logischen Mitteln
Summary(de): Lösen und Erstellen von Sudoku-Puzzles mit logischen Mitteln
Summary(de): Lösen und Erstellen von Sudoku-Puzzles mit logischen Mitteln
Name:           sudoku-savant
Version:        1.3
Release:        alt2_6
Summary:        Solve and generate sudoku puzzles through logical means
Summary(de):    Lösen und Erstellen von Sudoku-Puzzles mit logischen Mitteln

Group:          Games/Other
# Impossible to figure out the actual license in the sources.
# Upstream bug: https://sourceforge.net/tracker/?func=detail&aid=3272054&group_id=172187&atid=860784
License:        GPL+
URL:            http://sourceforge.net/projects/%{name}/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Patch is taken from the Opensuse package.
# Without it, "make" cannot install the icons and the *.desktop file
# into buildroot and tries to use the real system folders instead.
# Upstream bug: https://sourceforge.net/tracker/?func=detail&aid=3294399&group_id=172187&atid=860784
Patch0:         %{name}-Makefile.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
Source44: import.info

%description
A simple GUI-driven application to solve and generate sudoku puzzles through
logical means. Also supports manual solving, with pencil marks and cell
coloring. Should be able to solve any standard sudoku from a newspaper
or magazine.

%description -l de
Eine einfache grafische Anwendung zum Lösen und Erstellen von Sudoku-Puzzles
mit logischen Mitteln. Das manuelle Lösen wird ebenfalls unterstützt, mit
Hilfe von Markierungen und Einfärben der Felder. Es sollte möglich sein, jedes
Standard-Sudoku aus Zeitungen oder Zeitschriften zu lösen.

%prep
%setup -q
%patch0 -p0


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_6
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_4
- rebuild with fixed sourcedep analyser (#27020)

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- converted from Fedora by srpmconvert script

