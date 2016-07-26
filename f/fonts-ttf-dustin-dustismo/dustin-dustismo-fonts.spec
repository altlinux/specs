Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname dustin-dustismo-fonts
%global fontname dustin-dustismo
%global fontconf 63-%{fontname}

%global common_desc General purpose fonts by Dustin Norlander available in \
serif and sans-serif versions. The fonts cover all European Latin characters.

Name:          fonts-ttf-dustin-dustismo
Version:       20030318
Release:       alt3_14
Summary:       General purpose sans-serif font with bold, italic and bold-italic variations

License:       GPLv2+
URL:           http://www.dustismo.com
# Actual download URL
#URL:           http://ftp.de.debian.org/debian/pool/main/t/ttf-dustin/ttf-dustin_20030517.orig.tar.gz 
Source0:       Dustismo.zip
Source1:       %{oldname}-sans-fontconfig.conf
Source2:       %{oldname}-roman-fontconfig.conf
Source3:       %{fontname}.metainfo.xml
Source4:       %{fontname}-sans.metainfo.xml
Source5:       %{fontname}-roman.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-dustin-dustismo-common
Group: System/Fonts/True type
Summary:       Common files for %{oldname}

%description -n fonts-ttf-dustin-dustismo-common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-ttf-dustin-dustismo-sans
Group: System/Fonts/True type
Summary:       General purpos sans-serif fonts
Requires:      %{name}-common = %{version}
Provides:      %{oldname} = 20030318-3
Obsoletes:     %{oldname} < 20030318-3

%description -n fonts-ttf-dustin-dustismo-sans
%common_desc

General purpose sans-serif font with bold, italic and bold-italic variations

%files -n fonts-ttf-dustin-dustismo-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/dustismo_bold_italic.ttf
%{_fontbasedir}/*/%{_fontstem}/dustismo_bold.ttf
%{_fontbasedir}/*/%{_fontstem}/dustismo_italic.ttf
%{_fontbasedir}/*/%{_fontstem}/Dustismo.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml

%package -n fonts-ttf-dustin-dustismo-roman
Group: System/Fonts/True type
Summary:       General purpose serif font
Requires:      %{name}-common = %{version}
Provides:      %{oldname}-roman = 20030318-3
Obsoletes:     %{oldname}-roman < 20030318-3

%description -n fonts-ttf-dustin-dustismo-roman
%common_desc

General purpose serif font with bold, italic and bold-italic variations

%files -n fonts-ttf-dustin-dustismo-roman
%{_fontconfig_templatedir}/%{fontconf}-roman.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-roman.conf
%{_fontbasedir}/*/%{_fontstem}/Dustismo_Roman_Bold.ttf
%{_fontbasedir}/*/%{_fontstem}/Dustismo_Roman.ttf
%{_fontbasedir}/*/%{_fontstem}/Dustismo_Roman_Italic_Bold.ttf
%{_fontbasedir}/*/%{_fontstem}/Dustismo_Roman_Italic.ttf
%{_datadir}/appdata/%{fontname}-roman.metainfo.xml

%prep
%setup -n %{oldname}-%{version} -q -c %{oldname}
sed -i 's/\r//' license.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-roman.conf

for fontconf in %{fontconf}-sans.conf %{fontconf}-roman.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-roman.metainfo.xml
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

%files -n fonts-ttf-dustin-dustismo-common
%doc license.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_13
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_12
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20030318-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20030318-alt2_6
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 20030318-alt1_6
- initial release by fcimport

