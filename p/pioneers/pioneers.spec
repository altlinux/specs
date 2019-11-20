Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/rsvg-convert ImageMagick-tools pkgconfig(avahi-client) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-3.0) pkgconfig(libnotify)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           pioneers
Version:        15.5
Release:        alt1_1
Summary:        Turnbased board strategy game (colonize an island)
License:        GPLv2+
URL:            http://pio.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pio/%{name}-%{version}.tar.gz
Patch0:         pioneers-15.5-sanitize.patch
BuildRequires:  gcc
BuildRequires:  libgnome-devel gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel gettext gettext-tools scrollkeeper intltool
BuildRequires:  itstool
BuildRequires:  perl(XML/Parser.pm) desktop-file-utils
Requires:       icon-theme-hicolor
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Source44: import.info

%description
Pioneers is a computerized version of a well known strategy board game. The
goal of the game is to colonize an island. The players play the first
colonists hence the name pioneers.

Pioneers is a networkbased multiplayer game, this package contains the GUI
client as well as both a GUI and CLI version of the server for local games.


%package editor
Group: Games/Other
Summary:        Pioneers Game Editor
Requires:       pioneers = %{version}-%{release}

%description editor
Pioneers is a computerized version of a well known strategy board game. The
goal of the game is to colonize an island. The players play the first
colinists hence the name pioneers.

The game editor allows maps and game descriptions to be created and
edited graphically.


%prep
%setup -q
%patch0 -p1 -z .sanitize
	

%build
# pioneers uses some GNU extensions
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
%configure
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

# Remove the too much like the original splashscreen
rm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}/splash.png

# Reinstall the .desktop files
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-editor.desktop \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-server-gtk.desktop

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
<!-- Copyright 2014 Eduardo Mayorga <e@mayorgalinux.com> -->
<!--
BugReportURL: https://sourceforge.net/p/pio/bugs/286/
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">pioneers.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Multiplayer board game inspired by The Settlers of Catan</summary>
  <description>
    <p>
      Pioneers is a free videogame implementation of the famous German game Settlers of Catan.
      The goal is to build towns, cities and roads on a board that is different every time, while accumulating various types of cards.
      It can be played online.
    </p>
  </description>
  <url type="homepage">http://pio.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://pio.sourceforge.net/screenshots0.11/client.png</screenshot>
  </screenshots>
</application>
EOF

%check
if grep Catan `find $RPM_BUILD_ROOT ! -path "$RPM_BUILD_ROOT/usr/src/debug*"`;
  then
  exit 1
fi



%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README NEWS
%{_bindir}/%{name}
%{_bindir}/%{name}ai
%{_bindir}/%{name}-metaserver
%{_bindir}/%{name}-server-console
%{_bindir}/%{name}-server-gtk
%{_datadir}/games/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/help/C/%{name}
%{_mandir}/man6/%{name}*.6*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-server-gtk.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-server.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-server.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-server.svg
%{_datadir}/icons/hicolor/scalable/actions/%{name}*.svg


%files editor
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{name}-editor.desktop
%{_datadir}/pixmaps/%{name}-editor.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-editor.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}-editor.svg

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 15.5-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 15.3-alt1_5
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 15.3-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 15.3-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 15.3-alt1_2
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 15.3-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 14.1-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 14.1-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 14.1-alt1_5
- update to new release by fcimport

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 14.1-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 14.1-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 14.1-alt1_1
- update to new release by fcimport

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt5_3
- fixed build

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt4_3
- rebuild with fixed sourcedep analyser (#27020)

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt3_3
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt2_3
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt1_3
- converted from Fedora by srpmconvert script

