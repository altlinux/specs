# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/adonthell python-devel
# END SourceDeps(oneline)
Name:           wastesedge
Version:        0.3.4
Release:        alt2_0.17
Summary:        Official game package for Adonthell

Group:          Games/Other
License:        GPL+
URL:            http://adonthell.linuxgames.com/
## Due to legal issues (RHBZ#477481), upstream sources need to be modified
# Here is how are obtained the sources used in this package:
# $ wget http://savannah.nongnu.org/download/adonthell/%{name}-src-%{version}.tar.gz
# $ tar xzvf %{name}-src-%{version}.tar.gz
# $ rm %{name}-%{version}/gfx/window/font/avatar.ttf
# $ sed -i 's|avatar.ttf||g' %{name}-%{version}/gfx/window/font/Makefile.in
# $ tar czvf %{name}-src-%{version}-modified.tar.gz %{name}-%{version}/
Source0:        %{name}-src-%{version}-modified.tar.gz
Source1:        %{name}.desktop
Patch0:         %{name}-more.patch
BuildArch:      noarch

BuildRequires:  adonthell >= %{version}
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
Requires:       adonthell >= %{version}-%{release}
Requires:       icon-theme-hicolor
Source44: import.info


%description
As a loyal servant of the elven Lady Silverhair, you arrive at the remote
trading post of Waste's Edge, where she is engaged in negotiations with the
dwarvish merchant Bjarn Fingolson. But not all is well at Waste's Edge, and
soon you are confronted with circumstances that are about to destroy your
mistress' high reputation. And you are the only one to avert this ...


%prep
%setup -q
# fix wrong file permissions (fixed upstream for future release)
chmod a-x AUTHORS COPYING INSTALL README
# install locale files in the right place
sed -i 's|datadir = @gamedatadir@|datadir = ${prefix}/share|' po/Makefile.in.in
# patch configure to not use "more" any more
%patch0 -p0


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# install images in the correct folders
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32}/apps
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}_16x16.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}_32x32.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

# install desktop file not provided upstream
desktop-file-install --vendor=""                      \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        %{SOURCE1}
%find_lang %{name}
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


%files -f %{name}.lang
%doc AUTHORS COPYING PLAYING README
%{_bindir}/adonthell-%{name}
%{_datadir}/adonthell/games/%{name}/
%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt2_0.17
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_0.17
- update to new release by fcimport

* Sat Jul 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_0.16
- initial release by fcimport

