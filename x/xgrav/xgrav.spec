Name: xgrav
Version:  1.2.0
Release:  alt2_10
Summary: A simple physics simulation for a large number of particles

Group: Games/Other
License: GPLv2+
URL: http://aass.oru.se/~mbl/xgrav/
Source0: http://www.aass.oru.se/~mbl/xgrav/xgrav-%{version}.tgz
Source1: xgrav.desktop
#Created from screenshot of example1.g run.
Source2: xgrav.png
BuildRequires: desktop-file-utils libSDL-devel flex zlib-devel
Requires: icon-theme-hicolor
Source44: import.info

%description
X-Grav simulates the effect of gravity, collisions, heat dissipation and
a simple chemical reaction. The simulation is in no way meant to be 
realistic but rather a toy with which you can create stars, planets 
and even simple solar systems.

%prep
%setup -qn xgrav

chmod -x COPYING

%build

make LINUX_CFLAGS="-c $RPM_OPT_FLAGS `pkg-config --cflags sdl` \
-DWITH_ROOTWINDOW" LINUX_LDFLAGS="$RPM_OPT_FLAGS `pkg-config \
--libs sdl` -lGL `pkg-config --libs x11` -lm"

%install
mkdir -p  %{buildroot}%{_bindir}
install -m 755 xgrav %{buildroot}%{_bindir}/xgrav

mkdir -p  %{buildroot}%{_datadir}/xgrav
install -p -m 644 example* %{buildroot}%{_datadir}/xgrav

sed 's;/usr/share;%_datadir;' %{SOURCE1} > xgrav.desktop

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install             \
  --dir %{buildroot}%{_datadir}/applications \
  xgrav.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
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
%doc COPYING documentation.html README README.html TODO VERSION
%{_bindir}/xgrav
%{_datadir}/xgrav
%{_datadir}/applications/xgrav.desktop
%{_datadir}/icons/hicolor/32x32/apps/xgrav.png

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_10
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_10
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_9
- converted from Fedora by srpmconvert script

