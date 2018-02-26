# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSM-devel libX11-devel libXext-devel
# END SourceDeps(oneline)
Name:           xgalaxy
Version:        2.0.34
Release:        alt2_16
Summary:        Arcade game: shoot down the space ships attacking the planet
Group:          Games/Other
License:        GPL+
URL:            http://sourceforge.net/projects/xgalaga/
Source0:        http://downloads.sourceforge.net/xgalaga/xgalaga_%{version}.orig.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-hyperspace.desktop
Patch0:         http://ftp.debian.org/debian/pool/main/x/xgalaga/xgalaga_2.0.34-44.diff.gz
Patch1:         %{name}-2.0.34-fullscreen.patch
Patch2:         %{name}-2.0.34-%{name}.patch
Patch3:         %{name}-2.0.34-joy.patch
Patch4:         %{name}-2.0.34-fullscreen-viewport.patch
Patch5:         %{name}-2.0.34-alsa.patch
Patch6:         %{name}-2.0.34-dga-compile-fix.patch
BuildRequires:  libXt-devel libXpm-devel libXmu-devel libXxf86vm-devel
BuildRequires:  libalsa-devel desktop-file-utils ImageMagick
Requires:       icon-theme-hicolor
Obsoletes:      xgalaga <= %{version}
Provides:       xgalaga = %{version}-%{release}
Source44: import.info

%description
Arcade game for the X Window System where you have to shoot down the space
ships attacking the planet.
 

%prep
%setup -q -n xgalaga-%{version}
# many thanks to Debian for all their excellent work on xgalala
%patch0 -p1 -z .deb
%patch1 -p1 -z .fs
%patch2 -p1 -z .%{name}
%patch3 -p1 -z .joy
%patch4 -p1 -z .viewport
%patch5 -p1 -z .alsa
%patch6 -p1 -z .no-dga
sed -e 's/Debian/Fedora/g' debian/README.Debian > README.fedora
cat >> README.fedora << EOF

The latest Fedora %{name} package also includes fullscreen support, start
%{name} with -window to get the old windowed behavior. You can switch on the
fly between window and fullscreen mode with alt+enter.
EOF

# Change the name everywhere as upstreams name has already been used for a game
# much like this one in the past, upstreams use of this is a legal gray area.
sed -i 's/xgalaga/xgalaxy/g' `grep -rls xgalaga .`
sed -i 's/XGalaga/XGalaxy/g' `grep -rls XGalaga .`


%build
sed -i 's,LIBS = @LIBS@ libsprite/libsprite.a @X_LIBS@,LIBS = libsprite/libsprite.a @LIBS@ @X_LIBS@,' Makefile.in
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DXF86VIDMODE"
export X_LIBS=-lXxf86vm
./configure --libdir=%{_libdir} --exec-prefix=%{_bindir} \
  --prefix=%{_datadir}/%{name}
sed -i s/xgal.sndsrv.oss/xgal.sndsrv.alsa/ Makefile
make %{?_smp_mflags} SOUNDLIBS=-lasound
convert images/player3.xpm %{name}.png


%install
make install DESTDIR=$RPM_BUILD_ROOT
# move the sound-server binary out of %{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/xgal.sndsrv.alsa \
  $RPM_BUILD_ROOT%{_bindir}
ln -s ../../bin/xgal.sndsrv.alsa \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/xgal.sndsrv.alsa
# fix useless exec bit
chmod -x $RPM_BUILD_ROOT%{_datadir}/%{name}/*/*
# make install doesn't install the manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 644 xgal.6x $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps
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
%doc CHANGES COPYING README README.fedora
%{_bindir}/%{name}*
%{_bindir}/xgal.sndsrv.alsa
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_16
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt1_16
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt1_15
- initial release by fcimport

