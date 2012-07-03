# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           gemdropx
Version:        0.9
Release:        alt6_8
Summary:        Falling blocks puzzlegame
Group:          Games/Other
License:        GPL+
URL:            http://www.newbreedsoftware.com/gemdropx
Source0:        ftp://ftp.billsgames.com/unix/x/%{name}/src/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  libSDL_mixer-devel ImageMagick desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Gem Drop X is a fast-paced puzzle game where it is your job to clear
the screen of gems before they squash you.


%prep
%setup -q
mv data/sounds/README README-sounds.txt
mv data/images/README README-images.txt


%build
make XTRA_FLAGS="$RPM_OPT_FLAGS" DATA_PREFIX=%{_datadir}/%{name}


%install
# Makefile always wants to install under /usr/local, so DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/images
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 data/images/*.bmp $RPM_BUILD_ROOT%{_datadir}/%{name}/images
cp -a data/sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
 
# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install  \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
convert data/images/%{name}-icon.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
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
%doc README*.txt COPYING.txt AUTHORS.txt CHANGES.txt TODO.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt6_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt5_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt5_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt4_7
- rebuild with new rpm desktop cleaner

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_7
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_7
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_7
- converted from Fedora by srpmconvert script

