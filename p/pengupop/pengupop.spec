Name:           pengupop
Version:        2.2.2
Release:        alt4_8
Summary:        Networked Game in the vein of Move/Puzzle Bobble

Group:          Games/Other
License:        GPLv2+
URL:            http://www.junoplay.com/pengupop
Source0:        http://www.junoplay.com/files/%{name}-%{version}.tar.gz

BuildRequires:  libSDL-devel zlib-devel desktop-file-utils
Source44: import.info

%description
Finally a networked multiplayer game in the vein of the puzzle classic Bust a
Move/Puzzle Bobble. Beat your friends in this addictive game, or play against
a random opponent! The purpose of this game is to shoot colored orbs into your
playfield, so they form groups of three or more. You win if you manage to
remove all orbs. You lose if any orb attaches below the white line.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags} CFLAGS="$CFLAGS -D_FORTIFY_SOURCE=0" LIBS="-lm"

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp pengupop.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install                             \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
        --add-category X-Fedora                                 \
        pengupop.desktop
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
%doc AUTHORS COPYING
%{_bindir}/pengupop
%{_datadir}/applications/pengupop.desktop
%{_datadir}/icons/hicolor/48x48/apps/pengupop.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt3_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt3_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt2_7
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_7
- converted from Fedora by srpmconvert script

