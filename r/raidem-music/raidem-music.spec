Name:           raidem-music
Version:        1.0
Release:        alt2_6
Summary:        Background music for the game raidem
Group:          Games/Other
License:        CC-BY
URL:            http://www.dilvie.com/
Source0:        http://www.dilvie.com/music/dilvie_-_the_dragonfly.ogg
# transcoded from: http://www.dilvie.com/music/dilvie_-_up_in_ashes.mp3
Source1:        dilvie_-_up_in_ashes.ogg
Source2:	http://www.dilvie.com/music/dilvie_-_half_baked.ogg
Source3:        http://www.dilvie.com/music/dilvie_-_east_of_the_sun.ogg
Source4:        license.txt
Buildarch:      noarch
Requires:       raidem >= 0.3.1
Source44: import.info

%description
Music created by Eric Hamilton (dilvie) for the game Raid'em


%prep
%setup -q -c -T
cp %{SOURCE4} .


%build
# nothing todo content only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/menu
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/raidem/music/menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level1
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level2
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level2
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level3
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level3
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
%doc license.txt
%{_datadir}/raidem/music


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- initial release by fcimport

