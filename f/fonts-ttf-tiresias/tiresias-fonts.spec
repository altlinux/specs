# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname tiresias-fonts
%define fontname tiresias
%define fontconf 60-%{fontname}.conf

%define common_desc \
The Tiresias family of fonts has been designed for use in multiple environments \
to help improve legibility, especially for individuals with visual impairment. \
It includes specialized fonts for information labels, control labels (for key \
tops), large print publications, computer systems, television subtitling, and \
signs.

Name:		fonts-ttf-tiresias
Summary: 	Low vision fonts
Version:	1.0
Release:	alt3_10
# Font exception
License:	GPLv3+ with exceptions
Group:		System/Fonts/True type
Source0:	http://www.tiresias.org/fonts/infofont.zip
Source1:	http://www.tiresias.org/fonts/keyfont.zip
Source2:	http://www.tiresias.org/fonts/lpfont.zip
Source3:	http://www.tiresias.org/fonts/pcfont.zip
Source4:	http://www.tiresias.org/fonts/signfont.zip
Source5:	%{oldname}-info-fontconfig.conf
Source6:	%{oldname}-info-z-fontconfig.conf
Source7:	%{oldname}-key-v2-fontconfig.conf
Source8:	%{oldname}-lp-fontconfig.conf
Source9:	%{oldname}-pc-fontconfig.conf
Source10:	%{oldname}-pc-z-fontconfig.conf
Source11:	%{oldname}-sign-fontconfig.conf
Source12:	%{oldname}-sign-z-fontconfig.conf
URL:		http://www.tiresias.org/fonts/
BuildRequires:	fontpackages-devel
BuildArch:	noarch
Source44: import.info

%description
%common_desc

%package common
Summary:	Common files for Tiresias fonts (documentation...)
Group:		System/Fonts/True type

%description common
%common_desc

This package consists of files used by other Tiresias packages.

%package -n fonts-ttf-tiresias-info
Summary:	Specialized fonts for info terminals for the visually impaired
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-tiresias-info
%common_desc

The Infofont family is specialized for use in informational labels on public 
terminals such as ATMs using large characters. The only	difference between the
Infofont and the Infofont Z families is whether the zero is crossed out or not.
In the Infofont family, the zero is _not_ crossed out, which may lead to some
confusion.

%files -n fonts-ttf-tiresias-info
%{_fontconfig_templatedir}/%{fontconf}-infofont.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-infofont.conf
%{_fontbasedir}/*/%{_fontstem}/"Tiresias*Infofont*.ttf"

%package -n fonts-ttf-tiresias-info-z
Summary:	Specialized fonts for info terminals for the visually impaired
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-tiresias-info-z
%common_desc

The Infofont Z family is specialized for use in informational labels on public
terminals such as ATMs using large characters. The only difference between the
Infofont Z and the Infofont families is whether the zero is crossed out or not.
In the Infofont	Z family, the zero is crossed out.

%files -n fonts-ttf-tiresias-info-z
%{_fontconfig_templatedir}/%{fontconf}-infofont-z.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-infofont-z.conf
%{_fontbasedir}/*/%{_fontstem}/"TIRESIAS*INFOFONTZ*.ttf"

%package -n fonts-ttf-tiresias-key-v2
Summary:	Specialized fonts for labeling keycaps for the visually impaired
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-tiresias-key-v2
%common_desc

The Keyfont V2 family is specialized for use in labeling keycaps.

%files -n fonts-ttf-tiresias-key-v2
%{_fontconfig_templatedir}/%{fontconf}-keyfont-v2.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-keyfont-v2.conf
%{_fontbasedir}/*/%{_fontstem}/TIREKV__.ttf

%package -n fonts-ttf-tiresias-lp
Summary:	Specialized font for large print publications
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-tiresias-lp
%common_desc

The LPfont family is specialized for use in large print publications.

%files -n fonts-ttf-tiresias-lp
%{_fontconfig_templatedir}/%{fontconf}-lpfont.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-lpfont.conf
%{_fontbasedir}/*/%{_fontstem}/"Tiresias*LPfont*.ttf"

%package -n fonts-ttf-tiresias-pc
Summary:	Specialized fonts for use on PCs for the visually impaired
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-tiresias-pc
%common_desc

The PCfont family is specialized for people with poor vision to use on PC 
screens using large characters. The only difference between the PCfont and 
the PCfont Z families is whether the zero is crossed out or not. In the 
PCfont family, the zero is _not_ crossed out, which may lead to some
confusion.

%files -n fonts-ttf-tiresias-pc
%{_fontconfig_templatedir}/%{fontconf}-pcfont.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pcfont.conf
%{_fontbasedir}/*/%{_fontstem}/"Tiresias*PCfont*.ttf"

%package -n fonts-ttf-tiresias-pc-z
Summary:	Specialized fonts for use on PCs for the visually impaired
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-tiresias-pc-z
%common_desc

The PCfont family is specialized for people with poor vision to use on PC
screens using large characters.	The only difference between the PCfont and 
the PCfont Z families is whether the zero is crossed out or not. In the
PCfont Z family, the zero is crossed out.

%files -n fonts-ttf-tiresias-pc-z
%{_fontconfig_templatedir}/%{fontconf}-pcfont-z.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pcfont-z.conf
%{_fontbasedir}/*/%{_fontstem}/"TIRESIAS*PCFONTZ*.ttf"

%package -n fonts-ttf-tiresias-sign
Summary:	Specialized fonts for preparing signs for the visually impaired
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-tiresias-sign
%common_desc

The Signfont family is specialized for preparing signs for the visually 
impaired, using large characters. The only difference between the Signfont and 
the Signfont Z families is whether the zero is crossed out or not. In the
Signfont family, the zero is _not_ crossed out, which may lead to some
confusion.

%files -n fonts-ttf-tiresias-sign
%{_fontconfig_templatedir}/%{fontconf}-signfont.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-signfont.conf
%{_fontbasedir}/*/%{_fontstem}/"Tiresias*Signfont*.ttf"

%package -n fonts-ttf-tiresias-sign-z
Summary:	Specialized fonts for preparing signs for the visually impaired
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-tiresias-sign-z
%common_desc

The Signfont family is specialized for preparing signs for the visually 
impaired, using	large characters. The only difference between the Signfont and 
the Signfont Z families is whether the zero is crossed out or not. In the 
Signfont Z family, the zero is crossed out.

%files -n fonts-ttf-tiresias-sign-z
%{_fontconfig_templatedir}/%{fontconf}-signfont-z.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-signfont-z.conf
%{_fontbasedir}/*/%{_fontstem}/"TIRESIAS*SIGNFONTZ*.ttf"

%prep
%setup -q -c -n %{oldname}
%{__unzip} -qqo %{SOURCE1}
%{__unzip} -qqo %{SOURCE2}
%{__unzip} -qqo %{SOURCE3}
%{__unzip} -qqo %{SOURCE4}
for f in *.TTF; do 
	newname=`echo "$f"|sed -e 's/.TTF/.ttf/'`;
	mv "$f" "$newname"; 
done;
# correct end-of-line encoding
sed -i 's/\r//' COPYING/gpl.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-infofont.conf
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-infofont-z.conf
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-keyfont-v2.conf
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lpfont.conf
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pcfont.conf
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pcfont-z.conf
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-signfont.conf
install -m 0644 -p %{SOURCE12} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-signfont-z.conf

for fontconf in %{fontconf}-infofont.conf %{fontconf}-infofont-z.conf %{fontconf}-keyfont-v2.conf %{fontconf}-lpfont.conf\
		%{fontconf}-pcfont.conf %{fontconf}-pcfont-z.conf %{fontconf}-signfont.conf %{fontconf}-signfont-z.conf; do
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
%doc COPYING/copying.doc COPYING/gpl.txt
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_10
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9
- initial release by fcimport

