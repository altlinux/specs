# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           crystal-stacker
Version:        1.5
Release:        alt2_12
Summary:        Falling blocks, match 3 or more of the same color crystals
Group:          Games/Other
License:        Crystal Stacker
URL:            http://www.t3-i.com/cstacker.htm
Source0:        http://www.t3-i.com/ncdgames/cs15src.zip
Source1:        %{name}.desktop
Source2:        %{name}-theme-editor.desktop
Patch0:         crystal-stacker-1.5-ImplicitDSOLinking.patch
BuildRequires:  liballegro-devel dumb-devel ImageMagick desktop-file-utils
Source44: import.info

%description
If you've played Columns then you know what Crystal Stacker is all about. Match
3 or more of the same color crystals either horizontally, vertically, or dia-
gonally to destroy them. For every 45 crystals you destroy, the level increases
and the crystals fall faster. The higher the level, the more points you are   
awarded for destroying crystals.


%package theme-editor
Summary:	Themes editor for Crystal Stacker
Group:		Games/Other
Requires:	%{name} = %{version}

%description theme-editor
Create new Themes for Crystal Stacker


%prep
%setup -q -c
%patch0 -p1
%{__sed} -i 's/\r//' ce/*.txt cs/*.txt


%build
export CC="gcc -Wl,--no-as-needed"
pushd cs/source
make %{?_smp_mflags} -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
popd

pushd ce/source
make %{?_smp_mflags} -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-char-subscripts"
popd

convert cs/cs.ico %{name}.png
convert ce/ce.ico %{name}-theme-editor.png


%install
pushd cs/source
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

pushd ce/source
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png %{name}-theme-editor.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
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
%doc cs/*.txt
%{_bindir}/crystal-stacker
%dir %{_datadir}/crystal-stacker
%{_datadir}/crystal-stacker/cs.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files theme-editor
%doc ce/*.txt
%{_bindir}/crystal-stacker-theme-editor
%{_datadir}/crystal-stacker/ce.dat
%{_datadir}/applications/%{name}-theme-editor.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}-theme-editor.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_12
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_11
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_10
- converted from Fedora by srpmconvert script

