# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           vavoom
Version:        1.33
Release:        alt2_3
Summary:        Enhanced Doom, Heretic, Hexen and Strife source port
Source0:        http://downloads.sourceforge.net/vavoom/%{name}-%{version}.tar.bz2
Source1:        doom.autodlrc
Source2:        heretic.autodlrc
Source3:        hexen.autodlrc
Source4:        strife.autodlrc
Source5:        doom-shareware.sh
Source6:        heretic-shareware.sh
Source7:        hexen-demo.sh
Source8:        strife-demo.sh
Source9:        doom-shareware.desktop
Source10:       heretic-shareware.desktop
Source11:       hexen-demo.desktop
Source12:       strife-demo.desktop
Source13:       doom-logo.png
Source14:       tux-b2f.png
Patch0:         vavoom-1.21-datadir.patch
Patch1:         vavoom-1.27-CMakeLists.patch
URL:            http://vavoom-engine.com/
Group:          Games/Other
License:        GPLv2+
BuildRequires:  libSDL_mixer-devel libSDL_net-devel libpng-devel libjpeg-devel
BuildRequires:  libvorbis-devel libmikmod-devel libflac-devel libopenal-devel
BuildRequires:  libGLU-devel libwxGTK-devel desktop-file-utils ctest cmake
Requires:       timidity-instruments icon-theme-hicolor autodownloader
Source44: import.info

%description
Vavoom is an enhanced open-source port of Doom. Allowing you to play not only
the classic 3D first-person shooter Doom, but also the Doom derived classics
Heretic, Hexen and Strife. Compared to the original games it adds extra
features such as translucency and freelook support and ofcourse the capability
to play these classics under Linux.

%prep 
%setup -q
%patch0 -p1 -b .datadir
%patch1 -p1

%build
%{fedora_cmake} -DWITH_LIBMAD:BOOL=OFF

# This one line sed command is easier than trying to muck with the Makefile
# to add the proper -D definition.
sed -i "s|#define FL_BASEDIR.*|#define FL_BASEDIR \"%{_datadir}/%{name}\"|" source/files.h
sed -i "s|#define CONFIG_FILE.*|#define CONFIG_FILE \"%{_sysconfdir}/timidity.cfg\"|" source/timidity/timidity.h

make VERBOSE=1

%install
make install \
        DESTDIR=$RPM_BUILD_ROOT \
        INSTALL_PARMS="-m 0755" \
        INSTALL_EXEPARMS="-m 0755" \
        INSTALL_DIRPARMS="-m 0755 -d"

mv $RPM_BUILD_ROOT%{_bindir}/%{name}.* $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_bindir}/%{name}-dedicated.* $RPM_BUILD_ROOT%{_bindir}/%{name}-dedicated

# install autodl files and wrapper scripts
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/%{name}

install -p -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/doom-shareware
install -p -m 755 %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/heretic-shareware
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/hexen-demo
install -p -m 755 %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/strife-demo

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE9}
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE10}
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE11}
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE12}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE13} %{SOURCE14} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
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
%doc docs/*.log docs/gnu.txt docs/vavoom.txt
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/*.png

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.33-alt2_3
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_3
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_2
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_1
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_6
- initial release by fcimport

