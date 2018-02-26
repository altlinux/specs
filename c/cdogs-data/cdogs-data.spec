# upstream does data releases with a year-month-day versioning scheme, however
# this releases always coincide with a cdogs-sdl release, so since rpm handles
# year-month-day versioning scheme's badly I've decided to use the matching
# cdogs-sdl release version
%define cdogs_sdl_version 0.4
%define cdogs_data_version 2007-07-06

Name:           cdogs-data
Version:        %{cdogs_sdl_version}
Release:        alt2_7
Summary:        Data files for the CDogs game
Group:          Games/Other
License:        Redistributable, no modification permitted
URL:            http://lumaki.com/code/cdogs/
Source0:        http://icculus.org/cdogs-sdl/files/data/%{name}-%{cdogs_data_version}.tar.bz2
BuildArch:      noarch
Requires:       cdogs-sdl >= %{cdogs_sdl_version} icon-theme-hicolor
Source44: import.info

%description
Data files for the CDogs game.


%prep
# nothing to prep


%build
# nothing to build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
tar xj --strip-components=1 -f %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/cdogs_icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/cdogs.png
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/cdogs?icon.*
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
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/cdogs.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_6
- converted from Fedora by srpmconvert script

