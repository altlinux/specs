# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           scorchwentbonkers
Version:        1.1
Release:        alt2_11
Summary:        Realtime remake of Scorched Earth
Group:          Games/Other
License:        zlib
URL:            http://www.allegro.cc/depot/ScorchWentBonkers
# should be
# http://www.allegro.cc/files/depot/537/%{name}-src-%{version}.tar.gz
# but that is powered by a script which breaks every other day.
Source0:        %{name}-src-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-no-fmod.patch
Patch1:         %{name}-support-16bpp.patch
Patch2:         %{name}-unixify.patch
Patch3:         %{name}-fullscreen.patch
Patch4:         %{name}-divbyzero.patch
Patch5:         %{name}-1.1-al-4.4.patch
BuildRequires:  liballegro-devel liballegro-devel dumb-devel libAllegroOGG-devel
BuildRequires:  libGLU-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
As the name suggests, Scorch Went Bonkers is a remake of the old PC classic.
However, many things were changed and the type of fun delivered by the game is
different. Where Scorched Earth puts emphasis on tactics and careful
calculations, SWB requires quick thinking, perfect timing and only one finger
for controlling your tank. The game is real-time instead of turn based.


%prep
%setup -q -c
%patch0 -p1 -z .no-fmod
%patch1 -p1 -z .16bpp
%patch2 -p1 -z .unix
%patch3 -p1 -z .fs
%patch4 -p1 -z .dbz
%patch5 -p1
sed -i 's/\r//' doc/readme.htm


%build
make %{?_smp_mflags} -f Makefile.linux PREFIX=%{_prefix} \
  OPTFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-non-virtual-dtor"


%install
make -f Makefile.linux install PREFIX=$RPM_BUILD_ROOT%{_prefix}

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
%doc README doc/readme.htm
%{_bindir}/swb
%{_datadir}/swb
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_11
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_10
- initial release by fcimport

