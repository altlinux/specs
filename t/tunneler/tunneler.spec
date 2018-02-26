Name:           tunneler
Version:        1.1.1
Release:        alt2_8
Summary:        Clone of legendary Tunneler game

Group:          Games/Other
License:        GPLv2+
URL:            http://users.jyu.fi/~tvkalvas/code/tunneler/
Source0:        http://users.jyu.fi/~tvkalvas/code/tunneler/%{name}-%{version}.tar.gz
Source1:        tunneler.svg
Source2:        tunneler.desktop
Patch0:         tunneler-1.1.1-lm.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libSDL-devel
BuildRequires:  autoconf automake
Source44: import.info

%description
A clone of legendary game made by Geoffrey Silverton in 1991. In the game
two players using the same keyboard and the same screen each control an
underground tank. Goal is to find and destroy the opponent's tank. Since
only small part of the map is displayed on the split screen, you might
actually have some searching to do.


%prep
%setup -q
%patch0 -p1 -b .lm


%build
autoreconf -i
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install  %{SOURCE2} \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications
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
%{_bindir}/tunneler
%{_datadir}/icons/hicolor/scalable/apps/tunneler.svg
%{_datadir}/applications/*.desktop
%doc COPYING INSTALL README


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_8
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_7
- converted from Fedora by srpmconvert script

