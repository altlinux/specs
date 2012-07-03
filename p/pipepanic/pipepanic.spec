Name: pipepanic
Version: 0.1.3
Release: alt4_9
Summary: A pipe connecting game       

Group: Games/Other
License: GPLv2+
URL: http://www.users.waitrose.com/~thunor/pipepanic/
Source0: http://www.users.waitrose.com/~thunor/pipepanic/dload/%{name}-%{version}-source.tar.gz
Source1: pipepanic.desktop
Patch0: pipepanic-0.1.3-Makefile.patch
# Hans de Goede
Patch1: pipepanic-0.1.3-window-title.patch

BuildRequires: libSDL-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
Requires: icon-theme-hicolor
Source44: import.info


%description
Pipepanic is a pipe connecting game using libSDL. Connect as many 
different shaped pipes together as possible within the time given.


%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p0
%patch1 -p1

# Fix file encoding
iconv --from=ISO-8859-1 --to=UTF-8 COPYING-ARTWORK > COPYING-ARTWORK.conv 
mv COPYING-ARTWORK.conv COPYING-ARTWORK

# Fix DATADIR
sed -i 's:/opt/QtPalmtop/share/pipepanic/:%{_datadir}/%{name}/:' main.h


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install

# Install binary
mkdir -p %{buildroot}%{_bindir}
install -m 755 pipepanic %{buildroot}%{_bindir}

# Install data files
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 *.bmp %{buildroot}%{_datadir}/%{name}/

# Install window icon (needed by patch1)
convert PipepanicIcon32.png bmp3:- | \
  convert - -fill '#FF00FF' -opaque black -colors 256 \
    -compress none bmp3:icon.bmp
install -m 644 icon.bmp %{buildroot}%{_datadir}/%{name}/

# Install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m 644 PipepanicIcon16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 PipepanicIcon32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 PipepanicIcon48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 644 PipepanicIcon64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install          \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
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
%{_bindir}/pipepanic
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc AUTHORS ChangeLog COPYING COPYING-ARTWORK README


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_9
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_8
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt2_8
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_8
- converted from Fedora by srpmconvert script

