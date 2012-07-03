Name:           egoboo-data
Version:        2.7.5
Release:        alt2_8
Summary:        Data files for the Egoboo RPG
Group:          Games/Other
License:        GPL+
URL:            http://egoboo.sourceforge.net/
# This is http://downloads.sourceforge.net/egoboo/egoboo-data-2.7.5.tar.gz
# with the non free fonts removed
Source0:        %{name}-clean-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildArch:      noarch
# dejavu gets used as a replacement for the non free fonts
Requires:       fonts-ttf-dejavu icon-theme-hicolor
# so that we get uninstalled together with egoboo
Requires:       egoboo >= %{version}
Source44: import.info

%description
Data files for the Egoboo RPG. 


%prep
%setup -q
sed -i 's/\r//' Changelog.txt Readme.txt
rm -r modules/firedom.mod/objects/*.obj/CVS


%build
convert basicdat/icon.bmp -transparent '#c8c8c8' egoboo.png


%install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/egoboo
cp -a controls.txt setup.txt basicdat modules players \
  $RPM_BUILD_ROOT%{_datadir}/egoboo
ln -s ../../fonts/ttf/dejavu/DejaVuSans.ttf \
  $RPM_BUILD_ROOT%{_datadir}/egoboo/basicdat/Negatori.ttf

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -m 644 egoboo.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
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
%doc *.pdf Changelog.txt Readme.txt
%{_datadir}/egoboo
%{_datadir}/icons/hicolor/64x64/apps/egoboo.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_8
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_7
- converted from Fedora by srpmconvert script

