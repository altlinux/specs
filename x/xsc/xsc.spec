# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libICE-devel libSM-devel
# END SourceDeps(oneline)
Name: xsc
Version:  1.5
Release:  alt2_7
Summary: A clone of the old vector graphics video game Star Castle

Group: Games/Other
License: GPLv2        
URL: http://www.panix.com/~mbh/projects.html
Source0: http://www.panix.com/~mbh/xsc/xsc-%{version}.tar.gz
Source1: xsc.desktop
Source2: xsc.png
BuildRequires: desktop-file-utils libX11-devel
Requires: icon-theme-hicolor
Source44: import.info

%description
The object is to blast a hole in the rings and destroy the enemy ship.
The only problem is that it tracks your every move and as soon as you 
knock a hole in all three rings, and they all line up, it lets loose  
with the big nasty green fireballs.  Avoid them.  Avoid the little green
buzzers, too.  Shoot 'em if you want.

%prep
%setup -q

%build

%configure --x-includes="" --x-libraries=""
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p  %{buildroot}%{_bindir}
install -m 755 xsc %{buildroot}%{_bindir}/xsc

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
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
%{_bindir}/xsc
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_datadir}/applications/xsc.desktop
%{_datadir}/icons/hicolor/32x32/apps/xsc.png

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_6
- converted from Fedora by srpmconvert script

