Summary(ko): 한글 은글꼴 Core 모음
Summary(ko): 한글 은글꼴 Core 모음
%define oldname un-core-fonts
%define version 1.0.2
%define name un-core-fonts
%global fontname un-core
%global fontconf 65-1-%{fontname}

%global alphatag    080608
%global archivename un-fonts-core-%{version}-%{alphatag}

%global common_desc \
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Core set is composed of: \
\
- UnBatang: serif \
- UnDinaru: fantasy \
- UnDotum: sans-serif \
- UnGraphic: sans-serif style \
- UnGungseo: cursive, brush-stroke \
- UnPilgi: script

%define common_desc_ko \
은글꼴 시리즈는 HLaTex개발자이신 은광희님이 1998년에 개발한 폰트입니다. \
2003년에 박원규님이 FontForge를 이용하여 트루타입폰트로 변환했습니다. \
은글꼴은 가장 일반적인 글꼴들입니다. \
\
Core 모음: \
- 은바탕: serif \
- 은디나루: fantasy \
- 은돋음: sans-serif \
- 은그래픽: sans-serif style \
- 은궁서: cursive, brush-stroke \
- 은필기: script

Name:           fonts-ttf-un-core
Version:        1.0.2
Release:        alt3_0.18.080608
Summary:        Un Core family of Korean TrueType fonts
Summary(ko):    한글 은글꼴 Core 모음

Group:          System/Fonts/True type
License:        GPLv2
URL:            http://kldp.net/projects/unfonts/
Source0:        http://kldp.net/frs/download.php/4695/%{archivename}.tar.gz
Source1:        %{oldname}-batang-fontconfig.conf
Source2:        %{oldname}-dinaru-fontconfig.conf
Source3:        %{oldname}-dotum-fontconfig.conf
Source4:        %{oldname}-graphic-fontconfig.conf
Source5:        %{oldname}-gungseo-fontconfig.conf
Source6:        %{oldname}-pilgi-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%package common
Group: System/Fonts/True type
Summary:        Common files of Un Core fonts

%description common
%common_desc

This package consists of files used by other %{oldname} packages.

# un_subpkg 1:name 2:Name 3:Hangul [4:obsolete] [5:obsolete]
%define un_subpkg() \
%package -n fonts-ttf-%{fontname}-%1 \
Summary:        Un Core fonts - %(echo %2) \
Summary(ko):    한글 은글꼴 Core 모음 - %(echo %3) \
Group:          System/Fonts/True type \
Requires:       %{name}-common = %{version}-%{release} \
\
\

%un_subpkg batang UnBatang 은바탕 bold
%un_subpkg dinaru UnDinaru 은디나루 bold light
%un_subpkg dotum UnDotum 은돋음 bold
%un_subpkg graphic UnGraphic 은그래픽 bold
%un_subpkg gungseo UnGungseo 은궁서
%un_subpkg pilgi UnPilgi 은필기 bold


%description
%common_desc

%description -l ko
%common_desc_ko

%description -n fonts-ttf-un-core-batang
%common_desc

This package includes UnBatang, a serif font.

%description -l ko -n fonts-ttf-un-core-batang
%common_desc_ko

이 패키지에는 은바탕글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-core-dinaru
%common_desc

This package includes UnDinaru, a fantasy font.

%description -l ko -n fonts-ttf-un-core-dinaru
%common_desc_ko

이 패키지에는 은디나루글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-core-dotum
%common_desc

This package includes UnDotum, a sans-serif font.

%description -l ko -n fonts-ttf-un-core-dotum
%common_desc_ko

이 패키지에는 은돋음글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-core-graphic
%common_desc

This package includes UnGraphic, a sans-serif font.

%description -l ko -n fonts-ttf-un-core-graphic
%common_desc_ko

이 패키지에는 은그래픽글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-core-gungseo
%common_desc

This package includes UnGungseo, a cursive font.

%description -l ko -n fonts-ttf-un-core-gungseo
%common_desc_ko

이 패키지에는 은궁서글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-core-pilgi
%common_desc

This package includes UnPilgi, a script font.

%description -l ko -n fonts-ttf-un-core-pilgi
%common_desc_ko

이 패키지에는 은필기글꼴이 포함되어 있습니다.


%files -n fonts-ttf-un-core-batang
%{_fontconfig_templatedir}/%{fontconf}-batang.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-batang.conf
%{_fontbasedir}/*/%{_fontstem}/UnBatang.ttf
%{_fontbasedir}/*/%{_fontstem}/UnBatangBold.ttf
%files -n fonts-ttf-un-core-dinaru
%{_fontconfig_templatedir}/%{fontconf}-dinaru.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-dinaru.conf
%{_fontbasedir}/*/%{_fontstem}/UnDinaru.ttf
%{_fontbasedir}/*/%{_fontstem}/UnDinaruLight.ttf
%{_fontbasedir}/*/%{_fontstem}/UnDinaruBold.ttf
%files -n fonts-ttf-un-core-dotum
%{_fontconfig_templatedir}/%{fontconf}-dotum.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-dotum.conf
%{_fontbasedir}/*/%{_fontstem}/UnDotum.ttf
%{_fontbasedir}/*/%{_fontstem}/UnDotumBold.ttf
%files -n fonts-ttf-un-core-graphic
%{_fontconfig_templatedir}/%{fontconf}-graphic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-graphic.conf
%{_fontbasedir}/*/%{_fontstem}/UnGraphic.ttf
%{_fontbasedir}/*/%{_fontstem}/UnGraphicBold.ttf
%files -n fonts-ttf-un-core-gungseo
%{_fontconfig_templatedir}/%{fontconf}-gungseo.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gungseo.conf
%{_fontbasedir}/*/%{_fontstem}/UnGungseo.ttf
%files -n fonts-ttf-un-core-pilgi
%{_fontconfig_templatedir}/%{fontconf}-pilgi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pilgi.conf
%{_fontbasedir}/*/%{_fontstem}/UnPilgi.ttf
%{_fontbasedir}/*/%{_fontstem}/UnPilgiBold.ttf


%prep
%setup -q -n un-fonts


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-batang.conf
install -m 0644 -p %{SOURCE2}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dinaru.conf
install -m 0644 -p %{SOURCE3}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dotum.conf
install -m 0644 -p %{SOURCE4}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-graphic.conf
install -m 0644 -p %{SOURCE5}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gungseo.conf
install -m 0644 -p %{SOURCE6}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pilgi.conf

for fconf in %{fontconf}-batang.conf \
    %{fontconf}-dinaru.conf \
    %{fontconf}-dotum.conf \
    %{fontconf}-graphic.conf \
    %{fontconf}-gungseo.conf \
    %{fontconf}-pilgi.conf ; do
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
%doc COPYING README


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.18.080608
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.18.080608
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.16.080608
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_0.16.080608
- initial release by fcimport

