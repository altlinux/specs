# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/scrollkeeper-config pkgconfig(gthread-2.0)
# END SourceDeps(oneline)
Name:           quarry
Version:        0.2.0
Release:        alt5_9
Summary:        A multi-purpose board game GUI

Group:          Games/Other
License:        GPLv2+
URL:            http://home.gna.org/quarry/
Source0:        http://download.gna.org/quarry/quarry-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  librsvg-devel
BuildRequires:	libgtk+2-devel
BuildRequires:  scrollkeeper
#Requires:       
Requires(post):         scrollkeeper
Requires(postun):       scrollkeeper
Source44: import.info

%description
Quarry is a multi-purpose GUI for several board games, at present Go, Amazons
and Reversi. It allows users to play against computer players (third-party
programs, e.g. GNU Go or GRhino) or other humans, view and edit game records.
Future versions will also support Internet game servers and provide certain
features for developers of board game-playing engines for enhancing their
programs.

%prep
%setup -q


%build
%configure --disable-scrollkeeper-update
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# desktop file
desktop-file-install  \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --remove-key Version \
    --delete-original \
    $RPM_BUILD_ROOT%{_datadir}/applications/quarry.desktop

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
%doc AUTHORS ChangeLog COPYING COPYING-DOC NEWS README THANKS TODO
%{_bindir}/quarry
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/quarry.xml
%{_datadir}/pixmaps/quarry.png
%{_datadir}/omf/quarry/
%{_datadir}/quarry/


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_9
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_7
- rebuild with new rpm desktop cleaner

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_7
- rebuild with new librsvg

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_7
- converted from Fedora by srpmconvert script

