Summary(sv): Mah-Jong-program med nätmöjlighet
Summary(sv): Mah-Jong-program med nätmöjlighet
Summary(sv): Mah-Jong-program med nätmöjlighet
Summary(sv): Mah-Jong-program med nätmöjlighet
Summary(sv): Mah-Jong-program med nätmöjlighet
Name:        mj
Version:     1.12
Release:     alt2_1
Summary:     Mah-Jong program with network option
Summary(sv): Mah-Jong-program med nätmöjlighet

Group:       Games/Other
License:     GPLv2+
URL:         http://mahjong.julianbradfield.org/
# Upstreams: http://mahjong.julianbradfield.org/Source/%name-%version-src.tar.gz
Source0:     %name-GPL-%version-src.tar.bz2
# The bundled tiles have a non-commercial-use license.  So instead we
# use GPL tiles from kdegames instead.  The solution was suggested by
# Tom 'spot' Callaway in:
# http://lists.fedoraproject.org/pipermail/legal/2010-February/001109.html
# To produce the bundled sources from the upstreams, place them in a directory
# and run the command:
# ./remove-non-GPL.sh %version
Source1:     remove-non-GPL.sh

BuildRequires: perl
BuildRequires: libgtk+2-devel
BuildRequires: kde4games
BuildRequires: inkscape
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils

%global desktopdir %_datadir/applications
%global icontop %_datadir/icons/hicolor
%global icondir %icontop/32x32/apps
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
%global gettile() inkscape --without-gui --export-png=tile.png --export-id=%1 --file=tiles.svg --export-height=37 --export-width=27 --export-background=ivory; convert tile.png -crop 25x35+1+1 %2.xpm;


%prep
%setup -q -n %name-%version-src
# Convert the kdegames tiles to the format of the bundled ones.
mkdir tiles-kdegames
cd tiles-kdegames
# For some reason I can't figure out, inkscape fails to uncompress the svgz
# file when run in a mock chroot.  When I run on the command line it works
# fine.  To work around, I uncompress the svgz file in a separate step.
zcat %tiles > tiles.svg
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
%gettile DRAGON_2 GD
%gettile DRAGON_3 RD
# Pixmap representing the back of a tile.  Use chocolate3 as a bamboo color.
convert WD.xpm -fill chocolate3 -opaque ivory ./--.xpm
# Pixmap used for programming errors.  Use red.  Should never show up.
convert WD.xpm -fill red -opaque ivory XX.xpm
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
mkdir -p %buildroot%icondir
convert icon.ico %buildroot%icondir/%name.png
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz afm pfa pfb; do
    case "$fontpatt" in 
	pcf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi


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
%desktopdir/%name.desktop
%icondir/%name.png


%changelog
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

