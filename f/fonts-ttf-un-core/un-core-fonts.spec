Group: System/Fonts/True type
%define oldname un-core-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.2
%global fontname un-core
%global fontconf 67-%{fontname}

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

%global common_desc_ko \
i'.e..e.. i.'e..i..e.. HLaTexe.'e.'i..i'.i.. i'.e..i'.e.'i'. 1998e..i-. e.'e.'i.' i..i..i..e..e... \
2003e..i-. e..i..e.'e.'i'. FontForgee.. i'.i..i.'i-. i..e..i..i..i..i..e.' e..i''i..i..e..e... \
i'.e..e..i'. e..i.. i'.e.'i..i'. e..e..e..i..e..e... \
\
Core e..i'.: \
- i'.e..i..: serif \
- i'.e..e.'e..: fantasy \
- i'.e..i'.: sans-serif \
- i'.e..e.'i..: sans-serif style \
- i'.e..i.': cursive, brush-stroke \
- i'.i..e..: script

Name:           fonts-ttf-un-core
Version:        1.0.2
Release:        alt3_0.31.%{alphatag}
Summary:        Un Core family of Korean TrueType fonts
Summary(ko):    한글 은글꼴 Core 모음

License:        GPLv2
URL:            http://kldp.net/projects/unfonts/
Source0:        http://kldp.net/frs/download.php/4695/%{archivename}.tar.gz
Source1:        %{oldname}-batang-fontconfig.conf
Source2:        %{oldname}-dinaru-fontconfig.conf
Source3:        %{oldname}-dotum-fontconfig.conf
Source4:        %{oldname}-graphic-fontconfig.conf
Source5:        %{oldname}-gungseo-fontconfig.conf
Source6:        %{oldname}-pilgi-fontconfig.conf
Source7:        %{fontname}-batang.metainfo.xml
Source8:        %{fontname}-dinaru.metainfo.xml
Source9:        %{fontname}-dotum.metainfo.xml
Source10:       %{fontname}-graphic.metainfo.xml
Source11:       %{fontname}.metainfo.xml
Source12:       %{fontname}-gungseo.metainfo.xml
Source13:       %{fontname}-pilgi.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%package -n fonts-ttf-un-core-common
Group: System/Fonts/True type
Summary:        Common files of Un Core fonts

%description -n fonts-ttf-un-core-common
%common_desc

This package consists of files used by other %{oldname} packages.

# un_subpkg 1:name 2:Name 3:Hangul [4:obsolete] [5:obsolete]
%global un_subpkg() \
%package -n fonts-ttf-%{fontname}-%1 \
Summary:        Un Core fonts - %(echo %2) \
Summary(ko):    i.'e.. i'.e..e.. Core e..i'. - %(echo %3) \
Group:          System/Fonts/True type \
Requires:       %{name}-common = %{version}-%{release} \
\
\

%un_subpkg batang UnBatang i'.e..i.. bold
%un_subpkg dinaru UnDinaru i'.e..e.'e.. bold light
%un_subpkg dotum UnDotum i'.e..i'. bold
%un_subpkg graphic UnGraphic i'.e..e.'i.. bold
%un_subpkg gungseo UnGungseo i'.e..i.'
%un_subpkg pilgi UnPilgi i'.i..e.. bold


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
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/UnBatang.ttf
%{_fontbasedir}/*/%{_fontstem}/UnBatangBold.ttf
%{_datadir}/appdata/%{fontname}-batang.metainfo.xml
%files -n fonts-ttf-un-core-dinaru
%{_fontconfig_templatedir}/%{fontconf}-dinaru.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-dinaru.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/UnDinaru.ttf
%{_fontbasedir}/*/%{_fontstem}/UnDinaruLight.ttf
%{_fontbasedir}/*/%{_fontstem}/UnDinaruBold.ttf
%{_datadir}/appdata/%{fontname}-dinaru.metainfo.xml
%files -n fonts-ttf-un-core-dotum
%{_fontconfig_templatedir}/%{fontconf}-dotum.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-dotum.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/UnDotum.ttf
%{_fontbasedir}/*/%{_fontstem}/UnDotumBold.ttf
%{_datadir}/appdata/%{fontname}-dotum.metainfo.xml
%files -n fonts-ttf-un-core-graphic
%{_fontconfig_templatedir}/%{fontconf}-graphic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-graphic.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/UnGraphic.ttf
%{_fontbasedir}/*/%{_fontstem}/UnGraphicBold.ttf
%{_datadir}/appdata/%{fontname}-graphic.metainfo.xml
%files -n fonts-ttf-un-core-gungseo
%{_fontconfig_templatedir}/%{fontconf}-gungseo.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gungseo.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/UnGungseo.ttf
%{_datadir}/appdata/%{fontname}-gungseo.metainfo.xml
%files -n fonts-ttf-un-core-pilgi
%{_fontconfig_templatedir}/%{fontconf}-pilgi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pilgi.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/UnPilgi.ttf
%{_fontbasedir}/*/%{_fontstem}/UnPilgiBold.ttf
%{_datadir}/appdata/%{fontname}-pilgi.metainfo.xml

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

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE7} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-batang.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-dinaru.metainfo.xml
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-dotum.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-graphic.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-gungseo.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-pilgi.metainfo.xml
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

%files -n fonts-ttf-un-core-common
%doc README
%doc --no-dereference COPYING
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.31.080608
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.30.080608
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.24.080608
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.23.080608
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.21.080608
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.20.080608
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.19.080608
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_0.18.080608
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.18.080608
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.16.080608
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_0.16.080608
- initial release by fcimport

