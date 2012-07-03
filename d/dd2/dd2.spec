# BEGIN SourceDeps(oneline):
BuildRequires: libSDL-devel
# END SourceDeps(oneline)
Name:           dd2
Version:        0.2.2
Release:        alt2_7
Summary:        Dodgin' Diamond 2 - Shoot'em up arcade game
Group:          Games/Other
License:        GPLv2+
URL:            http://www.usebox.net/jjm/dd2/
Source0:        http://www.usebox.net/jjm/dd2/releases/dd2-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         dd2-0.2.1-glob-highscore.patch
Patch1:         dd2-0.2.1-640x480-fullscreen.patch
BuildRequires:  libSDL_mixer-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
This is a little shoot'em up arcade game for one or two players. It aims to
be an 'old school' arcade game with low resolution graphics, top-down scroll
action, energy based gameplay and different weapons with several levels of
power.


%prep
%setup -q
%patch0 -p1 -z .highscore
%patch1 -p1 -z .fs
#stop autoxxx from rerunning
touch src/data/Makefile.in


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/games
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-hiscore \
  $RPM_BUILD_ROOT%{_var}/games

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(2711,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%config(noreplace) %attr (0664,root,games) %{_var}/games/%{name}-hiscore


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_7
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_6
- converted from Fedora by srpmconvert script

