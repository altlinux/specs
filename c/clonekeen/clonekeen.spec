# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           clonekeen
Version:        0.8.3
Release:        alt2_9
Summary:        "Commander Keen: Invasion of the Vorticons" clone
Group:          Games/Other
License:        GPLv2+
URL:            http://clonekeen.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/CKBeta83_Src.zip
# This are the .dat files and the extra (GPL) levels from 
# http://downloads.sourceforge.net/%{name}/CKBeta83_Bin_W32.zip
# ep1attr.dat and ep3attr.dat are replaced with improved versions from
# http://jonathannielsen.com/mw/CloneKeen2X-1.0-src.zip
# The pristine upstream .zip's aren't used because the included sounds.ck?
# files are property of id Software
Source1:        %{name}-%{version}-data.tar.gz
Source2:        extract.c
Source3:        clonekeen-extract-sounds.c
Source4:        %{name}.sh
Source5:        %{name}.autodlrc
Source6:        %{name}.desktop
Source7:        %{name}.png
Patch0:         %{name}-fixes.patch
Patch1:         %{name}-clonekeen2x-fixes.patch
Patch2:         %{name}-options.patch
Patch3:         %{name}-missing-protos.patch
BuildRequires:  libSDL_mixer-devel libdynamite-devel desktop-file-utils
Requires:       icon-theme-hicolor autodownloader
Source44: import.info

%description
CloneKeen is an almost complete clone of the old classic DOS game,
"Commander Keen: Invasion of the Vorticons" by by id Software:
http://www.idsoftware.com/
CloneKeen requires the original id Software gamedata files to work.

If you posess the original DOS games. You can play all three episodes of the
game. If you don't, you can can still play the shareware episode one. Which can
be freely downloaded from Apogee, but cannot be distributed as a part of
Fedora. When you start CloneKeen for the first time it will offer to download
the shareware datafiles for you.


%prep
%setup -q -a 1 -n keen
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
cp -a %{SOURCE2} %{SOURCE3} .
rm src/scale2x/*.o
sed -i 's/\r//g' readme.txt src/changelog.txt


%build
make %{?_smp_mflags} -C src -f Makefile.lnx CFLAGS="$RPM_OPT_FLAGS"
gcc -o %{name}-extract $RPM_OPT_FLAGS extract.c -ldynamite
gcc -o %{name}-extract-sounds $RPM_OPT_FLAGS %{name}-extract-sounds.c


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/data

install -m 755 src/keen $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -m 755 %{name}-extract $RPM_BUILD_ROOT%{_libexecdir}
install -m 755 %{name}-extract-sounds $RPM_BUILD_ROOT%{_libexecdir}
install -p -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 bin/*.dat  $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 bin/data/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE6}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE7} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps

sed -i s,/usr/libexec,%{_libexecdir},g %buildroot%{_libexecdir}/%{name}* %buildroot%{_bindir}/%{name}
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
%doc readme.txt src/changelog.txt
%{_bindir}/%{name}
%{_libexecdir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt2_9
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_9
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_8
- converted from Fedora by srpmconvert script

