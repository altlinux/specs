Summary(ko): 한글 은글꼴 Extra 모음
Summary(ko): 한글 은글꼴 Extra 모음
%define oldname un-extra-fonts
%global fontname    un-extra
%global fontconf    66-%{fontname}

%global archivename un-fonts-extra
%define alphatag    080608

%define common_desc_en \
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Extra set is composed of: \
\
- UnPen, UnPenheulim: script \
- UnTaza: typewriter style \
- UnBom: decorative \
- UnShinmun \
- UnYetgul: old Korean printing style \
- UnJamoSora, UnJamoNovel, UnJamoDotum, UnJamoBatang \
- UnVada \
- UnPilgia: script \

%define common_desc_ko \
은글꼴 시리즈는 HLaTex개발자이신 은광희님이 1998년에 개발한 폰트입니다. \
2003년에 박원규님이 FontForge를 이용하여 트루타입폰트로 변환했습니다. \
은글꼴은 가장 일반적인 글꼴들입니다. \
\
Extra 모음 \
- 은펜, 은펜흘림: script \
- 은타자: typewriter style \
- 은봄: decorative \
- 은신문 \
- 은옛글: old Korean printing style \
- 은자모소라, 은자모노벨, 은자모돋음, 은자모바탕 \
- 은바다 \
- 은필기a: script \ 

Name:        fonts-ttf-un-extra
Version:     1.0.2
Release:     alt3_0.14.080608
Summary:     Un Extra family of Korean TrueType fonts
Summary(ko): 한글 은글꼴 Extra 모음

Group:     System/Fonts/True type
License:   GPLv2
URL:       http://kldp.net/projects/unfonts/
Source0:   http://kldp.net/frs/download.php/4696/%{archivename}-%{version}-%{alphatag}.tar.gz
Source1:   %{oldname}-bom-fontconfig.conf
Source2:   %{oldname}-jamobatang-fontconfig.conf
Source3:   %{oldname}-jamodotum-fontconfig.conf
Source4:   %{oldname}-jamonovel-fontconfig.conf
Source5:   %{oldname}-jamosora-fontconfig.conf
Source6:   %{oldname}-pen-fontconfig.conf
Source7:   %{oldname}-penheulim-fontconfig.conf
Source8:   %{oldname}-pilgia-fontconfig.conf
Source9:   %{oldname}-shinmun-fontconfig.conf
Source10:  %{oldname}-taza-fontconfig.conf
Source11:  %{oldname}-vada-fontconfig.conf
Source12:  %{oldname}-yetgul-fontconfig.conf

BuildArch: noarch
BuildRequires: fontpackages-devel
Source44: import.info


%package common
Group: System/Fonts/True type
Summary:     Common files for the Un Extra font set

%files common
%doc COPYING README


%define un_subpkg() \
%package -n fonts-ttf-%{fontname}-%1 \
Summary:     Un Extra fonts - %(echo %2) \
Summary(ko): 한글 은글꼴 Extra 모음 - %(echo %3) \
Group:       System/Fonts/True type \
Requires:    %{name}-common = %{version}-%{release} \
\
\

%un_subpkg bom UnBom 은봄
%un_subpkg jamobatang UnJamoBatang 은자모바탕
%un_subpkg jamodotum UnJamoDotum 은자모돋음
%un_subpkg jamonovel UnJamoNovel 은자모노벨
%un_subpkg jamosora UnJamoSora 은자모소라
%un_subpkg pen UnPen 은펜
%un_subpkg penheulim UnPenheulim 은펜흘림
%un_subpkg pilgia UnPilgia 은필기a
%un_subpkg shinmun UnShinmun 은신문
%un_subpkg taza UnTaza 은타자
%un_subpkg vada UnVada 은바다
%un_subpkg yetgul UnYetgul 은옛글

%description
%common_desc_en

%description -l ko
%common_desc_ko

%description common
%common_desc_en

This package consists of files used by other %{oldname} packages.

%description -n fonts-ttf-un-extra-bom
%common_desc_en

This package includes UnBom, a decorative font.

%description -l ko -n fonts-ttf-un-extra-bom
%common_desc_ko

이 패키지에는 은봄글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-jamobatang
%common_desc_en

This package includes the UnJamoBatang font.

%description -l ko -n fonts-ttf-un-extra-jamobatang
%common_desc_ko

이 패키지에는 은자모바탕글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-jamodotum
%common_desc_en

This package includes the UNJamoDotum font.

%description -l ko -n fonts-ttf-un-extra-jamodotum
%common_desc_ko

이 패키지에는 은자모돋음글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-jamonovel
%common_desc_en

This package includes the UNJamoNovel font.

%description -l ko -n fonts-ttf-un-extra-jamonovel
%common_desc_ko
 
이 패키지에는 은자모노벨글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-jamosora
%common_desc_en

This package includes the UNJamoSora font.

%description -l ko -n fonts-ttf-un-extra-jamosora
%common_desc_ko

이 패키지에는 은자모소라글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-pen
%common_desc_en

This package includes UnPen, a script font.

%description -l ko -n fonts-ttf-un-extra-pen
%common_desc_ko

이 패키지에는 은펜글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-penheulim
%common_desc_en

This package includes UnPenheulim, a script font.

%description -l ko -n fonts-ttf-un-extra-penheulim
%common_desc_ko

이 패키지에는 은펜흘림글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-pilgia
%common_desc_en

This package includes UnPilgia, a script font.

%description -l ko -n fonts-ttf-un-extra-pilgia
%common_desc_ko

이 패키지에는 은필기a글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-shinmun
%common_desc_en

This package includes the UnShinmun font.

%description -l ko -n fonts-ttf-un-extra-shinmun
%common_desc_ko

이 패키지에는 은신문글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-taza
%common_desc_en

This package includes UnTaza, a typewriter font.

%description -l ko -n fonts-ttf-un-extra-taza
%common_desc_ko

이 패키지에는 은타자글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-vada
%common_desc_en

This package includes the UnVada font.

%description -l ko -n fonts-ttf-un-extra-vada
%common_desc_ko

이 패키지에는 은바다글꼴이 포함되어 있습니다.

%description -n fonts-ttf-un-extra-yetgul
%common_desc_en

This package includes UnYetgul, an old Korean printing font.

%description -l ko -n fonts-ttf-un-extra-yetgul
%common_desc_ko

이 패키지에는 은옛글글꼴이 포함되어 있습니다.


%files -n fonts-ttf-un-extra-bom
%{_fontconfig_templatedir}/%{fontconf}-bom.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-bom.conf
%{_fontbasedir}/*/%{_fontstem}/UnBom.ttf
%files -n fonts-ttf-un-extra-jamobatang
%{_fontconfig_templatedir}/%{fontconf}-jamobatang.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-jamobatang.conf
%{_fontbasedir}/*/%{_fontstem}/UnJamoBatang.ttf
%files -n fonts-ttf-un-extra-jamodotum
%{_fontconfig_templatedir}/%{fontconf}-jamodotum.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-jamodotum.conf
%{_fontbasedir}/*/%{_fontstem}/UnJamoDotum.ttf
%files -n fonts-ttf-un-extra-jamonovel
%{_fontconfig_templatedir}/%{fontconf}-jamonovel.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-jamonovel.conf
%{_fontbasedir}/*/%{_fontstem}/UnJamoNovel.ttf
%files -n fonts-ttf-un-extra-jamosora
%{_fontconfig_templatedir}/%{fontconf}-jamosora.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-jamosora.conf
%{_fontbasedir}/*/%{_fontstem}/UnJamoSora.ttf
%files -n fonts-ttf-un-extra-pen
%{_fontconfig_templatedir}/%{fontconf}-pen.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pen.conf
%{_fontbasedir}/*/%{_fontstem}/UnPen.ttf
%files -n fonts-ttf-un-extra-penheulim
%{_fontconfig_templatedir}/%{fontconf}-penheulim.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-penheulim.conf
%{_fontbasedir}/*/%{_fontstem}/UnPenheulim.ttf
%files -n fonts-ttf-un-extra-pilgia
%{_fontconfig_templatedir}/%{fontconf}-pilgia.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pilgia.conf
%{_fontbasedir}/*/%{_fontstem}/UnPilgia.ttf
%files -n fonts-ttf-un-extra-shinmun
%{_fontconfig_templatedir}/%{fontconf}-shinmun.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-shinmun.conf
%{_fontbasedir}/*/%{_fontstem}/UnShinmun.ttf
%files -n fonts-ttf-un-extra-taza
%{_fontconfig_templatedir}/%{fontconf}-taza.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-taza.conf
%{_fontbasedir}/*/%{_fontstem}/UnTaza.ttf
%files -n fonts-ttf-un-extra-vada
%{_fontconfig_templatedir}/%{fontconf}-vada.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-vada.conf
%{_fontbasedir}/*/%{_fontstem}/UnVada.ttf
%files -n fonts-ttf-un-extra-yetgul
%{_fontconfig_templatedir}/%{fontconf}-yetgul.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-yetgul.conf
%{_fontbasedir}/*/%{_fontstem}/UnYetgul.ttf


%prep
%setup -q -n un-fonts


%build


%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bom.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-jamobatang.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-jamodotum.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-jamonovel.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-jamosora.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-penheulim.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pilgia.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-shinmun.conf
install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-taza.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-vada.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-yetgul.conf

for fconf in %{fontconf}-bom.conf \
    %{fontconf}-jamobatang.conf \
    %{fontconf}-jamodotum.conf \
    %{fontconf}-jamonovel.conf \
    %{fontconf}-jamosora.conf \
    %{fontconf}-pen.conf \
    %{fontconf}-penheulim.conf \
    %{fontconf}-pilgia.conf \
    %{fontconf}-shinmun.conf \
    %{fontconf}-taza.conf \
    %{fontconf}-vada.conf \
    %{fontconf}-yetgul.conf ; do
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


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.14.080608
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.14.080608
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.13.080608
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_0.13.080608
- initial release by fcimport

