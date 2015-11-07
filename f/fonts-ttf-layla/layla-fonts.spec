Group: System/Fonts/True type
%define oldname layla-fonts
%global fontname layla
%global fontconf 67-%{fontname}
Name:		fonts-ttf-layla
Version:	1.6
Release:	alt1_2
Summary:	A collection of traditional Arabic fonts
License:	OFL
URL:		http://sites.google.com/site/mohammedisam2000/home/projects
Source0:	http://sites.google.com/site/mohammedisam2000/home/projects/%{oldname}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info


%description
This package is a collection of traditional Arabic fonts (including Thuluth,
Koufi, Ruqaa..) in addition to other newly designed fonts. The aim is to 
provide all the basic fonts an Arabic user will need under X window system.
More fonts will be added regularly to the collection to make it the only font
source an Arabic user will need to install under the X window system

%package -n fonts-ttf-layla-diwani
Group: System/Fonts/True type
Summary: Arabic Diwani font - Part of the Layla fonts collection
Requires: fonts-ttf-layla-common = %{version}-%{release}
%description -n fonts-ttf-layla-diwani
Arabic Diwani font - Part of the Layla fonts collection

%package -n fonts-ttf-layla-koufi
Group: System/Fonts/True type
Summary: Arabic Koufi font - Part of the Layla fonts collection
Requires: fonts-ttf-layla-common = %{version}-%{release}
%description -n fonts-ttf-layla-koufi
Arabic Koufi font - Part of the Layla fonts collection

%package -n fonts-ttf-layla-thuluth
Group: System/Fonts/True type
Summary: Arabic Thuluth font - Part of the Layla fonts collection
Requires: fonts-ttf-layla-common = %{version}-%{release}
%description -n fonts-ttf-layla-thuluth
Arabic Thuluth font - Part of the Layla fonts collection

%package -n fonts-ttf-layla-boxer
Group: System/Fonts/True type
Summary: Arabic Boxer font - Part of the Layla fonts collection
Requires: fonts-ttf-layla-common = %{version}-%{release}
%description -n fonts-ttf-layla-boxer
Arabic Boxer font - Part of the Layla fonts collection

%package -n fonts-ttf-layla-ruqaa
Group: System/Fonts/True type
Summary: Arabic Ruqaa font - Part of the Layla fonts collection
Requires: fonts-ttf-layla-common = %{version}-%{release}
%description -n fonts-ttf-layla-ruqaa
Arabic Ruqaa font - Part of the Layla fonts collection

%package -n fonts-ttf-layla-basic-arabic
Group: System/Fonts/True type
Summary: Basic Arabic font - Part of the Layla fonts collection
Requires: fonts-ttf-layla-common = %{version}-%{release}
%description -n fonts-ttf-layla-basic-arabic
Basic Arabic font - Part of the Layla fonts collection

%package -n fonts-ttf-layla-arcyarc
Group: System/Fonts/True type
Summary: ArcyArc font - Part of the Layla fonts collection
Requires: fonts-ttf-layla-common = %{version}-%{release}
%description -n fonts-ttf-layla-arcyarc
ArcyArc font - Part of the Layla fonts collection

%package -n fonts-ttf-layla-digital
Group: System/Fonts/True type
Summary: Digital font - Part of the Layla fonts collection
Requires: fonts-ttf-layla-common = %{version}-%{release}
%description -n fonts-ttf-layla-digital
Digital font - Part of the Layla fonts collection

%package -n fonts-ttf-layla-common
Group: System/Fonts/True type
Summary: Common files for the Layla fonts package collection
%description -n fonts-ttf-layla-common
Common files for the Layla fonts package collection

%files -n fonts-ttf-layla-koufi
%{_fontconfig_templatedir}/%{fontconf}-Koufi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-Koufi.conf
%{_fontbasedir}/*/%{_fontstem}/LaylaKoufi*.ttf
%files -n fonts-ttf-layla-thuluth
%{_fontconfig_templatedir}/%{fontconf}-Thuluth.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-Thuluth.conf
%{_fontbasedir}/*/%{_fontstem}/LaylaThuluth*.ttf
%files -n fonts-ttf-layla-boxer
%{_fontconfig_templatedir}/%{fontconf}-Boxer.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-Boxer.conf
%{_fontbasedir}/*/%{_fontstem}/LaylaBoxer*.ttf
%files -n fonts-ttf-layla-ruqaa
%{_fontconfig_templatedir}/%{fontconf}-Ruqaa.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-Ruqaa.conf
%{_fontbasedir}/*/%{_fontstem}/LaylaRuqaa*.ttf
%files -n fonts-ttf-layla-basic-arabic
%{_fontconfig_templatedir}/%{fontconf}-BasicArabic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-BasicArabic.conf
%{_fontbasedir}/*/%{_fontstem}/LaylaBasicArabic*.ttf
%files -n fonts-ttf-layla-diwani
%{_fontconfig_templatedir}/%{fontconf}-Diwani.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-Diwani.conf
%{_fontbasedir}/*/%{_fontstem}/LaylaDiwani*.ttf
%files -n fonts-ttf-layla-arcyarc
%{_fontconfig_templatedir}/%{fontconf}-ArcyArc.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-ArcyArc.conf
%{_fontbasedir}/*/%{_fontstem}/LaylaArcyArc*.ttf
%files -n fonts-ttf-layla-digital
%{_fontconfig_templatedir}/%{fontconf}-Digital.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-Digital.conf
%{_fontbasedir}/*/%{_fontstem}/LaylaDigital*.ttf

%prep
%setup -n %{oldname}-%{version} -q

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
			%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p confs/%{fontconf}-Koufi.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Koufi.conf
install -m 0644 -p confs/%{fontconf}-Thuluth.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Thuluth.conf
install -m 0644 -p confs/%{fontconf}-Boxer.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Boxer.conf
install -m 0644 -p confs/%{fontconf}-Ruqaa.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Ruqaa.conf
install -m 0644 -p confs/%{fontconf}-BasicArabic.conf \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-BasicArabic.conf
install -m 0644 -p confs/%{fontconf}-Diwani.conf \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Diwani.conf
install -m 0644 -p confs/%{fontconf}-ArcyArc.conf \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ArcyArc.conf
install -m 0644 -p confs/%{fontconf}-Digital.conf \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-Digital.conf

for fconf in %{fontconf}-Koufi.conf \
		%{fontconf}-Diwani.conf \
		%{fontconf}-ArcyArc.conf \
		%{fontconf}-Digital.conf \
		%{fontconf}-Thuluth.conf \
		%{fontconf}-Boxer.conf \
		%{fontconf}-Ruqaa.conf \
		%{fontconf}-BasicArabic.conf ; do
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


%files -n fonts-ttf-layla-common
%doc README FONTLOG.txt ChangeLog OFL.txt OFL-FAQ.txt Authors


%changelog
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_2
- new version

