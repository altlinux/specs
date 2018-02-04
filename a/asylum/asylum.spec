# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
BuildRequires: gcc-c++
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           asylum
Version:        0.3.2
Release:        alt1_16
Summary:        Game involving shooting anything that moves & collecting others
Group:          Games/Other
# For detailed licensing, see the README
License:        GPLv3 and Public Domain
URL:            http://sdl-asylum.sourceforge.net
Source0:        http://downloads.sourceforge.net/sdl-%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Patch0:         asylum-0.3.2-paths.patch

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

%patch0 -p0

# Character encoding fixes
iconv -f iso8859-1 README -t utf8 > README.conv \
    && /bin/mv -f README.conv README

# Delete bundled binary to make absolutely sure we get a new one.
rm -f %{name}

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"

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
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop

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
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
EmailAddress: https://sourceforge.net/u/blotwell/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">asylum.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A retro platform style game where you enter the surreal world of a brain</summary>
  <description>
    <p>
      Asylum is a Linux port of the game "Asylum" written originally for the
      Acorn Archimedes.
    </p>
    <p>
      Enter the surreal world inside a young boy's brain and help destroy
      malfunctioning brain cells.
    </p>
  </description>
  <url type="homepage">http://sdl-asylum.sourceforge.net</url>
  <screenshots>
    <screenshot type="default">http://sourceforge.net/p/sdl-asylum/screenshot/134775.jpg</screenshot>
    <screenshot>http://sourceforge.net/p/sdl-asylum/screenshot/136451.jpg</screenshot>
  </screenshots>
</application>
EOF

# touching all ghosts; hack for rpm 4.0.4
for rpm404_ghost in %{_var}/games/%{name}/EgoHighScores %{_var}/games/%{name}/PsycheHighScores %{_var}/games/%{name}/IdHighScores %{_var}/games/%{name}/ExtendedHighScores
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done


%files
# Note the game is SETGID games for the hi-scores.
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%attr(0775,root,games) %dir %{_var}/games/%{name}
%attr(2711,root,games) %{_bindir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%doc Instruct README COPYING
%ghost %{_var}/games/%{name}/EgoHighScores
%ghost %{_var}/games/%{name}/PsycheHighScores
%ghost %{_var}/games/%{name}/IdHighScores
%ghost %{_var}/games/%{name}/ExtendedHighScores


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_16
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_11
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_6
- update to new release by fcimport

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_4
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_2
- update to new version

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_4
- converted from Fedora by srpmconvert script

