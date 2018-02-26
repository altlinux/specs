Name:           worminator
Version:        3.0R2.1
Release:        alt2_15
Summary:        Sidescrolling platform and shoot'em up action-game
Group:          Games/Other
License:        GPLv2+
URL:            http://sourceforge.net/projects/worminator/
Source0:        http://downloads.sourceforge.net/worminator/worminator-%{version}.tar.gz
Source1:        worminator.png
Source2:        worminator.desktop
Patch0:         worminator-3.0R2.1-speed.patch
BuildRequires:  liballegro-devel desktop-file-utils
Requires:       worminator-data >= 3.0R2.1-2 icon-theme-hicolor
Source44: import.info

%description
You play as The Worminator and fight your way through many levels of madness
and mayhem. Worminator features nine unique weapons, visible character damage,
full screen scrolling, sound and music, and much more!


%prep
%setup -q
%patch0 -p1 -z .speed
sed -i 's/\r//' ReadMe.txt


%build
gcc $RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations \
  -Wno-char-subscripts -DDATADIR=\"%{_datadir}/%{name}/\" -o %{name} \
  Worminator.c `allegro-config --libs` -lm


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install                             \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE2}
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
%doc ReadMe.txt changes.unix license.txt license-change.txt
%{_bindir}/%{name}
%{_datadir}/applications/worminator.desktop
%{_datadir}/icons/hicolor/32x32/apps/worminator.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_15
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt1_15
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt1_14
- update to new release by fcimport

* Thu May 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0R2.1-alt1_13.1
- fix build

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt1_13
- converted from Fedora by srpmconvert script

