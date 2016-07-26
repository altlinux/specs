Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname campivisivi-titillium-fonts
%global fontname campivisivi-titillium
%global fontconf 61-%{fontname}.conf

Name:		fonts-otf-campivisivi-titillium
Version:	20120913
Release:	alt1_12
Summary:	Sans-serif typeface designed inside Campi Visivi's Type Design course

License:	OFL
URL:		http://www.campivisivi.net/titillium/
Source0:	http://www.campivisivi.net/titillium/download/Titillium_roman_upright_italic_2_0_OT.zip
Source1:	%{oldname}-fontconfig.conf
Source2:	%{oldname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
Source44: import.info

%description
Sans-serif typeface from the Master of Visual Design Campi Visivi.

%prep
%setup -q -n "Titillium_roman_upright_italic_2_0_OT"

for file in *.txt; do
 sed 's/\r//g' "$file" | \
 fold -s > "$file.new" && \
 touch -r "$file" "$file.new" && \
 mv "$file.new" "$file"
done

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
		%{buildroot}%{_datadir}/appdata/%{oldname}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{oldname}.metainfo.xml
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf

%{_datadir}/appdata/%{oldname}.metainfo.xml
%doc OFL-FAQ.txt OFL-titillium.txt


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_6
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_5
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_4
- converted for ALT Linux by srpmconvert tools

