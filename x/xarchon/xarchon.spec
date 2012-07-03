# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libICE-devel libSM-devel libesd-devel
# END SourceDeps(oneline)
Name:           xarchon
Version:        0.50
Release:        alt2_12.1
Summary:        Arcade board game
Group:          Games/Other
License:        GPL+
URL:            http://xarchon.seul.org/
Source0:        http://xarchon.seul.org/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         %{name}-fonts.patch
Patch1:         %{name}-destdir.patch
Patch2:         http://ftp.debian.org/debian/pool/main/x/%{name}/%{name}_0.50-10.1.diff.gz
Patch3:         xarchon-0.50-gcc43.patch
Patch4:         xarchon-0.50-alt-DSO.patch
BuildRequires:  gtk+-devel esound-devel libXpm-devel
BuildRequires:  desktop-file-utils ImageMagick
Requires:       icon-theme-hicolor
Source44: import.info

%description
XArchon is a chess with a twist board game.


%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p2


%build
%configure
make %{?_smp_mflags}
convert data/icon.xpm %{name}.png


%install
make install DESTDIR=$RPM_BUILD_ROOT

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png \
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
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_mandir}/man6/%{name}.6.*


%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.50-alt2_12.1
- Fixed build

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_12
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_11
- converted from Fedora by srpmconvert script

