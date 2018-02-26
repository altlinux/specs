# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:		npush
Version:	0.7
Release:	alt2_6
Summary:	A logic game similar to Sokoban

Group:		Games/Other
License:	GPLv2+
URL:		http://npush.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
# patch npush.cpp to fix an issue with level path
Patch0:		npush-0.7-level.patch

BuildRequires:	libncurses-devel desktop-file-utils
Source44: import.info

%description
nPush is a logic game similar to Sokoban and Boulder Dash. 
You need to collect all the gold on the level and reach the exit. 
To make it hard there are some rocks that stand in your way,
and you also have some dynamite to blast them away. 
Main difference from Sokoban, KSokoban and similar games is that you 
can have multiple player-controlled characters you can move on the screen.

nPush is a terminal based application and uses nCurses library for 
user interface.


%prep
%setup -q
%patch0 -p0

# as-needed
sed -i -e 's,-lncurses -o $(PROGRAM) $(OBJECTS),-o $(PROGRAM) $(OBJECTS) -lncurses,' Makefile

%build

make %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}"


%install

mkdir -p  %{buildroot}%{_bindir}
install -p -m 755 npush %{buildroot}%{_bindir}/npush

mkdir -p %{buildroot}%{_datadir}/npush
cp -ra levels*  %{buildroot}%{_datadir}/npush

# desktop file stuff
desktop-file-install  \
	--add-category="LogicGame" \
	--delete-original \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	%{name}.desktop

# icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{name}.png				\
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
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
%doc CHANGES COPYING CREDITS readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_6
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_5
- initial release by fcimport

