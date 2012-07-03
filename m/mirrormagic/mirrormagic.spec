Name:           mirrormagic
Version:        2.0.2
Release:        alt5_9
Summary:        Puzzle game where you steer a beam of light using mirrors
Group:          Games/Other
License:        GPL+
URL:            http://www.artsoft.org/mirrormagic/
Source0:        http://www.artsoft.org/RELEASES/unix/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-%{version}-fixes.patch
Patch1:         %{name}-%{version}-64bit.patch
Patch2:         %{name}-%{version}-fs-toggle.patch
Patch3:         %{name}-%{version}-highscore.patch
Patch4:         %{name}-%{version}-yesno.patch
BuildRequires:  libSDL_image-devel libSDL_mixer-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
MirrorMagic is a game where you shoot around obstacles to collect energy using
your beam. It is similar to "Mindbender" (Amiga) from the same author. The goal
is to work out how to get around obstacles to shoot energy containers with your
beam, thereby opening the path to the next level. Included are many levels
familiar from the games "Deflektor" and "Mindbender".


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build
make %{?_smp_mflags} RO_GAME_DIR=%{_datadir}/%{name} \
  OPTIONS="$RPM_OPT_FLAGS -DUSE_USERDATADIR_FOR_COMMONDATA" sdl


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a graphics levels music sounds $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
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
%doc CHANGES COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt4_9
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt4_8
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_8
- rebuild with new rpm desktop cleaner

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_8
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_8
- converted from Fedora by srpmconvert script

