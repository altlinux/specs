# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSDL-devel libSM-devel libX11-devel
# END SourceDeps(oneline)
Name:           biloba
Version:        0.9.3
Release:        alt2_2
Summary:        A tactical board game

Group:          Games/Other
License:        GPLv2+
URL:            http://biloba.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        biloba.desktop

BuildRequires:  desktop-file-utils ImageMagick libSDL_image-devel libSDL_mixer-devel
Requires:       icon-theme-hicolor
Source44: import.info

%description
Biloba is a very innovative tactical board game. It can be played
by 2, 3 or 4 players and against the computer (AI).
You will be able to play on the same computer or online against
your opponents.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}

iconv -f iso-8859-1 -t utf-8 ChangeLog -o ChangeLog.char
mv ChangeLog.char ChangeLog

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{64x64,32x32,16x16}/apps
cp -p biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/biloba.png
convert -scale 32x32 biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/biloba.png
convert -scale 16x16 biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/biloba.png

desktop-file-install                     \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE1}

%files
%doc AUTHORS ChangeLog COPYING 
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_2
- update to new release by fcimport

* Wed Oct 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_1
- update to new release by fcimport

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_2
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- converted from Fedora by srpmconvert script

