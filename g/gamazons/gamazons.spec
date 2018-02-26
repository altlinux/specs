Name:           gamazons
Version:        0.83
Release:        alt4_8
Summary:        GNOME Amazons

Group:          Games/Other
License:        GPLv2
URL:            http://www.yorgalily.org/gamazons/
Source0:        http://www.yorgalily.org/gamazons/src/gamazons-%{version}.tar.gz

BuildRequires:  libgnomeui-devel desktop-file-utils
Source44: import.info

%description
Amazons is a game played on a 10x10 chess board. Each side has four
pieces (amazons) that move like chess queens (in a straight line in
any direction). Instead of capturing pieces like in chess, the game is
determined based on who moves last.

Each move consists of two parts. First an amazon moves to a new square
and then fires an arrow to another square (the arrow is fired in a
straight line in any direction from the square the amazon landed
on). The square the arrow lands on becomes a permenant block for the
rest of the game. No one can move over it, or fire an arrow over
it. Every turn an amazon must move and fire an arrow, so every turn
there is one less square available on the board. Try and block in your
opponent or section off a good chunk of the board for yourself.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install  \
                     --delete-original \
                     --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ \
                     --remove-key=OnlyShowIn \
  $RPM_BUILD_ROOT%{_datadir}/applications/gamazons.desktop
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
%doc COPYING src/gamazon.bugs src/thots
%{_bindir}/gamazons
%{_datadir}/applications/gamazons.desktop
%{_datadir}/gnome/help
%{_datadir}/gamazons
%{_datadir}/pixmaps/gamazons
%{_datadir}/pixmaps/gnome-gamazons.png



%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.83-alt3_8
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.83-alt3_7
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.83-alt3_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.83-alt2_6
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1_6
- converted from Fedora by srpmconvert script

