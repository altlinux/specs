# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname adf-gillius-fonts
%global fontname adf-gillius
%global fontconf 69-%{fontname}

%global common_desc \
The Gillius family from the Arkandis Digital Foundry is a set of sans-serif \
typefaces intended as an alternative to Gill Sans. Its two widths, regular and \
condensed, both feature a roman and an italic, and each includes a regular and \
bold weight.

Name:		fonts-otf-adf-gillius
Version:	1.008
Release:	alt3_5
Summary:	Gillius ADF sans-serif typeface family

Group:		System/Fonts/True type
License:	GPLv2+ with exceptions
URL:		http://arkandis.tuxfamily.org/adffonts.html
Source0:	http://arkandis.tuxfamily.org/fonts/Gillius-Collection.zip
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}-2-fontconfig.conf

BuildArch:	noarch
BuildRequires:	fontpackages-devel

Requires:	%{name}-common = %{version}-%{release}
Source44: import.info
%description
%common_desc

This is the base variant.

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/GilliusADF-*.otf


%package common
Group: System/Fonts/True type
Summary:	Common files of %{fontname}

%description common
%common_desc

This package consists of files used by other %{fontname} packages


%package -n fonts-ttf-adf-gillius-2
Group: System/Fonts/True type
Summary:	Gillius ADF No2 sans-serif typeface family
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-adf-gillius-2
%common_desc

A slightly rounder variant, which features the same set of weights,
widths, and slopes. 

%files -n fonts-ttf-adf-gillius-2
%{_fontconfig_templatedir}/%{fontconf}-2.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-2.conf
%{_fontbasedir}/*/%{_fontstem}/GilliusADFNo2-*.otf

%prep
%setup -q -n Gillius-Collection
for file in NOTICE OTF/COPYING; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
			%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-2.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-2.conf \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}-2.conf
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
%doc NOTICE OTF/COPYING

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.008-alt2_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.008-alt2_4
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.008-alt1_4
- initial release by fcimport

