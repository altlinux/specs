# sources are not ported to qt5
%def_with qt4
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global sum     Program to solve mathematical puzzles

Name:           kitsune
Version:        3.0
Release:        alt1_8
Summary:        %{sum}
Group:          Games/Puzzles
License:        GPLv2+
URL:            https://kitsune.tuxfamily.org/wiki/doku.php
Source0:        https://download.tuxfamily.org/kitsune/%{name}%{version}/%{name}%{version}.tar.gz
Source1:        kitsune-de.ts
Patch0:         kitsune-3.0-mga-manage-translations.patch

BuildRequires:  icoutils icoutils-extra
%if_with qt4
BuildRequires:  libqt4-devel
%else
BuildRequires:  qt5-base-devel qt5-declarative-devel qt5-tools
%endif
Source44: import.info

%description
Kitsune is a software aiming at solving digit problems of a famous
television game show called "Countdown" in England and "Des chiffres
et des lettres" in France.

It enables you to solve a problem of your choice, or to train yourself
with random problems. Facing a problem, Kitsune will find all the different
solutions: if the problem is solvable, this software will put up all the
ways to reach the target. If the problem is not solvable, it will put up
the best approximations. 

%prep
%setup -q -n %{name}%{version}
%patch0 -p1


# German translation seems to be missing from the source tarball
cp %{_sourcedir}/%{name}-de.ts txt/de/%{name}.ts

%build
%if_with qt4
lrelease-qt4 kitsune.pro
%qmake_qt4
%else
lrelease-qt5 kitsune.pro
%qmake_qt5
%endif
%make_build

%install
# Install binary
mkdir -p %{buildroot}%{_gamesbindir}
install -m 755 bin/kitsune %{buildroot}%{_gamesbindir}

# Extract and install icon
for size in 16 32 48; do
  install -d %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/
  icotool -x --width=${size} appliwin.ico -o %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/%{name}.png
done

# Remove translation source files from doc, and all pt content
find -name "*.ts" -delete
rm txt/pt -rf

# Mageia menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Kitsune
Comment=%{sum}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

%files
%doc Changelog.txt txt/*
%{_datadir}/applications/%{name}.desktop
%{_gamesbindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png


%changelog
* Fri Sep 15 2023 Igor Vlasenko <viy@altlinux.org> 3.0-alt1_8
- new version

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_24
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_22
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_20
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_13
- update to new release by fcimport

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_10
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_8
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_7
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_7
- converted from Fedora by srpmconvert script

