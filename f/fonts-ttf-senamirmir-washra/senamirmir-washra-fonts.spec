# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname senamirmir-washra-fonts
%define version 4.1
%define name senamirmir-washra-fonts
%global fontname senamirmir-washra
%global fontconf 65-%{fontname}

%global archivename washra-fonts-%{version}

%global common_desc \
A set of high quality unicode fonts for the  GeE.ez (Ethiopic) script \
published by the Senamirmir project. They can be used to write Ethiopic and \
Eritrean languages (Amharic, Blin, GeE.ez, Harari, MeE.en, Tigre, Tigrinyaa..).


Name:    fonts-ttf-senamirmir-washra
Version: 4.1
Release: alt3_7
Summary: Fonts for the GeE.ez (Ethiopic) script

Group:   System/Fonts/True type
License: OFL
URL:     http://www.senamirmir.org/projects/typography/typeface.html
Source0: http://www.senamirmir.org/downloads/%{archivename}.zip
# Problems reported upstream
# https://www.redhat.com/archives/fedora-fonts-list/2009-June/msg00002.html
Source1: %{oldname}-fontconfig.conf
# We need upstream or someone who knows local Ethiopian usage to suggest a
# classification we could relay to fontconfig. In the meanwhile, only three
# font families classified
Source2: %{oldname}-yigezu-bisrat-goffer-fontconfig.conf
Source3: %{oldname}-yigezu-bisrat-gothic-fontconfig.conf



BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
%common_desc

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/washrab.ttf
%{_fontbasedir}/*/%{_fontstem}/washrasb.ttf

%package common
Group: System/Fonts/True type
Summary:  Common files of %{oldname}

%description common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-ttf-senamirmir-washra-fantuwua
Group: System/Fonts/True type
Summary:  A font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-fantuwua
%common_desc

This package consists of the a.'Ethiopic Fantuwuaa.' font.

%files -n fonts-ttf-senamirmir-washra-fantuwua
%{_fontbasedir}/*/%{_fontstem}/fantuwua.ttf


%package -n fonts-ttf-senamirmir-washra-hiwua
Group: System/Fonts/True type
Summary:  A font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-hiwua
%common_desc

This package consists of the a.'Ethiopic Hiwuaa.' font.

%files -n fonts-ttf-senamirmir-washra-hiwua
%{_fontbasedir}/*/%{_fontstem}/hiwua.ttf


%package -n fonts-ttf-senamirmir-washra-jiret
Group: System/Fonts/True type
Summary:  A font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-jiret
%common_desc

This package consists of the a.'Ethiopia Jireta.' font.

%files -n fonts-ttf-senamirmir-washra-jiret
%{_fontbasedir}/*/%{_fontstem}/jiret.ttf


%package -n fonts-ttf-senamirmir-washra-tint
Group: System/Fonts/True type
Summary:  A font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-tint
%common_desc

This package consists of the a.'Ethiopic Tinta.' font.

%files -n fonts-ttf-senamirmir-washra-tint
%{_fontbasedir}/*/%{_fontstem}/tint.ttf


%package -n fonts-ttf-senamirmir-washra-wookianos
Group: System/Fonts/True type
Summary:  A font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-wookianos
%common_desc

This package consists of the a.'Ethiopic Wookianosa.' font.

%files -n fonts-ttf-senamirmir-washra-wookianos
%{_fontbasedir}/*/%{_fontstem}/wookianos.ttf


%package -n fonts-ttf-senamirmir-washra-yebse
Group: System/Fonts/True type
Summary:  A font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-yebse
%common_desc

This package consists of the a.'Ethiopic Yebsea.' font.

%files -n fonts-ttf-senamirmir-washra-yebse
%{_fontbasedir}/*/%{_fontstem}/yebse.ttf


%package -n fonts-ttf-senamirmir-washra-yigezu-bisrat-goffer
Group: System/Fonts/True type
Summary:  A decorative font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-yigezu-bisrat-goffer
%common_desc

This package consists of the a.'Ethiopic Yigezu Bisrat Goffera.' font, a a.'Gothic
Goffera.' decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book
a.'Ye-ethiopia khine tsehifeta.' (Ethiopian Typography) provided the original
design that served as inspiration for this work.

%files -n fonts-ttf-senamirmir-washra-yigezu-bisrat-goffer
%{_fontconfig_templatedir}/%{fontconf}-yigezu-bisrat-goffer.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-yigezu-bisrat-goffer.conf
%{_fontbasedir}/*/%{_fontstem}/goffer.ttf


%package -n fonts-ttf-senamirmir-washra-yigezu-bisrat-gothic
Group: System/Fonts/True type
Summary:  A decorative font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-yigezu-bisrat-gothic
%common_desc

This package consists of the a.'Ethiopic Yigezu Bisrat Gothica.' font, a a.'Gothica.'
decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book
a.'Ye-ethiopia khine tsehifeta.' (Ethiopian Typography) provided inspiration for
this work.

%files -n fonts-ttf-senamirmir-washra-yigezu-bisrat-gothic
%{_fontconfig_templatedir}/%{fontconf}-yigezu-bisrat-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-yigezu-bisrat-gothic.conf
%{_fontbasedir}/*/%{_fontstem}/yigezubisratgothic.ttf


%package -n fonts-ttf-senamirmir-washra-zelan
Group: System/Fonts/True type
Summary:  A font for the GeE.ez (Ethiopic) script
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-senamirmir-washra-zelan
%common_desc

This package consists of the a.'Ethiopic Zelana.' font.

%files -n fonts-ttf-senamirmir-washra-zelan
%{_fontbasedir}/*/%{_fontstem}/zelan.ttf


%prep
%setup -c -q
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# No info available to classify the other fonts
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-yigezu-bisrat-goffer.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-yigezu-bisrat-gothic.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-yigezu-bisrat-goffer.conf \
             %{fontconf}-yigezu-bisrat-gothic.conf ; do
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
%doc *.txt *.pdf *.doc


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_6
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_6
- initial release by fcimport

