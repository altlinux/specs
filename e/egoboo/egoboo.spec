Name:           egoboo
Version:        2.7.5
Release:        alt2_11
Summary:        A top down graphical (3D) RPG in the spirit of Nethack
Group:          Games/Other
License:        GPLv3
URL:            http://egoboo.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        KNOWN-BUGS.txt
Patch0:         %{name}-2.7.5-unix.patch
Patch1:         %{name}-2.4.3-opengl-wrapper.patch
BuildRequires:  libSDL_mixer-devel libSDL_ttf-devel libSDL_image-devel libenet-devel
BuildRequires:  desktop-file-utils
Requires:       %{name}-data = %{version} opengl-games-utils
Source44: import.info

%description
Egoboo is a top down rpg in the spirit of Nethack and other games of the
Roguelike genre. It uses OpenGL graphics and will have randomly generated
maps and customizable characters. The objective of the project is to bring the
fun and depth of roguelike gameplay, kicking and screaming, into the third
dimension.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp -a %{SOURCE2} .
sed -i 's/\r//g' game/change.log game/Egoboodoc.txt
iconv -f ISO-8859-1 -t UTF8 game/change.log > ChangeLog


%build
# We override ENET_OBJ and LDFLAGS to use the system enet
make -C game -f Makefile.unix ENET_OBJ= \
  CFLAGS="$RPM_OPT_FLAGS `sdl-config --cflags` -DENET11" \
  LDFLAGS="`sdl-config --libs` -lSDL_ttf -lSDL_mixer -lSDL_image -lGL -lGLU -lenet -lm"


%install
make -C game -f Makefile.unix ENET_OBJ= PREFIX=$RPM_BUILD_ROOT%{_prefix} \
  install

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
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
# note the end-users docs are in the -data package
%doc ChangeLog game/Egoboodoc.txt KNOWN-BUGS.txt
%{_bindir}/%{name}
/usr/libexec/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt2_11
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_11
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_10
- converted from Fedora by srpmconvert script

