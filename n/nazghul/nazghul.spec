# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libSDL-devel perl(FileHandle.pm) perl(SDL/Rect.pm) perl(SDL/Surface.pm)
# END SourceDeps(oneline)
Name:           nazghul
Version:        0.7.1
Release:        alt2_3.20120228gitb0a402a
Summary:        A computer role-playing game (CRPG) engine

License:        GPLv2+
URL:            http://myweb.cableone.net/gmcnutt/nazghul.html
Group:          Games/Other

# Occasionally upstream names things with an underscore.
%define         version_us %(echo %{version} | sed -e 's/\\./_/g')

#Source0:        nazghul-20120228gitb0a402a.txz

# Construct cvs checkout tarball with:
#  ./nazghul-make-snapshot %{cvsdate}
Source0:        nazghul-20120228gitb0a402a.txz
Source1:        haxima-music-license
Patch0:         nazghul-desktop.patch

# For building from a CVS snapshot
BuildRequires:  automake autoconf
BuildRequires:  libSDL_image-devel libSDL_mixer-devel desktop-file-utils libpng-devel
Source44: import.info

%description
Nazghul is an old-school RPG engine modeled after those made in the
heyday of top-down, 2d tile-based graphics. It is specifically modeled
after Ultima V.


%package -n haxima
Summary:        A full-featured role-playing game for the Nazghul engine
# The music files installed in /usr/share/nazghul/haxima/music have been
# relicensed as CC-BY-SA (specifically version 2).   See the
# haxima-music-license file for details. The rest of the package is GPLv2+.
License:        GPLv2+ and CC-BY-SA
Group:          Games/Other
Requires:       nazghul = %{version}
Provides:       nazghul-haxima = %{version}-%{release}
Obsoletes:      nazghul-haxima < 0.6.0-8

%description -n haxima
A complete, playable and full-featured role playing game which runs
under the Nazghul CRPG engine.

You must install Nazghul in order to play Haxima.


%prep
%setup -q -n %{name}
%patch0 -b .orig

# clean up CVS directories left in the source tarball
find . -depth -type d -name CVS -exec rm -rf {} \;

# Fix line endings
sed -i -e 's/\r//' doc/engine_extension_and_design/my_TODO.2004.05.05.txt

mv doc/* .

cp %SOURCE1 .


%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

mv %{buildroot}/%{_bindir}/haxima.sh %{buildroot}/%{_bindir}/haxima

desktop-file-install             \
    --dir %{buildroot}/%{_datadir}/applications \
    --add-category X-Fedora                     \
    haxima.desktop

install -D -m 644 icons/haxima.png %{buildroot}/%{_datadir}/pixmaps/haxima.png
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


%files
%{_bindir}/nazghul
%dir %{_datadir}/nazghul
%doc AUTHORS ChangeLog COPYING NEWS GAME_RULES GHULSCRIPT
%doc MAP_HACKERS_GUIDE engine_extension_and_design world_building


%files -n haxima
%{_bindir}/haxima
%{_datadir}/nazghul/haxima
%{_datadir}/applications/haxima.desktop
%{_datadir}/pixmaps/haxima.png
%doc USERS_GUIDE haxima-music-license


%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_3.20120228gitb0a402a
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_2.20120228gitb0a402a
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_1.20120104cvs
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_1.20120104cvs
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_4.20120104cvs
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3.20100413cvs
- update to new release by fcimport

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_2.20100413cvs
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_2.20100413cvs
- converted from Fedora by srpmconvert script

