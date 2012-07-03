# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           shippy
Version:        1.3.3.7
Release:        alt2_12
Summary:        Space invaders / Galaxians like game with powerups
Group:          Games/Other
License:        GPL+
URL:            http://www.shippysite.com/
Source0:        http://downloads.sourceforge.net/ship84/shipv%{version}UNIX.zip
Source1:        shippy.png
Source2:        shippy.desktop
Source3:        shippy.sh
Patch0:         shippy-merged.patch
BuildRequires:  dumb-devel libSDL_mixer-devel desktop-file-utils
Requires:       %{name}-common = %{version} icon-theme-hicolor
Provides:       %{name}-engine = %{version}
Source44: import.info

%description
Shippy1984 is a small, portable game designed to bring back nostalgia for the
ways games used to be made--addicting as hell! Mash buttons on your way to the
high score! Shippy1984 is designed from the ground up for the avid casual
gamer who feels left behind by the technological overload of today's games!
No longer! Shippy1984 is the game you have been waiting for!


%package allegro
Summary:	Shippy1984 Allegro version
Group:		Games/Other
Requires:	%{name}-common = %{version}
Provides:       %{name}-engine = %{version}

%description allegro
Alternative version of Shippy1984 compiled to use the allegro display library.


%package common
Summary:	Shippy1984 common files
Group:		Games/Other
Requires:       %{name}-engine = %{version}

%description common
Data files, desktop entry and icon, docs and wrapper-script for the
Shippy1984 game.


%prep
%setup -q -c
%patch0 -p1 -z .merged
sed -i 's/\r//' NOTES.txt LICENSE.txt docs/manual.html
mv docs html
#see comment in %%install
rm data/scores.lst


%build
make %{?_smp_mflags} SDL=1 \
 CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DDATADIR=\\\"%{_datadir}/%{name}/\\\"" \
 LDFLAGS="-g `sdl-config --libs` -lSDL_mixer"
mv %{name} %{name}-sdl

make %{?_smp_mflags} ALLEGRO=1 \
 CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DDATADIR=\\\"%{_datadir}/%{name}/\\\"" \
 LDFLAGS="-g -laldmb -ldumb `allegro-config --libs`"
mv %{name} %{name}-allegro


%install
# no make install target so DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 755 %{name}-sdl %{name}-allegro $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -p -m 644 data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
# scores.lst is a binary file which is different on MSB vs LSB, so we just
# create an empty file, then the game will use its identical internal defaults
# and fill it with data in platform format after the first run.
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/games
touch $RPM_BUILD_ROOT%{_var}/lib/games/%{name}.hs

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
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


%files
%attr(2711,root,games) %{_bindir}/%{name}-sdl

%files allegro
%attr(2711,root,games) %{_bindir}/%{name}-allegro

%files common
%doc NOTES.txt LICENSE.txt html
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%config(noreplace) %attr (0664,root,games) %{_var}/lib/games/%{name}.hs


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt1_12
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt1_11
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt1_10
- converted from Fedora by srpmconvert script

