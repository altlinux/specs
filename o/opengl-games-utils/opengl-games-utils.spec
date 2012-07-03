Name:           opengl-games-utils
Version:        0.2
Release:        alt2_2
Summary:        Utilities to check proper 3d support before launching 3d games
Group:          Games/Other
License:        Public Domain
URL:            http://fedoraproject.org/wiki/SIGs/Games
Source0:        opengl-game-wrapper.sh
Source1:        opengl-game-functions.sh
Source2:        README
BuildArch:      noarch
Requires:       zenity xdriinfo glxinfo
Source44: import.info

%description
This package contains various shell scripts which are intented for use by
3D games packages. These shell scripts can be used to check if direct rendering
is available before launching an OpenGL game. This package is intended for use
by other packages and is not intended for direct end user use!


%prep
%setup -c -T
cp %{SOURCE2} .


%build
# nothing to build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}
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
%doc README
%{_bindir}/opengl-game-wrapper.sh
%{_datadir}/%{name}


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_2
- update to new release by fcimport

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_1
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_10
- converted from Fedora by srpmconvert script

