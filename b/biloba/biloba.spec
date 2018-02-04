# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install imake libSDL-devel libX11-devel libXt-devel xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           biloba
Version:        0.9.3
Release:        alt2_14
Summary:        A tactical board game

Group:          Games/Other
License:        GPLv2+
URL:            http://biloba.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        biloba.desktop

BuildRequires:  desktop-file-utils ImageMagick-tools libSDL_image-devel libSDL_mixer-devel
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
%make_build

iconv -f iso-8859-1 -t utf-8 ChangeLog -o ChangeLog.char
mv ChangeLog.char ChangeLog

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{64x64,32x32,16x16}/apps
cp -p biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/biloba.png
convert -scale 32x32 biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/biloba.png
convert -scale 16x16 biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/biloba.png

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: colin@colino.net
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">biloba.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Strategic board game</summary>
  <description>
    <p>
      Biloba is a board game for 2 to 4 players that involves moving pawns around on
      an octagonal board with square cells. The goal of bilboa is to remove all of your
      opponent's pawns. Bilboa can be played both against AI and real opponents.
    </p>
  </description>
  <url type="homepage">http://biloba.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://biloba.sourceforge.net/2p.png</screenshot>
    <screenshot>http://biloba.sourceforge.net/3p.png</screenshot>
    <screenshot>http://biloba.sourceforge.net/4p.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

desktop-file-install                    \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE1}

%files
%doc AUTHORS ChangeLog COPYING 
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_14
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_11
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_9
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_5
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_3
- update to new release by fcimport

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

