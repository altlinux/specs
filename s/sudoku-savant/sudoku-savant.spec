# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate gcc-c++
# END SourceDeps(oneline)
Name:           sudoku-savant
Version:        1.3
Release:        alt2_17
Summary:        Solve and generate sudoku puzzles through logical means
Summary(de):    Lösen und Erstellen von Sudoku-Puzzles mit logischen Mitteln

Group:          Games/Other
# Impossible to figure out the actual license in the sources.
# Upstream bug: https://sourceforge.net/tracker/?func=detail&aid=3272054&group_id=172187&atid=860784
License:        GPL+
URL:            http://sourceforge.net/projects/%{name}/

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        sudoku-savant-icons.txz

# Patch is taken from the Opensuse package.
# Without it, "make" cannot install the icons and the *.desktop file
# into buildroot and tries to use the real system folders instead.
# Upstream bug: https://sourceforge.net/tracker/?func=detail&aid=3294399&group_id=172187&atid=860784
Patch0:         %{name}-Makefile.patch
Patch1:         %{name}-aarch64.patch

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
%patch1 -p1

cp -a %{SOURCE1} .

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

install -dm 755 %{buildroot}%{_datadir}/icons/hicolor
tar xJ --directory=%{buildroot}%{_datadir}/icons/hicolor < %{name}-icons.txz

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 William Moreno <williamjmorenor@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/sudoku-savant/bugs/3/
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">sudoku-savant.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Complete a numeric puzzle with the numbers from one to nine</summary>
  <description>
    <p>
      Sudoku Savnt a free version of the popular logic game Sudoku for the Linux desktop .
      The game is to fill a nine by nine grid with the numbers from one to nine
      filling the rows, columns and three by three squares without repeating a
      value on them.
    </p>
  </description>
  <url type="homepage">http://sourceforge.net/projects/sudoku-savant/</url>
</application>
EOF

%find_lang %{name}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%_iconsdir/hicolor/*/*/*
%exclude %{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_16
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_14
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_10
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_7
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_6
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_4
- rebuild with fixed sourcedep analyser (#27020)

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- converted from Fedora by srpmconvert script

