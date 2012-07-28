# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/convert /usr/bin/pngtopnm /usr/bin/rsvg-convert /usr/bin/scrollkeeper-config pkgconfig(avahi-client) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(libnotify)
# END SourceDeps(oneline)
Name:           pioneers
Version:        14.1
Release:        alt1_2
Summary:        Turnbased board strategy game (colonize an island)
Group:          Games/Other
License:        GPLv2+
URL:            http://pio.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pio/%{name}-%{version}.tar.gz
Patch0:         pioneers-14.1-sanitize.patch
Patch1:		pioneers-0.12.3-dso.patch
BuildRequires:  libgnome-devel gtk2-devel gettext scrollkeeper intltool
BuildRequires:  perl(XML/Parser.pm) desktop-file-utils
Requires:       icon-theme-hicolor
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Source44: import.info

%description
Pioneers is a computerized version of a well known strategy board game. The
goal of the game is to colonize an island. The players play the first
colonists hence the name pioneers.

Pioneers is a networkbased multiplayer game, this package contains the GUI
client as well as both a GUI and CLI version of the server for local games.


%package editor
Summary:        Pioneers Game Editor
Group:          Games/Other
Requires:       pioneers = %{version}-%{release}

%description editor
Pioneers is a computerized version of a well known strategy board game. The
goal of the game is to colonize an island. The players play the first
colinists hence the name pioneers.

The game editor allows maps and game descriptions to be created and
edited graphically.


%prep
%setup -q
#%patch0 -p1 -z .sanitize
%patch1 -p1 -z .dso
	

%build
# pioneers uses some GNU extensions
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

# Remove the too much like the original splashscreen
rm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}/splash.png

# Reinstall the .desktop files
desktop-file-install  --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-editor.desktop \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-server.desktop
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
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


%check
if grep Catan `find $RPM_BUILD_ROOT ! -path "$RPM_BUILD_ROOT/usr/src/debug*"`;
  then
  exit 1
fi


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README NEWS
%{_bindir}/%{name}
%{_bindir}/%{name}ai
%{_bindir}/%{name}-meta-server
%{_bindir}/%{name}-server-console
%{_bindir}/%{name}-server-gtk
%{_datadir}/games/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/omf/%{name}
%{_datadir}/gnome/help/%{name}
%{_mandir}/man6/%{name}*.6.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-server.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-server.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-server.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-server.svg

%files editor
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{name}-editor.desktop
%{_datadir}/pixmaps/%{name}-editor.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-editor.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}-editor.svg

%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 14.1-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 14.1-alt1_1
- update to new release by fcimport

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt5_3
- fixed build

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt4_3
- rebuild with fixed sourcedep analyser (#27020)

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt3_3
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt2_3
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt1_3
- converted from Fedora by srpmconvert script

