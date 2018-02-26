# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           flobopuyo
Version:        0.20
Release:        alt4_8
Summary:        2-player falling bubbles game

Group:          Games/Other
License:        GPLv2+
URL:            http://www.ios-software.com/?page=projet&quoi=29
# The upstream source link is a php script that sends the file.  This
# works fine for wget and curl, but confuses rpmbuild when it wants to unpack
# the source tarball.
#Source0:        http://www.ios-software.com/download.php3?what=20151&lg=AN
Source0:        %{name}-%{version}.tgz
Source1:        %{name}.desktop
# Icon converted with icns2png
Source2:        %{name}.png
# Wart
Patch0:         %{name}-0.20-64bit.patch
# Andrea Musuruane
Patch1:         %{name}-0.20-Makefile.patch

BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info


%description
A two-player falling bubbles game.  The goal is to make groups of four or more
Puyos (colored bubbles) to make them explode and send bad ghost Puyos to your
opponent.  You win the game if your opponent reaches the top of the board. You
can play against computer or another human.


%prep
%setup -q
%patch0
%patch1 -p1

# Fix end-of-line-encoding
sed -i 's/\r//' COPYING

# Remove AppleDouble files
rm data/sfx/._bi


%build
export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags} PREFIX=%{_prefix}


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

# Install man page
install -d -m 755 %{buildroot}%{_mandir}/man6
install -m 644 man/%{name}.6 %{buildroot}%{_mandir}/man6

# Install desktop file
desktop-file-install  \
        --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE1}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
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
%doc COPYING TODO Changelog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3_8
- update to new release by fcimport

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3_7
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_7
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_7
- converted from Fedora by srpmconvert script

