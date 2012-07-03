# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gzip gcc-c++ libXext-devel libXi-devel
# END SourceDeps(oneline)
Summary: 3D tabletennis game
Name: csmash
Version: 0.6.6
Release: alt3_24
License: GPLv2+
Group: Games/Other
URL: http://cannonsmash.sourceforge.net/
Source0: http://dl.sf.net/cannonsmash/csmash-%{version}.tar.gz
Source1: csmash-64x64.png
Source2: csmash.desktop
Patch0: csmash-0.6.6-64bit-gcc4-fixes.patch
Patch1: csmash-0.6.6-extraqualif.patch
Patch2: csmash-0.6.6-configure.patch
Patch3: csmash-0.6.6-datadir.patch
BuildRequires: libgtk+2-devel libjpeg-devel zlib-devel gettext
BuildRequires: libSDL-devel >= 1.2.0 libSDL_mixer-devel libSDL_image-devel
BuildRequires: desktop-file-utils
BuildRequires: libXmu-devel libXt-devel libICE-devel libX11-devel
BuildRequires: libGL-devel libGLU-devel
# Required for autoreconf
BuildRequires: autoconf automake gettext-devel
Source44: import.info

%description
CannonSmash is a 3D tabletennis game. The goal of this project is to
represent various strategy of tabletennis on computer game.
This program requires OpenGL and SDL. If your machine doesn't have 3D
accelaration video card, this program runs very slowly.


%prep
%setup -q
%patch0 -p1 -b .64bit-gcc4
%patch1 -p1 -b .extraqualif
%patch2 -p1 -b .configure
%patch3 -p1 -b .datadir
autoreconf --force --install -Im4
# Convert to UTF-8 while keeping the original timestamps
iconv -f iso8859-1 -t utf-8 README > tmp
touch -r README tmp
mv -f tmp README
chmod 0644 README


%build
%configure --disable-dependency-tracking
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

# Install the menu entry icon
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/csmash.png

# Now the menu entry
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor "" \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE2}
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


%files -f %{name}.lang
%doc AUTHORS COPYING CREDITS ChangeLog README README.en
%{_bindir}/csmash
%{_datadir}/applications/csmash.desktop
%{_datadir}/icons/hicolor/64x64/apps/csmash.png
%{_datadir}/csmash/


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt3_24
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt2_24
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt2_23
- update to new release by fcimport

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt2_22
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt1_22
- converted from Fedora by srpmconvert script

