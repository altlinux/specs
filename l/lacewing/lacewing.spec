# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           lacewing
Version:        1.10
Release:        alt2_17
Summary:        Arcade-style shoot-em-up
Group:          Games/Other
License:        GPLv2+
URL:            http://users.olis.net.au/zel/
Source0:        http://users.olis.net.au/zel/lwsrc.zip
Source1:        http://users.olis.net.au/zel/lwdata.zip
Source2:        lacewing.desktop
Source3:        lacewing.png
Patch0:         lacewing.patch
Patch1:         lacewing-fullscreen.patch
Patch2:         lacewing-nicecpu.patch
Patch3:         lacewing-warn.patch
BuildRequires:  liballegro-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info
Patch33: lacewing-1.10-alt-as-needed.patch

%description
Arcade-style shoot-em-up where you can choose a type of ship and depending on
the type of ship can pickup a number of upgrades during the game.

Lacewing is an arcade-style shoot-em-up which plays a little bit like a cross
between Spacewar and Centipede. It has a decidedly retro style to it. It has
a single-player mode, and also co-operative and duel modes for two players
(split-screen).


%prep
%setup -q -c
unzip -qqo %{SOURCE1}
%patch0 -p1 -z .unix
%patch1 -p1 -z .fullscreen
%patch2 -p1 -z .nicecpu
%patch3 -p1 -z .warn
sed -i 's/\r//' readme.txt licence.txt
chmod 644 readme.txt licence.txt
%patch33 -p1


%build
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations"


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
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
%doc readme.txt licence.txt
%{_bindir}/lacewing
%{_datadir}/lacewing
%{_datadir}/applications/lacewing.desktop
%{_datadir}/icons/hicolor/48x48/apps/lacewing.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_17
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_17
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_16
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_15
- initial release by fcimport

