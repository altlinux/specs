# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libICE-devel libSM-devel
# END SourceDeps(oneline)
Name:           abe
Version:        1.1
Release:        alt5_15

Summary:        Scrolling, platform-jumping, ancient pyramid exploring game
Group:          Games/Other
License:        GPL+
URL:            http://abe.sourceforge.net/
Source0:        http://downloads.sourceforge.net/abe/abe-%{version}.tar.gz
Source1:        %{name}.png
Patch0:         abe-1.1-settings.patch
Patch1:         abe-1.1-doublefree.patch
Patch2:         abe-1.1-format.patch

BuildRequires:  libSDL-devel >= 1.2.3 libSDL_mixer-devel >= 1.2.3
BuildRequires:  libXmu-devel libXi-devel
BuildRequires:  desktop-file-utils
Source44: import.info

%description
A scrolling, platform-jumping, key-collecting, ancient pyramid exploring game,
vaguely in the style of similar games for the Commodore+4.

%prep
%setup -q
%patch0 -p1
%patch1
%patch2

%build
%configure --with-data-dir=%{_datadir}/%{name}
sed -i "s/^CFLAGS =.*/CFLAGS = ${RPM_OPT_FLAGS} \$\(SDL_CFLAGS\)/" src/Makefile
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# make install does not copy the game data files.
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
cp -p -r images maps sounds $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/pixmaps/

cat << EOF > %{name}.desktop
[Desktop Entry]
Name=Abe
Comment="Abe's Amazing Adventure"
Exec=abe
Icon=abe
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Game;ArcadeGame;
EOF

desktop-file-install  --dir $RPM_BUILD_ROOT/%{_datadir}/applications/ %{name}.desktop

%files
%doc COPYING README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_15
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_15
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_14
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_13
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13
- rebuild with new rpm desktop cleaner

* Fri Mar 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13
- new origin release

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_12
- converted from Fedora by srpmconvert script

