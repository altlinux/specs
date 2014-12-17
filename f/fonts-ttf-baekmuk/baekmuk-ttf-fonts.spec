Group: System/Fonts/True type
%define oldname baekmuk-ttf-fonts
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name baekmuk-ttf-fonts
%define version 2.2
%global priority    65-2
%global fontname    baekmuk-ttf
%define archivename %{fontname}-%{version}
%define common_desc \
This package provides the free Korean TrueType fonts.

%define gsdir          %{_datadir}/ghostscript/conf.d
%define catalogue      %{_sysconfdir}/X11/fontpath.d

Name:           fonts-ttf-baekmuk
Version:        2.2
Release:        alt2_38
Summary:        Free Korean TrueType fonts

License:        Baekmuk
URL:            http://kldp.net/projects/baekmuk/
Source0:        http://kldp.net/frs/download.php/1429/%{archivename}.tar.gz
Source1:        FAPIcidfmap.ko
Source2:        cidfmap.ko
Source3:        baekmuk-ttf-batang.conf
Source4:        baekmuk-ttf-dotum.conf
Source5:        baekmuk-ttf-gulim.conf
Source6:        baekmuk-ttf-hline.conf
Source7:        %{fontname}-batang.metainfo.xml
Source8:        %{fontname}-dotum.metainfo.xml
Source9:        %{fontname}-gulim.metainfo.xml
Source10:       %{fontname}-hline.metainfo.xml
Source11:       %{fontname}.metainfo.xml

Provides:       fonts-ttf-korean = %{version}-%{release}

BuildArch:      noarch
BuildRequires:  fontpackages-devel >= 1.13 xorg-x11-font-utils
BuildRequires:  ttmkfdir >= 3.0.6
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-baekmuk-batang
Group: System/Fonts/True type
Summary:        Korean Baekmuk TrueType Batang typeface
Provides:       %{oldname}-batang = %{version}-%{release}
Requires:       fonts-ttf-baekmuk-common = %{version}-%{release}

%description -n fonts-ttf-baekmuk-batang
%common_desc

Batang is Korean TrueType font in Serif typeface.

%files -n fonts-ttf-baekmuk-batang
%{_fontconfig_templatedir}/*-%{fontname}-batang*.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-batang*.conf
%{_fontbasedir}/*/%{_fontstem}/batang.ttf
%{_datadir}/appdata/%{fontname}-batang.metainfo.xml

%package -n fonts-ttf-baekmuk-dotum
Group: System/Fonts/True type
Summary:        Korean Baekmuk TrueType Dotum typeface
Provides:       %{oldname}-dotum = %{version}-%{release}
Requires:       fonts-ttf-baekmuk-common = %{version}-%{release}

%description -n fonts-ttf-baekmuk-dotum
%common_desc

Dotum is Korean TrueType font in San-serif typeface.

%files -n fonts-ttf-baekmuk-dotum
%{_fontconfig_templatedir}/*-%{fontname}-dotum*.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-dotum*.conf
%{_fontbasedir}/*/%{_fontstem}/dotum.ttf
%{_datadir}/appdata/%{fontname}-dotum.metainfo.xml

%package -n fonts-ttf-baekmuk-gulim
Group: System/Fonts/True type
Summary:        Korean Baekmuk TrueType Gulim typeface
Provides:       %{oldname}-gulim = %{version}-%{release}
Requires:       fonts-ttf-baekmuk-common = %{version}-%{release}

%description -n fonts-ttf-baekmuk-gulim
%common_desc

Gulim is Korean TrueType font in Monospace typeface.

%files -n fonts-ttf-baekmuk-gulim
%{_fontconfig_templatedir}/*-%{fontname}-gulim*.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-gulim*.conf
%{_fontbasedir}/*/%{_fontstem}/gulim.ttf
%{_datadir}/appdata/%{fontname}-gulim.metainfo.xml

%package -n fonts-ttf-baekmuk-hline
Group: System/Fonts/True type
Summary:        Korean Baekmuk TrueType Headline typeface
Provides:       %{oldname}-hline = %{version}-%{release}
Requires:       fonts-ttf-baekmuk-common = %{version}-%{release}

%description -n fonts-ttf-baekmuk-hline
%common_desc

Headline is Korean TrueType font in Black face.

%files -n fonts-ttf-baekmuk-hline
%{_fontconfig_templatedir}/*-%{fontname}-hline*.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-hline*.conf
%{_fontbasedir}/*/%{_fontstem}/hline.ttf
%{_datadir}/appdata/%{fontname}-hline.metainfo.xml

%package -n fonts-ttf-baekmuk-ghostscript
Group: System/Fonts/True type
Summary:        Ghostscript files for Korean Baekmuk TrueType fonts
Requires: ghostscript-utils ghostscript
Requires:       fonts-ttf-baekmuk-batang = %{version}-%{release}
Requires:       fonts-ttf-baekmuk-dotum = %{version}-%{release}
Requires:       fonts-ttf-baekmuk-gulim = %{version}-%{release}
Requires:       fonts-ttf-baekmuk-hline = %{version}-%{release}

%description -n fonts-ttf-baekmuk-ghostscript
%common_desc

This is ghostscript files for Baekmuk Korean TrueType fonts.

%files -n fonts-ttf-baekmuk-ghostscript
%{gsdir}/cidfmap.ko
%{gsdir}/FAPIcidfmap.ko

%package -n fonts-ttf-baekmuk-common
Group: System/Fonts/True type
Summary:        Common files for Korean Baekmuk TrueType fonts
Provides:       baekmuk-ttf-common-fonts = %{version}-%{release}
Provides:       fonts-korean = %{version}-%{release}
Provides:       ttfonts-ko = %{version}-%{release}

%description -n fonts-ttf-baekmuk-common
%common_desc

This is common files for Baekmuk Korean TrueType fonts.

%files -n fonts-ttf-baekmuk-common
%doc COPYRIGHT COPYRIGHT.ko README
%dir %{_fontbasedir}/*/%{_fontstem}
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/fonts.dir
%verify(not md5 size mtime) %{_fontbasedir}/*/%{_fontstem}/fonts.scale
%verify(not md5 size mtime) %{catalogue}/%{fontname}*
%{_datadir}/appdata/%{fontname}.metainfo.xml

%prep
%setup -q -n %{archivename}

%build
%{nil}

%install
# font
%__install -d -m 0755 %{buildroot}%{_fontdir}
for i in batang dotum gulim hline; do
  %__install -p -m 0644 ttf/$i.ttf %{buildroot}%{_fontdir}
done

# fontconfig conf
%__install -m 0755 -d %{buildroot}%{_fontconfig_templatedir}
%__install -m 0755 -d %{buildroot}%{_fontconfig_confdir}
cd ../
for fconf in %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6}
do
    %__install -m 0644 $fconf %{buildroot}%{_fontconfig_templatedir}/%{priority}-$(basename $fconf)
    %__ln_s %{_fontconfig_templatedir}/%{priority}-$(basename $fconf) \
        %{buildroot}%{_fontconfig_confdir}/%{priority}-$(basename $fconf)
done
cd -

# fonts.{scale,dir}
%{_bindir}/ttmkfdir -d %{buildroot}%{_fontdir} \
  -o %{buildroot}%{_fontdir}/fonts.scale
%{_bindir}/mkfontdir %{buildroot}%{_fontdir}

# ghostscript
%__install -d -m 0755 %{buildroot}%{gsdir}
%__install -p -m 0644 %{SOURCE1} %{buildroot}%{gsdir}/
%__install -p -m 0644 %{SOURCE2} %{buildroot}%{gsdir}/

# catalogue
%__install -d -m 0755 %{buildroot}%{catalogue}
%__ln_s %{_fontdir} %{buildroot}%{catalogue}/%{fontname}

# convert Korean copyright file to utf8
%{_bindir}/iconv -f EUC-KR -t UTF-8 COPYRIGHT.ks > COPYRIGHT.ko

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE7} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-batang.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-dotum.metainfo.xml
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-gulim.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-hline.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
sed -i -e s,%{_datadir}/fonts/%{fontname},%{_datadir}/fonts/ttf/%{fontname},g %buildroot/usr/share/ghostscript/conf.d/*
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

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_38
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_37
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_36
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_35
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_34
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_33
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_32
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_32
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_31
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_30
- initial release by fcimport

