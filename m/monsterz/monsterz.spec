Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install /usr/bin/pathfix.py
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           monsterz
Version:        0.7.1
Release:        alt3_34
Summary:        Puzzle game, similar to Bejeweled or Zookeeper
License:        WTFPL
URL:            http://sam.zoy.org/monsterz/
Source0:        http://sam.zoy.org/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.score
Patch0:         %{name}-0.7.1-userpmopts.patch
Patch1:         %{name}-0.7.1-64bitfix.patch
Patch2:         %{name}-0.7.1-blit-crash.patch
Patch3:         %{name}-0.7.1-py3.patch
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
Requires:       python3-module-pygame
Requires:       icon-theme-hicolor
Provides:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-data < 0.7.1
Source44: import.info

%description
Monsterz is a little arcade puzzle game, similar to the famous Bejeweled or
Zookeeper. The goal of the game is to create rows of similar monsters, either
horizontally or vertically. The only allowed move is the swap of two adjacent
monsters, on the condition that it creates a row of three or more. When
alignments are cleared, pieces fall from the top of the screen to fill the
board again. Chain reactions earn you even more points.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%make_build prefix=%{_usr} datadir=%{_datadir} pkgdatadir=%{_datadir}/%{name} CFLAGS="%{optflags}"

# Build desktop icon
cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Monsterz
GenericName=Monsterz Puzzle Game
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF


%install
# Bypass make install as it requires root priviledges and the SRPM
# may not necessarily be built as root
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/{applications,icons/hicolor/64x64/apps}
mkdir -p %{buildroot}%{_datadir}/%{name}/{graphics,sound}
mkdir -p %{buildroot}%{_var}/games
install -pm0755 %{name} %{buildroot}%{_bindir}
install -pm0755 %{name}.py %{buildroot}%{_datadir}/%{name}
cp -a graphics/* %{buildroot}%{_datadir}/%{name}/graphics
cp -a sound/* %{buildroot}%{_datadir}/%{name}/sound

install -pm0664 %{SOURCE1} %{buildroot}%{_var}/games/%{name}

desktop-file-install \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop

install -pm0644 graphics/icon.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/%{name}
%attr(2711,root,games) %{_bindir}/%{name}
%attr(-,root,games) %config(noreplace) %{_var}/games/%{name}
%doc --no-dereference COPYING
%doc AUTHORS README TODO


%changelog
* Thu Oct 12 2023 Igor Vlasenko <viy@altlinux.org> 0.7.1-alt3_34
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt3_27
- update to new release by fcimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt3_25
- update to new release by fcimport

* Mon Oct 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.1-alt3
- python2 -> python3

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_23
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_19
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_16
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_11
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_8
- update to new release by fcimport

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.1-alt1_7.1
- Rebuild with Python-2.7

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_7
- converted from Fedora by srpmconvert script

