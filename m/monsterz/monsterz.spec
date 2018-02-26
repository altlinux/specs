Name:           monsterz
Version:        0.7.1
Release:        alt2_8
Summary:        Puzzle game, similar to Bejeweled or Zookeeper
Group:          Games/Other
License:        WTFPL
URL:            http://sam.zoy.org/monsterz/
Source0:        http://sam.zoy.org/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.score
Patch0:         %{name}-0.7.1-userpmopts.patch
Patch1:         %{name}-0.7.1-64bitfix.patch
Patch2:         %{name}-0.7.1-blit-crash.patch
BuildRequires:  desktop-file-utils
Requires:       python-module-pygame
Requires:       icon-theme-hicolor
Provides:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-data < 0.7.1
Source44: import.info

%description
Monsterz is a little arcade puzzle game, similar to the famous Bejeweled or
Zookeeper. The goal of the game is to create rows of similar monsters, either
horizontally or vertically. The only allowed move is the swap of two adjacent
monsters, on the condition that it creates a row of three or more. When
alignments are cleared, pieces fall from the top of the screen to fill the
board again. Chain reactions earn you even more points.


%prep
%setup -q
%patch0 -p1
%ifarch x86_64 ppc64
%patch1 -p1
%endif
%patch2 -p0


%build
make %{?_smp_mflags} prefix=%{_usr} datadir=%{_datadir} pkgdatadir=%{_datadir}/%{name} CFLAGS="%{optflags}"

# Build desktop icon
cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Monsterz
GenericName=Monsterz Puzzle Game
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF


%install
# Bypass make install as it requires root priviledges and the SRPM
# may not necessarily be built as root
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/{applications,icons/hicolor/64x64/apps}
mkdir -p %{buildroot}%{_datadir}/%{name}/{graphics,sound}
mkdir -p %{buildroot}%{_var}/games
install -pm0755 %{name} %{buildroot}%{_bindir}
install -pm0755 %{name}.py %{buildroot}%{_datadir}/%{name}
cp -a graphics/* %{buildroot}%{_datadir}/%{name}/graphics
cp -a sound/* %{buildroot}%{_datadir}/%{name}/sound

install -pm0664 %{SOURCE1} %{buildroot}%{_var}/games/%{name}

desktop-file-install  \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop

install -pm0644 graphics/icon.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
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
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/%{name}
%attr(2711,root,games) %{_bindir}/%{name}
%attr(-,root,games) %config(noreplace) %{_var}/games/%{name}
%doc AUTHORS COPYING README TODO


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_8
- update to new release by fcimport

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.1-alt1_7.1
- Rebuild with Python-2.7

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_7
- converted from Fedora by srpmconvert script

