# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           magicmaze
Version:        1.0.2
Release:        alt2_7
Summary:        Board game featuring a maze which the players change each turn
Group:          Games/Other
License:        zlib and Redistributable, no modification permitted
URL:            http://www.helixsoft.nl/project_page.php?file_name=magicmaze.proj
Source0:        http://www.helixsoft.nl/download/%{name}-%{version}_src.tar.gz
Source1:        %{name}.desktop
Patch0:         maze-1.0-gcc4.patch
Patch1:         maze-1.0-no-sound.patch
Patch2:         maze-1.0-fhs.patch
Patch3:         magicmaze-1.0.2-license-clarification.patch
Patch4:         magicmaze-1.0.2-trademarks.patch
BuildRequires:  libgstream-devel dumb-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
The board of the game is a complicated maze. You see reddish squares, which are
walls, and black lanes, which are walkable. Also you see brightly coloured
(humanoid) figures and little circles. The figures are the players, and the
rounds are coins which the players must collect.

Each player gets a turn. In the beginning of your turn, you get to change the
maze. You can see a small piece of maze "sticking out" of the board. You can
make that piece move around the board an rotate it. When you are done the
piece is pushed in the maze, thus making a whole column or row of the maze
shift. If you do this in a clever way, new passages open up, hopefully leading
you to a coin in your players color.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
chmod -x `find -type f`


%build
make %{?_smp_mflags} -f makefile.unx PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations -I/usr/include/gstream"


%install
make -f makefile.unx install PREFIX=$RPM_BUILD_ROOT%{_prefix}

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
%doc license.txt docs/readme.txt docs/todo.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_7
- update to new release by fcimport

* Thu Jul 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_6
- initial release by fcimport

