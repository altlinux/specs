%define oldname samyak-fonts
%define	fontname	samyak
%global fontconf	67-%{fontname}

# Common description
%define common_desc \
The Samyak package contains fonts for the display of \
Scripts Devanagari, Gujarati, Malayalam, Oriya and Tamil

Name:	 fonts-ttf-samyak
Version:	1.2.2
Release:	alt3_6
Summary:	Free Indian truetype/opentype fonts
Group:	System/Fonts/True type
License:	GPLv3+ with exceptions
URL:	http://sarovar.org/projects/samyak/
# Source0: http://sarovar.org/frs/?group_id=461&release_id=821
Source:	samyak-fonts-%{version}.tar.gz
Source1: 66-samyak-devanagari.conf
Source2: 67-samyak-tamil.conf
Source3: 68-samyak-malayalam.conf
Source4: 67-samyak-gujarati.conf
Source5: 67-samyak-oriya.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires: fontforge >= 20080429
Source44: import.info

%description
%common_desc

%package common
Summary:  Common files for samyak-fonts
Group:	System/Fonts/True type
Provides: %{fontname}-common-fonts = %{version}-%{release}
Obsoletes: %{fontname}-common-fonts < 1.2.1-4
%description common
%common_desc

%package -n fonts-ttf-samyak-devanagari
Summary: Open Type Fonts for Devanagari script
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{oldname}-devanagari = %{version}-%{release}
Obsoletes: %{oldname}-devanagari < 1.2.1-3
%description -n fonts-ttf-samyak-devanagari
This package contains truetype/opentype font for the display of \
Scripts Devanagari.

%files -n fonts-ttf-samyak-devanagari
%{_fontconfig_templatedir}/66-samyak-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/66-samyak-devanagari.conf
%{_fontbasedir}/*/%{_fontstem}/Samyak-Devanagari.ttf

%package -n fonts-ttf-samyak-tamil
Summary: Open Type Fonts for Tamil script
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{oldname}-tamil = %{version}-%{release}
Obsoletes: %{oldname}-tamil < 1.2.1-3
%description -n fonts-ttf-samyak-tamil
This package contains truetype/opentype font for the display of \
Scripts Tamil.

%files -n fonts-ttf-samyak-tamil
%{_fontconfig_templatedir}/%{fontconf}-tamil.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-tamil.conf
%{_fontbasedir}/*/%{_fontstem}/Samyak-Tamil.ttf

%package -n fonts-ttf-samyak-malayalam
Summary: Open Type Fonts for Malayalam script
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{oldname}-malayalam = %{version}-%{release}
Obsoletes: %{oldname}-malayalam < 1.2.1-3
%description -n fonts-ttf-samyak-malayalam
This package contains truetype/opentype font for the display of \
Scripts Malayalam.

%files -n fonts-ttf-samyak-malayalam
%{_fontconfig_templatedir}/68-samyak-malayalam.conf
%config(noreplace) %{_fontconfig_confdir}/68-samyak-malayalam.conf
%{_fontbasedir}/*/%{_fontstem}/Samyak-Malayalam.ttf

%package -n fonts-ttf-samyak-gujarati
Summary: Open Type Fonts for Gujarati script
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{oldname}-gujarati = %{version}-%{release}
Obsoletes: %{oldname}-gujarati < 1.2.1-3
%description -n fonts-ttf-samyak-gujarati
This package contains truetype/opentype font for the display of \
Scripts Gujarati.

%files -n fonts-ttf-samyak-gujarati
%{_fontconfig_templatedir}/%{fontconf}-gujarati.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gujarati.conf
%{_fontbasedir}/*/%{_fontstem}/Samyak-Gujarati.ttf

%package -n fonts-ttf-samyak-oriya
Summary: Open Type Fonts for Oriya script
Group: System/Fonts/True type
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{oldname}-oriya = %{version}-%{release}
Obsoletes: %{oldname}-oriya < 1.2.1-3
%description -n fonts-ttf-samyak-oriya
This package contains truetype/opentype font for the display of \
Scripts Oriya.

%files -n fonts-ttf-samyak-oriya
%{_fontconfig_templatedir}/%{fontconf}-oriya.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-oriya.conf
%{_fontbasedir}/*/%{_fontstem}/Samyak-Oriya.ttf


%prep
%setup -q -n samyak-fonts-%{version}

%build
mkdir -p TTFfiles/
./generate.pe */*.sfd

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p TTFfiles/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/66-samyak-devanagari.conf

install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-tamil.conf

install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/68-samyak-malayalam.conf

install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gujarati.conf

install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-oriya.conf


for fconf in 66-samyak-devanagari.conf \
		%{fontconf}-tamil.conf \
		68-samyak-malayalam.conf \
		%{fontconf}-gujarati.conf \
		%{fontconf}-oriya.conf ; do
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
%doc COPYING README AUTHORS
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt2_5
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_5
- initial release by fcimport

