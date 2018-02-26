# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname dustin-dustismo-fonts
%define fontname dustin-dustismo
%define fontconf 63-%{fontname}

%define common_desc General purpose fonts by Dustin Norlander available in \
serif and sans-serif versions. The fonts cover all European Latin characters.

Name:          fonts-ttf-dustin-dustismo
Version:       20030318
Release:       alt3_7
Summary:       General purpose sans-serif font with bold, italic and bold-italic variations

Group:         System/Fonts/True type
License:       GPLv2+
URL:           http://www.dustismo.com
# Actual download URL
#URL:           http://ftp.de.debian.org/debian/pool/main/t/ttf-dustin/ttf-dustin_20030517.orig.tar.gz 
Source0:       Dustismo.zip
Source1:       %{oldname}-sans-fontconfig.conf
Source2:       %{oldname}-roman-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
%common_desc

%package common
Summary:       Common files for %{oldname}
Group:         System/Fonts/True type

%description common
%common_desc

This package consists of files used by other %{oldname} packages.

%package -n fonts-ttf-dustin-dustismo-sans
Summary:       General purpos sans-serif fonts
Group:         System/Fonts/True type
Requires:      %{name}-common = %{version}-%{release}
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

%package -n fonts-ttf-dustin-dustismo-roman
Summary:       General purpose serif font
Group:         System/Fonts/True type
Requires:      %{name}-common = %{version}-%{release}
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

%prep
%setup -q -c %{oldname}
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
%doc license.txt

%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20030318-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20030318-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20030318-alt2_6
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 20030318-alt1_6
- initial release by fcimport

