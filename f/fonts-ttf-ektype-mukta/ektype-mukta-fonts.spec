Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname ektype-mukta-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname ektype-mukta
%global fontconf 67-%{fontname}
%global common_desc \
Mukta is a typeface available in \
seven weights, supporting Devanagari, Gujarati, Tamil and Latin scripts.

Name:			fonts-ttf-ektype-mukta
Version:			2.538
Release:			alt1_3
Summary:		Free Indian truetype/open type fonts
License:			OFL
URL:			https://github.com/EkType/Mukta
Source0:		https://github.com/EkType/Mukta/releases/download/%{version}/Mukta.Font.Family.%{version}.zip
Source1:		%{oldname}-devanagari-fontconfig.conf
Source2:		%{oldname}-vaani-fontconfig.conf
Source3:		%{oldname}-mahee-fontconfig.conf
Source4:		%{oldname}-malar-fontconfig.conf
Source5:		%{fontname}.devanagari.metainfo.xml
Source6:		%{fontname}.vaani.metainfo.xml
Source7:		%{fontname}.mahee.metainfo.xml
Source8:		%{fontname}.malar.metainfo.xml
BuildArch:		noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-ektype-mukta-common
Group: System/Fonts/True type
Summary:		Common files of %{oldname}

%description -n fonts-ttf-ektype-mukta-common
%common_desc

%package -n fonts-ttf-ektype-mukta-devanagari
Group: System/Fonts/True type
Summary:		Free Devanagari font
Requires:		%{name}-common = %{version}-%{release}
Obsoletes:		fonts-ttf-ekmukta < 1.2.2-alt1_7
Provides:		ekmukta-fonts = %{version}-%{release}

%description -n fonts-ttf-ektype-mukta-devanagari
%common_desc
This package provides a free devanagari truetype/open type font.
%files -n fonts-ttf-ektype-mukta-devanagari
%{_fontconfig_templatedir}/%{fontconf}-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-devanagari.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Mukta-*.ttf
%{_datadir}/metainfo/%{fontname}.devanagari.metainfo.xml

%package -n fonts-ttf-ektype-mukta-vaani
Group: System/Fonts/True type
Summary:		Free Gujarati font
Requires:		%{name}-common = %{version}-%{release}

%description -n fonts-ttf-ektype-mukta-vaani
%common_desc
This package provides a free Gujarati truetype/open type font.
%files -n fonts-ttf-ektype-mukta-vaani
%{_fontconfig_templatedir}/%{fontconf}-vaani.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-vaani.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MuktaVaani-*.ttf
%{_datadir}/metainfo/%{fontname}.vaani.metainfo.xml

%package -n fonts-ttf-ektype-mukta-mahee
Group: System/Fonts/True type
Summary:		Free Gurmukhi font
Requires:		%{name}-common = %{version}-%{release}

%description -n fonts-ttf-ektype-mukta-mahee
%common_desc
This package provides a free Gurmukhi truetype/open type font.
%files -n fonts-ttf-ektype-mukta-mahee
%{_fontconfig_templatedir}/%{fontconf}-mahee.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-mahee.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MuktaMahee-*.ttf
%{_datadir}/metainfo/%{fontname}.mahee.metainfo.xml

%package -n fonts-ttf-ektype-mukta-malar
Group: System/Fonts/True type
Summary:		Free Tamil font
Requires:		%{name}-common = %{version}-%{release}

%description -n fonts-ttf-ektype-mukta-malar
%common_desc
This package provides a free Tamil truetype/open type font.
%files -n fonts-ttf-ektype-mukta-malar
%{_fontconfig_templatedir}/%{fontconf}-malar.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-malar.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MuktaMalar-*.ttf
%{_datadir}/metainfo/%{fontname}.malar.metainfo.xml

%prep
%setup -n %{oldname}-%{version} -q -c

sed -i 's/\r$//' *.txt README.md

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p */*.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-devanagari.conf
install -m 0644 -p %{SOURCE2} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-vaani.conf
install -m 0644 -p %{SOURCE3} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mahee.conf
install -m 0644 -p %{SOURCE4} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-malar.conf

install -Dm 0644 -p %{SOURCE5} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.devanagari.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.vaani.metainfo.xml
install -Dm 0644 -p %{SOURCE7} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.mahee.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.malar.metainfo.xml

for fconf in %{fontconf}-devanagari.conf \
		%{fontconf}-vaani.conf \
		%{fontconf}-mahee.conf \
		%{fontconf}-malar.conf; do
	ln -s %{_fontconfig_templatedir}/$fconf \
		%{buildroot}%{_fontconfig_confdir}/$fconf
done
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

%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.*.metainfo.xml

%files -n fonts-ttf-ektype-mukta-common
%doc AUTHORS.txt README.md CONTRIBUTORS.txt
%doc --no-dereference OFL.txt Copyright.txt 

%changelog
* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.538-alt1_3
- new version

