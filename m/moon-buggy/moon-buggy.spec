# Enable oldstyle to have a nearly nothing requiring package after rebuilding
%define oldstyle 0

Summary:         Drive and jump with some kind of car across the moon
Name:            moon-buggy
Version:         1.0.51
Release:         alt2_6
License:         GPL+
Group:           Games/Other
URL:             http://seehuhn.de/pages/%{name}
Source0:         http://seehuhn.de/media/programs/%{name}-%{version}.tar.gz
Source1:         http://seehuhn.de/media/programs/%{name}-sound-%{version}.tar.gz
Source2:         %{name}.desktop
Source3:         %{name}-sound.desktop
Patch0:          moon-buggy-1.0.51-pause.patch
Patch1:          moon-buggy-1.0.51-sound.patch
BuildRequires:   libncurses-devel
%if !%{oldstyle}
BuildRequires:   esound-devel desktop-file-utils autoconf automake
%endif
Source44: import.info

%description
Moon-buggy is a simple character graphics game where you drive some kind
of car across the moon's surface. Unfortunately there are dangerous craters
there. Fortunately your car can jump over them! 

The game has some resemblance of the classic arcade game moon-patrol which
was released in 1982. A clone of this game was relased for the Commodore
C64 in 1983. The present, ASCII art version of moon-buggy was written many
years later by Jochen Voss.

%prep
%setup -q -a 1
%patch0 -p1 -b .pause
%if !%{oldstyle}
%patch1 -p1 -b .sound
mv -f %{name}-%{version}/* .
autoreconf -f
%endif

%build
%configure --sharedstatedir=%{_var}/games
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

# Create zero-sized highscore file
touch $RPM_BUILD_ROOT%{_var}/games/%{name}/mbscore

# Install working *.desktop files and an icon
%if !%{oldstyle}
desktop-file-install --vendor "" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
desktop-file-install --vendor "" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}

install -D -p -m 644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%endif

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o ChangeLog.utf8 ChangeLog
sed -i 's|\r$||g' ChangeLog.utf8
touch -c -r ChangeLog ChangeLog.utf8
mv -f ChangeLog.utf8 ChangeLog

iconv -f iso-8859-1 -t utf-8 -o TODO.utf8 TODO
sed -i 's|\r$||g' TODO.utf8
touch -c -r TODO TODO.utf8
mv -f TODO.utf8 TODO
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
%doc ANNOUNCE AUTHORS ChangeLog COPYING README THANKS
%if !%{oldstyle}
%doc README.sound
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-sound.desktop
%endif
%attr(2711,root,games) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_infodir}/%{name}.info.*
%attr(0775,root,games) %{_var}/games/%{name}
%verify(not md5 size mtime) %config(noreplace) %attr(664,root,games) %{_var}/games/%{name}/mbscore

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt1_6
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt1_5
- converted from Fedora by srpmconvert script

