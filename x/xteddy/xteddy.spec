# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSM-devel
# END SourceDeps(oneline)
Name:           xteddy
Version:        2.0.1
Release:        alt5_9
Summary:        Tool to sit around silently, look cute, and make you smile

Group:          Games/Other
License:        GPL+
URL:            http://fam-tille.de/debian/xteddy.html
Source0:        http://webstaff.itn.liu.se/~stegu/xteddy/%{name}-%{version}.tar.gz
# Both submitted upstream by mail
Patch0:         xteddy-2.0.1-visual.patch
Patch1:         xteddy-2.0.1-iconname.patch

BuildRequires:  imlib-devel libpng-devel
Source44: import.info
Patch33: xteddy-2.0.1-alt-link-X11.patch

%description
Xteddy is your virtual comfort when things get rough. It can do everything
a real teddy bear can do. That is, I can sit around silently, look cute,
and make you smile. 


%prep
%setup -q
%patch0 -p1 -b .visual
%patch1 -p1 -b .iconname
%patch33 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Xteddy
GenericName=Virtual teddy bear
Comment=Xteddy is your virtual teddy bear. It can sit around silently, look cute, and make you smile.
Icon=amusement_section
Exec=xteddy
Categories=Game;Amusement;
EOF
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
%{_bindir}/xteddy
%{_bindir}/xteddy_test
%{_bindir}/xtoys
%{_mandir}/man1/xteddy.1*
%{_datadir}/xteddy
%doc COPYING README AUTHORS ChangeLog NEWS
%doc xteddy.README xtuxxy.credit
%_desktopdir/%name.desktop


%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt5_9
- update to new release by fcimport

* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt5_8
- fixed build

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_8
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_7
- update to new release by fcimport

* Mon Oct 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_6
- fixed desktop file

* Mon Oct 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_6
- added desktop file

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_6
- converted from Fedora by srpmconvert script

