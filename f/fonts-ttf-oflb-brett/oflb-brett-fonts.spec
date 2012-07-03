%define oldname oflb-brett-fonts
%global fontname oflb-brett
%global fontconf 63-%{fontname}.conf

Name:           fonts-ttf-oflb-brett
Version:        20080506
Release:        alt3_9
Summary:        A handwriting font

Group:          System/Fonts/True type
License:        OFL
## Note that upstream is dead and there is no download link available at this minute
## so please don't report FTBFS bugs for this package.
URL:            http://openfontlibrary.org/media/files/brettalton/205
Source0:        BrettFont1.1.ttf
Source1:        %{oldname}-fontconfig.conf
#license text extracted from font file
Source2:        License.txt
BuildArch:      noarch
BuildRequires:  fontpackages-devel
Obsoletes:      brettfont-fonts < 20080506-7
Provides:       brettfont-fonts = %{version}-%{release}
Source44: import.info

%description
A handwriting font made by Brett Alton.


%prep
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}

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
%doc License.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080506-alt3_9
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080506-alt2_9
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20080506-alt2_8
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 20080506-alt1_8
- initial release by fcimport

