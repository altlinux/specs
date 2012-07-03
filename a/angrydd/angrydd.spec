Name:           angrydd
Version:        1.0.1
Release:        alt5_8
Summary:        Falling blocks game

Group:          Games/Other
License:        GPLv2
URL:            http://www.sacredchao.net/~piman/angrydd/
Source0:        http://www.sacredchao.net/~piman/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source3:        %{name}.desktop
BuildArch:      noarch

BuildRequires:  desktop-file-utils
Requires:       python-module-pygame icon-theme-hicolor libgtk+2
Source44: import.info

%description
In Angry, Drunken Dwarves (ADD), you are an angry, drunken dwarf. Why are you
so angry? Who knows. But you've decided to take your aggression out on other
dwarves, by dropping gems on their heads. Lots of gems. ADD is a member of the
classic "falling blocks" puzzle game family, similar to the Capcom game Puzzle
Fighter. The goal of the game is to build large gems by matching up colors,
then break them, raining more gems down onto your opponent. The first person
whose field fills up, loses.

%prep
%setup -q

sed -i 's|PREFIX ?= /usr/local|PREFIX ?= %{_prefix}|' Makefile
sed -i 's|TO = share/games/angrydd|TO = share/angrydd|' Makefile
sed -i 's|install -m 644|install -p -m 644|' Makefile
sed -i 's|cp -R|cp -Rp|' Makefile
sed -i 's|install -d $(DESTDIR)$(PREFIX)/games|install -d $(DESTDIR)%{_bindir}|' Makefile
sed -i 's|ln -sf ../$(TO)/angrydd.py $(DESTDIR)$(PREFIX)/games/angrydd|ln -sf ../$(TO)/angrydd.py $(DESTDIR)%{_bindir}/angrydd|' Makefile


%build
#there's nothing to build


%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/

desktop-file-install                     \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications           \
  %{SOURCE3}

%files
%doc COPYING README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt5_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4_8
- update to new release by fcimport

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt4_7.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4_7
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_6
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_6
- converted from Fedora by srpmconvert script

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_6
- converted from Fedora by srpmconvert script

