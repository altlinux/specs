# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           qascade
Version:        0.1
Release:        alt2_14
Summary:        Classic puzzle game

Group:          Games/Other
License:        GPLv2+
URL:            http://www.bitsnpieces.org.uk/qascade/
Source0:        http://www.bitsnpieces.org.uk/qascade/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-dblsep.patch

BuildRequires:  libqt3-devel
BuildRequires:  desktop-file-utils
Source44: import.info

%description
Qascade is a port of the simple yet addictive and enjoyable puzzle
game that came with the Psion Revo PDA.


%prep
%setup -q
%patch0


%build
[ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
qmake-qt3 INSTALL_ROOT=$RPM_BUILD_ROOT qascade.pro
perl -pi -e 's|^(C(XX)?FLAGS\s*=.*)$|$1 \$(RPM_OPT_FLAGS)|g' Makefile
make %{?_smp_mflags}


%install
[ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%makeinstall
desktop-file-install \
  --vendor fedora \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  %{SOURCE1}
install -D -p -m 644 %{name}.hscr \
  $RPM_BUILD_ROOT%{_var}/lib/games/%{name}.hscr
install -D -p -m 644 blue.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/qascade.png
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
%doc *.htm
%attr(2711,root,games) %{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/qascade.png
%attr(0664,games,games) %config(noreplace) %{_var}/lib/games/%{name}*


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_14
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_14
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_13
- converted from Fedora by srpmconvert script

