BuildRequires: gcc-c++
Name:           asylum
Version:        0.3.2
Release:        alt1_2
Summary:        SDL port of the game Asylum, originally for the Archimedes
Group:          Games/Other
# For detailed licensing, see the README
License:        GPLv3 and Public Domain
URL:            http://sdl-asylum.sourceforge.net
Source0:        http://downloads.sourceforge.net/sdl-%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png

BuildRequires:  desktop-file-utils
BuildRequires:  libSDL_mixer-devel
Requires:       icon-theme-hicolor
Source44: import.info

%description
SDL Asylum is a C port of the computer game Asylum, which was written by Andy
Southgate in 1994 for the Acorn Archimedes and is now public domain. The object
is to find things that look like brain cells and shut them down! The game
revolves around shooting anything which moves, collecting anything which
doesn't move and most importantly, finding your way to each of the eight
pulsating neurons scattered through the immense map.


%prep
%setup -q

# Character encoding fixes
iconv -f iso8859-1 README -t utf8 > README.conv \
    && /bin/mv -f README.conv README

# Delete bundled binary to make absolutely sure we get a new one.
rm -f %{name}


%build
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"

# Build desktop icon
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=Asylum
GenericName=Platform Game
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ActionGame;
EOF


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_var}/games/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
touch %{buildroot}%{_var}/games/%{name}/{EgoHighScores,PsycheHighScores,IdHighScores,ExtendedHighScores}

install -m0755 %{name} %{buildroot}%{_bindir}
cp -a data/* %{buildroot}%{_datadir}/%{name}

install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
desktop-file-install --vendor fedora \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop


%files
# Note the game is SETGID games for the hi-scores.
%{_datadir}/%{name}
%{_datadir}/applications/fedora-%{name}.desktop
%attr(0775,root,games) %dir %{_var}/games/%{name}
%attr(2711,root,games) %{_bindir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%doc Instruct README COPYING
%ghost %{_var}/games/%{name}/EgoHighScores
%ghost %{_var}/games/%{name}/PsycheHighScores
%ghost %{_var}/games/%{name}/IdHighScores
%ghost %{_var}/games/%{name}/ExtendedHighScores


%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_2
- update to new version

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_4
- converted from Fedora by srpmconvert script

