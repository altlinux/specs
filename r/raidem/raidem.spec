# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip zlib-devel
# END SourceDeps(oneline)
Name:           raidem
Version:        0.3.1
Release:        alt2_21.1
Summary:        2d top-down shoot'em up
Group:          Games/Other
License:        zlib
URL:            http://home.exetel.com.au/tjaden/raidem/
# This is an exacy copy of the upstream src except that lib/almp3 which is
# an included mp3 decoder has been removed.
Source0:        %{name}-%{version}-src.zip
Source1:        raidem.png
Source2:        raidem.desktop
Patch0:         raidem-0.3.1-syslibs.patch
Patch1:         raidem-0.3.1-zziplib.patch
Patch2:         raidem-libpng15.patch
Patch3:         raidem-gcc4.7-stdio.patch
Patch4:         raidem-new-api.patch
Patch5:         raidem-0.3.1-alt-objc2.patch
BuildRequires:  gcc-objc glyph-keeper-allegro-devel libfreetype-devel libadime-devel
BuildRequires:  zziplib-devel libpng-devel AllegroOGG-devel
BuildRequires:  automake desktop-file-utils gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel
Requires:       icon-theme-hicolor
Source44: import.info

%description
Raid'em is a 2d top-down shoot'em up. It began as a remake of Raid II
(abandoned long ago), but has turned out very differently.
Features: Neat looking graphics, LOTS of explosions and scrap
metal, Eye candy a-plenty, Many different powerups, A desert. And a space
platform. And some snow, 2 player mode, Demo recording and playback, Loads of
fun.


%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1 -z .syslibs
%patch1 -p1
%patch2 -z .libpng
%patch3 -p0 -z .gcc47
%patch4 -p0 -z .newapi
%patch5 -p2

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

# remove all included system libs, to avoid using the included system headers.
mv lib/loadpng lib/alrand ./
rm -fr lib/*
mv alrand loadpng lib/
aclocal
autoconf

%build
export CC=gcc
export CXX=g++

# override _datadir otherwise it expects its datafile directly under /use/share
%configure --datadir=%{_datadir}/%{name} --disable-id3
make %{?_smp_mflags}


%install
# DIY, since the Makefile uses install -s and install -g games, etc.
# Fixable but this is easier
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a data demos maps $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
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
%doc ChangeLog docs/LICENCE.txt docs/README.txt docs/damages.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2_21.1
- Built with gcc 4.7 & libgnustep-objc2 instead of libobjc

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_21
- gcc46 build

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_21
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_20
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_19
- update to new release by fcimport

* Tue Nov 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_17
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_16
- initial release by fcimport

