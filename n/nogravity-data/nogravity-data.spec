# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           nogravity-data
Version:        2.00
Release:        alt2_8
Summary:        Data files for No Gravity
Group:          Games/Other
License:        GPLv2+
URL:            http://www.realtech-vr.com/nogravity/
Source0:        http://downloads.sourceforge.net/nogravity/rt-%{name}.zip
BuildArch:      noarch
# So that we get removed together with nogravity itself
Requires:       nogravity >= %{version}
Source44: import.info

%description
Data files (audio, maps, etc) for No Gravity.


%prep
%setup -q -c
sed -i 's/\r//g' GNU.TXT


%build
# nothing to build data only 


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/nogravity
install -p -m 644 NOGRAVITY.RMX $RPM_BUILD_ROOT%{_datadir}/nogravity
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
%doc GNU.TXT
%{_datadir}/nogravity


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_8
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_7
- converted from Fedora by srpmconvert script

