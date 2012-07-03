# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname aajohan-comfortaa-fonts
%global fontname aajohan-comfortaa
%global fontconf 61-%{fontname}.conf

Name:           fonts-ttf-aajohan-comfortaa
Version:        2.002
Release:        alt2_5
Summary:        Modern style true type font

Group:          System/Fonts/True type
License:        OFL
URL:            http://aajohan.deviantart.com
Source0:        http://www.deviantart.com/download/105395949/comfortaa___font_by_aajohan-d1qr019.zip
Source1:        %{oldname}-fontconfig.conf
BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
Comfortaa is a sans-serif font comfortable in every aspect with
Bold, Regular, and Thin variants.
It has very good European language coverage and decent Cyrillic coverage.  

%prep
%setup -q -n Comfortaa

# Fixing
# wrong-file-end-of-line-encoding issue
# Thanks to Paul Flo Williams

for file in *.txt; do
 sed 's/\r//g' "$file" | \
 fold -s > "$file.new" && \
 touch -r "$file" "$file.new" && \
 mv "$file.new" "$file"
done

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.ttf

%doc FONTLOG.txt OFL.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.002-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.004-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_2
- initial release by fcimport

