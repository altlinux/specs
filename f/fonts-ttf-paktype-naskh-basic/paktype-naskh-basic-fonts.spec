%define oldname paktype-naskh-basic-fonts
%define fontname paktype-naskh-basic
%global fontconf 67-%{fontname}
%define fontdir %{_datadir}/fonts/%{fontname}

# Common description
%define common_desc \
The paktype-naskh-basic-fonts package contains fonts for the display of \
Arabic, Farsi, Urdu and Sindhi from PakType by Lateef Sagar.

Name:    fonts-ttf-paktype-naskh-basic
Version: 3.0
Release: alt3_10
License: GPLv2 with exceptions
URL: https://sourceforge.net/projects/paktype/
Source0: http://downloads.sourceforge.net/project/paktype/NaskhBasic-3.0.tar.gz
Source1: %{fontconf}-sa.conf
Source2: %{fontconf}-sindhi.conf
Source3: %{fontconf}-farsi.conf
Source4: %{fontconf}-urdu.conf
Source5: %{fontconf}.conf
BuildArch: noarch
BuildRequires:  fontpackages-devel
Requires:       %{name}-common
Group: System/Fonts/True type
Summary: Fonts for Arabic, Farsi, Urdu and Sindhi from PakType
Source44: import.info

 
%description
%common_desc

%package common
Summary:  Common files for paktype-naskh fonts
Group:  System/Fonts/True type
%description common
%common_desc


%package -n fonts-ttf-paktype-naskh-basic-farsi
Summary: Font for Farsi from PakType
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
%description -n fonts-ttf-paktype-naskh-basic-farsi
%common_desc 
This package provides a free Farsi truetype/opentype font 

%files -n fonts-ttf-paktype-naskh-basic-farsi
%{_fontconfig_templatedir}/%{fontconf}-farsi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-farsi.conf
%{_fontbasedir}/*/%{_fontstem}/PakTypeNaskhBasicFarsi.ttf

%package -n fonts-ttf-paktype-naskh-basic-sa
Summary: Fonts for Arabic, Farsi, Urdu and Sindhi from PakType
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
%description -n fonts-ttf-paktype-naskh-basic-sa
%common_desc

%files -n fonts-ttf-paktype-naskh-basic-sa
%{_fontconfig_templatedir}/%{fontconf}-sa.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sa.conf
%{_fontbasedir}/*/%{_fontstem}/PakTypeNaskhBasicSA.ttf

%package -n fonts-ttf-paktype-naskh-basic-sindhi
Summary: Font for Sindhi from PakType
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
%description -n fonts-ttf-paktype-naskh-basic-sindhi
%common_desc 
This package provides a free Sindhi truetype/opentype font 

%files -n fonts-ttf-paktype-naskh-basic-sindhi
%{_fontconfig_templatedir}/%{fontconf}-sindhi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sindhi.conf
%{_fontbasedir}/*/%{_fontstem}/PakTypeNaskhBasicSindhi.ttf

%package -n fonts-ttf-paktype-naskh-basic-urdu
Summary: Font for Urdu from PakType
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
%description -n fonts-ttf-paktype-naskh-basic-urdu
%common_desc 
This package provides a free Urdu truetype/opentype font 

%files -n fonts-ttf-paktype-naskh-basic-urdu
%{_fontconfig_templatedir}/%{fontconf}-urdu.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-urdu.conf
%{_fontbasedir}/*/%{_fontstem}/PakTypeNaskhBasicUrdu.ttf

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/PakTypeNaskhBasic.ttf

%prep
%setup -q -c
mv NaskhBasic-3.0/* .
mv Ready\ to\ use\ fonts/* .
mv PakType\ Naskh\ Basic\ Farsi.ttf PakTypeNaskhBasicFarsi.ttf
mv PakType\ Naskh\ Basic.ttf PakTypeNaskhBasic.ttf
mv PakType\ Naskh\ Basic\ SA.ttf PakTypeNaskhBasicSA.ttf
mv PakType\ Naskh\ Basic\ Urdu.ttf PakTypeNaskhBasicUrdu.ttf
mv PakType\ Naskh\ Basic\ Sindhi.ttf PakTypeNaskhBasicSindhi.ttf
mv License\ files/* .
mv PakType\ Naskh\ Basic\ Comparison\ Chart.htm  PakType_Naskh_Basic_Comparison_Chart.htm
mv PakType\ Naskh\ Basic\ Comparison\ Chart.pdf PakType_Naskh_Basic_Comparison_Chart.pdf
%{__sed} -i 's/\r//'  PakType_Naskh_Basic_Comparison_Chart.htm
mv PakType\ Naskh\ Basic\ License.txt  PakType_Naskh_Basic_License.txt
%{__sed} -i 's/\r//' PakType_Naskh_Basic_License.txt
chmod a-x PakType_Naskh_Basic_Comparison_Chart.htm PakType_Naskh_Basic_License.txt PakType_Naskh_Basic_Comparison_Chart.pdf
for txt in Readme.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\x92//g' $txt.new
   sed -i 's/\x93//g' $txt.new
   sed -i 's/\x94//g' $txt.new
   sed -i 's/\x96//g' $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done

%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakTypeNaskhBasicFarsi.ttf PakTypeNaskhBasic.ttf PakTypeNaskhBasicSA.ttf PakTypeNaskhBasicUrdu.ttf PakTypeNaskhBasicSindhi.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sa.conf


install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sindhi.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-farsi.conf


install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-urdu.conf

install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf


for fconf in %{fontconf}-sa.conf \
             %{fontconf}-sindhi.conf \
             %{fontconf}-farsi.conf \
             %{fontconf}-urdu.conf \
             %{fontconf}.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
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



%files common
%doc PakType_Naskh_Basic_Comparison_Chart.htm PakType_Naskh_Basic_License.txt PakType_Naskh_Basic_Comparison_Chart.pdf Readme.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt3_10
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt2_10
- update to new release by fcimport

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.0-alt2_9
- rebuild woth new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_9
- initial release by fcimport

