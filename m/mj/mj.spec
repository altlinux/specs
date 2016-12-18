# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install ImageMagick-tools
# END SourceDeps(oneline)
BuildRequires: libkmahjongg4-common
Name:        mj
Version:     1.14
Release:     alt1_9
Summary:     Mah-Jong program with network option
Summary(sv): Mah-Jong-program med nätmöjlighet

Group:       Games/Other
License:     GPLv2+
URL:         http://mahjong.julianbradfield.org/
# Upstreams: http://mahjong.julianbradfield.org/Source/%%name-%%version-src.tar.gz
Source0:     %name-GPL-%version-src.tar.bz2
# The bundled tiles have a non-commercial-use license.  So instead we
# use GPL tiles from kdegames instead.  The solution was suggested by
# Tom 'spot' Callaway in:
# http://lists.fedoraproject.org/pipermail/legal/2010-February/001109.html
# To produce the bundled sources from the upstreams, place them in a directory
# and run the command:
# ./remove-non-GPL.sh %%version
Source1:     remove-non-GPL.sh
Source2:     icon.svg
Patch:	     mj-1.14-crash.patch

BuildRequires: perl
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires: libkmahjongglib4
BuildRequires: inkscape
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils

%global desktopdir %_datadir/applications
%global icontop %_datadir/icons/hicolor
Source44: import.info

%description
This is the game of Mah-Jong, not be confused with the solitaire
matching game using the same tiles.  It is a set of three programs
which provide a networked Mah-Jong system, together with a computer
player.  Thus the game can be played by four humans, by a human and
three computer players, or any other combination.


%description -l sv
Detta är spelet Mah-Jong, inte att förväxla med det patiensliknande
matchningsspelet som använder samma brickor.  Det är en uppsättning
med tre program som utgör ett nätverksbaserat Mah-Jong-system,
tillsammans med en datorspelare.  Spelet kan alltså spelas av fyra
människor, av en människa och tre datorspelare, eller någon
kombination av de två.


%global tiles /usr/share/kde4/apps/kmahjongglib/tilesets/default.svgz
%global gettile() inkscape --without-gui --export-png=tile.png --export-id=%1 --file=%tiles --export-height=37 --export-width=27 --export-background=ivory; convert tile.png -crop 25x35+1+1 %2.xpm;


%prep
%setup -q -n %name-%version-src
%patch
# Convert the kdegames tiles to the format of the bundled ones.
mkdir tiles-kdegames
cd tiles-kdegames
for suit in "BAMBOO B 9" "CHARACTER C 9" "ROD D 9" "FLOWER F 4" "SEASON S 4"
do  set $suit
    for n in $(seq 1 $3)
    do  %gettile $1_$n $n$2
    done
done
%gettile WIND_1 NW
%gettile WIND_2 SW
%gettile WIND_3 EW
%gettile WIND_4 WW
%gettile DRAGON_1 WD
# Pixmap representing the back of a tile.  Use chocolate3 as a bamboo color.
convert WD.xpm -fill chocolate3 -opaque ivory ./--.xpm
# Pixmap used for programming errors.  Use red.  Should never show up.
convert WD.xpm -fill red -opaque ivory XX.xpm
%gettile DRAGON_2 GD
%gettile DRAGON_3 RD
# The "tongs" are ok according to the README file.
cp -p ../tiles-v1/tong* .


%build
make %{?_smp_mflags} FALLBACKTILES=./tiles-kdegames depend
make %{?_smp_mflags} EXTRA_CFLAGS="%optflags" LDLIBS=-lm \
     FALLBACKTILES=./tiles-kdegames
cat << EOF > %name.desktop
[Desktop Entry]
Name=Mah-Jong
GenericName=The game of Mah-Jong
GenericName[sv]=Spelet Mah-Jong
Comment=Play Mah-Jong against the computer or over the network
Comment[sv]=Spela Mah-Jong mot datorn eller över nätet
Exec=xmj
Icon=mj
Terminal=false
Type=Application
Categories=Game;
EOF


%install
make install install.man DESTDIR=%buildroot%_prefix/ MANDIR=share/man/man1 \
     INSTPGMFLAGS=
mkdir %buildroot%desktopdir
desktop-file-install --dir=%buildroot%desktopdir %name.desktop
mkdir -p %buildroot%icontop/scalable/apps
install -m 644 %SOURCE2 %buildroot%icontop/scalable/apps/%name.svg
for res in 16 22 24 32 48 256
do  mkdir -p %buildroot%icontop/${res}x${res}/apps
    inkscape --without-gui \
	     --export-png=%buildroot%icontop/${res}x${res}/apps/%name.png \
	     --file=%SOURCE2 --export-height=$res --export-width=$res
done

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
<!-- Copyright 2014 Your Name <email@address.com> -->
<!--
EmailAddress: mahjong@stevens-bradfield.com
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">mj.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Mahjong game platforms with network capability </summary>
  <description>
    <p>
      Game platforms with network capability game can be played by four humans,
      by a human vs three computer players, or any other combination.
    </p>
  </description>
  <url type="homepage">http://mahjong.julianbradfield.org/</url>
  <screenshots>
    <screenshot type="default">http://mahjong.julianbradfield.org/screenshots/11.gif</screenshot>
  </screenshots>
</application>
EOF

%post
touch --no-create %icontop &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %icontop &>/dev/null

fi

%files
%doc ChangeLog CHANGES LICENCE README rules.txt use.txt
%_bindir/*
%_mandir/man1/*
%{_datadir}/appdata/*.appdata.xml
%desktopdir/%name.desktop
%icontop/*/apps/%name.*


%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_7
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_2
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt4_5
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt4_4
- fc update

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.12-alt4_2
- fixed build

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.12-alt3_2
- fixed build

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.12-alt2_2
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.12-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_2
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_1
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_9
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_8
- converted from Fedora by srpmconvert script

