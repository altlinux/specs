# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname oflb-sportrop-fonts
%global fontname oflb-sportrop
%global fontconf 63-%{fontname}.conf

Name:           fonts-ttf-oflb-sportrop
Version:        0.9
Release:        alt3_10
Summary:        A multiline decorative font

Group:          System/Fonts/True type
License:        OFL
## Note that upstream is dead and there is no download link available at this minute
## so please don't report FTBFS bugs for this package.
URL:            http://openfontlibrary.org/media/files/gluk/287
Source0:        http://openfontlibrary.org/people/gluk/gluk_-_Sportrop.zip
Source1:        %{oldname}-fontconfig.conf
BuildArch:      noarch
BuildRequires:  fontpackages-devel
Obsoletes:      sportrop-fonts < 0.9-8
Provides:       sportrop-fonts = %{version}-%{release}
Source44: import.info

%description
A neat multiline font


%prep
%setup -q -c
chmod 0644 *.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done
 
%build
#nothing to do

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
%doc OFL_FAQ.txt OFL_License.txt tabl_c.jpg

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_10
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_10
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_9
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_9
- initial release by fcimport

