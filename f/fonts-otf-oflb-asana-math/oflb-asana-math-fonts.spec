%define oldname oflb-asana-math-fonts
%global fontname oflb-asana-math
%global fontconf 63-%{fontname}.conf

Name:           fonts-otf-oflb-asana-math
Version:        0.930
Release:        alt2_2
Summary:        An OpenType font with a MATH table

Group:          System/Fonts/True type
License:        OFL
## Note that upstream is dead and there is no download link available at this minute
## so please don't report FTBFS bugs for this package.
URL:            http://www.ctan.org/tex-archive/fonts/Asana-Math/
Source0:        http://ekalavya.imsc.res.in/tex-archive/fonts/Asana-Math/Asana-Math.otf
Source1:        %{oldname}-fontconfig.conf
Source2:        README.license
#license text extracted from font file
Source3:        License.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Obsoletes:      asana-math-fonts < 0.914-8
Provides:       asana-math-fonts = %{version}-%{release}
Source44: import.info

%description
An OpenType font with a MATH table that can be used with XeTeX to typeset math
content


%prep
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
#nothing to do

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
%{_fontbasedir}/*/%{_fontstem}/*.otf
%doc README.license License.txt


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.930-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.930-alt1_2
- update to new release by fcimport

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.930-alt1_1
- update to new release by fcimport

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.914-alt1_9
- initial release by fcimport

