Name:           sear-media
Version:        0.6
# No dist tag because this is large noarch game data.
Release:        alt2_8
Summary:        Media files for the sear worldforge client

Group:          Games/Other
License:        GPLv2+ or GFDL
URL:            http://www.worldforge.org
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-20070206.tar.gz
BuildArch:      noarch
Source44: import.info

%description
Media files for the sear WorldForge client.


%prep
%setup -q

# Remove editor swap file.
rm -f castle/.dot_it.sh.swp

# Rename some doc files to prevent filename conflicts
mv chicken/README README.chicken


%build
# Nothing to build!


%install
install -d $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}
cp -a * $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}

# Remove doc files from the installed media files.
rm -f $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}/COPYING.txt
rm -f $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}/LICENSING.txt
rm -f $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}/README
rm -f $RPM_BUILD_ROOT%{_datadir}/sear/%{name}-%{version}/README.chicken
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
%doc COPYING.txt LICENSING.txt README README.chicken
%dir %{_datadir}/sear
%{_datadir}/sear/%{name}-%{version}


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_8
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_7
- initial release by fcimport

